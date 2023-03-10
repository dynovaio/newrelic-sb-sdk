__all__ = [
    "WidgetLayout",
    "WidgetVisualization",
    "BaseNRQLQueryWidgetConfiguration",
    "AreaWidgetConfiguration",
    "BarWidgetConfiguration",
    "BillboardWidgetConfiguration",
    "LineWidgetConfiguration",
    "MarkdownWidgetConfiguration",
    "PieWidgetConfiguration",
    "TableWidgetConfiguration",
    "WidgetConfiguration",
    "Widget",
]


from dataclasses import dataclass
from typing import List

from ..core.base import BaseEntity
from .enums import WidgetVisualizationId
from .utils import NRQLQuery, Threshold


@dataclass(kw_only=True)
class WidgetLayout(BaseEntity):
    column: int = 1
    height: int = 3
    row: int = 1
    width: int = 4


@dataclass(kw_only=True)
class WidgetVisualization(BaseEntity):
    id: WidgetVisualizationId | str

    property_processors = {
        "id": WidgetVisualizationId.from_json,
    }


@dataclass(kw_only=True)
class BaseNRQLQueryWidgetConfiguration(BaseEntity):
    nrql_queries: List[NRQLQuery] | None = None

    property_processors = {
        "nrql_queries": NRQLQuery.from_json,
    }


@dataclass(kw_only=True)
class AreaWidgetConfiguration(BaseNRQLQueryWidgetConfiguration):
    pass


@dataclass(kw_only=True)
class BarWidgetConfiguration(BaseNRQLQueryWidgetConfiguration):
    pass


@dataclass(kw_only=True)
class BillboardWidgetConfiguration(BaseNRQLQueryWidgetConfiguration):
    thresholds: List[NRQLQuery] | None = None

    property_processors = {
        "nrql_queries": NRQLQuery.from_json,
        "thresholds": Threshold.from_json,
    }


@dataclass(kw_only=True)
class LineWidgetConfiguration(BaseNRQLQueryWidgetConfiguration):
    pass


@dataclass(kw_only=True)
class MarkdownWidgetConfiguration(BaseEntity):
    text: str = ""


@dataclass(kw_only=True)
class PieWidgetConfiguration(BaseNRQLQueryWidgetConfiguration):
    pass


@dataclass(kw_only=True)
class TableWidgetConfiguration(BaseNRQLQueryWidgetConfiguration):
    pass


@dataclass(kw_only=True)
class WidgetConfiguration(BaseEntity):
    area: AreaWidgetConfiguration | None = None
    bar: BarWidgetConfiguration | None = None  # pylint: disable=disallowed-name
    billboard: BillboardWidgetConfiguration | None = None
    line: LineWidgetConfiguration | None = None
    markdown: MarkdownWidgetConfiguration | None = None
    pie: PieWidgetConfiguration | None = None
    table: TableWidgetConfiguration | None = None

    property_processors = {
        "area": AreaWidgetConfiguration.from_json,
        "bar": BarWidgetConfiguration.from_json,
        "billboard": BillboardWidgetConfiguration.from_json,
        "line": LineWidgetConfiguration.from_json,
        "markdown": MarkdownWidgetConfiguration.from_json,
        "pie": PieWidgetConfiguration.from_json,
        "table": TableWidgetConfiguration.from_json,
    }


@dataclass(kw_only=True)
class Widget(BaseEntity):
    id: str | int | None = None
    title: str = ""
    # linked_entity_guids must be a list[str]
    # but we get an TypeError about parametrized generics
    # due to enforce_types
    linked_entity_guids: list | str | None = None
    layout: WidgetLayout | None = None
    visualization: WidgetVisualization | None = None
    configuration: WidgetConfiguration | None = None
    raw_configuration: dict | None = None

    property_processors = {
        "layout": WidgetLayout.from_json,
        "visualization": WidgetVisualization.from_json,
        "configuration": WidgetConfiguration.from_json,
    }
