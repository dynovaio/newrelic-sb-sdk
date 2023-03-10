__all__ = [
    "AgentApplicationBrowserLoader",
    "AgentApplicationSettingsBrowserLoader",
    "AgentApplicationSettingsBrowserLoaderInput",
    "AgentApplicationSettingsNetworkFilterMode",
    "AgentApplicationSettingsRecordSqlEnum",
    "AgentApplicationSettingsThresholdTypeEnum",
    "AgentApplicationSettingsTracer",
    "AgentApplicationSettingsUpdateErrorClass",
    "AgentFeaturesFilter",
    "AgentReleasesFilter",
    "AiDecisionsDecisionSortMethod",
    "AiDecisionsDecisionState",
    "AiDecisionsDecisionType",
    "AiDecisionsIncidentSelect",
    "AiDecisionsIssuePriority",
    "AiDecisionsOpinion",
    "AiDecisionsResultType",
    "AiDecisionsRuleSource",
    "AiDecisionsRuleState",
    "AiDecisionsRuleType",
    "AiDecisionsSuggestionState",
    "AiDecisionsVertexClass",
    "AiIssuesIncidentState",
    "AiIssuesIssueMutingState",
    "AiIssuesIssueState",
    "AiIssuesIssueUserAction",
    "AiIssuesPriority",
    "AiNotificationsAuthType",
    "AiNotificationsChannelFields",
    "AiNotificationsChannelStatus",
    "AiNotificationsChannelType",
    "AiNotificationsDestinationFields",
    "AiNotificationsDestinationStatus",
    "AiNotificationsDestinationType",
    "AiNotificationsErrorType",
    "AiNotificationsProduct",
    "AiNotificationsResult",
    "AiNotificationsSortOrder",
    "AiNotificationsSuggestionFilterType",
    "AiNotificationsUiComponentType",
    "AiNotificationsUiComponentValidation",
    "AiNotificationsVariableCategory",
    "AiNotificationsVariableFields",
    "AiNotificationsVariableType",
    "AiTopologyCollectorResultType",
    "AiTopologyCollectorVertexClass",
    "AiTopologyVertexClass",
    "AiWorkflowsCreateErrorType",
    "AiWorkflowsDeleteErrorType",
    "AiWorkflowsDestinationType",
    "AiWorkflowsEnrichmentType",
    "AiWorkflowsFilterType",
    "AiWorkflowsMutingRulesHandling",
    "AiWorkflowsNotificationTrigger",
    "AiWorkflowsOperator",
    "AiWorkflowsTestErrorType",
    "AiWorkflowsTestNotificationResponseStatus",
    "AiWorkflowsTestResponseStatus",
    "AiWorkflowsUpdateErrorType",
    "AlertsDayOfWeek",
    "AlertsFillOption",
    "AlertsIncidentPreference",
    "AlertsMutingRuleConditionGroupOperator",
    "AlertsMutingRuleConditionOperator",
    "AlertsMutingRuleScheduleRepeat",
    "AlertsMutingRuleStatus",
    "AlertsNotificationChannelCreateErrorType",
    "AlertsNotificationChannelDeleteErrorType",
    "AlertsNotificationChannelType",
    "AlertsNotificationChannelUpdateErrorType",
    "AlertsNotificationChannelsAddToPolicyErrorType",
    "AlertsNotificationChannelsRemoveFromPolicyErrorType",
    "AlertsNrqlBaselineDirection",
    "AlertsNrqlConditionPriority",
    "AlertsNrqlConditionTermsOperator",
    "AlertsNrqlConditionThresholdOccurrences",
    "AlertsNrqlConditionType",
    "AlertsNrqlDynamicConditionTermsOperator",
    "AlertsNrqlStaticConditionValueFunction",
    "AlertsOpsGenieDataCenterRegion",
    "AlertsSignalAggregationMethod",
    "AlertsViolationTimeLimit",
    "AlertsWebhookCustomPayloadType",
    "ApiAccessIngestKeyErrorType",
    "ApiAccessIngestKeyType",
    "ApiAccessKeyType",
    "ApiAccessUserKeyErrorType",
    "BrowserAgentInstallType",
    "ChangeTrackingDeploymentType",
    "ChartFormatType",
    "ChartImageType",
    "CloudMetricCollectionMode",
    "DashboardAddWidgetsToPageErrorType",
    "DashboardAlertSeverity",
    "DashboardCreateErrorType",
    "DashboardDeleteErrorType",
    "DashboardDeleteResultStatus",
    "DashboardEntityPermissions",
    "DashboardLiveUrlErrorType",
    "DashboardLiveUrlType",
    "DashboardPermissions",
    "DashboardUndeleteErrorType",
    "DashboardUpdateErrorType",
    "DashboardUpdatePageErrorType",
    "DashboardUpdateWidgetsInPageErrorType",
    "DashboardVariableReplacementStrategy",
    "DashboardVariableType",
    "DataDictionaryTextFormat",
    "DataManagementCategory",
    "DataManagementUnit",
    "DistributedTracingSpanAnomalyType",
    "DistributedTracingSpanClientType",
    "DistributedTracingSpanProcessBoundary",
    "EdgeComplianceTypeCode",
    "EdgeCreateSpanAttributeRuleResponseErrorType",
    "EdgeCreateTraceObserverResponseErrorType",
    "EdgeDataSourceGroupUpdateType",
    "EdgeDataSourceStatusType",
    "EdgeDeleteSpanAttributeRuleResponseErrorType",
    "EdgeDeleteTraceObserverResponseErrorType",
    "EdgeEndpointStatus",
    "EdgeEndpointType",
    "EdgeProviderRegion",
    "EdgeSpanAttributeKeyOperator",
    "EdgeSpanAttributeValueOperator",
    "EdgeTraceFilterAction",
    "EdgeTraceObserverStatus",
    "EdgeUpdateTraceObserverResponseErrorType",
    "EmbeddedChartType",
    "EntityAlertSeverity",
    "EntityCollectionType",
    "EntityDeleteErrorType",
    "EntityGoldenEventObjectId",
    "EntityGoldenGoldenMetricsErrorType",
    "EntityGoldenMetricUnit",
    "EntityInfrastructureIntegrationType",
    "EntityRelationshipEdgeDirection",
    "EntityRelationshipEdgeType",
    "EntityRelationshipType",
    "EntityRelationshipUserDefinedCreateOrReplaceErrorType",
    "EntityRelationshipUserDefinedDeleteErrorType",
    "EntitySearchCountsFacet",
    "EntitySearchQueryBuilderDomain",
    "EntitySearchQueryBuilderType",
    "EntitySearchSortCriteria",
    "EntityType",
    "ErrorsInboxAssignErrorGroupErrorType",
    "ErrorsInboxDirection",
    "ErrorsInboxErrorGroupSortOrderField",
    "ErrorsInboxErrorGroupState",
    "ErrorsInboxResourceType",
    "ErrorsInboxUpdateErrorGroupStateErrorType",
    "EventsToMetricsErrorReason",
    "HistoricalDataExportStatus",
    "IncidentIntelligenceEnvironmentConsentAccountsResult",
    "IncidentIntelligenceEnvironmentCreateEnvironmentResult",
    "IncidentIntelligenceEnvironmentCurrentEnvironmentResultReason",
    "IncidentIntelligenceEnvironmentDeleteEnvironmentResult",
    "IncidentIntelligenceEnvironmentDissentAccountsResult",
    "IncidentIntelligenceEnvironmentEnvironmentKind",
    "IncidentIntelligenceEnvironmentSupportedEnvironmentKind",
    "InstallationInstallStateType",
    "InstallationRecipeStatusType",
    "LogConfigurationsCreateDataPartitionRuleErrorType",
    "LogConfigurationsDataPartitionRuleMatchingOperator",
    "LogConfigurationsDataPartitionRuleMutationErrorType",
    "LogConfigurationsDataPartitionRuleRetentionPolicyType",
    "LogConfigurationsObfuscationMethod",
    "LogConfigurationsParsingRuleMutationErrorType",
    "MetricNormalizationCustomerRuleAction",
    "MetricNormalizationRuleAction",
    "MetricNormalizationRuleErrorType",
    "NerdStorageScope",
    "NerdStorageVaultActorScope",
    "NerdStorageVaultErrorType",
    "NerdStorageVaultResultStatus",
    "NerdpackMutationErrorType",
    "NerdpackMutationResult",
    "NerdpackRemovedTagResponseType",
    "NerdpackSubscriptionAccessType",
    "NerdpackSubscriptionModel",
    "NerdpackVersionFilterFallback",
    "Nr1CatalogAlertConditionType",
    "Nr1CatalogInstallPlanDestination",
    "Nr1CatalogInstallPlanDirectiveMode",
    "Nr1CatalogInstallPlanOperatingSystem",
    "Nr1CatalogInstallPlanTargetType",
    "Nr1CatalogInstallerType",
    "Nr1CatalogMutationResult",
    "Nr1CatalogNerdpackVisibility",
    "Nr1CatalogQuickstartAlertConditionType",
    "Nr1CatalogRenderFormat",
    "Nr1CatalogSearchComponentType",
    "Nr1CatalogSearchResultType",
    "Nr1CatalogSearchSortOption",
    "Nr1CatalogSubmitMetadataErrorType",
    "Nr1CatalogSupportLevel",
    "Nr1CatalogSupportedEntityTypesMode",
    "NrqlDropRulesAction",
    "NrqlDropRulesErrorReason",
    "OrganizationProvisioningUnit",
    "OrganizationUpdateErrorType",
    "PixieLinkPixieProjectErrorType",
    "PixieRecordPixieTosAcceptanceErrorType",
    "ReferenceEntityCreateRepositoryErrorType",
    "RegionScope",
    "ServiceLevelEventsQuerySelectFunction",
    "ServiceLevelObjectiveRollingTimeWindowUnit",
    "SortBy",
    "StreamingExportStatus",
    "SyntheticMonitorStatus",
    "SyntheticMonitorType",
    "SyntheticsDeviceOrientation",
    "SyntheticsDeviceType",
    "SyntheticsMonitorCreateErrorType",
    "SyntheticsMonitorPeriod",
    "SyntheticsMonitorStatus",
    "SyntheticsMonitorUpdateErrorType",
    "SyntheticsPrivateLocationMutationErrorType",
    "SyntheticsStepType",
    "TaggingMutationErrorType",
    "UserManagementRequestedTierName",
    "WhatsNewContentType",
    "WorkloadGroupRemainingEntitiesRuleBy",
    "WorkloadResultingGroupType",
    "WorkloadRollupStrategy",
    "WorkloadRuleThresholdType",
    "WorkloadStatusSource",
    "WorkloadStatusValue",
    "WorkloadStatusValueInput",
]


# pylint: disable=duplicate-code,unused-import,too-many-lines


import sgqlc.types
import sgqlc.types.datetime

from . import nerdgraph

__docformat__ = "markdown"


class AgentApplicationBrowserLoader(sgqlc.types.Enum):
    """Class for AgentApplicationBrowserLoader.

    Determines which browser loader will be configured. There are
    three browser loader types. They are Pro+SPA, Pro, and Lite. See
    [documentation](https://docs.newrelic.com/docs/browser/browser-
    monitoring/installation/install-browser-monitoring-agent/#agent-
    types) for further information.

    Enumeration Choices:

    * `LITE`: Lite: Gives you information about some basic page load
      timing and browser user information. Lacks the Browser Pro
      features and SPA features.
    * `NONE`: Don't use an agent.
    * `PRO`: Pro: Gives you access to the Browser Pro features. Lacks
      the functionality designed for single page app monitoring.
    * `SPA`: Pro+SPA: This is the default installed agent when you
      enable browser monitoring. Gives you access to all of the
      Browser Pro features and to Single Page App (SPA) monitoring.
      Provides detailed page timing data and the most up-to-date New
      Relic features, including distributed tracing, for all types of
      applications
    """

    __schema__ = nerdgraph
    __choices__ = ("LITE", "NONE", "PRO", "SPA")


class AgentApplicationSettingsBrowserLoader(sgqlc.types.Enum):
    """Class for AgentApplicationSettingsBrowserLoader.

    Determines which browser loader will be configured. Some allowed
    return values are specified for backwards-compatability and do not
    represent currently allowed values for new applications. See
    [documentation](https://docs.newrelic.com/docs/browser/browser-
    monitoring/installation/install-browser-monitoring-agent/#agent-
    types) for further information.

    Enumeration Choices:

    * `LITE`: Lite: Gives you information about some basic page load
      timing and browser user information. Lacks the Browser Pro
      features and SPA features.
    * `NONE`: Don't use an agent.
    * `PRO`: Pro: Gives you access to the Browser Pro features. Lacks
      the functionality designed for single page app monitoring.
    * `SPA`: Pro+SPA: This is the default installed agent when you
      enable browser monitoring. Gives you access to all of the
      Browser Pro features and to Single Page App (SPA) monitoring.
      Provides detailed page timing data and the most up-to-date New
      Relic features, including distributed tracing, for all types of
      applications.
    * `XHR`: This value is specified for backwards-compatability
    """

    __schema__ = nerdgraph
    __choices__ = ("LITE", "NONE", "PRO", "SPA", "XHR")


class AgentApplicationSettingsBrowserLoaderInput(sgqlc.types.Enum):
    """Class for AgentApplicationSettingsBrowserLoaderInput.

    We have three types of browser agents: Lite, Pro, and Pro+SPA.

    Enumeration Choices:

    * `LITE`: Lite: Gives you information about some basic page load
      timing and browser user information. Lacks the Browser Pro
      features and SPA features.
    * `NONE`: Don't use an agent.
    * `PRO`: Pro: Gives you access to the Browser Pro features. Lacks
      the functionality designed for single page app monitoring.
    * `SPA`: Pro+SPA: This is the default installed agent when you
      enable browser monitoring. Gives you access to all of the
      Browser Pro features and to Single Page App (SPA) monitoring.
      Provides detailed page timing data and the most up-to-date New
      Relic features, including distributed tracing, for all types of
      applications
    """

    __schema__ = nerdgraph
    __choices__ = ("LITE", "NONE", "PRO", "SPA")


class AgentApplicationSettingsNetworkFilterMode(sgqlc.types.Enum):
    """Class for AgentApplicationSettingsNetworkFilterMode.

    Configuration setting to apply either the show or hide strategy
    for network filtering.

    Enumeration Choices:

    * `DISABLED`: Disables both show and hide confurations.
    * `HIDE`: Use the hide list configuration.
    * `SHOW`: Use the show list configuration
    """

    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "HIDE", "SHOW")


class AgentApplicationSettingsRecordSqlEnum(sgqlc.types.Enum):
    """Class for AgentApplicationSettingsRecordSqlEnum.

    Obfuscation level for SQL queries reported in transaction trace
    nodes.  When turned on, the New Relic agent will attempt to remove
    values from SQL qeries.  For example:  ``` SELECT * FROM Table
    WHERE ssn='123-45-6789' ```  might become:  ``` SELECT * FROM
    Table WHERE ssn=? ```  This can behave differently for differnet
    applications and frameworks. Please test for your specific case.
    Note: RAW collection is not campatible with High Security mode and
    cannot be set if your agent is running in that mode.

    Enumeration Choices:

    * `OBFUSCATED`: This is the default value. This setting strips
      string literals and numeric sequences from your queries and
      replaces them with the ? character. For example: the query
      select * from table where ssn='123-45-6789' would become select
      * from table where ssn=?.
    * `OFF`: Query collection is turned off entirely.
    * `RAW`: If you are confident that full query data collection will
      not impact your data security or your users' privacy, you can
      change the setting to RAW, which will record all query values.
      NOTE: 'RAW' is not permitted when 'High security mode' is
      enabled
    """

    __schema__ = nerdgraph
    __choices__ = ("OBFUSCATED", "OFF", "RAW")


class AgentApplicationSettingsThresholdTypeEnum(sgqlc.types.Enum):
    """Class for AgentApplicationSettingsThresholdTypeEnum.

    Determines whether a threshold is statically configured or
    dynamically configured.

    Enumeration Choices:

    * `APDEX_F`: Configures the threshold to be 4 times the value of
      APDEX_T.
    * `VALUE`: Threshold will be statically configured via the
      corresponding "value" field
    """

    __schema__ = nerdgraph
    __choices__ = ("APDEX_F", "VALUE")


class AgentApplicationSettingsTracer(sgqlc.types.Enum):
    """Class for AgentApplicationSettingsTracer.

    The type of tracing being done.

    Enumeration Choices:

    * `CROSS_APPLICATION_TRACER`: Cross-application tracing feature
      enabled.
    * `DISTRIBUTED_TRACING`: Distributed tracing feature enabled.
    * `NONE`: Both cross-application and distributed tracing disabled
    """

    __schema__ = nerdgraph
    __choices__ = ("CROSS_APPLICATION_TRACER", "DISTRIBUTED_TRACING", "NONE")


class AgentApplicationSettingsUpdateErrorClass(sgqlc.types.Enum):
    """Class for AgentApplicationSettingsUpdateErrorClass.

    Categories of errors that could occur while attempting updates.

    Enumeration Choices:

    * `ACCESS_DENIED`: You are not authorized to update this field.
    * `INVALID_INPUT`: The given value for the field is not valid or
      out of range.
    * `NOT_FOUND`: No record could be found using the given input
      value
    """

    __schema__ = nerdgraph
    __choices__ = ("ACCESS_DENIED", "INVALID_INPUT", "NOT_FOUND")


class AgentFeaturesFilter(sgqlc.types.Enum):
    """Class for AgentFeaturesFilter.

    Agent Feature Filter

    Enumeration Choices:

    * `DOTNET`None
    * `ELIXIR`None
    * `GO`None
    * `HTML`None
    * `JAVA`None
    * `MOBILE`None
    * `NODEJS`None
    * `PHP`None
    * `PYTHON`None
    * `RUBY`None
    * `SDK`None
    """

    __schema__ = nerdgraph
    __choices__ = (
        "DOTNET",
        "ELIXIR",
        "GO",
        "HTML",
        "JAVA",
        "MOBILE",
        "NODEJS",
        "PHP",
        "PYTHON",
        "RUBY",
        "SDK",
    )


class AgentReleasesFilter(sgqlc.types.Enum):
    """Class for AgentReleasesFilter.

    Agent Release Filter

    Enumeration Choices:

    * `ANDROID`None
    * `BROWSER`None
    * `DOTNET`None
    * `ELIXIR`None
    * `GO`None
    * `INFRASTRUCTURE`None
    * `IOS`None
    * `JAVA`None
    * `NODEJS`None
    * `PHP`None
    * `PYTHON`None
    * `RUBY`None
    * `SDK`None
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ANDROID",
        "BROWSER",
        "DOTNET",
        "ELIXIR",
        "GO",
        "INFRASTRUCTURE",
        "IOS",
        "JAVA",
        "NODEJS",
        "PHP",
        "PYTHON",
        "RUBY",
        "SDK",
    )


class AiDecisionsDecisionSortMethod(sgqlc.types.Enum):
    """Class for AiDecisionsDecisionSortMethod.

    Sorting method for decisions.

    Enumeration Choices:

    * `ID`: Sort decisions by id
    * `LATEST_CREATED`: Sort decisions by latest_created
    * `STATE_LAST_MODIFIED`: Sort decisions by state_last_modified
    """

    __schema__ = nerdgraph
    __choices__ = ("ID", "LATEST_CREATED", "STATE_LAST_MODIFIED")


class AiDecisionsDecisionState(sgqlc.types.Enum):
    """Class for AiDecisionsDecisionState.

    State of decision.

    Enumeration Choices:

    * `DISABLED`: Decision state is disabled
    * `ENABLED`: Decision state is enabled
    """

    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "ENABLED")


class AiDecisionsDecisionType(sgqlc.types.Enum):
    """Class for AiDecisionsDecisionType.

    Type of decision

    Enumeration Choices:

    * `EXPLICIT`: Decision type is explicit
    * `GLOBAL`: Decision type is global
    * `IMPLICIT`: Decision type is implicit
    """

    __schema__ = nerdgraph
    __choices__ = ("EXPLICIT", "GLOBAL", "IMPLICIT")


class AiDecisionsIncidentSelect(sgqlc.types.Enum):
    """Class for AiDecisionsIncidentSelect.

    Select incident for comparison.

    Enumeration Choices:

    * `FIRST_INCIDENT`: Select first incident in comparison.
    * `SECOND_INCIDENT`: Select second incident in comparison
    """

    __schema__ = nerdgraph
    __choices__ = ("FIRST_INCIDENT", "SECOND_INCIDENT")


class AiDecisionsIssuePriority(sgqlc.types.Enum):
    """Class for AiDecisionsIssuePriority.

    Priority of issue.

    Enumeration Choices:

    * `CRITICAL`: Issue priority of critical
    * `HIGH`: Issue priority of high
    * `LOW`: Issue priority of low
    * `MEDIUM`: Issue priority of medium
    """

    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "HIGH", "LOW", "MEDIUM")


class AiDecisionsOpinion(sgqlc.types.Enum):
    """Class for AiDecisionsOpinion.

    Types of opinions users can leave as feedback.

    Enumeration Choices:

    * `DISLIKE`: A dislike opinion
    * `LIKE`: A like opinion
    """

    __schema__ = nerdgraph
    __choices__ = ("DISLIKE", "LIKE")


class AiDecisionsResultType(sgqlc.types.Enum):
    """Class for AiDecisionsResultType.

    Status of an operation.

    Enumeration Choices:

    * `FAILURE`: Failed operation
    * `SUCCESS`: Successful operation
    """

    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class AiDecisionsRuleSource(sgqlc.types.Enum):
    """Class for AiDecisionsRuleSource.

    Possible creation sources for rules.

    Enumeration Choices:

    * `ADMIN`: Created by ADMIN
    * `GENERATED`: Created by GENERATED
    * `SYSTEM`: Created by SYSTEM
    * `USER`: Created by USER
    """

    __schema__ = nerdgraph
    __choices__ = ("ADMIN", "GENERATED", "SYSTEM", "USER")


class AiDecisionsRuleState(sgqlc.types.Enum):
    """Class for AiDecisionsRuleState.

    State of rule.

    Enumeration Choices:

    * `DISABLED`: Rule state is disabled
    * `ENABLED`: Rule state is enabled
    """

    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "ENABLED")


class AiDecisionsRuleType(sgqlc.types.Enum):
    """Class for AiDecisionsRuleType.

    Type of rule

    Enumeration Choices:

    * `EXPLICIT`: Rule type is explicit
    * `GLOBAL`: Rule type is global
    * `IMPLICIT`: Rule type is implicit
    """

    __schema__ = nerdgraph
    __choices__ = ("EXPLICIT", "GLOBAL", "IMPLICIT")


class AiDecisionsSuggestionState(sgqlc.types.Enum):
    """Class for AiDecisionsSuggestionState.

    State of suggestion

    Enumeration Choices:

    * `ACCEPTED`: Suggestion is accepted
    * `DECLINED`: Suggestion is declined
    * `POSTPONED`: Suggestion is postponed
    * `UNDECIDED`: Suggestion is undecided
    """

    __schema__ = nerdgraph
    __choices__ = ("ACCEPTED", "DECLINED", "POSTPONED", "UNDECIDED")


class AiDecisionsVertexClass(sgqlc.types.Enum):
    """Class for AiDecisionsVertexClass.

    Class of vertex.

    Enumeration Choices:

    * `APPLICATION`: Vertex class is application
    * `CLOUDSERVICE`: Vertex class is cloudservice
    * `CLUSTER`: Vertex class is cluster
    * `DATASTORE`: Vertex class is datastore
    * `HOST`: Vertex class is host
    * `TEAM`: Vertex class is team
    """

    __schema__ = nerdgraph
    __choices__ = (
        "APPLICATION",
        "CLOUDSERVICE",
        "CLUSTER",
        "DATASTORE",
        "HOST",
        "TEAM",
    )


class AiIssuesIncidentState(sgqlc.types.Enum):
    """Class for AiIssuesIncidentState.

    Incident state

    Enumeration Choices:

    * `CLOSED`: Incident is closed
    * `CREATED`: Incident is created
    """

    __schema__ = nerdgraph
    __choices__ = ("CLOSED", "CREATED")


class AiIssuesIssueMutingState(sgqlc.types.Enum):
    """Class for AiIssuesIssueMutingState.

    Issue muting state

    Enumeration Choices:

    * `FULLY_MUTED`: Issue is muted
    * `NOT_MUTED`: Issue is not muted
    * `PARTIALLY_MUTED`: Issue is partially muted
    """

    __schema__ = nerdgraph
    __choices__ = ("FULLY_MUTED", "NOT_MUTED", "PARTIALLY_MUTED")


class AiIssuesIssueState(sgqlc.types.Enum):
    """Class for AiIssuesIssueState.

    Issue state

    Enumeration Choices:

    * `ACTIVATED`: Issue is activated
    * `CLOSED`: Issue is closed
    * `CREATED`: Issue is created
    * `DEACTIVATED`: Issue is deactivated
    """

    __schema__ = nerdgraph
    __choices__ = ("ACTIVATED", "CLOSED", "CREATED", "DEACTIVATED")


class AiIssuesIssueUserAction(sgqlc.types.Enum):
    """Class for AiIssuesIssueUserAction.

    User operations with issue

    Enumeration Choices:

    * `ACK`: Acknowledge issue
    * `RESOLVE`: Resolve issue
    * `UNACK`: Unacknowledge issue
    """

    __schema__ = nerdgraph
    __choices__ = ("ACK", "RESOLVE", "UNACK")


class AiIssuesPriority(sgqlc.types.Enum):
    """Class for AiIssuesPriority.

    Issue priority

    Enumeration Choices:

    * `CRITICAL`: Critical priority
    * `HIGH`: High priority
    * `LOW`: Low priority
    * `MEDIUM`: Medium priority
    """

    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "HIGH", "LOW", "MEDIUM")


class AiNotificationsAuthType(sgqlc.types.Enum):
    """Class for AiNotificationsAuthType.

    Authentication types

    Enumeration Choices:

    * `BASIC`: Basic user and password authentication
    * `OAUTH2`: OAuth based authentication
    * `TOKEN`: Token based authentication
    """

    __schema__ = nerdgraph
    __choices__ = ("BASIC", "OAUTH2", "TOKEN")


class AiNotificationsChannelFields(sgqlc.types.Enum):
    """Class for AiNotificationsChannelFields.

    Channel fields to filter by

    Enumeration Choices:

    * `ACTIVE`: active field
    * `CREATED_AT`: created timestamp field
    * `DEFAULT`: default field
    * `DESTINATION_ID`: destination id field
    * `NAME`: name field
    * `PRODUCT`: product field
    * `STATUS`: status field
    * `TYPE`: type field
    * `UPDATED_AT`: updated timestamp field
    * `UPDATED_BY`: updated_by field
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ACTIVE",
        "CREATED_AT",
        "DEFAULT",
        "DESTINATION_ID",
        "NAME",
        "PRODUCT",
        "STATUS",
        "TYPE",
        "UPDATED_AT",
        "UPDATED_BY",
    )


