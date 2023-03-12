__all__ = ["get_new_relic_user_key_from_env", "NewRelicGqlClient", "NewRelicRestClient"]


import json
import os
import pathlib
import re
from textwrap import dedent
from typing import Any, Dict

import dotenv
from requests import Response, Session

from ..utils.query import build_query


def get_new_relic_user_key_from_env(env_file_name: str | None = None) -> str:
    """Recovery new relic credentials from environmentn variables."""

    if env_file_name is not None:
        env_file = pathlib.Path(env_file_name)

        if env_file.exists():
            dotenv.load_dotenv(env_file)

    new_relic_user_key = os.environ.get("NEW_RELIC_USER_KEY", None)

    if new_relic_user_key is None:
        raise ValueError("Environment variable NEW_RELIC_USER_KEY is not set.")

    return new_relic_user_key


class NewRelicGqlClient(Session):
    """Client for New Relic GraphQL API."""

    url: str = "https://api.newrelic.com/graphql"

    def __init__(self, *, new_relic_user_key: str):
        super().__init__()

        self.headers.update(
            {
                "Content-Type": "application/json",
                "API-Key": new_relic_user_key,
            }
        )

    def execute(
        self, query: str, variables: Dict[str, Any] | None = None, **kwargs
    ) -> Response:
        data = json.dumps(
            {
                "query": query,
                "variables": variables,
            },
        )
        return self.post(self.url, data=data, **kwargs)

    @staticmethod
    def build_query(query_string: str, query_params: Dict[str, Any]) -> str:
        return build_query(query_string, query_params)


class NewRelicRestClient(Session):
    """Client for New Relic Rest API."""

    url: str = "https://api.newrelic.com/v2/"

    def __init__(self, *, new_relic_user_key: str):
        super().__init__()

        self.headers.update(
            {
                "Content-Type": "application/json",
                "Api-Key": new_relic_user_key,
            }
        )
