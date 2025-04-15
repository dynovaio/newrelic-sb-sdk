__all__ = [
    "logger",
    "get_new_relic_account_id_from_env",
    "get_new_relic_user_key_from_env",
    "NewRelicGqlClient",
    "NewRelicRestClient",
]


import json
import logging
import os
import pathlib
import warnings
from typing import Any, Callable, Dict, Union

import dotenv
from requests import Response, Session
from sgqlc.operation import Operation
from sgqlc.types import Schema

from ..graphql import nerdgraph
from ..graphql.objects import RootMutationType, RootQueryType
from ..utils.query import build_query
from ..version import VERSION

logger = logging.getLogger("newrelic_sb_sdk")


def _get_variable_from_env(
    variable_name: str,
    env_file_name: Union[str, None] = None,
    caster: Union[Callable, None] = None,
) -> Any:
    """Recover environment variable from environment or .env file."""

    if env_file_name is not None:
        env_file = pathlib.Path(env_file_name)

        if env_file.exists():
            dotenv.load_dotenv(env_file)

    variable = os.environ.get(variable_name, None)

    if variable is None:
        raise ValueError(f"Environment variable '{variable_name}' is not set.")

    if caster is not None:
        try:
            variable = caster(variable)
        except Exception as e:
            raise ValueError(
                f"Failed to cast environment variable '{variable_name}': {e}."
            ) from e

    logger.debug(
        "Environment variable '%s' loaded: %r (type: %r).",
        variable_name,
        variable,
        type(variable),
    )

    return variable


def get_new_relic_account_id_from_env(env_file_name: Union[str, None] = None) -> int:
    """Recovery new relic account id from environmentn variables."""

    return _get_variable_from_env(
        "NEW_RELIC_ACCOUNT_ID",
        env_file_name,
        caster=int,
    )


def get_new_relic_user_key_from_env(env_file_name: Union[str, None] = None) -> str:
    """Recovery new relic credentials from environmentn variables."""

    return _get_variable_from_env(
        "NEW_RELIC_USER_KEY",
        env_file_name,
    )


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

        warnings.warn(
            "NewRelicRestClient is deprecated. Use NewRelicGqlClient instead."
            " NewRelicRestClient will be removed in future versions.",
            DeprecationWarning,
            stacklevel=2,
        )

        logger.debug("NewRelicRestClient initialized with headers: %r", self.headers)

    @staticmethod
    def _get_version():
        return ".".join(VERSION)