class AiNotificationsChannelStatus(sgqlc.types.Enum):
    """Class for AiNotificationsChannelStatus.

    Channel statuses

    Enumeration Choices:

    * `CONFIGURATION_ERROR`: Configuration Error channel status
    * `CONFIGURATION_WARNING`: Configuration Warning channel status
    * `DEFAULT`: Default channel status
    * `UNKNOWN_ERROR`: Unknown Error channel status
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CONFIGURATION_ERROR",
        "CONFIGURATION_WARNING",
        "DEFAULT",
        "UNKNOWN_ERROR",
    )


class AiNotificationsChannelType(sgqlc.types.Enum):
    """Class for AiNotificationsChannelType.

    Channel type

    Enumeration Choices:

    * `EMAIL`: Email channel type
    * `EVENT_BRIDGE`: Event Bridge channel type
    * `JIRA_CLASSIC`: Jira Classic channel type
    * `JIRA_NEXTGEN`: Jira Nextgen channel type
    * `MOBILE_PUSH`: Mobile push channel type
    * `PAGERDUTY_ACCOUNT_INTEGRATION`: PagerDuty channel type
    * `PAGERDUTY_SERVICE_INTEGRATION`: Pager Duty channel type
    * `SERVICENOW_EVENTS`: Servicenow events channel type
    * `SERVICENOW_INCIDENTS`: Servicenow incidents channel type
    * `SLACK`: Slack channel type
    * `SLACK_COLLABORATION`: Slack Collaboration channel type
    * `SLACK_LEGACY`: Legacy Slack channel type based on Incoming
      Webhooks
    * `WEBHOOK`: Webhook channel type
    """

    __schema__ = nerdgraph
    __choices__ = (
        "EMAIL",
        "EVENT_BRIDGE",
        "JIRA_CLASSIC",
        "JIRA_NEXTGEN",
        "MOBILE_PUSH",
        "PAGERDUTY_ACCOUNT_INTEGRATION",
        "PAGERDUTY_SERVICE_INTEGRATION",
        "SERVICENOW_EVENTS",
        "SERVICENOW_INCIDENTS",
        "SLACK",
        "SLACK_COLLABORATION",
        "SLACK_LEGACY",
        "WEBHOOK",
    )


class AiNotificationsDestinationFields(sgqlc.types.Enum):
    """Class for AiNotificationsDestinationFields.

    Destination fields

    Enumeration Choices:

    * `ACTIVE`: active field
    * `CREATED_AT`: created_at field
    * `DEFAULT`: default field
    * `LAST_SENT`: last_sent field
    * `NAME`: name field
    * `STATUS`: status field
    * `TYPE`: type field
    * `UPDATED_AT`: updated_at field
    * `UPDATED_BY`: updated_by field
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ACTIVE",
        "CREATED_AT",
        "DEFAULT",
        "LAST_SENT",
        "NAME",
        "STATUS",
        "TYPE",
        "UPDATED_AT",
        "UPDATED_BY",
    )


class AiNotificationsDestinationStatus(sgqlc.types.Enum):
    """Class for AiNotificationsDestinationStatus.

    Destination statuses

    Enumeration Choices:

    * `AUTHENTICATION_ERROR`: Authentication Error destination status
    * `AUTHORIZATION_ERROR`: Authorization Error destination status
    * `AUTHORIZATION_WARNING`: Authorization Warning destination
      status
    * `AUTH_ERROR`: Auth Error destination status
    * `CONFIGURATION_ERROR`: Configuration Error destination status
    * `DEFAULT`: Default destination status
    * `EXTERNAL_SERVER_ERROR`: External Server Error destination
      status
    * `TEMPORARY_WARNING`: Temporary Warning destination status
    * `THROTTLING_WARNING`: Throttling Warning destination status
    * `TIMEOUT_ERROR`: Timeout Error destination status
    * `UNINSTALLED`: Uninstalled destination status
    * `UNKNOWN_ERROR`: Unknown Error destination status
    """

    __schema__ = nerdgraph
    __choices__ = (
        "AUTHENTICATION_ERROR",
        "AUTHORIZATION_ERROR",
        "AUTHORIZATION_WARNING",
        "AUTH_ERROR",
        "CONFIGURATION_ERROR",
        "DEFAULT",
        "EXTERNAL_SERVER_ERROR",
        "TEMPORARY_WARNING",
        "THROTTLING_WARNING",
        "TIMEOUT_ERROR",
        "UNINSTALLED",
        "UNKNOWN_ERROR",
    )


class AiNotificationsDestinationType(sgqlc.types.Enum):
    """Class for AiNotificationsDestinationType.

    Destination types

    Enumeration Choices:

    * `EMAIL`: Email destination type
    * `EVENT_BRIDGE`: EventBridge destination type
    * `JIRA`: Jira destination type
    * `MOBILE_PUSH`: Mobile push destination type
    * `PAGERDUTY_ACCOUNT_INTEGRATION`: PagerDuty destination type
    * `PAGERDUTY_SERVICE_INTEGRATION`: PagerDuty destination type}
    * `SERVICE_NOW`: ServiceNow destination type
    * `SLACK`: Slack destination type
    * `SLACK_COLLABORATION`: Slack Collaboration destination type
    * `SLACK_LEGACY`: Legacy Slack destination type based on Incoming
      Webhooks
    * `WEBHOOK`: WebHook destination type
    """

    __schema__ = nerdgraph
    __choices__ = (
        "EMAIL",
        "EVENT_BRIDGE",
        "JIRA",
        "MOBILE_PUSH",
        "PAGERDUTY_ACCOUNT_INTEGRATION",
        "PAGERDUTY_SERVICE_INTEGRATION",
        "SERVICE_NOW",
        "SLACK",
        "SLACK_COLLABORATION",
        "SLACK_LEGACY",
        "WEBHOOK",
    )


class AiNotificationsErrorType(sgqlc.types.Enum):
    """Class for AiNotificationsErrorType.

    Error types

    Enumeration Choices:

    * `CONNECTION_ERROR`: Unable to connect to external service to
      perform this action
    * `ENTITY_IN_USE`: This operation could not be completed because
      the entity is in use
    * `EXTERNAL_SERVER_ERROR`: An external server error has occurred
    * `INVALID_CREDENTIALS`: The credentials provided were invalid,
      Please check them and try again
    * `INVALID_KEY`: Could not provide suggestions for this key
    * `INVALID_PARAMETER`: The parameter provided does not correspond
      to any valid entity
    * `LIMIT_REACHED`: Entities limit has been reached
    * `MISSING_CAPABILITIES`: User is missing capabilities
    * `MISSING_CONSTRAINTS`: This key requires additional constraints
    * `MISSING_PARAMETERS`: At least one parameter is required to
      complete this action
    * `OAUTH_NOT_SUPPORTED`: This destination does not support OAuth
      authentication
    * `SUGGESTIONS_UNAVAILABLE`: This destination does not provide any
      suggestions
    * `TIMEOUT_ERROR`: Request did not finish within time limit
    * `TYPE_EXAMPLE_MISMATCH`: The variable type is different from the
      example type
    * `UNAUTHORIZED_ACCOUNT`: This account is not allowed to perform
      this action
    * `UNEXPECTED_PARAMETER`: Received one or more unexpected
      parameters
    * `UNINSTALLED_DESTINATION`: The New Relic application was removed
    * `UNKNOWN_ERROR`: An unknown error has occurred
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CONNECTION_ERROR",
        "ENTITY_IN_USE",
        "EXTERNAL_SERVER_ERROR",
        "INVALID_CREDENTIALS",
        "INVALID_KEY",
        "INVALID_PARAMETER",
        "LIMIT_REACHED",
        "MISSING_CAPABILITIES",
        "MISSING_CONSTRAINTS",
        "MISSING_PARAMETERS",
        "OAUTH_NOT_SUPPORTED",
        "SUGGESTIONS_UNAVAILABLE",
        "TIMEOUT_ERROR",
        "TYPE_EXAMPLE_MISMATCH",
        "UNAUTHORIZED_ACCOUNT",
        "UNEXPECTED_PARAMETER",
        "UNINSTALLED_DESTINATION",
        "UNKNOWN_ERROR",
    )


class AiNotificationsProduct(sgqlc.types.Enum):
    """Class for AiNotificationsProduct.

    Product types

    Enumeration Choices:

    * `ALERTS`: Alerts product type
    * `DISCUSSIONS`: Discussions and comments product type
    * `ERROR_TRACKING`: Error Tracking product type
    * `IINT`: Incident Intelligence product type
    * `NTFC`: Notifications internal product type
    * `PD`: Proactive Detection product type
    * `SHARING`: Sharing product type
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ALERTS",
        "DISCUSSIONS",
        "ERROR_TRACKING",
        "IINT",
        "NTFC",
        "PD",
        "SHARING",
    )


class AiNotificationsResult(sgqlc.types.Enum):
    """Class for AiNotificationsResult.

    Result status

    Enumeration Choices:

    * `FAIL`: Failure
    * `SUCCESS`: Success
    """

    __schema__ = nerdgraph
    __choices__ = ("FAIL", "SUCCESS")


class AiNotificationsSortOrder(sgqlc.types.Enum):
    """Class for AiNotificationsSortOrder.

    Sort order

    Enumeration Choices:

    * `ASC`: Ascending sort order
    * `DESC`: Descending sort order
    """

    __schema__ = nerdgraph
    __choices__ = ("ASC", "DESC")


class AiNotificationsSuggestionFilterType(sgqlc.types.Enum):
    """Class for AiNotificationsSuggestionFilterType.

    Filters for the suggestions object

    Enumeration Choices:

    * `CONTAINS`: Contains specific string
    * `STARTSWITH`: Starts with a specific string
    """

    __schema__ = nerdgraph
    __choices__ = ("CONTAINS", "STARTSWITH")


class AiNotificationsUiComponentType(sgqlc.types.Enum):
    """Class for AiNotificationsUiComponentType.

    UI component type

    Enumeration Choices:

    * `DICTIONARY_WITH_MASK`: Dictionary type component
    * `PAYLOAD`: Handlebars powered payload editor
    * `SELECT`: Select component
    * `TEXT_AREA`: Multiline text box
    * `TEXT_FIELD`: Single line text field
    * `TOGGLE`: Toggle component
    """

    __schema__ = nerdgraph
    __choices__ = (
        "DICTIONARY_WITH_MASK",
        "PAYLOAD",
        "SELECT",
        "TEXT_AREA",
        "TEXT_FIELD",
        "TOGGLE",
    )


class AiNotificationsUiComponentValidation(sgqlc.types.Enum):
    """Class for AiNotificationsUiComponentValidation.

    Type of Validation required for this component

    Enumeration Choices:

    * `DATE`: Data should be a valid DATE ISO-8601 format
    * `DATETIME`: Data should be a valid DATETIME ISO-8601 format
    * `EMAIL`: Data should be a valid email
    * `JSON`: Data should be a valid JSON
    * `NONE`: No validation
    * `NUMBER`: Data should be a valid number
    * `URL`: Data should be a valid URL
    """

    __schema__ = nerdgraph
    __choices__ = ("DATE", "DATETIME", "EMAIL", "JSON", "NONE", "NUMBER", "URL")


class AiNotificationsVariableCategory(sgqlc.types.Enum):
    """Class for AiNotificationsVariableCategory.

    Category fields to group by

    Enumeration Choices:

    * `CONDITION`: Condition category
    * `ENTITIES`: Entities category
    * `INCIDENT`: Incident category
    * `ISSUE`: Issue category
    * `OTHER`: Default category
    * `POLICY`: Policy category
    * `TAGS`: Tags category
    * `WORKFLOW`: Workflow category
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CONDITION",
        "ENTITIES",
        "INCIDENT",
        "ISSUE",
        "OTHER",
        "POLICY",
        "TAGS",
        "WORKFLOW",
    )


class AiNotificationsVariableFields(sgqlc.types.Enum):
    """Class for AiNotificationsVariableFields.

    Variable fields to filter by

    Enumeration Choices:

    * `ACTIVE`: active field
    * `DEFAULT`: default field
    * `DESCRIPTION`: description field
    * `EXAMPLE`: example field
    * `KEY`: key field
    * `LABEL`: label field
    * `NAME`: name field
    * `PRODUCT`: product field
    * `TYPE`: type field
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ACTIVE",
        "DEFAULT",
        "DESCRIPTION",
        "EXAMPLE",
        "KEY",
        "LABEL",
        "NAME",
        "PRODUCT",
        "TYPE",
    )


class AiNotificationsVariableType(sgqlc.types.Enum):
    """Class for AiNotificationsVariableType.

    Variable types

    Enumeration Choices:

    * `BOOLEAN`: Boolean variable type
    * `LIST`: List variable type
    * `NUMBER`: number variable type
    * `OBJECT`: Object variable type
    * `STRING`: String variable type
    """

    __schema__ = nerdgraph
    __choices__ = ("BOOLEAN", "LIST", "NUMBER", "OBJECT", "STRING")


class AiTopologyCollectorResultType(sgqlc.types.Enum):
    """Class for AiTopologyCollectorResultType.

    Status of an operation.

    Enumeration Choices:

    * `FAILURE`: Failed operation
    * `SUCCESS`: Successful operation
    """

    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class AiTopologyCollectorVertexClass(sgqlc.types.Enum):
    """Class for AiTopologyCollectorVertexClass.

    Class of vertex.

    Enumeration Choices:

    * `APPLICATION`: Vertex class is application
    * `CLOUDSERVICE`: Vertex class is cloudservice
    * `CLUSTER`: Vertex class is cluster
    * `DATASTORE`: Vertex class is datastore
    * `HOST`: Vertex class is host
    * `TEAM`: Vertex class is team
    """

    __schema__ = nerdgraph
    __choices__ = (
        "APPLICATION",
        "CLOUDSERVICE",
        "CLUSTER",
        "DATASTORE",
        "HOST",
        "TEAM",
    )


class AiTopologyVertexClass(sgqlc.types.Enum):
    """Class for AiTopologyVertexClass.

    Class of vertex.

    Enumeration Choices:

    * `APPLICATION`: Vertex class is application
    * `CLOUDSERVICE`: Vertex class is cloudservice
    * `CLUSTER`: Vertex class is cluster
    * `DATASTORE`: Vertex class is datastore
    * `HOST`: Vertex class is host
    * `TEAM`: Vertex class is team
    """

    __schema__ = nerdgraph
    __choices__ = (
        "APPLICATION",
        "CLOUDSERVICE",
        "CLUSTER",
        "DATASTORE",
        "HOST",
        "TEAM",
    )


class AiWorkflowsCreateErrorType(sgqlc.types.Enum):
    """Class for AiWorkflowsCreateErrorType.

    Type of create error

    Enumeration Choices:

    * `CHANNEL_NOT_FOUND`: We couldn't find a channel with the given
      id
    * `DUPLICATE`: A workflow with this name already exists
    * `INVALID_PARAMETER`: One or more of the parameters you provided
      are incorrect
    * `LIMIT_REACHED`: Reached the maximum number of workflows per
      account
    * `MISSING_ENTITLEMENT`: This account is missing the required
      entitlement(s) to perform this action
    * `UNAUTHORIZED_ACCOUNT`: This account in not authorized to
      perform this action
    * `UNSUPPORTED_CHANNEL_TYPE`: The given channel id represents an
      unsupported channel type
    * `VALIDATION_ERROR`: The parameter provided does not have a valid
      form
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CHANNEL_NOT_FOUND",
        "DUPLICATE",
        "INVALID_PARAMETER",
        "LIMIT_REACHED",
        "MISSING_ENTITLEMENT",
        "UNAUTHORIZED_ACCOUNT",
        "UNSUPPORTED_CHANNEL_TYPE",
        "VALIDATION_ERROR",
    )


class AiWorkflowsDeleteErrorType(sgqlc.types.Enum):
    """Class for AiWorkflowsDeleteErrorType.

    Type of delete error

    Enumeration Choices:

    * `INVALID_PARAMETER`: One or more of the parameters you provided
      are incorrect
    * `UNAUTHORIZED_ACCOUNT`: This account in not authorized to
      perform this action
    * `VALIDATION_ERROR`: The parameter provided does not have a valid
      form
    """

    __schema__ = nerdgraph
    __choices__ = ("INVALID_PARAMETER", "UNAUTHORIZED_ACCOUNT", "VALIDATION_ERROR")


class AiWorkflowsDestinationType(sgqlc.types.Enum):
    """Class for AiWorkflowsDestinationType.

    Type of Destination Configuration

    Enumeration Choices:

    * `EMAIL`: Email Destination Configuration type
    * `EVENT_BRIDGE`: Event Bridge Destination Configuration type
    * `JIRA`: Jira Destination Configuration type
    * `PAGERDUTY_ACCOUNT_INTEGRATION`: Pager Duty with account
      integration Destination Configuration type
    * `PAGERDUTY_SERVICE_INTEGRATION`: Pager Duty with service
      integration Destination Configuration type
    * `SERVICE_NOW`: Service Now Destination Configuration type
    * `SLACK`: Slack Destination Configuration type
    * `SLACK_LEGACY`: Slack legacy Destination Configuration type
    * `WEBHOOK`: Webhook Destination Configuration type
    """

    __schema__ = nerdgraph
    __choices__ = (
        "EMAIL",
        "EVENT_BRIDGE",
        "JIRA",
        "PAGERDUTY_ACCOUNT_INTEGRATION",
        "PAGERDUTY_SERVICE_INTEGRATION",
        "SERVICE_NOW",
        "SLACK",
        "SLACK_LEGACY",
        "WEBHOOK",
    )


class AiWorkflowsEnrichmentType(sgqlc.types.Enum):
    """Class for AiWorkflowsEnrichmentType.

    Type of Enrichment

    Enumeration Choices:

    * `NRQL`: NRQL Enrichment type
    """

    __schema__ = nerdgraph
    __choices__ = ("NRQL",)


class AiWorkflowsFilterType(sgqlc.types.Enum):
    """Class for AiWorkflowsFilterType.

    Type of Filter

    Enumeration Choices:

    * `FILTER`: Standard Filter type
    * `VIEW`: View Filter type
    """

    __schema__ = nerdgraph
    __choices__ = ("FILTER", "VIEW")


class AiWorkflowsMutingRulesHandling(sgqlc.types.Enum):
    """Class for AiWorkflowsMutingRulesHandling.

    The wanted behavior for muted issues in the workflow

    Enumeration Choices:

    * `DONT_NOTIFY_FULLY_MUTED_ISSUES`: Notify only about partially
      muted and unmuted issues
    * `DONT_NOTIFY_FULLY_OR_PARTIALLY_MUTED_ISSUES`: Notify only about
      unmuted issues
    * `NOTIFY_ALL_ISSUES`: Notify about all issues
    """

    __schema__ = nerdgraph
    __choices__ = (
        "DONT_NOTIFY_FULLY_MUTED_ISSUES",
        "DONT_NOTIFY_FULLY_OR_PARTIALLY_MUTED_ISSUES",
        "NOTIFY_ALL_ISSUES",
    )


class AiWorkflowsNotificationTrigger(sgqlc.types.Enum):
    """Class for AiWorkflowsNotificationTrigger.

    Notification Triggers for the Destination Configuration

    Enumeration Choices:

    * `ACKNOWLEDGED`: Send a notification when the issue is
      acknowledged
    * `ACTIVATED`: Send a notification when the issue is activated
    * `CLOSED`: Send a notification when the issue is closed
    * `OTHER_UPDATES`: Sends notification when the issue has other
      updates
    * `PRIORITY_CHANGED`: Send a notification when the issue's
      priority has changed
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ACKNOWLEDGED",
        "ACTIVATED",
        "CLOSED",
        "OTHER_UPDATES",
        "PRIORITY_CHANGED",
    )


