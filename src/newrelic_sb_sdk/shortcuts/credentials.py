__all__ = ["validate"]


from typing import Union

from sgqlc.operation import Operation

from ..client import NewRelicClient
from ..graphql.objects import Account, User
from ..utils.response import raise_response_errors


def validate(*, client: NewRelicClient, account: Account | None = None) -> User:
    operation = Operation(
        client.schema.query_type,
    )
    operation.actor.user.__fields__(
        "id",
        "email",
        "name",
    )

    response = client.execute(operation)

    raise_response_errors(
        response=response,
        account=account,
    )

    data = operation + response.json()
    data = data.actor.user

    return data
