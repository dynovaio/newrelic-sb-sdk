__all__ = [
    "Boolean",
    "Date",
    "DateTime",
    "Float",
    "ID",
    "Int",
    "String",
    "AgentApplicationSettingsCustomJsConfiguration",
    "AgentApplicationSettingsErrorCollectorHttpStatus",
    "AgentApplicationSettingsRawJsConfiguration",
    "AiDecisionsRuleExpression",
    "AttributeMap",
    "ChangeTrackingRawCustomAttributesMap",
    "CollaborationRawContextMetadata",
    "DashboardWidgetRawConfiguration",
    "DistributedTracingSpanAttributes",
    "Duration",
    "EntityAlertViolationInt",
    "EntityGuid",
    "EntitySearchQuery",
    "EpochMilliseconds",
    "EpochSeconds",
    "ErrorsInboxRawEvent",
    "InstallationRawMetadata",
    "LogConfigurationsLogDataPartitionName",
    "Milliseconds",
    "Minutes",
    "NaiveDateTime",
    "NerdStorageDocument",
    "NerdpackTagName",
    "Nr1CatalogRawNerdletState",
    "NrdbRawResults",
    "NrdbResult",
    "Nrql",
    "Seconds",
    "SecureValue",
    "SemVer",
]


# pylint: disable=duplicate-code,unused-import,too-many-lines


import sgqlc.types
import sgqlc.types.datetime

from . import nerdgraph

__docformat__ = "markdown"


class AgentApplicationSettingsCustomJsConfiguration(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class AgentApplicationSettingsErrorCollectorHttpStatus(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class AgentApplicationSettingsRawJsConfiguration(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class AiDecisionsRuleExpression(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class AttributeMap(sgqlc.types.Scalar):
    __schema__ = nerdgraph


Boolean = sgqlc.types.Boolean


class ChangeTrackingRawCustomAttributesMap(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class CollaborationRawContextMetadata(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class DashboardWidgetRawConfiguration(sgqlc.types.Scalar):
    __schema__ = nerdgraph


Date = sgqlc.types.datetime.Date


DateTime = sgqlc.types.datetime.DateTime


class DistributedTracingSpanAttributes(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class Duration(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class EntityAlertViolationInt(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class EntityGuid(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class EntitySearchQuery(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class EpochMilliseconds(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class EpochSeconds(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class ErrorsInboxRawEvent(sgqlc.types.Scalar):
    __schema__ = nerdgraph


Float = sgqlc.types.Float


ID = sgqlc.types.ID


class InstallationRawMetadata(sgqlc.types.Scalar):
    __schema__ = nerdgraph


Int = sgqlc.types.Int


class LogConfigurationsLogDataPartitionName(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class Milliseconds(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class Minutes(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class NaiveDateTime(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class NerdStorageDocument(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class NerdpackTagName(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class Nr1CatalogRawNerdletState(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class NrdbRawResults(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class NrdbResult(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class Nrql(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class Seconds(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class SecureValue(sgqlc.types.Scalar):
    __schema__ = nerdgraph


class SemVer(sgqlc.types.Scalar):
    __schema__ = nerdgraph


String = sgqlc.types.String