class AiWorkflowsOperator(sgqlc.types.Enum):
    """Class for AiWorkflowsOperator.

    Type of Filter

    Enumeration Choices:

    * `CONTAINS`: String or list attribute contains this value
    * `DOES_NOT_CONTAIN`: String or list attribute does not contain
      this value
    * `DOES_NOT_EQUAL`: String or Numeric attribute does not equal
      this value
    * `DOES_NOT_EXACTLY_MATCH`: Element in list attribute does not
      exactly match this value
    * `ENDS_WITH`: String attribute ends with this value
    * `EQUAL`: String or Numeric attribute equals this value
    * `EXACTLY_MATCHES`: Element in list attribute exactly matches
      this value
    * `GREATER_OR_EQUAL`: Numeric attribute is greater or equal to
      this value
    * `GREATER_THAN`: Numeric attribute is greater than this value
    * `IS`: Boolean attribute equals value
    * `IS_NOT`: Boolean attribute does not equal value
    * `LESS_OR_EQUAL`: Numeric attribute is less or equal to this
      value
    * `LESS_THAN`: Numeric attribute is less than this value
    * `STARTS_WITH`: String attribute starts with this value
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CONTAINS",
        "DOES_NOT_CONTAIN",
        "DOES_NOT_EQUAL",
        "DOES_NOT_EXACTLY_MATCH",
        "ENDS_WITH",
        "EQUAL",
        "EXACTLY_MATCHES",
        "GREATER_OR_EQUAL",
        "GREATER_THAN",
        "IS",
        "IS_NOT",
        "LESS_OR_EQUAL",
        "LESS_THAN",
        "STARTS_WITH",
    )


class AiWorkflowsTestErrorType(sgqlc.types.Enum):
    """Class for AiWorkflowsTestErrorType.

    Type of test error

    Enumeration Choices:

    * `CHANNEL_NOT_FOUND`: We couldn't find a channel with the given
      id
    * `FAILED_RUNNING_TEST`: Failed running test workflow
    * `MISSING_ENTITLEMENT`: This account is missing the required
      entitlement(s) to perform this action
    * `UNAUTHORIZED_ACCOUNT`: This account is not allowed to preform
      this action
    * `UNSUPPORTED_CHANNEL_TYPE`: The given channel id represents an
      unsupported channel type
    * `VALIDATION_ERROR`: The parameter provided does not have a valid
      form
    * `WARNING_FAILED_SENDING_NOTIFICATION`: Failed to send a
      notification to the channel
    * `WARNING_NO_FILTERED_ISSUE_FOUND`: There are no issues that
      match this filter
    * `WARNING_NO_MATCHING_DYNAMIC_VARIABLES_FOUND`: There are no
      issues that match these dynamic variables
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CHANNEL_NOT_FOUND",
        "FAILED_RUNNING_TEST",
        "MISSING_ENTITLEMENT",
        "UNAUTHORIZED_ACCOUNT",
        "UNSUPPORTED_CHANNEL_TYPE",
        "VALIDATION_ERROR",
        "WARNING_FAILED_SENDING_NOTIFICATION",
        "WARNING_NO_FILTERED_ISSUE_FOUND",
        "WARNING_NO_MATCHING_DYNAMIC_VARIABLES_FOUND",
    )


class AiWorkflowsTestNotificationResponseStatus(sgqlc.types.Enum):
    """Class for AiWorkflowsTestNotificationResponseStatus.

    Status of the test notification

    Enumeration Choices:

    * `FAILURE`: The test notification failed
    * `SUCCESS`: The test notification succeeded
    """

    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class AiWorkflowsTestResponseStatus(sgqlc.types.Enum):
    """Class for AiWorkflowsTestResponseStatus.

    Status of the test

    Enumeration Choices:

    * `FAILURE`: The test failed
    * `SUCCESS`: The test succeeded
    """

    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class AiWorkflowsUpdateErrorType(sgqlc.types.Enum):
    """Class for AiWorkflowsUpdateErrorType.

    Type of update error

    Enumeration Choices:

    * `CHANNEL_NOT_FOUND`: We couldn't find a channel with the given
      id
    * `DUPLICATE`: A workflow with this name already exists
    * `INVALID_PARAMETER`: One or more of the parameters you provided
      are incorrect
    * `MISSING_ENTITLEMENT`: This account is missing the required
      entitlement(s) to perform this action
    * `UNAUTHORIZED_ACCOUNT`: This account in not authorized to
      perform this action
    * `UNSUPPORTED_CHANNEL_TYPE`: The given channel id represents an
      unsupported channel type
    * `VALIDATION_ERROR`: The parameter provided does not have a valid
      form
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CHANNEL_NOT_FOUND",
        "DUPLICATE",
        "INVALID_PARAMETER",
        "MISSING_ENTITLEMENT",
        "UNAUTHORIZED_ACCOUNT",
        "UNSUPPORTED_CHANNEL_TYPE",
        "VALIDATION_ERROR",
    )


class AlertsDayOfWeek(sgqlc.types.Enum):
    """Class for AlertsDayOfWeek.

    The day of the week used to configure a WEEKLY scheduled
    MutingRule

    Enumeration Choices:

    * `FRIDAY`: Friday
    * `MONDAY`: Monday
    * `SATURDAY`: Saturday
    * `SUNDAY`: Sunday
    * `THURSDAY`: Thursday
    * `TUESDAY`: Tuesday
    * `WEDNESDAY`: Wednesday
    """

    __schema__ = nerdgraph
    __choices__ = (
        "FRIDAY",
        "MONDAY",
        "SATURDAY",
        "SUNDAY",
        "THURSDAY",
        "TUESDAY",
        "WEDNESDAY",
    )


class AlertsFillOption(sgqlc.types.Enum):
    """Class for AlertsFillOption.

    The available fill options.

    Enumeration Choices:

    * `LAST_VALUE`: Fill using the last known value.
    * `NONE`: Do not fill data.
    * `STATIC`: Fill using a static value
    """

    __schema__ = nerdgraph
    __choices__ = ("LAST_VALUE", "NONE", "STATIC")


class AlertsIncidentPreference(sgqlc.types.Enum):
    """Class for AlertsIncidentPreference.

    Determines how incidents are created for critical violations of
    the conditions contained in the policy.

    Enumeration Choices:

    * `PER_CONDITION`: A condition will create a condition-level
      incident when it violates its critical threshold. Other
      violating conditions will create their own incidents.
    * `PER_CONDITION_AND_TARGET`: Each target of each condition will
      create an entity-level incident upon critical violation. Other
      violating targets will create their own incidents (even on the
      same condition).
    * `PER_POLICY`: A condition will create a policy-level incident
      when it violates its critical threshold. Other violating
      conditions will be grouped into this incident
    """

    __schema__ = nerdgraph
    __choices__ = ("PER_CONDITION", "PER_CONDITION_AND_TARGET", "PER_POLICY")


class AlertsMutingRuleConditionGroupOperator(sgqlc.types.Enum):
    """Class for AlertsMutingRuleConditionGroupOperator.

    An operator used to combine MutingRuleConditions within a
    MutingRuleConditionGroup.

    Enumeration Choices:

    * `AND`: Match conditions by AND
    * `OR`: Match conditions by OR
    """

    __schema__ = nerdgraph
    __choices__ = ("AND", "OR")


class AlertsMutingRuleConditionOperator(sgqlc.types.Enum):
    """Class for AlertsMutingRuleConditionOperator.

    The list of operators to be used in a MutingRuleCondition. Each
    operator is limited to one value in the `values` list unless
    otherwise specified.

    Enumeration Choices:

    * `ANY`: Where attribute is any.
    * `CONTAINS`: Where attribute contains value.
    * `ENDS_WITH`: Where attribute ends with value.
    * `EQUALS`: Where attribute equals value.
    * `IN`: Where attribute in values. (Limit 500)
    * `IS_BLANK`: Where attribute is blank.
    * `IS_NOT_BLANK`: Where attribute is not blank.
    * `NOT_CONTAINS`: Where attribute does not contain value.
    * `NOT_ENDS_WITH`: Where attribute does not end with value.
    * `NOT_EQUALS`: Where attribute does not equal value.
    * `NOT_IN`: Where attribute not in values. (Limit 500)
    * `NOT_STARTS_WITH`: Where attribute does not start with value.
    * `STARTS_WITH`: Where attribute starts with value
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ANY",
        "CONTAINS",
        "ENDS_WITH",
        "EQUALS",
        "IN",
        "IS_BLANK",
        "IS_NOT_BLANK",
        "NOT_CONTAINS",
        "NOT_ENDS_WITH",
        "NOT_EQUALS",
        "NOT_IN",
        "NOT_STARTS_WITH",
        "STARTS_WITH",
    )


class AlertsMutingRuleScheduleRepeat(sgqlc.types.Enum):
    """Class for AlertsMutingRuleScheduleRepeat.

    Details about if or how frequently a MutingRule's schedule
    repeats.

    Enumeration Choices:

    * `DAILY`: Schedule repeats once per calendar day
    * `MONTHLY`: Schedule repeats once per calendar month
    * `WEEKLY`: Schedule repeats once per specified day per calendar
      week
    """

    __schema__ = nerdgraph
    __choices__ = ("DAILY", "MONTHLY", "WEEKLY")


class AlertsMutingRuleStatus(sgqlc.types.Enum):
    """Class for AlertsMutingRuleStatus.

    The status of a MutingRule based on whether it is Enabled and has
    a Schedule

    Enumeration Choices:

    * `ACTIVE`: Muting is enabled and active.
    * `ENDED`: Muting is enabled, but no longer active (there's no
      future schedule).
    * `INACTIVE`: Muting is disabled.
    * `SCHEDULED`: Muting is enabled but not active yet (there's a
      future schedule)
    """

    __schema__ = nerdgraph
    __choices__ = ("ACTIVE", "ENDED", "INACTIVE", "SCHEDULED")


class AlertsNotificationChannelCreateErrorType(sgqlc.types.Enum):
    """Class for AlertsNotificationChannelCreateErrorType.

    The error type for creating a notification channel.

    Enumeration Choices:

    * `BAD_USER_INPUT`: Bad user input error.
    * `FORBIDDEN_ERROR`: Forbidden error.
    * `SERVER_ERROR`: Server error.
    * `TOO_MANY_REQUESTS_ERROR`: Too many requests error
    """

    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNotificationChannelDeleteErrorType(sgqlc.types.Enum):
    """Class for AlertsNotificationChannelDeleteErrorType.

    The error type for deleting a notification channel.

    Enumeration Choices:

    * `BAD_USER_INPUT`: Bad user input error.
    * `FORBIDDEN_ERROR`: Forbidden error.
    * `NOT_FOUND_ERROR`: Not found error.
    * `SERVER_ERROR`: Server error.
    * `TOO_MANY_REQUESTS_ERROR`: Too many requests error
    """

    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "NOT_FOUND_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNotificationChannelType(sgqlc.types.Enum):
    """Class for AlertsNotificationChannelType.

    The type of the notification channel which determines its
    configuration field.

    Enumeration Choices:

    * `EMAIL`: Email notification channel.
    * `OPSGENIE`: OpsGenie notification channel.
    * `PAGERDUTY`: PagerDuty notification channel.
    * `SLACK`: Slack notification channel.
    * `VICTOROPS`: VictorOps notification channel.
    * `WEBHOOK`: Webhook notification channel.
    * `XMATTERS`: xMatters notification channel
    """

    __schema__ = nerdgraph
    __choices__ = (
        "EMAIL",
        "OPSGENIE",
        "PAGERDUTY",
        "SLACK",
        "VICTOROPS",
        "WEBHOOK",
        "XMATTERS",
    )


class AlertsNotificationChannelUpdateErrorType(sgqlc.types.Enum):
    """Class for AlertsNotificationChannelUpdateErrorType.

    The error type for updating a notification channel.

    Enumeration Choices:

    * `BAD_USER_INPUT`: Bad user input error.
    * `FORBIDDEN_ERROR`: Forbidden error.
    * `NOT_FOUND_ERROR`: Not found error.
    * `SERVER_ERROR`: Server error.
    * `TOO_MANY_REQUESTS_ERROR`: Too many requests error
    """

    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "NOT_FOUND_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNotificationChannelsAddToPolicyErrorType(sgqlc.types.Enum):
    """Class for AlertsNotificationChannelsAddToPolicyErrorType.

    The error type for associating notification channels with a
    policy.

    Enumeration Choices:

    * `BAD_USER_INPUT`: Bad user input error.
    * `FORBIDDEN_ERROR`: Forbidden error.
    * `NOT_FOUND_ERROR`: Not found error.
    * `SERVER_ERROR`: Server error.
    * `TOO_MANY_REQUESTS_ERROR`: Too many requests error
    """

    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "NOT_FOUND_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNotificationChannelsRemoveFromPolicyErrorType(sgqlc.types.Enum):
    """Class for AlertsNotificationChannelsRemoveFromPolicyErrorType.

    The error type for dissociating notification channels from a
    policy.

    Enumeration Choices:

    * `BAD_USER_INPUT`: Bad user input error.
    * `FORBIDDEN_ERROR`: Forbidden error.
    * `NOT_FOUND_ERROR`: Not found error.
    * `SERVER_ERROR`: Server error.
    * `TOO_MANY_REQUESTS_ERROR`: Too many requests error
    """

    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "NOT_FOUND_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNrqlBaselineDirection(sgqlc.types.Enum):
    """Class for AlertsNrqlBaselineDirection.

    Direction for a baseline NRQL condition.

    Enumeration Choices:

    * `LOWER_ONLY`: Only lower direction.
    * `UPPER_AND_LOWER`: Both upper and lower direction.
    * `UPPER_ONLY`: Only upper direction
    """

    __schema__ = nerdgraph
    __choices__ = ("LOWER_ONLY", "UPPER_AND_LOWER", "UPPER_ONLY")


class AlertsNrqlConditionPriority(sgqlc.types.Enum):
    """Class for AlertsNrqlConditionPriority.

    Value determining whether to open a critical or warning violation
    for a NrqlCondition.

    Enumeration Choices:

    * `CRITICAL`: When a critical priority violation occurs,
      notifications will be sent. The number of incidents opened and
      notifications sent depends on the incident preference defined in
      the condition's policy.
    * `WARNING`: Does not generate notifications. Use a warning
      priority when you want to monitor when a system behavior is
      concerning or noteworthy, but not important enough to require a
      notification
    """

    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "WARNING")


