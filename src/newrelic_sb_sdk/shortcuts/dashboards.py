__all__ = ["get_all_dashboards", "get_dashboard"]


import re
from typing import List, Union

from sgqlc.operation import Operation
from sgqlc.types import Arg, Variable, non_null

from newrelic_sb_sdk.graphql.enums import (
    EntitySearchCountsFacet,
    EntitySearchQueryBuilderType,
)
from newrelic_sb_sdk.graphql.input_objects import (
    EntitySearchOptions,
    EntitySearchQueryBuilder,
    EntitySearchQueryBuilderTag,
)

from ..client import NewRelicGqlClient
from ..graphql.objects import DashboardEntity, DashboardEntityOutline
from ..graphql.scalars import EntityGuid, String
from ..utils.response import raise_response_errors

_RE_PARSE = re.compile(
    r"^(?P<Y>\d{4})-?(?P<m>\d{2})-?(?P<d>\d{2})T"
    r"(?P<H>\d{2}):?(?P<M>\d{2})(:?(?P<S>\d{2})){0,1}(?P<MS>|[.]\d+)"
    r"(?P<TZ>|Z|(?P<TZH>[+-]\d{2}):?(?P<TZM>\d{2}))$"
)


def _patch_datetime(datetimestr):
    m = _RE_PARSE.match(datetimestr)

    if m and m.group("S") is None:
        return datetimestr.replace("Z", ":00Z")

    return datetimestr


def get_all_dashboards(
    *,
    client: NewRelicGqlClient,
    options: Union[EntitySearchOptions, None] = None,
) -> List[DashboardEntityOutline]:
    operation = Operation(
        client.schema.query_type,
        variables={
            "cursor": Arg(String),
            "options": Arg(EntitySearchOptions),
        },
    )

    entity_search = operation.actor.entity_search(
        query_builder=EntitySearchQueryBuilder(
            type=EntitySearchQueryBuilderType("DASHBOARD"),
            tags=[
                EntitySearchQueryBuilderTag(
                    key="isDashboardPage",
                    value="false",
                )
            ],
        ),
        options=Variable("options"),
    )

    entity_search.count()
    entity_search_counts = entity_search.counts(
        facet=[EntitySearchCountsFacet("ACCOUNT_ID")],
    )

    entity_search_counts.count()
    entity_search_counts.facet()

    entity_search_results = entity_search.results(
        cursor=Variable("cursor"),
    )
    entity_search_results.next_cursor()
    entity_search_results_as_dashboards = entity_search_results.entities.__as__(
        DashboardEntityOutline
    )
    entity_search_results_as_dashboards.guid()

    entity_search_results_as_dashboards.guid()
    entity_search_results_as_dashboards.name()
    entity_search_results_as_dashboards.account.id()
    entity_search_results_as_dashboards.account.name()
    entity_search_results_as_dashboards.created_at()
    entity_search_results_as_dashboards.dashboard_parent_guid()
    entity_search_results_as_dashboards.entity_type()
    entity_search_results_as_dashboards.first_indexed_at()
    entity_search_results_as_dashboards.owner.email()
    entity_search_results_as_dashboards.owner.user_id()
    entity_search_results_as_dashboards.permissions()
    entity_search_results_as_dashboards.tags.key()
    entity_search_results_as_dashboards.tags.values()
    entity_search_results_as_dashboards.type()
    entity_search_results_as_dashboards.updated_at()

    response = client.execute(
        operation,
        variables={
            "options": options,
            "cursor": None,
        },
    )

    raise_response_errors(
        response=response,
    )

    data = (operation + response.json()).actor.entity_search
    cursor = data.results.next_cursor
    dashboards = data.results.entities

    while cursor is not None:
        response = client.execute(
            operation,
            variables={
                "options": options,
                "cursor": cursor,
            },
        )

        raise_response_errors(
            response=response,
        )

        data = (operation + response.json()).actor.entity_search
        cursor = data.results.next_cursor
        dashboards += data.results.entities

    return dashboards


def get_dashboard(
    *,
    client: NewRelicGqlClient,
    guid: EntityGuid,
) -> DashboardEntity:

    operation = Operation(
        client.schema.query_type,
        variables={
            "guid": Arg(non_null(EntityGuid)),
        },
    )

    dashboard = operation.actor.entity(
        guid=Variable("guid"),
    ).__as__(
        DashboardEntity,
    )

    dashboard.account.id()
    dashboard.account.name()
    dashboard.created_at()
    dashboard.dashboard_parent_guid()
    dashboard.description()
    dashboard.domain()
    dashboard.entity_type()
    dashboard.first_indexed_at()
    dashboard.guid()
    dashboard.indexed_at()
    dashboard.last_reporting_change_at()
    dashboard.name()
    dashboard.owner.email()
    dashboard.owner.user_id()
    dashboard.permalink()
    dashboard.permissions()
    dashboard.type()
    dashboard.updated_at()
    dashboard.pages.created_at()
    dashboard.pages.description()
    dashboard.pages.guid()
    dashboard.pages.name()
    dashboard.pages.owner.email()
    dashboard.pages.owner.user_id()
    dashboard.pages.updated_at()
    dashboard.pages.widgets.id()
    dashboard.pages.widgets.layout.column()
    dashboard.pages.widgets.layout.height()
    dashboard.pages.widgets.layout.row()
    dashboard.pages.widgets.layout.width()
    dashboard.pages.widgets.raw_configuration()
    dashboard.pages.widgets.title()
    dashboard.pages.widgets.visualization.id()

    response = client.execute(
        operation,
        variables={
            "guid": guid,
        },
    )

    raise_response_errors(response=response)

    response_json = response.json()

    response_json["data"]["actor"]["entity"]["createdAt"] = _patch_datetime(
        response_json["data"]["actor"]["entity"]["createdAt"]
    )
    response_json["data"]["actor"]["entity"]["updatedAt"] = _patch_datetime(
        response_json["data"]["actor"]["entity"]["updatedAt"]
    )

    for p, page in enumerate(response_json["data"]["actor"]["entity"]["pages"]):
        page["createdAt"] = _patch_datetime(
            page["createdAt"],
        )
        page["updatedAt"] = _patch_datetime(
            page["updatedAt"],
        )
        response_json["data"]["actor"]["entity"]["pages"][p] = page

    return (operation + response_json).actor.entity
