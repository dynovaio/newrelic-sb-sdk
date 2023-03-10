__all__ = [
    "AccountManagementCreateInput",
    "AccountManagementUpdateInput",
    "AgentApplicationBrowserSettingsInput",
    "AgentApplicationSettingsApmConfigInput",
    "AgentApplicationSettingsBrowserAjaxInput",
    "AgentApplicationSettingsBrowserConfigInput",
    "AgentApplicationSettingsBrowserDistributedTracingInput",
    "AgentApplicationSettingsBrowserMonitoringInput",
    "AgentApplicationSettingsBrowserPrivacyInput",
    "AgentApplicationSettingsErrorCollectorInput",
    "AgentApplicationSettingsIgnoredStatusCodeRuleInput",
    "AgentApplicationSettingsJfrInput",
    "AgentApplicationSettingsMobileSettingsInput",
    "AgentApplicationSettingsNetworkAliasesInput",
    "AgentApplicationSettingsNetworkSettingsInput",
    "AgentApplicationSettingsSlowSqlInput",
    "AgentApplicationSettingsThreadProfilerInput",
    "AgentApplicationSettingsTracerTypeInput",
    "AgentApplicationSettingsTransactionTracerInput",
    "AgentApplicationSettingsUpdateInput",
    "AgentEnvironmentFilter",
    "AiDecisionsAllInput",
    "AiDecisionsAndInput",
    "AiDecisionsAttributeExistsInput",
    "AiDecisionsCategoricalClusteringInput",
    "AiDecisionsFixedContainsInput",
    "AiDecisionsFixedCosineDistanceInput",
    "AiDecisionsFixedEndsWithInput",
    "AiDecisionsFixedEqualInput",
    "AiDecisionsFixedFuzzyScoreInput",
    "AiDecisionsFixedFuzzyWuzzyAdaptiveRatioInput",
    "AiDecisionsFixedFuzzyWuzzyPartialRatioInput",
    "AiDecisionsFixedFuzzyWuzzyRatioInput",
    "AiDecisionsFixedFuzzyWuzzyTokenSetRatioInput",
    "AiDecisionsFixedGreaterThanInput",
    "AiDecisionsFixedGreaterThanOrEqualInput",
    "AiDecisionsFixedHammingDistanceInput",
    "AiDecisionsFixedJaccardDistanceInput",
    "AiDecisionsFixedJaroWinklerInput",
    "AiDecisionsFixedLessThanInput",
    "AiDecisionsFixedLessThanOrEqualInput",
    "AiDecisionsFixedLevenshteinInput",
    "AiDecisionsFixedLongestCommonSubsequenceDistanceInput",
    "AiDecisionsFixedNumericalEqualInput",
    "AiDecisionsFixedRegularExpressionInput",
    "AiDecisionsFixedSoundExInput",
    "AiDecisionsFixedStartsWithInput",
    "AiDecisionsIncidentObjectInput",
    "AiDecisionsNotInput",
    "AiDecisionsOneInput",
    "AiDecisionsOrInput",
    "AiDecisionsOverrideConfigurationInput",
    "AiDecisionsRelativeCommonPrefixInput",
    "AiDecisionsRelativeContainsInput",
    "AiDecisionsRelativeCosineDistanceInput",
    "AiDecisionsRelativeEndsWithInput",
    "AiDecisionsRelativeEqualInput",
    "AiDecisionsRelativeFuzzyScoreInput",
    "AiDecisionsRelativeFuzzyWuzzyAdaptiveRatioInput",
    "AiDecisionsRelativeFuzzyWuzzyPartialRatioInput",
    "AiDecisionsRelativeFuzzyWuzzyRatioInput",
    "AiDecisionsRelativeFuzzyWuzzyTokenSetRatioInput",
    "AiDecisionsRelativeGreaterThanInput",
    "AiDecisionsRelativeGreaterThanOrEqualInput",
    "AiDecisionsRelativeHammingDistanceInput",
    "AiDecisionsRelativeJaccardDistanceInput",
    "AiDecisionsRelativeJaroWinklerInput",
    "AiDecisionsRelativeLessThanInput",
    "AiDecisionsRelativeLessThanOrEqualInput",
    "AiDecisionsRelativeLevenshteinInput",
    "AiDecisionsRelativeLongestCommonSubsequenceDistanceInput",
    "AiDecisionsRelativeNumericalEqualInput",
    "AiDecisionsRelativeRegularExpressionInput",
    "AiDecisionsRelativeSoundExInput",
    "AiDecisionsRelativeStartsWithInput",
    "AiDecisionsRelativeTopologicallyDependentInput",
    "AiDecisionsRuleBlueprint",
    "AiDecisionsRuleExpressionInput",
    "AiDecisionsSearchBlueprint",
    "AiDecisionsSimulationBlueprint",
    "AiDecisionsSuggestionBlueprint",
    "AiDecisionsWholeCosineDistanceInput",
    "AiDecisionsWholeJaccardSimilarityInput",
    "AiIssuesFilterIncidents",
    "AiIssuesFilterIncidentsEvents",
    "AiIssuesFilterIssues",
    "AiIssuesFilterIssuesEvents",
    "AiIssuesGracePeriodConfigurationInput",
    "AiNotificationsBasicAuthInput",
    "AiNotificationsChannelFilter",
    "AiNotificationsChannelInput",
    "AiNotificationsChannelSorter",
    "AiNotificationsChannelUpdate",
    "AiNotificationsConstraint",
    "AiNotificationsCredentialsInput",
    "AiNotificationsDestinationFilter",
    "AiNotificationsDestinationInput",
    "AiNotificationsDestinationSorter",
    "AiNotificationsDestinationUpdate",
    "AiNotificationsDynamicVariable",
    "AiNotificationsExampleValue",
    "AiNotificationsOAuth2AuthInput",
    "AiNotificationsPropertyFilter",
    "AiNotificationsPropertyInput",
    "AiNotificationsSuggestionFilter",
    "AiNotificationsTokenAuthInput",
    "AiNotificationsVariableFilter",
    "AiNotificationsVariableSorter",
    "AiTopologyCollectorAttributeInput",
    "AiTopologyCollectorEdgeBlueprint",
    "AiTopologyCollectorVertexBlueprint",
    "AiWorkflowsCreateWorkflowInput",
    "AiWorkflowsDestinationConfigurationInput",
    "AiWorkflowsEnrichmentsInput",
    "AiWorkflowsFilterInput",
    "AiWorkflowsFilters",
    "AiWorkflowsNrqlConfigurationInput",
    "AiWorkflowsNrqlEnrichmentInput",
    "AiWorkflowsNrqlTestEnrichmentInput",
    "AiWorkflowsNrqlUpdateEnrichmentInput",
    "AiWorkflowsPredicateInput",
    "AiWorkflowsTestEnrichmentsInput",
    "AiWorkflowsTestWorkflowInput",
    "AiWorkflowsUpdateEnrichmentsInput",
    "AiWorkflowsUpdateWorkflowInput",
    "AiWorkflowsUpdatedFilterInput",
    "AlertsEmailNotificationChannelCreateInput",
    "AlertsEmailNotificationChannelUpdateInput",
    "AlertsMutingRuleConditionGroupInput",
    "AlertsMutingRuleConditionInput",
    "AlertsMutingRuleInput",
    "AlertsMutingRuleScheduleInput",
    "AlertsMutingRuleScheduleUpdateInput",
    "AlertsMutingRuleUpdateInput",
    "AlertsNotificationChannelCreateConfiguration",
    "AlertsNotificationChannelUpdateConfiguration",
    "AlertsNrqlConditionBaselineInput",
    "AlertsNrqlConditionExpirationInput",
    "AlertsNrqlConditionOutlierInput",
    "AlertsNrqlConditionQueryInput",
    "AlertsNrqlConditionSignalInput",
    "AlertsNrqlConditionStaticInput",
    "AlertsNrqlConditionTermsInput",
    "AlertsNrqlConditionUpdateBaselineInput",
    "AlertsNrqlConditionUpdateOutlierInput",
    "AlertsNrqlConditionUpdateQueryInput",
    "AlertsNrqlConditionUpdateStaticInput",
    "AlertsNrqlConditionsSearchCriteriaInput",
    "AlertsNrqlDynamicConditionTermsInput",
    "AlertsOpsGenieNotificationChannelCreateInput",
    "AlertsOpsGenieNotificationChannelUpdateInput",
    "AlertsPagerDutyNotificationChannelCreateInput",
    "AlertsPagerDutyNotificationChannelUpdateInput",
    "AlertsPoliciesSearchCriteriaInput",
    "AlertsPolicyInput",
    "AlertsPolicyUpdateInput",
    "AlertsSlackNotificationChannelCreateInput",
    "AlertsSlackNotificationChannelUpdateInput",
    "AlertsVictorOpsNotificationChannelCreateInput",
    "AlertsVictorOpsNotificationChannelUpdateInput",
    "AlertsWebhookBasicAuthMutationInput",
    "AlertsWebhookCustomHeaderMutationInput",
    "AlertsWebhookNotificationChannelCreateInput",
    "AlertsWebhookNotificationChannelUpdateInput",
    "AlertsXMattersNotificationChannelCreateInput",
    "AlertsXMattersNotificationChannelUpdateInput",
    "ApiAccessCreateIngestKeyInput",
    "ApiAccessCreateInput",
    "ApiAccessCreateUserKeyInput",
    "ApiAccessDeleteInput",
    "ApiAccessKeySearchQuery",
    "ApiAccessKeySearchScope",
    "ApiAccessUpdateIngestKeyInput",
    "ApiAccessUpdateInput",
    "ApiAccessUpdateUserKeyInput",
    "ApmApplicationEntitySettings",
    "AuthorizationManagementAccountAccessGrant",
    "AuthorizationManagementGrantAccess",
    "AuthorizationManagementOrganizationAccessGrant",
    "AuthorizationManagementRevokeAccess",
    "ChangeTrackingDeploymentInput",
    "ChangeTrackingSearchFilter",
    "ChangeTrackingTimeWindowInputWithDefaults",
    "CloudAlbIntegrationInput",
    "CloudApigatewayIntegrationInput",
    "CloudAutoscalingIntegrationInput",
    "CloudAwsAppsyncIntegrationInput",
    "CloudAwsAthenaIntegrationInput",
    "CloudAwsCognitoIntegrationInput",
    "CloudAwsConnectIntegrationInput",
    "CloudAwsDirectconnectIntegrationInput",
    "CloudAwsDisableIntegrationsInput",
    "CloudAwsDocdbIntegrationInput",
    "CloudAwsFsxIntegrationInput",
    "CloudAwsGlueIntegrationInput",
    "CloudAwsGovCloudLinkAccountInput",
    "CloudAwsGovCloudMigrateToAssumeroleInput",
    "CloudAwsGovcloudDisableIntegrationsInput",
    "CloudAwsGovcloudIntegrationsInput",
    "CloudAwsIntegrationsInput",
    "CloudAwsKinesisanalyticsIntegrationInput",
    "CloudAwsLinkAccountInput",
    "CloudAwsMediaconvertIntegrationInput",
    "CloudAwsMediapackagevodIntegrationInput",
    "CloudAwsMetadataIntegrationInput",
    "CloudAwsMqIntegrationInput",
    "CloudAwsMskIntegrationInput",
    "CloudAwsNeptuneIntegrationInput",
    "CloudAwsQldbIntegrationInput",
    "CloudAwsRoute53resolverIntegrationInput",
    "CloudAwsStatesIntegrationInput",
    "CloudAwsTagsGlobalIntegrationInput",
    "CloudAwsTransitgatewayIntegrationInput",
    "CloudAwsWafIntegrationInput",
    "CloudAwsWafv2IntegrationInput",
    "CloudAwsXrayIntegrationInput",
    "CloudAzureApimanagementIntegrationInput",
    "CloudAzureAppgatewayIntegrationInput",
    "CloudAzureAppserviceIntegrationInput",
    "CloudAzureContainersIntegrationInput",
    "CloudAzureCosmosdbIntegrationInput",
    "CloudAzureCostmanagementIntegrationInput",
    "CloudAzureDatafactoryIntegrationInput",
    "CloudAzureDisableIntegrationsInput",
    "CloudAzureEventhubIntegrationInput",
    "CloudAzureExpressrouteIntegrationInput",
    "CloudAzureFirewallsIntegrationInput",
    "CloudAzureFrontdoorIntegrationInput",
    "CloudAzureFunctionsIntegrationInput",
    "CloudAzureIntegrationsInput",
    "CloudAzureKeyvaultIntegrationInput",
    "CloudAzureLinkAccountInput",
    "CloudAzureLoadbalancerIntegrationInput",
    "CloudAzureLogicappsIntegrationInput",
    "CloudAzureMachinelearningIntegrationInput",
    "CloudAzureMariadbIntegrationInput",
    "CloudAzureMonitorIntegrationInput",
    "CloudAzureMysqlIntegrationInput",
    "CloudAzureMysqlflexibleIntegrationInput",
    "CloudAzurePostgresqlIntegrationInput",
    "CloudAzurePostgresqlflexibleIntegrationInput",
    "CloudAzurePowerbidedicatedIntegrationInput",
    "CloudAzureRediscacheIntegrationInput",
    "CloudAzureServicebusIntegrationInput",
    "CloudAzureSqlIntegrationInput",
    "CloudAzureSqlmanagedIntegrationInput",
    "CloudAzureStorageIntegrationInput",
    "CloudAzureVirtualmachineIntegrationInput",
    "CloudAzureVirtualnetworksIntegrationInput",
    "CloudAzureVmsIntegrationInput",
    "CloudAzureVpngatewaysIntegrationInput",
    "CloudBillingIntegrationInput",
    "CloudCloudfrontIntegrationInput",
    "CloudCloudtrailIntegrationInput",
    "CloudDisableAccountIntegrationInput",
    "CloudDisableIntegrationsInput",
    "CloudDynamodbIntegrationInput",
    "CloudEbsIntegrationInput",
    "CloudEc2IntegrationInput",
    "CloudEcsIntegrationInput",
    "CloudEfsIntegrationInput",
    "CloudElasticacheIntegrationInput",
    "CloudElasticbeanstalkIntegrationInput",
    "CloudElasticsearchIntegrationInput",
    "CloudElbIntegrationInput",
    "CloudEmrIntegrationInput",
    "CloudGcpAlloydbIntegrationInput",
    "CloudGcpAppengineIntegrationInput",
    "CloudGcpBigqueryIntegrationInput",
    "CloudGcpBigtableIntegrationInput",
    "CloudGcpComposerIntegrationInput",
    "CloudGcpDataflowIntegrationInput",
    "CloudGcpDataprocIntegrationInput",
    "CloudGcpDatastoreIntegrationInput",
    "CloudGcpDisableIntegrationsInput",
    "CloudGcpFirebasedatabaseIntegrationInput",
    "CloudGcpFirebasehostingIntegrationInput",
    "CloudGcpFirebasestorageIntegrationInput",
    "CloudGcpFirestoreIntegrationInput",
    "CloudGcpFunctionsIntegrationInput",
    "CloudGcpIntegrationsInput",
    "CloudGcpInterconnectIntegrationInput",
    "CloudGcpKubernetesIntegrationInput",
    "CloudGcpLinkAccountInput",
    "CloudGcpLoadbalancingIntegrationInput",
    "CloudGcpMemcacheIntegrationInput",
    "CloudGcpPubsubIntegrationInput",
    "CloudGcpRedisIntegrationInput",
    "CloudGcpRouterIntegrationInput",
    "CloudGcpRunIntegrationInput",
    "CloudGcpSpannerIntegrationInput",
    "CloudGcpSqlIntegrationInput",
    "CloudGcpStorageIntegrationInput",
    "CloudGcpVmsIntegrationInput",
    "CloudGcpVpcaccessIntegrationInput",
    "CloudHealthIntegrationInput",
    "CloudIamIntegrationInput",
    "CloudIntegrationsInput",
    "CloudIotIntegrationInput",
    "CloudKinesisFirehoseIntegrationInput",
    "CloudKinesisIntegrationInput",
    "CloudLambdaIntegrationInput",
    "CloudLinkCloudAccountsInput",
    "CloudRdsIntegrationInput",
    "CloudRedshiftIntegrationInput",
    "CloudRenameAccountsInput",
    "CloudRoute53IntegrationInput",
    "CloudS3IntegrationInput",
    "CloudSesIntegrationInput",
    "CloudSnsIntegrationInput",
    "CloudSqsIntegrationInput",
    "CloudTrustedadvisorIntegrationInput",
    "CloudUnlinkAccountsInput",
    "CloudVpcIntegrationInput",
    "DashboardAreaWidgetConfigurationInput",
    "DashboardBarWidgetConfigurationInput",
    "DashboardBillboardWidgetConfigurationInput",
    "DashboardBillboardWidgetThresholdInput",
    "DashboardInput",
    "DashboardLineWidgetConfigurationInput",
    "DashboardLiveUrlsFilterInput",
    "DashboardMarkdownWidgetConfigurationInput",
    "DashboardPageInput",
    "DashboardPieWidgetConfigurationInput",
    "DashboardSnapshotUrlInput",
    "DashboardSnapshotUrlTimeWindowInput",
    "DashboardTableWidgetConfigurationInput",
    "DashboardUpdatePageInput",
    "DashboardUpdateWidgetInput",
    "DashboardVariableDefaultItemInput",
    "DashboardVariableDefaultValueInput",
    "DashboardVariableEnumItemInput",
    "DashboardVariableInput",
    "DashboardVariableNrqlQueryInput",
    "DashboardWidgetConfigurationInput",
    "DashboardWidgetInput",
    "DashboardWidgetLayoutInput",
    "DashboardWidgetNrqlQueryInput",
    "DashboardWidgetVisualizationInput",
    "DataManagementAccountFeatureSettingInput",
    "DataManagementFeatureSettingLookup",
    "DataManagementRuleInput",
    "DateTimeWindowInput",
    "DomainTypeInput",
    "EdgeCreateSpanAttributeRuleInput",
    "EdgeCreateTraceFilterRulesInput",
    "EdgeCreateTraceObserverInput",
    "EdgeDataSourceGroupInput",
    "EdgeDeleteTraceFilterRulesInput",
    "EdgeDeleteTraceObserverInput",
    "EdgeRandomTraceFilterInput",
    "EdgeUpdateTraceObserverInput",
    "EntityGoldenContextInput",
    "EntityGoldenMetricInput",
    "EntityGoldenNrqlTimeWindowInput",
    "EntityGoldenTagInput",
    "EntityRelationshipEdgeFilter",
    "EntityRelationshipEdgeTypeFilter",
    "EntityRelationshipEntityDomainTypeFilter",
    "EntityRelationshipFilter",
    "EntitySearchOptions",
    "EntitySearchQueryBuilder",
    "EntitySearchQueryBuilderTag",
    "ErrorsInboxAssignErrorGroupInput",
    "ErrorsInboxAssignmentSearchFilterInput",
    "ErrorsInboxErrorEventInput",
    "ErrorsInboxErrorGroupSearchFilterInput",
    "ErrorsInboxErrorGroupSortOrderInput",
    "ErrorsInboxResourceFilterInput",
    "EventsToMetricsCreateRuleInput",
    "EventsToMetricsDeleteRuleInput",
    "EventsToMetricsUpdateRuleInput",
    "InstallationInstallStatusInput",
    "InstallationRecipeStatus",
    "InstallationStatusErrorInput",
    "LogConfigurationsCreateDataPartitionRuleInput",
    "LogConfigurationsCreateObfuscationActionInput",
    "LogConfigurationsCreateObfuscationExpressionInput",
    "LogConfigurationsCreateObfuscationRuleInput",
    "LogConfigurationsDataPartitionRuleMatchingCriteriaInput",
    "LogConfigurationsParsingRuleConfiguration",
    "LogConfigurationsPipelineConfigurationInput",
    "LogConfigurationsUpdateDataPartitionRuleInput",
    "LogConfigurationsUpdateObfuscationActionInput",
    "LogConfigurationsUpdateObfuscationExpressionInput",
    "LogConfigurationsUpdateObfuscationRuleInput",
    "MetricNormalizationCreateRuleInput",
    "MetricNormalizationEditRuleInput",
    "NerdStorageScopeInput",
    "NerdStorageVaultScope",
    "NerdStorageVaultWriteSecretInput",
    "NerdpackAllowListInput",
    "NerdpackCreationInput",
    "NerdpackDataFilter",
    "NerdpackOverrideVersionRules",
    "NerdpackRemoveVersionTagInput",
    "NerdpackSubscribeAccountsInput",
    "NerdpackTagVersionInput",
    "NerdpackUnsubscribeAccountsInput",
    "NerdpackVersionFilter",
    "Nr1CatalogCommunityContactChannelInput",
    "Nr1CatalogEmailContactChannelInput",
    "Nr1CatalogIssuesContactChannelInput",
    "Nr1CatalogSearchFilter",
    "Nr1CatalogSubmitMetadataInput",
    "Nr1CatalogSupportInput",
    "NrqlDropRulesCreateDropRuleInput",
    "NrqlQueryOptions",
    "OrganizationCreateSharedAccountInput",
    "OrganizationCustomerOrganizationFilterInput",
    "OrganizationProvisioningProductInput",
    "OrganizationProvisioningUnitOfMeasureInput",
    "OrganizationRevokeSharedAccountInput",
    "OrganizationUpdateInput",
    "OrganizationUpdateSharedAccountInput",
    "QueryHistoryQueryHistoryOptionsInput",
    "ReferenceEntityCreateRepositoryInput",
    "ServiceLevelEventsCreateInput",
    "ServiceLevelEventsQueryCreateInput",
    "ServiceLevelEventsQuerySelectCreateInput",
    "ServiceLevelEventsQuerySelectUpdateInput",
    "ServiceLevelEventsQueryUpdateInput",
    "ServiceLevelEventsUpdateInput",
    "ServiceLevelIndicatorCreateInput",
    "ServiceLevelIndicatorUpdateInput",
    "ServiceLevelObjectiveCreateInput",
    "ServiceLevelObjectiveRollingTimeWindowCreateInput",
    "ServiceLevelObjectiveRollingTimeWindowUpdateInput",
    "ServiceLevelObjectiveTimeWindowCreateInput",
    "ServiceLevelObjectiveTimeWindowUpdateInput",
    "ServiceLevelObjectiveUpdateInput",
    "SortCriterionWithDirection",
    "StreamingExportAwsInput",
    "StreamingExportAzureInput",
    "StreamingExportRuleInput",
    "SyntheticsCreateBrokenLinksMonitorInput",
    "SyntheticsCreateCertCheckMonitorInput",
    "SyntheticsCreateScriptApiMonitorInput",
    "SyntheticsCreateScriptBrowserMonitorInput",
    "SyntheticsCreateSimpleBrowserMonitorInput",
    "SyntheticsCreateSimpleMonitorInput",
    "SyntheticsCreateStepMonitorInput",
    "SyntheticsCustomHeaderInput",
    "SyntheticsDeviceEmulationInput",
    "SyntheticsLocationsInput",
    "SyntheticsPrivateLocationInput",
    "SyntheticsRuntimeInput",
    "SyntheticsScriptBrowserMonitorAdvancedOptionsInput",
    "SyntheticsScriptedMonitorLocationsInput",
    "SyntheticsSimpleBrowserMonitorAdvancedOptionsInput",
    "SyntheticsSimpleMonitorAdvancedOptionsInput",
    "SyntheticsStepInput",
    "SyntheticsStepMonitorAdvancedOptionsInput",
    "SyntheticsTag",
    "SyntheticsUpdateBrokenLinksMonitorInput",
    "SyntheticsUpdateCertCheckMonitorInput",
    "SyntheticsUpdateScriptApiMonitorInput",
    "SyntheticsUpdateScriptBrowserMonitorInput",
    "SyntheticsUpdateSimpleBrowserMonitorInput",
    "SyntheticsUpdateSimpleMonitorInput",
    "SyntheticsUpdateStepMonitorInput",
    "TaggingTagInput",
    "TaggingTagValueInput",
    "TimeWindowInput",
    "UserManagementCreateGroup",
    "UserManagementCreateUser",
    "UserManagementDeleteGroup",
    "UserManagementDeleteUser",
    "UserManagementUpdateGroup",
    "UserManagementUpdateUser",
    "UserManagementUsersGroupsInput",
    "UsersUserSearchQuery",
    "UsersUserSearchScope",
    "WhatsNewContentSearchQuery",
    "WorkloadAutomaticStatusInput",
    "WorkloadCreateInput",
    "WorkloadDuplicateInput",
    "WorkloadEntitySearchQueryInput",
    "WorkloadRegularRuleInput",
    "WorkloadRemainingEntitiesRuleInput",
    "WorkloadRemainingEntitiesRuleRollupInput",
    "WorkloadRollupInput",
    "WorkloadScopeAccountsInput",
    "WorkloadStaticStatusInput",
    "WorkloadStatusConfigInput",
    "WorkloadUpdateAutomaticStatusInput",
    "WorkloadUpdateCollectionEntitySearchQueryInput",
    "WorkloadUpdateInput",
    "WorkloadUpdateRegularRuleInput",
    "WorkloadUpdateStaticStatusInput",
    "WorkloadUpdateStatusConfigInput",
]