class AlertsNrqlConditionTermsOperator(sgqlc.types.Enum):
    """Class for AlertsNrqlConditionTermsOperator.

    Operator used to compare against the threshold for NrqlConditions.

    Enumeration Choices:

    * `ABOVE`: For comparing values above a threshold.
    * `ABOVE_OR_EQUALS`: For comparing values above or equal to a
      threshold.
    * `BELOW`: For comparing values below a threshold.
    * `BELOW_OR_EQUALS`: For comparing values below or equal to a
      threshold.
    * `EQUALS`: For comparing values equal to a threshold.
    * `NOT_EQUALS`: For comparing values that do not equal a
      threshold
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ABOVE",
        "ABOVE_OR_EQUALS",
        "BELOW",
        "BELOW_OR_EQUALS",
        "EQUALS",
        "NOT_EQUALS",
    )


class AlertsNrqlConditionThresholdOccurrences(sgqlc.types.Enum):
    """Class for AlertsNrqlConditionThresholdOccurrences.

    How many data points must be in violation for a NrqlCondition
    term's threshold duration.

    Enumeration Choices:

    * `ALL`: All points must be in violation during a term's threshold
      duration.
    * `AT_LEAST_ONCE`: At least one data point must be in violation
      during a term's threshold duration
    """

    __schema__ = nerdgraph
    __choices__ = ("ALL", "AT_LEAST_ONCE")


class AlertsNrqlConditionType(sgqlc.types.Enum):
    """Class for AlertsNrqlConditionType.

    Types of NrqlConditions.

    Enumeration Choices:

    * `BASELINE`: Baseline NrqlCondition.
    * `OUTLIER`: Outlier NrqlCondition.
    * `STATIC`: Static NrqlCondition
    """

    __schema__ = nerdgraph
    __choices__ = ("BASELINE", "OUTLIER", "STATIC")


class AlertsNrqlDynamicConditionTermsOperator(sgqlc.types.Enum):
    """Class for AlertsNrqlDynamicConditionTermsOperator.

    Operator used to compare against the threshold for
    `NrqlConditions`. Only `ABOVE` is allowed for baseline NRQL
    conditions.

    Enumeration Choices:

    * `ABOVE`: For comparing values above a threshold
    """

    __schema__ = nerdgraph
    __choices__ = ("ABOVE",)


class AlertsNrqlStaticConditionValueFunction(sgqlc.types.Enum):
    """Class for AlertsNrqlStaticConditionValueFunction.

    Deprecated.  By default, condition is evaluated based on each
    query's returned value.  To aggregate data in time "windows", use
    `signal.slideBy`.  Function used to aggregate the NRQL query
    value(s) for comparison to the `terms.threshold`. When the result
    of this aggregate surpasses the `terms.threshold`, a violation
    will be opened.

    Enumeration Choices:
    """

    __schema__ = nerdgraph
    __choices__ = ()


class AlertsOpsGenieDataCenterRegion(sgqlc.types.Enum):
    """Class for AlertsOpsGenieDataCenterRegion.

    OpsGenie data center region

    Enumeration Choices:

    * `EU`: EU data center region
    * `US`: US data center region
    """

    __schema__ = nerdgraph
    __choices__ = ("EU", "US")


class AlertsSignalAggregationMethod(sgqlc.types.Enum):
    """Class for AlertsSignalAggregationMethod.

    The method that determines when we consider an aggregation window
    to be complete so that we can evaluate the signal for violations.
    Default is `CADENCE`.

    Enumeration Choices:

    * `CADENCE`: `CADENCE` streams data points as the clocks at New
      Relic advance past the end of their window. This ensures a
      rigorous evaluation cadence, but does not take into account
      extraneous data latency.  Use in conjunction with the
      `aggregationDelay` field.
    * `EVENT_FLOW`: `EVENT_FLOW` streams data points for evaluation as
      data for newer time windows arrive. Whenever data is received,
      any data points older than the specified delay will be
      evaluated.  Use in conjunction with the `aggregationDelay`
      field.
    * `EVENT_TIMER`: `EVENT_TIMER` streams data points after the
      specified timer elapses since data last arrived for that window.
      Special measures are taken to make sure data points flow in
      order.  Use in conjunction with the `aggregationTimer` field
    """

    __schema__ = nerdgraph
    __choices__ = ("CADENCE", "EVENT_FLOW", "EVENT_TIMER")


class AlertsViolationTimeLimit(sgqlc.types.Enum):
    """Class for AlertsViolationTimeLimit.

    Duration after which a violation will automatically close.

    Enumeration Choices:

    * `EIGHT_HOURS`: Violation will close after eight hours.
    * `FOUR_HOURS`: Violation will close after four hours.
    * `NON_MATCHABLE_LIMIT_VALUE`: Time limit specified does not match
      available options.
    * `ONE_HOUR`: Violation will close after one hour.
    * `THIRTY_DAYS`: Violation will close after thirty days.
    * `TWELVE_HOURS`: Violation will close after twelve hours.
    * `TWENTY_FOUR_HOURS`: Violation will close after twenty four
      hours.
    * `TWO_HOURS`: Violation will close after two hours
    """

    __schema__ = nerdgraph
    __choices__ = (
        "EIGHT_HOURS",
        "FOUR_HOURS",
        "NON_MATCHABLE_LIMIT_VALUE",
        "ONE_HOUR",
        "THIRTY_DAYS",
        "TWELVE_HOURS",
        "TWENTY_FOUR_HOURS",
        "TWO_HOURS",
    )


class AlertsWebhookCustomPayloadType(sgqlc.types.Enum):
    """Class for AlertsWebhookCustomPayloadType.

    Webhook custom payload type

    Enumeration Choices:

    * `FORM`: FORM payload type
    * `JSON`: JSON payload type
    """

    __schema__ = nerdgraph
    __choices__ = ("FORM", "JSON")


class ApiAccessIngestKeyErrorType(sgqlc.types.Enum):
    """Class for ApiAccessIngestKeyErrorType.

    The type of error.

    Enumeration Choices:

    * `FORBIDDEN`: Occurs when the user issuing the mutation does not
      have sufficient permissions to perform the action for a key.
    * `INVALID`: Occurs when the action taken on a key did not
      successfully pass validation.
    * `NOT_FOUND`: Occurs when the requested key `id` was not found
    """

    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN", "INVALID", "NOT_FOUND")


class ApiAccessIngestKeyType(sgqlc.types.Enum):
    """Class for ApiAccessIngestKeyType.

    The type of ingest key, which dictates what types of agents can
    use it to report.

    Enumeration Choices:

    * `BROWSER`: Ingest keys of type `BROWSER` mean browser agents
      will use them to report data to New Relic.
    * `LICENSE`: For ingest keys of type `LICENSE`: APM and
      Infrastructure agents use the key to report data to New Relic
    """

    __schema__ = nerdgraph
    __choices__ = ("BROWSER", "LICENSE")


class ApiAccessKeyType(sgqlc.types.Enum):
    """Class for ApiAccessKeyType.

    The type of key.

    Enumeration Choices:

    * `INGEST`: An ingest key is used by New Relic agents to
      authenticate with New Relic and send data to the assigned
      account.
    * `USER`: A user key is used by New Relic users to authenticate
      with New Relic and to interact with the New Relic GraphQL API
    """

    __schema__ = nerdgraph
    __choices__ = ("INGEST", "USER")


class ApiAccessUserKeyErrorType(sgqlc.types.Enum):
    """Class for ApiAccessUserKeyErrorType.

    The type of error.

    Enumeration Choices:

    * `FORBIDDEN`: Occurs when the user issuing the mutation does not
      have sufficient permissions to perform the action for a key.
    * `INVALID`: Occurs when the action taken on a key did not
      successfully pass validation.
    * `NOT_FOUND`: Occurs when the requested key `id` was not found
    """

    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN", "INVALID", "NOT_FOUND")


class BrowserAgentInstallType(sgqlc.types.Enum):
    """Class for BrowserAgentInstallType.

    Browser agent install types.

    Enumeration Choices:

    * `LITE`: Lite agent install type.
    * `PRO`: Pro agent install type.
    * `PRO_SPA`: Pro + SPA agent install type
    """

    __schema__ = nerdgraph
    __choices__ = ("LITE", "PRO", "PRO_SPA")


class ChangeTrackingDeploymentType(sgqlc.types.Enum):
    """Class for ChangeTrackingDeploymentType.

    Type of deployment.

    Enumeration Choices:

    * `BASIC`: A vanilla deployment
    * `BLUE_GREEN`: Blue-green deployment
    * `CANARY`: Canary deployment
    * `OTHER`: Other types of deployment.
    * `ROLLING`: Rolling deployment.
    * `SHADOW`: Shadow deployment
    """

    __schema__ = nerdgraph
    __choices__ = ("BASIC", "BLUE_GREEN", "CANARY", "OTHER", "ROLLING", "SHADOW")


class ChartFormatType(sgqlc.types.Enum):
    """Class for ChartFormatType.

    Represents all the format types available for static charts.

    Enumeration Choices:

    * `PDF`None
    * `PNG`None
    """

    __schema__ = nerdgraph
    __choices__ = ("PDF", "PNG")


class ChartImageType(sgqlc.types.Enum):
    """Class for ChartImageType.

    Represents all the visualization types available for static
    charts.

    Enumeration Choices:

    * `APDEX`None
    * `AREA`None
    * `BAR`None
    * `BASELINE`None
    * `BILLBOARD`None
    * `BULLET`None
    * `EVENT_FEED`None
    * `FUNNEL`None
    * `HEATMAP`None
    * `HISTOGRAM`None
    * `LINE`None
    * `PIE`None
    * `SCATTER`None
    * `STACKED_HORIZONTAL_BAR`None
    * `TABLE`None
    * `VERTICAL_BAR`None
    """

    __schema__ = nerdgraph
    __choices__ = (
        "APDEX",
        "AREA",
        "BAR",
        "BASELINE",
        "BILLBOARD",
        "BULLET",
        "EVENT_FEED",
        "FUNNEL",
        "HEATMAP",
        "HISTOGRAM",
        "LINE",
        "PIE",
        "SCATTER",
        "STACKED_HORIZONTAL_BAR",
        "TABLE",
        "VERTICAL_BAR",
    )


class CloudMetricCollectionMode(sgqlc.types.Enum):
    """Class for CloudMetricCollectionMode.

    How metrics will be collected.

    Enumeration Choices:

    * `PULL`: Metrics will be pulled by NewRelic
    * `PUSH`: Metrics will be pushed by the provider
    """

    __schema__ = nerdgraph
    __choices__ = ("PULL", "PUSH")


class DashboardAddWidgetsToPageErrorType(sgqlc.types.Enum):
    """Class for DashboardAddWidgetsToPageErrorType.

    Expected error types that can be returned by addWidgetsToPage
    operation.

    Enumeration Choices:

    * `FORBIDDEN_OPERATION`: User is not allowed to execute the
      operation.
    * `INVALID_INPUT`: Invalid input error.
    * `PAGE_NOT_FOUND`: Page not found in the system
    """

    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN_OPERATION", "INVALID_INPUT", "PAGE_NOT_FOUND")


class DashboardAlertSeverity(sgqlc.types.Enum):
    """Class for DashboardAlertSeverity.

    Alert severity.

    Enumeration Choices:

    * `CRITICAL`: CRITICAL.
    * `NOT_ALERTING`: NOT_ALERTING.
    * `WARNING`: WARNING
    """

    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "NOT_ALERTING", "WARNING")


class DashboardCreateErrorType(sgqlc.types.Enum):
    """Class for DashboardCreateErrorType.

    Expected error types that can be returned by create operation.

    Enumeration Choices:

    * `INVALID_INPUT`: Invalid input error
    """

    __schema__ = nerdgraph
    __choices__ = ("INVALID_INPUT",)


class DashboardDeleteErrorType(sgqlc.types.Enum):
    """Class for DashboardDeleteErrorType.

    Expected error types that can be returned by delete operation.

    Enumeration Choices:

    * `DASHBOARD_NOT_FOUND`: Dashboard not found in the system.
    * `FORBIDDEN_OPERATION`: User is not allowed to execute the
      operation
    """

    __schema__ = nerdgraph
    __choices__ = ("DASHBOARD_NOT_FOUND", "FORBIDDEN_OPERATION")


class DashboardDeleteResultStatus(sgqlc.types.Enum):
    """Class for DashboardDeleteResultStatus.

    Result status of delete operation.

    Enumeration Choices:

    * `FAILURE`: FAILURE.
    * `SUCCESS`: SUCCESS
    """

    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class DashboardEntityPermissions(sgqlc.types.Enum):
    """Class for DashboardEntityPermissions.

    Permisions that represent visibility & editability

    Enumeration Choices:

    * `PRIVATE`: Private
    * `PUBLIC_READ_ONLY`: Public read only
    * `PUBLIC_READ_WRITE`: Public read & write
    """

    __schema__ = nerdgraph
    __choices__ = ("PRIVATE", "PUBLIC_READ_ONLY", "PUBLIC_READ_WRITE")


class DashboardLiveUrlErrorType(sgqlc.types.Enum):
    """Class for DashboardLiveUrlErrorType.

    Live URL error type.

    Enumeration Choices:

    * `OPERATION_FAILURE`: General operation failure.
    * `UNAUTHORIZED`: Unauthorized error.
    * `UNSUPPORTED`: Not supported error.
    * `URL_NOT_FOUND`: URL not found in the system
    """

    __schema__ = nerdgraph
    __choices__ = ("OPERATION_FAILURE", "UNAUTHORIZED", "UNSUPPORTED", "URL_NOT_FOUND")


class DashboardLiveUrlType(sgqlc.types.Enum):
    """Class for DashboardLiveUrlType.

    Live URL type.

    Enumeration Choices:

    * `DASHBOARD`: Dashboard.
    * `WIDGET`: Widget
    """

    __schema__ = nerdgraph
    __choices__ = ("DASHBOARD", "WIDGET")


class DashboardPermissions(sgqlc.types.Enum):
    """Class for DashboardPermissions.

    Permissions that represent visibility & editing.

    Enumeration Choices:

    * `PRIVATE`: Only you can see the dashboard. Everything but the
      metadata is hidden.
    * `PUBLIC_READ_ONLY`: All users are able to see the dashboard, but
      only you have full rights to work with the dashboard. Other
      users can access the dashboard but are not able to edit or
      delete it, although they can duplicate it.
    * `PUBLIC_READ_WRITE`: All users have full rights to the
      dashboard
    """

    __schema__ = nerdgraph
    __choices__ = ("PRIVATE", "PUBLIC_READ_ONLY", "PUBLIC_READ_WRITE")


class DashboardUndeleteErrorType(sgqlc.types.Enum):
    """Class for DashboardUndeleteErrorType.

    Expected error types that can be returned by undelete operation.

    Enumeration Choices:

    * `DASHBOARD_NOT_FOUND`: Dashboard not found in the system.
    * `FORBIDDEN_OPERATION`: User is not allowed to execute the
      operation
    """

    __schema__ = nerdgraph
    __choices__ = ("DASHBOARD_NOT_FOUND", "FORBIDDEN_OPERATION")


class DashboardUpdateErrorType(sgqlc.types.Enum):
    """Class for DashboardUpdateErrorType.

    Expected error types that can be returned by update operation.

    Enumeration Choices:

    * `FORBIDDEN_OPERATION`: User is not allowed to execute the
      operation.
    * `INVALID_INPUT`: Invalid input error
    """

    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN_OPERATION", "INVALID_INPUT")


class DashboardUpdatePageErrorType(sgqlc.types.Enum):
    """Class for DashboardUpdatePageErrorType.

    Expected error types that can be returned by updatePage operation.

    Enumeration Choices:

    * `FORBIDDEN_OPERATION`: User is not allowed to execute the
      operation.
    * `INVALID_INPUT`: Invalid input error.
    * `PAGE_NOT_FOUND`: Page not found in the system
    """

    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN_OPERATION", "INVALID_INPUT", "PAGE_NOT_FOUND")


class DashboardUpdateWidgetsInPageErrorType(sgqlc.types.Enum):
    """Class for DashboardUpdateWidgetsInPageErrorType.

    Expected error types that can be returned by updateWidgetsInPage
    operation.

    Enumeration Choices:

    * `FORBIDDEN_OPERATION`: User is not allowed to execute the
      operation.
    * `INVALID_INPUT`: Invalid input error.
    * `PAGE_NOT_FOUND`: Page not found in the system.
    * `WIDGET_NOT_FOUND`: Widget not found in the system
    """

    __schema__ = nerdgraph
    __choices__ = (
        "FORBIDDEN_OPERATION",
        "INVALID_INPUT",
        "PAGE_NOT_FOUND",
        "WIDGET_NOT_FOUND",
    )


class DashboardVariableReplacementStrategy(sgqlc.types.Enum):
    """Class for DashboardVariableReplacementStrategy.

    Possible strategies when replacing variables in a NRQL query.

    Enumeration Choices:

    * `DEFAULT`: Replace the variable based on its automatically-
      inferred type.
    * `IDENTIFIER`: Replace the variable value as an identifier.
    * `NUMBER`: Replace the variable value as a number.
    * `STRING`: Replace the variable value as a string
    """

    __schema__ = nerdgraph
    __choices__ = ("DEFAULT", "IDENTIFIER", "NUMBER", "STRING")


class DashboardVariableType(sgqlc.types.Enum):
    """Class for DashboardVariableType.

    Indicates where a variable's possible values may come from.

    Enumeration Choices:

    * `ENUM`: Value comes from an enumerated list of possible values.
    * `NRQL`: Value comes from the results of a NRQL query.
    * `STRING`: Dashboard user can supply an arbitrary string value to
      variable
    """

    __schema__ = nerdgraph
    __choices__ = ("ENUM", "NRQL", "STRING")


class DataDictionaryTextFormat(sgqlc.types.Enum):
    """Class for DataDictionaryTextFormat.

    Enumerated list of text output

    Enumeration Choices:

    * `HTML`: Text as HTML output
    * `MARKDOWN`: Text as markdown output
    * `PLAIN`: Text as plain output, stripped of markup
    """

    __schema__ = nerdgraph
    __choices__ = ("HTML", "MARKDOWN", "PLAIN")


class DataManagementCategory(sgqlc.types.Enum):
    """Class for DataManagementCategory.

    Category of a limit

    Enumeration Choices:

    * `ALERTING`: Limits on Alerting
    * `INGEST`: Limits on Ingest
    * `QUERY`: Limits on Query
    """

    __schema__ = nerdgraph
    __choices__ = ("ALERTING", "INGEST", "QUERY")


class DataManagementUnit(sgqlc.types.Enum):
    """Class for DataManagementUnit.

    Unit for a limit value

    Enumeration Choices:

    * `BYTES`: Value is in bytes
    * `COUNT`: Value is a count
    * `GIGABYTES`: Value is in gigabytes
    """

    __schema__ = nerdgraph
    __choices__ = ("BYTES", "COUNT", "GIGABYTES")


class DistributedTracingSpanAnomalyType(sgqlc.types.Enum):
    """Class for DistributedTracingSpanAnomalyType.

    The type of Span Anomaly being reported (currently only Duration
    is supported).

    Enumeration Choices:

    * `DURATION`: An anomaly type related to the duration of the span
    """

    __schema__ = nerdgraph
    __choices__ = ("DURATION",)


class DistributedTracingSpanClientType(sgqlc.types.Enum):
    """Class for DistributedTracingSpanClientType.

    Represents whether a span is a call to a datastore or an external
    service.

    Enumeration Choices:

    * `DATASTORE`: A span that represents a call to a datastore.
    * `EXTERNAL`: A span that represents a call to an external
      service
    """

    __schema__ = nerdgraph
    __choices__ = ("DATASTORE", "EXTERNAL")


class DistributedTracingSpanProcessBoundary(sgqlc.types.Enum):
    """Class for DistributedTracingSpanProcessBoundary.

    The position of a span with respect to the boundaries between
    processes in the trace.

    Enumeration Choices:

    * `ENTRY`: The first span in a process.
    * `EXIT`: A span that is the parent of an ENTRY span, or has an
      attribute name prefixed with either `db.` or `http.`, such as
      `db.statement` or `http.url`. If a span is both the first span
      in its process and has a `db.` or `http.`, its processBoundary
      value will be ENTRY.
    * `IN_PROCESS`: A span that is neither an ENTRY nor EXIT span. In-
      process spans are operations within each process, like internal
      method calls and functions
    """

    __schema__ = nerdgraph
    __choices__ = ("ENTRY", "EXIT", "IN_PROCESS")


class EdgeComplianceTypeCode(sgqlc.types.Enum):
    """Class for EdgeComplianceTypeCode.

    Compliance type codes that can be applied to a trace observer

    Enumeration Choices:

    * `FEDRAMP`: Fedramp compliant
    """

    __schema__ = nerdgraph
    __choices__ = ("FEDRAMP",)


class EdgeCreateSpanAttributeRuleResponseErrorType(sgqlc.types.Enum):
    """Class for EdgeCreateSpanAttributeRuleResponseErrorType.

    Known error codes and messages for
    `CreateSpanAttributeRuleResponseError`.

    Enumeration Choices:

    * `DUPLICATE_RULES`: Duplicate span attribute trace filter rules
      found
    * `EXCEEDS_SPAN_ATTRIBUTE_RULE_LIMITS`: The trace filter rule
      creation exceeds the number of allowed span attribute rules for
      a trace observer
    * `INVALID_INPUT`: Invalid trace filter rule input provided.
    * `NOT_FOUND`: No trace observer was found with the id given.
    * `OPPOSING_RULES`: Span attribute trace filter rules found that
      would cancel each other out
    """

    __schema__ = nerdgraph
    __choices__ = (
        "DUPLICATE_RULES",
        "EXCEEDS_SPAN_ATTRIBUTE_RULE_LIMITS",
        "INVALID_INPUT",
        "NOT_FOUND",
        "OPPOSING_RULES",
    )


class EdgeCreateTraceObserverResponseErrorType(sgqlc.types.Enum):
    """Class for EdgeCreateTraceObserverResponseErrorType.

    Known error codes and messages for
    `CreateTraceObserverResponseError`.

    Enumeration Choices:

    * `ALREADY_EXISTS`: A trace observer already exists for this
      account family and provider region.
    * `NO_AVAILABILITY_IN_REGION`: Trace observers aren’t available in
      provider region
    """

    __schema__ = nerdgraph
    __choices__ = ("ALREADY_EXISTS", "NO_AVAILABILITY_IN_REGION")


class EdgeDataSourceGroupUpdateType(sgqlc.types.Enum):
    """Class for EdgeDataSourceGroupUpdateType.

    The type of update you would like to apply to the existing data
    source group.

    Enumeration Choices:

    * `ADD`: Add the supplied entity guids to those that are currently
      active.
    * `REMOVE`: Remove the supplied entity guids from those that are
      currently active.
    * `REPLACE`: Replace the currently active entity guids with the
      ones supplied
    """

    __schema__ = nerdgraph
    __choices__ = ("ADD", "REMOVE", "REPLACE")


class EdgeDataSourceStatusType(sgqlc.types.Enum):
    """Class for EdgeDataSourceStatusType.

    The status of whether data is being sent to the trace observer for
    a particular data source.

    Enumeration Choices:

    * `ACTIVE`: The data source telemetry is being sent to this trace
      observer.
    * `INACTIVE`: The data source telemetry is *not* being sent to
      this trace observer
    """

    __schema__ = nerdgraph
    __choices__ = ("ACTIVE", "INACTIVE")


class EdgeDeleteSpanAttributeRuleResponseErrorType(sgqlc.types.Enum):
    """Class for EdgeDeleteSpanAttributeRuleResponseErrorType.

    Known error codes and messages for
    `DeleteSpanAttributeRuleResponseError`.

    Enumeration Choices:

    * `NOT_FOUND`: No trace observer was found with the id given
    """

    __schema__ = nerdgraph
    __choices__ = ("NOT_FOUND",)


class EdgeDeleteTraceObserverResponseErrorType(sgqlc.types.Enum):
    """Class for EdgeDeleteTraceObserverResponseErrorType.

    Known error codes and messages for
    `DeleteTraceObserverResponseError`.

    Enumeration Choices:

    * `ALREADY_DELETED`: The trace observer has already been deleted.
    * `NOT_FOUND`: No trace observer was found with the id given
    """

    __schema__ = nerdgraph
    __choices__ = ("ALREADY_DELETED", "NOT_FOUND")


class EdgeEndpointStatus(sgqlc.types.Enum):
    """Class for EdgeEndpointStatus.

    Status of the endpoint.

    Enumeration Choices:

    * `CREATED`: The endpoint has been created and is available for
      use.
    * `DELETED`: The endpoint has been deleted and is no longer
      available for use
    """

    __schema__ = nerdgraph
    __choices__ = ("CREATED", "DELETED")


class EdgeEndpointType(sgqlc.types.Enum):
    """Class for EdgeEndpointType.

    Type of connection established with the trace observer. Currently,
    only `PUBLIC` is supported.

    Enumeration Choices:

    * `PUBLIC`: PUBLIC: the endpoint is reachable on the internet
    """

    __schema__ = nerdgraph
    __choices__ = ("PUBLIC",)


class EdgeProviderRegion(sgqlc.types.Enum):
    """Class for EdgeProviderRegion.

    Provider and region where the trace observer is located.
    Currently, only AWS regions are supported.

    Enumeration Choices:

    * `AWS_AP_SOUTHEAST_1`: Provider: `AWS`, Region: `ap-southeast-1`
    * `AWS_AP_SOUTHEAST_2`: Provider: `AWS`, Region: `ap-southeast-2`
    * `AWS_EU_CENTRAL_1`: Provider: `AWS`, Region: `eu-central-1`
    * `AWS_EU_WEST_1`: Provider: `AWS`, Region: `eu-west-1`
    * `AWS_US_EAST_1`: Provider: `AWS`, Region: `us-east-1`
    * `AWS_US_EAST_2`: Provider: `AWS`, Region: `us-east-2`
    * `AWS_US_WEST_2`: Provider: `AWS`, Region: `us-west-2`
    """

    __schema__ = nerdgraph
    __choices__ = (
        "AWS_AP_SOUTHEAST_1",
        "AWS_AP_SOUTHEAST_2",
        "AWS_EU_CENTRAL_1",
        "AWS_EU_WEST_1",
        "AWS_US_EAST_1",
        "AWS_US_EAST_2",
        "AWS_US_WEST_2",
    )


class EdgeSpanAttributeKeyOperator(sgqlc.types.Enum):
    """Class for EdgeSpanAttributeKeyOperator.

    Span attribute key operator types

    Enumeration Choices:

    * `EQUALS`: Matches on an exact value
    * `LIKE`: Matches on a value that starts-with and/or ends-with the
      provided value
    """

    __schema__ = nerdgraph
    __choices__ = ("EQUALS", "LIKE")


class EdgeSpanAttributeValueOperator(sgqlc.types.Enum):
    """Class for EdgeSpanAttributeValueOperator.

    Span attribute value operator types

    Enumeration Choices:

    * `EQUALS`: Matches on an exact value
    * `IS_NOT_NULL`: Matches on any value
    * `LIKE`: Matches on a value that starts-with and/or ends-with the
      provided value
    """

    __schema__ = nerdgraph
    __choices__ = ("EQUALS", "IS_NOT_NULL", "LIKE")


class EdgeTraceFilterAction(sgqlc.types.Enum):
    """Class for EdgeTraceFilterAction.

    Type of action to perform when a `TraceFilter` match occurs

    Enumeration Choices:

    * `DISCARD`: Discards traces that match the filter
    * `KEEP`: Keeps traces that match the filter
    """

    __schema__ = nerdgraph
    __choices__ = ("DISCARD", "KEEP")


class EdgeTraceObserverStatus(sgqlc.types.Enum):
    """Class for EdgeTraceObserverStatus.

    Status of the trace observer.

    Enumeration Choices:

    * `CREATED`: The trace observer has been created and is available
      for use.
    * `DELETED`: The trace observer has been deleted and is no longer
      available for use
    """

    __schema__ = nerdgraph
    __choices__ = ("CREATED", "DELETED")


class EdgeUpdateTraceObserverResponseErrorType(sgqlc.types.Enum):
    """Class for EdgeUpdateTraceObserverResponseErrorType.

    Known error codes and messages for
    `UpdateTraceObserverResponseError`.

    Enumeration Choices:

    * `INVALID_INPUT`: Invalid input provided.
    * `NOT_FOUND`: No trace observer was found with the id given
    """

    __schema__ = nerdgraph
    __choices__ = ("INVALID_INPUT", "NOT_FOUND")


class EmbeddedChartType(sgqlc.types.Enum):
    """Class for EmbeddedChartType.

    Represents all the visualization types available for embedded
    charts.

    Enumeration Choices:

    * `APDEX`None
    * `AREA`None
    * `BAR`None
    * `BASELINE`None
    * `BILLBOARD`None
    * `BULLET`None
    * `EMPTY`None
    * `EVENT_FEED`None
    * `FUNNEL`None
    * `HEATMAP`None
    * `HISTOGRAM`None
    * `JSON`None
    * `LINE`None
    * `MARKDOWN`None
    * `PIE`None
    * `SCATTER`None
    * `STACKED_HORIZONTAL_BAR`None
    * `TABLE`None
    * `TRAFFIC_LIGHT`None
    * `VERTICAL_BAR`None
    """

    __schema__ = nerdgraph
    __choices__ = (
        "APDEX",
        "AREA",
        "BAR",
        "BASELINE",
        "BILLBOARD",
        "BULLET",
        "EMPTY",
        "EVENT_FEED",
        "FUNNEL",
        "HEATMAP",
        "HISTOGRAM",
        "JSON",
        "LINE",
        "MARKDOWN",
        "PIE",
        "SCATTER",
        "STACKED_HORIZONTAL_BAR",
        "TABLE",
        "TRAFFIC_LIGHT",
        "VERTICAL_BAR",
    )


class EntityAlertSeverity(sgqlc.types.Enum):
    """Class for EntityAlertSeverity.

    The alert severity of the entity.

    Enumeration Choices:

    * `CRITICAL`: Indicates an entity has a critical violation in
      progress.
    * `NOT_ALERTING`: Indicates an entity has no violations and
      therefore is not alerting.
    * `NOT_CONFIGURED`: Indicates an entity is not configured for
      alerting.
    * `WARNING`: Indicates an entity  has a warning violation in
      progress
    """

    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "NOT_ALERTING", "NOT_CONFIGURED", "WARNING")


class EntityCollectionType(sgqlc.types.Enum):
    """Class for EntityCollectionType.

    Indicates where this collection is used

    Enumeration Choices:

    * `WORKLOAD`: Collections that define the entities that belong to
      a workload
    * `WORKLOAD_STATUS_RULE_GROUP`: Collections that define the entity
      groups that are used to calculate the status of a workload
    """

    __schema__ = nerdgraph
    __choices__ = ("WORKLOAD", "WORKLOAD_STATUS_RULE_GROUP")


class EntityDeleteErrorType(sgqlc.types.Enum):
    """Class for EntityDeleteErrorType.

    List of all potential error types that an entity delete operation
    might return.

    Enumeration Choices:

    * `FORBIDDEN`: Forbidden request
    * `INTERNAL_ERROR`: Internal error
    * `INVALID_INPUT`: Invalid input
    """

    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN", "INTERNAL_ERROR", "INVALID_INPUT")


class EntityGoldenEventObjectId(sgqlc.types.Enum):
    """Class for EntityGoldenEventObjectId.

    Types of references for the default WHERE clause.

    Enumeration Choices:

    * `DOMAIN_IDS`: The WHERE clause will be done against a domainId.
    * `ENTITY_GUIDS`: The WHERE clause will be done against a GUID
    """

    __schema__ = nerdgraph
    __choices__ = ("DOMAIN_IDS", "ENTITY_GUIDS")


class EntityGoldenGoldenMetricsErrorType(sgqlc.types.Enum):
    """Class for EntityGoldenGoldenMetricsErrorType.

    An object that represents a golden metrics error

    Enumeration Choices:

    * `INVALID_CONTEXT`: The context defined in the request is not
      valid.
    * `INVALID_DOMAIN_TYPE`: The domain type defined in the request is
      not valid.
    * `INVALID_QUERY_PARAMS`: There is some parameter validation that
      has failed
    * `LIMIT_EXCEEDED`: Number of metrics defined in the requests
      exceeds the limit.
    * `NOT_AUTHORIZED`: The user does not have permissions to perform
      the operation
    """

    __schema__ = nerdgraph
    __choices__ = (
        "INVALID_CONTEXT",
        "INVALID_DOMAIN_TYPE",
        "INVALID_QUERY_PARAMS",
        "LIMIT_EXCEEDED",
        "NOT_AUTHORIZED",
    )


class EntityGoldenMetricUnit(sgqlc.types.Enum):
    """Class for EntityGoldenMetricUnit.

    The different units that can be used to express golden metrics.

    Enumeration Choices:

    * `APDEX`: Apdex (Application Performance Index).
    * `BITS`: Bits.
    * `BITS_PER_SECOND`: Bits per second.
    * `BYTES`: Bytes.
    * `BYTES_PER_SECOND`: Bytes per second.
    * `CELSIUS`: Degrees celsius.
    * `COUNT`: Count.
    * `HERTZ`: Hertz.
    * `MESSAGES_PER_SECOND`: Messages per second.
    * `MS`: Milliseconds.
    * `OPERATIONS_PER_SECOND`: Operations per second.
    * `PAGES_PER_SECOND`: Pages loaded per second.
    * `PERCENTAGE`: Percentage.
    * `REQUESTS_PER_MINUTE`: Requests received per minute.
    * `REQUESTS_PER_SECOND`: Requests received per second.
    * `SECONDS`: Seconds.
    * `TIMESTAMP`: Timestamp
    """

    __schema__ = nerdgraph
    __choices__ = (
        "APDEX",
        "BITS",
        "BITS_PER_SECOND",
        "BYTES",
        "BYTES_PER_SECOND",
        "CELSIUS",
        "COUNT",
        "HERTZ",
        "MESSAGES_PER_SECOND",
        "MS",
        "OPERATIONS_PER_SECOND",
        "PAGES_PER_SECOND",
        "PERCENTAGE",
        "REQUESTS_PER_MINUTE",
        "REQUESTS_PER_SECOND",
        "SECONDS",
        "TIMESTAMP",
    )


class EntityInfrastructureIntegrationType(sgqlc.types.Enum):
    """Class for EntityInfrastructureIntegrationType.

    The type of Infrastructure Integration

    Enumeration Choices:

    * `APACHE_SERVER`: APACHE_SERVER integration
    * `AWSELASTICSEARCHNODE`: AWSELASTICSEARCHNODE integration
    * `AWS_ALB`: AWS_ALB integration
    * `AWS_ALB_LISTENER`: AWS_ALB_LISTENER integration
    * `AWS_ALB_LISTENER_RULE`: AWS_ALB_LISTENER_RULE integration
    * `AWS_ALB_TARGET_GROUP`: AWS_ALB_TARGET_GROUP integration
    * `AWS_API_GATEWAY_API`: AWS_API_GATEWAY_API integration
    * `AWS_API_GATEWAY_RESOURCE`: AWS_API_GATEWAY_RESOURCE integration
    * `AWS_API_GATEWAY_RESOURCE_WITH_METRICS`:
      AWS_API_GATEWAY_RESOURCE_WITH_METRICS integration
    * `AWS_API_GATEWAY_STAGE`: AWS_API_GATEWAY_STAGE integration
    * `AWS_AUTO_SCALING_GROUP`: AWS_AUTO_SCALING_GROUP integration
    * `AWS_AUTO_SCALING_INSTANCE`: AWS_AUTO_SCALING_INSTANCE
      integration
    * `AWS_AUTO_SCALING_LAUNCH_CONFIGURATION`:
      AWS_AUTO_SCALING_LAUNCH_CONFIGURATION integration
    * `AWS_AUTO_SCALING_POLICY`: AWS_AUTO_SCALING_POLICY integration
    * `AWS_AUTO_SCALING_REGION_LIMIT`: AWS_AUTO_SCALING_REGION_LIMIT
      integration
    * `AWS_BILLING_ACCOUNT_COST`: AWS_BILLING_ACCOUNT_COST integration
    * `AWS_BILLING_ACCOUNT_SERVICE_COST`:
      AWS_BILLING_ACCOUNT_SERVICE_COST integration
    * `AWS_BILLING_BUDGET`: AWS_BILLING_BUDGET integration
    * `AWS_BILLING_SERVICE_COST`: AWS_BILLING_SERVICE_COST integration
    * `AWS_CLOUD_FRONT_DISTRIBUTION`: AWS_CLOUD_FRONT_DISTRIBUTION
      integration
    * `AWS_CLOUD_TRAIL`: AWS_CLOUD_TRAIL integration
    * `AWS_DYNAMO_DB_GLOBAL_SECONDARY_INDEX`:
      AWS_DYNAMO_DB_GLOBAL_SECONDARY_INDEX integration
    * `AWS_DYNAMO_DB_REGION`: AWS_DYNAMO_DB_REGION integration
    * `AWS_DYNAMO_DB_TABLE`: AWS_DYNAMO_DB_TABLE integration
    * `AWS_EBS_VOLUME`: AWS_EBS_VOLUME integration
    * `AWS_ECS_CLUSTER`: AWS_ECS_CLUSTER integration
    * `AWS_ECS_SERVICE`: AWS_ECS_SERVICE integration
    * `AWS_EFS_FILE_SYSTEM`: AWS_EFS_FILE_SYSTEM integration
    * `AWS_ELASTICSEARCH_CLUSTER`: AWS_ELASTICSEARCH_CLUSTER
      integration
    * `AWS_ELASTICSEARCH_INSTANCE`: AWS_ELASTICSEARCH_INSTANCE
      integration
    * `AWS_ELASTIC_BEANSTALK_ENVIRONMENT`:
      AWS_ELASTIC_BEANSTALK_ENVIRONMENT integration
    * `AWS_ELASTIC_BEANSTALK_INSTANCE`: AWS_ELASTIC_BEANSTALK_INSTANCE
      integration
    * `AWS_ELASTIC_MAP_REDUCE_CLUSTER`: AWS_ELASTIC_MAP_REDUCE_CLUSTER
      integration
    * `AWS_ELASTIC_MAP_REDUCE_INSTANCE`:
      AWS_ELASTIC_MAP_REDUCE_INSTANCE integration
    * `AWS_ELASTIC_MAP_REDUCE_INSTANCE_FLEET`:
      AWS_ELASTIC_MAP_REDUCE_INSTANCE_FLEET integration
    * `AWS_ELASTIC_MAP_REDUCE_INSTANCE_GROUP`:
      AWS_ELASTIC_MAP_REDUCE_INSTANCE_GROUP integration
    * `AWS_ELASTI_CACHE_MEMCACHED_CLUSTER`:
      AWS_ELASTI_CACHE_MEMCACHED_CLUSTER integration
    * `AWS_ELASTI_CACHE_MEMCACHED_NODE`:
      AWS_ELASTI_CACHE_MEMCACHED_NODE integration
    * `AWS_ELASTI_CACHE_REDIS_CLUSTER`: AWS_ELASTI_CACHE_REDIS_CLUSTER
      integration
    * `AWS_ELASTI_CACHE_REDIS_NODE`: AWS_ELASTI_CACHE_REDIS_NODE
      integration
    * `AWS_ELB`: AWS_ELB integration
    * `AWS_HEALTH_ISSUE`: AWS_HEALTH_ISSUE integration
    * `AWS_HEALTH_NOTIFICATION`: AWS_HEALTH_NOTIFICATION integration
    * `AWS_HEALTH_SCHEDULED_CHANGE`: AWS_HEALTH_SCHEDULED_CHANGE
      integration
    * `AWS_HEALTH_UNKNOWN`: AWS_HEALTH_UNKNOWN integration
    * `AWS_IAM`: AWS_IAM integration
    * `AWS_IAM_GROUP`: AWS_IAM_GROUP integration
    * `AWS_IAM_OPEN_ID_PROVIDER`: AWS_IAM_OPEN_ID_PROVIDER integration
    * `AWS_IAM_POLICY`: AWS_IAM_POLICY integration
    * `AWS_IAM_ROLE`: AWS_IAM_ROLE integration
    * `AWS_IAM_SAML_PROVIDER`: AWS_IAM_SAML_PROVIDER integration
    * `AWS_IAM_SERVER_CERTIFICATE`: AWS_IAM_SERVER_CERTIFICATE
      integration
    * `AWS_IAM_USER`: AWS_IAM_USER integration
    * `AWS_IAM_VIRTUAL_MFA_DEVICE`: AWS_IAM_VIRTUAL_MFA_DEVICE
      integration
    * `AWS_IOT_BROKER`: AWS_IOT_BROKER integration
    * `AWS_IOT_RULE`: AWS_IOT_RULE integration
    * `AWS_IOT_RULE_ACTION`: AWS_IOT_RULE_ACTION integration
    * `AWS_KINESIS_DELIVERY_STREAM`: AWS_KINESIS_DELIVERY_STREAM
      integration
    * `AWS_KINESIS_STREAM`: AWS_KINESIS_STREAM integration
    * `AWS_KINESIS_STREAM_SHARD`: AWS_KINESIS_STREAM_SHARD integration
    * `AWS_LAMBDA_AGENT_TRANSACTION`: AWS_LAMBDA_AGENT_TRANSACTION
      integration
    * `AWS_LAMBDA_AGENT_TRANSACTION_ERROR`:
      AWS_LAMBDA_AGENT_TRANSACTION_ERROR integration
    * `AWS_LAMBDA_EDGE_FUNCTION`: AWS_LAMBDA_EDGE_FUNCTION integration
    * `AWS_LAMBDA_EVENT_SOURCE_MAPPING`:
      AWS_LAMBDA_EVENT_SOURCE_MAPPING integration
    * `AWS_LAMBDA_FUNCTION`: AWS_LAMBDA_FUNCTION integration
    * `AWS_LAMBDA_FUNCTION_ALIAS`: AWS_LAMBDA_FUNCTION_ALIAS
      integration
    * `AWS_LAMBDA_OPERATION`: AWS_LAMBDA_OPERATION integration
    * `AWS_LAMBDA_REGION`: AWS_LAMBDA_REGION integration
    * `AWS_LAMBDA_SPAN`: AWS_LAMBDA_SPAN integration
    * `AWS_LAMBDA_TRACE`: AWS_LAMBDA_TRACE integration
    * `AWS_RDS_DB_CLUSTER`: AWS_RDS_DB_CLUSTER integration
    * `AWS_RDS_DB_INSTANCE`: AWS_RDS_DB_INSTANCE integration
    * `AWS_REDSHIFT_CLUSTER`: AWS_REDSHIFT_CLUSTER integration
    * `AWS_REDSHIFT_NODE`: AWS_REDSHIFT_NODE integration
    * `AWS_ROUTE53_HEALTH_CHECK`: AWS_ROUTE53_HEALTH_CHECK integration
    * `AWS_ROUTE53_ZONE`: AWS_ROUTE53_ZONE integration
    * `AWS_ROUTE53_ZONE_RECORD_SET`: AWS_ROUTE53_ZONE_RECORD_SET
      integration
    * `AWS_S3_BUCKET`: AWS_S3_BUCKET integration
    * `AWS_S3_BUCKET_REQUESTS`: AWS_S3_BUCKET_REQUESTS integration
    * `AWS_SES_CONFIGURATION_SET`: AWS_SES_CONFIGURATION_SET
      integration
    * `AWS_SES_EVENT_DESTINATION`: AWS_SES_EVENT_DESTINATION
      integration
    * `AWS_SES_RECEIPT_FILTER`: AWS_SES_RECEIPT_FILTER integration
    * `AWS_SES_RECEIPT_RULE`: AWS_SES_RECEIPT_RULE integration
    * `AWS_SES_RECEIPT_RULE_SET`: AWS_SES_RECEIPT_RULE_SET integration
    * `AWS_SES_REGION`: AWS_SES_REGION integration
    * `AWS_SNS_SUBSCRIPTION`: AWS_SNS_SUBSCRIPTION integration
    * `AWS_SNS_TOPIC`: AWS_SNS_TOPIC integration
    * `AWS_SQS_QUEUE`: AWS_SQS_QUEUE integration
    * `AWS_VPC`: AWS_VPC integration
    * `AWS_VPC_ENDPOINT`: AWS_VPC_ENDPOINT integration
    * `AWS_VPC_INTERNET_GATEWAY`: AWS_VPC_INTERNET_GATEWAY integration
    * `AWS_VPC_NAT_GATEWAY`: AWS_VPC_NAT_GATEWAY integration
    * `AWS_VPC_NETWORK_ACL`: AWS_VPC_NETWORK_ACL integration
    * `AWS_VPC_NETWORK_INTERFACE`: AWS_VPC_NETWORK_INTERFACE
      integration
    * `AWS_VPC_PEERING_CONNECTION`: AWS_VPC_PEERING_CONNECTION
      integration
    * `AWS_VPC_ROUTE_TABLE`: AWS_VPC_ROUTE_TABLE integration
    * `AWS_VPC_SECURITY_GROUP`: AWS_VPC_SECURITY_GROUP integration
    * `AWS_VPC_SUBNET`: AWS_VPC_SUBNET integration
    * `AWS_VPC_VPN_CONNECTION`: AWS_VPC_VPN_CONNECTION integration
    * `AWS_VPC_VPN_TUNNEL`: AWS_VPC_VPN_TUNNEL integration
    * `AZURE_APP_SERVICE_HOST_NAME`: AZURE_APP_SERVICE_HOST_NAME
      integration
    * `AZURE_APP_SERVICE_WEB_APP`: AZURE_APP_SERVICE_WEB_APP
      integration
    * `AZURE_COSMOS_DB_ACCOUNT`: AZURE_COSMOS_DB_ACCOUNT integration
    * `AZURE_FUNCTIONS_APP`: AZURE_FUNCTIONS_APP integration
    * `AZURE_LOAD_BALANCER`: AZURE_LOAD_BALANCER integration
    * `AZURE_LOAD_BALANCER_BACKEND`: AZURE_LOAD_BALANCER_BACKEND
      integration
    * `AZURE_LOAD_BALANCER_FRONTEND_IP`:
      AZURE_LOAD_BALANCER_FRONTEND_IP integration
    * `AZURE_LOAD_BALANCER_INBOUND_NAT_POOL`:
      AZURE_LOAD_BALANCER_INBOUND_NAT_POOL integration
    * `AZURE_LOAD_BALANCER_INBOUND_NAT_RULE`:
      AZURE_LOAD_BALANCER_INBOUND_NAT_RULE integration
    * `AZURE_LOAD_BALANCER_PROBE`: AZURE_LOAD_BALANCER_PROBE
      integration
    * `AZURE_LOAD_BALANCER_RULE`: AZURE_LOAD_BALANCER_RULE integration
    * `AZURE_MARIADB_SERVER`: AZURE_MARIADB_SERVER integration
    * `AZURE_MYSQL_SERVER`: AZURE_MYSQL_SERVER integration
    * `AZURE_POSTGRESQL_SERVER`: AZURE_POSTGRESQL_SERVER integration
    * `AZURE_REDIS_CACHE`: AZURE_REDIS_CACHE integration
    * `AZURE_REDIS_CACHE_SHARD`: AZURE_REDIS_CACHE_SHARD integration
    * `AZURE_SERVICE_BUS_NAMESPACE`: AZURE_SERVICE_BUS_NAMESPACE
      integration
    * `AZURE_SERVICE_BUS_QUEUE`: AZURE_SERVICE_BUS_QUEUE integration
    * `AZURE_SERVICE_BUS_SUBSCRIPTION`: AZURE_SERVICE_BUS_SUBSCRIPTION
      integration
    * `AZURE_SERVICE_BUS_TOPIC`: AZURE_SERVICE_BUS_TOPIC integration
    * `AZURE_SQL_DATABASE`: AZURE_SQL_DATABASE integration
    * `AZURE_SQL_ELASTIC_POOL`: AZURE_SQL_ELASTIC_POOL integration
    * `AZURE_SQL_FIREWALL`: AZURE_SQL_FIREWALL integration
    * `AZURE_SQL_REPLICATION_LINK`: AZURE_SQL_REPLICATION_LINK
      integration
    * `AZURE_SQL_RESTORE_POINT`: AZURE_SQL_RESTORE_POINT integration
    * `AZURE_SQL_SERVER`: AZURE_SQL_SERVER integration
    * `AZURE_STORAGE_ACCOUNT`: AZURE_STORAGE_ACCOUNT integration
    * `AZURE_VIRTUAL_NETWORKS`: AZURE_VIRTUAL_NETWORKS integration
    * `AZURE_VIRTUAL_NETWORKS_IP_CONFIGURATION`:
      AZURE_VIRTUAL_NETWORKS_IP_CONFIGURATION integration
    * `AZURE_VIRTUAL_NETWORKS_NETWORK_INTERFACE`:
      AZURE_VIRTUAL_NETWORKS_NETWORK_INTERFACE integration
    * `AZURE_VIRTUAL_NETWORKS_PEERING`: AZURE_VIRTUAL_NETWORKS_PEERING
      integration
    * `AZURE_VIRTUAL_NETWORKS_PUBLIC_IP_ADDRESS`:
      AZURE_VIRTUAL_NETWORKS_PUBLIC_IP_ADDRESS integration
    * `AZURE_VIRTUAL_NETWORKS_ROUTE`: AZURE_VIRTUAL_NETWORKS_ROUTE
      integration
    * `AZURE_VIRTUAL_NETWORKS_ROUTE_TABLE`:
      AZURE_VIRTUAL_NETWORKS_ROUTE_TABLE integration
    * `AZURE_VIRTUAL_NETWORKS_SECURITY_GROUP`:
      AZURE_VIRTUAL_NETWORKS_SECURITY_GROUP integration
    * `AZURE_VIRTUAL_NETWORKS_SECURITY_RULE`:
      AZURE_VIRTUAL_NETWORKS_SECURITY_RULE integration
    * `AZURE_VIRTUAL_NETWORKS_SUBNET`: AZURE_VIRTUAL_NETWORKS_SUBNET
      integration
    * `CASSANDRA_NODE`: CASSANDRA_NODE integration
    * `CONSUL_AGENT`: CONSUL_AGENT integration
    * `COUCHBASE_BUCKET`: COUCHBASE_BUCKET integration
    * `COUCHBASE_CLUSTER`: COUCHBASE_CLUSTER integration
    * `COUCHBASE_NODE`: COUCHBASE_NODE integration
    * `COUCHBASE_QUERY_ENGINE`: COUCHBASE_QUERY_ENGINE integration
    * `ELASTICSEARCH_NODE`: ELASTICSEARCH_NODE integration
    * `F5_NODE`: F5_NODE integration
    * `F5_POOL`: F5_POOL integration
    * `F5_POOL_MEMBER`: F5_POOL_MEMBER integration
    * `F5_SYSTEM`: F5_SYSTEM integration
    * `F5_VIRTUAL_SERVER`: F5_VIRTUAL_SERVER integration
    * `GCP_APP_ENGINE_SERVICE`: GCP_APP_ENGINE_SERVICE integration
    * `GCP_BIG_QUERY_DATA_SET`: GCP_BIG_QUERY_DATA_SET integration
    * `GCP_BIG_QUERY_PROJECT`: GCP_BIG_QUERY_PROJECT integration
    * `GCP_BIG_QUERY_TABLE`: GCP_BIG_QUERY_TABLE integration
    * `GCP_CLOUD_FUNCTION`: GCP_CLOUD_FUNCTION integration
    * `GCP_CLOUD_SQL`: GCP_CLOUD_SQL integration
    * `GCP_CLOUD_TASKS_QUEUE`: GCP_CLOUD_TASKS_QUEUE integration
    * `GCP_HTTP_LOAD_BALANCER`: GCP_HTTP_LOAD_BALANCER integration
    * `GCP_INTERNAL_LOAD_BALANCER`: GCP_INTERNAL_LOAD_BALANCER
      integration
    * `GCP_KUBERNETES_CONTAINER`: GCP_KUBERNETES_CONTAINER integration
    * `GCP_KUBERNETES_NODE`: GCP_KUBERNETES_NODE integration
    * `GCP_KUBERNETES_POD`: GCP_KUBERNETES_POD integration
    * `GCP_PUB_SUB_SUBSCRIPTION`: GCP_PUB_SUB_SUBSCRIPTION integration
    * `GCP_PUB_SUB_TOPIC`: GCP_PUB_SUB_TOPIC integration
    * `GCP_SPANNER_DATABASE`: GCP_SPANNER_DATABASE integration
    * `GCP_SPANNER_INSTANCE`: GCP_SPANNER_INSTANCE integration
    * `GCP_STORAGE_BUCKET`: GCP_STORAGE_BUCKET integration
    * `GCP_TCP_SSL_PROXY_LOAD_BALANCER`:
      GCP_TCP_SSL_PROXY_LOAD_BALANCER integration
    * `GCP_VIRTUAL_MACHINE_DISK`: GCP_VIRTUAL_MACHINE_DISK integration
    * `KAFKA_BROKER`: KAFKA_BROKER integration
    * `KAFKA_TOPIC`: KAFKA_TOPIC integration
    * `KUBERNETES_CLUSTER`: KUBERNETES_CLUSTER integration
    * `MEMCACHED_INSTANCE`: MEMCACHED_INSTANCE integration
    * `MSSQL_INSTANCE`: MSSQL_INSTANCE integration
    * `MYSQL_NODE`: MYSQL_NODE integration
    * `NA`: NA integration
    * `NGINX_SERVER`: NGINX_SERVER integration
    * `ORACLE_DB_INSTANCE`: ORACLE_DB_INSTANCE integration
    * `POSTGRE_SQL_INSTANCE`: POSTGRE_SQL_INSTANCE integration
    * `RABBIT_MQ_CLUSTER`: RABBIT_MQ_CLUSTER integration
    * `RABBIT_MQ_EXCHANGE`: RABBIT_MQ_EXCHANGE integration
    * `RABBIT_MQ_NODE`: RABBIT_MQ_NODE integration
    * `RABBIT_MQ_QUEUE`: RABBIT_MQ_QUEUE integration
    * `REDIS_INSTANCE`: REDIS_INSTANCE integration
    * `VARNISH_INSTANCE`: VARNISH_INSTANCE integration
    """

    __schema__ = nerdgraph
    __choices__ = (
        "APACHE_SERVER",
        "AWSELASTICSEARCHNODE",
        "AWS_ALB",
        "AWS_ALB_LISTENER",
        "AWS_ALB_LISTENER_RULE",
        "AWS_ALB_TARGET_GROUP",
        "AWS_API_GATEWAY_API",
        "AWS_API_GATEWAY_RESOURCE",
        "AWS_API_GATEWAY_RESOURCE_WITH_METRICS",
        "AWS_API_GATEWAY_STAGE",
        "AWS_AUTO_SCALING_GROUP",
        "AWS_AUTO_SCALING_INSTANCE",
        "AWS_AUTO_SCALING_LAUNCH_CONFIGURATION",
        "AWS_AUTO_SCALING_POLICY",
        "AWS_AUTO_SCALING_REGION_LIMIT",
        "AWS_BILLING_ACCOUNT_COST",
        "AWS_BILLING_ACCOUNT_SERVICE_COST",
        "AWS_BILLING_BUDGET",
        "AWS_BILLING_SERVICE_COST",
        "AWS_CLOUD_FRONT_DISTRIBUTION",
        "AWS_CLOUD_TRAIL",
        "AWS_DYNAMO_DB_GLOBAL_SECONDARY_INDEX",
        "AWS_DYNAMO_DB_REGION",
        "AWS_DYNAMO_DB_TABLE",
        "AWS_EBS_VOLUME",
        "AWS_ECS_CLUSTER",
        "AWS_ECS_SERVICE",
        "AWS_EFS_FILE_SYSTEM",
        "AWS_ELASTICSEARCH_CLUSTER",
        "AWS_ELASTICSEARCH_INSTANCE",
        "AWS_ELASTIC_BEANSTALK_ENVIRONMENT",
        "AWS_ELASTIC_BEANSTALK_INSTANCE",
        "AWS_ELASTIC_MAP_REDUCE_CLUSTER",
        "AWS_ELASTIC_MAP_REDUCE_INSTANCE",
        "AWS_ELASTIC_MAP_REDUCE_INSTANCE_FLEET",
        "AWS_ELASTIC_MAP_REDUCE_INSTANCE_GROUP",
        "AWS_ELASTI_CACHE_MEMCACHED_CLUSTER",
        "AWS_ELASTI_CACHE_MEMCACHED_NODE",
        "AWS_ELASTI_CACHE_REDIS_CLUSTER",
        "AWS_ELASTI_CACHE_REDIS_NODE",
        "AWS_ELB",
        "AWS_HEALTH_ISSUE",
        "AWS_HEALTH_NOTIFICATION",
        "AWS_HEALTH_SCHEDULED_CHANGE",
        "AWS_HEALTH_UNKNOWN",
        "AWS_IAM",
        "AWS_IAM_GROUP",
        "AWS_IAM_OPEN_ID_PROVIDER",
        "AWS_IAM_POLICY",
        "AWS_IAM_ROLE",
        "AWS_IAM_SAML_PROVIDER",
        "AWS_IAM_SERVER_CERTIFICATE",
        "AWS_IAM_USER",
        "AWS_IAM_VIRTUAL_MFA_DEVICE",
        "AWS_IOT_BROKER",
        "AWS_IOT_RULE",
        "AWS_IOT_RULE_ACTION",
        "AWS_KINESIS_DELIVERY_STREAM",
        "AWS_KINESIS_STREAM",
        "AWS_KINESIS_STREAM_SHARD",
        "AWS_LAMBDA_AGENT_TRANSACTION",
        "AWS_LAMBDA_AGENT_TRANSACTION_ERROR",
        "AWS_LAMBDA_EDGE_FUNCTION",
        "AWS_LAMBDA_EVENT_SOURCE_MAPPING",
        "AWS_LAMBDA_FUNCTION",
        "AWS_LAMBDA_FUNCTION_ALIAS",
        "AWS_LAMBDA_OPERATION",
        "AWS_LAMBDA_REGION",
        "AWS_LAMBDA_SPAN",
        "AWS_LAMBDA_TRACE",
        "AWS_RDS_DB_CLUSTER",
        "AWS_RDS_DB_INSTANCE",
        "AWS_REDSHIFT_CLUSTER",
        "AWS_REDSHIFT_NODE",
        "AWS_ROUTE53_HEALTH_CHECK",
        "AWS_ROUTE53_ZONE",
        "AWS_ROUTE53_ZONE_RECORD_SET",
        "AWS_S3_BUCKET",
        "AWS_S3_BUCKET_REQUESTS",
        "AWS_SES_CONFIGURATION_SET",
        "AWS_SES_EVENT_DESTINATION",
        "AWS_SES_RECEIPT_FILTER",
        "AWS_SES_RECEIPT_RULE",
        "AWS_SES_RECEIPT_RULE_SET",
        "AWS_SES_REGION",
        "AWS_SNS_SUBSCRIPTION",
        "AWS_SNS_TOPIC",
        "AWS_SQS_QUEUE",
        "AWS_VPC",
        "AWS_VPC_ENDPOINT",
        "AWS_VPC_INTERNET_GATEWAY",
        "AWS_VPC_NAT_GATEWAY",
        "AWS_VPC_NETWORK_ACL",
        "AWS_VPC_NETWORK_INTERFACE",
        "AWS_VPC_PEERING_CONNECTION",
        "AWS_VPC_ROUTE_TABLE",
        "AWS_VPC_SECURITY_GROUP",
        "AWS_VPC_SUBNET",
        "AWS_VPC_VPN_CONNECTION",
        "AWS_VPC_VPN_TUNNEL",
        "AZURE_APP_SERVICE_HOST_NAME",
        "AZURE_APP_SERVICE_WEB_APP",
        "AZURE_COSMOS_DB_ACCOUNT",
        "AZURE_FUNCTIONS_APP",
        "AZURE_LOAD_BALANCER",
        "AZURE_LOAD_BALANCER_BACKEND",
        "AZURE_LOAD_BALANCER_FRONTEND_IP",
        "AZURE_LOAD_BALANCER_INBOUND_NAT_POOL",
        "AZURE_LOAD_BALANCER_INBOUND_NAT_RULE",
        "AZURE_LOAD_BALANCER_PROBE",
        "AZURE_LOAD_BALANCER_RULE",
        "AZURE_MARIADB_SERVER",
        "AZURE_MYSQL_SERVER",
        "AZURE_POSTGRESQL_SERVER",
        "AZURE_REDIS_CACHE",
        "AZURE_REDIS_CACHE_SHARD",
        "AZURE_SERVICE_BUS_NAMESPACE",
        "AZURE_SERVICE_BUS_QUEUE",
        "AZURE_SERVICE_BUS_SUBSCRIPTION",
        "AZURE_SERVICE_BUS_TOPIC",
        "AZURE_SQL_DATABASE",
        "AZURE_SQL_ELASTIC_POOL",
        "AZURE_SQL_FIREWALL",
        "AZURE_SQL_REPLICATION_LINK",
        "AZURE_SQL_RESTORE_POINT",
        "AZURE_SQL_SERVER",
        "AZURE_STORAGE_ACCOUNT",
        "AZURE_VIRTUAL_NETWORKS",
        "AZURE_VIRTUAL_NETWORKS_IP_CONFIGURATION",
        "AZURE_VIRTUAL_NETWORKS_NETWORK_INTERFACE",
        "AZURE_VIRTUAL_NETWORKS_PEERING",
        "AZURE_VIRTUAL_NETWORKS_PUBLIC_IP_ADDRESS",
        "AZURE_VIRTUAL_NETWORKS_ROUTE",
        "AZURE_VIRTUAL_NETWORKS_ROUTE_TABLE",
        "AZURE_VIRTUAL_NETWORKS_SECURITY_GROUP",
        "AZURE_VIRTUAL_NETWORKS_SECURITY_RULE",
        "AZURE_VIRTUAL_NETWORKS_SUBNET",
        "CASSANDRA_NODE",
        "CONSUL_AGENT",
        "COUCHBASE_BUCKET",
        "COUCHBASE_CLUSTER",
        "COUCHBASE_NODE",
        "COUCHBASE_QUERY_ENGINE",
        "ELASTICSEARCH_NODE",
        "F5_NODE",
        "F5_POOL",
        "F5_POOL_MEMBER",
        "F5_SYSTEM",
        "F5_VIRTUAL_SERVER",
        "GCP_APP_ENGINE_SERVICE",
        "GCP_BIG_QUERY_DATA_SET",
        "GCP_BIG_QUERY_PROJECT",
        "GCP_BIG_QUERY_TABLE",
        "GCP_CLOUD_FUNCTION",
        "GCP_CLOUD_SQL",
        "GCP_CLOUD_TASKS_QUEUE",
        "GCP_HTTP_LOAD_BALANCER",
        "GCP_INTERNAL_LOAD_BALANCER",
        "GCP_KUBERNETES_CONTAINER",
        "GCP_KUBERNETES_NODE",
        "GCP_KUBERNETES_POD",
        "GCP_PUB_SUB_SUBSCRIPTION",
        "GCP_PUB_SUB_TOPIC",
        "GCP_SPANNER_DATABASE",
        "GCP_SPANNER_INSTANCE",
        "GCP_STORAGE_BUCKET",
        "GCP_TCP_SSL_PROXY_LOAD_BALANCER",
        "GCP_VIRTUAL_MACHINE_DISK",
        "KAFKA_BROKER",
        "KAFKA_TOPIC",
        "KUBERNETES_CLUSTER",
        "MEMCACHED_INSTANCE",
        "MSSQL_INSTANCE",
        "MYSQL_NODE",
        "NA",
        "NGINX_SERVER",
        "ORACLE_DB_INSTANCE",
        "POSTGRE_SQL_INSTANCE",
        "RABBIT_MQ_CLUSTER",
        "RABBIT_MQ_EXCHANGE",
        "RABBIT_MQ_NODE",
        "RABBIT_MQ_QUEUE",
        "REDIS_INSTANCE",
        "VARNISH_INSTANCE",
    )


class EntityRelationshipEdgeDirection(sgqlc.types.Enum):
    """Class for EntityRelationshipEdgeDirection.

    Values for relationship direction filter.

    Enumeration Choices:

    * `BOTH`: Traverse both inbound and outbound connections.
    * `INBOUND`: Traverse inbound connections to the source of the
      relationship.
    * `OUTBOUND`: Traverse outbound connections to the target of the
      relationship
    """

    __schema__ = nerdgraph
    __choices__ = ("BOTH", "INBOUND", "OUTBOUND")


class EntityRelationshipEdgeType(sgqlc.types.Enum):
    """Class for EntityRelationshipEdgeType.

    The type of the relationship.

    Enumeration Choices:

    * `BUILT_FROM`: The target entity contains the code for the source
      entity.
    * `CALLS`: The source entity calls the target entity.
    * `CONNECTS_TO`: The source entity has a connection to the target
      entity.
    * `CONSUMES`: The source entity consumes messages from a target
      kafka topic or other queue systems.
    * `CONTAINS`: The source entity contains the target entity.
    * `HOSTS`: The source entity hosts the target.
    * `IS`: The source and target entities are perspectives on the
      same thing.
    * `MANAGES`: The source entity manages the target, that represents
      a subsystem of the source.
    * `MEASURES`: The source entity is used to measure the target
      entity.
    * `PRODUCES`: The source entity produces messages to a target
      kafka topic or other queue systems.
    * `SERVES`: The source is an Application that serves the target
      Browser application
    """

    __schema__ = nerdgraph
    __choices__ = (
        "BUILT_FROM",
        "CALLS",
        "CONNECTS_TO",
        "CONSUMES",
        "CONTAINS",
        "HOSTS",
        "IS",
        "MANAGES",
        "MEASURES",
        "PRODUCES",
        "SERVES",
    )


class EntityRelationshipType(sgqlc.types.Enum):
    """Class for EntityRelationshipType.

    The type of the relationship.  For details, visit [our
    docs](https://docs.newrelic.com/docs/apis/graphql-
    api/tutorials/graphql-relationships-api-tutorial).

    Enumeration Choices:
    """

    __schema__ = nerdgraph
    __choices__ = ()


class EntityRelationshipUserDefinedCreateOrReplaceErrorType(sgqlc.types.Enum):
    """Class for EntityRelationshipUserDefinedCreateOrReplaceErrorType.

    The different error types for the
    entityRelationshipUserDefinedCreateOrReplace mutation.

    Enumeration Choices:

    * `LIMIT_EXCEEDED`: Number of user-defined relationships for a
      given entity has exceeded the limit (2000 relationships).
    * `NOT_ALLOWED`: The operation is not allowed.
    * `NOT_AUTHORIZED`: The user does not have permissions to perform
      the operation
    """

    __schema__ = nerdgraph
    __choices__ = ("LIMIT_EXCEEDED", "NOT_ALLOWED", "NOT_AUTHORIZED")


class EntityRelationshipUserDefinedDeleteErrorType(sgqlc.types.Enum):
    """Class for EntityRelationshipUserDefinedDeleteErrorType.

    The different error types for the
    entityRelationshipUserDefinedDelete mutation.

    Enumeration Choices:

    * `NOT_AUTHORIZED`: The user does not have permissions to perform
      the operation
    """

    __schema__ = nerdgraph
    __choices__ = ("NOT_AUTHORIZED",)


class EntitySearchCountsFacet(sgqlc.types.Enum):
    """Class for EntitySearchCountsFacet.

    Possible entity search count facets.

    Enumeration Choices:

    * `ACCOUNT_ID`: Facet by account id.
    * `ALERT_SEVERITY`: Facet by alert severity.
    * `DOMAIN`: Facet by entity domain.
    * `DOMAIN_TYPE`: Facet by entity domain and entity type.
    * `NAME`: Facet by entity name
    * `REPORTING`: Facet by reporting state.
    * `TYPE`: Facet by entity type
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ACCOUNT_ID",
        "ALERT_SEVERITY",
        "DOMAIN",
        "DOMAIN_TYPE",
        "NAME",
        "REPORTING",
        "TYPE",
    )


