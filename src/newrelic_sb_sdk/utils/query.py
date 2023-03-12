__all__ = ["NULL_CURSOR", "build_query"]


import json
from textwrap import dedent
from typing import Any, Dict

NULL_CURSOR: str = json.dumps(None)


def build_query(query_string: str, query_params: Dict[str, Any]) -> str:
    return dedent(query_string.strip()) % query_params
