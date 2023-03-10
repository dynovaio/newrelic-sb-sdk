__all__ = ["NULL_CURSOR", "build_query"]


import json
from textwrap import dedent

NULL_CURSOR: str = json.dumps(None)


def build_query(query_string: str, **kwargs) -> str:
    query = dedent(query_string.strip()) % kwargs

    return json.dumps(
        {
            "query": query,
        }
    )