class EntitySearchQueryBuilderDomain(sgqlc.types.Enum):
    """Class for EntitySearchQueryBuilderDomain.

    The domain to search

    Enumeration Choices:

    * `APM`: Any APM entity
    * `BROWSER`: Any Browser entity
    * `EXT`: Any External entity
    * `INFRA`: Any Infrastructure entity
    * `MOBILE`: Any Mobile entity
    * `SYNTH`: Any Synthetics entity
    """

    __schema__ = nerdgraph
    __choices__ = ("APM", "BROWSER", "EXT", "INFRA", "MOBILE", "SYNTH")


class EntitySearchQueryBuilderType(sgqlc.types.Enum):
    """Class for EntitySearchQueryBuilderType.

    The type of entity

    Enumeration Choices:

    * `APPLICATION`: An application
    * `DASHBOARD`: A dashboard
    * `HOST`: A host
    * `MONITOR`: A monitor
    * `WORKLOAD`: A workload
    """

    __schema__ = nerdgraph
    __choices__ = ("APPLICATION", "DASHBOARD", "HOST", "MONITOR", "WORKLOAD")


class EntitySearchSortCriteria(sgqlc.types.Enum):
    """Class for EntitySearchSortCriteria.

    Possible entity sorting criteria.

    Enumeration Choices:

    * `ALERT_SEVERITY`: Sort by alert severity.
    * `DOMAIN`: Sort by entity domain.
    * `MOST_RELEVANT`: Sort by relevance. Note that these results
      can't be paginated.
    * `NAME`: Sort by entity name.
    * `REPORTING`: Sort by reporting state.
    * `TYPE`: Sort by entity type
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ALERT_SEVERITY",
        "DOMAIN",
        "MOST_RELEVANT",
        "NAME",
        "REPORTING",
        "TYPE",
    )


class EntityType(sgqlc.types.Enum):
    """Class for EntityType.

    The specific type of entity

    Enumeration Choices:

    * `APM_APPLICATION_ENTITY`: An APM Application
    * `APM_DATABASE_INSTANCE_ENTITY`: A database instance seen by an
      APM Application
    * `APM_EXTERNAL_SERVICE_ENTITY`: An external service seen by an
      APM Application
    * `BROWSER_APPLICATION_ENTITY`: A Browser Application
    * `DASHBOARD_ENTITY`: A Dashboard entity
    * `EXTERNAL_ENTITY`: An External entity. For more information
      about defining External entities, see the [open source
      documentation](https://github.com/newrelic-experimental/entity-
      synthesis-definitions).
    * `GENERIC_ENTITY`: A Generic entity with no detailed data
    * `GENERIC_INFRASTRUCTURE_ENTITY`: An Infrastructure entity
    * `INFRASTRUCTURE_AWS_LAMBDA_FUNCTION_ENTITY`: An Infrastructure
      Integration AWS Lambda Function entity
    * `INFRASTRUCTURE_HOST_ENTITY`: An Infrastructure Host entity
    * `KEY_TRANSACTION_ENTITY`: A Key Transaction entity
    * `MOBILE_APPLICATION_ENTITY`: A Mobile Application
    * `SECURE_CREDENTIAL_ENTITY`: A Secure Credential entity
    * `SYNTHETIC_MONITOR_ENTITY`: A Synthetic Monitor entity
    * `THIRD_PARTY_SERVICE_ENTITY`: A Third Party Service entity
    * `UNAVAILABLE_ENTITY`: A entity that is unavailable
    * `WORKLOAD_ENTITY`: A Workload entity
    """

    __schema__ = nerdgraph
    __choices__ = (
        "APM_APPLICATION_ENTITY",
        "APM_DATABASE_INSTANCE_ENTITY",
        "APM_EXTERNAL_SERVICE_ENTITY",
        "BROWSER_APPLICATION_ENTITY",
        "DASHBOARD_ENTITY",
        "EXTERNAL_ENTITY",
        "GENERIC_ENTITY",
        "GENERIC_INFRASTRUCTURE_ENTITY",
        "INFRASTRUCTURE_AWS_LAMBDA_FUNCTION_ENTITY",
        "INFRASTRUCTURE_HOST_ENTITY",
        "KEY_TRANSACTION_ENTITY",
        "MOBILE_APPLICATION_ENTITY",
        "SECURE_CREDENTIAL_ENTITY",
        "SYNTHETIC_MONITOR_ENTITY",
        "THIRD_PARTY_SERVICE_ENTITY",
        "UNAVAILABLE_ENTITY",
        "WORKLOAD_ENTITY",
    )


class ErrorsInboxAssignErrorGroupErrorType(sgqlc.types.Enum):
    """Class for ErrorsInboxAssignErrorGroupErrorType.

    Type of assign error group error.

    Enumeration Choices:

    * `NOT_AUTHORIZED`: The user does not have permissions to perform
      the operation
    """

    __schema__ = nerdgraph
    __choices__ = ("NOT_AUTHORIZED",)


class ErrorsInboxDirection(sgqlc.types.Enum):
    """Class for ErrorsInboxDirection.

    Sort order direction

    Enumeration Choices:

    * `DESC`: Descending sort order
    """

    __schema__ = nerdgraph
    __choices__ = ("DESC",)


class ErrorsInboxErrorGroupSortOrderField(sgqlc.types.Enum):
    """Class for ErrorsInboxErrorGroupSortOrderField.

    Sort fields

    Enumeration Choices:

    * `LAST_OCCURRENCE_IN_WINDOW`: Order by last occurrence in the
      current time window.
    * `OCCURRENCES`: Order by error group occurrences
    """

    __schema__ = nerdgraph
    __choices__ = ("LAST_OCCURRENCE_IN_WINDOW", "OCCURRENCES")


class ErrorsInboxErrorGroupState(sgqlc.types.Enum):
    """Class for ErrorsInboxErrorGroupState.

    Current state of the error group.

    Enumeration Choices:

    * `IGNORED`: Error group is ignored.
    * `RESOLVED`: Error group is resolved.
    * `UNRESOLVED`: Error group is unresolved
    """

    __schema__ = nerdgraph
    __choices__ = ("IGNORED", "RESOLVED", "UNRESOLVED")


class ErrorsInboxResourceType(sgqlc.types.Enum):
    """Class for ErrorsInboxResourceType.

    A Type of resource

    Enumeration Choices:

    * `JIRA_ISSUE`: A JIRA issue
    """

    __schema__ = nerdgraph
    __choices__ = ("JIRA_ISSUE",)


class ErrorsInboxUpdateErrorGroupStateErrorType(sgqlc.types.Enum):
    """Class for ErrorsInboxUpdateErrorGroupStateErrorType.

    Type of update error group state error.

    Enumeration Choices:

    * `NOT_AUTHORIZED`: The user does not have permissions to perform
      the operation
    """

    __schema__ = nerdgraph
    __choices__ = ("NOT_AUTHORIZED",)


class EventsToMetricsErrorReason(sgqlc.types.Enum):
    """Class for EventsToMetricsErrorReason.

    General error categories.

    Enumeration Choices:

    * `GENERAL`: Other errors.
    * `INVALID_INPUT`: Indicates some part of your submission was
      invalid.
    * `USER_NOT_AUTHORIZED`: The user attempting to submit this rule
      is not authorized to do so
    """

    __schema__ = nerdgraph
    __choices__ = ("GENERAL", "INVALID_INPUT", "USER_NOT_AUTHORIZED")


class HistoricalDataExportStatus(sgqlc.types.Enum):
    """Class for HistoricalDataExportStatus.

    Customer-facing status of an export

    Enumeration Choices:

    * `CANCELED`: Export Canceled
    * `COMPLETE_FAILED`: Export Failed
    * `COMPLETE_SUCCESS`: Export Successful
    * `IN_PROGRESS`: Export in progress
    * `UNKNOWN`: Unknown Status of this Export
    * `WAITING`: Export waiting to start
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CANCELED",
        "COMPLETE_FAILED",
        "COMPLETE_SUCCESS",
        "IN_PROGRESS",
        "UNKNOWN",
        "WAITING",
    )


