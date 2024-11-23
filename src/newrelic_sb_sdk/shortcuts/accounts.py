__all__ = ["get_all_accounts", "get_account"]


from typing import List, Union

from sgqlc.operation import Operation

from ..client import NewRelicGqlClient
from ..graphql.input_objects import TimeWindowInput
from ..graphql.objects import Account
from ..utils.response import raise_response_errors


def get_all_accounts(
    *,
    client: NewRelicGqlClient,
    include_event_types: bool = False,
    time_window: Union[TimeWindowInput, None] = None,
) -> List[Account]:
    operation = Operation(client.schema.query_type)

    operation.actor.accounts.id()
    operation.actor.accounts.name()

    if include_event_types:
        if time_window:
            operation.actor.accounts.reporting_event_types(time_window=time_window)
        else:
            operation.actor.accounts.reporting_event_types()

    response = client.execute(operation)

    raise_response_errors(response=response)

    data = operation + response.json()
    data = data.actor.accounts

    return data


def get_account(*, client: NewRelicGqlClient, account_id: int) -> Account:
    operation = Operation(client.schema.query_type)

    account = operation.actor.account(id=account_id)

    account.id()
    account.name()

    response = client.execute(operation)

    raise_response_errors(response=response)

    data = operation + response.json()
    data = data.actor.account

    return data
