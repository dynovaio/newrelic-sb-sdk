__all__ = [
    "AgentApplicationBrowserLoader",
    "AgentApplicationSegmentsListType",
    "AgentApplicationSettingsBrowserLoader",
    "AgentApplicationSettingsBrowserLoaderInput",
    "AgentApplicationSettingsMobileSessionReplayMode",
    "AgentApplicationSettingsMobileSessionReplayModeInput",
    "AgentApplicationSettingsNetworkFilterMode",
    "AgentApplicationSettingsRecordSqlEnum",
    "AgentApplicationSettingsSessionTraceMode",
    "AgentApplicationSettingsSessionTraceModeInput",
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
    "AiWorkflowsBatchCreateMigratedWorkflowsErrorType",
    "AiWorkflowsBatchDeleteMigratedWorkflowsErrorType",
    "AiWorkflowsCreateErrorType",
    "AiWorkflowsDeleteErrorType",
    "AiWorkflowsDestinationType",
    "AiWorkflowsEnrichmentType",
    "AiWorkflowsFetchWorkflowsByIssuesFilterErrorType",
    "AiWorkflowsFilterType",
    "AiWorkflowsMutingRulesHandling",
    "AiWorkflowsNotificationTrigger",
    "AiWorkflowsOperator",
    "AiWorkflowsTestErrorType",
    "AiWorkflowsTestNotificationResponseStatus",
    "AiWorkflowsTestResponseStatus",
    "AiWorkflowsUpdateErrorType",
    "AlertsActionOnMutingRuleWindowEnded",
    "AlertsAsNrqlSourceProduct",
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
    "AlertsNrqlSignalSeasonality",
    "AlertsNrqlStaticConditionValueFunction",
    "AlertsOpsGenieDataCenterRegion",
    "AlertsSignalAggregationMethod",
    "AlertsViolationTimeLimit",
    "AlertsWebhookCustomPayloadType",
    "ApiAccessIngestKeyErrorType",
    "ApiAccessIngestKeyType",
    "ApiAccessKeyType",
    "ApiAccessUserKeyErrorType",
    "AuthorizationManagementGranteeTypeEnum",
    "BrowserAgentInstallType",
    "ChangeTrackingCategoryType",
    "ChangeTrackingDeploymentType",
    "ChangeTrackingValidationFlag",
    "ChartFormatType",
    "ChartImageType",
    "CloudMetricCollectionMode",
    "CollaborationExternalApplicationType",
    "CollaborationStatus",
    "DashboardAddWidgetsToPageErrorType",
    "DashboardAlertSeverity",
    "DashboardCreateErrorType",
    "DashboardDeleteErrorType",
    "DashboardDeleteResultStatus",
    "DashboardEntityPermissions",
    "DashboardLiveUrlAuthType",
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
    "DataManagementType",
    "DataManagementUnit",
    "DataSourceGapsGapTypeIdentifier",
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
    "EntityManagementAiToolParameterType",
    "EntityManagementAssignmentType",
    "EntityManagementCategory",
    "EntityManagementCategoryScopeType",
    "EntityManagementCommunicationMode",
    "EntityManagementCommunicationStatus",
    "EntityManagementConsumptionMetric",
    "EntityManagementDirection",
    "EntityManagementEncodingName",
    "EntityManagementEncodingType",
    "EntityManagementEntityScope",
    "EntityManagementExecutionStatus",
    "EntityManagementExternalOwnerType",
    "EntityManagementFleetDeploymentPhase",
    "EntityManagementHostingPlatform",
    "EntityManagementIncidentStatus",
    "EntityManagementInstallationStatus",
    "EntityManagementIssueType",
    "EntityManagementJiraIssueType",
    "EntityManagementKeyType",
    "EntityManagementLicenseName",
    "EntityManagementManagedEntityType",
    "EntityManagementMessageType",
    "EntityManagementOverlapPolicy",
    "EntityManagementPriority",
    "EntityManagementRegion",
    "EntityManagementSigningAlgorithm",
    "EntityManagementStatusCode",
    "EntityManagementSyncConfigurationMode",
    "EntityManagementSyncGroupRuleConditionType",
    "EntityManagementTeamExternalIntegrationType",
    "EntityManagementTextSplitterType",
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
    "ErrorsInboxEventSource",
    "ErrorsInboxIssueType",
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
    "KnowledgePublishStatus",
    "KnowledgeSearchSortOption",
    "KnowledgeSearchSources",
    "LogConfigurationsCreateDataPartitionRuleErrorType",
    "LogConfigurationsDataPartitionRuleMatchingOperator",
    "LogConfigurationsDataPartitionRuleMutationErrorType",
    "LogConfigurationsDataPartitionRuleRetentionPolicyType",
    "LogConfigurationsLiveArchiveRetentionPolicyType",
    "LogConfigurationsObfuscationMethod",
    "LogConfigurationsParsingRuleMutationErrorType",
    "MachineLearningEncodingName",
    "MachineLearningFilterByKeys",
    "MachineLearningOperator",
    "MachineLearningTextSplitterType",
    "MetricNormalizationCustomerRuleAction",
    "MetricNormalizationRuleAction",
    "MetricNormalizationRuleErrorType",
    "MultiTenantAuthorizationGrantScopeEnum",
    "MultiTenantAuthorizationGrantSortEnum",
    "MultiTenantAuthorizationGranteeTypeEnum",
    "MultiTenantAuthorizationPermissionCategoryEnum",
    "MultiTenantAuthorizationRoleScopeEnum",
    "MultiTenantAuthorizationRoleSortEnum",
    "MultiTenantAuthorizationRoleTypeEnum",
    "MultiTenantAuthorizationSortDirectionEnum",
    "MultiTenantIdentityCapability",
    "MultiTenantIdentityEmailVerificationState",
    "MultiTenantIdentitySortDirection",
    "MultiTenantIdentitySortKeyEnum",
    "MultiTenantIdentityUserSortKey",
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
    "NrqlCancelQueryMutationRequestStatus",
    "NrqlDropRulesAction",
    "NrqlDropRulesErrorReason",
    "OrganizationAccountShareSortDirectionEnum",
    "OrganizationAccountShareSortKeyEnum",
    "OrganizationAccountSortDirectionEnum",
    "OrganizationAccountSortKeyEnum",
    "OrganizationAccountStatus",
    "OrganizationAuthenticationTypeEnum",
    "OrganizationBillingStructure",
    "OrganizationMembersOrganizationMemberType",
    "OrganizationOrganizationCreateJobResultStatusEnum",
    "OrganizationOrganizationCreateJobStatusEnum",
    "OrganizationProvisioningTypeEnum",
    "OrganizationProvisioningUnit",
    "OrganizationRegionCodeEnum",
    "OrganizationSharingMode",
    "OrganizationSortDirectionEnum",
    "OrganizationSortKeyEnum",
    "OrganizationUpdateErrorType",
    "PixieLinkPixieProjectErrorType",
    "PixieRecordPixieTosAcceptanceErrorType",
    "ReferenceEntityCreateRepositoryErrorType",
    "RegionScope",
    "SecretsManagementScopeType",
    "SecretsManagementSortDirection",
    "SecretsManagementSortKey",
    "ServiceLevelEventsQuerySelectFunction",
    "ServiceLevelObjectiveRollingTimeWindowUnit",
    "SessionsClientType",
    "SessionsPrincipalType",
    "SortBy",
    "StreamingExportPayloadCompression",
    "StreamingExportStatus",
    "SyntheticMonitorStatus",
    "SyntheticMonitorType",
    "SyntheticsBrowser",
    "SyntheticsDevice",
    "SyntheticsDeviceOrientation",
    "SyntheticsDeviceType",
    "SyntheticsMonitorCreateErrorType",
    "SyntheticsMonitorDowntimeDayOfMonthOrdinal",
    "SyntheticsMonitorDowntimeWeekDays",
    "SyntheticsMonitorPeriod",
    "SyntheticsMonitorStatus",
    "SyntheticsMonitorUpdateErrorType",
    "SyntheticsPrivateLocationMutationErrorType",
    "SyntheticsStepType",
    "SystemIdentityIdentitySortFieldKey",
    "SystemIdentitySortOrder",
    "TaggingMutationErrorType",
    "UserManagementGroupSortKey",
    "UserManagementRequestedTierName",
    "UserManagementSortDirection",
    "UserManagementTypeEnum",
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
    __schema__ = nerdgraph
    __choices__ = ("LITE", "NONE", "PRO", "SPA")


class AgentApplicationSegmentsListType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INTERNAL", "USER")


class AgentApplicationSettingsBrowserLoader(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("LITE", "NONE", "PRO", "SPA", "XHR")


class AgentApplicationSettingsBrowserLoaderInput(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("LITE", "NONE", "PRO", "SPA")


class AgentApplicationSettingsMobileSessionReplayMode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CUSTOM", "DEFAULT")


class AgentApplicationSettingsMobileSessionReplayModeInput(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CUSTOM", "DEFAULT")


class AgentApplicationSettingsNetworkFilterMode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "HIDE", "SHOW")


class AgentApplicationSettingsRecordSqlEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("OBFUSCATED", "OFF", "RAW")


class AgentApplicationSettingsSessionTraceMode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FIXED_RATE", "PROBABILISTIC")


class AgentApplicationSettingsSessionTraceModeInput(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FIXED_RATE", "PROBABILISTIC")


class AgentApplicationSettingsThresholdTypeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("APDEX_F", "VALUE")


class AgentApplicationSettingsTracer(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CROSS_APPLICATION_TRACER", "DISTRIBUTED_TRACING", "NONE", "OPT_OUT")


class AgentApplicationSettingsUpdateErrorClass(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCESS_DENIED", "INVALID_INPUT", "NOT_FOUND")


class AgentFeaturesFilter(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = (
        "ANDROID",
        "AWS_FIREHOSE_LOG_FORWARDER",
        "AWS_LAMBDA_LOG_FORWARDER",
        "BROWSER",
        "DOTNET",
        "ELIXIR",
        "FLUENTBIT",
        "GO",
        "INFRASTRUCTURE",
        "IOS",
        "JAVA",
        "KUBERNETES",
        "NODEJS",
        "NRDOT",
        "PHP",
        "PIPELINE_CONTROL_GATEWAY",
        "PROMETHEUS",
        "PYTHON",
        "RUBY",
        "SDK",
        "STREAMING_FOR_BROWSER",
        "STREAMING_FOR_MOBILE",
        "STREAMING_FOR_OTHERS",
    )


class AiDecisionsDecisionSortMethod(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ID", "LATEST_CREATED", "STATE_LAST_MODIFIED")


class AiDecisionsDecisionState(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "ENABLED")


class AiDecisionsDecisionType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("EXPLICIT", "GLOBAL", "IMPLICIT")


class AiDecisionsIncidentSelect(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FIRST_INCIDENT", "SECOND_INCIDENT")


class AiDecisionsIssuePriority(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "HIGH", "LOW", "MEDIUM")


class AiDecisionsOpinion(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DISLIKE", "LIKE")


class AiDecisionsResultType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class AiDecisionsRuleSource(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ADMIN", "GENERATED", "SYSTEM", "USER")


class AiDecisionsRuleState(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "ENABLED")


class AiDecisionsRuleType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("EXPLICIT", "GLOBAL", "IMPLICIT")


class AiDecisionsSuggestionState(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCEPTED", "DECLINED", "POSTPONED", "UNDECIDED")


class AiDecisionsVertexClass(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("CLOSED", "CREATED")


class AiIssuesIssueMutingState(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FULLY_MUTED", "NOT_MUTED", "PARTIALLY_MUTED")


class AiIssuesIssueState(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACTIVATED", "CLOSED", "CREATED", "DEACTIVATED")


class AiIssuesIssueUserAction(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "ACK",
        "CLOSE_BY_MUTING_RULE_ID",
        "MARK_AS_INVESTIGATING",
        "RESOLVE",
        "UNACK",
    )


class AiIssuesPriority(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "HIGH", "LOW", "MEDIUM")


class AiNotificationsAuthType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BASIC", "CUSTOM_HEADERS", "OAUTH2", "TOKEN")


class AiNotificationsChannelFields(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = (
        "CONFIGURATION_ERROR",
        "CONFIGURATION_WARNING",
        "DEFAULT",
        "UNKNOWN_ERROR",
    )


class AiNotificationsChannelType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "EMAIL",
        "EVENT_BRIDGE",
        "JIRA_CLASSIC",
        "JIRA_NEXTGEN",
        "MICROSOFT_TEAMS",
        "MOBILE_PUSH",
        "PAGERDUTY_ACCOUNT_INTEGRATION",
        "PAGERDUTY_SERVICE_INTEGRATION",
        "SERVICENOW_EVENTS",
        "SERVICENOW_INCIDENTS",
        "SERVICE_NOW_APP",
        "SLACK",
        "SLACK_COLLABORATION",
        "SLACK_LEGACY",
        "WEBHOOK",
        "WORKFLOW_AUTOMATION",
    )


class AiNotificationsDestinationFields(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = (
        "EMAIL",
        "EVENT_BRIDGE",
        "JIRA",
        "MICROSOFT_TEAMS",
        "MOBILE_PUSH",
        "PAGERDUTY_ACCOUNT_INTEGRATION",
        "PAGERDUTY_SERVICE_INTEGRATION",
        "SERVICE_NOW",
        "SERVICE_NOW_APP",
        "SLACK",
        "SLACK_COLLABORATION",
        "SLACK_LEGACY",
        "WEBHOOK",
        "WORKFLOW_AUTOMATION",
    )


class AiNotificationsErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "CONNECTION_ERROR",
        "ENTITY_IN_USE",
        "EXTERNAL_SERVER_ERROR",
        "FEATURE_FLAG_DISABLED",
        "INVALID_CHANNEL_NAME",
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
    __schema__ = nerdgraph
    __choices__ = (
        "ALERTS",
        "APM",
        "CHANGE_TRACKING",
        "COMMERCE",
        "CSSP",
        "DISCUSSIONS",
        "ERROR_TRACKING",
        "IINT",
        "NTFC",
        "PD",
        "SECURITY",
        "SHARING",
    )


class AiNotificationsResult(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FAIL", "SUCCESS")


class AiNotificationsSortOrder(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASC", "DESC")


class AiNotificationsSuggestionFilterType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CONTAINS", "STARTSWITH")


class AiNotificationsUiComponentType(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("DATE", "DATETIME", "EMAIL", "JSON", "NONE", "NUMBER", "URL")


class AiNotificationsVariableCategory(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("BOOLEAN", "LIST", "NUMBER", "OBJECT", "STRING")


class AiTopologyCollectorResultType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class AiTopologyCollectorVertexClass(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "APPLICATION",
        "BROWSERAPPLICATION",
        "CLOUDSERVICE",
        "CLUSTER",
        "DATASTORE",
        "HOST",
        "MONITOR",
        "TEAM",
    )


class AiTopologyVertexClass(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "APPLICATION",
        "BROWSERAPPLICATION",
        "CLOUDSERVICE",
        "CLUSTER",
        "DATASTORE",
        "HOST",
        "MONITOR",
        "TEAM",
    )


class AiWorkflowsBatchCreateMigratedWorkflowsErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "CHANNEL_NOT_FOUND",
        "DUPLICATE",
        "FAILED_CREATING_ISSUES_FILTER",
        "INVALID_PARAMETER",
        "LIMIT_REACHED",
        "UNAUTHORIZED_API_KEY",
        "UNSUPPORTED_CHANNEL_TYPE",
        "UNSUPPORTED_NOTIFICATION_TRIGGER",
        "VALIDATION_ERROR",
    )


class AiWorkflowsBatchDeleteMigratedWorkflowsErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "FAILED_DELETING_ISSUES_FILTER",
        "INVALID_PARAMETER",
        "UNAUTHORIZED_API_KEY",
        "VALIDATION_ERROR",
    )


class AiWorkflowsCreateErrorType(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("INVALID_PARAMETER", "UNAUTHORIZED_ACCOUNT", "VALIDATION_ERROR")


class AiWorkflowsDestinationType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "EMAIL",
        "EVENT_BRIDGE",
        "JIRA",
        "MICROSOFT_TEAMS",
        "PAGERDUTY_ACCOUNT_INTEGRATION",
        "PAGERDUTY_SERVICE_INTEGRATION",
        "SERVICE_NOW",
        "SERVICE_NOW_APP",
        "SLACK",
        "SLACK_LEGACY",
        "WEBHOOK",
        "WORKFLOW_AUTOMATION",
    )


class AiWorkflowsEnrichmentType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("NRQL",)


class AiWorkflowsFetchWorkflowsByIssuesFilterErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("UNAUTHORIZED_API_KEY", "VALIDATION_ERROR")


class AiWorkflowsFilterType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FILTER", "VIEW")


class AiWorkflowsMutingRulesHandling(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "DONT_NOTIFY_FULLY_MUTED_ISSUES",
        "DONT_NOTIFY_FULLY_OR_PARTIALLY_MUTED_ISSUES",
        "NOTIFY_ALL_ISSUES",
    )


class AiWorkflowsNotificationTrigger(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "ACKNOWLEDGED",
        "ACTIVATED",
        "CLOSED",
        "INVESTIGATING",
        "OTHER_UPDATES",
        "PRIORITY_CHANGED",
    )


class AiWorkflowsOperator(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class AiWorkflowsTestResponseStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class AiWorkflowsUpdateErrorType(sgqlc.types.Enum):
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


class AlertsActionOnMutingRuleWindowEnded(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CLOSE_ISSUES_ON_INACTIVE", "DO_NOTHING")


class AlertsAsNrqlSourceProduct(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "APM",
        "BROWSER",
        "INFRASTRUCTURE",
        "MOBILE",
        "NRQL",
        "SERVERS",
        "SYNTHETICS",
    )


class AlertsDayOfWeek(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("LAST_VALUE", "NONE", "STATIC")


class AlertsIncidentPreference(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("PER_CONDITION", "PER_CONDITION_AND_TARGET", "PER_POLICY")


class AlertsMutingRuleConditionGroupOperator(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("AND", "OR")


class AlertsMutingRuleConditionOperator(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("DAILY", "MONTHLY", "WEEKLY")


class AlertsMutingRuleStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACTIVE", "ENDED", "INACTIVE", "SCHEDULED")


class AlertsNotificationChannelCreateErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNotificationChannelDeleteErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "NOT_FOUND_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNotificationChannelType(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "NOT_FOUND_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNotificationChannelsAddToPolicyErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "NOT_FOUND_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNotificationChannelsRemoveFromPolicyErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "BAD_USER_INPUT",
        "FORBIDDEN_ERROR",
        "NOT_FOUND_ERROR",
        "SERVER_ERROR",
        "TOO_MANY_REQUESTS_ERROR",
    )


class AlertsNrqlBaselineDirection(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("LOWER_ONLY", "UPPER_AND_LOWER", "UPPER_ONLY")


class AlertsNrqlConditionPriority(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "WARNING")


class AlertsNrqlConditionTermsOperator(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("ALL", "AT_LEAST_ONCE")


class AlertsNrqlConditionType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BASELINE", "OUTLIER", "STATIC")


class AlertsNrqlDynamicConditionTermsOperator(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ABOVE",)


class AlertsNrqlSignalSeasonality(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DAILY", "HOURLY", "NEW_RELIC_CALCULATION", "NONE", "WEEKLY")


class AlertsNrqlStaticConditionValueFunction(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ()


class AlertsOpsGenieDataCenterRegion(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("EU", "US")


class AlertsSignalAggregationMethod(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CADENCE", "EVENT_FLOW", "EVENT_TIMER")


class AlertsViolationTimeLimit(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("FORM", "JSON")


class ApiAccessIngestKeyErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN", "INVALID", "NOT_FOUND")


class ApiAccessIngestKeyType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BROWSER", "LICENSE")


class ApiAccessKeyType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INGEST", "USER")


class ApiAccessUserKeyErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN", "INVALID", "NOT_FOUND")


class AuthorizationManagementGranteeTypeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("GROUP", "SYSTEM_IDENTITY", "SYSTEM_IDENTITY_GROUP", "USER")


class BrowserAgentInstallType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("LITE", "PRO", "PRO_SPA")


class ChangeTrackingCategoryType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "BUSINESS_EVENT__CONVENTION",
        "BUSINESS_EVENT__MARKETING_CAMPAIGN",
        "BUSINESS_EVENT__OTHER",
        "CUSTOMER_DEFINED__CUSTOM",
        "DEPLOYMENT_LIFECYCLE__ARTIFACT_COPY",
        "DEPLOYMENT_LIFECYCLE__ARTIFACT_DELETION",
        "DEPLOYMENT_LIFECYCLE__ARTIFACT_DEPLOYMENT",
        "DEPLOYMENT_LIFECYCLE__ARTIFACT_MOVE",
        "DEPLOYMENT_LIFECYCLE__BUILD_DELETION",
        "DEPLOYMENT_LIFECYCLE__BUILD_PROMOTION",
        "DEPLOYMENT_LIFECYCLE__BUILD_UPLOAD",
        "DEPLOYMENT_LIFECYCLE__IMAGE_DELETION",
        "DEPLOYMENT_LIFECYCLE__IMAGE_PROMOTION",
        "DEPLOYMENT_LIFECYCLE__IMAGE_PUSH",
        "DEPLOYMENT_LIFECYCLE__RELEASE_BUNDLE_CREATION",
        "DEPLOYMENT_LIFECYCLE__RELEASE_BUNDLE_DELETION",
        "DEPLOYMENT_LIFECYCLE__RELEASE_BUNDLE_SIGN",
        "DEPLOYMENT__BASIC",
        "DEPLOYMENT__BLUE_GREEN",
        "DEPLOYMENT__CANARY",
        "DEPLOYMENT__OTHER",
        "DEPLOYMENT__ROLLING",
        "DEPLOYMENT__SHADOW",
        "FEATURE_FLAG__BASIC",
        "OPERATIONAL__CRASH",
        "OPERATIONAL__OTHER",
        "OPERATIONAL__SCHEDULED_MAINTENANCE_PERIOD",
        "OPERATIONAL__SERVER_REBOOT",
    )


class ChangeTrackingDeploymentType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BASIC", "BLUE_GREEN", "CANARY", "OTHER", "ROLLING", "SHADOW")


class ChangeTrackingValidationFlag(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "ALLOW_CUSTOM_CATEGORY_OR_TYPE",
        "FAIL_ON_FIELD_LENGTH",
        "FAIL_ON_REST_API_FAILURES",
    )


class ChartFormatType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("PDF", "PNG")


class ChartImageType(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("PULL", "PUSH")


class CollaborationExternalApplicationType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CODESTREAM", "EMAIL", "SLACK", "TEAMS")


class CollaborationStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ARCHIVED", "CLOSED", "OPEN")


class DashboardAddWidgetsToPageErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN_OPERATION", "INVALID_INPUT", "PAGE_NOT_FOUND")


class DashboardAlertSeverity(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "NOT_ALERTING", "WARNING")


class DashboardCreateErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INVALID_INPUT",)


class DashboardDeleteErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DASHBOARD_NOT_FOUND", "FORBIDDEN_OPERATION")


class DashboardDeleteResultStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class DashboardEntityPermissions(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("PRIVATE", "PUBLIC_READ_ONLY", "PUBLIC_READ_WRITE")


class DashboardLiveUrlAuthType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("PASSWORD",)


class DashboardLiveUrlErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("OPERATION_FAILURE", "UNAUTHORIZED", "UNSUPPORTED", "URL_NOT_FOUND")


class DashboardLiveUrlType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DASHBOARD", "WIDGET")


class DashboardPermissions(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("PRIVATE", "PUBLIC_READ_ONLY", "PUBLIC_READ_WRITE")


class DashboardUndeleteErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DASHBOARD_NOT_FOUND", "FORBIDDEN_OPERATION")


class DashboardUpdateErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN_OPERATION", "INVALID_INPUT")


class DashboardUpdatePageErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN_OPERATION", "INVALID_INPUT", "PAGE_NOT_FOUND")


class DashboardUpdateWidgetsInPageErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "FORBIDDEN_OPERATION",
        "INVALID_INPUT",
        "PAGE_NOT_FOUND",
        "WIDGET_NOT_FOUND",
    )


class DashboardVariableReplacementStrategy(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DEFAULT", "IDENTIFIER", "NUMBER", "STRING")


class DashboardVariableType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ENUM", "NRQL", "STRING")


class DataDictionaryTextFormat(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("HTML", "MARKDOWN", "PLAIN")


class DataManagementCategory(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ALERTING", "INGEST", "QUERY")


class DataManagementType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("GAUGE", "RATE")


class DataManagementUnit(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BYTES", "COUNT", "GIGABYTES")


class DataSourceGapsGapTypeIdentifier(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "APACHE",
        "APM_AGENT_LOGS",
        "CASSANDRA",
        "CONSUL",
        "COUCHBASE",
        "ELASTICSEARCH",
        "GO",
        "HAPROXY",
        "INFRA_LOGS",
        "JAVA",
        "JMX",
        "MEMCACHED",
        "MICROSOFT_NET",
        "MICROSOFT_SQL_SERVER",
        "MONGODB",
        "MYSQL",
        "NAGIOS",
        "NGINX",
        "NODE_JS",
        "PHP",
        "PIXIE",
        "POSTGRESQL",
        "PYTHON",
        "RABBITMQ",
        "REDIS",
        "RUBY",
        "VARNISH",
    )


class DistributedTracingSpanAnomalyType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DURATION",)


class DistributedTracingSpanClientType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DATASTORE", "EXTERNAL")


class DistributedTracingSpanProcessBoundary(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ENTRY", "EXIT", "IN_PROCESS")


class EdgeComplianceTypeCode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FEDRAMP",)


class EdgeCreateSpanAttributeRuleResponseErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "DUPLICATE_RULES",
        "EXCEEDS_SPAN_ATTRIBUTE_RULE_LIMITS",
        "INVALID_INPUT",
        "NOT_FOUND",
        "OPPOSING_RULES",
    )


class EdgeCreateTraceObserverResponseErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ALREADY_EXISTS", "NO_AVAILABILITY_IN_REGION")


class EdgeDataSourceGroupUpdateType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ADD", "REMOVE", "REPLACE")


class EdgeDataSourceStatusType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACTIVE", "INACTIVE")


class EdgeDeleteSpanAttributeRuleResponseErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("NOT_FOUND",)


class EdgeDeleteTraceObserverResponseErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ALREADY_DELETED", "NOT_FOUND")


class EdgeEndpointStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CREATED", "DELETED")


class EdgeEndpointType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("PUBLIC",)


class EdgeProviderRegion(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("EQUALS", "LIKE")


class EdgeSpanAttributeValueOperator(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("EQUALS", "IS_NOT_NULL", "LIKE")


class EdgeTraceFilterAction(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DISCARD", "KEEP")


class EdgeTraceObserverStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CREATED", "DELETED")


class EdgeUpdateTraceObserverResponseErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INVALID_INPUT", "NOT_FOUND")


class EmbeddedChartType(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("CRITICAL", "NOT_ALERTING", "NOT_CONFIGURED", "WARNING")


class EntityCollectionType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("TEAM", "WORKLOAD", "WORKLOAD_STATUS_RULE_GROUP")


class EntityDeleteErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN", "INTERNAL_ERROR", "INVALID_INPUT")


class EntityGoldenEventObjectId(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DOMAIN_IDS", "ENTITY_GUIDS")


class EntityGoldenGoldenMetricsErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "INVALID_CONTEXT",
        "INVALID_DOMAIN_TYPE",
        "INVALID_QUERY_PARAMS",
        "LIMIT_EXCEEDED",
        "NOT_AUTHORIZED",
    )


class EntityGoldenMetricUnit(sgqlc.types.Enum):
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


class EntityManagementAiToolParameterType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BOOLEAN", "INTEGER", "LIST", "OBJECT", "STRING")


class EntityManagementAssignmentType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("NEW_RELIC_TEAM_ID", "NEW_RELIC_USER_ID")


class EntityManagementCategory(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CHAT", "INCIDENT", "ISSUE", "VULNERABILITY")


class EntityManagementCategoryScopeType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT", "GLOBAL")


class EntityManagementCommunicationMode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT_STATUS", "GLOBAL_STATUS")


class EntityManagementCommunicationStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("IDENTIFIED", "INVESTIGATING", "MONITORING", "RESOLVED")


class EntityManagementConsumptionMetric(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ADVANCED_CCU", "CCU", "CORE_CCU")


class EntityManagementDirection(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ONEWAY", "TWOWAY")


class EntityManagementEncodingName(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CL100_K_BASE", "GPT_3_5_TURBO", "O200_K_BASE")


class EntityManagementEncodingType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BASE64", "UTF8")


class EntityManagementEntityScope(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT", "ORGANIZATION")


class EntityManagementExecutionStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FAILED", "PARTIAL_SUCCESS", "SUCCESS")


class EntityManagementExternalOwnerType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("GROUP", "ORGANIZATION", "OTHER", "USER", "WORKSPACE")


class EntityManagementFleetDeploymentPhase(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("COMPLETED", "CREATED", "FAILED", "INTERNAL_FAILURE", "IN_PROGRESS")


class EntityManagementHostingPlatform(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BITBUCKET", "DEVLAKE", "GITHUB", "GITLAB", "OTHER")


class EntityManagementIncidentStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CLOSED", "ONGOING")


class EntityManagementInstallationStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INSTALLED", "UNINSTALLATION_IN_PROGRESS", "UNINSTALLED")


class EntityManagementIssueType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ERROR", "PERFORMANCE")


class EntityManagementJiraIssueType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BUG", "STORY", "TASK")


class EntityManagementKeyType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INGEST", "USER")


class EntityManagementLicenseName(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "AFL_3_0",
        "AGPL_3_0",
        "APACHE_2_0",
        "BSD_2_CLAUSE",
        "BSD_3_CLAUSE",
        "BSL_1_0",
        "CC0_1_0",
        "CDDL",
        "EPL_2_0",
        "GPL_2_0",
        "GPL_3_0",
        "GPL_3_0_ONLY",
        "GPL_3_0_PLUS",
        "LGPL_2_1",
        "LGPL_3_0",
        "LGPL_3_0_ONLY",
        "LGPL_3_0_PLUS",
        "MIT",
        "MPL_1_1",
        "MPL_2_0",
        "NA",
        "UNLICENSE",
    )


class EntityManagementManagedEntityType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("HOST", "KUBERNETESCLUSTER")


class EntityManagementMessageType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("JSON", "TEXT", "YAML")


class EntityManagementOverlapPolicy(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CANCEL", "SKIP")


class EntityManagementPriority(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("HIGH", "HIGHEST", "LOW", "LOWEST", "MEDIUM")


class EntityManagementRegion(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("EU", "STAGING", "US")


class EntityManagementSigningAlgorithm(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("RSA256",)


class EntityManagementStatusCode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("MISSING_DATA_SOURCE", "SYSTEM_ERROR")


class EntityManagementSyncConfigurationMode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ALL", "MESSAGES", "WORKITEM")


class EntityManagementSyncGroupRuleConditionType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CONTAINS", "ENDS_WITH", "STARTS_WITH")


class EntityManagementTeamExternalIntegrationType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("GITHUB_TEAM", "IAM_GROUP", "SERVICENOW_TEAM")


class EntityManagementTextSplitterType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "CHARACTER_TEXT_SPLITTER",
        "MARKDOWN_TEXT_SPLITTER",
        "TOKEN_TEXT_SPLITTER",
    )


class EntityRelationshipEdgeDirection(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BOTH", "INBOUND", "OUTBOUND")


class EntityRelationshipEdgeType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "BUILT_FROM",
        "BYPASS_CALLS",
        "CALLS",
        "CONNECTS_TO",
        "CONSUMES",
        "CONTAINS",
        "HOSTS",
        "IS",
        "MANAGES",
        "MEASURES",
        "MONITORS",
        "OPERATES_IN",
        "OWNS",
        "PRODUCES",
        "SECURES",
        "SERVES",
        "TRIGGERS",
    )


class EntityRelationshipType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ()


class EntityRelationshipUserDefinedCreateOrReplaceErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("LIMIT_EXCEEDED", "NOT_ALLOWED", "NOT_AUTHORIZED")


class EntityRelationshipUserDefinedDeleteErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("NOT_AUTHORIZED",)


class EntitySearchCountsFacet(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("APM", "BROWSER", "EXT", "INFRA", "MOBILE", "SYNTH")


class EntitySearchQueryBuilderType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("APPLICATION", "DASHBOARD", "HOST", "MONITOR", "WORKLOAD")


class EntitySearchSortCriteria(sgqlc.types.Enum):
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
        "TEAM_ENTITY",
        "THIRD_PARTY_SERVICE_ENTITY",
        "UNAVAILABLE_ENTITY",
        "WORKLOAD_ENTITY",
    )


class ErrorsInboxAssignErrorGroupErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("NOT_AUTHORIZED",)


class ErrorsInboxDirection(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DESC",)


class ErrorsInboxErrorGroupSortOrderField(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FIRST_SEEN", "LAST_OCCURRENCE_IN_WINDOW", "OCCURRENCES")


class ErrorsInboxErrorGroupState(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("IGNORED", "RESOLVED", "UNRESOLVED")


class ErrorsInboxEventSource(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "AWS_LAMBDA_INVOCATION_ERROR",
        "ERROR_TRACE",
        "EXCESSIVE_DATABASE_QUERY",
        "JAVA_SCRIPT_ERROR",
        "LARGE_HTTP_PAYLOAD_REQUEST",
        "MOBILE_CRASH",
        "MOBILE_HANDLED_EXCEPTION",
        "MOBILE_REQUEST_ERROR",
        "N_PLUS_ONE_DATABASE_QUERY",
        "SEQUENTIAL_DATABASE_QUERY",
        "SLOW_HTTP_REQUEST",
        "SLOW_SQL_TRACE",
        "SPAN",
        "TRANSACTION_ERROR",
        "VIDEO_ERROR_ACTION",
    )


class ErrorsInboxIssueType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ERROR", "PERFORMANCE")


class ErrorsInboxResourceType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("JIRA_ISSUE",)


class ErrorsInboxUpdateErrorGroupStateErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("NOT_AUTHORIZED",)


class EventsToMetricsErrorReason(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("GENERAL", "INVALID_INPUT", "USER_NOT_AUTHORIZED")


class HistoricalDataExportStatus(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = (
        "ALREADY_CONSENTED",
        "CONSENTED",
        "USER_NOT_AUTHORIZED_MISSING_CAPABILITY",
    )


class IncidentIntelligenceEnvironmentCreateEnvironmentResult(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = (
        "CURRENT_ACCOUNT_NOT_ENTITLED",
        "ENVIRONMENT_FOUND",
        "MULTIPLE_ENVIRONMENTS",
        "NO_ENVIRONMENT",
        "USER_NOT_AUTHORIZED_FOR_ACCOUNT",
    )


class IncidentIntelligenceEnvironmentDeleteEnvironmentResult(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "ACCOUNT_NOT_ENTITLED",
        "DELETED",
        "DOES_NOT_EXIST",
        "USER_NOT_AUTHORIZED",
        "USER_NOT_AUTHORIZED_MISSING_CAPABILITY",
    )


class IncidentIntelligenceEnvironmentDissentAccountsResult(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "CONSENTED_ACCOUNTS_NOT_FOUND",
        "DISSENTED",
        "USER_NOT_AUTHORIZED_MISSING_CAPABILITY",
    )


class IncidentIntelligenceEnvironmentEnvironmentKind(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CROSS_ACCOUNT_ENVIRONMENT", "SINGLE_ACCOUNT_ENVIRONMENT")


class IncidentIntelligenceEnvironmentSupportedEnvironmentKind(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CROSS_ACCOUNT", "SINGLE_AND_CROSS_ACCOUNT")


class InstallationInstallStateType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("COMPLETED", "STARTED")


class InstallationRecipeStatusType(sgqlc.types.Enum):
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


class KnowledgePublishStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ARCHIVED", "DRAFT", "ONLINE", "PENDING")


class KnowledgeSearchSortOption(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("MOST_RECENT", "MOST_RELEVANT")


class KnowledgeSearchSources(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ALL", "ARTICLES", "DOCS", "FORUM")


class LogConfigurationsCreateDataPartitionRuleErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "DUPLICATE_DATA_PARTITION_RULE_NAME",
        "INVALID_DATA_PARTITION_INPUT",
        "MAX_DATA_PARTITION_RULES",
    )


class LogConfigurationsDataPartitionRuleMatchingOperator(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("EQUALS", "LIKE")


class LogConfigurationsDataPartitionRuleMutationErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INVALID_ID", "INVALID_RULE", "NOT_FOUND")


class LogConfigurationsDataPartitionRuleRetentionPolicyType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("SECONDARY", "STANDARD")


class LogConfigurationsLiveArchiveRetentionPolicyType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("NONE", "STANDARD_ARCHIVE")


class LogConfigurationsObfuscationMethod(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("HASH_SHA256", "MASK")


class LogConfigurationsParsingRuleMutationErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INVALID_GROK", "INVALID_ID", "INVALID_NRQL", "NOT_FOUND")


class MachineLearningEncodingName(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CL_100_K_BASE", "GPT_3_5_TURBO", "O_200_K_BASE")


class MachineLearningFilterByKeys(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("KNOWLEDGE_CATEGORY",)


class MachineLearningOperator(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("EQUAL",)


class MachineLearningTextSplitterType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "CHARACTER_TEXT_SPLITTER",
        "MARKDOWN_TEXT_SPLITTER",
        "TOKEN_TEXT_SPLITTER",
    )


class MetricNormalizationCustomerRuleAction(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DENY_NEW_METRICS", "IGNORE", "REPLACE")


class MetricNormalizationRuleAction(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DENY_NEW_METRICS", "IGNORE", "REPLACE")


class MetricNormalizationRuleErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "CREATION_ERROR",
        "EDITION_ERROR",
        "RULE_NOT_FOUND",
        "VALIDATION_ERROR",
    )


class MultiTenantAuthorizationGrantScopeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT", "GROUP", "ORGANIZATION", "OTHER")


class MultiTenantAuthorizationGrantSortEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ID",)


class MultiTenantAuthorizationGranteeTypeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("GROUP", "SYSTEM_IDENTITY", "SYSTEM_IDENTITY_GROUP", "USER")


class MultiTenantAuthorizationPermissionCategoryEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DELETE", "MANAGE", "MODIFY", "OTHER", "READ", "VIEW")


class MultiTenantAuthorizationRoleScopeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT", "GROUP", "ORGANIZATION", "OTHER")


class MultiTenantAuthorizationRoleSortEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ID", "NAME", "SCOPE", "TYPE")


class MultiTenantAuthorizationRoleTypeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CUSTOM", "STANDARD")


class MultiTenantAuthorizationSortDirectionEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASCENDING", "DESCENDING")


class MultiTenantIdentityCapability(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "DELETE_GROUP",
        "GRANT_GROUP_MEMBERSHIP",
        "REVOKE_GROUP_MEMBERSHIP",
        "UPDATE_GROUP_NAME",
    )


class MultiTenantIdentityEmailVerificationState(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("NOT_VERIFIABLE", "PENDING", "VERIFIED")


class MultiTenantIdentitySortDirection(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASCENDING", "DESCENDING")


class MultiTenantIdentitySortKeyEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("AUTHENTICATION_DOMAIN_ID", "ID", "NAME")


class MultiTenantIdentityUserSortKey(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("EMAIL", "ID", "LAST_ACTIVE", "NAME", "TYPE")


class NerdStorageScope(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT", "ACTOR", "ENTITY")


class NerdStorageVaultActorScope(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CURRENT_USER",)


class NerdStorageVaultErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCESS_DENIED", "BAD_INPUT", "NOT_FOUND", "VALIDATION_FAILED")


class NerdStorageVaultResultStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FAILURE", "SUCCESS")


class NerdpackMutationErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "CAPABILITY_NOT_GRANTED",
        "DOWNSTREAM_ERROR",
        "NOT_FOUND",
        "TNC_NOT_ACCEPTED",
        "UNAUTHORIZED_ACCOUNT",
    )


class NerdpackMutationResult(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ERROR", "OK")


class NerdpackRemovedTagResponseType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("NOTHING_TO_REMOVE", "REMOVED")


class NerdpackSubscriptionAccessType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DIRECT", "INHERITED")


class NerdpackSubscriptionModel(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CORE", "GLOBAL", "OWNER_AND_ALLOWED")


class NerdpackVersionFilterFallback(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("LATEST_SEMVER",)


class Nr1CatalogAlertConditionType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BASELINE", "STATIC")


class Nr1CatalogInstallPlanDestination(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("APPLICATION", "CLOUD", "HOST", "KUBERNETES", "UNKNOWN")


class Nr1CatalogInstallPlanDirectiveMode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("LINK", "NERDLET", "TARGETED")


class Nr1CatalogInstallPlanOperatingSystem(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DARWIN", "LINUX", "WINDOWS")


class Nr1CatalogInstallPlanTargetType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("AGENT", "INTEGRATION", "ON_HOST_INTEGRATION", "UNKNOWN")


class Nr1CatalogInstallerType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INSTALL_PLAN",)


class Nr1CatalogMutationResult(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ERROR", "OK")


class Nr1CatalogNerdpackVisibility(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("GLOBAL", "OWNER_AND_ALLOWED")


class Nr1CatalogQuickstartAlertConditionType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BASELINE", "STATIC")


class Nr1CatalogRenderFormat(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("MARKDOWN",)


class Nr1CatalogSearchComponentType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ALERTS", "APPS", "DASHBOARDS", "DATA_SOURCES", "VISUALIZATIONS")


class Nr1CatalogSearchResultType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "ALERT_POLICY_TEMPLATE",
        "DASHBOARD_TEMPLATE",
        "DATA_SOURCE",
        "NERDPACK",
        "QUICKSTART",
    )


class Nr1CatalogSearchSortOption(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ALPHABETICAL", "POPULARITY", "RELEVANCE", "REVERSE_ALPHABETICAL")


class Nr1CatalogSubmitMetadataErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "NERDPACK_NOT_FOUND",
        "SERVER_ERROR",
        "UNAUTHORIZED",
        "UNSUPPORTED_TYPE",
        "VALIDATION_FAILED",
    )


class Nr1CatalogSupportLevel(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("COMMUNITY", "ENTERPRISE", "NEW_RELIC", "VERIFIED")


class Nr1CatalogSupportedEntityTypesMode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ALL", "NONE", "SPECIFIC")


class NrqlCancelQueryMutationRequestStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCEPTED", "REJECTED")


class NrqlDropRulesAction(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "DROP_ATTRIBUTES",
        "DROP_ATTRIBUTES_FROM_METRIC_AGGREGATES",
        "DROP_DATA",
    )


class NrqlDropRulesErrorReason(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "FEATURE_FLAG_DISABLED",
        "GENERAL",
        "INVALID_INPUT",
        "INVALID_QUERY",
        "RULE_NOT_FOUND",
        "USER_NOT_AUTHORIZED",
    )


class OrganizationAccountShareSortDirectionEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASCENDING", "DESCENDING")


class OrganizationAccountShareSortKeyEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT_ID", "TARGET_ORGANIZATION_NAME")


class OrganizationAccountSortDirectionEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASCENDING", "DESCENDING")


class OrganizationAccountSortKeyEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ID", "NAME")


class OrganizationAccountStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACTIVE", "CANCELED")


class OrganizationAuthenticationTypeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "HEROKU_SSO", "OIDC_SSO", "PASSWORD", "SAML_SSO")


class OrganizationBillingStructure(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT_HIERARCHY", "CUSTOMER_CONTRACT", "UNSTRUCTURED")


class OrganizationMembersOrganizationMemberType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("GROUP", "SYSTEM_IDENTITY", "SYSTEM_IDENTITY_GROUP", "USER")


class OrganizationOrganizationCreateJobResultStatusEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CREATED", "FAILED", "RUNNING", "SUCCEEDED")


class OrganizationOrganizationCreateJobStatusEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ALL", "CREATED", "FAILED", "RUNNING", "SUCCEEDED")


class OrganizationProvisioningTypeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "MANUAL", "SCIM")


class OrganizationProvisioningUnit(sgqlc.types.Enum):
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


class OrganizationRegionCodeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("EU01", "US01")


class OrganizationSharingMode(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "ALL",
        "MANAGED",
        "SHARED_WITH_OTHER_ORGANIZATIONS",
        "SHARED_WITH_THIS_ORGANIZATION",
    )


class OrganizationSortDirectionEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASCENDING", "DESCENDING")


class OrganizationSortKeyEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ID", "NAME")


class OrganizationUpdateErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INVALID_RECORD", "NOT_AUTHORIZED")


class PixieLinkPixieProjectErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "ALREADY_LINKED",
        "AUTO_CREATION_NOT_SUPPORTED",
        "INVALID_NEWRELIC_ACCOUNT",
        "INVALID_PIXIE_API_KEY",
        "UNLINKING_NOT_SUPPORTED",
    )


class PixieRecordPixieTosAcceptanceErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("MISSING_DATA",)


class ReferenceEntityCreateRepositoryErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FORBIDDEN", "INVALID_INPUT")


class RegionScope(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("GLOBAL", "IN_REGION")


class SecretsManagementScopeType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ACCOUNT", "ORGANIZATION")


class SecretsManagementSortDirection(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASC", "DESC")


class SecretsManagementSortKey(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CREATED_AT",)


class ServiceLevelEventsQuerySelectFunction(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("COUNT", "GET_CDF_COUNT", "GET_FIELD", "SUM")


class ServiceLevelObjectiveRollingTimeWindowUnit(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DAY",)


class SessionsClientType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("INTEGRATION", "NEW_RELIC_APP", "WEB")


class SessionsPrincipalType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("USER",)


class SortBy(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASC", "DESC")


class StreamingExportPayloadCompression(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "GZIP")


class StreamingExportStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "CREATION_FAILED",
        "CREATION_IN_PROGRESS",
        "DELETED",
        "DISABLED",
        "ENABLED",
    )


class SyntheticMonitorStatus(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DELETED", "DISABLED", "ENABLED", "FAULTY", "MUTED", "PAUSED")


class SyntheticMonitorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "BROKEN_LINKS",
        "BROWSER",
        "CERT_CHECK",
        "SCRIPT_API",
        "SCRIPT_BROWSER",
        "SIMPLE",
        "STEP_MONITOR",
    )


class SyntheticsBrowser(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CHROME", "EDGE", "FIREFOX", "NONE")


class SyntheticsDevice(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "DESKTOP",
        "MOBILE_LANDSCAPE",
        "MOBILE_PORTRAIT",
        "NONE",
        "TABLET_LANDSCAPE",
        "TABLET_PORTRAIT",
    )


class SyntheticsDeviceOrientation(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("LANDSCAPE", "NONE", "PORTRAIT")


class SyntheticsDeviceType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("MOBILE", "NONE", "TABLET")


class SyntheticsMonitorCreateErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "BAD_REQUEST",
        "INTERNAL_SERVER_ERROR",
        "NOT_FOUND",
        "PAYMENT_REQUIRED",
        "RATE_LIMITED",
        "TAGGING_ERROR",
        "UNAUTHORIZED",
        "UNKNOWN_ERROR",
    )


class SyntheticsMonitorDowntimeDayOfMonthOrdinal(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FIRST", "FOURTH", "LAST", "SECOND", "THIRD")


class SyntheticsMonitorDowntimeWeekDays(sgqlc.types.Enum):
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


class SyntheticsMonitorPeriod(sgqlc.types.Enum):
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
    __schema__ = nerdgraph
    __choices__ = ("DISABLED", "ENABLED")


class SyntheticsMonitorUpdateErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = (
        "BAD_REQUEST",
        "INTERNAL_SERVER_ERROR",
        "NOT_FOUND",
        "PAYMENT_REQUIRED",
        "RATE_LIMITED",
        "SCRIPT_ERROR",
        "TAGGING_ERROR",
        "UNAUTHORIZED",
        "UNKNOWN_ERROR",
    )


class SyntheticsPrivateLocationMutationErrorType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BAD_REQUEST", "INTERNAL_SERVER_ERROR", "NOT_FOUND", "UNAUTHORIZED")


class SyntheticsStepType(sgqlc.types.Enum):
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


class SystemIdentityIdentitySortFieldKey(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("CLIENT_ID", "ID", "NAME")


class SystemIdentitySortOrder(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASC", "DESC")


class TaggingMutationErrorType(sgqlc.types.Enum):
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


class UserManagementGroupSortKey(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DISPLAY_NAME", "ID")


class UserManagementRequestedTierName(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BASIC_USER_TIER", "CORE_USER_TIER", "FULL_USER_TIER")


class UserManagementSortDirection(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ASCENDING", "DESCENDING")


class UserManagementTypeEnum(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BASIC", "CORE", "FULL_PLATFORM")


class WhatsNewContentType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ANNOUNCEMENT", "EOL_ANNOUNCEMENT")


class WorkloadGroupRemainingEntitiesRuleBy(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ENTITY_TYPE", "NONE")


class WorkloadResultingGroupType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("REGULAR_GROUP", "REMAINING_ENTITIES")


class WorkloadRollupStrategy(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("BEST_STATUS_WINS", "WORST_STATUS_WINS")


class WorkloadRuleThresholdType(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("FIXED", "PERCENTAGE")


class WorkloadStatusSource(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("ROLLUP_RULE", "STATIC", "UNKNOWN", "WORKLOAD")


class WorkloadStatusValue(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DEGRADED", "DISRUPTED", "OPERATIONAL", "UNKNOWN")


class WorkloadStatusValueInput(sgqlc.types.Enum):
    __schema__ = nerdgraph
    __choices__ = ("DEGRADED", "DISRUPTED", "OPERATIONAL")
