__all__ = ["validate"]


from sgqlc.operation import Operation

from ..client import NewRelicGqlClient
from ..graphql.objects import Account, User
from ..utils.response import raise_response_errors


def validate(*, client: NewRelicGqlClient, account: Account | None = None) -> User:
    operation = Operation(
        client.schema.query_type,
    )
    operation.actor.user.__fields__(
        "id",
        "email",
        "name",
    )

    response = client.execute(
        operation.__to_graphql__(),
    )

    raise_response_errors(
        response=response,
        account=account,
    )

    data = operation + response.json()
    data = data.actor.user

    return data
