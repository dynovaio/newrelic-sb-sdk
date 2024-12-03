__all__ = [
    "logger",
    "get_new_relic_user_key_from_env",
    "NewRelicGqlClient",
    "NewRelicRestClient",
]


import json
import logging
import os
import pathlib
from typing import Any, Dict, Union

import dotenv
from requests import Response, Session
from sgqlc.operation import Operation
from sgqlc.types import Schema

from ..graphql import nerdgraph
from ..graphql.objects import RootMutationType, RootQueryType
from ..utils.query import build_query
from ..version import VERSION

logger = logging.getLogger("newrelic_sb_sdk")


def get_new_relic_user_key_from_env(env_file_name: Union[str, None] = None) -> str:
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

    _url: str = "https://api.newrelic.com/graphql"
    _schema: Schema = nerdgraph

    def __init__(self, *, new_relic_user_key: str):
        super().__init__()

        self.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "API-Key": new_relic_user_key,
                "User-Agent": f"newrelic-sb-sdk/{self._get_version()}",
            }
        )
        logger.debug("NewRelicGqlClient initialized with headers: %r", self.headers)

        self._setup_schema()

    @staticmethod
    def _get_version():
        return ".".join(VERSION)

    def _setup_schema(self):
        self._schema.query_type = RootQueryType
        self._schema.mutation_type = RootMutationType

    def execute(
        self,
        query: Union[str, Operation],
        *,
        variables: Union[Dict[str, Any], None] = None,
        **kwargs,
    ) -> Response:
        if isinstance(query, Operation):
            query = query.__to_graphql__()

        data = json.dumps(
            {
                "query": query,
                "variables": variables,
            },
        )

        logger.debug("NewRelicGqlClient executing with query: %r", query)
        logger.debug("NewRelicGqlClient executing with variables: %r", variables)

        return self.post(self._url, data=data, **kwargs)

    @staticmethod
    def build_query(
        template: str, *, params: Union[Dict[str, Any], None] = None
    ) -> str:
        return build_query(template, params=params)

    @property
    def schema(self) -> Schema:
        return self._schema


class NewRelicRestClient(Session):
    """Client for New Relic Rest API."""

    url: str = "https://api.newrelic.com/v2/"

    def __init__(self, *, new_relic_user_key: str):
        super().__init__()

        self.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Api-Key": new_relic_user_key,
                "User-Agent": f"newrelic-sb-sdk/{self._get_version()}",
            }
        )

        logger.debug("NewRelicRestClient initialized with headers: %r", self.headers)

    @staticmethod
    def _get_version():
        return ".".join(VERSION)
