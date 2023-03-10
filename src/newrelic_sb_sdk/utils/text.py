__all__ = ["snake2camel", "camel2snake", "camelize_keys", "snakeize_keys"]


import re


def snake2camel(snake_string: str) -> str:
    """Convert snake case to camel case."""
    head, *tail = snake_string.split("_")
    camel_string = "".join(
        [
            head.lower(),
            *[word.capitalize() for word in tail],
        ]
    )
    return camel_string


def camel2snake(camel_string: str) -> str:
    """Convert camel case to snake case."""
    return re.sub(r"(([A-Z][a-z])|([0-9])+)", r"_\1", camel_string).lower().strip("_")


def camelize_keys(obj: dict, convert_objects_inside_lists: bool = True) -> dict:
    """Convert dictionary keys to camel case."""
    camelized_obj = {}

    for key, value in dict(obj).items():
        key = snake2camel(key) if isinstance(key, str) else key

        if isinstance(value, dict):
            value = camelize_keys(value)
        elif isinstance(value, list) and convert_objects_inside_lists:
            value = [
                camelize_keys(item) if isinstance(item, dict) else item
                for item in value
            ]

        camelized_obj.update(
            {
                key: value,
            },
        )

    return camelized_obj


def snakeize_keys(obj: dict, convert_objects_inside_lists: bool = True) -> dict:
    """Convert dictionary keys to snake case."""
    snakeized_obj = {}

    for key, value in dict(obj).items():
        key = camel2snake(key) if isinstance(key, str) else key

        if isinstance(value, dict):
            value = snakeize_keys(value)
        elif isinstance(value, list) and convert_objects_inside_lists:
            value = [
                snakeize_keys(item) if isinstance(item, dict) else item
                for item in value
            ]

        snakeized_obj.update(
            {
                key: value,
            },
        )

    return snakeized_obj
