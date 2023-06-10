__all__ = ["NULL_CURSOR", "build_query"]


import json
from textwrap import dedent
from typing import Any, Dict, Union

NULL_CURSOR: str = json.dumps(None)


def build_query(
    *, query_string: str, query_params: Union[Dict[str, Any], None] = None
) -> str:
    if not query_params:
        query_params = {}

    return dedent(query_string.strip()) % query_params