# pylint: disable=duplicate-code,unused-import,too-many-lines


import sgqlc.types
import sgqlc.types.datetime

from newrelic_sb_sdk.graphql.enums import (
    AgentApplicationBrowserLoader,
    AgentApplicationSettingsBrowserLoaderInput,
    AgentApplicationSettingsNetworkFilterMode,
    AgentApplicationSettingsRecordSqlEnum,
    AgentApplicationSettingsThresholdTypeEnum,
    AgentApplicationSettingsTracer,
    AiDecisionsIncidentSelect,
    AiDecisionsIssuePriority,
    AiDecisionsRuleSource,
    AiDecisionsRuleType,
    AiDecisionsVertexClass,
    AiIssuesIncidentState,
    AiIssuesIssueState,
    AiNotificationsAuthType,
    AiNotificationsChannelFields,
    AiNotificationsChannelType,
    AiNotificationsDestinationFields,
    AiNotificationsDestinationType,
    AiNotificationsProduct,
    AiNotificationsSortOrder,
    AiNotificationsSuggestionFilterType,
    AiNotificationsVariableFields,
    AiNotificationsVariableType,
    AiTopologyCollectorVertexClass,
    AiWorkflowsDestinationType,
    AiWorkflowsFilterType,
    AiWorkflowsMutingRulesHandling,
    AiWorkflowsNotificationTrigger,
    AiWorkflowsOperator,
    AlertsDayOfWeek,
    AlertsFillOption,
    AlertsIncidentPreference,
    AlertsMutingRuleConditionGroupOperator,
    AlertsMutingRuleConditionOperator,
    AlertsMutingRuleScheduleRepeat,
    AlertsNrqlBaselineDirection,
    AlertsNrqlConditionPriority,
    AlertsNrqlConditionTermsOperator,
    AlertsNrqlConditionThresholdOccurrences,
    AlertsNrqlDynamicConditionTermsOperator,
    AlertsNrqlStaticConditionValueFunction,
    AlertsOpsGenieDataCenterRegion,
    AlertsSignalAggregationMethod,
    AlertsViolationTimeLimit,
    AlertsWebhookCustomPayloadType,
    ApiAccessIngestKeyType,
    ApiAccessKeyType,
    ChangeTrackingDeploymentType,
    CloudMetricCollectionMode,
    DashboardAlertSeverity,
    DashboardLiveUrlType,
    DashboardPermissions,
    DashboardVariableReplacementStrategy,
    DashboardVariableType,
    EdgeComplianceTypeCode,
    EdgeDataSourceGroupUpdateType,
    EdgeProviderRegion,
    EdgeSpanAttributeKeyOperator,
    EdgeSpanAttributeValueOperator,
    EdgeTraceFilterAction,
    EntityAlertSeverity,
    EntityInfrastructureIntegrationType,
    EntityRelationshipEdgeDirection,
    EntityRelationshipEdgeType,
    EntitySearchQueryBuilderDomain,
    EntitySearchQueryBuilderType,
    EntitySearchSortCriteria,
    EntityType,
    ErrorsInboxDirection,
    ErrorsInboxErrorGroupSortOrderField,
    ErrorsInboxErrorGroupState,
    ErrorsInboxResourceType,
    InstallationInstallStateType,
    InstallationRecipeStatusType,
    LogConfigurationsDataPartitionRuleMatchingOperator,
    LogConfigurationsDataPartitionRuleRetentionPolicyType,
    LogConfigurationsObfuscationMethod,
    MetricNormalizationCustomerRuleAction,
    NerdpackSubscriptionModel,
    NerdpackVersionFilterFallback,
    NerdStorageScope,
    NerdStorageVaultActorScope,
    Nr1CatalogSearchComponentType,
    Nr1CatalogSearchResultType,
    NrqlDropRulesAction,
    OrganizationProvisioningUnit,
    ServiceLevelEventsQuerySelectFunction,
    ServiceLevelObjectiveRollingTimeWindowUnit,
    SortBy,
    SyntheticsDeviceOrientation,
    SyntheticsDeviceType,
    SyntheticsMonitorPeriod,
    SyntheticsMonitorStatus,
    SyntheticsStepType,
    UserManagementRequestedTierName,
    WhatsNewContentType,
    WorkloadGroupRemainingEntitiesRuleBy,
    WorkloadRollupStrategy,
    WorkloadRuleThresholdType,
    WorkloadStatusValueInput,
)
from newrelic_sb_sdk.graphql.scalars import (
    ID,
    AgentApplicationSettingsErrorCollectorHttpStatus,
    Boolean,
    DashboardWidgetRawConfiguration,
    DateTime,
    EntityGuid,
    EpochMilliseconds,
    EpochSeconds,
    Float,
    InstallationRawMetadata,
    Int,
    LogConfigurationsLogDataPartitionName,
    Milliseconds,
    NaiveDateTime,
    NerdpackTagName,
    Nrql,
    Seconds,
    SecureValue,
    SemVer,
    String,
)

from . import nerdgraph

__docformat__ = "markdown"


class AccountManagementCreateInput(sgqlc.types.Input):
    """Class for AccountManagementCreateInput.

    Attributes for creating an account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "region_code")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AccountManagementUpdateInput(sgqlc.types.Input):
    """Class for AccountManagementUpdateInput.

    The attributes for updating an account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")


class AgentApplicationBrowserSettingsInput(sgqlc.types.Input):
    """Class for AgentApplicationBrowserSettingsInput.

    Configure additional browser settings here.
    """

    __schema__ = nerdgraph
    __field_names__ = ("cookies_enabled", "distributed_tracing_enabled", "loader_type")
    cookies_enabled = sgqlc.types.Field(Boolean, graphql_name="cookiesEnabled")


class AgentApplicationSettingsApmConfigInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsApmConfigInput.

    Provides fields to set general APM application settings.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apdex_target", "use_server_side_config")
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class AgentApplicationSettingsBrowserAjaxInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsBrowserAjaxInput.

    Configuration settings related to how a browser agent handles Ajax
    requests.
    """

    __schema__ = nerdgraph
    __field_names__ = ("deny_list",)
    deny_list = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="denyList"
    )


class AgentApplicationSettingsBrowserConfigInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsBrowserConfigInput.

    Provides fields to set general browser application settings.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apdex_target",)
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class AgentApplicationSettingsBrowserDistributedTracingInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsBrowserDistributedTracingInput.

    Configure distributed traces from within browser apps.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "allowed_origins",
        "cors_enabled",
        "cors_use_newrelic_header",
        "cors_use_tracecontext_headers",
        "enabled",
        "exclude_newrelic_header",
    )
    allowed_origins = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="allowedOrigins"
    )


class AgentApplicationSettingsBrowserMonitoringInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsBrowserMonitoringInput.

    Set browser monitoring application settings.
    """

    __schema__ = nerdgraph
    __field_names__ = ("ajax", "distributed_tracing", "loader", "privacy")
    ajax = sgqlc.types.Field(
        AgentApplicationSettingsBrowserAjaxInput, graphql_name="ajax"
    )


class AgentApplicationSettingsBrowserPrivacyInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsBrowserPrivacyInput.

    Browser monitoring's page load timing feature can track sessions
    by using cookies that contain a simple session identifier.
    """

    __schema__ = nerdgraph
    __field_names__ = ("cookies_enabled",)
    cookies_enabled = sgqlc.types.Field(Boolean, graphql_name="cookiesEnabled")


class AgentApplicationSettingsErrorCollectorInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsErrorCollectorInput.

    The error collector captures information about uncaught exceptions
    and sends them to New Relic for viewing. For more information
    about what these settings do and which ones are applicable for
    your application, please see https://docs.newrelic.com for more
    information about agent configuration for your language agent.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "enabled",
        "expected_error_classes",
        "expected_error_codes",
        "ignored_error_classes",
        "ignored_error_codes",
    )
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsIgnoredStatusCodeRuleInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsIgnoredStatusCodeRuleInput.

    Input data that maps ignore status codes associated with different
    hosts.
    """

    __schema__ = nerdgraph
    __field_names__ = ("hosts", "status_codes")
    hosts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="hosts",
    )


class AgentApplicationSettingsJfrInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsJfrInput.

    In the Java agent (v8.0.0 or later), the Java Flight Recorder can
    be turned on to collect additional information about the
    application. This setting cannot be updated for non-java agents.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsMobileSettingsInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsMobileSettingsInput.

    Configure mobile settings here.
    """

    __schema__ = nerdgraph
    __field_names__ = ("network_settings", "use_crash_reports")
    network_settings = sgqlc.types.Field(
        "AgentApplicationSettingsNetworkSettingsInput", graphql_name="networkSettings"
    )


class AgentApplicationSettingsNetworkAliasesInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsNetworkAliasesInput.

    Input data that maps hosts to alias names for grouping and
    identification purposes.
    """

    __schema__ = nerdgraph
    __field_names__ = ("alias", "hosts")
    alias = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="alias")


class AgentApplicationSettingsNetworkSettingsInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsNetworkSettingsInput.

    Configure mobile network settings here.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aliases",
        "filter_mode",
        "hide_list",
        "ignored_status_code_rules",
        "show_list",
    )
    aliases = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AgentApplicationSettingsNetworkAliasesInput)
        ),
        graphql_name="aliases",
    )


class AgentApplicationSettingsSlowSqlInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsSlowSqlInput.

    In APM, when transaction traces are collected, there may be
    additional Slow query data available.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsThreadProfilerInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsThreadProfilerInput.

    Settings for the thread profiler.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsTracerTypeInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsTracerTypeInput.

    Input object for setting the type of tracing performed.
    """

    __schema__ = nerdgraph
    __field_names__ = ("value",)
    value = sgqlc.types.Field(AgentApplicationSettingsTracer, graphql_name="value")


class AgentApplicationSettingsTransactionTracerInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsTransactionTracerInput.

    Fields related to transaction traces and data collection for
    traces.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "capture_memcache_keys",
        "enabled",
        "explain_enabled",
        "explain_threshold_type",
        "explain_threshold_value",
        "log_sql",
        "record_sql",
        "stack_trace_threshold",
        "transaction_threshold_type",
        "transaction_threshold_value",
    )
    capture_memcache_keys = sgqlc.types.Field(
        Boolean, graphql_name="captureMemcacheKeys"
    )


class AgentApplicationSettingsUpdateInput(sgqlc.types.Input):
    """Class for AgentApplicationSettingsUpdateInput.

    The new settings to use - leave blank any settings you do not wish
    to modify.  While all settings can be specified here, some may not
    affect your installed agents, depending on the language agent and
    the current version installed. Note: not all settings of your
    agent are available to be set server-side.   Please see
    docs.newrelic.com for more information about the capabilities of
    individual agents.  [Go agent
    configuration](https://docs.newrelic.com/docs/agents/go-
    agent/configuration/go-agent-configuration/)  [Java agent
    configuration](https://docs.newrelic.com/docs/agents/java-
    agent/configuration/java-agent-configuration-config-file/)  [.Net
    agent configuration](https://docs.newrelic.com/docs/agents/net-
    agent/configuration/net-agent-configuration/)  [nodejs agent
    configuration](https://docs.newrelic.com/docs/agents/nodejs-
    agent/installation-configuration/nodejs-agent-configuration/)
    [PHP agent
    configuration](https://docs.newrelic.com/docs/agents/php-
    agent/configuration/php-agent-configuration/)  [Python agent
    configuration](https://docs.newrelic.com/docs/agents/python-
    agent/configuration/python-agent-configuration/)  [Ruby agent
    configuration](https://docs.newrelic.com/docs/agents/ruby-
    agent/configuration/ruby-agent-configuration/).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "alias",
        "apm_config",
        "browser_config",
        "browser_monitoring",
        "error_collector",
        "jfr",
        "mobile_settings",
        "name",
        "slow_sql",
        "thread_profiler",
        "tracer_type",
        "transaction_tracer",
    )
    alias = sgqlc.types.Field(String, graphql_name="alias")


class AgentEnvironmentFilter(sgqlc.types.Input):
    """Class for AgentEnvironmentFilter.

    A filter that can be applied to filter results.
    """

    __schema__ = nerdgraph
    __field_names__ = ("contains", "does_not_contain", "equals", "starts_with")
    contains = sgqlc.types.Field(String, graphql_name="contains")


class AiDecisionsAllInput(sgqlc.types.Input):
    """Class for AiDecisionsAllInput.

    Input type for All expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("children",)
    children = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiDecisionsRuleExpressionInput"))
        ),
        graphql_name="children",
    )


class AiDecisionsAndInput(sgqlc.types.Input):
    """Class for AiDecisionsAndInput.

    Input type for And expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsRuleExpressionInput"), graphql_name="left"
    )


class AiDecisionsAttributeExistsInput(sgqlc.types.Input):
    """Class for AiDecisionsAttributeExistsInput.

    Input type for AttributeExists expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident",)
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsCategoricalClusteringInput(sgqlc.types.Input):
    """Class for AiDecisionsCategoricalClusteringInput.

    Input type for CategoricalClustering expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("threshold",)
    threshold = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="threshold")


class AiDecisionsFixedContainsInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedContainsInput.

    Input type for FixedContains expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("container", "value")
    container = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="container"
    )


class AiDecisionsFixedCosineDistanceInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedCosineDistanceInput.

    Input type for FixedCosineDistance expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedEndsWithInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedEndsWithInput.

    Input type for FixedEndsWith expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedEqualInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedEqualInput.

    Input type for FixedEqual expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedFuzzyScoreInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedFuzzyScoreInput.

    Input type for FixedFuzzyScore expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedFuzzyWuzzyAdaptiveRatioInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedFuzzyWuzzyAdaptiveRatioInput.

    Input type for FixedFuzzyWuzzyAdaptiveRatio expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_similarity", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedFuzzyWuzzyPartialRatioInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedFuzzyWuzzyPartialRatioInput.

    Input type for FixedFuzzyWuzzyPartialRatio expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_similarity", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedFuzzyWuzzyRatioInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedFuzzyWuzzyRatioInput.

    Input type for FixedFuzzyWuzzyRatio expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_similarity", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedFuzzyWuzzyTokenSetRatioInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedFuzzyWuzzyTokenSetRatioInput.

    Input type for FixedFuzzyWuzzyTokenSetRatio expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_similarity", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedGreaterThanInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedGreaterThanInput.

    Input type for FixedGreaterThan expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")


class AiDecisionsFixedGreaterThanOrEqualInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedGreaterThanOrEqualInput.

    Input type for FixedGreaterThanOrEqual expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")


class AiDecisionsFixedHammingDistanceInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedHammingDistanceInput.

    Input type for FixedHammingDistance expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedJaccardDistanceInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedJaccardDistanceInput.

    Input type for FixedJaccardDistance expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedJaroWinklerInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedJaroWinklerInput.

    Input type for FixedJaroWinkler expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedLessThanInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedLessThanInput.

    Input type for FixedLessThan expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")


class AiDecisionsFixedLessThanOrEqualInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedLessThanOrEqualInput.

    Input type for FixedLessThanOrEqual expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")


class AiDecisionsFixedLevenshteinInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedLevenshteinInput.

    Input type for FixedLevenshtein expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedLongestCommonSubsequenceDistanceInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedLongestCommonSubsequenceDistanceInput.

    Input type for FixedLongestCommonSubsequenceDistance expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedNumericalEqualInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedNumericalEqualInput.

    Input type for FixedNumericalEqual expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")


class AiDecisionsFixedRegularExpressionInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedRegularExpressionInput.

    Input type for FixedRegularExpression expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedSoundExInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedSoundExInput.

    Input type for FixedSoundEx expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedStartsWithInput(sgqlc.types.Input):
    """Class for AiDecisionsFixedStartsWithInput.

    Input type for FixedStartsWith expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsIncidentObjectInput(sgqlc.types.Input):
    """Class for AiDecisionsIncidentObjectInput.

    Represents an attribute of an incident.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "select")
    attribute = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attribute"
    )


class AiDecisionsNotInput(sgqlc.types.Input):
    """Class for AiDecisionsNotInput.

    Input type for Not expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("child",)
    child = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsRuleExpressionInput"), graphql_name="child"
    )


class AiDecisionsOneInput(sgqlc.types.Input):
    """Class for AiDecisionsOneInput.

    Input type for One expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("children",)
    children = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiDecisionsRuleExpressionInput"))
        ),
        graphql_name="children",
    )


class AiDecisionsOrInput(sgqlc.types.Input):
    """Class for AiDecisionsOrInput.

    Input type for Or expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsRuleExpressionInput"), graphql_name="left"
    )


class AiDecisionsOverrideConfigurationInput(sgqlc.types.Input):
    """Class for AiDecisionsOverrideConfigurationInput.

    Configuration for overriding properties of issues created by
    merges.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "priority", "title")
    description = sgqlc.types.Field(String, graphql_name="description")


class AiDecisionsRelativeCommonPrefixInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeCommonPrefixInput.

    Input type for RelativeCommonPrefix expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("value",)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsRelativeContainsInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeContainsInput.

    Input type for RelativeContains expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("contained", "container")
    contained = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="contained"
    )


class AiDecisionsRelativeCosineDistanceInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeCosineDistanceInput.

    Input type for RelativeCosineDistance expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeEndsWithInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeEndsWithInput.

    Input type for RelativeEndsWith expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("contained", "container")
    contained = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="contained"
    )


class AiDecisionsRelativeEqualInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeEqualInput.

    Input type for RelativeEqual expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeFuzzyScoreInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeFuzzyScoreInput.

    Input type for RelativeFuzzyScore expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "min_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeFuzzyWuzzyAdaptiveRatioInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeFuzzyWuzzyAdaptiveRatioInput.

    Input type for RelativeFuzzyWuzzyAdaptiveRatio expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "min_similarity", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeFuzzyWuzzyPartialRatioInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeFuzzyWuzzyPartialRatioInput.

    Input type for RelativeFuzzyWuzzyPartialRatio expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "min_similarity", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeFuzzyWuzzyRatioInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeFuzzyWuzzyRatioInput.

    Input type for RelativeFuzzyWuzzyRatio expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "min_similarity", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeFuzzyWuzzyTokenSetRatioInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeFuzzyWuzzyTokenSetRatioInput.

    Input type for RelativeFuzzyWuzzyTokenSetRatio expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "min_similarity", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeGreaterThanInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeGreaterThanInput.

    Input type for RelativeGreaterThan expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeGreaterThanOrEqualInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeGreaterThanOrEqualInput.

    Input type for RelativeGreaterThanOrEqual expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeHammingDistanceInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeHammingDistanceInput.

    Input type for RelativeHammingDistance expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeJaccardDistanceInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeJaccardDistanceInput.

    Input type for RelativeJaccardDistance expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeJaroWinklerInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeJaroWinklerInput.

    Input type for RelativeJaroWinkler expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "min_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeLessThanInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeLessThanInput.

    Input type for RelativeLessThan expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeLessThanOrEqualInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeLessThanOrEqualInput.

    Input type for RelativeLessThanOrEqual expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeLevenshteinInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeLevenshteinInput.

    Input type for RelativeLevenshtein expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeLongestCommonSubsequenceDistanceInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeLongestCommonSubsequenceDistanceInput.

    Input type for RelativeLongestCommonSubsequenceDistance expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeNumericalEqualInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeNumericalEqualInput.

    Input type for RelativeNumericalEqual expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeRegularExpressionInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeRegularExpressionInput.

    Input type for RelativeRegularExpression expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "right", "value")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeSoundExInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeSoundExInput.

    Input type for RelativeSoundEx expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("left", "min_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )


class AiDecisionsRelativeStartsWithInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeStartsWithInput.

    Input type for RelativeStartsWith expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("contained", "container")
    contained = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="contained"
    )


class AiDecisionsRelativeTopologicallyDependentInput(sgqlc.types.Input):
    """Class for AiDecisionsRelativeTopologicallyDependentInput.

    Input type for RelativeTopologicallyDependent expression.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "from_",
        "graph_id",
        "max_hops",
        "required_attributes",
        "required_classes",
        "to",
    )
    from_ = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))),
        graphql_name="from",
    )


class AiDecisionsRuleBlueprint(sgqlc.types.Input):
    """Class for AiDecisionsRuleBlueprint.

    Blueprint for rule creation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "correlation_window_length",
        "creator",
        "description",
        "min_correlation_threshold",
        "name",
        "override_configuration",
        "rule_expression",
        "rule_type",
        "source",
    )
    correlation_window_length = sgqlc.types.Field(
        Milliseconds, graphql_name="correlationWindowLength"
    )


class AiDecisionsRuleExpressionInput(sgqlc.types.Input):
    """Class for AiDecisionsRuleExpressionInput.

    Rule expression input.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "all",
        "and_",
        "attribute_exists",
        "categorical_clustering",
        "fixed_contains",
        "fixed_cosine_distance",
        "fixed_ends_with",
        "fixed_equal",
        "fixed_fuzzy_score",
        "fixed_fuzzy_wuzzy_adaptive_ratio",
        "fixed_fuzzy_wuzzy_partial_ratio",
        "fixed_fuzzy_wuzzy_ratio",
        "fixed_fuzzy_wuzzy_token_set_ratio",
        "fixed_greater_than",
        "fixed_greater_than_or_equal",
        "fixed_hamming_distance",
        "fixed_jaccard_distance",
        "fixed_jaro_winkler",
        "fixed_less_than",
        "fixed_less_than_or_equal",
        "fixed_levenshtein",
        "fixed_longest_common_subsequence_distance",
        "fixed_numerical_equal",
        "fixed_regular_expression",
        "fixed_sound_ex",
        "fixed_starts_with",
        "not_",
        "one",
        "or_",
        "relative_common_prefix",
        "relative_contains",
        "relative_cosine_distance",
        "relative_ends_with",
        "relative_equal",
        "relative_fuzzy_score",
        "relative_fuzzy_wuzzy_adaptive_ratio",
        "relative_fuzzy_wuzzy_partial_ratio",
        "relative_fuzzy_wuzzy_ratio",
        "relative_fuzzy_wuzzy_token_set_ratio",
        "relative_greater_than",
        "relative_greater_than_or_equal",
        "relative_hamming_distance",
        "relative_jaccard_distance",
        "relative_jaro_winkler",
        "relative_less_than",
        "relative_less_than_or_equal",
        "relative_levenshtein",
        "relative_longest_common_subsequence_distance",
        "relative_numerical_equal",
        "relative_regular_expression",
        "relative_sound_ex",
        "relative_starts_with",
        "relative_topologically_dependent",
        "whole_cosine_distance",
        "whole_jaccard_similarity",
    )
    all = sgqlc.types.Field(AiDecisionsAllInput, graphql_name="all")


class AiDecisionsSearchBlueprint(sgqlc.types.Input):
    """Class for AiDecisionsSearchBlueprint.

    Blueprint for a search operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("expression", "limit", "retention_window_length")
    expression = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsRuleExpressionInput), graphql_name="expression"
    )


class AiDecisionsSimulationBlueprint(sgqlc.types.Input):
    """Class for AiDecisionsSimulationBlueprint.

    Blueprint for simulation creation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "correlation_window_length",
        "expression",
        "min_correlation_threshold",
        "retention_window_length",
    )
    correlation_window_length = sgqlc.types.Field(
        Milliseconds, graphql_name="correlationWindowLength"
    )


class AiDecisionsSuggestionBlueprint(sgqlc.types.Input):
    """Class for AiDecisionsSuggestionBlueprint.

    Blueprint for suggestion creation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "correlation_window_length",
        "description",
        "hash",
        "min_correlation_threshold",
        "name",
        "override_configuration",
        "rule_expression",
        "suggester",
        "support",
    )
    correlation_window_length = sgqlc.types.Field(
        Milliseconds, graphql_name="correlationWindowLength"
    )


class AiDecisionsWholeCosineDistanceInput(sgqlc.types.Input):
    """Class for AiDecisionsWholeCosineDistanceInput.

    Input type for WholeCosineDistance expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("max_distance",)
    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="maxDistance"
    )


class AiDecisionsWholeJaccardSimilarityInput(sgqlc.types.Input):
    """Class for AiDecisionsWholeJaccardSimilarityInput.

    Input type for WholeJaccardSimilarity expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("threshold",)
    threshold = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="threshold")


class AiIssuesFilterIncidents(sgqlc.types.Input):
    """Class for AiIssuesFilterIncidents.

    Filter incidents.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_types", "ids", "priority", "states")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )


class AiIssuesFilterIncidentsEvents(sgqlc.types.Input):
    """Class for AiIssuesFilterIncidentsEvents.

    Filter incidents events.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_types", "ids")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )


class AiIssuesFilterIssues(sgqlc.types.Input):
    """Class for AiIssuesFilterIssues.

    Filter issues.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_types", "ids", "priority", "states")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )


class AiIssuesFilterIssuesEvents(sgqlc.types.Input):
    """Class for AiIssuesFilterIssuesEvents.

    Filter issues events.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_types", "ids")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )


class AiIssuesGracePeriodConfigurationInput(sgqlc.types.Input):
    """Class for AiIssuesGracePeriodConfigurationInput.

    Grace periods for issue to be activated per priority.
    """

    __schema__ = nerdgraph
    __field_names__ = ("critical", "high", "low", "medium")
    critical = sgqlc.types.Field(sgqlc.types.non_null(Seconds), graphql_name="critical")


class AiNotificationsBasicAuthInput(sgqlc.types.Input):
    """Class for AiNotificationsBasicAuthInput.

    Basic auth input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("password", "user")
    password = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="password"
    )


class AiNotificationsChannelFilter(sgqlc.types.Input):
    """Class for AiNotificationsChannelFilter.

    Filter channel object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "active",
        "destination_id",
        "id",
        "ids",
        "name",
        "product",
        "property",
        "type",
    )
    active = sgqlc.types.Field(Boolean, graphql_name="active")


class AiNotificationsChannelInput(sgqlc.types.Input):
    """Class for AiNotificationsChannelInput.

    Channel input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("destination_id", "name", "product", "properties", "type")
    destination_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="destinationId"
    )


class AiNotificationsChannelSorter(sgqlc.types.Input):
    """Class for AiNotificationsChannelSorter.

    Sort object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("direction", "field")
    direction = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsSortOrder), graphql_name="direction"
    )


class AiNotificationsChannelUpdate(sgqlc.types.Input):
    """Class for AiNotificationsChannelUpdate.

    Channel update object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("active", "name", "properties")
    active = sgqlc.types.Field(Boolean, graphql_name="active")


class AiNotificationsConstraint(sgqlc.types.Input):
    """Class for AiNotificationsConstraint.

    List of schema/suggestions constraints.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class AiNotificationsCredentialsInput(sgqlc.types.Input):
    """Class for AiNotificationsCredentialsInput.

    Credential input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("basic", "oauth2", "token", "type")
    basic = sgqlc.types.Field(AiNotificationsBasicAuthInput, graphql_name="basic")


class AiNotificationsDestinationFilter(sgqlc.types.Input):
    """Class for AiNotificationsDestinationFilter.

    Filter destination object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "active",
        "auth_type",
        "id",
        "ids",
        "name",
        "property",
        "type",
        "updated_at",
    )
    active = sgqlc.types.Field(Boolean, graphql_name="active")


class AiNotificationsDestinationInput(sgqlc.types.Input):
    """Class for AiNotificationsDestinationInput.

    Destination input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("auth", "name", "properties", "type")
    auth = sgqlc.types.Field(AiNotificationsCredentialsInput, graphql_name="auth")


class AiNotificationsDestinationSorter(sgqlc.types.Input):
    """Class for AiNotificationsDestinationSorter.

    Sort object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("direction", "field")
    direction = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsSortOrder), graphql_name="direction"
    )


class AiNotificationsDestinationUpdate(sgqlc.types.Input):
    """Class for AiNotificationsDestinationUpdate.

    Destination update object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("active", "auth", "disable_auth", "name", "properties")
    active = sgqlc.types.Field(Boolean, graphql_name="active")


class AiNotificationsDynamicVariable(sgqlc.types.Input):
    """Class for AiNotificationsDynamicVariable.

    A list of dynamic variables used by the Channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("example_value", "name")
    example_value = sgqlc.types.Field(
        "AiNotificationsExampleValue", graphql_name="exampleValue"
    )


class AiNotificationsExampleValue(sgqlc.types.Input):
    """Class for AiNotificationsExampleValue.

    Example properties to be added to the rendering context, for tests.
    """

    __schema__ = nerdgraph
    __field_names__ = ("example", "type")
    example = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="example")


class AiNotificationsOAuth2AuthInput(sgqlc.types.Input):
    """Class for AiNotificationsOAuth2AuthInput.

    OAuth2 auth input object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "access_token_url",
        "authorization_url",
        "client_id",
        "client_secret",
        "prefix",
        "refresh_interval",
        "refresh_token",
        "refreshable",
        "scope",
        "token",
    )
    access_token_url = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="accessTokenUrl"
    )


class AiNotificationsPropertyFilter(sgqlc.types.Input):
    """Class for AiNotificationsPropertyFilter.

    Filter object by property.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class AiNotificationsPropertyInput(sgqlc.types.Input):
    """Class for AiNotificationsPropertyInput.

    Property object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_value", "key", "label", "value")
    display_value = sgqlc.types.Field(String, graphql_name="displayValue")


class AiNotificationsSuggestionFilter(sgqlc.types.Input):
    """Class for AiNotificationsSuggestionFilter.

    Suggestion filter object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type", "value")
    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsSuggestionFilterType), graphql_name="type"
    )


class AiNotificationsTokenAuthInput(sgqlc.types.Input):
    """Class for AiNotificationsTokenAuthInput.

    Token auth input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("prefix", "token")
    prefix = sgqlc.types.Field(String, graphql_name="prefix")


class AiNotificationsVariableFilter(sgqlc.types.Input):
    """Class for AiNotificationsVariableFilter.

    Filter variable object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("active", "key", "label", "name", "product")
    active = sgqlc.types.Field(Boolean, graphql_name="active")


class AiNotificationsVariableSorter(sgqlc.types.Input):
    """Class for AiNotificationsVariableSorter.

    Sort object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("direction", "field")
    direction = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsSortOrder), graphql_name="direction"
    )


class AiTopologyCollectorAttributeInput(sgqlc.types.Input):
    """Class for AiTopologyCollectorAttributeInput.

    A key-value entry.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class AiTopologyCollectorEdgeBlueprint(sgqlc.types.Input):
    """Class for AiTopologyCollectorEdgeBlueprint.

    Blueprint for edge creation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("directed", "from_vertex_name", "to_vertex_name")
    directed = sgqlc.types.Field(Boolean, graphql_name="directed")


class AiTopologyCollectorVertexBlueprint(sgqlc.types.Input):
    """Class for AiTopologyCollectorVertexBlueprint.

    Blueprint for vertex creation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("defining_attributes", "name", "vertex_class")
    defining_attributes = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiTopologyCollectorAttributeInput))
        ),
        graphql_name="definingAttributes",
    )


class AiWorkflowsCreateWorkflowInput(sgqlc.types.Input):
    """Class for AiWorkflowsCreateWorkflowInput.

    Workflow input object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "destination_configurations",
        "destinations_enabled",
        "enrichments",
        "enrichments_enabled",
        "issues_filter",
        "muting_rules_handling",
        "name",
        "workflow_enabled",
    )
    destination_configurations = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null("AiWorkflowsDestinationConfigurationInput")
            )
        ),
        graphql_name="destinationConfigurations",
    )


class AiWorkflowsDestinationConfigurationInput(sgqlc.types.Input):
    """Class for AiWorkflowsDestinationConfigurationInput.

    Destination Configuration input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("channel_id", "notification_triggers")
    channel_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="channelId")


class AiWorkflowsEnrichmentsInput(sgqlc.types.Input):
    """Class for AiWorkflowsEnrichmentsInput.

    Enrichment input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql",)
    nrql = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiWorkflowsNrqlEnrichmentInput"))
        ),
        graphql_name="nrql",
    )


class AiWorkflowsFilterInput(sgqlc.types.Input):
    """Class for AiWorkflowsFilterInput.

    Filter input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "predicates", "type")
    name = sgqlc.types.Field(String, graphql_name="name")


