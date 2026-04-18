__all__ = ["logger", "nrql", "perform_nrql_query"]


import logging
import time
import warnings
from textwrap import dedent
from typing import Union

from sgqlc.operation import Operation
from sgqlc.types import ID, Arg, Int, Variable, list_of, non_null

from newrelic_sb_sdk.graphql.objects import (
    Account,
    CrossAccountNrdbResultContainer,
    NrdbResult,
)

from ..client import NewRelicClient
from ..graphql.scalars import Nrql
from ..utils.exceptions import NewRelicError
from ..utils.response import raise_response_errors

logger = logging.getLogger("newrelic_sb_sdk")


def nrql(query: str) -> Nrql:
    """Format a raw SQL string into a GraphQL-compatible scalar.

    Args:
        query: The string NRQL query.

    Returns:
        A scalar object formatted for the API schema.
    """

    return Nrql(dedent(query.strip()))


def _perform_nrql_query(
    *,
    client: NewRelicClient,
    account: Account,
    nrql_query: Nrql,
    timeout: int = 60,
    async_: bool = False,
) -> CrossAccountNrdbResultContainer:
    """Execute a NRQL database query.

    Args:
        client: The New Relic API client instance for authentication.
        account: The target New Relic account object.
        nrql_query: Formatted SQL payload.
        timeout: Native request lifetime limit parameter. Defaults to 60.
        async_: Boolean flagging background processing. Defaults to False.

    Returns:
        A baseline cross-account configuration containing execution metrics.
    """

    # pylint: disable=redefined-outer-name

    logger.debug(
        "%d - %s - Performing NRQL query: %s",
        account.id,
        account.name,
        nrql_query,
    )

    operation = Operation(
        client.schema.query_type,
        variables={
            "accounts": Arg(non_null(list_of(non_null(Int)))),
            "nrqlQuery": Arg(non_null(Nrql)),
        },
    )

    nrql = operation.actor.nrql(
        accounts=Variable("accounts"),
        query=Variable("nrqlQuery"),
        timeout=timeout,
        async_=async_,
    )

    nrql.results()
    nrql.query_progress.completed()  # type: ignore
    nrql.query_progress.query_id()  # type: ignore
    nrql.query_progress.result_expiration()  # type: ignore
    nrql.query_progress.retry_after()  # type: ignore
    nrql.query_progress.retry_deadline()  # type: ignore

    response = client.execute(
        operation,
        variables={
            "accounts": [account.id],
            "nrqlQuery": nrql_query,
        },
    )

    raise_response_errors(
        response=response,
        account=account,
    )

    return (operation + response.json()).actor.nrql


def _check_nrql_query_progress(
    *,
    client: NewRelicClient,
    account: Account,
    query_id: ID,
) -> CrossAccountNrdbResultContainer:
    """Examine the background job status using its identifier.

    Args:
        client: The New Relic API client instance for authentication.
        account: The target New Relic account object.
        query_id: System token representing the background job.

    Returns:
        A cross-account execution block containing updated metadata.
    """

    logger.debug(
        "%d - %s - Checking NRQL query progress: %s",
        account.id,
        account.name,
        query_id,
    )

    operation = Operation(
        client.schema.query_type,
        variables={
            "accounts": Arg(non_null(list_of(non_null(Int)))),
            "queryId": Arg(non_null(ID)),
        },
    )

    query_progress = operation.actor.nrql_query_progress(
        accounts=Variable("accounts"),
        queryId=Variable("queryId"),
    )

    query_progress.results()  # type: ignore
    query_progress.query_progress.completed()  # type: ignore
    query_progress.query_progress.query_id()  # type: ignore
    query_progress.query_progress.result_expiration()  # type: ignore
    query_progress.query_progress.retry_after()  # type: ignore
    query_progress.query_progress.retry_deadline()  # type: ignore

    response = client.execute(
        operation,
        variables={
            "accounts": [account.id],
            "queryId": query_id,
        },
    )

    raise_response_errors(
        response=response,
        account=account,
    )

    return (operation + response.json()).actor.nrql_query_progress


def perform_nrql_query(
    *,
    client: NewRelicClient,
    account: Account,
    nrql_query: Nrql,
    timeout: int = 60,
    max_retry: int | None = None,
    max_retries: int = 5,
    retry_delay: int = 5,
) -> list[NrdbResult]:
    """Wrap asynchronous polling complexities into a single synchronous request.

    Args:
        client: The New Relic API client instance for authentication.
        account: The target New Relic account object.
        nrql_query: Formatted SQL payload.
        timeout: Maximum native polling lifecycle timeout. Defaults to 60.
        max_retry: Legacy parameter. Defaults to None.
        max_retries: Limit parameter restricting failed iterations. Defaults to 5.
        retry_delay: Delay value evaluated between checks. Defaults to 5.

    Returns:
        A list of returned query objects.
    """

    # pylint: disable=redefined-outer-name

    if max_retry is not None:
        warnings.warn(
            f"{account.id} - {account.name} - max_retry is deprecated and will "
            "be removed in the future. Use max_retries instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        max_retries = max_retry

    logger.debug(
        "%d - %s - Performing NRQL query: %s",
        account.id,
        account.name,
        nrql_query,
    )

    nrql: CrossAccountNrdbResultContainer = CrossAccountNrdbResultContainer(
        json_data={},
    )

    for retry in range(max_retries):
        try:
            nrql = _perform_nrql_query(
                client=client,
                account=account,
                nrql_query=nrql_query,
                timeout=timeout,
                async_=True,
            )

            logger.debug(
                "%d - %s - Created NRQL query with ID: %s",
                account.id,
                account.name,
                nrql.query_progress.query_id,
            )

            while not nrql.query_progress.completed:
                logger.debug(
                    "%d - %s - NRQL query %s is not completed yet, "
                    "waiting for %d seconds",
                    account.id,
                    account.name,
                    nrql.query_progress.query_id,
                    nrql.query_progress.retry_after,
                )

                time.sleep(nrql.query_progress.retry_after)  # type: ignore

                nrql = _check_nrql_query_progress(
                    client=client,
                    account=account,
                    query_id=nrql.query_progress.query_id,  # type: ignore
                )

            break

        except NewRelicError as e:
            if retry == max_retries - 1:
                raise e

            logger.error(
                "%d - %s - Failed to perform NRQL with error: %s",
                account.id,
                account.name,
                str(e),
            )
            logger.error(
                "%d - %s - Retrying NRQL query with trial: %d",
                account.id,
                account.name,
                retry + 1,
            )
            logger.error(
                "%d - %s - Waiting for %d seconds before retrying",
                account.id,
                account.name,
                retry_delay,
            )

            time.sleep(retry_delay)

    return nrql.results
