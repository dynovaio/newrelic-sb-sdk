__all__ = ["print_response", "get_response_data"]


import json


def print_response(response, compact: bool = False):
    """Print response in json format."""
    print(
        json.dumps(
            response.json(),
            indent=None if compact else 4,
        )
    )


def get_response_data(
    response, key_path: str | None = None, action: str = "actor"
) -> dict | None:
    """Get response body entries from a keypath."""
    data = response.json().get("data").get(action)

    if key_path is not None:
        for key in key_path.split(":"):
            if key.isdecimal() and isinstance(data, list):
                data = data[int(key)]
            else:
                data = data.get(key)

    return data