class AiWorkflowsFilters(sgqlc.types.Input):
    """Class for AiWorkflowsFilters.

    Filter on the workflow objects.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "channel_id",
        "destination_type",
        "enrichment_id",
        "filter_id",
        "id",
        "name",
        "name_like",
        "workflow_enabled",
    )
    channel_id = sgqlc.types.Field(ID, graphql_name="channelId")


class AiWorkflowsNrqlConfigurationInput(sgqlc.types.Input):
    """Class for AiWorkflowsNrqlConfigurationInput.

    NRQL type configuration input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("query",)
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="query")


class AiWorkflowsNrqlEnrichmentInput(sgqlc.types.Input):
    """Class for AiWorkflowsNrqlEnrichmentInput.

    NRQL type enrichment input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("configuration", "name")
    configuration = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiWorkflowsNrqlConfigurationInput))
        ),
        graphql_name="configuration",
    )


class AiWorkflowsNrqlTestEnrichmentInput(sgqlc.types.Input):
    """Class for AiWorkflowsNrqlTestEnrichmentInput.

    NRQL type test enrichment input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("configuration", "id", "name")
    configuration = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiWorkflowsNrqlConfigurationInput))
        ),
        graphql_name="configuration",
    )


class AiWorkflowsNrqlUpdateEnrichmentInput(sgqlc.types.Input):
    """Class for AiWorkflowsNrqlUpdateEnrichmentInput.

    NRQL type update enrichment input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("configuration", "id", "name")
    configuration = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiWorkflowsNrqlConfigurationInput))
        ),
        graphql_name="configuration",
    )


class AiWorkflowsPredicateInput(sgqlc.types.Input):
    """Class for AiWorkflowsPredicateInput.

    PredicateInput input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "operator", "values")
    attribute = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attribute"
    )


class AiWorkflowsTestEnrichmentsInput(sgqlc.types.Input):
    """Class for AiWorkflowsTestEnrichmentsInput.

    Test Enrichment input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql",)
    nrql = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(AiWorkflowsNrqlTestEnrichmentInput)
            )
        ),
        graphql_name="nrql",
    )


class AiWorkflowsTestWorkflowInput(sgqlc.types.Input):
    """Class for AiWorkflowsTestWorkflowInput.

    Test Workflow input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("destination_configurations", "enrichments", "issues_filter")
    destination_configurations = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(AiWorkflowsDestinationConfigurationInput)
            )
        ),
        graphql_name="destinationConfigurations",
    )


class AiWorkflowsUpdateEnrichmentsInput(sgqlc.types.Input):
    """Class for AiWorkflowsUpdateEnrichmentsInput.

    Update Enrichment input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql",)
    nrql = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(AiWorkflowsNrqlUpdateEnrichmentInput)
            )
        ),
        graphql_name="nrql",
    )


class AiWorkflowsUpdateWorkflowInput(sgqlc.types.Input):
    """Class for AiWorkflowsUpdateWorkflowInput.

    Update Workflow input object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "destination_configurations",
        "destinations_enabled",
        "enrichments",
        "enrichments_enabled",
        "id",
        "issues_filter",
        "muting_rules_handling",
        "name",
        "workflow_enabled",
    )
    destination_configurations = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AiWorkflowsDestinationConfigurationInput)
        ),
        graphql_name="destinationConfigurations",
    )


class AiWorkflowsUpdatedFilterInput(sgqlc.types.Input):
    """Class for AiWorkflowsUpdatedFilterInput.

    Update Filter input object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("filter_input", "id")
    filter_input = sgqlc.types.Field(
        sgqlc.types.non_null(AiWorkflowsFilterInput), graphql_name="filterInput"
    )


class AlertsEmailNotificationChannelCreateInput(sgqlc.types.Input):
    """Class for AlertsEmailNotificationChannelCreateInput.

    The input for creating a new Email notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("emails", "include_json", "name")
    emails = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="emails",
    )


class AlertsEmailNotificationChannelUpdateInput(sgqlc.types.Input):
    """Class for AlertsEmailNotificationChannelUpdateInput.

    The input for updating an existing Email notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("emails", "include_json", "name")
    emails = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="emails"
    )


class AlertsMutingRuleConditionGroupInput(sgqlc.types.Input):
    """Class for AlertsMutingRuleConditionGroupInput.

    A group of MutingRuleConditions combined by an operator.
    """

    __schema__ = nerdgraph
    __field_names__ = ("conditions", "operator")
    conditions = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AlertsMutingRuleConditionInput"))
        ),
        graphql_name="conditions",
    )


class AlertsMutingRuleConditionInput(sgqlc.types.Input):
    """Class for AlertsMutingRuleConditionInput.

    A condition which describes how to target a New Relic Alerts
    Violation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "operator", "values")
    attribute = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attribute"
    )


class AlertsMutingRuleInput(sgqlc.types.Input):
    """Class for AlertsMutingRuleInput.

    Input for creating MutingRules for New Relic Alerts Violations.
    """

    __schema__ = nerdgraph
    __field_names__ = ("condition", "description", "enabled", "name", "schedule")
    condition = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsMutingRuleConditionGroupInput),
        graphql_name="condition",
    )


class AlertsMutingRuleScheduleInput(sgqlc.types.Input):
    """Class for AlertsMutingRuleScheduleInput.

    The time window when the MutingRule should actively mute
    violations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "end_repeat",
        "end_time",
        "repeat",
        "repeat_count",
        "start_time",
        "time_zone",
        "weekly_repeat_days",
    )
    end_repeat = sgqlc.types.Field(NaiveDateTime, graphql_name="endRepeat")


class AlertsMutingRuleScheduleUpdateInput(sgqlc.types.Input):
    """Class for AlertsMutingRuleScheduleUpdateInput.

    The time window when the MutingRule should actively mute
    violations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "end_repeat",
        "end_time",
        "repeat",
        "repeat_count",
        "start_time",
        "time_zone",
        "weekly_repeat_days",
    )
    end_repeat = sgqlc.types.Field(NaiveDateTime, graphql_name="endRepeat")


class AlertsMutingRuleUpdateInput(sgqlc.types.Input):
    """Class for AlertsMutingRuleUpdateInput.

    Input for updating MutingRules for New Relic Alerts Violations.
    """

    __schema__ = nerdgraph
    __field_names__ = ("condition", "description", "enabled", "name", "schedule")
    condition = sgqlc.types.Field(
        AlertsMutingRuleConditionGroupInput, graphql_name="condition"
    )


class AlertsNotificationChannelCreateConfiguration(sgqlc.types.Input):
    """Class for AlertsNotificationChannelCreateConfiguration.

    The input configuration for creating a notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "email",
        "ops_genie",
        "pager_duty",
        "slack",
        "victor_ops",
        "webhook",
        "x_matters",
    )
    email = sgqlc.types.Field(
        AlertsEmailNotificationChannelCreateInput, graphql_name="email"
    )


class AlertsNotificationChannelUpdateConfiguration(sgqlc.types.Input):
    """Class for AlertsNotificationChannelUpdateConfiguration.

    The input configuration for updating a notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "email",
        "ops_genie",
        "pager_duty",
        "slack",
        "victor_ops",
        "webhook",
        "x_matters",
    )
    email = sgqlc.types.Field(
        AlertsEmailNotificationChannelUpdateInput, graphql_name="email"
    )


class AlertsNrqlConditionBaselineInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionBaselineInput.

    Input for creating a baseline NRQL condition.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "baseline_direction",
        "description",
        "enabled",
        "expiration",
        "name",
        "nrql",
        "runbook_url",
        "signal",
        "terms",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    baseline_direction = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlBaselineDirection),
        graphql_name="baselineDirection",
    )


class AlertsNrqlConditionExpirationInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionExpirationInput.

    Also known as **loss of signal**, these are settings for how
    violations are opened or closed when a signal expires.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "close_violations_on_expiration",
        "expiration_duration",
        "open_violation_on_expiration",
    )
    close_violations_on_expiration = sgqlc.types.Field(
        Boolean, graphql_name="closeViolationsOnExpiration"
    )


class AlertsNrqlConditionOutlierInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionOutlierInput.

    Input for creating an outlier NRQL condition.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "enabled",
        "expected_groups",
        "expiration",
        "name",
        "nrql",
        "open_violation_on_group_overlap",
        "runbook_url",
        "signal",
        "terms",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class AlertsNrqlConditionQueryInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionQueryInput.

    Information for generating the condition NRQL query. The output of
    data from this NRQL query will be compared to the condition terms
    to detect violations.
    """

    __schema__ = nerdgraph
    __field_names__ = ("evaluation_offset", "query")
    evaluation_offset = sgqlc.types.Field(Int, graphql_name="evaluationOffset")


class AlertsNrqlConditionSignalInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionSignalInput.

    Configuration that defines the signal that the NRQL condition will
    use to evaluate.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aggregation_delay",
        "aggregation_method",
        "aggregation_timer",
        "aggregation_window",
        "evaluation_delay",
        "evaluation_offset",
        "fill_option",
        "fill_value",
        "slide_by",
    )
    aggregation_delay = sgqlc.types.Field(Seconds, graphql_name="aggregationDelay")


class AlertsNrqlConditionStaticInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionStaticInput.

    Input for creating a static NRQL condition.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "enabled",
        "expiration",
        "name",
        "nrql",
        "runbook_url",
        "signal",
        "terms",
        "value_function",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class AlertsNrqlConditionTermsInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionTermsInput.

    NRQL condition terms determine when a violation will be opened.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "operator",
        "priority",
        "threshold",
        "threshold_duration",
        "threshold_occurrences",
    )
    operator = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlConditionTermsOperator), graphql_name="operator"
    )


class AlertsNrqlConditionUpdateBaselineInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionUpdateBaselineInput.

    Input for updating a baseline NRQL condition.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "baseline_direction",
        "description",
        "enabled",
        "expiration",
        "name",
        "nrql",
        "runbook_url",
        "signal",
        "terms",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    baseline_direction = sgqlc.types.Field(
        AlertsNrqlBaselineDirection, graphql_name="baselineDirection"
    )


class AlertsNrqlConditionUpdateOutlierInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionUpdateOutlierInput.

    Input for updating an outlier NRQL condition.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "enabled",
        "expected_groups",
        "expiration",
        "name",
        "nrql",
        "open_violation_on_group_overlap",
        "runbook_url",
        "signal",
        "terms",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class AlertsNrqlConditionUpdateQueryInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionUpdateQueryInput.

    Information for generating the condition NRQL query. Output from
    this NRQL query will be compared to the condition terms to detect
    violations.
    """

    __schema__ = nerdgraph
    __field_names__ = ("evaluation_offset", "query")
    evaluation_offset = sgqlc.types.Field(Int, graphql_name="evaluationOffset")


class AlertsNrqlConditionUpdateStaticInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionUpdateStaticInput.

    Input for updating a static NRQL condition.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "enabled",
        "expiration",
        "name",
        "nrql",
        "runbook_url",
        "signal",
        "terms",
        "value_function",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class AlertsNrqlConditionsSearchCriteriaInput(sgqlc.types.Input):
    """Class for AlertsNrqlConditionsSearchCriteriaInput.

    Search criteria for returning specific NRQL conditions.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "name",
        "name_like",
        "policy_id",
        "query",
        "query_like",
        "terms_operator",
    )
    name = sgqlc.types.Field(String, graphql_name="name")


class AlertsNrqlDynamicConditionTermsInput(sgqlc.types.Input):
    """Class for AlertsNrqlDynamicConditionTermsInput.

    NRQL condition terms determine when a violation will be opened.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "operator",
        "priority",
        "threshold",
        "threshold_duration",
        "threshold_occurrences",
    )
    operator = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlDynamicConditionTermsOperator),
        graphql_name="operator",
    )


class AlertsOpsGenieNotificationChannelCreateInput(sgqlc.types.Input):
    """Class for AlertsOpsGenieNotificationChannelCreateInput.

    The input for creating a new OpsGenie notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "api_key",
        "data_center_region",
        "name",
        "recipients",
        "tags",
        "teams",
    )
    api_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiKey"
    )


class AlertsOpsGenieNotificationChannelUpdateInput(sgqlc.types.Input):
    """Class for AlertsOpsGenieNotificationChannelUpdateInput.

    The input for updating an existing OpsGenie notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "api_key",
        "data_center_region",
        "name",
        "recipients",
        "tags",
        "teams",
    )
    api_key = sgqlc.types.Field(SecureValue, graphql_name="apiKey")


class AlertsPagerDutyNotificationChannelCreateInput(sgqlc.types.Input):
    """Class for AlertsPagerDutyNotificationChannelCreateInput.

    The input for creating a new PagerDuty notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("api_key", "name")
    api_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiKey"
    )


class AlertsPagerDutyNotificationChannelUpdateInput(sgqlc.types.Input):
    """Class for AlertsPagerDutyNotificationChannelUpdateInput.

    The input for updating an existing PagerDuty notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("api_key", "name")
    api_key = sgqlc.types.Field(SecureValue, graphql_name="apiKey")


class AlertsPoliciesSearchCriteriaInput(sgqlc.types.Input):
    """Class for AlertsPoliciesSearchCriteriaInput.

    Search criteria for returning specific policies.
    """

    __schema__ = nerdgraph
    __field_names__ = ("ids", "name", "name_like")
    ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="ids"
    )


class AlertsPolicyInput(sgqlc.types.Input):
    """Class for AlertsPolicyInput.

    Container for conditions with associated notifications channels.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident_preference", "name")
    incident_preference = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsIncidentPreference),
        graphql_name="incidentPreference",
    )


class AlertsPolicyUpdateInput(sgqlc.types.Input):
    """Class for AlertsPolicyUpdateInput.

    Policy fields to be updated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incident_preference", "name")
    incident_preference = sgqlc.types.Field(
        AlertsIncidentPreference, graphql_name="incidentPreference"
    )


class AlertsSlackNotificationChannelCreateInput(sgqlc.types.Input):
    """Class for AlertsSlackNotificationChannelCreateInput.

    The input for creating a new Slack notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "team_channel", "url")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AlertsSlackNotificationChannelUpdateInput(sgqlc.types.Input):
    """Class for AlertsSlackNotificationChannelUpdateInput.

    The input for updating an existing Slack notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "team_channel", "url")
    name = sgqlc.types.Field(String, graphql_name="name")


class AlertsVictorOpsNotificationChannelCreateInput(sgqlc.types.Input):
    """Class for AlertsVictorOpsNotificationChannelCreateInput.

    The input for creating a new VictorOps notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "name", "route_key")
    key = sgqlc.types.Field(sgqlc.types.non_null(SecureValue), graphql_name="key")


class AlertsVictorOpsNotificationChannelUpdateInput(sgqlc.types.Input):
    """Class for AlertsVictorOpsNotificationChannelUpdateInput.

    The input for updating an existing VictorOps notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "name", "route_key")
    key = sgqlc.types.Field(SecureValue, graphql_name="key")


class AlertsWebhookBasicAuthMutationInput(sgqlc.types.Input):
    """Class for AlertsWebhookBasicAuthMutationInput.

    Webhook basic auth.
    """

    __schema__ = nerdgraph
    __field_names__ = ("password", "username")
    password = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="password"
    )


class AlertsWebhookCustomHeaderMutationInput(sgqlc.types.Input):
    """Class for AlertsWebhookCustomHeaderMutationInput.

    Webhook header.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "value")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AlertsWebhookNotificationChannelCreateInput(sgqlc.types.Input):
    """Class for AlertsWebhookNotificationChannelCreateInput.

    The input for creating a new Webhook notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "base_url",
        "basic_auth",
        "custom_http_headers",
        "custom_payload_body",
        "custom_payload_type",
        "name",
    )
    base_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="baseUrl")


class AlertsWebhookNotificationChannelUpdateInput(sgqlc.types.Input):
    """Class for AlertsWebhookNotificationChannelUpdateInput.

    The input for updating an existing Webhook notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "base_url",
        "basic_auth",
        "custom_http_headers",
        "custom_payload_body",
        "custom_payload_type",
        "name",
    )
    base_url = sgqlc.types.Field(String, graphql_name="baseUrl")


class AlertsXMattersNotificationChannelCreateInput(sgqlc.types.Input):
    """Class for AlertsXMattersNotificationChannelCreateInput.

    The input for creating a new xMatters notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("integration_url", "name")
    integration_url = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="integrationUrl"
    )


class AlertsXMattersNotificationChannelUpdateInput(sgqlc.types.Input):
    """Class for AlertsXMattersNotificationChannelUpdateInput.

    The input for updating an existing xMatters notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("integration_url", "name")
    integration_url = sgqlc.types.Field(SecureValue, graphql_name="integrationUrl")


class ApiAccessCreateIngestKeyInput(sgqlc.types.Input):
    """Class for ApiAccessCreateIngestKeyInput.

    The input for any ingest keys you want to create. Each ingest key
    must have a type that communicates what kind of data it is for.
    You can optionally add a name or notes to your key, which can be
    updated later.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "ingest_type", "name", "notes")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class ApiAccessCreateInput(sgqlc.types.Input):
    """Class for ApiAccessCreateInput.

    The input object to create one or more keys.
    """

    __schema__ = nerdgraph
    __field_names__ = ("ingest", "user")
    ingest = sgqlc.types.Field(
        sgqlc.types.list_of(ApiAccessCreateIngestKeyInput), graphql_name="ingest"
    )


class ApiAccessCreateUserKeyInput(sgqlc.types.Input):
    """Class for ApiAccessCreateUserKeyInput.

    The input for any ingest keys you want to create. Each ingest key
    must have a type that communicates what kind of data it is for.
    You can optionally add a name or notes to your key, which can be
    updated later.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "name", "notes", "user_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class ApiAccessDeleteInput(sgqlc.types.Input):
    """Class for ApiAccessDeleteInput.

    The input to delete keys.
    """

    __schema__ = nerdgraph
    __field_names__ = ("ingest_key_ids", "user_key_ids")
    ingest_key_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="ingestKeyIds"
    )


class ApiAccessKeySearchQuery(sgqlc.types.Input):
    """Class for ApiAccessKeySearchQuery.

    Parameters by which to filter the search.
    """

    __schema__ = nerdgraph
    __field_names__ = ("scope", "types")
    scope = sgqlc.types.Field("ApiAccessKeySearchScope", graphql_name="scope")


class ApiAccessKeySearchScope(sgqlc.types.Input):
    """Class for ApiAccessKeySearchScope.

    The scope of keys to be returned. Note that some filters only
    apply to certain key types.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "ingest_types", "user_ids")
    account_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="accountIds")


class ApiAccessUpdateIngestKeyInput(sgqlc.types.Input):
    """Class for ApiAccessUpdateIngestKeyInput.

    The `id` and data to update one or more keys.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key_id", "name", "notes")
    key_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="keyId")


class ApiAccessUpdateInput(sgqlc.types.Input):
    """Class for ApiAccessUpdateInput.

    The `id` and data to update one or more keys.
    """

    __schema__ = nerdgraph
    __field_names__ = ("ingest", "user")
    ingest = sgqlc.types.Field(
        sgqlc.types.list_of(ApiAccessUpdateIngestKeyInput), graphql_name="ingest"
    )


class ApiAccessUpdateUserKeyInput(sgqlc.types.Input):
    """Class for ApiAccessUpdateUserKeyInput.

    The `id` and data to update one or more keys.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key_id", "name", "notes")
    key_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="keyId")


