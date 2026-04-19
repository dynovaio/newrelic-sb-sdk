__all__ = ["NULL_CURSOR", "build_query"]


import json
from textwrap import dedent
from typing import Any, Union

NULL_CURSOR: str = json.dumps(None)


def build_query(template: str, *, params: dict[str, Any] | None = None) -> str:
    """Render a query payload using templates and parameters.

    Args:
        template: The baseline template text.
        params: The configuration values to combine into the template representation.
            Defaults to None.

    Returns:
        The completed query string parameter definitions.
    """

    if not params:
        params = {}

    return dedent(template.strip()) % params
