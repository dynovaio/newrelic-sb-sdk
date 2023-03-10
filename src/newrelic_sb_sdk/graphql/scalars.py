__all__ = [
    "Boolean",
    "Date",
    "DateTime",
    "Float",
    "ID",
    "Int",
    "String",
    "AgentApplicationSettingsErrorCollectorHttpStatus",
    "AiDecisionsRuleExpression",
    "AttributeMap",
    "DashboardWidgetRawConfiguration",
    "DistributedTracingSpanAttributes",
    "EntityAlertViolationInt",
    "EntityGuid",
    "EntitySearchQuery",
    "EpochMilliseconds",
    "EpochSeconds",
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


class AgentApplicationSettingsErrorCollectorHttpStatus(sgqlc.types.Scalar):
    """Class for AgentApplicationSettingsErrorCollectorHttpStatus.

    A list of HTTP status codes, such as "404" or "500".
    """

    __schema__ = nerdgraph


class AiDecisionsRuleExpression(sgqlc.types.Scalar):
    """Class for AiDecisionsRuleExpression.

    Expression used for comparing incidents as part of a correlation.
    """

    __schema__ = nerdgraph


class AttributeMap(sgqlc.types.Scalar):
    """Class for AttributeMap.

    This scalar represents a map of attributes in the form of key-
    value pairs.
    """

    __schema__ = nerdgraph


Boolean = sgqlc.types.Boolean


class DashboardWidgetRawConfiguration(sgqlc.types.Scalar):
    """Class for DashboardWidgetRawConfiguration.

    Raw JSON payload with full configuration of a widget.
    """

    __schema__ = nerdgraph


Date = sgqlc.types.datetime.Date


DateTime = sgqlc.types.datetime.DateTime


class DistributedTracingSpanAttributes(sgqlc.types.Scalar):
    """Class for DistributedTracingSpanAttributes.

    Map of key value pairs for a span.
    """

    __schema__ = nerdgraph


class EntityAlertViolationInt(sgqlc.types.Scalar):
    """Class for EntityAlertViolationInt.

    The `ViolationInt` scalar type represents 52-bit signed integers.
    """

    __schema__ = nerdgraph


class EntityGuid(sgqlc.types.Scalar):
    """Class for EntityGuid.

    An encoded Entity GUID.
    """

    __schema__ = nerdgraph


class EntitySearchQuery(sgqlc.types.Scalar):
    """Class for EntitySearchQuery.

    A query string using Entity Search query syntax.
    """

    __schema__ = nerdgraph


class EpochMilliseconds(sgqlc.types.Scalar):
    """Class for EpochMilliseconds.

    The `EpochMilliseconds` scalar represents the number of
    milliseconds since the Unix epoch.
    """

    __schema__ = nerdgraph


class EpochSeconds(sgqlc.types.Scalar):
    """Class for EpochSeconds.

    The `EpochSeconds` scalar represents the number of seconds since
    the Unix epoch.
    """

    __schema__ = nerdgraph


Float = sgqlc.types.Float


ID = sgqlc.types.ID


class InstallationRawMetadata(sgqlc.types.Scalar):
    """Class for InstallationRawMetadata.

    An arbitrary key:value object containing additional data related
    to the environment where the installation occurred.
    """

    __schema__ = nerdgraph


Int = sgqlc.types.Int


class LogConfigurationsLogDataPartitionName(sgqlc.types.Scalar):
    """Class for LogConfigurationsLogDataPartitionName.

    The name of a log data partition. Has to start with 'Log_' prefix
    and can only contain alphanumeric characters and underscores.
    """

    __schema__ = nerdgraph


class Milliseconds(sgqlc.types.Scalar):
    """Class for Milliseconds.

    The `Milliseconds` scalar represents a duration in milliseconds.
    """

    __schema__ = nerdgraph


class Minutes(sgqlc.types.Scalar):
    """Class for Minutes.

    The `Minutes` scalar represents a duration in minutes.
    """

    __schema__ = nerdgraph


class NaiveDateTime(sgqlc.types.Scalar):
    """Class for NaiveDateTime.

    The `NaiveDateTime` scalar represents a date and time without a
    Time Zone. The `NaiveDateTime` appears as an ISO8601 formatted
    string.
    """

    __schema__ = nerdgraph


class NerdStorageDocument(sgqlc.types.Scalar):
    """Class for NerdStorageDocument.

    This scalar represents a NerdStorage document.
    """

    __schema__ = nerdgraph


class NerdpackTagName(sgqlc.types.Scalar):
    """Class for NerdpackTagName.

    A string representing a nerdpack tag.
    """

    __schema__ = nerdgraph


class Nr1CatalogRawNerdletState(sgqlc.types.Scalar):
    """Class for Nr1CatalogRawNerdletState.

    Represents JSON nerdlet state data.
    """

    __schema__ = nerdgraph


class NrdbRawResults(sgqlc.types.Scalar):
    """Class for NrdbRawResults.

    This scalar represents the raw nrql query results as returned from
    NRDB. It is a `Map` of `String` keys to values.  The shape of
    these objects reflect the query used to generate them, the
    contents of the objects is not part of the GraphQL schema.
    """

    __schema__ = nerdgraph


class NrdbResult(sgqlc.types.Scalar):
    """Class for NrdbResult.

    This scalar represents a NRDB Result. It is a `Map` of `String`
    keys to values.  The shape of these objects reflect the query used
    to generate them, the contents of the objects is not part of the
    GraphQL schema.
    """

    __schema__ = nerdgraph


class Nrql(sgqlc.types.Scalar):
    """Class for Nrql.

    This scalar represents a NRQL query string.  See the [NRQL
    Docs](https://docs.newrelic.com/docs/insights/nrql-new-relic-
    query-language/nrql-resources/nrql-syntax-components-functions)
    for more information about NRQL syntax.
    """

    __schema__ = nerdgraph


class Seconds(sgqlc.types.Scalar):
    """Class for Seconds.

    The `Seconds` scalar represents a duration in seconds.
    """

    __schema__ = nerdgraph


class SecureValue(sgqlc.types.Scalar):
    """Class for SecureValue.

    The `SecureValue` scalar represents a secure value, ie a password,
    an API key, etc.
    """

    __schema__ = nerdgraph


class SemVer(sgqlc.types.Scalar):
    """Class for SemVer.

    The `SemVer` scalar represents a version designation conforming to
    the SemVer specification.
    """

    __schema__ = nerdgraph


String = sgqlc.types.String