class IncidentIntelligenceEnvironmentConsentAccountsResult(sgqlc.types.Enum):
    """Class for IncidentIntelligenceEnvironmentConsentAccountsResult.

    Result options for account consent marking

    Enumeration Choices:

    * `ALREADY_CONSENTED`: All of the accounts have been already
      marked with consent
    * `CONSENTED`: Accounts were consented
    * `USER_NOT_AUTHORIZED_MISSING_CAPABILITY`: The user is not
      authorized to consent due to a missing capability
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ALREADY_CONSENTED",
        "CONSENTED",
        "USER_NOT_AUTHORIZED_MISSING_CAPABILITY",
    )


class IncidentIntelligenceEnvironmentCreateEnvironmentResult(sgqlc.types.Enum):
    """Class for IncidentIntelligenceEnvironmentCreateEnvironmentResult.

    Result options for environment creation

    Enumeration Choices:

    * `ACCOUNTS_ALREADY_ASSOCIATED`: The specified associated accounts
      are already associated to other environments
    * `ACCOUNT_NOT_CONSENTED`: The account is not marked with consent
      for environment creation
    * `ACCOUNT_NOT_ENTITLED`: The account is not entitled to incident
      intelligence
    * `ACTION_UNAUTHORIZED`: Action not allowed, please contact
      support
    * `ALREADY_EXISTS`: The environment already exists and cannot be
      created again for the same parent account id tree
    * `ASSOCIATED_ACCOUNTS_NOT_AUTHORIZED`: The specified associated
      accounts are not authorized to the user
    * `CREATED`: The environment was created successfully
    * `USER_NOT_AUTHORIZED`: The user is not authorized to create an
      environment
    * `USER_NOT_AUTHORIZED_MISSING_CAPABILITY`: The user is not
      authorized to create the environment due to a missing capability
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ACCOUNTS_ALREADY_ASSOCIATED",
        "ACCOUNT_NOT_CONSENTED",
        "ACCOUNT_NOT_ENTITLED",
        "ACTION_UNAUTHORIZED",
        "ALREADY_EXISTS",
        "ASSOCIATED_ACCOUNTS_NOT_AUTHORIZED",
        "CREATED",
        "USER_NOT_AUTHORIZED",
        "USER_NOT_AUTHORIZED_MISSING_CAPABILITY",
    )


