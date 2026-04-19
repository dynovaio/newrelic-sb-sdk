__all__ = ["snake2camel", "camel2snake", "camelize_keys", "snakeize_keys", "mask_text"]


import re


def snake2camel(snake_string: str) -> str:
    """Convert a snake_case string into camelCase.

    Args:
        snake_string: The base snake_case string.

    Returns:
        The target camelCase text formatting.
    """

    head, *tail = snake_string.split("_")
    camel_string = "".join(
        [
            head.lower(),
            *[word.capitalize() for word in tail],
        ]
    )
    return camel_string


def camel2snake(camel_string: str) -> str:
    """Convert a camelCase string into snake_case.

    Args:
        camel_string: The base camelCase string.

    Returns:
        The target snake_case text formatting.
    """

    return re.sub(r"(([A-Z][a-z])|([0-9])+)", r"_\1", camel_string).lower().strip("_")


def camelize_keys(obj: dict, convert_objects_inside_lists: bool = True) -> dict:
    """Recursively convert dictionary keys from snake_case to camelCase.

    Args:
        obj: The active dictionary object.
        convert_objects_inside_lists: Enables iteration inside lists.
            Defaults to True.

    Returns:
        A dictionary representation utilizing camelized keys.
    """

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
    """Recursively convert dictionary keys from camelCase to snake_case.

    Args:
        obj: The active dictionary object.
        convert_objects_inside_lists: Enables iterating inside lists.
            Defaults to True.

    Returns:
        A dictionary representation utilizing snakeized keys.
    """

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


def mask_text(*, text: str, start: int = 0, end: int = -1) -> str:
    """Mask textual strings by substituting core elements.

    Args:
        text: The target input strings.
        start: Offset representing length boundary from the prefix. Defaults to 0.
        end: Offset representing length boundary from the suffix. Defaults to -1.

    Returns:
        The masked format matching standard bounds length.
    """

    if not len(text):
        return text

    body = "*" * len(text[start:end])

    if not body:
        return text

    head = text[:start]
    tail = text[end:]
    body = "*" * len(text[start:end])

    return f"{head}{body}{tail}".strip()
