__all__ = [
    "AlertSeverity",
    "WidgetType",
    "WidgetVisualizationId",
    "DashboardPermission",
]


from ..core.base import BaseEnum


class AlertSeverity(BaseEnum):
    CRITICAL = "CRITICAL"
    NOT_ALERTING = "NOT_ALERTING"
    WARNING = "WARNING"


class WidgetType(BaseEnum):
    AREA = "area"
    BAR = "bar"
    BILLBOARD = "billboard"
    LINE = "line"
    MARKDOWN = "markdown"
    PIE = "pie"
    TABLE = "table"


class WidgetVisualizationId(BaseEnum):
    # Visualizations
    AREA = "viz.area"
    BAR = "viz.bar"
    BILLBOARD = "viz.billboard"
    BULLET = "viz.bullet"
    EVENT_FEED = "viz.event-feed"
    FUNNEL = "viz.funnel"
    HEATMAP = "viz.heatmap"
    HISTOGRAM = "viz.histogram"
    JSON = "viz.json"
    LINE = "viz.line"
    MARKDOWN = "viz.markdown"
    PIE = "viz.pie"
    TABLE = "viz.table"

    # Infrastructure
    INVENTORY = "infra.inventory"

    # Topology
    SERVICE_MAP = "topology.service-map"


class DashboardPermission(BaseEnum):
    PRIVATE = "PRIVATE"
    PUBLIC_READ_ONLY = "PUBLIC_READ_ONLY"
    PUBLIC_READ_WRITE = "PUBLIC_READ_WRITE"
