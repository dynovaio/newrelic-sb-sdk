__all__ = ["NULL_CURSOR", "build_query"]


import json
from textwrap import dedent
from typing import Any, Dict, Union

NULL_CURSOR: str = json.dumps(None)


def build_query(template: str, *, params: Union[Dict[str, Any], None] = None) -> str:
    if not params:
        params = {}

    return dedent(template.strip()) % params