class IncidentIntelligenceEnvironmentCurrentEnvironmentResultReason(sgqlc.types.Enum):
    """Class for IncidentIntelligenceEnvironmentCurrentEnvironmentResultReason.

    Current environment result reasoning

    Enumeration Choices:

    * `CURRENT_ACCOUNT_NOT_ENTITLED`: The current account is not
      entitled for incident intelligence
    * `ENVIRONMENT_FOUND`: The user is attached to an environment
    * `MULTIPLE_ENVIRONMENTS`: The user is attached to more than one
      environment, hence the user is authorized to more then one
      parent account that has an environment. To get a list of
      possible environments, query authorizedEnvironment and select
      one of the accounts.
    * `NO_ENVIRONMENT`: The user is not attached to any environment
    * `USER_NOT_AUTHORIZED_FOR_ACCOUNT`: The user is not authorized to
      access environments from the current account
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CURRENT_ACCOUNT_NOT_ENTITLED",
        "ENVIRONMENT_FOUND",
        "MULTIPLE_ENVIRONMENTS",
        "NO_ENVIRONMENT",
        "USER_NOT_AUTHORIZED_FOR_ACCOUNT",
    )


class IncidentIntelligenceEnvironmentDeleteEnvironmentResult(sgqlc.types.Enum):
    """Class for IncidentIntelligenceEnvironmentDeleteEnvironmentResult.

    Result options for environment deletion

    Enumeration Choices:

    * `ACCOUNT_NOT_ENTITLED`: The account is not entitled to incident
      intelligence
    * `DELETED`: The environment was deleted successfully
    * `DOES_NOT_EXIST`: The environment does not exists and cannot be
      deleted
    * `USER_NOT_AUTHORIZED`: The user is not authorized to delete an
      environment
    * `USER_NOT_AUTHORIZED_MISSING_CAPABILITY`: The user is not
      authorized to delete the environment due to a missing capability
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ACCOUNT_NOT_ENTITLED",
        "DELETED",
        "DOES_NOT_EXIST",
        "USER_NOT_AUTHORIZED",
        "USER_NOT_AUTHORIZED_MISSING_CAPABILITY",
    )


class IncidentIntelligenceEnvironmentDissentAccountsResult(sgqlc.types.Enum):
    """Class for IncidentIntelligenceEnvironmentDissentAccountsResult.

    Result options for account consent marking

    Enumeration Choices:

    * `CONSENTED_ACCOUNTS_NOT_FOUND`: There are no accounts authorized
      by the user that are consented for Incident Intelligence usage
    * `DISSENTED`: Accounts were dissented
    * `USER_NOT_AUTHORIZED_MISSING_CAPABILITY`: The user is not
      authorized to dissent due to a missing capability
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CONSENTED_ACCOUNTS_NOT_FOUND",
        "DISSENTED",
        "USER_NOT_AUTHORIZED_MISSING_CAPABILITY",
    )


class IncidentIntelligenceEnvironmentEnvironmentKind(sgqlc.types.Enum):
    """Class for IncidentIntelligenceEnvironmentEnvironmentKind.

    Incident Intelligence environment kinds

    Enumeration Choices:

    * `CROSS_ACCOUNT_ENVIRONMENT`: The environment can contain more
      than one account so that cross-account correlation between
      accounts is supported
    * `SINGLE_ACCOUNT_ENVIRONMENT`: The environment only contains a
      single account
    """

    __schema__ = nerdgraph
    __choices__ = ("CROSS_ACCOUNT_ENVIRONMENT", "SINGLE_ACCOUNT_ENVIRONMENT")


class IncidentIntelligenceEnvironmentSupportedEnvironmentKind(sgqlc.types.Enum):
    """Class for IncidentIntelligenceEnvironmentSupportedEnvironmentKind.

    Which environment kinds the request will provide

    Enumeration Choices:

    * `CROSS_ACCOUNT`: Will return environments that are cross account
      (based on the parent-account and sub-account)
    * `SINGLE_AND_CROSS_ACCOUNT`: Will return environments that are
      cross account (based on the parent-account and sub-account) and
      single accounts
    """

    __schema__ = nerdgraph
    __choices__ = ("CROSS_ACCOUNT", "SINGLE_AND_CROSS_ACCOUNT")


class InstallationInstallStateType(sgqlc.types.Enum):
    """Class for InstallationInstallStateType.

    An enum that represent the installation state.

    Enumeration Choices:

    * `COMPLETED`: Defines a completed installation.
    * `STARTED`: Defines an installation that has been started
    """

    __schema__ = nerdgraph
    __choices__ = ("COMPLETED", "STARTED")


class InstallationRecipeStatusType(sgqlc.types.Enum):
    """Class for InstallationRecipeStatusType.

    An enum that represents the various recipe statuses.

    Enumeration Choices:

    * `AVAILABLE`: Defines an available recipe when attempting to
      install.
    * `CANCELED`: Defines a canceled recipe when attempting to
      install.
    * `DETECTED`: Defines when New Relic instrumentation compatibility
      is detected.
    * `FAILED`: Defines a recipe that has failed during installation.
    * `INSTALLED`: Defines a recipe that has been installed.
    * `INSTALLING`: Defines a recipe currently being installed.
    * `RECOMMENDED`: Defines a recipe that has been recommended during
      installation.
    * `SKIPPED`: Defines a recipe that has been skipped during
      installation.
    * `UNSUPPORTED`: Defines a recipe that is unsupported
    """

    __schema__ = nerdgraph
    __choices__ = (
        "AVAILABLE",
        "CANCELED",
        "DETECTED",
        "FAILED",
        "INSTALLED",
        "INSTALLING",
        "RECOMMENDED",
        "SKIPPED",
        "UNSUPPORTED",
    )


class LogConfigurationsCreateDataPartitionRuleErrorType(sgqlc.types.Enum):
    """Class for LogConfigurationsCreateDataPartitionRuleErrorType.

    Expected error types as result of creating a new data partition
    rule.

    Enumeration Choices:

    * `DUPLICATE_DATA_PARTITION_RULE_NAME`: A data partition rule with
      the provided name already exists.
    * `INVALID_DATA_PARTITION_INPUT`: The provided data partition does
      not match the validation requirements
    * `MAX_DATA_PARTITION_RULES`: Customer has reached the maximum
      number of allowed data partition rules
    """

    __schema__ = nerdgraph
    __choices__ = (
        "DUPLICATE_DATA_PARTITION_RULE_NAME",
        "INVALID_DATA_PARTITION_INPUT",
        "MAX_DATA_PARTITION_RULES",
    )


class LogConfigurationsDataPartitionRuleMatchingOperator(sgqlc.types.Enum):
    """Class for LogConfigurationsDataPartitionRuleMatchingOperator.

    The matching method for the rule to allocate the data partition
    data. Select EQUALS to target logs that match your criteria
    exactly, or select LIKE to apply a fuzzy match.

    Enumeration Choices:

    * `EQUALS`: When applying the rule will allocate data for those
      attributes that are an exact match with the provided value.
    * `LIKE`: When applying the rule will allocate data for those
      attributes that contain the provided value
    """

    __schema__ = nerdgraph
    __choices__ = ("EQUALS", "LIKE")


class LogConfigurationsDataPartitionRuleMutationErrorType(sgqlc.types.Enum):
    """Class for LogConfigurationsDataPartitionRuleMutationErrorType.

    Expected default error types as result of mutating an existing
    data partition rule.

    Enumeration Choices:

    * `INVALID_ID`: Number format error. ID should be convertible to
      int.
    * `INVALID_RULE`: Partition rule must be specified with a valid
      nrql where clause
    * `NOT_FOUND`: Couldn't find the provided data partition rule
    """

    __schema__ = nerdgraph
    __choices__ = ("INVALID_ID", "INVALID_RULE", "NOT_FOUND")


class LogConfigurationsDataPartitionRuleRetentionPolicyType(sgqlc.types.Enum):
    """Class for LogConfigurationsDataPartitionRuleRetentionPolicyType.

    The retention policy for the data partition data.

    Enumeration Choices:

    * `SECONDARY`: The alternative data retention policy, 30 days of
      data retention since the log data is ingested.
    * `STANDARD`: The maximum retention period associated with the
      account. This is determined by the customer’s
      subscription/contract with New Relic
    """

    __schema__ = nerdgraph
    __choices__ = ("SECONDARY", "STANDARD")


class LogConfigurationsObfuscationMethod(sgqlc.types.Enum):
    """Class for LogConfigurationsObfuscationMethod.

    Methods for replacing obfuscated values.

    Enumeration Choices:

    * `HASH_SHA256`: Replace the matched data with a SHA256 hash.
    * `MASK`: Replace the matched data with a static value
    """

    __schema__ = nerdgraph
    __choices__ = ("HASH_SHA256", "MASK")


class LogConfigurationsParsingRuleMutationErrorType(sgqlc.types.Enum):
    """Class for LogConfigurationsParsingRuleMutationErrorType.

    Expected default error types as result of mutating an existing
    parsing rule.

    Enumeration Choices:

    * `INVALID_GROK`: Invalid Grok
    * `INVALID_ID`: Number format error. ID should be convertible to
      int.
    * `INVALID_NRQL`: Invalid NRQL
    * `NOT_FOUND`: Couldn't find the specified parsing rule
    """

    __schema__ = nerdgraph
    __choices__ = ("INVALID_GROK", "INVALID_ID", "INVALID_NRQL", "NOT_FOUND")


class MetricNormalizationCustomerRuleAction(sgqlc.types.Enum):
    """Class for MetricNormalizationCustomerRuleAction.

    The different rule actions for customers.

    Enumeration Choices:

    * `DENY_NEW_METRICS`: Deny new metrics (only for NR
      Administrators)
    * `IGNORE`: Ignore matching metrics.
    * `REPLACE`: Replace metrics
    """

    __schema__ = nerdgraph
    __choices__ = ("DENY_NEW_METRICS", "IGNORE", "REPLACE")


class MetricNormalizationRuleAction(sgqlc.types.Enum):
    """Class for MetricNormalizationRuleAction.

    The different rule actions.

    Enumeration Choices:

    * `DENY_NEW_METRICS`: Deny new metrics.
    * `IGNORE`: Ignore matching metrics.
    * `REPLACE`: Replace metrics
    """

    __schema__ = nerdgraph
    __choices__ = ("DENY_NEW_METRICS", "IGNORE", "REPLACE")


class MetricNormalizationRuleErrorType(sgqlc.types.Enum):
    """Class for MetricNormalizationRuleErrorType.

    The different types of errors the API can return.

    Enumeration Choices:

    * `CREATION_ERROR`: Creation Error.
    * `EDITION_ERROR`: Edition Error.
    * `RULE_NOT_FOUND`: Rule does not exist.
    * `VALIDATION_ERROR`: Validation error
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CREATION_ERROR",
        "EDITION_ERROR",
        "RULE_NOT_FOUND",
        "VALIDATION_ERROR",
    )


class NerdStorageScope(sgqlc.types.Enum):
    """Class for NerdStorageScope.

    The access level of the NerdStorage data.

    Enumeration Choices:

    * `ACCOUNT`: Account-level storage.
    * `ACTOR`: Actor-level storage.
    * `ENTITY`: Entity-level storage
    """

    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT", "ACTOR", "ENTITY")


class NerdStorageVaultActorScope(sgqlc.types.Enum):
    """Class for NerdStorageVaultActorScope.

    NerdStorageVault data will only be visible to the User that
    created them.

    Enumeration Choices:

    * `CURRENT_USER`: Store and retrieve NerdStorageVault data for the
      current user
    """

    __schema__ = nerdgraph
    __choices__ = ("CURRENT_USER",)


class NerdStorageVaultErrorType(sgqlc.types.Enum):
    """Class for NerdStorageVaultErrorType.

    The possible types why an error may have occurred.

    Enumeration Choices:

    * `ACCESS_DENIED`: Indicates the client performing the operation
      does not have sufficient permission.
    * `BAD_INPUT`: Indicates the mutation has malformed input and
      needs to be corrected before the mutation can be processed.
    * `NOT_FOUND`: Indicates that the resource does not exist.
    * `VALIDATION_FAILED`: Indicates the mutation has failed
      validation
    """

    __schema__ = nerdgraph
    __choices__ = ("ACCESS_DENIED", "BAD_INPUT", "NOT_FOUND", "VALIDATION_FAILED")


class NerdStorageVaultResultStatus(sgqlc.types.Enum):
    """Class for NerdStorageVaultResultStatus.

    Mutation result status.

    Enumeration Choices:

    * `FAILURE`: The mutation failed.
    * `SUCCESS`: The mutation succeeded
    """

    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class NerdpackMutationErrorType(sgqlc.types.Enum):
    """Class for NerdpackMutationErrorType.

    Error reason for the mutation.

    Enumeration Choices:

    * `CAPABILITY_NOT_GRANTED`: The user does not have the required
      capability to execute the operation.
    * `DOWNSTREAM_ERROR`: Downstream service error.
    * `NOT_FOUND`: Resource not found for given operation.
    * `TNC_NOT_ACCEPTED`: Terms and conditions have not been accepted
      by the operation account.
    * `UNAUTHORIZED_ACCOUNT`: Account is not authorized to execute the
      operation
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CAPABILITY_NOT_GRANTED",
        "DOWNSTREAM_ERROR",
        "NOT_FOUND",
        "TNC_NOT_ACCEPTED",
        "UNAUTHORIZED_ACCOUNT",
    )


class NerdpackMutationResult(sgqlc.types.Enum):
    """Class for NerdpackMutationResult.

    Mutation result.

    Enumeration Choices:

    * `ERROR`: Error executing mutation.
    * `OK`: Successful mutation execution
    """

    __schema__ = nerdgraph
    __choices__ = ("ERROR", "OK")


class NerdpackRemovedTagResponseType(sgqlc.types.Enum):
    """Class for NerdpackRemovedTagResponseType.

    Indicates if a tag has been removed for a nerdpack

    Enumeration Choices:

    * `NOTHING_TO_REMOVE`: Indicates the tag has not been removed
    * `REMOVED`: Indicates the tag has been removed
    """

    __schema__ = nerdgraph
    __choices__ = ("NOTHING_TO_REMOVE", "REMOVED")


class NerdpackSubscriptionAccessType(sgqlc.types.Enum):
    """Class for NerdpackSubscriptionAccessType.

    Type of access to the subscribed Nerdpack.

    Enumeration Choices:

    * `DIRECT`: Direct subscription with user account.
    * `INHERITED`: Master account subscription
    """

    __schema__ = nerdgraph
    __choices__ = ("DIRECT", "INHERITED")


class NerdpackSubscriptionModel(sgqlc.types.Enum):
    """Class for NerdpackSubscriptionModel.

    Type that define the rules for account subscription.

    Enumeration Choices:

    * `CORE`: Product nerdpacks displayed to everybody, no
      subscription required .
    * `GLOBAL`: Any NR user can subscribe to the nerdpack.
    * `OWNER_AND_ALLOWED`: Only owner, master and allowed accounts can
      subscribe to the nerdpack
    """

    __schema__ = nerdgraph
    __choices__ = ("CORE", "GLOBAL", "OWNER_AND_ALLOWED")


class NerdpackVersionFilterFallback(sgqlc.types.Enum):
    """Class for NerdpackVersionFilterFallback.

    Fallback version to return if no version matches with the given
    filters.

    Enumeration Choices:

    * `LATEST_SEMVER`: Latest version (semver)
    """

    __schema__ = nerdgraph
    __choices__ = ("LATEST_SEMVER",)


class Nr1CatalogAlertConditionType(sgqlc.types.Enum):
    """Class for Nr1CatalogAlertConditionType.

    Possible types of configured alert conditions

    Enumeration Choices:

    * `BASELINE`: A baseline alert condition
    * `STATIC`: A static alert condition
    """

    __schema__ = nerdgraph
    __choices__ = ("BASELINE", "STATIC")


class Nr1CatalogInstallPlanDestination(sgqlc.types.Enum):
    """Class for Nr1CatalogInstallPlanDestination.

    Possible destinations for the install plan target

    Enumeration Choices:

    * `APPLICATION`: Application (APM) install
    * `CLOUD`: Cloud provider install
    * `HOST`: Host install
    * `KUBERNETES`: Kubernetes install
    * `UNKNOWN`: Unknown install - special case when the target where
      the install takes place is unknown (such as guided install)
    """

    __schema__ = nerdgraph
    __choices__ = ("APPLICATION", "CLOUD", "HOST", "KUBERNETES", "UNKNOWN")


class Nr1CatalogInstallPlanDirectiveMode(sgqlc.types.Enum):
    """Class for Nr1CatalogInstallPlanDirectiveMode.

    Possible modes for an install plan directive

    Enumeration Choices:

    * `LINK`: Directs the installation toward an external link
    * `NERDLET`: Directs the installation to open a stacked Nerdlet to
      perform the installation
    * `TARGETED`: Directs the installation toward a specific target
    """

    __schema__ = nerdgraph
    __choices__ = ("LINK", "NERDLET", "TARGETED")


class Nr1CatalogInstallPlanOperatingSystem(sgqlc.types.Enum):
    """Class for Nr1CatalogInstallPlanOperatingSystem.

    Possible types for the install plan operating system

    Enumeration Choices:

    * `DARWIN`: Mac operating system
    * `LINUX`: Linux operating system
    * `WINDOWS`: Windows operating system
    """

    __schema__ = nerdgraph
    __choices__ = ("DARWIN", "LINUX", "WINDOWS")


class Nr1CatalogInstallPlanTargetType(sgqlc.types.Enum):
    """Class for Nr1CatalogInstallPlanTargetType.

    Possible types for the install plan target

    Enumeration Choices:

    * `AGENT`: Agent install
    * `INTEGRATION`: Integration install
    * `ON_HOST_INTEGRATION`: On host integration install
    * `UNKNOWN`: Unknown install - special case when the target where
      the install takes place is unknown (such as guided install)
    """

    __schema__ = nerdgraph
    __choices__ = ("AGENT", "INTEGRATION", "ON_HOST_INTEGRATION", "UNKNOWN")


class Nr1CatalogInstallerType(sgqlc.types.Enum):
    """Class for Nr1CatalogInstallerType.

    Type of installer

    Enumeration Choices:

    * `INSTALL_PLAN`: Install plan
    """

    __schema__ = nerdgraph
    __choices__ = ("INSTALL_PLAN",)


class Nr1CatalogMutationResult(sgqlc.types.Enum):
    """Class for Nr1CatalogMutationResult.

    Outcome of the mutation

    Enumeration Choices:

    * `ERROR`: The mutation failed
    * `OK`: The mutation was processed successfully
    """

    __schema__ = nerdgraph
    __choices__ = ("ERROR", "OK")


class Nr1CatalogNerdpackVisibility(sgqlc.types.Enum):
    """Class for Nr1CatalogNerdpackVisibility.

    Possible visibilities for the Nerdpack

    Enumeration Choices:

    * `GLOBAL`: Indicates the Nerdpack is available globally across
      all accounts
    * `OWNER_AND_ALLOWED`: Indicates the Nerdpack is only available to
      the owning and allowed accounts
    """

    __schema__ = nerdgraph
    __choices__ = ("GLOBAL", "OWNER_AND_ALLOWED")


class Nr1CatalogQuickstartAlertConditionType(sgqlc.types.Enum):
    """Class for Nr1CatalogQuickstartAlertConditionType.

    Possible types of configured alert conditions

    Enumeration Choices:

    * `BASELINE`: A baseline alert condition
    * `STATIC`: A static alert condition
    """

    __schema__ = nerdgraph
    __choices__ = ("BASELINE", "STATIC")


class Nr1CatalogRenderFormat(sgqlc.types.Enum):
    """Class for Nr1CatalogRenderFormat.

    Supported rendering formats for data

    Enumeration Choices:

    * `MARKDOWN`: Renders the output in Markdown
    """

    __schema__ = nerdgraph
    __choices__ = ("MARKDOWN",)


class Nr1CatalogSearchComponentType(sgqlc.types.Enum):
    """Class for Nr1CatalogSearchComponentType.

    Possible component types to filter the search

    Enumeration Choices:

    * `ALERTS`: Filter search results that contain alerts
    * `APPS`: Filter search results that contain apps
    * `DASHBOARDS`: Filter search results that contain dashboards
    * `DATA_SOURCES`: Filter search results that contain data sources
    * `VISUALIZATIONS`: Filter search results that contain
      visualizations
    """

    __schema__ = nerdgraph
    __choices__ = ("ALERTS", "APPS", "DASHBOARDS", "DATA_SOURCES", "VISUALIZATIONS")


class Nr1CatalogSearchResultType(sgqlc.types.Enum):
    """Class for Nr1CatalogSearchResultType.

    Possible search result types used to filter search results

    Enumeration Choices:

    * `ALERT_POLICY_TEMPLATE`: Filter search results by alert policy
      templates
    * `DASHBOARD_TEMPLATE`: Filter search results by dashboard
      templates
    * `DATA_SOURCE`: Filter search results by data sources
    * `NERDPACK`: Filter search results by nerdpacks
    * `QUICKSTART`: Filter search results by quickstarts
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ALERT_POLICY_TEMPLATE",
        "DASHBOARD_TEMPLATE",
        "DATA_SOURCE",
        "NERDPACK",
        "QUICKSTART",
    )


class Nr1CatalogSearchSortOption(sgqlc.types.Enum):
    """Class for Nr1CatalogSearchSortOption.

    Possible options to sort search results

    Enumeration Choices:

    * `ALPHABETICAL`: Sort the search results alphabetically
    * `POPULARITY`: Sort the search results by most popular
    * `RELEVANCE`: Sort the search results by the most relevant to the
      search query
    * `REVERSE_ALPHABETICAL`: Sort the search results alphabetically
      in reverse order
    """

    __schema__ = nerdgraph
    __choices__ = ("ALPHABETICAL", "POPULARITY", "RELEVANCE", "REVERSE_ALPHABETICAL")


class Nr1CatalogSubmitMetadataErrorType(sgqlc.types.Enum):
    """Class for Nr1CatalogSubmitMetadataErrorType.

    The type of error that occurred during the mutation when
    submitting metadata

    Enumeration Choices:

    * `NERDPACK_NOT_FOUND`: The Nerdpack cannot be found
    * `SERVER_ERROR`: Something went wrong in the service
    * `UNAUTHORIZED`: The user does not have permission to update the
      metadata for the Nerdpack
    * `UNSUPPORTED_TYPE`: The type of the Nerdpack is not supported in
      the New Relic One Catalog
    * `VALIDATION_FAILED`: The submitted metadata is not valid and
      needs to be corrected to be accepted
    """

    __schema__ = nerdgraph
    __choices__ = (
        "NERDPACK_NOT_FOUND",
        "SERVER_ERROR",
        "UNAUTHORIZED",
        "UNSUPPORTED_TYPE",
        "VALIDATION_FAILED",
    )


class Nr1CatalogSupportLevel(sgqlc.types.Enum):
    """Class for Nr1CatalogSupportLevel.

    Possible levels of support

    Enumeration Choices:

    * `COMMUNITY`: Community supported
    * `ENTERPRISE`: Enterprise supported
    * `NEW_RELIC`: New Relic supported
    * `VERIFIED`: Partner supported
    """

    __schema__ = nerdgraph
    __choices__ = ("COMMUNITY", "ENTERPRISE", "NEW_RELIC", "VERIFIED")


class Nr1CatalogSupportedEntityTypesMode(sgqlc.types.Enum):
    """Class for Nr1CatalogSupportedEntityTypesMode.

    Possible modes for supported entity types

    Enumeration Choices:

    * `ALL`: Indicates that all entity types are supported
    * `NONE`: Indicates that no entity types are supported
    * `SPECIFIC`: Indicates that a specific set of entity types are
      supported
    """

    __schema__ = nerdgraph
    __choices__ = ("ALL", "NONE", "SPECIFIC")


