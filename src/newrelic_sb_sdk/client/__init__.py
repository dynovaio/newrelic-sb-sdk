__all__ = ["get_new_relic_user_key_from_env", "NewRelicGqlClient", "NewRelicRestClient"]


import json
import os
import pathlib
import re
from textwrap import dedent

import dotenv
from requests import Session


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
        self, query=None, query_kwargs=None, **kwargs
    ):  # pylint: disable=arguments-differ
        data = self._build_query(query, **(query_kwargs or {}))
        return self.post(self.url, data=data, **kwargs)

    @staticmethod
    def _build_query(query_string, **kwargs):
        return json.dumps({"query": dedent(query_string.strip()) % kwargs})


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
