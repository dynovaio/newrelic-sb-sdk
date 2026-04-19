__all__ = ["print_response", "get_response_data", "raise_response_errors"]


import json
from typing import Any, Union

from requests import Response

from ..graphql.objects import Account
from .exceptions import NewRelicError


def print_response(response, compact: bool = False):
    """Print an HTTP Response formatted as JSON.

    Args:
        response: The HTTP response element.
        compact: Toggles nested indentation formatting rules. Defaults to False.
    """

    print(
        json.dumps(
            response.json(),
            indent=None if compact else 4,
        )
    )


def get_response_data(
    response, key_path: str | None = None, action: str = "actor"
) -> dict[str, Any] | None:
    """Extract entries from an HTTP response payload.

    Args:
        response: The HTTP response payload.
        key_path: Nested path querying internal parameters. Defaults to None.
        action: Filters specific block limits. Defaults to "actor".

    Returns:
        The matched element extracted iteratively from the payload.
    """

    data = response.json().get("data").get(action)

    if key_path is not None:
        for key in key_path.split(":"):
            if key.isdecimal() and isinstance(data, list):
                data = data[int(key)]
            else:
                data = data.get(key)

    return data


def raise_response_errors(*, response: Response, account: Account | None = None):
    """Validate response bounds and raise exceptions on errors.

    Args:
        response: The HTTP response payload.
        account: The targeted context configuring standard bounds representation.
            Defaults to None.

    Raises:
        NewRelicError: Raised when parameters match failure criteria.
    """

    response.raise_for_status()

    response_json = response.json()

    if errors := response_json.get("errors", None):
        for error in errors:
            message = error["message"]

            if account:
                message = f"{account.id} - {account.name} - {message}"

            raise NewRelicError(message)