class ApmApplicationEntitySettings(sgqlc.types.Input):
    """Class for ApmApplicationEntitySettings.

    The ApmApplicationEntity's settings to update.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apdex_target",)
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class AuthorizationManagementAccountAccessGrant(sgqlc.types.Input):
    """Class for AuthorizationManagementAccountAccessGrant.

    The Account and Role a Group should have access to.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "role_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AuthorizationManagementGrantAccess(sgqlc.types.Input):
    """Class for AuthorizationManagementGrantAccess.

    The input object representing the access to grant for the group.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_access_grants",
        "group_id",
        "organization_access_grants",
    )
    account_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AuthorizationManagementAccountAccessGrant)
        ),
        graphql_name="accountAccessGrants",
    )


class AuthorizationManagementOrganizationAccessGrant(sgqlc.types.Input):
    """Class for AuthorizationManagementOrganizationAccessGrant.

    The Organization Role a Group should have access to.
    """

    __schema__ = nerdgraph
    __field_names__ = ("role_id",)
    role_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="roleId")


class AuthorizationManagementRevokeAccess(sgqlc.types.Input):
    """Class for AuthorizationManagementRevokeAccess.

    The input object representing the access to revoke for the group.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_access_grants",
        "group_id",
        "organization_access_grants",
    )
    account_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AuthorizationManagementAccountAccessGrant)
        ),
        graphql_name="accountAccessGrants",
    )


class ChangeTrackingDeploymentInput(sgqlc.types.Input):
    """Class for ChangeTrackingDeploymentInput.

    A deployment.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "changelog",
        "commit",
        "deep_link",
        "deployment_type",
        "description",
        "entity_guid",
        "group_id",
        "timestamp",
        "user",
        "version",
    )
    changelog = sgqlc.types.Field(String, graphql_name="changelog")


class ChangeTrackingSearchFilter(sgqlc.types.Input):
    """Class for ChangeTrackingSearchFilter.

    The object contains the filters to be applied to the search.
    """

    __schema__ = nerdgraph
    __field_names__ = ("limit", "query", "time_window")
    limit = sgqlc.types.Field(Int, graphql_name="limit")


class ChangeTrackingTimeWindowInputWithDefaults(sgqlc.types.Input):
    """Class for ChangeTrackingTimeWindowInputWithDefaults.

    Represents a time window input with default values.
    """

    __schema__ = nerdgraph
    __field_names__ = ("end_time", "start_time")
    end_time = sgqlc.types.Field(EpochMilliseconds, graphql_name="endTime")


class CloudAlbIntegrationInput(sgqlc.types.Input):
    """Class for CloudAlbIntegrationInput.

    Elastic Load Balancing - Application Load Balancer (ALB).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "load_balancer_prefixes",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudApigatewayIntegrationInput(sgqlc.types.Input):
    """Class for CloudApigatewayIntegrationInput.

    Amazon API Gateway.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "stage_prefixes",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAutoscalingIntegrationInput(sgqlc.types.Input):
    """Class for CloudAutoscalingIntegrationInput.

    AWS Auto Scaling.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsAppsyncIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsAppsyncIntegrationInput.

    AppSync.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsAthenaIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsAthenaIntegrationInput.

    Athena.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsCognitoIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsCognitoIntegrationInput.

    Cognito.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsConnectIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsConnectIntegrationInput.

    Connect.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsDirectconnectIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsDirectconnectIntegrationInput.

    Direct Connect.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsDisableIntegrationsInput(sgqlc.types.Input):
    """Class for CloudAwsDisableIntegrationsInput.

    List of integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "alb",
        "apigateway",
        "autoscaling",
        "aws_appsync",
        "aws_athena",
        "aws_cognito",
        "aws_connect",
        "aws_directconnect",
        "aws_docdb",
        "aws_fsx",
        "aws_glue",
        "aws_kinesisanalytics",
        "aws_mediaconvert",
        "aws_mediapackagevod",
        "aws_metadata",
        "aws_mq",
        "aws_msk",
        "aws_neptune",
        "aws_qldb",
        "aws_route53resolver",
        "aws_states",
        "aws_tags_global",
        "aws_transitgateway",
        "aws_waf",
        "aws_wafv2",
        "aws_xray",
        "billing",
        "cloudfront",
        "cloudtrail",
        "dynamodb",
        "ebs",
        "ec2",
        "ecs",
        "efs",
        "elasticache",
        "elasticbeanstalk",
        "elasticsearch",
        "elb",
        "emr",
        "health",
        "iam",
        "iot",
        "kinesis",
        "kinesis_firehose",
        "lambda_",
        "rds",
        "redshift",
        "route53",
        "s3",
        "ses",
        "sns",
        "sqs",
        "trustedadvisor",
        "vpc",
    )
    alb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="alb"
    )


class CloudAwsDocdbIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsDocdbIntegrationInput.

    DocumentDB.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsFsxIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsFsxIntegrationInput.

    FSx.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsGlueIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsGlueIntegrationInput.

    Glue.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsGovCloudLinkAccountInput(sgqlc.types.Input):
    """Class for CloudAwsGovCloudLinkAccountInput.

    Information required to link an AWS GovCloud account to a NewRelic
    account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "access_key_id",
        "aws_account_id",
        "metric_collection_mode",
        "name",
        "secret_access_key",
    )
    access_key_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="accessKeyId"
    )


class CloudAwsGovCloudMigrateToAssumeroleInput(sgqlc.types.Input):
    """Class for CloudAwsGovCloudMigrateToAssumeroleInput.

    Information required to migrate an existing AWS GovCloud account
    to use AssumeRole Authentication.
    """

    __schema__ = nerdgraph
    __field_names__ = ("arn", "linked_account_id")
    arn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="arn")


class CloudAwsGovcloudDisableIntegrationsInput(sgqlc.types.Input):
    """Class for CloudAwsGovcloudDisableIntegrationsInput.

    List of integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "alb",
        "apigateway",
        "autoscaling",
        "aws_directconnect",
        "aws_states",
        "cloudtrail",
        "dynamodb",
        "ebs",
        "ec2",
        "elasticsearch",
        "elb",
        "emr",
        "iam",
        "lambda_",
        "rds",
        "redshift",
        "route53",
        "s3",
        "sns",
        "sqs",
    )
    alb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="alb"
    )


class CloudAwsGovcloudIntegrationsInput(sgqlc.types.Input):
    """Class for CloudAwsGovcloudIntegrationsInput.

    List of integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "alb",
        "apigateway",
        "autoscaling",
        "aws_directconnect",
        "aws_states",
        "cloudtrail",
        "dynamodb",
        "ebs",
        "ec2",
        "elasticsearch",
        "elb",
        "emr",
        "iam",
        "lambda_",
        "rds",
        "redshift",
        "route53",
        "s3",
        "sns",
        "sqs",
    )
    alb = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAlbIntegrationInput), graphql_name="alb"
    )


class CloudAwsIntegrationsInput(sgqlc.types.Input):
    """Class for CloudAwsIntegrationsInput.

    List of integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "alb",
        "apigateway",
        "autoscaling",
        "aws_appsync",
        "aws_athena",
        "aws_cognito",
        "aws_connect",
        "aws_directconnect",
        "aws_docdb",
        "aws_fsx",
        "aws_glue",
        "aws_kinesisanalytics",
        "aws_mediaconvert",
        "aws_mediapackagevod",
        "aws_metadata",
        "aws_mq",
        "aws_msk",
        "aws_neptune",
        "aws_qldb",
        "aws_route53resolver",
        "aws_states",
        "aws_tags_global",
        "aws_transitgateway",
        "aws_waf",
        "aws_wafv2",
        "aws_xray",
        "billing",
        "cloudfront",
        "cloudtrail",
        "dynamodb",
        "ebs",
        "ec2",
        "ecs",
        "efs",
        "elasticache",
        "elasticbeanstalk",
        "elasticsearch",
        "elb",
        "emr",
        "health",
        "iam",
        "iot",
        "kinesis",
        "kinesis_firehose",
        "lambda_",
        "rds",
        "redshift",
        "route53",
        "s3",
        "ses",
        "sns",
        "sqs",
        "trustedadvisor",
        "vpc",
    )
    alb = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAlbIntegrationInput), graphql_name="alb"
    )


class CloudAwsKinesisanalyticsIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsKinesisanalyticsIntegrationInput.

    Kinesis Data Analytics.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsLinkAccountInput(sgqlc.types.Input):
    """Class for CloudAwsLinkAccountInput.

    Information required to link a AWS account to a NewRelic account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("arn", "metric_collection_mode", "name")
    arn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="arn")


class CloudAwsMediaconvertIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsMediaconvertIntegrationInput.

    Elemental MediaConvert.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsMediapackagevodIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsMediapackagevodIntegrationInput.

    MediaPackage VOD.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsMetadataIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsMetadataIntegrationInput.

    Fetch Metadata for AWS integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAwsMqIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsMqIntegrationInput.

    MQ.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsMskIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsMskIntegrationInput.

    Managed Kafka.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsNeptuneIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsNeptuneIntegrationInput.

    Neptune.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsQldbIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsQldbIntegrationInput.

    QLDB.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsRoute53resolverIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsRoute53resolverIntegrationInput.

    Route53 Resolver.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsStatesIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsStatesIntegrationInput.

    Step Functions.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsTagsGlobalIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsTagsGlobalIntegrationInput.

    Fetch tags for all integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAwsTransitgatewayIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsTransitgatewayIntegrationInput.

    Transit Gateway.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsWafIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsWafIntegrationInput.

    WAF.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsWafv2IntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsWafv2IntegrationInput.

    WAFV2.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsXrayIntegrationInput(sgqlc.types.Input):
    """Class for CloudAwsXrayIntegrationInput.

    X-Ray.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAzureApimanagementIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureApimanagementIntegrationInput.

    Api Management.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureAppgatewayIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureAppgatewayIntegrationInput.

    App Gateway.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureAppserviceIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureAppserviceIntegrationInput.

    Azure App Service.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureContainersIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureContainersIntegrationInput.

    Containers.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureCosmosdbIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureCosmosdbIntegrationInput.

    Azure Cosmos DB.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureCostmanagementIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureCostmanagementIntegrationInput.

    Cost Management.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_keys",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureDatafactoryIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureDatafactoryIntegrationInput.

    Data Factory.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureDisableIntegrationsInput(sgqlc.types.Input):
    """Class for CloudAzureDisableIntegrationsInput.

    List of integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "azure_apimanagement",
        "azure_appgateway",
        "azure_appservice",
        "azure_containers",
        "azure_cosmosdb",
        "azure_costmanagement",
        "azure_datafactory",
        "azure_eventhub",
        "azure_expressroute",
        "azure_firewalls",
        "azure_frontdoor",
        "azure_functions",
        "azure_keyvault",
        "azure_loadbalancer",
        "azure_logicapps",
        "azure_machinelearning",
        "azure_mariadb",
        "azure_monitor",
        "azure_mysql",
        "azure_mysqlflexible",
        "azure_postgresql",
        "azure_postgresqlflexible",
        "azure_powerbidedicated",
        "azure_rediscache",
        "azure_servicebus",
        "azure_sql",
        "azure_sqlmanaged",
        "azure_storage",
        "azure_virtualmachine",
        "azure_virtualnetworks",
        "azure_vms",
        "azure_vpngateways",
    )
    azure_apimanagement = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureApimanagement",
    )


class CloudAzureEventhubIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureEventhubIntegrationInput.

    Event Hub.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureExpressrouteIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureExpressrouteIntegrationInput.

    Express Route.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureFirewallsIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureFirewallsIntegrationInput.

    Firewalls.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureFrontdoorIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureFrontdoorIntegrationInput.

    Front Door.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureFunctionsIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureFunctionsIntegrationInput.

    Azure Functions.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureIntegrationsInput(sgqlc.types.Input):
    """Class for CloudAzureIntegrationsInput.

    List of integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "azure_apimanagement",
        "azure_appgateway",
        "azure_appservice",
        "azure_containers",
        "azure_cosmosdb",
        "azure_costmanagement",
        "azure_datafactory",
        "azure_eventhub",
        "azure_expressroute",
        "azure_firewalls",
        "azure_frontdoor",
        "azure_functions",
        "azure_keyvault",
        "azure_loadbalancer",
        "azure_logicapps",
        "azure_machinelearning",
        "azure_mariadb",
        "azure_monitor",
        "azure_mysql",
        "azure_mysqlflexible",
        "azure_postgresql",
        "azure_postgresqlflexible",
        "azure_powerbidedicated",
        "azure_rediscache",
        "azure_servicebus",
        "azure_sql",
        "azure_sqlmanaged",
        "azure_storage",
        "azure_virtualmachine",
        "azure_virtualnetworks",
        "azure_vms",
        "azure_vpngateways",
    )
    azure_apimanagement = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureApimanagementIntegrationInput),
        graphql_name="azureApimanagement",
    )


class CloudAzureKeyvaultIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureKeyvaultIntegrationInput.

    Key Vault.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureLinkAccountInput(sgqlc.types.Input):
    """Class for CloudAzureLinkAccountInput.

    Information required to link a Azure account to a NewRelic
    account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "application_id",
        "client_secret",
        "name",
        "subscription_id",
        "tenant_id",
    )
    application_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="applicationId"
    )


class CloudAzureLoadbalancerIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureLoadbalancerIntegrationInput.

    Azure Load Balancer.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureLogicappsIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureLogicappsIntegrationInput.

    Logic Apps.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureMachinelearningIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureMachinelearningIntegrationInput.

    Machine Learning.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureMariadbIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureMariadbIntegrationInput.

    Database for MariaDB.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureMonitorIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureMonitorIntegrationInput.

    Azure Monitor metrics.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "enabled",
        "exclude_tags",
        "include_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
        "resource_types",
    )
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class CloudAzureMysqlIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureMysqlIntegrationInput.

    Database for MySQL.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureMysqlflexibleIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureMysqlflexibleIntegrationInput.

    MySQL Flexible Server.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzurePostgresqlIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzurePostgresqlIntegrationInput.

    Database for PostgreSQL.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzurePostgresqlflexibleIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzurePostgresqlflexibleIntegrationInput.

    PostgreSQL Flexible Server.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzurePowerbidedicatedIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzurePowerbidedicatedIntegrationInput.

    Power BI Dedicated.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureRediscacheIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureRediscacheIntegrationInput.

    Azure Redis Cache.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureServicebusIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureServicebusIntegrationInput.

    Azure Service Bus.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureSqlIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureSqlIntegrationInput.

    Azure SQL Database.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureSqlmanagedIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureSqlmanagedIntegrationInput.

    SQL Managed Instances.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureStorageIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureStorageIntegrationInput.

    Azure Storage.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureVirtualmachineIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureVirtualmachineIntegrationInput.

    Virtual machine scale sets.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureVirtualnetworksIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureVirtualnetworksIntegrationInput.

    Azure Virtual Network.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureVmsIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureVmsIntegrationInput.

    Azure Virtual Machines.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudAzureVpngatewaysIntegrationInput(sgqlc.types.Input):
    """Class for CloudAzureVpngatewaysIntegrationInput.

    VPN Gateways.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "resource_groups",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudBillingIntegrationInput(sgqlc.types.Input):
    """Class for CloudBillingIntegrationInput.

    AWS Billing.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudCloudfrontIntegrationInput(sgqlc.types.Input):
    """Class for CloudCloudfrontIntegrationInput.

    Amazon CloudFront.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_lambdas_at_edge",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    fetch_lambdas_at_edge = sgqlc.types.Field(
        Boolean, graphql_name="fetchLambdasAtEdge"
    )


class CloudCloudtrailIntegrationInput(sgqlc.types.Input):
    """Class for CloudCloudtrailIntegrationInput.

    AWS CloudTrail.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudDisableAccountIntegrationInput(sgqlc.types.Input):
    """Class for CloudDisableAccountIntegrationInput.

    Information required to disable a cloud service integration from a
    linked account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("linked_account_id",)
    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )


class CloudDisableIntegrationsInput(sgqlc.types.Input):
    """Class for CloudDisableIntegrationsInput.

    List of providers.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws", "aws_govcloud", "azure", "gcp")
    aws = sgqlc.types.Field(CloudAwsDisableIntegrationsInput, graphql_name="aws")


class CloudDynamodbIntegrationInput(sgqlc.types.Input):
    """Class for CloudDynamodbIntegrationInput.

    Amazon DynamoDB.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEbsIntegrationInput(sgqlc.types.Input):
    """Class for CloudEbsIntegrationInput.

    Amazon Elastic Block Store (EBS).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEc2IntegrationInput(sgqlc.types.Input):
    """Class for CloudEc2IntegrationInput.

    Amazon Elastic Compute Cloud (EC2).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "duplicate_ec2_tags",
        "fetch_ip_addresses",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEcsIntegrationInput(sgqlc.types.Input):
    """Class for CloudEcsIntegrationInput.

    Amazon Elastic Container Service (ECS).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEfsIntegrationInput(sgqlc.types.Input):
    """Class for CloudEfsIntegrationInput.

    Amazon Elastic File System (EFS).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudElasticacheIntegrationInput(sgqlc.types.Input):
    """Class for CloudElasticacheIntegrationInput.

    Amazon ElastiCache.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudElasticbeanstalkIntegrationInput(sgqlc.types.Input):
    """Class for CloudElasticbeanstalkIntegrationInput.

    AWS Elastic Beanstalk.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudElasticsearchIntegrationInput(sgqlc.types.Input):
    """Class for CloudElasticsearchIntegrationInput.

    Amazon Elasticsearch Service.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_nodes",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudElbIntegrationInput(sgqlc.types.Input):
    """Class for CloudElbIntegrationInput.

    Elastic Load Balancing - Classic Load Balancer (ELB).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEmrIntegrationInput(sgqlc.types.Input):
    """Class for CloudEmrIntegrationInput.

    Amazon Elastic MapReduce (EMR).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudGcpAlloydbIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpAlloydbIntegrationInput.

    AlloyDB.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpAppengineIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpAppengineIntegrationInput.

    Google App Engine.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpBigqueryIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpBigqueryIntegrationInput.

    BigQuery.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_table_metrics",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    fetch_table_metrics = sgqlc.types.Field(Boolean, graphql_name="fetchTableMetrics")


class CloudGcpBigtableIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpBigtableIntegrationInput.

    Bigtable.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpComposerIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpComposerIntegrationInput.

    Composer.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpDataflowIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpDataflowIntegrationInput.

    Dataflow.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpDataprocIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpDataprocIntegrationInput.

    Dataproc.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpDatastoreIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpDatastoreIntegrationInput.

    Datastore.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpDisableIntegrationsInput(sgqlc.types.Input):
    """Class for CloudGcpDisableIntegrationsInput.

    List of integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "gcp_alloydb",
        "gcp_appengine",
        "gcp_bigquery",
        "gcp_bigtable",
        "gcp_composer",
        "gcp_dataflow",
        "gcp_dataproc",
        "gcp_datastore",
        "gcp_firebasedatabase",
        "gcp_firebasehosting",
        "gcp_firebasestorage",
        "gcp_firestore",
        "gcp_functions",
        "gcp_interconnect",
        "gcp_kubernetes",
        "gcp_loadbalancing",
        "gcp_memcache",
        "gcp_pubsub",
        "gcp_redis",
        "gcp_router",
        "gcp_run",
        "gcp_spanner",
        "gcp_sql",
        "gcp_storage",
        "gcp_vms",
        "gcp_vpcaccess",
    )
    gcp_alloydb = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpAlloydb",
    )


class CloudGcpFirebasedatabaseIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpFirebasedatabaseIntegrationInput.

    Firebase Database.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpFirebasehostingIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpFirebasehostingIntegrationInput.

    Firebase Hosting.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpFirebasestorageIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpFirebasestorageIntegrationInput.

    Firebase Storage.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpFirestoreIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpFirestoreIntegrationInput.

    Firestore.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpFunctionsIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpFunctionsIntegrationInput.

    Google Cloud Functions.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpIntegrationsInput(sgqlc.types.Input):
    """Class for CloudGcpIntegrationsInput.

    List of integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "gcp_alloydb",
        "gcp_appengine",
        "gcp_bigquery",
        "gcp_bigtable",
        "gcp_composer",
        "gcp_dataflow",
        "gcp_dataproc",
        "gcp_datastore",
        "gcp_firebasedatabase",
        "gcp_firebasehosting",
        "gcp_firebasestorage",
        "gcp_firestore",
        "gcp_functions",
        "gcp_interconnect",
        "gcp_kubernetes",
        "gcp_loadbalancing",
        "gcp_memcache",
        "gcp_pubsub",
        "gcp_redis",
        "gcp_router",
        "gcp_run",
        "gcp_spanner",
        "gcp_sql",
        "gcp_storage",
        "gcp_vms",
        "gcp_vpcaccess",
    )
    gcp_alloydb = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpAlloydbIntegrationInput), graphql_name="gcpAlloydb"
    )


class CloudGcpInterconnectIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpInterconnectIntegrationInput.

    Interconnect.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpKubernetesIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpKubernetesIntegrationInput.

    Google Kubernetes Engine.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpLinkAccountInput(sgqlc.types.Input):
    """Class for CloudGcpLinkAccountInput.

    Information required to link a GCP account to a NewRelic account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "project_id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class CloudGcpLoadbalancingIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpLoadbalancingIntegrationInput.

    Google Cloud Load Balancing.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpMemcacheIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpMemcacheIntegrationInput.

    Memcache.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpPubsubIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpPubsubIntegrationInput.

    Cloud Pub/Sub.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")


class CloudGcpRedisIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpRedisIntegrationInput.

    Redis.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpRouterIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpRouterIntegrationInput.

    Router.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpRunIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpRunIntegrationInput.

    Run.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpSpannerIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpSpannerIntegrationInput.

    Cloud Spanner.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")


class CloudGcpSqlIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpSqlIntegrationInput.

    Google Cloud SQL.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpStorageIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpStorageIntegrationInput.

    Google Cloud Storage.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")


class CloudGcpVmsIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpVmsIntegrationInput.

    Google Compute Engine.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudGcpVpcaccessIntegrationInput(sgqlc.types.Input):
    """Class for CloudGcpVpcaccessIntegrationInput.

    VPC Access.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudHealthIntegrationInput(sgqlc.types.Input):
    """Class for CloudHealthIntegrationInput.

    AWS Health.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudIamIntegrationInput(sgqlc.types.Input):
    """Class for CloudIamIntegrationInput.

    AWS Identity and Access Management (IAM).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudIntegrationsInput(sgqlc.types.Input):
    """Class for CloudIntegrationsInput.

    List of providers.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws", "aws_govcloud", "azure", "gcp")
    aws = sgqlc.types.Field(CloudAwsIntegrationsInput, graphql_name="aws")


class CloudIotIntegrationInput(sgqlc.types.Input):
    """Class for CloudIotIntegrationInput.

    AWS IoT.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudKinesisFirehoseIntegrationInput(sgqlc.types.Input):
    """Class for CloudKinesisFirehoseIntegrationInput.

    Amazon Kinesis Data Firehose.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudKinesisIntegrationInput(sgqlc.types.Input):
    """Class for CloudKinesisIntegrationInput.

    Amazon Kinesis Data Streams.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_shards",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudLambdaIntegrationInput(sgqlc.types.Input):
    """Class for CloudLambdaIntegrationInput.

    AWS Lambda.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudLinkCloudAccountsInput(sgqlc.types.Input):
    """Class for CloudLinkCloudAccountsInput.

    Specific Cloud provider information required to link the Cloud
    provider account to a NewRelic account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws", "aws_govcloud", "azure", "gcp")
    aws = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudAwsLinkAccountInput)),
        graphql_name="aws",
    )


class CloudRdsIntegrationInput(sgqlc.types.Input):
    """Class for CloudRdsIntegrationInput.

    Amazon Relation Database Service (RDS).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudRedshiftIntegrationInput(sgqlc.types.Input):
    """Class for CloudRedshiftIntegrationInput.

    Amazon Redshift.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudRenameAccountsInput(sgqlc.types.Input):
    """Class for CloudRenameAccountsInput.

    Information required when operating on a Linked Account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("linked_account_id", "name")
    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )


class CloudRoute53IntegrationInput(sgqlc.types.Input):
    """Class for CloudRoute53IntegrationInput.

    Amazon Route 53.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_extended_inventory",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )


class CloudS3IntegrationInput(sgqlc.types.Input):
    """Class for CloudS3IntegrationInput.

    Amazon Simple Storage Service (S3).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_extended_inventory",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )


class CloudSesIntegrationInput(sgqlc.types.Input):
    """Class for CloudSesIntegrationInput.

    Amazon Simple Email Service (SES).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudSnsIntegrationInput(sgqlc.types.Input):
    """Class for CloudSnsIntegrationInput.

    Amazon Simple Notification Service (SNS).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudSqsIntegrationInput(sgqlc.types.Input):
    """Class for CloudSqsIntegrationInput.

    Amazon Simple Queue Service (SQS).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "queue_prefixes",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudTrustedadvisorIntegrationInput(sgqlc.types.Input):
    """Class for CloudTrustedadvisorIntegrationInput.

    Trusted Advisor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )


class CloudUnlinkAccountsInput(sgqlc.types.Input):
    """Class for CloudUnlinkAccountsInput.

    Information required to unlink (remove) a linked account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("linked_account_id",)
    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )


class CloudVpcIntegrationInput(sgqlc.types.Input):
    """Class for CloudVpcIntegrationInput.

    Amazon Virtual Private Cloud (VPC).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_nat_gateway",
        "fetch_vpn",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class DashboardAreaWidgetConfigurationInput(sgqlc.types.Input):
    """Class for DashboardAreaWidgetConfigurationInput.

    Configuration for visualization type 'viz.area'.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardBarWidgetConfigurationInput(sgqlc.types.Input):
    """Class for DashboardBarWidgetConfigurationInput.

    Configuration for visualization type 'viz.bar'. Learn more about [
    bar](https://docs.newrelic.com/docs/apis/nerdgraph/examples/create
    -widgets-dashboards-api/#bar) widget.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardBillboardWidgetConfigurationInput(sgqlc.types.Input):
    """Class for DashboardBillboardWidgetConfigurationInput.

    Configuration for visualization type 'viz.billboard'. Learn more
    about [billboard](https://docs.newrelic.com/docs/apis/nerdgraph/ex
    amples/create-widgets-dashboards-api/#billboard) widget.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries", "thresholds")
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardBillboardWidgetThresholdInput(sgqlc.types.Input):
    """Class for DashboardBillboardWidgetThresholdInput.

    Billboard widget threshold input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("alert_severity", "value")
    alert_severity = sgqlc.types.Field(
        DashboardAlertSeverity, graphql_name="alertSeverity"
    )


class DashboardInput(sgqlc.types.Input):
    """Class for DashboardInput.

    Dashboard input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "pages", "permissions", "variables")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardLineWidgetConfigurationInput(sgqlc.types.Input):
    """Class for DashboardLineWidgetConfigurationInput.

    Configuration for visualization type 'viz.line'. Learn more about
    [line](https://docs.newrelic.com/docs/apis/nerdgraph/examples/crea
    te-widgets-dashboards-api/#line) widget.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardLiveUrlsFilterInput(sgqlc.types.Input):
    """Class for DashboardLiveUrlsFilterInput.

    Live URLs input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type", "uuid")
    type = sgqlc.types.Field(DashboardLiveUrlType, graphql_name="type")


class DashboardMarkdownWidgetConfigurationInput(sgqlc.types.Input):
    """Class for DashboardMarkdownWidgetConfigurationInput.

    Configuration for visualization type 'viz.markdown'. Learn more
    about [markdown](https://docs.newrelic.com/docs/apis/nerdgraph/exa
    mples/create-widgets-dashboards-api/#markdown) widget.
    """

    __schema__ = nerdgraph
    __field_names__ = ("text",)
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="text")


class DashboardPageInput(sgqlc.types.Input):
    """Class for DashboardPageInput.

    Page input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "guid", "name", "widgets")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardPieWidgetConfigurationInput(sgqlc.types.Input):
    """Class for DashboardPieWidgetConfigurationInput.

    Configuration for visualization type 'viz.pie'.  Learn more about
    [pie](https://docs.newrelic.com/docs/apis/nerdgraph/examples/creat
    e-widgets-dashboards-api/#pie) widget.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardSnapshotUrlInput(sgqlc.types.Input):
    """Class for DashboardSnapshotUrlInput.

    Parameters that affect the data and the rendering of the
    dashboards returned by the snapshot url mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("time_window",)
    time_window = sgqlc.types.Field(
        "DashboardSnapshotUrlTimeWindowInput", graphql_name="timeWindow"
    )


class DashboardSnapshotUrlTimeWindowInput(sgqlc.types.Input):
    """Class for DashboardSnapshotUrlTimeWindowInput.

    Period of time from which the data to be displayed on the
    dashboard will be obtained.
    """

    __schema__ = nerdgraph
    __field_names__ = ("begin_time", "duration", "end_time")
    begin_time = sgqlc.types.Field(EpochMilliseconds, graphql_name="beginTime")


class DashboardTableWidgetConfigurationInput(sgqlc.types.Input):
    """Class for DashboardTableWidgetConfigurationInput.

    Configuration for visualization type 'viz.table'.  Learn more
    about [table](https://docs.newrelic.com/docs/apis/nerdgraph/exampl
    es/create-widgets-dashboards-api/#table) widget.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardUpdatePageInput(sgqlc.types.Input):
    """Class for DashboardUpdatePageInput.

    Page input used when updating an individual page.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "widgets")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardUpdateWidgetInput(sgqlc.types.Input):
    """Class for DashboardUpdateWidgetInput.

    Input type used when updating widgets.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "configuration",
        "id",
        "layout",
        "linked_entity_guids",
        "raw_configuration",
        "title",
        "visualization",
    )
    configuration = sgqlc.types.Field(
        "DashboardWidgetConfigurationInput", graphql_name="configuration"
    )


class DashboardVariableDefaultItemInput(sgqlc.types.Input):
    """Class for DashboardVariableDefaultItemInput.

    Represents a possible default value item.
    """

    __schema__ = nerdgraph
    __field_names__ = ("value",)
    value = sgqlc.types.Field(
        sgqlc.types.non_null("DashboardVariableDefaultValueInput"), graphql_name="value"
    )


class DashboardVariableDefaultValueInput(sgqlc.types.Input):
    """Class for DashboardVariableDefaultValueInput.

    Specifies a default value for variables.
    """

    __schema__ = nerdgraph
    __field_names__ = ("string",)
    string = sgqlc.types.Field(String, graphql_name="string")


class DashboardVariableEnumItemInput(sgqlc.types.Input):
    """Class for DashboardVariableEnumItemInput.

    Input type that represents a possible value for a variable of type
    ENUM.
    """

    __schema__ = nerdgraph
    __field_names__ = ("title", "value")
    title = sgqlc.types.Field(String, graphql_name="title")


class DashboardVariableInput(sgqlc.types.Input):
    """Class for DashboardVariableInput.

    Definition of a variable that is local to this dashboard.
    Variables are placeholders for dynamic values in widget NRQLs.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "default_value",
        "default_values",
        "is_multi_selection",
        "items",
        "name",
        "nrql_query",
        "replacement_strategy",
        "title",
        "type",
    )
    default_value = sgqlc.types.Field(
        DashboardVariableDefaultValueInput, graphql_name="defaultValue"
    )


class DashboardVariableNrqlQueryInput(sgqlc.types.Input):
    """Class for DashboardVariableNrqlQueryInput.

    Configuration for variables of type NRQL.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "query")
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )


class DashboardWidgetConfigurationInput(sgqlc.types.Input):
    """Class for DashboardWidgetConfigurationInput.

    Typed configuration for known visualizations. At most one may be
    populated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("area", "bar", "billboard", "line", "markdown", "pie", "table")
    area = sgqlc.types.Field(DashboardAreaWidgetConfigurationInput, graphql_name="area")


class DashboardWidgetInput(sgqlc.types.Input):
    """Class for DashboardWidgetInput.

    Widget input.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "configuration",
        "id",
        "layout",
        "linked_entity_guids",
        "raw_configuration",
        "title",
        "visualization",
    )
    configuration = sgqlc.types.Field(
        DashboardWidgetConfigurationInput, graphql_name="configuration"
    )


class DashboardWidgetLayoutInput(sgqlc.types.Input):
    """Class for DashboardWidgetLayoutInput.

    Widget layout input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("column", "height", "row", "width")
    column = sgqlc.types.Field(Int, graphql_name="column")


class DashboardWidgetNrqlQueryInput(sgqlc.types.Input):
    """Class for DashboardWidgetNrqlQueryInput.

    NRQL query used by a widget.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "query")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class DashboardWidgetVisualizationInput(sgqlc.types.Input):
    """Class for DashboardWidgetVisualizationInput.

    Visualization configuration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(String, graphql_name="id")


class DataManagementAccountFeatureSettingInput(sgqlc.types.Input):
    """Class for DataManagementAccountFeatureSettingInput.

    Input object to add and change a feature setting toggle for an
    account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled", "feature_setting", "locked")
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class DataManagementFeatureSettingLookup(sgqlc.types.Input):
    """Class for DataManagementFeatureSettingLookup.

    Input object to lookup a feature setting.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key",)
    key = sgqlc.types.Field(String, graphql_name="key")


class DataManagementRuleInput(sgqlc.types.Input):
    """Class for DataManagementRuleInput.

    Input rule type for bulk rule creation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("namespace", "retention_in_days")
    namespace = sgqlc.types.Field(String, graphql_name="namespace")


class DateTimeWindowInput(sgqlc.types.Input):
    """Class for DateTimeWindowInput.

    Represents a date time window input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("end_time", "start_time")
    end_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name="endTime")


class DomainTypeInput(sgqlc.types.Input):
    """Class for DomainTypeInput.

    Input for getting details about an entity type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("domain", "type")
    domain = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="domain")


class EdgeCreateSpanAttributeRuleInput(sgqlc.types.Input):
    """Class for EdgeCreateSpanAttributeRuleInput.

    Data required to create a span attribute trace filter rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("action", "key", "key_operator", "value", "value_operator")
    action = sgqlc.types.Field(
        sgqlc.types.non_null(EdgeTraceFilterAction), graphql_name="action"
    )


class EdgeCreateTraceFilterRulesInput(sgqlc.types.Input):
    """Class for EdgeCreateTraceFilterRulesInput.

    Input for creating multiple trace filter rules.
    """

    __schema__ = nerdgraph
    __field_names__ = ("span_attribute_rules",)
    span_attribute_rules = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EdgeCreateSpanAttributeRuleInput)),
        graphql_name="spanAttributeRules",
    )


class EdgeCreateTraceObserverInput(sgqlc.types.Input):
    """Class for EdgeCreateTraceObserverInput.

    Data required to create a trace observer.
    """

    __schema__ = nerdgraph
    __field_names__ = ("compliance_types", "monitoring", "name", "provider_region")
    compliance_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EdgeComplianceTypeCode)),
        graphql_name="complianceTypes",
    )


class EdgeDataSourceGroupInput(sgqlc.types.Input):
    """Class for EdgeDataSourceGroupInput.

    Data required to change the data source group.
    """

    __schema__ = nerdgraph
    __field_names__ = ("guids", "update_type")
    guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)), graphql_name="guids"
    )


class EdgeDeleteTraceFilterRulesInput(sgqlc.types.Input):
    """Class for EdgeDeleteTraceFilterRulesInput.

    Input for deleting multiple trace filter rules by id.
    """

    __schema__ = nerdgraph
    __field_names__ = ("span_attribute_rule_ids",)
    span_attribute_rule_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)),
        graphql_name="spanAttributeRuleIds",
    )


class EdgeDeleteTraceObserverInput(sgqlc.types.Input):
    """Class for EdgeDeleteTraceObserverInput.

    Data required to delete a trace observer.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")


class EdgeRandomTraceFilterInput(sgqlc.types.Input):
    """Class for EdgeRandomTraceFilterInput.

    Data required to change the random trace filter configuration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("percent_kept",)
    percent_kept = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="percentKept"
    )


class EdgeUpdateTraceObserverInput(sgqlc.types.Input):
    """Class for EdgeUpdateTraceObserverInput.

    Data required to update a trace observer.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "data_source_group_config",
        "id",
        "monitoring",
        "name",
        "random_trace_filter_config",
    )
    data_source_group_config = sgqlc.types.Field(
        EdgeDataSourceGroupInput, graphql_name="dataSourceGroupConfig"
    )


class EntityGoldenContextInput(sgqlc.types.Input):
    """Class for EntityGoldenContextInput.

    Input type used to define the context for the golden metrics.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account", "guid")
    account = sgqlc.types.Field(Int, graphql_name="account")


class EntityGoldenMetricInput(sgqlc.types.Input):
    """Class for EntityGoldenMetricInput.

    Input type for the metrics.
    """

    __schema__ = nerdgraph
    __field_names__ = ("event_id", "facet", "from_", "name", "select", "title", "where")
    event_id = sgqlc.types.Field(String, graphql_name="eventId")


class EntityGoldenNrqlTimeWindowInput(sgqlc.types.Input):
    """Class for EntityGoldenNrqlTimeWindowInput.

    Time range to apply to the golden metric NRQL query.
    """

    __schema__ = nerdgraph
    __field_names__ = ("since", "until")
    since = sgqlc.types.Field(Nrql, graphql_name="since")


class EntityGoldenTagInput(sgqlc.types.Input):
    """Class for EntityGoldenTagInput.

    An input that represents a golden tag.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key",)
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class EntityRelationshipEdgeFilter(sgqlc.types.Input):
    """Class for EntityRelationshipEdgeFilter.

    EntityRelationship edge filter.
    """

    __schema__ = nerdgraph
    __field_names__ = ("direction", "entity_domain_types", "relationship_types")
    direction = sgqlc.types.Field(
        EntityRelationshipEdgeDirection, graphql_name="direction"
    )


class EntityRelationshipEdgeTypeFilter(sgqlc.types.Input):
    """Class for EntityRelationshipEdgeTypeFilter.

    Filter on relationship types.
    """

    __schema__ = nerdgraph
    __field_names__ = ("exclude", "include")
    exclude = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityRelationshipEdgeType)),
        graphql_name="exclude",
    )


