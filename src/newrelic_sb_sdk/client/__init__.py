__all__ = [
    "logger",
    "get_new_relic_account_id_from_env",
    "get_new_relic_user_key_from_env",
    "NewRelicClient",
    "NewRelicGqlClient",
    "NewRelicRestClient",
]


import json
import logging
import os
import pathlib
import warnings
from collections.abc import Callable
from typing import Any

import dotenv
from requests import Response, Session
from sgqlc.operation import Operation
from sgqlc.types import Schema

from ..graphql import nerdgraph
from ..graphql.objects import RootMutationType, RootQueryType
from ..utils.exceptions import InvalidUserKey
from ..utils.query import build_query
from ..utils.text import mask_text
from ..utils.validators import validate_user_key
from ..version import VERSION

logger = logging.getLogger("newrelic_sb_sdk")


def _get_variable_from_env(
    variable_name: str,
    env_file_name: str | None = None,
    caster: Callable | None = None,
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


def get_new_relic_account_id_from_env(env_file_name: str | None = None) -> int:
    """Recovery new relic account id from environmentn variables."""

    return _get_variable_from_env(
        "NEW_RELIC_ACCOUNT_ID",
        env_file_name,
        caster=int,
    )


def get_new_relic_user_key_from_env(env_file_name: str | None = None) -> str:
    """Recovery new relic credentials from environmentn variables."""

    return _get_variable_from_env(
        "NEW_RELIC_USER_KEY",
        env_file_name,
    )


class NewRelicClient(Session):
    """Client for New Relic GraphQL API."""

    _url: str = "https://api.newrelic.com/graphql"
    _schema: Schema = nerdgraph

    def __init__(self, *, new_relic_user_key: str):
        """Initialize the NewRelicClient.

        Args:
            new_relic_user_key (str): The New Relic user key for API authentication.

        Raises:
            InvalidUserKey: If the provided user key does not match the valid format.
        """
        super().__init__()

        if not validate_user_key(new_relic_user_key):
            raise InvalidUserKey(new_relic_user_key)

        self.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "API-Key": new_relic_user_key,
                "User-Agent": f"newrelic-sb-sdk/{self._get_version()}",
            }
        )

        logger.debug(
            "NewRelicClient initialized with headers: %r",
            {
                **self.headers,
                "API-Key": mask_text(
                    text=new_relic_user_key,
                    start=8,
                    end=-1,
                ),
            },
        )

        self._setup_schema()

    def _setup_schema(self):
        self._schema.query_type = RootQueryType
        self._schema.mutation_type = RootMutationType

    @staticmethod
    def _get_version():
        return ".".join(VERSION)

    def execute(
        self,
        query: str | Operation,
        *,
        variables: dict[str, Any] | None = None,
        **kwargs,
    ) -> Response:
        """Execute a GraphQL query against the New Relic API.

        Args:
            query (str | Operation): The GraphQL query string or an sgqlc Operation object.
            variables (dict[str, Any] | None, optional): A dictionary of variables for the query. Defaults to None.
            **kwargs: Additional keyword arguments passed to the underlying `requests.Session.post` method.

        Returns:
            Response: The HTTP response from the New Relic API.
        """
        if isinstance(query, Operation):
            query = query.__to_graphql__()

        data = json.dumps(
            {
                "query": query,
                "variables": variables,
            },
        )

        logger.debug("NewRelicClient executing with query: %r", query)
        logger.debug("NewRelicClient executing with variables: %r", variables)

        return self.post(self._url, data=data, **kwargs)

    @staticmethod
    def build_query(template: str, *, params: dict[str, Any] | None = None) -> str:
        """Build a query string from a template and parameters.

        Args:
            template (str): The query template string.
            params (dict[str, Any] | None, optional): The variables to format the template with. Defaults to None.

        Returns:
            str: The fully formed query string.
        """
        return build_query(template, params=params)

    @property
    def schema(self) -> Schema:
        """Returns the GraphQL Schema associated with the client."""
        return self._schema


class NewRelicGqlClient(NewRelicClient):
    """Deprecated alias for NewRelicClient for making GraphQL requests."""

    def __init__(self, *, new_relic_user_key: str):
        """Initialize the NewRelicGqlClient.

        Args:
            new_relic_user_key (str): The New Relic user key for API authentication.
        """
        warnings.warn(
            "NewRelicGqlClient is deprecated. Use NewRelicClient instead."
            " NewRelicGqlClient will be removed in future versions.",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(new_relic_user_key=new_relic_user_key)


class NewRelicRestClient(Session):
    """Deprecated Client for New Relic Rest API."""

    url: str = "https://api.newrelic.com/v2/"

    def __init__(self, *, new_relic_user_key: str):
        """Initialize the NewRelicRestClient.

        Args:
            new_relic_user_key (str): The New Relic user key for API authentication.
        """
        super().__init__()

        warnings.warn(
            "NewRelicRestClient is deprecated because the New Relic REST API v2 is very limited "
            "and progressively moving to NerdGraph. Use NewRelicClient instead."
            " NewRelicRestClient will be removed in future versions.",
            DeprecationWarning,
            stacklevel=2,
        )

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
