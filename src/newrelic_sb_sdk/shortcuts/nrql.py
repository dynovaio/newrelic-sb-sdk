__all__ = ["logger", "nrql", "perform_nrql_query"]


import logging
import time
import warnings
from textwrap import dedent
from typing import List, Union

from sgqlc.operation import Operation
from sgqlc.types import ID, Arg, Int, Variable, list_of, non_null

from newrelic_sb_sdk.graphql.objects import (
    Account,
    CrossAccountNrdbResultContainer,
    NrdbResult,
)

from ..client import NewRelicGqlClient
from ..graphql.scalars import Nrql
from ..utils.exceptions import NewRelicError
from ..utils.response import raise_response_errors

logger = logging.getLogger("newrelic_sb_sdk")


def nrql(query: str) -> Nrql:
    return Nrql(dedent(query.strip()))


def _perform_nrql_query(
    *,
    client: NewRelicGqlClient,
    account: Account,
    nrql_query: Nrql,
    timeout: int = 60,
    async_: bool = False,
) -> CrossAccountNrdbResultContainer:
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
    nrql.query_progress.completed()
    nrql.query_progress.query_id()
    nrql.query_progress.result_expiration()
    nrql.query_progress.retry_after()
    nrql.query_progress.retry_deadline()

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
    client: NewRelicGqlClient,
    account: Account,
    query_id: ID,
) -> CrossAccountNrdbResultContainer:
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

    query_progress.results()
    query_progress.query_progress.completed()
    query_progress.query_progress.query_id()
    query_progress.query_progress.result_expiration()
    query_progress.query_progress.retry_after()
    query_progress.query_progress.retry_deadline()

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
    client: NewRelicGqlClient,
    account: Account,
    nrql_query: Nrql,
    timeout: int = 60,
    max_retry: Union[int, None] = None,
    max_retries: int = 5,
    retry_delay: int = 5,
) -> List[NrdbResult]:
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

                time.sleep(nrql.query_progress.retry_after)

                nrql = _check_nrql_query_progress(
                    client=client,
                    account=account,
                    query_id=nrql.query_progress.query_id,
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
