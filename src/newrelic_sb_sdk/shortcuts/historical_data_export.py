__all__ = [
    "logger",
    "MAX_ALLOWED_DATA_POINTS",
    "MAX_ALLOWED_CONCURRENT_EXPORTS",
    "create_historical_data_export",
    "get_all_historical_data_exports",
    "get_historical_data_export",
    "cancel_historical_data_export",
    "can_execute_historical_data_export",
    "perform_historical_data_export",
]


import logging
import time
import warnings
from typing import List, Union

from sgqlc.operation import Operation
from sgqlc.types import Arg, Variable, non_null

from newrelic_sb_sdk.graphql.objects import (
    Account,
    HistoricalDataExportCustomerExportResponse,
)

from ..client import NewRelicGqlClient
from ..graphql import nerdgraph
from ..graphql.enums import HistoricalDataExportStatus
from ..graphql.scalars import ID, Int, Nrql, String
from ..utils.download import download_files
from ..utils.exceptions import NewRelicError
from ..utils.response import raise_response_errors

logger = logging.getLogger("newrelic_sb_sdk")


# Limits imposed by New Relic, check out documentation for more details.
# https://docs.newrelic.com/docs/apis/nerdgraph/examples/nerdgraph-historical-data-export/

MAX_ALLOWED_DATA_POINTS: int = 200000000
MAX_ALLOWED_CONCURRENT_EXPORTS: int = 2


def create_historical_data_export(
    *,
    client: NewRelicGqlClient,
    account: Account,
    nrql_query: Nrql,
) -> HistoricalDataExportCustomerExportResponse:
    operation = Operation(
        nerdgraph.mutation_type,
        variables={
            "accountId": Arg(non_null(Int)),
            "nrql": Arg(Nrql),
        },
    )

    create_export = operation.historical_data_export_create_export(
        account_id=Variable("accountId"),
        nrql=Variable("nrql"),
    )

    create_export.id()
    create_export.nrql()
    create_export.created_at()
    create_export.event_count()
    create_export.event_types()
    create_export.percent_complete()
    create_export.results()
    create_export.status()
    create_export.message()

    create_export.user.email()
    create_export.user.id()
    create_export.user.name()

    create_export.account.id()
    create_export.account.name()

    response = client.execute(
        operation.__to_graphql__(),
        variables={
            "accountId": account.id,
            "nrql": nrql_query,
        },
    )

    raise_response_errors(response=response, account=account)

    data = operation + response.json()

    return data.historical_data_export_create_export


def get_all_historical_data_exports(
    *,
    client: NewRelicGqlClient,
    account: Account,
) -> List[HistoricalDataExportCustomerExportResponse]:
    operation = Operation(
        nerdgraph.query_type,
        variables={
            "accountId": Arg(non_null(Int)),
        },
    )

    exports = operation.actor.account(
        id=Variable("accountId"),
    ).historical_data_export.exports()

    exports.id()
    exports.nrql()
    exports.created_at()
    exports.event_count()
    exports.event_types()
    exports.percent_complete()
    exports.results()
    exports.status()
    exports.message()
    exports.available_until()
    exports.begin_time()
    exports.end_time()

    exports.user.id()
    exports.user.name()
    exports.user.email()

    exports.account.id()
    exports.account.name()

    response = client.execute(
        operation.__to_graphql__(),
        variables={
            "accountId": account.id,
        },
    )

    raise_response_errors(response=response, account=account)

    return (operation + response.json()).actor.account.historical_data_export.exports


def get_historical_data_export(
    *,
    client: NewRelicGqlClient,
    account: Account,
    export_id: ID,
) -> HistoricalDataExportCustomerExportResponse:
    operation = Operation(
        nerdgraph.query_type,
        variables={
            "accountId": Arg(non_null(Int)),
            "exportId": Arg(non_null(ID)),
        },
    )

    export = operation.actor.account(
        id=Variable("accountId"),
    ).historical_data_export.export(
        id=Variable("exportId"),
    )

    export.id()
    export.nrql()
    export.created_at()
    export.event_count()
    export.event_types()
    export.percent_complete()
    export.results()
    export.status()
    export.message()
    export.available_until()
    export.begin_time()
    export.end_time()

    export.user.id()
    export.user.name()
    export.user.email()

    export.account.id()
    export.account.name()

    response = client.execute(
        operation.__to_graphql__(),
        variables={
            "accountId": account.id,
            "exportId": export_id,
        },
    )

    raise_response_errors(response=response, account=account)

    return (operation + response.json()).actor.account.historical_data_export.export