class EntityRelationshipEntityDomainTypeFilter(sgqlc.types.Input):
    """Class for EntityRelationshipEntityDomainTypeFilter.

    Filter on entity domain-types.
    """

    __schema__ = nerdgraph
    __field_names__ = ("exclude", "include")
    exclude = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(DomainTypeInput)),
        graphql_name="exclude",
    )


class EntityRelationshipFilter(sgqlc.types.Input):
    """Class for EntityRelationshipFilter.

    Relationship filter.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_type", "infrastructure_integration_type")
    entity_type = sgqlc.types.Field(
        sgqlc.types.list_of(EntityType), graphql_name="entityType"
    )


class EntitySearchOptions(sgqlc.types.Input):
    """Class for EntitySearchOptions.

    Additional entity search options.
    """

    __schema__ = nerdgraph
    __field_names__ = ("case_sensitive_tag_matching", "limit")
    case_sensitive_tag_matching = sgqlc.types.Field(
        Boolean, graphql_name="caseSensitiveTagMatching"
    )


class EntitySearchQueryBuilder(sgqlc.types.Input):
    """Class for EntitySearchQueryBuilder.

    An object that can be used to discover and create the entity
    search query argument.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "alert_severity",
        "alertable",
        "domain",
        "infrastructure_integration_type",
        "name",
        "reporting",
        "tags",
        "type",
    )
    alert_severity = sgqlc.types.Field(
        EntityAlertSeverity, graphql_name="alertSeverity"
    )


class EntitySearchQueryBuilderTag(sgqlc.types.Input):
    """Class for EntitySearchQueryBuilderTag.

    An entity tag.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class ErrorsInboxAssignErrorGroupInput(sgqlc.types.Input):
    """Class for ErrorsInboxAssignErrorGroupInput.

    Input for assignment mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("user_email", "user_id")
    user_email = sgqlc.types.Field(String, graphql_name="userEmail")


class ErrorsInboxAssignmentSearchFilterInput(sgqlc.types.Input):
    """Class for ErrorsInboxAssignmentSearchFilterInput.

    Input type for assignment search filter.
    """

    __schema__ = nerdgraph
    __field_names__ = ("user_email", "user_id")
    user_email = sgqlc.types.Field(String, graphql_name="userEmail")


class ErrorsInboxErrorEventInput(sgqlc.types.Input):
    """Class for ErrorsInboxErrorEventInput.

    Input for error events.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_guid", "message", "name")
    entity_guid = sgqlc.types.Field(
        sgqlc.types.non_null(EntityGuid), graphql_name="entityGuid"
    )


class ErrorsInboxErrorGroupSearchFilterInput(sgqlc.types.Input):
    """Class for ErrorsInboxErrorGroupSearchFilterInput.

    Set of filters for scoping error group searches.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_ids",
        "application_versions",
        "assignment",
        "ids",
        "is_assigned",
        "states",
    )
    account_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="accountIds"
    )


class ErrorsInboxErrorGroupSortOrderInput(sgqlc.types.Input):
    """Class for ErrorsInboxErrorGroupSortOrderInput.

    Sort object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("direction", "field")
    direction = sgqlc.types.Field(
        sgqlc.types.non_null(ErrorsInboxDirection), graphql_name="direction"
    )


class ErrorsInboxResourceFilterInput(sgqlc.types.Input):
    """Class for ErrorsInboxResourceFilterInput.

    Criteria for the resource filter.
    """

    __schema__ = nerdgraph
    __field_names__ = ("types",)
    types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ErrorsInboxResourceType)),
        graphql_name="types",
    )


class EventsToMetricsCreateRuleInput(sgqlc.types.Input):
    """Class for EventsToMetricsCreateRuleInput.

    Details needed to create an events to metrics conversion rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "description", "name", "nrql")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class EventsToMetricsDeleteRuleInput(sgqlc.types.Input):
    """Class for EventsToMetricsDeleteRuleInput.

    Identifying information about the events to metrics rule you want
    to delete.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "rule_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class EventsToMetricsUpdateRuleInput(sgqlc.types.Input):
    """Class for EventsToMetricsUpdateRuleInput.

    Identifying information about the events to metrics rule you want
    to update.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "enabled", "rule_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class InstallationInstallStatusInput(sgqlc.types.Input):
    """Class for InstallationInstallStatusInput.

    An object that contains the overall installation status to be
    created.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "cli_version",
        "deployed_by",
        "enabled_proxy",
        "error",
        "host_name",
        "install_id",
        "install_library_version",
        "is_unsupported",
        "kernel_arch",
        "kernel_version",
        "log_file_path",
        "os",
        "platform",
        "platform_family",
        "platform_version",
        "redirect_url",
        "state",
        "targeted_install",
        "timestamp",
    )
    cli_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="cliVersion"
    )


class InstallationRecipeStatus(sgqlc.types.Input):
    """Class for InstallationRecipeStatus.

    An object that represents a recipe status.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "cli_version",
        "complete",
        "display_name",
        "entity_guid",
        "error",
        "host_name",
        "install_id",
        "install_library_version",
        "kernel_arch",
        "kernel_version",
        "log_file_path",
        "metadata",
        "name",
        "os",
        "platform",
        "platform_family",
        "platform_version",
        "redirect_url",
        "status",
        "targeted_install",
        "task_path",
        "validation_duration_milliseconds",
    )
    cli_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="cliVersion"
    )


class InstallationStatusErrorInput(sgqlc.types.Input):
    """Class for InstallationStatusErrorInput.

    An object that represents a status error whenever an recipe has
    failed to install.
    """

    __schema__ = nerdgraph
    __field_names__ = ("details", "message")
    details = sgqlc.types.Field(String, graphql_name="details")


class LogConfigurationsCreateDataPartitionRuleInput(sgqlc.types.Input):
    """Class for LogConfigurationsCreateDataPartitionRuleInput.

    A new data partition rule.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "enabled",
        "matching_criteria",
        "nrql",
        "retention_policy",
        "target_data_partition",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class LogConfigurationsCreateObfuscationActionInput(sgqlc.types.Input):
    """Class for LogConfigurationsCreateObfuscationActionInput.

    Input for creating an obfuscation action on a rule being created.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attributes", "expression_id", "method")
    attributes = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="attributes",
    )


class LogConfigurationsCreateObfuscationExpressionInput(sgqlc.types.Input):
    """Class for LogConfigurationsCreateObfuscationExpressionInput.

    Input for creating an obfuscation expression.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "regex")
    description = sgqlc.types.Field(String, graphql_name="description")


class LogConfigurationsCreateObfuscationRuleInput(sgqlc.types.Input):
    """Class for LogConfigurationsCreateObfuscationRuleInput.

    Input for creating an obfuscation rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("actions", "description", "enabled", "filter", "name")
    actions = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(LogConfigurationsCreateObfuscationActionInput)
            )
        ),
        graphql_name="actions",
    )


class LogConfigurationsDataPartitionRuleMatchingCriteriaInput(sgqlc.types.Input):
    """Class for LogConfigurationsDataPartitionRuleMatchingCriteriaInput.

    The data partition rule matching criteria.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute_name", "matching_expression", "matching_method")
    attribute_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attributeName"
    )


class LogConfigurationsParsingRuleConfiguration(sgqlc.types.Input):
    """Class for LogConfigurationsParsingRuleConfiguration.

    A new parsing rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "description", "enabled", "grok", "lucene", "nrql")
    attribute = sgqlc.types.Field(String, graphql_name="attribute")


class LogConfigurationsPipelineConfigurationInput(sgqlc.types.Input):
    """Class for LogConfigurationsPipelineConfigurationInput.

    The pipeline configuration for an account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "enrichment_disabled",
        "json_parsing_disabled",
        "obfuscation_disabled",
        "parsing_disabled",
        "patterns_enabled",
        "recursive_json_parsing_disabled",
        "transformation_disabled",
    )
    enrichment_disabled = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="enrichmentDisabled"
    )


class LogConfigurationsUpdateDataPartitionRuleInput(sgqlc.types.Input):
    """Class for LogConfigurationsUpdateDataPartitionRuleInput.

    An object for updating an existing data partition rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "enabled", "id", "matching_criteria", "nrql")
    description = sgqlc.types.Field(String, graphql_name="description")


class LogConfigurationsUpdateObfuscationActionInput(sgqlc.types.Input):
    """Class for LogConfigurationsUpdateObfuscationActionInput.

    Input for creating an obfuscation action on a rule being updated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attributes", "expression_id", "method")
    attributes = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="attributes",
    )


class LogConfigurationsUpdateObfuscationExpressionInput(sgqlc.types.Input):
    """Class for LogConfigurationsUpdateObfuscationExpressionInput.

    Input for updating an obfuscation expression. Null fields are left
    untouched by mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "id", "name", "regex")
    description = sgqlc.types.Field(String, graphql_name="description")


class LogConfigurationsUpdateObfuscationRuleInput(sgqlc.types.Input):
    """Class for LogConfigurationsUpdateObfuscationRuleInput.

    Input for updating an obfuscation rule. Null fields are left
    untouched by mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("actions", "description", "enabled", "filter", "id", "name")
    actions = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(LogConfigurationsUpdateObfuscationActionInput)
        ),
        graphql_name="actions",
    )


class MetricNormalizationCreateRuleInput(sgqlc.types.Input):
    """Class for MetricNormalizationCreateRuleInput.

    Input object used to represent the rule to be created.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "action",
        "application_guid",
        "enabled",
        "eval_order",
        "match_expression",
        "notes",
        "replacement",
        "terminate_chain",
    )
    action = sgqlc.types.Field(
        sgqlc.types.non_null(MetricNormalizationCustomerRuleAction),
        graphql_name="action",
    )


class MetricNormalizationEditRuleInput(sgqlc.types.Input):
    """Class for MetricNormalizationEditRuleInput.

    Input object used to represent the rule to be created.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "action",
        "enabled",
        "eval_order",
        "id",
        "match_expression",
        "notes",
        "replacement",
        "terminate_chain",
    )
    action = sgqlc.types.Field(
        sgqlc.types.non_null(MetricNormalizationCustomerRuleAction),
        graphql_name="action",
    )


class NerdStorageScopeInput(sgqlc.types.Input):
    """Class for NerdStorageScopeInput.

    The data access level and ID for the selected scope.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")


class NerdStorageVaultScope(sgqlc.types.Input):
    """Class for NerdStorageVaultScope.

    The NerdStorageVault data access level.
    """

    __schema__ = nerdgraph
    __field_names__ = ("actor",)
    actor = sgqlc.types.Field(NerdStorageVaultActorScope, graphql_name="actor")


class NerdStorageVaultWriteSecretInput(sgqlc.types.Input):
    """Class for NerdStorageVaultWriteSecretInput.

    The data to be stored in NerdStorageVault.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class NerdpackAllowListInput(sgqlc.types.Input):
    """Class for NerdpackAllowListInput.

    Input data for allow list handling.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name="accountIds"
    )


class NerdpackCreationInput(sgqlc.types.Input):
    """Class for NerdpackCreationInput.

    Input data for creating a new nerdpack.
    """

    __schema__ = nerdgraph
    __field_names__ = ("owner_account",)
    owner_account = sgqlc.types.Field(Int, graphql_name="ownerAccount")


class NerdpackDataFilter(sgqlc.types.Input):
    """Class for NerdpackDataFilter.

    Data to filter subscribable nerdpack list.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "subscription_model", "tag")
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class NerdpackOverrideVersionRules(sgqlc.types.Input):
    """Class for NerdpackOverrideVersionRules.

    Attributes to match a specific nerdpack versions.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nerdpack_id", "tag", "version")
    nerdpack_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="nerdpackId")


class NerdpackRemoveVersionTagInput(sgqlc.types.Input):
    """Class for NerdpackRemoveVersionTagInput.

    Input data that identifies nerdpack tag.
    """

    __schema__ = nerdgraph
    __field_names__ = ("tag",)
    tag = sgqlc.types.Field(NerdpackTagName, graphql_name="tag")


class NerdpackSubscribeAccountsInput(sgqlc.types.Input):
    """Class for NerdpackSubscribeAccountsInput.

    New subscriptions input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "tag")
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )


class NerdpackTagVersionInput(sgqlc.types.Input):
    """Class for NerdpackTagVersionInput.

    Input data for nerdpack version tagging.
    """

    __schema__ = nerdgraph
    __field_names__ = ("tag", "version")
    tag = sgqlc.types.Field(NerdpackTagName, graphql_name="tag")


class NerdpackUnsubscribeAccountsInput(sgqlc.types.Input):
    """Class for NerdpackUnsubscribeAccountsInput.

    Data of accounts to be unsubscribed.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )


class NerdpackVersionFilter(sgqlc.types.Input):
    """Class for NerdpackVersionFilter.

    Attributes to filter a list of nerdpack versions. Restrictions:
    'tags' attribute cannot combined with other attributes.
    """

    __schema__ = nerdgraph
    __field_names__ = ("fallback", "tag", "tags", "version")
    fallback = sgqlc.types.Field(NerdpackVersionFilterFallback, graphql_name="fallback")


class Nr1CatalogCommunityContactChannelInput(sgqlc.types.Input):
    """Class for Nr1CatalogCommunityContactChannelInput.

    Details about the contact channel where users can get support via
    the web.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogEmailContactChannelInput(sgqlc.types.Input):
    """Class for Nr1CatalogEmailContactChannelInput.

    Details about the contact channel where users can get support via
    email.
    """

    __schema__ = nerdgraph
    __field_names__ = ("address",)
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="address")


class Nr1CatalogIssuesContactChannelInput(sgqlc.types.Input):
    """Class for Nr1CatalogIssuesContactChannelInput.

    Details about the contact channel where users can get support via
    the repository issues page.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogSearchFilter(sgqlc.types.Input):
    """Class for Nr1CatalogSearchFilter.

    Criteria for applying filters to a search.
    """

    __schema__ = nerdgraph
    __field_names__ = ("categories", "category", "components", "keywords", "types")
    categories = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="categories"
    )


class Nr1CatalogSubmitMetadataInput(sgqlc.types.Input):
    """Class for Nr1CatalogSubmitMetadataInput.

    Metadata associated with the Nerdpack that will be available in
    the New Relic One Catalog.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "additional_info",
        "category_terms",
        "details",
        "documentation",
        "keywords",
        "repository",
        "support",
        "tagline",
        "version",
        "whats_new",
    )
    additional_info = sgqlc.types.Field(String, graphql_name="additionalInfo")


class Nr1CatalogSupportInput(sgqlc.types.Input):
    """Class for Nr1CatalogSupportInput.

    A container specifying the various types support channels.
    """

    __schema__ = nerdgraph
    __field_names__ = ("community", "email", "issues")
    community = sgqlc.types.Field(
        Nr1CatalogCommunityContactChannelInput, graphql_name="community"
    )


class NrqlDropRulesCreateDropRuleInput(sgqlc.types.Input):
    """Class for NrqlDropRulesCreateDropRuleInput.

    Details needed to create a NRQL drop rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("action", "description", "nrql")
    action = sgqlc.types.Field(
        sgqlc.types.non_null(NrqlDropRulesAction), graphql_name="action"
    )


class NrqlQueryOptions(sgqlc.types.Input):
    """Class for NrqlQueryOptions.

    Additional options for NRQL queries.
    """

    __schema__ = nerdgraph
    __field_names__ = ("event_namespaces",)
    event_namespaces = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="eventNamespaces",
    )


class OrganizationCreateSharedAccountInput(sgqlc.types.Input):
    """Class for OrganizationCreateSharedAccountInput.

    Attributes for creating a shared account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "limiting_role_id",
        "name",
        "target_organization_id",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class OrganizationCustomerOrganizationFilterInput(sgqlc.types.Input):
    """Class for OrganizationCustomerOrganizationFilterInput.

    A filter for customer organizations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "authentication_domain_id",
        "customer_id",
        "id",
        "name",
    )
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class OrganizationProvisioningProductInput(sgqlc.types.Input):
    """Class for OrganizationProvisioningProductInput.

    A product.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "name", "units_of_measure")
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")


class OrganizationProvisioningUnitOfMeasureInput(sgqlc.types.Input):
    """Class for OrganizationProvisioningUnitOfMeasureInput.

    UOM or unit of measure used to know what a product charges for,
    such as events, hosts, CUs, etc.
    """

    __schema__ = nerdgraph
    __field_names__ = ("quantity", "unit")
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="quantity")


class OrganizationRevokeSharedAccountInput(sgqlc.types.Input):
    """Class for OrganizationRevokeSharedAccountInput.

    Attributes for revoking an account share.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")


class OrganizationUpdateInput(sgqlc.types.Input):
    """Class for OrganizationUpdateInput.

    Attributes for updating an organization.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class OrganizationUpdateSharedAccountInput(sgqlc.types.Input):
    """Class for OrganizationUpdateSharedAccountInput.

    Attributes for updating an account share.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "limiting_role_id")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")


class QueryHistoryQueryHistoryOptionsInput(sgqlc.types.Input):
    """Class for QueryHistoryQueryHistoryOptionsInput.

    Input condition to select query records.
    """

    __schema__ = nerdgraph
    __field_names__ = ("limit",)
    limit = sgqlc.types.Field(Int, graphql_name="limit")


class ReferenceEntityCreateRepositoryInput(sgqlc.types.Input):
    """Class for ReferenceEntityCreateRepositoryInput.

    Information needed to create a repository entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "name", "url")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class ServiceLevelEventsCreateInput(sgqlc.types.Input):
    """Class for ServiceLevelEventsCreateInput.

    The events that define the SLI.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "bad_events", "good_events", "valid_events")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class ServiceLevelEventsQueryCreateInput(sgqlc.types.Input):
    """Class for ServiceLevelEventsQueryCreateInput.

    The query that represents the events to fetch.
    """

    __schema__ = nerdgraph
    __field_names__ = ("from_", "select", "where")
    from_ = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="from")


class ServiceLevelEventsQuerySelectCreateInput(sgqlc.types.Input):
    """Class for ServiceLevelEventsQuerySelectCreateInput.

    The NRQL SELECT clause to aggregate events.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "function")
    attribute = sgqlc.types.Field(String, graphql_name="attribute")


class ServiceLevelEventsQuerySelectUpdateInput(sgqlc.types.Input):
    """Class for ServiceLevelEventsQuerySelectUpdateInput.

    The NRQL SELECT clause to aggregate events.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "function")
    attribute = sgqlc.types.Field(String, graphql_name="attribute")


class ServiceLevelEventsQueryUpdateInput(sgqlc.types.Input):
    """Class for ServiceLevelEventsQueryUpdateInput.

    The query that represents the events to fetch.
    """

    __schema__ = nerdgraph
    __field_names__ = ("from_", "select", "where")
    from_ = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="from")


class ServiceLevelEventsUpdateInput(sgqlc.types.Input):
    """Class for ServiceLevelEventsUpdateInput.

    The events that define the SLI.
    """

    __schema__ = nerdgraph
    __field_names__ = ("bad_events", "good_events", "valid_events")
    bad_events = sgqlc.types.Field(
        ServiceLevelEventsQueryUpdateInput, graphql_name="badEvents"
    )