class NrqlDropRulesAction(sgqlc.types.Enum):
    """Class for NrqlDropRulesAction.

    Specifies how data matching the drop rule's NRQL string should be
    processed.

    Enumeration Choices:

    * `DROP_ATTRIBUTES`: This action will strip the attributes
      specified in the SELECT clause of the NRQL string for all events
      that match the associated NRQL string.
    * `DROP_ATTRIBUTES_FROM_METRIC_AGGREGATES`: This action will strip
      the attributes specified in the SELECT clause of the NRQL string
      for metric aggregates. The event type must be Metric.
    * `DROP_DATA`: This action will drop all data that match the
      associated NRQL string. That string MUST be a `SELECT *`
    """

    __schema__ = nerdgraph
    __choices__ = (
        "DROP_ATTRIBUTES",
        "DROP_ATTRIBUTES_FROM_METRIC_AGGREGATES",
        "DROP_DATA",
    )


class NrqlDropRulesErrorReason(sgqlc.types.Enum):
    """Class for NrqlDropRulesErrorReason.

    General error categories.

    Enumeration Choices:

    * `FEATURE_FLAG_DISABLED`: Targeted account does not have access
      to this feature.
    * `GENERAL`: Other errors.
    * `INVALID_INPUT`: Something about the request was invalid.
    * `INVALID_QUERY`: The provided NRQL string was ill formed or used
      invalid features.
    * `RULE_NOT_FOUND`: The drop rule being acted upon did not exist.
    * `USER_NOT_AUTHORIZED`: The current user does not have authority
      to perform the given action
    """

    __schema__ = nerdgraph
    __choices__ = (
        "FEATURE_FLAG_DISABLED",
        "GENERAL",
        "INVALID_INPUT",
        "INVALID_QUERY",
        "RULE_NOT_FOUND",
        "USER_NOT_AUTHORIZED",
    )


class OrganizationProvisioningUnit(sgqlc.types.Enum):
    """Class for OrganizationProvisioningUnit.

    Types of units for entitlements

    Enumeration Choices:

    * `ADDITIONAL_DAYS_OF_RETENTION`: Additional days of data
      retention
    * `APPS`: Mobile unit of measure of the number of mobile
      applications
    * `APP_TRANSACTIONS_IN_MILLIONS`: Proactive Detection unit of
      measure
    * `CHECKS`: Synthetics unit of measure
    * `COMPUTE_UNIT`: APM unit of measure of the number of compute
      units
    * `DATA_RETENTION_IN_DAYS`: The time that we retain data in days
    * `DPM`: Metrics unit of measure
    * `EVENTS_IN_MILLIONS`: Insight events in multiples of millions
    * `GB_INGESTED`: NR1 Data unit of measure
    * `GB_PER_DAY`: Logs unit of measure
    * `GRACE_PERIOD`: Grace period in days before customer is billed
      for users
    * `HOSTS`: APM unit of measure for hosts
    * `INCIDENT_EVENTS`: AI unit of measure
    * `INGESTED_EVENTS`: Serverless unit of measure
    * `MONTHLY_ACTIVE_USERS`: Mobile unit of measure
    * `PAGE_VIEWS`: Browser unit of measure
    * `PROVISIONED_USERS`: NR1 Users unit of measure
    * `SPANS_IN_MILLIONS`: Traces unit of measure
    * `USERS`: Mobile unit of measure of the number of users
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ADDITIONAL_DAYS_OF_RETENTION",
        "APPS",
        "APP_TRANSACTIONS_IN_MILLIONS",
        "CHECKS",
        "COMPUTE_UNIT",
        "DATA_RETENTION_IN_DAYS",
        "DPM",
        "EVENTS_IN_MILLIONS",
        "GB_INGESTED",
        "GB_PER_DAY",
        "GRACE_PERIOD",
        "HOSTS",
        "INCIDENT_EVENTS",
        "INGESTED_EVENTS",
        "MONTHLY_ACTIVE_USERS",
        "PAGE_VIEWS",
        "PROVISIONED_USERS",
        "SPANS_IN_MILLIONS",
        "USERS",
    )


class OrganizationUpdateErrorType(sgqlc.types.Enum):
    """Class for OrganizationUpdateErrorType.

    An enum specifying the specific types of errors that may be
    returned.

    Enumeration Choices:

    * `INVALID_RECORD`: Returned when the attributes provided for an
      object are invalid.
    * `NOT_AUTHORIZED`: Returned when the actor has insufficient
      capabilties to fulfill the request
    """

    __schema__ = nerdgraph
    __choices__ = ("INVALID_RECORD", "NOT_AUTHORIZED")


class PixieLinkPixieProjectErrorType(sgqlc.types.Enum):
    """Class for PixieLinkPixieProjectErrorType.

    The errors that can be returned when linking a New Relic account
    and Pixie project

    Enumeration Choices:

    * `ALREADY_LINKED`: There is already a linked Pixie project for
      this New Relic account.
    * `AUTO_CREATION_NOT_SUPPORTED`: Automatic Pixie project creation
      not supported.
    * `INVALID_NEWRELIC_ACCOUNT`: The provided account is not valid.
    * `INVALID_PIXIE_API_KEY`: The provided Pixie API key is not
      valid.
    * `UNLINKING_NOT_SUPPORTED`: Unlinking is not supported
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ALREADY_LINKED",
        "AUTO_CREATION_NOT_SUPPORTED",
        "INVALID_NEWRELIC_ACCOUNT",
        "INVALID_PIXIE_API_KEY",
        "UNLINKING_NOT_SUPPORTED",
    )


class PixieRecordPixieTosAcceptanceErrorType(sgqlc.types.Enum):
    """Class for PixieRecordPixieTosAcceptanceErrorType.

    The errors that can be returned when recording the Pixie terms of
    service acceptance

    Enumeration Choices:

    * `MISSING_DATA`: Some required data to record the Pixie terms of
      service acceptance is missing
    """

    __schema__ = nerdgraph
    __choices__ = ("MISSING_DATA",)


class ReferenceEntityCreateRepositoryErrorType(sgqlc.types.Enum):
    """Class for ReferenceEntityCreateRepositoryErrorType.

    List of all potential error types that an entity create operation
    might return.

    Enumeration Choices:

    * `FORBIDDEN`: Forbidden request
    * `INVALID_INPUT`: Invalid input
    """

    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN", "INVALID_INPUT")


class RegionScope(sgqlc.types.Enum):
    """Class for RegionScope.

    Enumeration Choices:

    * `GLOBAL`: Do not filter by region
    * `IN_REGION`: Filter by region
    """

    __schema__ = nerdgraph
    __choices__ = ("GLOBAL", "IN_REGION")


class ServiceLevelEventsQuerySelectFunction(sgqlc.types.Enum):
    """Class for ServiceLevelEventsQuerySelectFunction.

    The function to use in the SELECT clause.

    Enumeration Choices:

    * `COUNT`: COUNT.
    * `SUM`: SUM
    """

    __schema__ = nerdgraph
    __choices__ = ("COUNT", "SUM")


class ServiceLevelObjectiveRollingTimeWindowUnit(sgqlc.types.Enum):
    """Class for ServiceLevelObjectiveRollingTimeWindowUnit.

    The rolling time window units.

    Enumeration Choices:

    * `DAY`: Day
    """

    __schema__ = nerdgraph
    __choices__ = ("DAY",)


class SortBy(sgqlc.types.Enum):
    """Class for SortBy.

    The `SortBy` enum is for designating sort order.

    Enumeration Choices:

    * `ASC`: Sort in ascending order.
    * `DESC`: Sort in descending order
    """

    __schema__ = nerdgraph
    __choices__ = ("ASC", "DESC")


class StreamingExportStatus(sgqlc.types.Enum):
    """Class for StreamingExportStatus.

    Set of streaming rules states

    Enumeration Choices:

    * `CREATION_FAILED`: Status set for a streaming rule that could
      not be created due to an error
    * `CREATION_IN_PROGRESS`: Status set for a streaming rule being
      set up
    * `DELETED`: Status set for a streaming rule when it is deleted
    * `DISABLED`: Status set for a streaming rule when it is disabled
    * `ENABLED`: Status set for a streaming rule when it is enabled
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "DELETED",
        "DISABLED",
        "ENABLED",
    )


class SyntheticMonitorStatus(sgqlc.types.Enum):
    """Class for SyntheticMonitorStatus.

    Enumeration Choices:

    * `DELETED`None
    * `DISABLED`None
    * `ENABLED`None
    * `FAULTY`None
    * `MUTED`None
    * `PAUSED`None
    """

    __schema__ = nerdgraph
    __choices__ = ("DELETED", "DISABLED", "ENABLED", "FAULTY", "MUTED", "PAUSED")


class SyntheticMonitorType(sgqlc.types.Enum):
    """Class for SyntheticMonitorType.

    The types of Synthetic Monitors.

    Enumeration Choices:

    * `BROWSER`None
    * `CERT_CHECK`None
    * `SCRIPT_API`None
    * `SCRIPT_BROWSER`None
    * `SIMPLE`None
    * `STEP_MONITOR`None
    """

    __schema__ = nerdgraph
    __choices__ = (
        "BROWSER",
        "CERT_CHECK",
        "SCRIPT_API",
        "SCRIPT_BROWSER",
        "SIMPLE",
        "STEP_MONITOR",
    )


class SyntheticsDeviceOrientation(sgqlc.types.Enum):
    """Class for SyntheticsDeviceOrientation.

    enum of Orientations that the user can select for their emulated
    device

    Enumeration Choices:

    * `LANDSCAPE`: This allows the screenshot to be taken in the
      landscape orientation
    * `NONE`: This will disable device emulation
    * `PORTRAIT`: This allows the screenshot to be taken in the
      portrait orientation
    """

    __schema__ = nerdgraph
    __choices__ = ("LANDSCAPE", "NONE", "PORTRAIT")


class SyntheticsDeviceType(sgqlc.types.Enum):
    """Class for SyntheticsDeviceType.

    enum of DeviceTypes that the user can use for device emulation

    Enumeration Choices:

    * `MOBILE`: This will be dimensions for a typical mobile device
    * `NONE`: This will disable device emulation
    * `TABLET`: This will be dimensions for a typical tablet device
    """

    __schema__ = nerdgraph
    __choices__ = ("MOBILE", "NONE", "TABLET")


class SyntheticsMonitorCreateErrorType(sgqlc.types.Enum):
    """Class for SyntheticsMonitorCreateErrorType.

    Types of errors that can be returned from a create monitor request

    Enumeration Choices:

    * `BAD_REQUEST`: Received a request missing required fields or
      containing invalid data
    * `INTERNAL_SERVER_ERROR`: An unknown error occurred while
      processing request to mutate monitor
    * `NOT_FOUND`: Monitor not found for given guid (monitor does not
      exist on account or has already been deleted)
    * `PAYMENT_REQUIRED`: Monitor creation exceeds account
      subscription limits
    * `TAGGING_ERROR`: Monitor tags were not updated.
    * `UNAUTHORIZED`: User does not have authorization to perform
      monitor mutation.
    * `UNKNOWN_ERROR`: An unknown error occurred while processing
      request to create monitor
    """

    __schema__ = nerdgraph
    __choices__ = (
        "BAD_REQUEST",
        "INTERNAL_SERVER_ERROR",
        "NOT_FOUND",
        "PAYMENT_REQUIRED",
        "TAGGING_ERROR",
        "UNAUTHORIZED",
        "UNKNOWN_ERROR",
    )


class SyntheticsMonitorPeriod(sgqlc.types.Enum):
    """Class for SyntheticsMonitorPeriod.

    Enum of monitor period types

    Enumeration Choices:

    * `EVERY_10_MINUTES`: 10 minute monitor period
    * `EVERY_12_HOURS`: 12 hour monitor period (720 minutes)
    * `EVERY_15_MINUTES`: 15 minute monitor period
    * `EVERY_30_MINUTES`: 30 minute monitor period
    * `EVERY_5_MINUTES`: 5 minute monitor period
    * `EVERY_6_HOURS`: 6 hour monitor period (360 minutes)
    * `EVERY_DAY`: 1 day monitor period (1440 minutes)
    * `EVERY_HOUR`: 1 hour monitor period (60 minutes)
    * `EVERY_MINUTE`: 1 minute monitor period
    """

    __schema__ = nerdgraph
    __choices__ = (
        "EVERY_10_MINUTES",
        "EVERY_12_HOURS",
        "EVERY_15_MINUTES",
        "EVERY_30_MINUTES",
        "EVERY_5_MINUTES",
        "EVERY_6_HOURS",
        "EVERY_DAY",
        "EVERY_HOUR",
        "EVERY_MINUTE",
    )


class SyntheticsMonitorStatus(sgqlc.types.Enum):
    """Class for SyntheticsMonitorStatus.

    Run state of the monitor

    Enumeration Choices:

    * `DISABLED`: Monitor disabled runs status of a monitor
    * `ENABLED`: Enabled status of a monitor
    * `MUTED`: Alerts muted status of a monitor
    """

    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "ENABLED", "MUTED")


class SyntheticsMonitorUpdateErrorType(sgqlc.types.Enum):
    """Class for SyntheticsMonitorUpdateErrorType.

    Types of errors that can be returned from a Monitor mutation
    request

    Enumeration Choices:

    * `BAD_REQUEST`: Received a request missing required fields or
      containing invalid data
    * `INTERNAL_SERVER_ERROR`: An unknown error occurred while
      processing request to mutate monitor
    * `NOT_FOUND`: Monitor not found for given guid (monitor does not
      exist on account or has already been deleted)
    * `SCRIPT_ERROR`: An error occurred while updating monitor script
    * `TAGGING_ERROR`: Monitor tags were not updated.
    * `UNAUTHORIZED`: User does not have authorization to perform
      monitor mutation.
    * `UNKNOWN_ERROR`: An unknown error occurred while processing
      request to update monitor
    """

    __schema__ = nerdgraph
    __choices__ = (
        "BAD_REQUEST",
        "INTERNAL_SERVER_ERROR",
        "NOT_FOUND",
        "SCRIPT_ERROR",
        "TAGGING_ERROR",
        "UNAUTHORIZED",
        "UNKNOWN_ERROR",
    )


class SyntheticsPrivateLocationMutationErrorType(sgqlc.types.Enum):
    """Class for SyntheticsPrivateLocationMutationErrorType.

    Types of errors that can be returned from a Private Location
    mutation request

    Enumeration Choices:

    * `BAD_REQUEST`: Received a request missing required fields or
      containing invalid data
    * `INTERNAL_SERVER_ERROR`: An unknown error occurred while
      processing request to purge specified private location job queue
    * `NOT_FOUND`: Private location not found for key (private
      location does not exist on account or has already been deleted)
    * `UNAUTHORIZED`: User does not have authorization to purge job
      queue for specified private location
    """

    __schema__ = nerdgraph
    __choices__ = ("BAD_REQUEST", "INTERNAL_SERVER_ERROR", "NOT_FOUND", "UNAUTHORIZED")


class SyntheticsStepType(sgqlc.types.Enum):
    """Class for SyntheticsStepType.

    enum of of script step types

    Enumeration Choices:

    * `ASSERT_ELEMENT`: Assert on element accessed by ID, CSS, or
      x-path
    * `ASSERT_MODAL`: Assert on modal exists
    * `ASSERT_TEXT`: Assert on text accessed by ID, CSS, or x-path
    * `ASSERT_TITLE`: Assert on title of page
    * `CLICK_ELEMENT`: Click on an element by ID, CSS, or x-path
    * `DISMISS_MODAL`: Preform actions on a modal to dismiss
    * `DOUBLE_CLICK_ELEMENT`: Double click on an element by ID, CSS,
      or x-path
    * `HOVER_ELEMENT`: Hover over an element by x-path
    * `NAVIGATE`: Navigate to the specified url
    * `SECURE_TEXT_ENTRY`: Input secure credential into element
      accessed by ID, CSS, or x-path
    * `SELECT_ELEMENT`: Select a dropdown element by value, text, ID,
      CSS, or x-path
    * `TEXT_ENTRY`: Input text into element accessed by ID, CSS, or
      x-path
    """

    __schema__ = nerdgraph
    __choices__ = (
        "ASSERT_ELEMENT",
        "ASSERT_MODAL",
        "ASSERT_TEXT",
        "ASSERT_TITLE",
        "CLICK_ELEMENT",
        "DISMISS_MODAL",
        "DOUBLE_CLICK_ELEMENT",
        "HOVER_ELEMENT",
        "NAVIGATE",
        "SECURE_TEXT_ENTRY",
        "SELECT_ELEMENT",
        "TEXT_ENTRY",
    )


class TaggingMutationErrorType(sgqlc.types.Enum):
    """Class for TaggingMutationErrorType.

    The different types of errors the API can return.

    Enumeration Choices:

    * `CONCURRENT_TASK_EXCEPTION`: Too many concurrent tasks for the
      same GUID are being sent and we cannot process. Please serialize
      your requests for the given GUID.
    * `INVALID_DOMAIN_TYPE`: Domain Type invalid. The decoded domain
      type from the provided GUID is not valid. Please provide a
      correct GUID.
    * `INVALID_ENTITY_GUID`: We could not decode the provided GUID.
      Entity guid needs to be base64 encoded.
    * `INVALID_KEY`: The tag key is not valid. Char length has been
      reached, contains a disallowed character(eg :) or is empty
    * `INVALID_VALUE`: The tag value is not valid. Char length has
      been reached, contains a disallowed character(eg :) or is empty
    * `NOT_FOUND`: The given GUID or tag you're looking for does not
      exist.
    * `NOT_PERMITTED`: You've attempted to do something your
      Domain/EntityType is not permitted to do. Its also possible that
      an api key is required.
    * `TOO_MANY_CHARS_QUERY_FILTER`: One of the query filters exceeds
      the character limit.
    * `TOO_MANY_TAG_KEYS`: The given entity has reached its tag key
      count limit. You will need to delete existing tags for the given
      GUID before continuing.
    * `TOO_MANY_TAG_VALUES`: The given entity has reached its tag
      value count limit. You will need to delete existing values for
      the given GUID before continuing.
    * `UPDATE_WILL_BE_DELAYED`: The changes will be reflected in the
      entity with some delay
    """

    __schema__ = nerdgraph
    __choices__ = (
        "CONCURRENT_TASK_EXCEPTION",
        "INVALID_DOMAIN_TYPE",
        "INVALID_ENTITY_GUID",
        "INVALID_KEY",
        "INVALID_VALUE",
        "NOT_FOUND",
        "NOT_PERMITTED",
        "TOO_MANY_CHARS_QUERY_FILTER",
        "TOO_MANY_TAG_KEYS",
        "TOO_MANY_TAG_VALUES",
        "UPDATE_WILL_BE_DELAYED",
    )


class UserManagementRequestedTierName(sgqlc.types.Enum):
    """Class for UserManagementRequestedTierName.

    Valid request types for user change requests

    Enumeration Choices:

    * `BASIC_USER_TIER`: basic tier
    * `CORE_USER_TIER`: core tier
    * `FULL_USER_TIER`: full tier
    """

    __schema__ = nerdgraph
    __choices__ = ("BASIC_USER_TIER", "CORE_USER_TIER", "FULL_USER_TIER")


class WhatsNewContentType(sgqlc.types.Enum):
    """Class for WhatsNewContentType.

    Represents the different types of content available when searching
    by news.

    Enumeration Choices:

    * `ANNOUNCEMENT`: News the content of which is type of
      announcement
    """

    __schema__ = nerdgraph
    __choices__ = ("ANNOUNCEMENT",)


class WorkloadGroupRemainingEntitiesRuleBy(sgqlc.types.Enum):
    """Class for WorkloadGroupRemainingEntitiesRuleBy.

    Indicates by which field the remaining entities rule should be
    grouped.

    Enumeration Choices:

    * `ENTITY_TYPE`: Group the remaining entities rule by entity type.
    * `NONE`: Do not apply any grouping to the remaining entities
      rule
    """

    __schema__ = nerdgraph
    __choices__ = ("ENTITY_TYPE", "NONE")


class WorkloadResultingGroupType(sgqlc.types.Enum):
    """Class for WorkloadResultingGroupType.

    Represents the type of the rule that the resulting group of
    entities belongs to.

    Enumeration Choices:

    * `REGULAR_GROUP`: The rule considers the entities within a
      specific group in the workload.
    * `REMAINING_ENTITIES`: The rule considers all the entities within
      the workload that aren’t evaluated in any other rule
    """

    __schema__ = nerdgraph
    __choices__ = ("REGULAR_GROUP", "REMAINING_ENTITIES")


class WorkloadRollupStrategy(sgqlc.types.Enum):
    """Class for WorkloadRollupStrategy.

    Represents the rollup strategy that is applied to a group of
    entities.

    Enumeration Choices:

    * `BEST_STATUS_WINS`: The group status matches the less critical
      status of all belonging entities.
    * `WORST_STATUS_WINS`: The group status matches the most critical
      status of all belonging entities
    """

    __schema__ = nerdgraph
    __choices__ = ("BEST_STATUS_WINS", "WORST_STATUS_WINS")


class WorkloadRuleThresholdType(sgqlc.types.Enum):
    """Class for WorkloadRuleThresholdType.

    Represents the type of the threshold defined for a rule.

    Enumeration Choices:

    * `FIXED`: The worst status is rolled up only after a certain
      number of entities within the workload are not operational.
    * `PERCENTAGE`: The worst status is rolled up only after a certain
      percentage of entities within the workload are not operational
    """

    __schema__ = nerdgraph
    __choices__ = ("FIXED", "PERCENTAGE")


class WorkloadStatusSource(sgqlc.types.Enum):
    """Class for WorkloadStatusSource.

    Indicates where the status value derives from.

    Enumeration Choices:

    * `ROLLUP_RULE`: Refers to the result of an automatic rule defined
      for a workload.
    * `STATIC`: Refers to a static status defined for a workload.
    * `UNKNOWN`: Refers to an undetermined status source.
    * `WORKLOAD`: Refers to the override policy that is applied to a
      set of partial results within a workload. Any static status
      always overrides any other status values calculated
      automatically. Otherwise, the worst status of the partial
      results is rolled up
    """

    __schema__ = nerdgraph
    __choices__ = ("ROLLUP_RULE", "STATIC", "UNKNOWN", "WORKLOAD")


class WorkloadStatusValue(sgqlc.types.Enum):
    """Class for WorkloadStatusValue.

    The status of the workload, which is derived from the static and
    the automatic statuses configured. Any static status always
    overrides any other status values calculated automatically.

    Enumeration Choices:

    * `DEGRADED`: The status of the workload is degraded.
    * `DISRUPTED`: The status of the workload is disrupted.
    * `OPERATIONAL`: The status of the workload is operational.
    * `UNKNOWN`: The status of the workload is unknown
    """

    __schema__ = nerdgraph
    __choices__ = ("DEGRADED", "DISRUPTED", "OPERATIONAL", "UNKNOWN")


class WorkloadStatusValueInput(sgqlc.types.Enum):
    """Class for WorkloadStatusValueInput.

    The status value. Any static status always overrides any other
    status values calculated automatically.

    Enumeration Choices:

    * `DEGRADED`: The status of the workload is degraded.
    * `DISRUPTED`: The status of the workload is disrupted.
    * `OPERATIONAL`: The status of the workload is operational
    """

    __schema__ = nerdgraph
    __choices__ = ("DEGRADED", "DISRUPTED", "OPERATIONAL")