def cancel_historical_data_export(
    *,
    client: NewRelicGqlClient,
    account: Account,
    export_id: str,
) -> HistoricalDataExportCustomerExportResponse:
    operation = Operation(
        nerdgraph.mutation_type,
        variables={
            "accountId": Arg(non_null(Int)),
            "exportId": Arg(non_null(String)),
        },
    )

    cancel_export = operation.historical_data_export_cancel_export(
        account_id=Variable("accountId"),
        id=Variable("exportId"),
    )

    cancel_export.id()
    cancel_export.nrql()
    cancel_export.created_at()
    cancel_export.event_count()
    cancel_export.event_types()
    cancel_export.percent_complete()
    cancel_export.results()
    cancel_export.status()
    cancel_export.message()
    cancel_export.available_until()
    cancel_export.begin_time()
    cancel_export.end_time()

    cancel_export.user.id()
    cancel_export.user.name()
    cancel_export.user.email()

    cancel_export.account.id()
    cancel_export.account.name()

    response = client.execute(
        operation.__to_graphql__(),
        variables={
            "accountId": account.id,
            "exportId": export_id,
        },
    )

    raise_response_errors(response=response, account=account)

    return (operation + response.json()).historical_data_export_cancel_export


def can_execute_historical_data_export(
    *, client: NewRelicGqlClient, account: Account
) -> bool:
    historical_data_exports = get_all_historical_data_exports(
        client=client, account=account
    )

    still_running_statuses = [
        HistoricalDataExportStatus("WAITING"),
        HistoricalDataExportStatus("IN_PROGRESS"),
    ]

    can_execute = (
        len(
            [
                export
                for export in historical_data_exports
                if export.status in still_running_statuses
            ]
        )
        < MAX_ALLOWED_CONCURRENT_EXPORTS
    )

    return can_execute


def _perform_historical_data_export(
    *,
    client: NewRelicGqlClient,
    account: Account,
    nrql_query: Nrql,
    max_retry: Union[int, None] = None,
    max_retries: int = 5,
    retry_delay: int = 30,
) -> HistoricalDataExportCustomerExportResponse:
    # pylint: disable=too-complex,inconsistent-return-statements

    if max_retry is not None:
        warnings.warn(
            "max_retry is deprecated, use max_retries instead",
            DeprecationWarning,
            stacklevel=2,
        )
        max_retries = max_retry

    logger.debug(
        "%d - %s - Getting historical data",
        account.id,
        account.name,
    )
    logger.debug(
        "%d - %s - Extracting data with query: %s",
        account.id,
        account.name,
        nrql_query,
    )

    still_running_statuses = [
        HistoricalDataExportStatus("WAITING"),
        HistoricalDataExportStatus("IN_PROGRESS"),
    ]

    for retry in range(max_retries + 1):
        try:
            if not can_execute_historical_data_export(client=client, account=account):
                logger.debug(
                    "%d - %s - Too many concurrent historical data exports. "
                    "Retrying in %d seconds.",
                    account.id,
                    account.name,
                    (retry + 1) * retry_delay,
                )
                time.sleep((retry + 1) * retry_delay)
                continue

            logger.debug(
                "%d - %s - Creating historical data export with query: %s",
                account.id,
                account.name,
                nrql_query,
            )

            historical_data_export = create_historical_data_export(
                client=client, account=account, nrql_query=nrql_query
            )

            logger.debug(
                "%d - %s - Historical data export created with ID: %s",
                account.id,
                account.name,
                historical_data_export.id,
            )

            while historical_data_export.status != HistoricalDataExportStatus(
                "COMPLETE_SUCCESS"
            ):
                logger.debug(
                    "%d - %s - Historical data export with ID: %s "
                    "is still running. Current status: %s "
                    "(%.2f%%)",
                    account.id,
                    account.name,
                    historical_data_export.id,
                    historical_data_export.status,
                    historical_data_export.percent_complete,
                )

                time.sleep(retry_delay)

                historical_data_export = get_historical_data_export(
                    client=client, account=account, export_id=historical_data_export.id
                )

                if historical_data_export.status not in still_running_statuses:
                    break

            if historical_data_export.status != HistoricalDataExportStatus(
                "COMPLETE_SUCCESS"
            ):
                logger.error(
                    "%d - %s - Failed historical data export with ID: %s "
                    "- Status: %s - Message: '%s'",
                    account.id,
                    account.name,
                    historical_data_export.id,
                    historical_data_export.status,
                    historical_data_export.message,
                )

                raise NewRelicError(
                    f"{account.id} - {account.name} - Failed historical data "
                    f"export with ID: {historical_data_export.id} - Status: "
                    f"{historical_data_export.status} - Message: "
                    f"'{historical_data_export.message}'"
                )

            return historical_data_export
        except Exception as e:  # pylint: disable=broad-except
            if historical_data_export:
                cancel_historical_data_export(
                    client=client, account=account, export_id=historical_data_export.id
                )

            if retry == max_retries - 1:
                raise NewRelicError(
                    f"{account.id} - {account.name} - Failed to extract data: {e}"
                ) from e

            time.sleep(retry_delay)


def perform_historical_data_export(
    *,
    client: NewRelicGqlClient,
    account: Account,
    nrql_query: Nrql,
    base_file_name: str,
):

    export = _perform_historical_data_export(
        client=client, account=account, nrql_query=nrql_query
    )

    if not export.results:
        logger.error(
            "Historical export with ID %s completed successfully but no "
            "results were found",
            export.id,
        )
    else:
        download_files(
            urls=export.results,
            base_file_name=base_file_name,
            file_extension="json.gz",
        )

    cancel_historical_data_export(client=client, account=account, export_id=export.id)