class ServiceLevelIndicatorCreateInput(sgqlc.types.Input):
    """Class for ServiceLevelIndicatorCreateInput.

    The input object that represents the SLI that will be created.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "events", "name", "objectives", "slug")
    description = sgqlc.types.Field(String, graphql_name="description")


class ServiceLevelIndicatorUpdateInput(sgqlc.types.Input):
    """Class for ServiceLevelIndicatorUpdateInput.

    The input object that represents the SLI that will be updated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "events", "name", "objectives")
    description = sgqlc.types.Field(String, graphql_name="description")


class ServiceLevelObjectiveCreateInput(sgqlc.types.Input):
    """Class for ServiceLevelObjectiveCreateInput.

    The input object that represents an objective definition.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "target", "time_window")
    description = sgqlc.types.Field(String, graphql_name="description")


class ServiceLevelObjectiveRollingTimeWindowCreateInput(sgqlc.types.Input):
    """Class for ServiceLevelObjectiveRollingTimeWindowCreateInput.

    The rolling time window configuration of the SLO.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "unit")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class ServiceLevelObjectiveRollingTimeWindowUpdateInput(sgqlc.types.Input):
    """Class for ServiceLevelObjectiveRollingTimeWindowUpdateInput.

    The rolling time window configuration of the SLO.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "unit")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class ServiceLevelObjectiveTimeWindowCreateInput(sgqlc.types.Input):
    """Class for ServiceLevelObjectiveTimeWindowCreateInput.

    The time window configuration of the SLO.
    """

    __schema__ = nerdgraph
    __field_names__ = ("rolling",)
    rolling = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelObjectiveRollingTimeWindowCreateInput),
        graphql_name="rolling",
    )


class ServiceLevelObjectiveTimeWindowUpdateInput(sgqlc.types.Input):
    """Class for ServiceLevelObjectiveTimeWindowUpdateInput.

    The time window configuration of the SLO.
    """

    __schema__ = nerdgraph
    __field_names__ = ("rolling",)
    rolling = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelObjectiveRollingTimeWindowUpdateInput),
        graphql_name="rolling",
    )


class ServiceLevelObjectiveUpdateInput(sgqlc.types.Input):
    """Class for ServiceLevelObjectiveUpdateInput.

    The input object that represents an objective definition.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "target", "time_window")
    description = sgqlc.types.Field(String, graphql_name="description")


class SortCriterionWithDirection(sgqlc.types.Input):
    """Class for SortCriterionWithDirection.

    Possible entity sorting criterion with direction.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "direction", "tag")
    attribute = sgqlc.types.Field(EntitySearchSortCriteria, graphql_name="attribute")


class StreamingExportAwsInput(sgqlc.types.Input):
    """Class for StreamingExportAwsInput.

    AWS input parameters for a new streaming rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_account_id", "delivery_stream_name", "region", "role")
    aws_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="awsAccountId"
    )


class StreamingExportAzureInput(sgqlc.types.Input):
    """Class for StreamingExportAzureInput.

    Azure input parameters for a new streaming rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("event_hub_connection_string", "event_hub_name")
    event_hub_connection_string = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="eventHubConnectionString"
    )


class StreamingExportRuleInput(sgqlc.types.Input):
    """Class for StreamingExportRuleInput.

    The input parameters for a new streaming rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "nrql")
    description = sgqlc.types.Field(String, graphql_name="description")


class SyntheticsCreateBrokenLinksMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsCreateBrokenLinksMonitorInput.

    The monitor input values needed to create a Broken Links monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "locations",
        "name",
        "period",
        "status",
        "tags",
        "uri",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class SyntheticsCreateCertCheckMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsCreateCertCheckMonitorInput.

    The monitor input values needed to create a Cert Check monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "domain",
        "locations",
        "name",
        "number_days_to_fail_before_cert_expires",
        "period",
        "status",
        "tags",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class SyntheticsCreateScriptApiMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsCreateScriptApiMonitorInput.

    The monitor input values needed to create a Script Api monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "locations",
        "name",
        "period",
        "runtime",
        "script",
        "status",
        "tags",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class SyntheticsCreateScriptBrowserMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsCreateScriptBrowserMonitorInput.

    The monitor input values needed to create a Script Browser monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "locations",
        "name",
        "period",
        "runtime",
        "script",
        "status",
        "tags",
    )
    advanced_options = sgqlc.types.Field(
        "SyntheticsScriptBrowserMonitorAdvancedOptionsInput",
        graphql_name="advancedOptions",
    )


class SyntheticsCreateSimpleBrowserMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsCreateSimpleBrowserMonitorInput.

    The monitor input values needed to create a Simple Browser monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "locations",
        "name",
        "period",
        "runtime",
        "status",
        "tags",
        "uri",
    )
    advanced_options = sgqlc.types.Field(
        "SyntheticsSimpleBrowserMonitorAdvancedOptionsInput",
        graphql_name="advancedOptions",
    )


class SyntheticsCreateSimpleMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsCreateSimpleMonitorInput.

    The monitor input values needed to create a Simple (ping) monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "locations",
        "name",
        "period",
        "status",
        "tags",
        "uri",
    )
    advanced_options = sgqlc.types.Field(
        "SyntheticsSimpleMonitorAdvancedOptionsInput", graphql_name="advancedOptions"
    )


class SyntheticsCreateStepMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsCreateStepMonitorInput.

    The monitor input values needed to create a Step monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "locations",
        "name",
        "period",
        "status",
        "steps",
        "tags",
    )
    advanced_options = sgqlc.types.Field(
        "SyntheticsStepMonitorAdvancedOptionsInput", graphql_name="advancedOptions"
    )


class SyntheticsCustomHeaderInput(sgqlc.types.Input):
    """Class for SyntheticsCustomHeaderInput.

    Custom header input for monitor jobs.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "value")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class SyntheticsDeviceEmulationInput(sgqlc.types.Input):
    """Class for SyntheticsDeviceEmulationInput.

    Information related to device browser emulation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("device_orientation", "device_type")
    device_orientation = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsDeviceOrientation),
        graphql_name="deviceOrientation",
    )


class SyntheticsLocationsInput(sgqlc.types.Input):
    """Class for SyntheticsLocationsInput.

    The location(s) from which a non-scripted monitor runs.
    """

    __schema__ = nerdgraph
    __field_names__ = ("private", "public")
    private = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="private")


class SyntheticsPrivateLocationInput(sgqlc.types.Input):
    """Class for SyntheticsPrivateLocationInput.

    Information realating to a private location.
    """

    __schema__ = nerdgraph
    __field_names__ = ("guid", "vse_password")
    guid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="guid")


class SyntheticsRuntimeInput(sgqlc.types.Input):
    """Class for SyntheticsRuntimeInput.

    Input to determine which runtime the monitor will run.
    """

    __schema__ = nerdgraph
    __field_names__ = ("runtime_type", "runtime_type_version", "script_language")
    runtime_type = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="runtimeType"
    )


class SyntheticsScriptBrowserMonitorAdvancedOptionsInput(sgqlc.types.Input):
    """Class for SyntheticsScriptBrowserMonitorAdvancedOptionsInput.

    The advanced options inputs available for a Script Browser monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = ("device_emulation", "enable_screenshot_on_failure_and_script")
    device_emulation = sgqlc.types.Field(
        SyntheticsDeviceEmulationInput, graphql_name="deviceEmulation"
    )


class SyntheticsScriptedMonitorLocationsInput(sgqlc.types.Input):
    """Class for SyntheticsScriptedMonitorLocationsInput.

    The location(s) from which the scripted monitor runs.
    """

    __schema__ = nerdgraph
    __field_names__ = ("private", "public")
    private = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(SyntheticsPrivateLocationInput)),
        graphql_name="private",
    )


class SyntheticsSimpleBrowserMonitorAdvancedOptionsInput(sgqlc.types.Input):
    """Class for SyntheticsSimpleBrowserMonitorAdvancedOptionsInput.

    The advanced options inputs available for a Simple Browser monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "custom_headers",
        "device_emulation",
        "enable_screenshot_on_failure_and_script",
        "response_validation_text",
        "use_tls_validation",
    )
    custom_headers = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsCustomHeaderInput), graphql_name="customHeaders"
    )


class SyntheticsSimpleMonitorAdvancedOptionsInput(sgqlc.types.Input):
    """Class for SyntheticsSimpleMonitorAdvancedOptionsInput.

    The advanced options inputs available for a Simple (ping) monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "custom_headers",
        "redirect_is_failure",
        "response_validation_text",
        "should_bypass_head_request",
        "use_tls_validation",
    )
    custom_headers = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsCustomHeaderInput), graphql_name="customHeaders"
    )


class SyntheticsStepInput(sgqlc.types.Input):
    """Class for SyntheticsStepInput.

    A step that will be added to the monitor script.
    """

    __schema__ = nerdgraph
    __field_names__ = ("ordinal", "type", "values")
    ordinal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="ordinal")


class SyntheticsStepMonitorAdvancedOptionsInput(sgqlc.types.Input):
    """Class for SyntheticsStepMonitorAdvancedOptionsInput.

    The advanced options inputs available for a Step monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enable_screenshot_on_failure_and_script",)
    enable_screenshot_on_failure_and_script = sgqlc.types.Field(
        Boolean, graphql_name="enableScreenshotOnFailureAndScript"
    )


class SyntheticsTag(sgqlc.types.Input):
    """Class for SyntheticsTag.

    Tag entries for the monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "values")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class SyntheticsUpdateBrokenLinksMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsUpdateBrokenLinksMonitorInput.

    The monitor values that can be updated on a Broken Links monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "locations",
        "name",
        "period",
        "status",
        "tags",
        "uri",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class SyntheticsUpdateCertCheckMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsUpdateCertCheckMonitorInput.

    The monitor values that can be updated on a Cert Check monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "domain",
        "locations",
        "name",
        "number_days_to_fail_before_cert_expires",
        "period",
        "status",
        "tags",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class SyntheticsUpdateScriptApiMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsUpdateScriptApiMonitorInput.

    The monitor values that can be updated on a Script Api monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "locations",
        "name",
        "period",
        "runtime",
        "script",
        "status",
        "tags",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class SyntheticsUpdateScriptBrowserMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsUpdateScriptBrowserMonitorInput.

    The monitor values that can be updated on a Script Browser monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "locations",
        "name",
        "period",
        "runtime",
        "script",
        "status",
        "tags",
    )
    advanced_options = sgqlc.types.Field(
        SyntheticsScriptBrowserMonitorAdvancedOptionsInput,
        graphql_name="advancedOptions",
    )


class SyntheticsUpdateSimpleBrowserMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsUpdateSimpleBrowserMonitorInput.

    The monitor values that can be updated on a Simple Browser monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "locations",
        "name",
        "period",
        "runtime",
        "status",
        "tags",
        "uri",
    )
    advanced_options = sgqlc.types.Field(
        SyntheticsSimpleBrowserMonitorAdvancedOptionsInput,
        graphql_name="advancedOptions",
    )


class SyntheticsUpdateSimpleMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsUpdateSimpleMonitorInput.

    The monitor values that can be updated on a simple (ping) monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "locations",
        "name",
        "period",
        "status",
        "tags",
        "uri",
    )
    advanced_options = sgqlc.types.Field(
        SyntheticsSimpleMonitorAdvancedOptionsInput, graphql_name="advancedOptions"
    )


class SyntheticsUpdateStepMonitorInput(sgqlc.types.Input):
    """Class for SyntheticsUpdateStepMonitorInput.

    The monitor values that can be updated on a Step monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "locations",
        "name",
        "period",
        "status",
        "steps",
        "tags",
    )
    advanced_options = sgqlc.types.Field(
        SyntheticsStepMonitorAdvancedOptionsInput, graphql_name="advancedOptions"
    )


class TaggingTagInput(sgqlc.types.Input):
    """Class for TaggingTagInput.

    An object that represents a tag key-values pair.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "values")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class TaggingTagValueInput(sgqlc.types.Input):
    """Class for TaggingTagValueInput.

    An object that represents a tag key-value pair.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class TimeWindowInput(sgqlc.types.Input):
    """Class for TimeWindowInput.

    Represents a time window input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("end_time", "start_time")
    end_time = sgqlc.types.Field(
        sgqlc.types.non_null(EpochMilliseconds), graphql_name="endTime"
    )


class UserManagementCreateGroup(sgqlc.types.Input):
    """Class for UserManagementCreateGroup.

    The input object representing the group being created.
    """

    __schema__ = nerdgraph
    __field_names__ = ("authentication_domain_id", "display_name")
    authentication_domain_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="authenticationDomainId"
    )


class UserManagementCreateUser(sgqlc.types.Input):
    """Class for UserManagementCreateUser.

    The input object representing the user being created.
    """

    __schema__ = nerdgraph
    __field_names__ = ("authentication_domain_id", "email", "name", "user_type")
    authentication_domain_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="authenticationDomainId"
    )


class UserManagementDeleteGroup(sgqlc.types.Input):
    """Class for UserManagementDeleteGroup.

    The input object representing the group to remove.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")


class UserManagementDeleteUser(sgqlc.types.Input):
    """Class for UserManagementDeleteUser.

    The input object representing the user being deleted.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class UserManagementUpdateGroup(sgqlc.types.Input):
    """Class for UserManagementUpdateGroup.

    The input object representing the group being updated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_name", "id")
    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )


class UserManagementUpdateUser(sgqlc.types.Input):
    """Class for UserManagementUpdateUser.

    The input object representing the user being updated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("email", "id", "name", "time_zone", "user_type")
    email = sgqlc.types.Field(String, graphql_name="email")


class UserManagementUsersGroupsInput(sgqlc.types.Input):
    """Class for UserManagementUsersGroupsInput.

    The input object representing the group(s) and user(s) to update.
    """

    __schema__ = nerdgraph
    __field_names__ = ("group_ids", "user_ids")
    group_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))),
        graphql_name="groupIds",
    )


class UsersUserSearchQuery(sgqlc.types.Input):
    """Class for UsersUserSearchQuery.

    Query object for UserSearch.
    """

    __schema__ = nerdgraph
    __field_names__ = ("scope",)
    scope = sgqlc.types.Field("UsersUserSearchScope", graphql_name="scope")


class UsersUserSearchScope(sgqlc.types.Input):
    """Class for UsersUserSearchScope.

    Different scopes that can be used to filter the returned users.
    """

    __schema__ = nerdgraph
    __field_names__ = ("email", "name", "search", "user_ids")
    email = sgqlc.types.Field(String, graphql_name="email")


class WhatsNewContentSearchQuery(sgqlc.types.Input):
    """Class for WhatsNewContentSearchQuery.

    A query that represents a criteria for searching news.
    """

    __schema__ = nerdgraph
    __field_names__ = ("content_type", "unread_only")
    content_type = sgqlc.types.Field(WhatsNewContentType, graphql_name="contentType")


class WorkloadAutomaticStatusInput(sgqlc.types.Input):
    """Class for WorkloadAutomaticStatusInput.

    An input object used to represent an automatic status
    configuration. If not provided, a status configuration will be
    created by default.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled", "remaining_entities_rule", "rules")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")


class WorkloadCreateInput(sgqlc.types.Input):
    """Class for WorkloadCreateInput.

    The input object used to represent the workload to be created.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "entity_guids",
        "entity_search_queries",
        "name",
        "scope_accounts",
        "status_config",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class WorkloadDuplicateInput(sgqlc.types.Input):
    """Class for WorkloadDuplicateInput.

    The input object used to represent the workload duplicate.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class WorkloadEntitySearchQueryInput(sgqlc.types.Input):
    """Class for WorkloadEntitySearchQueryInput.

    The input object used to represent the entity search query to be
    created.
    """

    __schema__ = nerdgraph
    __field_names__ = ("query",)
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="query")


class WorkloadRegularRuleInput(sgqlc.types.Input):
    """Class for WorkloadRegularRuleInput.

    The input object used to represent a rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_search_queries", "rollup")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )


class WorkloadRemainingEntitiesRuleInput(sgqlc.types.Input):
    """Class for WorkloadRemainingEntitiesRuleInput.

    The input object used to represent a remaining entities rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("rollup",)
    rollup = sgqlc.types.Field(
        sgqlc.types.non_null("WorkloadRemainingEntitiesRuleRollupInput"),
        graphql_name="rollup",
    )


class WorkloadRemainingEntitiesRuleRollupInput(sgqlc.types.Input):
    """Class for WorkloadRemainingEntitiesRuleRollupInput.

    The input object used to represent a rollup strategy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("group_by", "strategy", "threshold_type", "threshold_value")
    group_by = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadGroupRemainingEntitiesRuleBy),
        graphql_name="groupBy",
    )


class WorkloadRollupInput(sgqlc.types.Input):
    """Class for WorkloadRollupInput.

    The input object used to represent a rollup strategy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("strategy", "threshold_type", "threshold_value")
    strategy = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadRollupStrategy), graphql_name="strategy"
    )


class WorkloadScopeAccountsInput(sgqlc.types.Input):
    """Class for WorkloadScopeAccountsInput.

    The input object containing accounts that will be used to get
    entities from.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )


class WorkloadStaticStatusInput(sgqlc.types.Input):
    """Class for WorkloadStaticStatusInput.

    The input object used to represent the configuration of a static
    status.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "enabled", "status", "summary")
    description = sgqlc.types.Field(String, graphql_name="description")


class WorkloadStatusConfigInput(sgqlc.types.Input):
    """Class for WorkloadStatusConfigInput.

    The input object used to provide the configuration that defines
    how the status of the workload is calculated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("automatic", "static")
    automatic = sgqlc.types.Field(
        WorkloadAutomaticStatusInput, graphql_name="automatic"
    )


class WorkloadUpdateAutomaticStatusInput(sgqlc.types.Input):
    """Class for WorkloadUpdateAutomaticStatusInput.

    An input object used to represent an automatic status
    configuration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled", "remaining_entities_rule", "rules")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")


class WorkloadUpdateCollectionEntitySearchQueryInput(sgqlc.types.Input):
    """Class for WorkloadUpdateCollectionEntitySearchQueryInput.

    The input object used to represent the entity search query to be
    updated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "query")
    id = sgqlc.types.Field(Int, graphql_name="id")


class WorkloadUpdateInput(sgqlc.types.Input):
    """Class for WorkloadUpdateInput.

    The input object used to identify the workload to be updated and
    the new values.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "entity_guids",
        "entity_search_queries",
        "name",
        "scope_accounts",
        "status_config",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class WorkloadUpdateRegularRuleInput(sgqlc.types.Input):
    """Class for WorkloadUpdateRegularRuleInput.

    The input object used to represent a rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_search_queries", "id", "rollup")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )


class WorkloadUpdateStaticStatusInput(sgqlc.types.Input):
    """Class for WorkloadUpdateStaticStatusInput.

    The input object used to represent the configuration of a static
    status.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "enabled", "id", "status", "summary")
    description = sgqlc.types.Field(String, graphql_name="description")


class WorkloadUpdateStatusConfigInput(sgqlc.types.Input):
    """Class for WorkloadUpdateStatusConfigInput.

    The input object used to provide the configuration that defines
    how the status of the workload is calculated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("automatic", "static")
    automatic = sgqlc.types.Field(
        WorkloadUpdateAutomaticStatusInput, graphql_name="automatic"
    )
