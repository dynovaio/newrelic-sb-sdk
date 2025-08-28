__all__ = [
    "AccountManagementCreateInput",
    "AccountManagementUpdateInput",
    "AgentApplicationBrowserSettingsInput",
    "AgentApplicationSegmentsBrowserSegmentAllowListInput",
    "AgentApplicationSegmentsSegmentAllowListFilters",
    "AgentApplicationSettingsApmConfigInput",
    "AgentApplicationSettingsApplicationExitInfoInput",
    "AgentApplicationSettingsBrowserAjaxInput",
    "AgentApplicationSettingsBrowserConfigInput",
    "AgentApplicationSettingsBrowserDistributedTracingInput",
    "AgentApplicationSettingsBrowserMonitoringInput",
    "AgentApplicationSettingsBrowserPrivacyInput",
    "AgentApplicationSettingsErrorCollectorInput",
    "AgentApplicationSettingsIgnoredStatusCodeRuleInput",
    "AgentApplicationSettingsJfrInput",
    "AgentApplicationSettingsMaskInputOptionsInput",
    "AgentApplicationSettingsMobileSessionReplayInput",
    "AgentApplicationSettingsMobileSettingsInput",
    "AgentApplicationSettingsNetworkAliasesInput",
    "AgentApplicationSettingsNetworkSettingsInput",
    "AgentApplicationSettingsSessionReplayInput",
    "AgentApplicationSettingsSessionTraceInput",
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
    "AiNotificationsCustomHeaderInput",
    "AiNotificationsCustomHeadersAuthInput",
    "AiNotificationsDestinationFilter",
    "AiNotificationsDestinationInput",
    "AiNotificationsDestinationSorter",
    "AiNotificationsDestinationUpdate",
    "AiNotificationsDynamicVariable",
    "AiNotificationsExampleValue",
    "AiNotificationsOAuth2AuthInput",
    "AiNotificationsPropertyFilter",
    "AiNotificationsPropertyInput",
    "AiNotificationsSecureUrlInput",
    "AiNotificationsSecureUrlUpdate",
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
    "AlertsAsNrqlConditionsSearchCriteriaInput",
    "AlertsEmailNotificationChannelCreateInput",
    "AlertsEmailNotificationChannelUpdateInput",
    "AlertsMutingRuleConditionGroupInput",
    "AlertsMutingRuleConditionInput",
    "AlertsMutingRuleInput",
    "AlertsMutingRuleScheduleInput",
    "AlertsMutingRuleScheduleUpdateInput",
    "AlertsMutingRuleUpdateInput",
    "AlertsMutingRulesFilterCriteriaInput",
    "AlertsNotificationChannelCreateConfiguration",
    "AlertsNotificationChannelUpdateConfiguration",
    "AlertsNrqlConditionBaselineInput",
    "AlertsNrqlConditionExpirationInput",
    "AlertsNrqlConditionOutlierInput",
    "AlertsNrqlConditionPredictionInput",
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
    "AuthorizationManagementEntity",
    "AuthorizationManagementEntityAccessGrants",
    "AuthorizationManagementGrantAccess",
    "AuthorizationManagementGrantee",
    "AuthorizationManagementGroupAccessGrant",
    "AuthorizationManagementOrganizationAccessGrant",
    "AuthorizationManagementRevokeAccess",
    "ChangeTrackingCategoryAndTypeInput",
    "ChangeTrackingCategoryFieldsInput",
    "ChangeTrackingCategoryRelatedInput",
    "ChangeTrackingChangeTrackingSearchFilter",
    "ChangeTrackingCreateEventInput",
    "ChangeTrackingDataHandlingRules",
    "ChangeTrackingDeploymentFieldsInput",
    "ChangeTrackingDeploymentInput",
    "ChangeTrackingEntitySearchInput",
    "ChangeTrackingFeatureFlagFieldsInput",
    "ChangeTrackingSearchFilter",
    "ChangeTrackingTimeWindowInputWithDefaults",
    "CloudAlbIntegrationInput",
    "CloudApigatewayIntegrationInput",
    "CloudAutoscalingIntegrationInput",
    "CloudAwsAppsyncIntegrationInput",
    "CloudAwsAthenaIntegrationInput",
    "CloudAwsAutoDiscoveryIntegrationInput",
    "CloudAwsCognitoIntegrationInput",
    "CloudAwsConnectIntegrationInput",
    "CloudAwsDirectconnectIntegrationInput",
    "CloudAwsDisableIntegrationsInput",
    "CloudAwsDocdbIntegrationInput",
    "CloudAwsFsxIntegrationInput",
    "CloudAwsGlueIntegrationInput",
    "CloudAwsGovCloudLinkAccountInput",
    "CloudAwsGovCloudMigrateToAssumeroleInput",
    "CloudAwsGovCloudUpdateAccountInput",
    "CloudAwsGovcloudDisableIntegrationsInput",
    "CloudAwsGovcloudIntegrationsInput",
    "CloudAwsIntegrationsInput",
    "CloudAwsKinesisanalyticsIntegrationInput",
    "CloudAwsLinkAccountInput",
    "CloudAwsMediaconvertIntegrationInput",
    "CloudAwsMediapackagevodIntegrationInput",
    "CloudAwsMetadataGovIntegrationInput",
    "CloudAwsMetadataIntegrationInput",
    "CloudAwsMqIntegrationInput",
    "CloudAwsMsElasticacheGovIntegrationInput",
    "CloudAwsMsElasticacheIntegrationInput",
    "CloudAwsMskIntegrationInput",
    "CloudAwsNeptuneIntegrationInput",
    "CloudAwsQldbIntegrationInput",
    "CloudAwsRoute53resolverIntegrationInput",
    "CloudAwsStatesIntegrationInput",
    "CloudAwsTagsGlobalGovIntegrationInput",
    "CloudAwsTagsGlobalIntegrationInput",
    "CloudAwsTransitgatewayIntegrationInput",
    "CloudAwsUpdateAccountInput",
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
    "CloudAzureUpdateAccountInput",
    "CloudAzureVirtualmachineIntegrationInput",
    "CloudAzureVirtualnetworksIntegrationInput",
    "CloudAzureVmsIntegrationInput",
    "CloudAzureVpngatewaysIntegrationInput",
    "CloudBillingIntegrationInput",
    "CloudCciAwsDisableIntegrationsInput",
    "CloudCciAwsIntegrationsInput",
    "CloudCciAwsLinkAccountInput",
    "CloudCciAwsS3IntegrationInput",
    "CloudCloudfrontIntegrationInput",
    "CloudCloudtrailIntegrationInput",
    "CloudConfluentDisableIntegrationsInput",
    "CloudConfluentIntegrationsInput",
    "CloudConfluentKafkaConnectorResourceIntegrationInput",
    "CloudConfluentKafkaKsqlResourceIntegrationInput",
    "CloudConfluentKafkaResourceIntegrationInput",
    "CloudConfluentLinkAccountInput",
    "CloudConfluentUpdateAccountInput",
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
    "CloudFossaDisableIntegrationsInput",
    "CloudFossaIntegrationsInput",
    "CloudFossaIssuesIntegrationInput",
    "CloudFossaLinkAccountInput",
    "CloudFossaUpdateAccountInput",
    "CloudGcpAiplatformIntegrationInput",
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
    "CloudGcpUpdateAccountInput",
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
    "CloudSecurityHubIntegrationInput",
    "CloudSesIntegrationInput",
    "CloudSnsIntegrationInput",
    "CloudSqsIntegrationInput",
    "CloudTrustedadvisorIntegrationInput",
    "CloudUnlinkAccountsInput",
    "CloudUpdateCloudAccountsInput",
    "CloudVpcIntegrationInput",
    "CollaborationAssistantConfigInput",
    "CustomRoleContainerInput",
    "DashboardAreaWidgetConfigurationInput",
    "DashboardBarWidgetConfigurationInput",
    "DashboardBillboardWidgetConfigurationInput",
    "DashboardBillboardWidgetThresholdInput",
    "DashboardInput",
    "DashboardLineWidgetConfigurationInput",
    "DashboardLiveUrlAuthCreationInput",
    "DashboardLiveUrlAuthFactorInput",
    "DashboardLiveUrlAuthUpdateInput",
    "DashboardLiveUrlCreationPoliciesFilterInput",
    "DashboardLiveUrlOptionsInput",
    "DashboardLiveUrlsFilterInput",
    "DashboardMarkdownWidgetConfigurationInput",
    "DashboardPageInput",
    "DashboardPieWidgetConfigurationInput",
    "DashboardSnapshotUrlInput",
    "DashboardSnapshotUrlTimeWindowInput",
    "DashboardTableWidgetConfigurationInput",
    "DashboardUpdateLiveUrlCreationPoliciesInput",
    "DashboardUpdatePageInput",
    "DashboardUpdateWidgetInput",
    "DashboardVariableDefaultItemInput",
    "DashboardVariableDefaultValueInput",
    "DashboardVariableEnumItemInput",
    "DashboardVariableInput",
    "DashboardVariableNrqlQueryInput",
    "DashboardVariableOptionsInput",
    "DashboardWidgetConfigurationInput",
    "DashboardWidgetInput",
    "DashboardWidgetLayoutInput",
    "DashboardWidgetNrqlQueryInput",
    "DashboardWidgetVisualizationInput",
    "DataManagementAccountFeatureSettingInput",
    "DataManagementAccountLimitInput",
    "DataManagementFeatureSettingLookup",
    "DataManagementLimitLookupInput",
    "DataManagementRuleInput",
    "DataSourceGapsGapsQuery",
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
    "EntityManagementAiAgentEntityCreateInput",
    "EntityManagementAiAgentEntityUpdateInput",
    "EntityManagementAiAgentToolConfigCreateInput",
    "EntityManagementAiAgentToolConfigUpdateInput",
    "EntityManagementAiToolEntityCreateInput",
    "EntityManagementAiToolEntityUpdateInput",
    "EntityManagementAiToolParameterCreateInput",
    "EntityManagementAiToolParameterUpdateInput",
    "EntityManagementAttributeCreateInput",
    "EntityManagementAttributeUpdateInput",
    "EntityManagementCategoryScopeCreateInput",
    "EntityManagementCategoryScopeUpdateInput",
    "EntityManagementCharacterTextSplitterOptionsCreateInput",
    "EntityManagementCharacterTextSplitterOptionsUpdateInput",
    "EntityManagementCollectionElementsFilter",
    "EntityManagementCollectionEntityCreateInput",
    "EntityManagementCollectionEntityUpdateInput",
    "EntityManagementCollectionIdFilterArgument",
    "EntityManagementConfigCreateInput",
    "EntityManagementConfigUpdateInput",
    "EntityManagementConfluenceIntegrationCreateInput",
    "EntityManagementConfluenceIntegrationUpdateInput",
    "EntityManagementConfluenceRagSettingsEntityCreateInput",
    "EntityManagementConfluenceRagSettingsEntityUpdateInput",
    "EntityManagementDiscoverySettingsUpdateInput",
    "EntityManagementEntityReferenceInput",
    "EntityManagementExternalOwnerCreateInput",
    "EntityManagementExternalOwnerUpdateInput",
    "EntityManagementGenericEntityUpdateInput",
    "EntityManagementGitRepositoryEntityCreateInput",
    "EntityManagementGitRepositoryEntityUpdateInput",
    "EntityManagementInboxIssueCategoryEntityCreateInput",
    "EntityManagementInboxIssueCategoryEntityUpdateInput",
    "EntityManagementLlmConfigCreateInput",
    "EntityManagementLlmConfigUpdateInput",
    "EntityManagementMarkdownTextSplitterOptionsCreateInput",
    "EntityManagementMarkdownTextSplitterOptionsUpdateInput",
    "EntityManagementNrqlRuleEngineCreateInput",
    "EntityManagementNrqlRuleEngineUpdateInput",
    "EntityManagementPerformanceInboxSettingEntityCreateInput",
    "EntityManagementPerformanceInboxSettingEntityUpdateInput",
    "EntityManagementPipelineCloudRuleEntityCreateInput",
    "EntityManagementPipelineCloudRuleEntityUpdateInput",
    "EntityManagementRagToolEntityCreateInput",
    "EntityManagementRagToolEntityUpdateInput",
    "EntityManagementRelationshipCreateInput",
    "EntityManagementRelationshipUpdateInput",
    "EntityManagementRepositoryLicenseCreateInput",
    "EntityManagementRepositoryLicenseUpdateInput",
    "EntityManagementScheduleCreateInput",
    "EntityManagementScheduleUpdateInput",
    "EntityManagementScopedReferenceInput",
    "EntityManagementScorecardEntityCreateInput",
    "EntityManagementScorecardEntityUpdateInput",
    "EntityManagementScorecardRuleEntityCreateInput",
    "EntityManagementScorecardRuleEntityUpdateInput",
    "EntityManagementSyncGroupRuleConditionUpdateInput",
    "EntityManagementSyncGroupRuleUpdateInput",
    "EntityManagementSyncGroupsSettingsUpdateInput",
    "EntityManagementTagInput",
    "EntityManagementTeamEntityCreateInput",
    "EntityManagementTeamEntityUpdateInput",
    "EntityManagementTeamExternalIntegrationCreateInput",
    "EntityManagementTeamExternalIntegrationUpdateInput",
    "EntityManagementTeamResourceCreateInput",
    "EntityManagementTeamResourceUpdateInput",
    "EntityManagementTeamsOrganizationSettingsEntityUpdateInput",
    "EntityManagementTokenTextSplitterOptionsCreateInput",
    "EntityManagementTokenTextSplitterOptionsUpdateInput",
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
    "ErrorsInboxStateVersionInput",
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
    "MachineLearningAddDocumentIndexConfiguration",
    "MachineLearningCharacterTextSplitterOptionsInput",
    "MachineLearningFilterBy",
    "MachineLearningIndexOptions",
    "MachineLearningMarkdownTextSplitterOptionsInput",
    "MachineLearningTokenTextSplitterOptionsInput",
    "MetricNormalizationCreateRuleInput",
    "MetricNormalizationEditRuleInput",
    "MultiTenantAuthorizationGrantAuthenticationDomainIdInputFilter",
    "MultiTenantAuthorizationGrantFilterInputExpression",
    "MultiTenantAuthorizationGrantGroupIdInputFilter",
    "MultiTenantAuthorizationGrantIdInputFilter",
    "MultiTenantAuthorizationGrantOrganizationIdInputFilter",
    "MultiTenantAuthorizationGrantRoleIdInputFilter",
    "MultiTenantAuthorizationGrantScopeIdInputFilter",
    "MultiTenantAuthorizationGrantScopeTypeInputFilter",
    "MultiTenantAuthorizationGrantScopeTypeV2InputFilter",
    "MultiTenantAuthorizationGrantSortInput",
    "MultiTenantAuthorizationGranteeIdInputFilter",
    "MultiTenantAuthorizationGranteeInputFilter",
    "MultiTenantAuthorizationGranteeTypeInputFilter",
    "MultiTenantAuthorizationPermissionFilter",
    "MultiTenantAuthorizationPermissionFilterRoleIdInput",
    "MultiTenantAuthorizationPermissionFilterScopeInput",
    "MultiTenantAuthorizationRoleFilterInputExpression",
    "MultiTenantAuthorizationRoleGroupIdInputFilter",
    "MultiTenantAuthorizationRoleIdInputFilter",
    "MultiTenantAuthorizationRoleNameInputFilter",
    "MultiTenantAuthorizationRoleOrganizationIdInputFilter",
    "MultiTenantAuthorizationRoleScopeInputFilter",
    "MultiTenantAuthorizationRoleScopeV2InputFilter",
    "MultiTenantAuthorizationRoleSortInput",
    "MultiTenantAuthorizationRoleTypeInputFilter",
    "MultiTenantIdentityAllowsCapabilityInput",
    "MultiTenantIdentityAuthenticationDomainIdInput",
    "MultiTenantIdentityEmailVerificationStateInput",
    "MultiTenantIdentityGroupFilterInput",
    "MultiTenantIdentityGroupIdInput",
    "MultiTenantIdentityGroupMemberIdInput",
    "MultiTenantIdentityGroupNameInput",
    "MultiTenantIdentityGroupSortInput",
    "MultiTenantIdentityGroupUserFilterInput",
    "MultiTenantIdentityOrganizationIdInput",
    "MultiTenantIdentityPendingUpgradeRequestInput",
    "MultiTenantIdentityUserEmailInput",
    "MultiTenantIdentityUserFilterInput",
    "MultiTenantIdentityUserGroupIdInput",
    "MultiTenantIdentityUserIdInput",
    "MultiTenantIdentityUserNameInput",
    "MultiTenantIdentityUserNotGroupIdInput",
    "MultiTenantIdentityUserSortInput",
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
    "OrganizationAccountFilterInput",
    "OrganizationAccountIdFilterInput",
    "OrganizationAccountIdInput",
    "OrganizationAccountNameFilterInput",
    "OrganizationAccountOrganizationIdFilterInput",
    "OrganizationAccountShareFilterInput",
    "OrganizationAccountShareSortInput",
    "OrganizationAccountSharingModeFilterInput",
    "OrganizationAccountSortInput",
    "OrganizationAccountStatusFilterInput",
    "OrganizationAuthenticationDomainFilterInput",
    "OrganizationAuthenticationDomainSortInput",
    "OrganizationContractCustomerIdInputFilter",
    "OrganizationContractOrganizationIdInputFilter",
    "OrganizationCreateOrganizationInput",
    "OrganizationCreateSharedAccountInput",
    "OrganizationCustomerContractFilterInput",
    "OrganizationCustomerOrganizationFilterInput",
    "OrganizationIdInput",
    "OrganizationMembersOrganizationMemberAuthenticationDomainIdFilter",
    "OrganizationMembersOrganizationMemberFilter",
    "OrganizationMembersOrganizationMemberOrganizationIdFilter",
    "OrganizationMembersOrganizationMemberSearchFilter",
    "OrganizationMembersOrganizationMemberTypeFilter",
    "OrganizationNameInput",
    "OrganizationNewManagedAccountInput",
    "OrganizationOrganizationAccountIdInputFilter",
    "OrganizationOrganizationAuthenticationDomainIdInputFilter",
    "OrganizationOrganizationCreateAsyncResultFilterInput",
    "OrganizationOrganizationCreateJobCustomerIdInput",
    "OrganizationOrganizationCreateJobIdInput",
    "OrganizationOrganizationCreateJobStatusInput",
    "OrganizationOrganizationCustomerIdInputFilter",
    "OrganizationOrganizationGroupFilterInput",
    "OrganizationOrganizationGroupIdInputFilter",
    "OrganizationOrganizationGroupNameInputFilter",
    "OrganizationOrganizationGroupOrganizationIdInputFilter",
    "OrganizationOrganizationIdInput",
    "OrganizationOrganizationIdInputFilter",
    "OrganizationOrganizationNameInputFilter",
    "OrganizationProvisioningProductInput",
    "OrganizationProvisioningUnitOfMeasureInput",
    "OrganizationRevokeSharedAccountInput",
    "OrganizationSharedAccountInput",
    "OrganizationTargetIdInput",
    "OrganizationUpdateInput",
    "OrganizationUpdateSharedAccountInput",
    "QueryHistoryQueryHistoryOptionsInput",
    "ReferenceEntityCreateRepositoryInput",
    "SecretsManagementBooleanFilter",
    "SecretsManagementScope",
    "SecretsManagementScopeFilter",
    "SecretsManagementSecretsCollectionFilter",
    "SecretsManagementSecretsCollectionSort",
    "SecretsManagementStringFilter",
    "SecretsManagementTagInput",
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
    "SessionsClientTypeFilter",
    "SessionsSessionFilter",
    "SortCriterionWithDirection",
    "StreamingExportAwsInput",
    "StreamingExportAzureInput",
    "StreamingExportGcpInput",
    "StreamingExportRuleInput",
    "SyntheticsCreateBrokenLinksMonitorInput",
    "SyntheticsCreateCertCheckMonitorInput",
    "SyntheticsCreateScriptApiMonitorInput",
    "SyntheticsCreateScriptBrowserMonitorInput",
    "SyntheticsCreateSimpleBrowserMonitorInput",
    "SyntheticsCreateSimpleMonitorInput",
    "SyntheticsCreateStepMonitorInput",
    "SyntheticsCustomHeaderInput",
    "SyntheticsDateWindowEndConfig",
    "SyntheticsDaysOfWeek",
    "SyntheticsDeviceEmulationInput",
    "SyntheticsExtendedTypeMonitorRuntimeInput",
    "SyntheticsLocationsInput",
    "SyntheticsMonitorDowntimeDailyConfig",
    "SyntheticsMonitorDowntimeMonthlyConfig",
    "SyntheticsMonitorDowntimeMonthlyFrequency",
    "SyntheticsMonitorDowntimeOnceConfig",
    "SyntheticsMonitorDowntimeWeeklyConfig",
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
    "SystemIdentityClientIdFilter",
    "SystemIdentityGroupFilter",
    "SystemIdentityGroupIdFilter",
    "SystemIdentityGroupNameFilter",
    "SystemIdentityIdentityFilter",
    "SystemIdentityIdentityIdFilter",
    "SystemIdentityIdentitySort",
    "SystemIdentityIdentitySortField",
    "SystemIdentityNameFilter",
    "SystemIdentityOrganizationIdFilter",
    "TaggingTagInput",
    "TaggingTagValueInput",
    "TimeWindowInput",
    "UserManagementCreateGroup",
    "UserManagementCreateUser",
    "UserManagementDeleteGroup",
    "UserManagementDeleteUser",
    "UserManagementDisplayNameInput",
    "UserManagementEmailInput",
    "UserManagementEmailVerificationStateInput",
    "UserManagementGroupFilterInput",
    "UserManagementGroupIdInput",
    "UserManagementGroupSortInput",
    "UserManagementNameInput",
    "UserManagementPendingUpgradeRequestInput",
    "UserManagementTypeInput",
    "UserManagementUpdateGroup",
    "UserManagementUpdateUser",
    "UserManagementUserFilterInput",
    "UserManagementUserIdInput",
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


# pylint: disable=duplicate-code,unused-import,too-many-lines,disallowed-name


import sgqlc.types
import sgqlc.types.datetime

from newrelic_sb_sdk.graphql.enums import (
    AgentApplicationBrowserLoader,
    AgentApplicationSegmentsListType,
    AgentApplicationSettingsBrowserLoaderInput,
    AgentApplicationSettingsMobileSessionReplayModeInput,
    AgentApplicationSettingsNetworkFilterMode,
    AgentApplicationSettingsRecordSqlEnum,
    AgentApplicationSettingsSessionTraceModeInput,
    AgentApplicationSettingsThresholdTypeEnum,
    AgentApplicationSettingsTracer,
    AiDecisionsIncidentSelect,
    AiDecisionsIssuePriority,
    AiDecisionsRuleSource,
    AiDecisionsRuleType,
    AiDecisionsVertexClass,
    AiIssuesIncidentState,
    AiIssuesIssueMutingState,
    AiIssuesIssueState,
    AiNotificationsAuthType,
    AiNotificationsChannelFields,
    AiNotificationsChannelStatus,
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
    AlertsActionOnMutingRuleWindowEnded,
    AlertsAsNrqlSourceProduct,
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
    AlertsNrqlSignalSeasonality,
    AlertsNrqlStaticConditionValueFunction,
    AlertsOpsGenieDataCenterRegion,
    AlertsSignalAggregationMethod,
    AlertsViolationTimeLimit,
    AlertsWebhookCustomPayloadType,
    ApiAccessIngestKeyType,
    ApiAccessKeyType,
    AuthorizationManagementGranteeTypeEnum,
    ChangeTrackingDeploymentType,
    ChangeTrackingValidationFlag,
    CloudMetricCollectionMode,
    DashboardAlertSeverity,
    DashboardLiveUrlAuthType,
    DashboardLiveUrlType,
    DashboardPermissions,
    DashboardVariableReplacementStrategy,
    DashboardVariableType,
    DataSourceGapsGapTypeIdentifier,
    EdgeComplianceTypeCode,
    EdgeDataSourceGroupUpdateType,
    EdgeProviderRegion,
    EdgeSpanAttributeKeyOperator,
    EdgeSpanAttributeValueOperator,
    EdgeTraceFilterAction,
    EntityAlertSeverity,
    EntityInfrastructureIntegrationType,
    EntityManagementAiToolParameterType,
    EntityManagementCategoryScopeType,
    EntityManagementEncodingName,
    EntityManagementEntityScope,
    EntityManagementExternalOwnerType,
    EntityManagementHostingPlatform,
    EntityManagementIssueType,
    EntityManagementLicenseName,
    EntityManagementSyncGroupRuleConditionType,
    EntityManagementTeamExternalIntegrationType,
    EntityManagementTextSplitterType,
    EntityRelationshipEdgeDirection,
    EntityRelationshipEdgeType,
    EntitySearchQueryBuilderDomain,
    EntitySearchQueryBuilderType,
    EntitySearchSortCriteria,
    EntityType,
    ErrorsInboxDirection,
    ErrorsInboxErrorGroupSortOrderField,
    ErrorsInboxErrorGroupState,
    ErrorsInboxEventSource,
    ErrorsInboxResourceType,
    InstallationInstallStateType,
    InstallationRecipeStatusType,
    LogConfigurationsDataPartitionRuleMatchingOperator,
    LogConfigurationsDataPartitionRuleRetentionPolicyType,
    LogConfigurationsObfuscationMethod,
    MachineLearningEncodingName,
    MachineLearningFilterByKeys,
    MachineLearningOperator,
    MachineLearningTextSplitterType,
    MetricNormalizationCustomerRuleAction,
    MultiTenantAuthorizationGranteeTypeEnum,
    MultiTenantAuthorizationGrantScopeEnum,
    MultiTenantAuthorizationGrantSortEnum,
    MultiTenantAuthorizationRoleScopeEnum,
    MultiTenantAuthorizationRoleSortEnum,
    MultiTenantAuthorizationRoleTypeEnum,
    MultiTenantAuthorizationSortDirectionEnum,
    MultiTenantIdentityCapability,
    MultiTenantIdentitySortDirection,
    MultiTenantIdentitySortKeyEnum,
    MultiTenantIdentityUserSortKey,
    NerdpackSubscriptionModel,
    NerdpackVersionFilterFallback,
    NerdStorageScope,
    NerdStorageVaultActorScope,
    Nr1CatalogSearchComponentType,
    Nr1CatalogSearchResultType,
    NrqlDropRulesAction,
    OrganizationAccountShareSortDirectionEnum,
    OrganizationAccountShareSortKeyEnum,
    OrganizationAccountSortDirectionEnum,
    OrganizationAccountSortKeyEnum,
    OrganizationAccountStatus,
    OrganizationMembersOrganizationMemberType,
    OrganizationOrganizationCreateJobStatusEnum,
    OrganizationProvisioningUnit,
    OrganizationRegionCodeEnum,
    OrganizationSharingMode,
    OrganizationSortDirectionEnum,
    OrganizationSortKeyEnum,
    SecretsManagementScopeType,
    SecretsManagementSortDirection,
    SecretsManagementSortKey,
    ServiceLevelEventsQuerySelectFunction,
    ServiceLevelObjectiveRollingTimeWindowUnit,
    SessionsClientType,
    SortBy,
    StreamingExportPayloadCompression,
    SyntheticsBrowser,
    SyntheticsDevice,
    SyntheticsDeviceOrientation,
    SyntheticsDeviceType,
    SyntheticsMonitorDowntimeDayOfMonthOrdinal,
    SyntheticsMonitorDowntimeWeekDays,
    SyntheticsMonitorPeriod,
    SyntheticsMonitorStatus,
    SyntheticsStepType,
    SystemIdentityIdentitySortFieldKey,
    SystemIdentitySortOrder,
    UserManagementGroupSortKey,
    UserManagementRequestedTierName,
    UserManagementSortDirection,
    UserManagementTypeEnum,
    WhatsNewContentType,
    WorkloadGroupRemainingEntitiesRuleBy,
    WorkloadRollupStrategy,
    WorkloadRuleThresholdType,
    WorkloadStatusValueInput,
)
from newrelic_sb_sdk.graphql.scalars import (
    ID,
    AgentApplicationSettingsCustomJsConfiguration,
    AgentApplicationSettingsErrorCollectorHttpStatus,
    Boolean,
    ChangeTrackingRawCustomAttributesMap,
    DashboardWidgetRawConfiguration,
    Date,
    DateTime,
    EntityGuid,
    EpochMilliseconds,
    EpochSeconds,
    ErrorsInboxRawEvent,
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
    __schema__ = nerdgraph
    __field_names__ = ("name", "organization_id", "region_code")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    organization_id = sgqlc.types.Field(ID, graphql_name="organizationId")

    region_code = sgqlc.types.Field(String, graphql_name="regionCode")


class AccountManagementUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AgentApplicationBrowserSettingsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("cookies_enabled", "distributed_tracing_enabled", "loader_type")
    cookies_enabled = sgqlc.types.Field(Boolean, graphql_name="cookiesEnabled")

    distributed_tracing_enabled = sgqlc.types.Field(
        Boolean, graphql_name="distributedTracingEnabled"
    )

    loader_type = sgqlc.types.Field(
        AgentApplicationBrowserLoader, graphql_name="loaderType"
    )


class AgentApplicationSegmentsBrowserSegmentAllowListInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("segments",)
    segments = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name="segments"
    )


class AgentApplicationSegmentsSegmentAllowListFilters(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("list_type",)
    list_type = sgqlc.types.Field(
        AgentApplicationSegmentsListType, graphql_name="listType"
    )


class AgentApplicationSettingsApmConfigInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("apdex_target", "use_server_side_config")
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    use_server_side_config = sgqlc.types.Field(
        Boolean, graphql_name="useServerSideConfig"
    )


class AgentApplicationSettingsApplicationExitInfoInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsBrowserAjaxInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("deny_list",)
    deny_list = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="denyList"
    )


class AgentApplicationSettingsBrowserConfigInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("apdex_target",)
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class AgentApplicationSettingsBrowserDistributedTracingInput(sgqlc.types.Input):
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

    cors_enabled = sgqlc.types.Field(Boolean, graphql_name="corsEnabled")

    cors_use_newrelic_header = sgqlc.types.Field(
        Boolean, graphql_name="corsUseNewrelicHeader"
    )

    cors_use_tracecontext_headers = sgqlc.types.Field(
        Boolean, graphql_name="corsUseTracecontextHeaders"
    )

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    exclude_newrelic_header = sgqlc.types.Field(
        Boolean, graphql_name="excludeNewrelicHeader"
    )


class AgentApplicationSettingsBrowserMonitoringInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "ajax",
        "distributed_tracing",
        "loader",
        "pinned_version",
        "privacy",
    )
    ajax = sgqlc.types.Field(
        AgentApplicationSettingsBrowserAjaxInput, graphql_name="ajax"
    )

    distributed_tracing = sgqlc.types.Field(
        AgentApplicationSettingsBrowserDistributedTracingInput,
        graphql_name="distributedTracing",
    )

    loader = sgqlc.types.Field(
        AgentApplicationSettingsBrowserLoaderInput, graphql_name="loader"
    )

    pinned_version = sgqlc.types.Field(String, graphql_name="pinnedVersion")

    privacy = sgqlc.types.Field(
        "AgentApplicationSettingsBrowserPrivacyInput", graphql_name="privacy"
    )


class AgentApplicationSettingsBrowserPrivacyInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("cookies_enabled",)
    cookies_enabled = sgqlc.types.Field(Boolean, graphql_name="cookiesEnabled")


class AgentApplicationSettingsErrorCollectorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "enabled",
        "expected_error_classes",
        "expected_error_codes",
        "ignored_error_classes",
        "ignored_error_codes",
    )
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    expected_error_classes = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="expectedErrorClasses",
    )

    expected_error_codes = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AgentApplicationSettingsErrorCollectorHttpStatus)
        ),
        graphql_name="expectedErrorCodes",
    )

    ignored_error_classes = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="ignoredErrorClasses",
    )

    ignored_error_codes = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AgentApplicationSettingsErrorCollectorHttpStatus)
        ),
        graphql_name="ignoredErrorCodes",
    )


class AgentApplicationSettingsIgnoredStatusCodeRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("hosts", "status_codes")
    hosts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="hosts",
    )

    status_codes = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="statusCodes",
    )


class AgentApplicationSettingsJfrInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsMaskInputOptionsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "color",
        "date",
        "datetime_local",
        "email",
        "month",
        "number",
        "range",
        "search",
        "select",
        "tel",
        "text",
        "text_area",
        "time",
        "url",
        "week",
    )
    color = sgqlc.types.Field(Boolean, graphql_name="color")

    date = sgqlc.types.Field(Boolean, graphql_name="date")

    datetime_local = sgqlc.types.Field(Boolean, graphql_name="datetimeLocal")

    email = sgqlc.types.Field(Boolean, graphql_name="email")

    month = sgqlc.types.Field(Boolean, graphql_name="month")

    number = sgqlc.types.Field(Boolean, graphql_name="number")

    range = sgqlc.types.Field(Boolean, graphql_name="range")

    search = sgqlc.types.Field(Boolean, graphql_name="search")

    select = sgqlc.types.Field(Boolean, graphql_name="select")

    tel = sgqlc.types.Field(Boolean, graphql_name="tel")

    text = sgqlc.types.Field(Boolean, graphql_name="text")

    text_area = sgqlc.types.Field(Boolean, graphql_name="textArea")

    time = sgqlc.types.Field(Boolean, graphql_name="time")

    url = sgqlc.types.Field(Boolean, graphql_name="url")

    week = sgqlc.types.Field(Boolean, graphql_name="week")


class AgentApplicationSettingsMobileSessionReplayInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "custom_masking_rules",
        "enabled",
        "error_sampling_rate",
        "mask_all_images",
        "mask_all_user_touches",
        "mask_application_text",
        "mask_user_input_text",
        "mode",
        "sampling_rate",
    )
    custom_masking_rules = sgqlc.types.Field(
        AgentApplicationSettingsCustomJsConfiguration, graphql_name="customMaskingRules"
    )

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    error_sampling_rate = sgqlc.types.Field(Float, graphql_name="errorSamplingRate")

    mask_all_images = sgqlc.types.Field(Boolean, graphql_name="maskAllImages")

    mask_all_user_touches = sgqlc.types.Field(
        Boolean, graphql_name="maskAllUserTouches"
    )

    mask_application_text = sgqlc.types.Field(
        Boolean, graphql_name="maskApplicationText"
    )

    mask_user_input_text = sgqlc.types.Field(Boolean, graphql_name="maskUserInputText")

    mode = sgqlc.types.Field(
        AgentApplicationSettingsMobileSessionReplayModeInput, graphql_name="mode"
    )

    sampling_rate = sgqlc.types.Field(Float, graphql_name="samplingRate")


class AgentApplicationSettingsMobileSettingsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "application_exit_info",
        "mobile_session_replay",
        "network_settings",
        "use_crash_reports",
    )
    application_exit_info = sgqlc.types.Field(
        AgentApplicationSettingsApplicationExitInfoInput,
        graphql_name="applicationExitInfo",
    )

    mobile_session_replay = sgqlc.types.Field(
        AgentApplicationSettingsMobileSessionReplayInput,
        graphql_name="mobileSessionReplay",
    )

    network_settings = sgqlc.types.Field(
        "AgentApplicationSettingsNetworkSettingsInput", graphql_name="networkSettings"
    )

    use_crash_reports = sgqlc.types.Field(Boolean, graphql_name="useCrashReports")


class AgentApplicationSettingsNetworkAliasesInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("alias", "hosts")
    alias = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="alias")

    hosts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="hosts",
    )


class AgentApplicationSettingsNetworkSettingsInput(sgqlc.types.Input):
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

    filter_mode = sgqlc.types.Field(
        AgentApplicationSettingsNetworkFilterMode, graphql_name="filterMode"
    )

    hide_list = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="hideList"
    )

    ignored_status_code_rules = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AgentApplicationSettingsIgnoredStatusCodeRuleInput)
        ),
        graphql_name="ignoredStatusCodeRules",
    )

    show_list = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="showList"
    )


class AgentApplicationSettingsSessionReplayInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "auto_start",
        "block_selector",
        "collect_fonts",
        "enabled",
        "error_sampling_rate",
        "fix_stylesheets",
        "inline_images",
        "inline_stylesheet",
        "mask_all_inputs",
        "mask_input_options",
        "mask_text_selector",
        "preload",
        "sampling_rate",
    )
    auto_start = sgqlc.types.Field(Boolean, graphql_name="autoStart")

    block_selector = sgqlc.types.Field(String, graphql_name="blockSelector")

    collect_fonts = sgqlc.types.Field(Boolean, graphql_name="collectFonts")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    error_sampling_rate = sgqlc.types.Field(Float, graphql_name="errorSamplingRate")

    fix_stylesheets = sgqlc.types.Field(Boolean, graphql_name="fixStylesheets")

    inline_images = sgqlc.types.Field(Boolean, graphql_name="inlineImages")

    inline_stylesheet = sgqlc.types.Field(Boolean, graphql_name="inlineStylesheet")

    mask_all_inputs = sgqlc.types.Field(Boolean, graphql_name="maskAllInputs")

    mask_input_options = sgqlc.types.Field(
        AgentApplicationSettingsMaskInputOptionsInput, graphql_name="maskInputOptions"
    )

    mask_text_selector = sgqlc.types.Field(String, graphql_name="maskTextSelector")

    preload = sgqlc.types.Field(Boolean, graphql_name="preload")

    sampling_rate = sgqlc.types.Field(Float, graphql_name="samplingRate")


class AgentApplicationSettingsSessionTraceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled", "error_sampling_rate", "mode", "sampling_rate")
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    error_sampling_rate = sgqlc.types.Field(Float, graphql_name="errorSamplingRate")

    mode = sgqlc.types.Field(
        AgentApplicationSettingsSessionTraceModeInput, graphql_name="mode"
    )

    sampling_rate = sgqlc.types.Field(Float, graphql_name="samplingRate")


class AgentApplicationSettingsSlowSqlInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsThreadProfilerInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsTracerTypeInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("value",)
    value = sgqlc.types.Field(AgentApplicationSettingsTracer, graphql_name="value")


class AgentApplicationSettingsTransactionTracerInput(sgqlc.types.Input):
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

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    explain_enabled = sgqlc.types.Field(Boolean, graphql_name="explainEnabled")

    explain_threshold_type = sgqlc.types.Field(
        AgentApplicationSettingsThresholdTypeEnum, graphql_name="explainThresholdType"
    )

    explain_threshold_value = sgqlc.types.Field(
        Seconds, graphql_name="explainThresholdValue"
    )

    log_sql = sgqlc.types.Field(Boolean, graphql_name="logSql")

    record_sql = sgqlc.types.Field(
        AgentApplicationSettingsRecordSqlEnum, graphql_name="recordSql"
    )

    stack_trace_threshold = sgqlc.types.Field(
        Seconds, graphql_name="stackTraceThreshold"
    )

    transaction_threshold_type = sgqlc.types.Field(
        AgentApplicationSettingsThresholdTypeEnum,
        graphql_name="transactionThresholdType",
    )

    transaction_threshold_value = sgqlc.types.Field(
        Seconds, graphql_name="transactionThresholdValue"
    )


class AgentApplicationSettingsUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "alias",
        "apm_config",
        "browser_config",
        "browser_monitoring",
        "capture_memcache_keys",
        "error_collector",
        "jfr",
        "mobile_settings",
        "name",
        "session_replay",
        "session_trace",
        "slow_sql",
        "thread_profiler",
        "tracer_type",
        "transaction_tracer",
    )
    alias = sgqlc.types.Field(String, graphql_name="alias")

    apm_config = sgqlc.types.Field(
        AgentApplicationSettingsApmConfigInput, graphql_name="apmConfig"
    )

    browser_config = sgqlc.types.Field(
        AgentApplicationSettingsBrowserConfigInput, graphql_name="browserConfig"
    )

    browser_monitoring = sgqlc.types.Field(
        AgentApplicationSettingsBrowserMonitoringInput, graphql_name="browserMonitoring"
    )

    capture_memcache_keys = sgqlc.types.Field(
        Boolean, graphql_name="captureMemcacheKeys"
    )

    error_collector = sgqlc.types.Field(
        AgentApplicationSettingsErrorCollectorInput, graphql_name="errorCollector"
    )

    jfr = sgqlc.types.Field(AgentApplicationSettingsJfrInput, graphql_name="jfr")

    mobile_settings = sgqlc.types.Field(
        AgentApplicationSettingsMobileSettingsInput, graphql_name="mobileSettings"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    session_replay = sgqlc.types.Field(
        AgentApplicationSettingsSessionReplayInput, graphql_name="sessionReplay"
    )

    session_trace = sgqlc.types.Field(
        AgentApplicationSettingsSessionTraceInput, graphql_name="sessionTrace"
    )

    slow_sql = sgqlc.types.Field(
        AgentApplicationSettingsSlowSqlInput, graphql_name="slowSql"
    )

    thread_profiler = sgqlc.types.Field(
        AgentApplicationSettingsThreadProfilerInput, graphql_name="threadProfiler"
    )

    tracer_type = sgqlc.types.Field(
        AgentApplicationSettingsTracerTypeInput, graphql_name="tracerType"
    )

    transaction_tracer = sgqlc.types.Field(
        AgentApplicationSettingsTransactionTracerInput, graphql_name="transactionTracer"
    )


class AgentEnvironmentFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "does_not_contain", "equals", "starts_with")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    does_not_contain = sgqlc.types.Field(String, graphql_name="doesNotContain")

    equals = sgqlc.types.Field(String, graphql_name="equals")

    starts_with = sgqlc.types.Field(String, graphql_name="startsWith")


class AiDecisionsAllInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("children",)
    children = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiDecisionsRuleExpressionInput"))
        ),
        graphql_name="children",
    )


class AiDecisionsAndInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsRuleExpressionInput"), graphql_name="left"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsRuleExpressionInput"), graphql_name="right"
    )


class AiDecisionsAttributeExistsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident",)
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsCategoricalClusteringInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("threshold",)
    threshold = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="threshold")


class AiDecisionsFixedContainsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("container", "value")
    container = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="container"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedCosineDistanceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="maxDistance"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedEndsWithInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedEqualInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedFuzzyScoreInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    min_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="minDistance"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedFuzzyWuzzyAdaptiveRatioInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_similarity", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    min_similarity = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minSimilarity"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedFuzzyWuzzyPartialRatioInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_similarity", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    min_similarity = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minSimilarity"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedFuzzyWuzzyRatioInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_similarity", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    min_similarity = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minSimilarity"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedFuzzyWuzzyTokenSetRatioInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_similarity", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    min_similarity = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minSimilarity"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedGreaterThanInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")

    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedGreaterThanOrEqualInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")

    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedHammingDistanceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="maxDistance"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedJaccardDistanceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="maxDistance"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedJaroWinklerInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    min_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minDistance"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedLessThanInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")

    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedLessThanOrEqualInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")

    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedLevenshteinInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="maxDistance"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedLongestCommonSubsequenceDistanceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "max_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="maxDistance"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedNumericalEqualInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("compared", "incident")
    compared = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="compared")

    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )


class AiDecisionsFixedRegularExpressionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedSoundExInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "min_distance", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    min_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="minDistance"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsFixedStartsWithInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident", "value")
    incident = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsIncidentObjectInput"), graphql_name="incident"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsIncidentObjectInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attribute", "select")
    attribute = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attribute"
    )

    select = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentSelect), graphql_name="select"
    )


class AiDecisionsNotInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("child",)
    child = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsRuleExpressionInput"), graphql_name="child"
    )


class AiDecisionsOneInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("children",)
    children = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiDecisionsRuleExpressionInput"))
        ),
        graphql_name="children",
    )


class AiDecisionsOrInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsRuleExpressionInput"), graphql_name="left"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsRuleExpressionInput"), graphql_name="right"
    )


class AiDecisionsOverrideConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "priority", "title")
    description = sgqlc.types.Field(String, graphql_name="description")

    priority = sgqlc.types.Field(AiDecisionsIssuePriority, graphql_name="priority")

    title = sgqlc.types.Field(String, graphql_name="title")


class AiDecisionsRelativeCommonPrefixInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("value",)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsRelativeContainsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contained", "container")
    contained = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="contained"
    )

    container = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="container"
    )


class AiDecisionsRelativeCosineDistanceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="maxDistance"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeEndsWithInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contained", "container")
    contained = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="contained"
    )

    container = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="container"
    )


class AiDecisionsRelativeEqualInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeFuzzyScoreInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "min_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    min_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="minDistance"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeFuzzyWuzzyAdaptiveRatioInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "min_similarity", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    min_similarity = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minSimilarity"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeFuzzyWuzzyPartialRatioInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "min_similarity", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    min_similarity = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minSimilarity"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeFuzzyWuzzyRatioInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "min_similarity", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    min_similarity = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minSimilarity"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeFuzzyWuzzyTokenSetRatioInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "min_similarity", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    min_similarity = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minSimilarity"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeGreaterThanInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeGreaterThanOrEqualInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeHammingDistanceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="maxDistance"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeJaccardDistanceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="maxDistance"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeJaroWinklerInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "min_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    min_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="minDistance"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeLessThanInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeLessThanOrEqualInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeLevenshteinInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="maxDistance"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeLongestCommonSubsequenceDistanceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "max_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="maxDistance"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeNumericalEqualInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeRegularExpressionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "right", "value")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiDecisionsRelativeSoundExInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("left", "min_distance", "right")
    left = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="left"
    )

    min_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="minDistance"
    )

    right = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="right"
    )


class AiDecisionsRelativeStartsWithInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contained", "container")
    contained = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="contained"
    )

    container = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsIncidentObjectInput), graphql_name="container"
    )


class AiDecisionsRelativeTopologicallyDependentInput(sgqlc.types.Input):
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

    graph_id = sgqlc.types.Field(ID, graphql_name="graphId")

    max_hops = sgqlc.types.Field(Int, graphql_name="maxHops")

    required_attributes = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="requiredAttributes",
    )

    required_classes = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiDecisionsVertexClass))
        ),
        graphql_name="requiredClasses",
    )

    to = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))),
        graphql_name="to",
    )


class AiDecisionsRuleBlueprint(sgqlc.types.Input):
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

    creator = sgqlc.types.Field(String, graphql_name="creator")

    description = sgqlc.types.Field(String, graphql_name="description")

    min_correlation_threshold = sgqlc.types.Field(
        Int, graphql_name="minCorrelationThreshold"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    override_configuration = sgqlc.types.Field(
        AiDecisionsOverrideConfigurationInput, graphql_name="overrideConfiguration"
    )

    rule_expression = sgqlc.types.Field(
        sgqlc.types.non_null("AiDecisionsRuleExpressionInput"),
        graphql_name="ruleExpression",
    )

    rule_type = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsRuleType), graphql_name="ruleType"
    )

    source = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsRuleSource), graphql_name="source"
    )


class AiDecisionsRuleExpressionInput(sgqlc.types.Input):
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

    and_ = sgqlc.types.Field(AiDecisionsAndInput, graphql_name="and")

    attribute_exists = sgqlc.types.Field(
        AiDecisionsAttributeExistsInput, graphql_name="attributeExists"
    )

    categorical_clustering = sgqlc.types.Field(
        AiDecisionsCategoricalClusteringInput, graphql_name="categoricalClustering"
    )

    fixed_contains = sgqlc.types.Field(
        AiDecisionsFixedContainsInput, graphql_name="fixedContains"
    )

    fixed_cosine_distance = sgqlc.types.Field(
        AiDecisionsFixedCosineDistanceInput, graphql_name="fixedCosineDistance"
    )

    fixed_ends_with = sgqlc.types.Field(
        AiDecisionsFixedEndsWithInput, graphql_name="fixedEndsWith"
    )

    fixed_equal = sgqlc.types.Field(
        AiDecisionsFixedEqualInput, graphql_name="fixedEqual"
    )

    fixed_fuzzy_score = sgqlc.types.Field(
        AiDecisionsFixedFuzzyScoreInput, graphql_name="fixedFuzzyScore"
    )

    fixed_fuzzy_wuzzy_adaptive_ratio = sgqlc.types.Field(
        AiDecisionsFixedFuzzyWuzzyAdaptiveRatioInput,
        graphql_name="fixedFuzzyWuzzyAdaptiveRatio",
    )

    fixed_fuzzy_wuzzy_partial_ratio = sgqlc.types.Field(
        AiDecisionsFixedFuzzyWuzzyPartialRatioInput,
        graphql_name="fixedFuzzyWuzzyPartialRatio",
    )

    fixed_fuzzy_wuzzy_ratio = sgqlc.types.Field(
        AiDecisionsFixedFuzzyWuzzyRatioInput, graphql_name="fixedFuzzyWuzzyRatio"
    )

    fixed_fuzzy_wuzzy_token_set_ratio = sgqlc.types.Field(
        AiDecisionsFixedFuzzyWuzzyTokenSetRatioInput,
        graphql_name="fixedFuzzyWuzzyTokenSetRatio",
    )

    fixed_greater_than = sgqlc.types.Field(
        AiDecisionsFixedGreaterThanInput, graphql_name="fixedGreaterThan"
    )

    fixed_greater_than_or_equal = sgqlc.types.Field(
        AiDecisionsFixedGreaterThanOrEqualInput, graphql_name="fixedGreaterThanOrEqual"
    )

    fixed_hamming_distance = sgqlc.types.Field(
        AiDecisionsFixedHammingDistanceInput, graphql_name="fixedHammingDistance"
    )

    fixed_jaccard_distance = sgqlc.types.Field(
        AiDecisionsFixedJaccardDistanceInput, graphql_name="fixedJaccardDistance"
    )

    fixed_jaro_winkler = sgqlc.types.Field(
        AiDecisionsFixedJaroWinklerInput, graphql_name="fixedJaroWinkler"
    )

    fixed_less_than = sgqlc.types.Field(
        AiDecisionsFixedLessThanInput, graphql_name="fixedLessThan"
    )

    fixed_less_than_or_equal = sgqlc.types.Field(
        AiDecisionsFixedLessThanOrEqualInput, graphql_name="fixedLessThanOrEqual"
    )

    fixed_levenshtein = sgqlc.types.Field(
        AiDecisionsFixedLevenshteinInput, graphql_name="fixedLevenshtein"
    )

    fixed_longest_common_subsequence_distance = sgqlc.types.Field(
        AiDecisionsFixedLongestCommonSubsequenceDistanceInput,
        graphql_name="fixedLongestCommonSubsequenceDistance",
    )

    fixed_numerical_equal = sgqlc.types.Field(
        AiDecisionsFixedNumericalEqualInput, graphql_name="fixedNumericalEqual"
    )

    fixed_regular_expression = sgqlc.types.Field(
        AiDecisionsFixedRegularExpressionInput, graphql_name="fixedRegularExpression"
    )

    fixed_sound_ex = sgqlc.types.Field(
        AiDecisionsFixedSoundExInput, graphql_name="fixedSoundEx"
    )

    fixed_starts_with = sgqlc.types.Field(
        AiDecisionsFixedStartsWithInput, graphql_name="fixedStartsWith"
    )

    not_ = sgqlc.types.Field(AiDecisionsNotInput, graphql_name="not")

    one = sgqlc.types.Field(AiDecisionsOneInput, graphql_name="one")

    or_ = sgqlc.types.Field(AiDecisionsOrInput, graphql_name="or")

    relative_common_prefix = sgqlc.types.Field(
        AiDecisionsRelativeCommonPrefixInput, graphql_name="relativeCommonPrefix"
    )

    relative_contains = sgqlc.types.Field(
        AiDecisionsRelativeContainsInput, graphql_name="relativeContains"
    )

    relative_cosine_distance = sgqlc.types.Field(
        AiDecisionsRelativeCosineDistanceInput, graphql_name="relativeCosineDistance"
    )

    relative_ends_with = sgqlc.types.Field(
        AiDecisionsRelativeEndsWithInput, graphql_name="relativeEndsWith"
    )

    relative_equal = sgqlc.types.Field(
        AiDecisionsRelativeEqualInput, graphql_name="relativeEqual"
    )

    relative_fuzzy_score = sgqlc.types.Field(
        AiDecisionsRelativeFuzzyScoreInput, graphql_name="relativeFuzzyScore"
    )

    relative_fuzzy_wuzzy_adaptive_ratio = sgqlc.types.Field(
        AiDecisionsRelativeFuzzyWuzzyAdaptiveRatioInput,
        graphql_name="relativeFuzzyWuzzyAdaptiveRatio",
    )

    relative_fuzzy_wuzzy_partial_ratio = sgqlc.types.Field(
        AiDecisionsRelativeFuzzyWuzzyPartialRatioInput,
        graphql_name="relativeFuzzyWuzzyPartialRatio",
    )

    relative_fuzzy_wuzzy_ratio = sgqlc.types.Field(
        AiDecisionsRelativeFuzzyWuzzyRatioInput, graphql_name="relativeFuzzyWuzzyRatio"
    )

    relative_fuzzy_wuzzy_token_set_ratio = sgqlc.types.Field(
        AiDecisionsRelativeFuzzyWuzzyTokenSetRatioInput,
        graphql_name="relativeFuzzyWuzzyTokenSetRatio",
    )

    relative_greater_than = sgqlc.types.Field(
        AiDecisionsRelativeGreaterThanInput, graphql_name="relativeGreaterThan"
    )

    relative_greater_than_or_equal = sgqlc.types.Field(
        AiDecisionsRelativeGreaterThanOrEqualInput,
        graphql_name="relativeGreaterThanOrEqual",
    )

    relative_hamming_distance = sgqlc.types.Field(
        AiDecisionsRelativeHammingDistanceInput, graphql_name="relativeHammingDistance"
    )

    relative_jaccard_distance = sgqlc.types.Field(
        AiDecisionsRelativeJaccardDistanceInput, graphql_name="relativeJaccardDistance"
    )

    relative_jaro_winkler = sgqlc.types.Field(
        AiDecisionsRelativeJaroWinklerInput, graphql_name="relativeJaroWinkler"
    )

    relative_less_than = sgqlc.types.Field(
        AiDecisionsRelativeLessThanInput, graphql_name="relativeLessThan"
    )

    relative_less_than_or_equal = sgqlc.types.Field(
        AiDecisionsRelativeLessThanOrEqualInput, graphql_name="relativeLessThanOrEqual"
    )

    relative_levenshtein = sgqlc.types.Field(
        AiDecisionsRelativeLevenshteinInput, graphql_name="relativeLevenshtein"
    )

    relative_longest_common_subsequence_distance = sgqlc.types.Field(
        AiDecisionsRelativeLongestCommonSubsequenceDistanceInput,
        graphql_name="relativeLongestCommonSubsequenceDistance",
    )

    relative_numerical_equal = sgqlc.types.Field(
        AiDecisionsRelativeNumericalEqualInput, graphql_name="relativeNumericalEqual"
    )

    relative_regular_expression = sgqlc.types.Field(
        AiDecisionsRelativeRegularExpressionInput,
        graphql_name="relativeRegularExpression",
    )

    relative_sound_ex = sgqlc.types.Field(
        AiDecisionsRelativeSoundExInput, graphql_name="relativeSoundEx"
    )

    relative_starts_with = sgqlc.types.Field(
        AiDecisionsRelativeStartsWithInput, graphql_name="relativeStartsWith"
    )

    relative_topologically_dependent = sgqlc.types.Field(
        AiDecisionsRelativeTopologicallyDependentInput,
        graphql_name="relativeTopologicallyDependent",
    )

    whole_cosine_distance = sgqlc.types.Field(
        "AiDecisionsWholeCosineDistanceInput", graphql_name="wholeCosineDistance"
    )

    whole_jaccard_similarity = sgqlc.types.Field(
        "AiDecisionsWholeJaccardSimilarityInput", graphql_name="wholeJaccardSimilarity"
    )


class AiDecisionsSearchBlueprint(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("expression", "limit", "retention_window_length")
    expression = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsRuleExpressionInput), graphql_name="expression"
    )

    limit = sgqlc.types.Field(Int, graphql_name="limit")

    retention_window_length = sgqlc.types.Field(
        Milliseconds, graphql_name="retentionWindowLength"
    )


class AiDecisionsSimulationBlueprint(sgqlc.types.Input):
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

    expression = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsRuleExpressionInput), graphql_name="expression"
    )

    min_correlation_threshold = sgqlc.types.Field(
        Int, graphql_name="minCorrelationThreshold"
    )

    retention_window_length = sgqlc.types.Field(
        Milliseconds, graphql_name="retentionWindowLength"
    )


class AiDecisionsSuggestionBlueprint(sgqlc.types.Input):
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

    description = sgqlc.types.Field(String, graphql_name="description")

    hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="hash")

    min_correlation_threshold = sgqlc.types.Field(
        Int, graphql_name="minCorrelationThreshold"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    override_configuration = sgqlc.types.Field(
        AiDecisionsOverrideConfigurationInput, graphql_name="overrideConfiguration"
    )

    rule_expression = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsRuleExpressionInput),
        graphql_name="ruleExpression",
    )

    suggester = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="suggester"
    )

    support = sgqlc.types.Field(String, graphql_name="support")


class AiDecisionsWholeCosineDistanceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("max_distance",)
    max_distance = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="maxDistance"
    )


class AiDecisionsWholeJaccardSimilarityInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("threshold",)
    threshold = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="threshold")


class AiIssuesFilterIncidents(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_types", "ids", "priority", "states")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )

    entity_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="entityTypes"
    )

    ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="ids"
    )

    priority = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="priority"
    )

    states = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AiIssuesIncidentState)),
        graphql_name="states",
    )


class AiIssuesFilterIncidentsEvents(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_types", "ids")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )

    entity_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="entityTypes"
    )

    ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="ids"
    )


class AiIssuesFilterIssues(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "condition_ids",
        "contains",
        "entity_guids",
        "entity_types",
        "ids",
        "is_acknowledged",
        "is_correlated",
        "muting_states",
        "policy_ids",
        "priority",
        "sources",
        "states",
    )
    condition_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="conditionIds"
    )

    contains = sgqlc.types.Field(String, graphql_name="contains")

    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )

    entity_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="entityTypes"
    )

    ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="ids"
    )

    is_acknowledged = sgqlc.types.Field(Boolean, graphql_name="isAcknowledged")

    is_correlated = sgqlc.types.Field(Boolean, graphql_name="isCorrelated")

    muting_states = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AiIssuesIssueMutingState)),
        graphql_name="mutingStates",
    )

    policy_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="policyIds"
    )

    priority = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="priority"
    )

    sources = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="sources"
    )

    states = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AiIssuesIssueState)),
        graphql_name="states",
    )


class AiIssuesFilterIssuesEvents(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_types", "ids")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )

    entity_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="entityTypes"
    )

    ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="ids"
    )


class AiIssuesGracePeriodConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("critical", "high", "low", "medium")
    critical = sgqlc.types.Field(sgqlc.types.non_null(Seconds), graphql_name="critical")

    high = sgqlc.types.Field(sgqlc.types.non_null(Seconds), graphql_name="high")

    low = sgqlc.types.Field(sgqlc.types.non_null(Seconds), graphql_name="low")

    medium = sgqlc.types.Field(sgqlc.types.non_null(Seconds), graphql_name="medium")


class AiNotificationsBasicAuthInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("password", "user")
    password = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="password"
    )

    user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="user")


class AiNotificationsChannelFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "active",
        "destination_id",
        "id",
        "ids",
        "name",
        "product",
        "property",
        "statuses",
        "type",
    )
    active = sgqlc.types.Field(Boolean, graphql_name="active")

    destination_id = sgqlc.types.Field(ID, graphql_name="destinationId")

    id = sgqlc.types.Field(ID, graphql_name="id")

    ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="ids"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    product = sgqlc.types.Field(AiNotificationsProduct, graphql_name="product")

    property = sgqlc.types.Field(
        "AiNotificationsPropertyFilter", graphql_name="property"
    )

    statuses = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AiNotificationsChannelStatus)),
        graphql_name="statuses",
    )

    type = sgqlc.types.Field(AiNotificationsChannelType, graphql_name="type")


class AiNotificationsChannelInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("destination_id", "name", "product", "properties", "type")
    destination_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="destinationId"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    product = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsProduct), graphql_name="product"
    )

    properties = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiNotificationsPropertyInput"))
        ),
        graphql_name="properties",
    )

    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsChannelType), graphql_name="type"
    )


class AiNotificationsChannelSorter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "field")
    direction = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsSortOrder), graphql_name="direction"
    )

    field = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsChannelFields), graphql_name="field"
    )


class AiNotificationsChannelUpdate(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("active", "name", "properties")
    active = sgqlc.types.Field(Boolean, graphql_name="active")

    name = sgqlc.types.Field(String, graphql_name="name")

    properties = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("AiNotificationsPropertyInput")),
        graphql_name="properties",
    )


class AiNotificationsConstraint(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiNotificationsCredentialsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("basic", "custom_headers", "oauth2", "token", "type")
    basic = sgqlc.types.Field(AiNotificationsBasicAuthInput, graphql_name="basic")

    custom_headers = sgqlc.types.Field(
        "AiNotificationsCustomHeadersAuthInput", graphql_name="customHeaders"
    )

    oauth2 = sgqlc.types.Field("AiNotificationsOAuth2AuthInput", graphql_name="oauth2")

    token = sgqlc.types.Field("AiNotificationsTokenAuthInput", graphql_name="token")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsAuthType), graphql_name="type"
    )


class AiNotificationsCustomHeaderInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(SecureValue, graphql_name="value")


class AiNotificationsCustomHeadersAuthInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("custom_headers",)
    custom_headers = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiNotificationsCustomHeaderInput))
        ),
        graphql_name="customHeaders",
    )


class AiNotificationsDestinationFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "active",
        "auth_type",
        "exact_name",
        "id",
        "ids",
        "name",
        "property",
        "type",
        "updated_at",
    )
    active = sgqlc.types.Field(Boolean, graphql_name="active")

    auth_type = sgqlc.types.Field(AiNotificationsAuthType, graphql_name="authType")

    exact_name = sgqlc.types.Field(String, graphql_name="exactName")

    id = sgqlc.types.Field(ID, graphql_name="id")

    ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="ids"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    property = sgqlc.types.Field(
        "AiNotificationsPropertyFilter", graphql_name="property"
    )

    type = sgqlc.types.Field(AiNotificationsDestinationType, graphql_name="type")

    updated_at = sgqlc.types.Field(DateTime, graphql_name="updatedAt")


class AiNotificationsDestinationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("auth", "name", "properties", "secure_url", "type")
    auth = sgqlc.types.Field(AiNotificationsCredentialsInput, graphql_name="auth")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    properties = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiNotificationsPropertyInput"))
        ),
        graphql_name="properties",
    )

    secure_url = sgqlc.types.Field(
        "AiNotificationsSecureUrlInput", graphql_name="secureUrl"
    )

    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsDestinationType), graphql_name="type"
    )


class AiNotificationsDestinationSorter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "field")
    direction = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsSortOrder), graphql_name="direction"
    )

    field = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsDestinationFields), graphql_name="field"
    )


class AiNotificationsDestinationUpdate(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "active",
        "auth",
        "disable_auth",
        "name",
        "properties",
        "secure_url",
    )
    active = sgqlc.types.Field(Boolean, graphql_name="active")

    auth = sgqlc.types.Field(AiNotificationsCredentialsInput, graphql_name="auth")

    disable_auth = sgqlc.types.Field(Boolean, graphql_name="disableAuth")

    name = sgqlc.types.Field(String, graphql_name="name")

    properties = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("AiNotificationsPropertyInput")),
        graphql_name="properties",
    )

    secure_url = sgqlc.types.Field(
        "AiNotificationsSecureUrlUpdate", graphql_name="secureUrl"
    )


class AiNotificationsDynamicVariable(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("example_value", "name")
    example_value = sgqlc.types.Field(
        "AiNotificationsExampleValue", graphql_name="exampleValue"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AiNotificationsExampleValue(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("example", "type")
    example = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="example")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsVariableType), graphql_name="type"
    )


class AiNotificationsOAuth2AuthInput(sgqlc.types.Input):
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

    authorization_url = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="authorizationUrl"
    )

    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="clientId")

    client_secret = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="clientSecret"
    )

    prefix = sgqlc.types.Field(String, graphql_name="prefix")

    refresh_interval = sgqlc.types.Field(Int, graphql_name="refreshInterval")

    refresh_token = sgqlc.types.Field(SecureValue, graphql_name="refreshToken")

    refreshable = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="refreshable"
    )

    scope = sgqlc.types.Field(String, graphql_name="scope")

    token = sgqlc.types.Field(sgqlc.types.non_null(SecureValue), graphql_name="token")


class AiNotificationsPropertyFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiNotificationsPropertyInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("display_value", "key", "label", "value")
    display_value = sgqlc.types.Field(String, graphql_name="displayValue")

    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    label = sgqlc.types.Field(String, graphql_name="label")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiNotificationsSecureUrlInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("prefix", "secure_suffix")
    prefix = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="prefix")

    secure_suffix = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="secureSuffix"
    )


class AiNotificationsSecureUrlUpdate(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("prefix", "secure_suffix")
    prefix = sgqlc.types.Field(String, graphql_name="prefix")

    secure_suffix = sgqlc.types.Field(SecureValue, graphql_name="secureSuffix")


class AiNotificationsSuggestionFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("type", "value")
    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsSuggestionFilterType), graphql_name="type"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiNotificationsTokenAuthInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("prefix", "token")
    prefix = sgqlc.types.Field(String, graphql_name="prefix")

    token = sgqlc.types.Field(sgqlc.types.non_null(SecureValue), graphql_name="token")


class AiNotificationsVariableFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("active", "key", "label", "name", "product")
    active = sgqlc.types.Field(Boolean, graphql_name="active")

    key = sgqlc.types.Field(String, graphql_name="key")

    label = sgqlc.types.Field(String, graphql_name="label")

    name = sgqlc.types.Field(String, graphql_name="name")

    product = sgqlc.types.Field(AiNotificationsProduct, graphql_name="product")


class AiNotificationsVariableSorter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "field")
    direction = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsSortOrder), graphql_name="direction"
    )

    field = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsVariableFields), graphql_name="field"
    )


class AiTopologyCollectorAttributeInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class AiTopologyCollectorEdgeBlueprint(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("directed", "from_vertex_name", "to_vertex_name")
    directed = sgqlc.types.Field(Boolean, graphql_name="directed")

    from_vertex_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="fromVertexName"
    )

    to_vertex_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="toVertexName"
    )


class AiTopologyCollectorVertexBlueprint(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("defining_attributes", "name", "vertex_class")
    defining_attributes = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiTopologyCollectorAttributeInput))
        ),
        graphql_name="definingAttributes",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    vertex_class = sgqlc.types.Field(
        sgqlc.types.non_null(AiTopologyCollectorVertexClass), graphql_name="vertexClass"
    )


class AiWorkflowsCreateWorkflowInput(sgqlc.types.Input):
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

    destinations_enabled = sgqlc.types.Field(
        Boolean, graphql_name="destinationsEnabled"
    )

    enrichments = sgqlc.types.Field(
        "AiWorkflowsEnrichmentsInput", graphql_name="enrichments"
    )

    enrichments_enabled = sgqlc.types.Field(Boolean, graphql_name="enrichmentsEnabled")

    issues_filter = sgqlc.types.Field(
        "AiWorkflowsFilterInput", graphql_name="issuesFilter"
    )

    muting_rules_handling = sgqlc.types.Field(
        sgqlc.types.non_null(AiWorkflowsMutingRulesHandling),
        graphql_name="mutingRulesHandling",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    workflow_enabled = sgqlc.types.Field(Boolean, graphql_name="workflowEnabled")


class AiWorkflowsDestinationConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("channel_id", "notification_triggers", "update_original_message")
    channel_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="channelId")

    notification_triggers = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AiWorkflowsNotificationTrigger)),
        graphql_name="notificationTriggers",
    )

    update_original_message = sgqlc.types.Field(
        Boolean, graphql_name="updateOriginalMessage"
    )


class AiWorkflowsEnrichmentsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("nrql",)
    nrql = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiWorkflowsNrqlEnrichmentInput"))
        ),
        graphql_name="nrql",
    )


class AiWorkflowsFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "predicates", "type")
    name = sgqlc.types.Field(String, graphql_name="name")

    predicates = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiWorkflowsPredicateInput"))
        ),
        graphql_name="predicates",
    )

    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiWorkflowsFilterType), graphql_name="type"
    )


class AiWorkflowsFilters(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "channel_id",
        "destination_type",
        "enrichment_id",
        "filter_id",
        "guid",
        "id",
        "name",
        "name_like",
        "workflow_enabled",
    )
    channel_id = sgqlc.types.Field(ID, graphql_name="channelId")

    destination_type = sgqlc.types.Field(
        AiWorkflowsDestinationType, graphql_name="destinationType"
    )

    enrichment_id = sgqlc.types.Field(ID, graphql_name="enrichmentId")

    filter_id = sgqlc.types.Field(ID, graphql_name="filterId")

    guid = sgqlc.types.Field(EntityGuid, graphql_name="guid")

    id = sgqlc.types.Field(ID, graphql_name="id")

    name = sgqlc.types.Field(String, graphql_name="name")

    name_like = sgqlc.types.Field(String, graphql_name="nameLike")

    workflow_enabled = sgqlc.types.Field(Boolean, graphql_name="workflowEnabled")


class AiWorkflowsNrqlConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("query",)
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="query")


class AiWorkflowsNrqlEnrichmentInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("configuration", "name")
    configuration = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiWorkflowsNrqlConfigurationInput))
        ),
        graphql_name="configuration",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AiWorkflowsNrqlTestEnrichmentInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("configuration", "id", "name")
    configuration = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiWorkflowsNrqlConfigurationInput))
        ),
        graphql_name="configuration",
    )

    id = sgqlc.types.Field(ID, graphql_name="id")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AiWorkflowsNrqlUpdateEnrichmentInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("configuration", "id", "name")
    configuration = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiWorkflowsNrqlConfigurationInput))
        ),
        graphql_name="configuration",
    )

    id = sgqlc.types.Field(ID, graphql_name="id")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AiWorkflowsPredicateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attribute", "operator", "values")
    attribute = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attribute"
    )

    operator = sgqlc.types.Field(
        sgqlc.types.non_null(AiWorkflowsOperator), graphql_name="operator"
    )

    values = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="values",
    )


class AiWorkflowsTestEnrichmentsInput(sgqlc.types.Input):
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

    enrichments = sgqlc.types.Field(
        AiWorkflowsTestEnrichmentsInput, graphql_name="enrichments"
    )

    issues_filter = sgqlc.types.Field(
        AiWorkflowsFilterInput, graphql_name="issuesFilter"
    )


class AiWorkflowsUpdateEnrichmentsInput(sgqlc.types.Input):
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

    destinations_enabled = sgqlc.types.Field(
        Boolean, graphql_name="destinationsEnabled"
    )

    enrichments = sgqlc.types.Field(
        AiWorkflowsUpdateEnrichmentsInput, graphql_name="enrichments"
    )

    enrichments_enabled = sgqlc.types.Field(Boolean, graphql_name="enrichmentsEnabled")

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    issues_filter = sgqlc.types.Field(
        "AiWorkflowsUpdatedFilterInput", graphql_name="issuesFilter"
    )

    muting_rules_handling = sgqlc.types.Field(
        AiWorkflowsMutingRulesHandling, graphql_name="mutingRulesHandling"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    workflow_enabled = sgqlc.types.Field(Boolean, graphql_name="workflowEnabled")


class AiWorkflowsUpdatedFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("filter_input", "id")
    filter_input = sgqlc.types.Field(
        sgqlc.types.non_null(AiWorkflowsFilterInput), graphql_name="filterInput"
    )

    id = sgqlc.types.Field(ID, graphql_name="id")


class AlertsAsNrqlConditionsSearchCriteriaInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "name",
        "name_like",
        "policy_id",
        "source_product",
        "terms_operator",
    )
    name = sgqlc.types.Field(String, graphql_name="name")

    name_like = sgqlc.types.Field(String, graphql_name="nameLike")

    policy_id = sgqlc.types.Field(ID, graphql_name="policyId")

    source_product = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AlertsAsNrqlSourceProduct)),
        graphql_name="sourceProduct",
    )

    terms_operator = sgqlc.types.Field(
        AlertsNrqlConditionTermsOperator, graphql_name="termsOperator"
    )


class AlertsEmailNotificationChannelCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("emails", "include_json", "name")
    emails = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="emails",
    )

    include_json = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="includeJson"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AlertsEmailNotificationChannelUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("emails", "include_json", "name")
    emails = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="emails"
    )

    include_json = sgqlc.types.Field(Boolean, graphql_name="includeJson")

    name = sgqlc.types.Field(String, graphql_name="name")


class AlertsMutingRuleConditionGroupInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("conditions", "operator")
    conditions = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AlertsMutingRuleConditionInput"))
        ),
        graphql_name="conditions",
    )

    operator = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsMutingRuleConditionGroupOperator),
        graphql_name="operator",
    )


class AlertsMutingRuleConditionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attribute", "operator", "values")
    attribute = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attribute"
    )

    operator = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsMutingRuleConditionOperator), graphql_name="operator"
    )

    values = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name="values"
    )


class AlertsMutingRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "action_on_muting_rule_window_ended",
        "condition",
        "description",
        "enabled",
        "name",
        "schedule",
    )
    action_on_muting_rule_window_ended = sgqlc.types.Field(
        AlertsActionOnMutingRuleWindowEnded,
        graphql_name="actionOnMutingRuleWindowEnded",
    )

    condition = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsMutingRuleConditionGroupInput),
        graphql_name="condition",
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    schedule = sgqlc.types.Field(
        "AlertsMutingRuleScheduleInput", graphql_name="schedule"
    )


class AlertsMutingRuleScheduleInput(sgqlc.types.Input):
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

    end_time = sgqlc.types.Field(NaiveDateTime, graphql_name="endTime")

    repeat = sgqlc.types.Field(AlertsMutingRuleScheduleRepeat, graphql_name="repeat")

    repeat_count = sgqlc.types.Field(Int, graphql_name="repeatCount")

    start_time = sgqlc.types.Field(NaiveDateTime, graphql_name="startTime")

    time_zone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="timeZone")

    weekly_repeat_days = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AlertsDayOfWeek)),
        graphql_name="weeklyRepeatDays",
    )


class AlertsMutingRuleScheduleUpdateInput(sgqlc.types.Input):
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

    end_time = sgqlc.types.Field(NaiveDateTime, graphql_name="endTime")

    repeat = sgqlc.types.Field(AlertsMutingRuleScheduleRepeat, graphql_name="repeat")

    repeat_count = sgqlc.types.Field(Int, graphql_name="repeatCount")

    start_time = sgqlc.types.Field(NaiveDateTime, graphql_name="startTime")

    time_zone = sgqlc.types.Field(String, graphql_name="timeZone")

    weekly_repeat_days = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AlertsDayOfWeek)),
        graphql_name="weeklyRepeatDays",
    )


class AlertsMutingRuleUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "action_on_muting_rule_window_ended",
        "condition",
        "description",
        "enabled",
        "name",
        "schedule",
    )
    action_on_muting_rule_window_ended = sgqlc.types.Field(
        AlertsActionOnMutingRuleWindowEnded,
        graphql_name="actionOnMutingRuleWindowEnded",
    )

    condition = sgqlc.types.Field(
        AlertsMutingRuleConditionGroupInput, graphql_name="condition"
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    name = sgqlc.types.Field(String, graphql_name="name")

    schedule = sgqlc.types.Field(
        AlertsMutingRuleScheduleUpdateInput, graphql_name="schedule"
    )


class AlertsMutingRulesFilterCriteriaInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AlertsNotificationChannelCreateConfiguration(sgqlc.types.Input):
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

    ops_genie = sgqlc.types.Field(
        "AlertsOpsGenieNotificationChannelCreateInput", graphql_name="opsGenie"
    )

    pager_duty = sgqlc.types.Field(
        "AlertsPagerDutyNotificationChannelCreateInput", graphql_name="pagerDuty"
    )

    slack = sgqlc.types.Field(
        "AlertsSlackNotificationChannelCreateInput", graphql_name="slack"
    )

    victor_ops = sgqlc.types.Field(
        "AlertsVictorOpsNotificationChannelCreateInput", graphql_name="victorOps"
    )

    webhook = sgqlc.types.Field(
        "AlertsWebhookNotificationChannelCreateInput", graphql_name="webhook"
    )

    x_matters = sgqlc.types.Field(
        "AlertsXMattersNotificationChannelCreateInput", graphql_name="xMatters"
    )


class AlertsNotificationChannelUpdateConfiguration(sgqlc.types.Input):
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

    ops_genie = sgqlc.types.Field(
        "AlertsOpsGenieNotificationChannelUpdateInput", graphql_name="opsGenie"
    )

    pager_duty = sgqlc.types.Field(
        "AlertsPagerDutyNotificationChannelUpdateInput", graphql_name="pagerDuty"
    )

    slack = sgqlc.types.Field(
        "AlertsSlackNotificationChannelUpdateInput", graphql_name="slack"
    )

    victor_ops = sgqlc.types.Field(
        "AlertsVictorOpsNotificationChannelUpdateInput", graphql_name="victorOps"
    )

    webhook = sgqlc.types.Field(
        "AlertsWebhookNotificationChannelUpdateInput", graphql_name="webhook"
    )

    x_matters = sgqlc.types.Field(
        "AlertsXMattersNotificationChannelUpdateInput", graphql_name="xMatters"
    )


class AlertsNrqlConditionBaselineInput(sgqlc.types.Input):
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
        "signal_seasonality",
        "terms",
        "title_template",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    baseline_direction = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlBaselineDirection),
        graphql_name="baselineDirection",
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    expiration = sgqlc.types.Field(
        "AlertsNrqlConditionExpirationInput", graphql_name="expiration"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    nrql = sgqlc.types.Field(
        sgqlc.types.non_null("AlertsNrqlConditionQueryInput"), graphql_name="nrql"
    )

    runbook_url = sgqlc.types.Field(String, graphql_name="runbookUrl")

    signal = sgqlc.types.Field("AlertsNrqlConditionSignalInput", graphql_name="signal")

    signal_seasonality = sgqlc.types.Field(
        AlertsNrqlSignalSeasonality, graphql_name="signalSeasonality"
    )

    terms = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("AlertsNrqlDynamicConditionTermsInput")
        ),
        graphql_name="terms",
    )

    title_template = sgqlc.types.Field(String, graphql_name="titleTemplate")

    violation_time_limit = sgqlc.types.Field(
        AlertsViolationTimeLimit, graphql_name="violationTimeLimit"
    )

    violation_time_limit_seconds = sgqlc.types.Field(
        Seconds, graphql_name="violationTimeLimitSeconds"
    )


class AlertsNrqlConditionExpirationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "close_violations_on_expiration",
        "expiration_duration",
        "ignore_on_expected_termination",
        "open_violation_on_expiration",
    )
    close_violations_on_expiration = sgqlc.types.Field(
        Boolean, graphql_name="closeViolationsOnExpiration"
    )

    expiration_duration = sgqlc.types.Field(Seconds, graphql_name="expirationDuration")

    ignore_on_expected_termination = sgqlc.types.Field(
        Boolean, graphql_name="ignoreOnExpectedTermination"
    )

    open_violation_on_expiration = sgqlc.types.Field(
        Boolean, graphql_name="openViolationOnExpiration"
    )


class AlertsNrqlConditionOutlierInput(sgqlc.types.Input):
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
        "title_template",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    expiration = sgqlc.types.Field(
        AlertsNrqlConditionExpirationInput, graphql_name="expiration"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    nrql = sgqlc.types.Field(
        sgqlc.types.non_null("AlertsNrqlConditionQueryInput"), graphql_name="nrql"
    )

    runbook_url = sgqlc.types.Field(String, graphql_name="runbookUrl")

    signal = sgqlc.types.Field("AlertsNrqlConditionSignalInput", graphql_name="signal")

    terms = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null("AlertsNrqlDynamicConditionTermsInput")
            )
        ),
        graphql_name="terms",
    )

    title_template = sgqlc.types.Field(String, graphql_name="titleTemplate")

    violation_time_limit = sgqlc.types.Field(
        AlertsViolationTimeLimit, graphql_name="violationTimeLimit"
    )

    violation_time_limit_seconds = sgqlc.types.Field(
        Seconds, graphql_name="violationTimeLimitSeconds"
    )


class AlertsNrqlConditionPredictionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("predict_by", "prefer_prediction_violation")
    predict_by = sgqlc.types.Field(Seconds, graphql_name="predictBy")

    prefer_prediction_violation = sgqlc.types.Field(
        Boolean, graphql_name="preferPredictionViolation"
    )


class AlertsNrqlConditionQueryInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("data_account_id", "evaluation_offset", "query")
    data_account_id = sgqlc.types.Field(Int, graphql_name="dataAccountId")

    evaluation_offset = sgqlc.types.Field(Int, graphql_name="evaluationOffset")

    query = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="query")


class AlertsNrqlConditionSignalInput(sgqlc.types.Input):
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

    aggregation_method = sgqlc.types.Field(
        AlertsSignalAggregationMethod, graphql_name="aggregationMethod"
    )

    aggregation_timer = sgqlc.types.Field(Seconds, graphql_name="aggregationTimer")

    aggregation_window = sgqlc.types.Field(Seconds, graphql_name="aggregationWindow")

    evaluation_delay = sgqlc.types.Field(Seconds, graphql_name="evaluationDelay")

    evaluation_offset = sgqlc.types.Field(Int, graphql_name="evaluationOffset")

    fill_option = sgqlc.types.Field(AlertsFillOption, graphql_name="fillOption")

    fill_value = sgqlc.types.Field(Float, graphql_name="fillValue")

    slide_by = sgqlc.types.Field(Seconds, graphql_name="slideBy")


class AlertsNrqlConditionStaticInput(sgqlc.types.Input):
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
        "title_template",
        "value_function",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    expiration = sgqlc.types.Field(
        AlertsNrqlConditionExpirationInput, graphql_name="expiration"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    nrql = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlConditionQueryInput), graphql_name="nrql"
    )

    runbook_url = sgqlc.types.Field(String, graphql_name="runbookUrl")

    signal = sgqlc.types.Field(AlertsNrqlConditionSignalInput, graphql_name="signal")

    terms = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("AlertsNrqlConditionTermsInput")),
        graphql_name="terms",
    )

    title_template = sgqlc.types.Field(String, graphql_name="titleTemplate")

    value_function = sgqlc.types.Field(
        AlertsNrqlStaticConditionValueFunction, graphql_name="valueFunction"
    )

    violation_time_limit = sgqlc.types.Field(
        AlertsViolationTimeLimit, graphql_name="violationTimeLimit"
    )

    violation_time_limit_seconds = sgqlc.types.Field(
        Seconds, graphql_name="violationTimeLimitSeconds"
    )


class AlertsNrqlConditionTermsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "disable_health_status_reporting",
        "operator",
        "prediction",
        "priority",
        "threshold",
        "threshold_duration",
        "threshold_occurrences",
    )
    disable_health_status_reporting = sgqlc.types.Field(
        Boolean, graphql_name="disableHealthStatusReporting"
    )

    operator = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlConditionTermsOperator), graphql_name="operator"
    )

    prediction = sgqlc.types.Field(
        AlertsNrqlConditionPredictionInput, graphql_name="prediction"
    )

    priority = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlConditionPriority), graphql_name="priority"
    )

    threshold = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="threshold")

    threshold_duration = sgqlc.types.Field(
        sgqlc.types.non_null(Seconds), graphql_name="thresholdDuration"
    )

    threshold_occurrences = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlConditionThresholdOccurrences),
        graphql_name="thresholdOccurrences",
    )


class AlertsNrqlConditionUpdateBaselineInput(sgqlc.types.Input):
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
        "signal_seasonality",
        "terms",
        "title_template",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    baseline_direction = sgqlc.types.Field(
        AlertsNrqlBaselineDirection, graphql_name="baselineDirection"
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    expiration = sgqlc.types.Field(
        AlertsNrqlConditionExpirationInput, graphql_name="expiration"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    nrql = sgqlc.types.Field("AlertsNrqlConditionUpdateQueryInput", graphql_name="nrql")

    runbook_url = sgqlc.types.Field(String, graphql_name="runbookUrl")

    signal = sgqlc.types.Field(AlertsNrqlConditionSignalInput, graphql_name="signal")

    signal_seasonality = sgqlc.types.Field(
        AlertsNrqlSignalSeasonality, graphql_name="signalSeasonality"
    )

    terms = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("AlertsNrqlDynamicConditionTermsInput")
        ),
        graphql_name="terms",
    )

    title_template = sgqlc.types.Field(String, graphql_name="titleTemplate")

    violation_time_limit = sgqlc.types.Field(
        AlertsViolationTimeLimit, graphql_name="violationTimeLimit"
    )

    violation_time_limit_seconds = sgqlc.types.Field(
        Seconds, graphql_name="violationTimeLimitSeconds"
    )


class AlertsNrqlConditionUpdateOutlierInput(sgqlc.types.Input):
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
        "title_template",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    expiration = sgqlc.types.Field(
        AlertsNrqlConditionExpirationInput, graphql_name="expiration"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    nrql = sgqlc.types.Field("AlertsNrqlConditionUpdateQueryInput", graphql_name="nrql")

    runbook_url = sgqlc.types.Field(String, graphql_name="runbookUrl")

    signal = sgqlc.types.Field(AlertsNrqlConditionSignalInput, graphql_name="signal")

    terms = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("AlertsNrqlDynamicConditionTermsInput")
        ),
        graphql_name="terms",
    )

    title_template = sgqlc.types.Field(String, graphql_name="titleTemplate")

    violation_time_limit = sgqlc.types.Field(
        AlertsViolationTimeLimit, graphql_name="violationTimeLimit"
    )

    violation_time_limit_seconds = sgqlc.types.Field(
        Seconds, graphql_name="violationTimeLimitSeconds"
    )


class AlertsNrqlConditionUpdateQueryInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("data_account_id", "evaluation_offset", "query")
    data_account_id = sgqlc.types.Field(Int, graphql_name="dataAccountId")

    evaluation_offset = sgqlc.types.Field(Int, graphql_name="evaluationOffset")

    query = sgqlc.types.Field(String, graphql_name="query")


class AlertsNrqlConditionUpdateStaticInput(sgqlc.types.Input):
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
        "title_template",
        "value_function",
        "violation_time_limit",
        "violation_time_limit_seconds",
    )
    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    expiration = sgqlc.types.Field(
        AlertsNrqlConditionExpirationInput, graphql_name="expiration"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    nrql = sgqlc.types.Field(AlertsNrqlConditionUpdateQueryInput, graphql_name="nrql")

    runbook_url = sgqlc.types.Field(String, graphql_name="runbookUrl")

    signal = sgqlc.types.Field(AlertsNrqlConditionSignalInput, graphql_name="signal")

    terms = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AlertsNrqlConditionTermsInput)),
        graphql_name="terms",
    )

    title_template = sgqlc.types.Field(String, graphql_name="titleTemplate")

    value_function = sgqlc.types.Field(
        AlertsNrqlStaticConditionValueFunction, graphql_name="valueFunction"
    )

    violation_time_limit = sgqlc.types.Field(
        AlertsViolationTimeLimit, graphql_name="violationTimeLimit"
    )

    violation_time_limit_seconds = sgqlc.types.Field(
        Seconds, graphql_name="violationTimeLimitSeconds"
    )


class AlertsNrqlConditionsSearchCriteriaInput(sgqlc.types.Input):
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

    name_like = sgqlc.types.Field(String, graphql_name="nameLike")

    policy_id = sgqlc.types.Field(ID, graphql_name="policyId")

    query = sgqlc.types.Field(String, graphql_name="query")

    query_like = sgqlc.types.Field(String, graphql_name="queryLike")

    terms_operator = sgqlc.types.Field(
        AlertsNrqlConditionTermsOperator, graphql_name="termsOperator"
    )


class AlertsNrqlDynamicConditionTermsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "disable_health_status_reporting",
        "operator",
        "priority",
        "threshold",
        "threshold_duration",
        "threshold_occurrences",
    )
    disable_health_status_reporting = sgqlc.types.Field(
        Boolean, graphql_name="disableHealthStatusReporting"
    )

    operator = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlDynamicConditionTermsOperator),
        graphql_name="operator",
    )

    priority = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlConditionPriority), graphql_name="priority"
    )

    threshold = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="threshold")

    threshold_duration = sgqlc.types.Field(
        sgqlc.types.non_null(Seconds), graphql_name="thresholdDuration"
    )

    threshold_occurrences = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlConditionThresholdOccurrences),
        graphql_name="thresholdOccurrences",
    )


class AlertsOpsGenieNotificationChannelCreateInput(sgqlc.types.Input):
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

    data_center_region = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsOpsGenieDataCenterRegion),
        graphql_name="dataCenterRegion",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    recipients = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="recipients"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="tags"
    )

    teams = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="teams"
    )


class AlertsOpsGenieNotificationChannelUpdateInput(sgqlc.types.Input):
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

    data_center_region = sgqlc.types.Field(
        AlertsOpsGenieDataCenterRegion, graphql_name="dataCenterRegion"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    recipients = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="recipients"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="tags"
    )

    teams = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="teams"
    )


class AlertsPagerDutyNotificationChannelCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("api_key", "name")
    api_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiKey"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AlertsPagerDutyNotificationChannelUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("api_key", "name")
    api_key = sgqlc.types.Field(SecureValue, graphql_name="apiKey")

    name = sgqlc.types.Field(String, graphql_name="name")


class AlertsPoliciesSearchCriteriaInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("ids", "name", "name_like")
    ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="ids"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    name_like = sgqlc.types.Field(String, graphql_name="nameLike")


class AlertsPolicyInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident_preference", "name")
    incident_preference = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsIncidentPreference),
        graphql_name="incidentPreference",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AlertsPolicyUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("incident_preference", "name")
    incident_preference = sgqlc.types.Field(
        AlertsIncidentPreference, graphql_name="incidentPreference"
    )

    name = sgqlc.types.Field(String, graphql_name="name")


class AlertsSlackNotificationChannelCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "team_channel", "url")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    team_channel = sgqlc.types.Field(String, graphql_name="teamChannel")

    url = sgqlc.types.Field(sgqlc.types.non_null(SecureValue), graphql_name="url")


class AlertsSlackNotificationChannelUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "team_channel", "url")
    name = sgqlc.types.Field(String, graphql_name="name")

    team_channel = sgqlc.types.Field(String, graphql_name="teamChannel")

    url = sgqlc.types.Field(SecureValue, graphql_name="url")


class AlertsVictorOpsNotificationChannelCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "name", "route_key")
    key = sgqlc.types.Field(sgqlc.types.non_null(SecureValue), graphql_name="key")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    route_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="routeKey")


class AlertsVictorOpsNotificationChannelUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "name", "route_key")
    key = sgqlc.types.Field(SecureValue, graphql_name="key")

    name = sgqlc.types.Field(String, graphql_name="name")

    route_key = sgqlc.types.Field(String, graphql_name="routeKey")


class AlertsWebhookBasicAuthMutationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("password", "username")
    password = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="password"
    )

    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="username")


class AlertsWebhookCustomHeaderMutationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "value")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    value = sgqlc.types.Field(sgqlc.types.non_null(SecureValue), graphql_name="value")


class AlertsWebhookNotificationChannelCreateInput(sgqlc.types.Input):
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

    basic_auth = sgqlc.types.Field(
        AlertsWebhookBasicAuthMutationInput, graphql_name="basicAuth"
    )

    custom_http_headers = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AlertsWebhookCustomHeaderMutationInput)
        ),
        graphql_name="customHttpHeaders",
    )

    custom_payload_body = sgqlc.types.Field(String, graphql_name="customPayloadBody")

    custom_payload_type = sgqlc.types.Field(
        AlertsWebhookCustomPayloadType, graphql_name="customPayloadType"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AlertsWebhookNotificationChannelUpdateInput(sgqlc.types.Input):
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

    basic_auth = sgqlc.types.Field(
        AlertsWebhookBasicAuthMutationInput, graphql_name="basicAuth"
    )

    custom_http_headers = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AlertsWebhookCustomHeaderMutationInput)
        ),
        graphql_name="customHttpHeaders",
    )

    custom_payload_body = sgqlc.types.Field(String, graphql_name="customPayloadBody")

    custom_payload_type = sgqlc.types.Field(
        AlertsWebhookCustomPayloadType, graphql_name="customPayloadType"
    )

    name = sgqlc.types.Field(String, graphql_name="name")


class AlertsXMattersNotificationChannelCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("integration_url", "name")
    integration_url = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="integrationUrl"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AlertsXMattersNotificationChannelUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("integration_url", "name")
    integration_url = sgqlc.types.Field(SecureValue, graphql_name="integrationUrl")

    name = sgqlc.types.Field(String, graphql_name="name")


class ApiAccessCreateIngestKeyInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "ingest_type", "name", "notes")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    ingest_type = sgqlc.types.Field(
        sgqlc.types.non_null(ApiAccessIngestKeyType), graphql_name="ingestType"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    notes = sgqlc.types.Field(String, graphql_name="notes")


class ApiAccessCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("ingest", "user")
    ingest = sgqlc.types.Field(
        sgqlc.types.list_of(ApiAccessCreateIngestKeyInput), graphql_name="ingest"
    )

    user = sgqlc.types.Field(
        sgqlc.types.list_of("ApiAccessCreateUserKeyInput"), graphql_name="user"
    )


class ApiAccessCreateUserKeyInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "name", "notes", "user_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    name = sgqlc.types.Field(String, graphql_name="name")

    notes = sgqlc.types.Field(String, graphql_name="notes")

    user_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="userId")


class ApiAccessDeleteInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("ingest_key_ids", "user_key_ids")
    ingest_key_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="ingestKeyIds"
    )

    user_key_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="userKeyIds"
    )


class ApiAccessKeySearchQuery(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("scope", "types")
    scope = sgqlc.types.Field("ApiAccessKeySearchScope", graphql_name="scope")

    types = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(ApiAccessKeyType)),
        graphql_name="types",
    )


class ApiAccessKeySearchScope(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "ingest_types", "user_ids")
    account_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="accountIds")

    ingest_types = sgqlc.types.Field(
        sgqlc.types.list_of(ApiAccessIngestKeyType), graphql_name="ingestTypes"
    )

    user_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="userIds")


class ApiAccessUpdateIngestKeyInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key_id", "name", "notes")
    key_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="keyId")

    name = sgqlc.types.Field(String, graphql_name="name")

    notes = sgqlc.types.Field(String, graphql_name="notes")


class ApiAccessUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("ingest", "user")
    ingest = sgqlc.types.Field(
        sgqlc.types.list_of(ApiAccessUpdateIngestKeyInput), graphql_name="ingest"
    )

    user = sgqlc.types.Field(
        sgqlc.types.list_of("ApiAccessUpdateUserKeyInput"), graphql_name="user"
    )


class ApiAccessUpdateUserKeyInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key_id", "name", "notes")
    key_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="keyId")

    name = sgqlc.types.Field(String, graphql_name="name")

    notes = sgqlc.types.Field(String, graphql_name="notes")


class ApmApplicationEntitySettings(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("apdex_target",)
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class AuthorizationManagementAccountAccessGrant(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "role_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    role_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="roleId")


class AuthorizationManagementEntity(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")


class AuthorizationManagementEntityAccessGrants(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("entity", "role_id")
    entity = sgqlc.types.Field(
        sgqlc.types.non_null(AuthorizationManagementEntity), graphql_name="entity"
    )

    role_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="roleId")


class AuthorizationManagementGrantAccess(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "account_access_grants",
        "entity_access_grants",
        "grantee",
        "group_access_grants",
        "group_id",
        "organization_access_grants",
    )
    account_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AuthorizationManagementAccountAccessGrant)
        ),
        graphql_name="accountAccessGrants",
    )

    entity_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AuthorizationManagementEntityAccessGrants)
        ),
        graphql_name="entityAccessGrants",
    )

    grantee = sgqlc.types.Field(
        "AuthorizationManagementGrantee", graphql_name="grantee"
    )

    group_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("AuthorizationManagementGroupAccessGrant")
        ),
        graphql_name="groupAccessGrants",
    )

    group_id = sgqlc.types.Field(ID, graphql_name="groupId")

    organization_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("AuthorizationManagementOrganizationAccessGrant")
        ),
        graphql_name="organizationAccessGrants",
    )


class AuthorizationManagementGrantee(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(AuthorizationManagementGranteeTypeEnum),
        graphql_name="type",
    )


class AuthorizationManagementGroupAccessGrant(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("group_id", "role_id")
    group_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="groupId")

    role_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="roleId")


class AuthorizationManagementOrganizationAccessGrant(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("role_id",)
    role_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="roleId")


class AuthorizationManagementRevokeAccess(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "account_access_grants",
        "entity_access_grants",
        "grantee",
        "group_access_grants",
        "group_id",
        "organization_access_grants",
    )
    account_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AuthorizationManagementAccountAccessGrant)
        ),
        graphql_name="accountAccessGrants",
    )

    entity_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AuthorizationManagementEntityAccessGrants)
        ),
        graphql_name="entityAccessGrants",
    )

    grantee = sgqlc.types.Field(AuthorizationManagementGrantee, graphql_name="grantee")

    group_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AuthorizationManagementGroupAccessGrant)
        ),
        graphql_name="groupAccessGrants",
    )

    group_id = sgqlc.types.Field(ID, graphql_name="groupId")

    organization_access_grants = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(AuthorizationManagementOrganizationAccessGrant)
        ),
        graphql_name="organizationAccessGrants",
    )


class ChangeTrackingCategoryAndTypeInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("category", "type")
    category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="category")

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")


class ChangeTrackingCategoryFieldsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("deployment", "feature_flag")
    deployment = sgqlc.types.Field(
        "ChangeTrackingDeploymentFieldsInput", graphql_name="deployment"
    )

    feature_flag = sgqlc.types.Field(
        "ChangeTrackingFeatureFlagFieldsInput", graphql_name="featureFlag"
    )


class ChangeTrackingCategoryRelatedInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("category_fields", "kind")
    category_fields = sgqlc.types.Field(
        ChangeTrackingCategoryFieldsInput, graphql_name="categoryFields"
    )

    kind = sgqlc.types.Field(
        sgqlc.types.non_null(ChangeTrackingCategoryAndTypeInput), graphql_name="kind"
    )


class ChangeTrackingChangeTrackingSearchFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "limit", "query", "time_window")
    account_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="accountIds"
    )

    limit = sgqlc.types.Field(Int, graphql_name="limit")

    query = sgqlc.types.Field(String, graphql_name="query")

    time_window = sgqlc.types.Field(
        "ChangeTrackingTimeWindowInputWithDefaults", graphql_name="timeWindow"
    )


class ChangeTrackingCreateEventInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "category_and_type_data",
        "custom_attributes",
        "description",
        "entity_search",
        "group_id",
        "short_description",
        "timestamp",
        "user",
    )
    category_and_type_data = sgqlc.types.Field(
        sgqlc.types.non_null(ChangeTrackingCategoryRelatedInput),
        graphql_name="categoryAndTypeData",
    )

    custom_attributes = sgqlc.types.Field(
        ChangeTrackingRawCustomAttributesMap, graphql_name="customAttributes"
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    entity_search = sgqlc.types.Field(
        sgqlc.types.non_null("ChangeTrackingEntitySearchInput"),
        graphql_name="entitySearch",
    )

    group_id = sgqlc.types.Field(String, graphql_name="groupId")

    short_description = sgqlc.types.Field(String, graphql_name="shortDescription")

    timestamp = sgqlc.types.Field(EpochMilliseconds, graphql_name="timestamp")

    user = sgqlc.types.Field(String, graphql_name="user")


class ChangeTrackingDataHandlingRules(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("validation_flags",)
    validation_flags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ChangeTrackingValidationFlag)),
        graphql_name="validationFlags",
    )


class ChangeTrackingDeploymentFieldsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("changelog", "commit", "deep_link", "version")
    changelog = sgqlc.types.Field(String, graphql_name="changelog")

    commit = sgqlc.types.Field(String, graphql_name="commit")

    deep_link = sgqlc.types.Field(String, graphql_name="deepLink")

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="version")


class ChangeTrackingDeploymentInput(sgqlc.types.Input):
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

    commit = sgqlc.types.Field(String, graphql_name="commit")

    deep_link = sgqlc.types.Field(String, graphql_name="deepLink")

    deployment_type = sgqlc.types.Field(
        ChangeTrackingDeploymentType, graphql_name="deploymentType"
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    entity_guid = sgqlc.types.Field(
        sgqlc.types.non_null(EntityGuid), graphql_name="entityGuid"
    )

    group_id = sgqlc.types.Field(String, graphql_name="groupId")

    timestamp = sgqlc.types.Field(EpochMilliseconds, graphql_name="timestamp")

    user = sgqlc.types.Field(String, graphql_name="user")

    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="version")


class ChangeTrackingEntitySearchInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("query",)
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="query")


class ChangeTrackingFeatureFlagFieldsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("feature_flag_id",)
    feature_flag_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="featureFlagId"
    )


class ChangeTrackingSearchFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("limit", "query", "time_window")
    limit = sgqlc.types.Field(Int, graphql_name="limit")

    query = sgqlc.types.Field(String, graphql_name="query")

    time_window = sgqlc.types.Field(
        "ChangeTrackingTimeWindowInputWithDefaults", graphql_name="timeWindow"
    )


class ChangeTrackingTimeWindowInputWithDefaults(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("end_time", "start_time")
    end_time = sgqlc.types.Field(EpochMilliseconds, graphql_name="endTime")

    start_time = sgqlc.types.Field(EpochMilliseconds, graphql_name="startTime")


class CloudAlbIntegrationInput(sgqlc.types.Input):
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

    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    load_balancer_prefixes = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="loadBalancerPrefixes"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudApigatewayIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    stage_prefixes = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="stagePrefixes"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudAutoscalingIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsAppsyncIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsAthenaIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsAutoDiscoveryIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsCognitoIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsConnectIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsDirectconnectIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "alb",
        "apigateway",
        "autoscaling",
        "aws_appsync",
        "aws_athena",
        "aws_auto_discovery",
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
        "aws_ms_elasticache",
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
        "security_hub",
        "ses",
        "sns",
        "sqs",
        "trustedadvisor",
        "vpc",
    )
    alb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="alb"
    )

    apigateway = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="apigateway",
    )

    autoscaling = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="autoscaling",
    )

    aws_appsync = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsAppsync",
    )

    aws_athena = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsAthena",
    )

    aws_auto_discovery = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsAutoDiscovery",
    )

    aws_cognito = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsCognito",
    )

    aws_connect = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsConnect",
    )

    aws_directconnect = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsDirectconnect",
    )

    aws_docdb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsDocdb",
    )

    aws_fsx = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsFsx",
    )

    aws_glue = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsGlue",
    )

    aws_kinesisanalytics = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsKinesisanalytics",
    )

    aws_mediaconvert = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsMediaconvert",
    )

    aws_mediapackagevod = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsMediapackagevod",
    )

    aws_metadata = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsMetadata",
    )

    aws_mq = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="awsMq"
    )

    aws_ms_elasticache = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsMsElasticache",
    )

    aws_msk = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsMsk",
    )

    aws_neptune = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsNeptune",
    )

    aws_qldb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsQldb",
    )

    aws_route53resolver = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsRoute53resolver",
    )

    aws_states = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsStates",
    )

    aws_tags_global = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsTagsGlobal",
    )

    aws_transitgateway = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsTransitgateway",
    )

    aws_waf = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsWaf",
    )

    aws_wafv2 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsWafv2",
    )

    aws_xray = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsXray",
    )

    billing = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="billing",
    )

    cloudfront = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="cloudfront",
    )

    cloudtrail = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="cloudtrail",
    )

    dynamodb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="dynamodb",
    )

    ebs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="ebs"
    )

    ec2 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="ec2"
    )

    ecs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="ecs"
    )

    efs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="efs"
    )

    elasticache = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="elasticache",
    )

    elasticbeanstalk = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="elasticbeanstalk",
    )

    elasticsearch = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="elasticsearch",
    )

    elb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="elb"
    )

    emr = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="emr"
    )

    health = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="health",
    )

    iam = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="iam"
    )

    iot = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="iot"
    )

    kinesis = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="kinesis",
    )

    kinesis_firehose = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="kinesisFirehose",
    )

    lambda_ = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="lambda",
    )

    rds = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="rds"
    )

    redshift = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="redshift",
    )

    route53 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="route53",
    )

    s3 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="s3"
    )

    security_hub = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="securityHub",
    )

    ses = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="ses"
    )

    sns = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="sns"
    )

    sqs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="sqs"
    )

    trustedadvisor = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="trustedadvisor",
    )

    vpc = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="vpc"
    )


class CloudAwsDocdbIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsFsxIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsGlueIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsGovCloudLinkAccountInput(sgqlc.types.Input):
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

    aws_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="awsAccountId"
    )

    metric_collection_mode = sgqlc.types.Field(
        CloudMetricCollectionMode, graphql_name="metricCollectionMode"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    secret_access_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="secretAccessKey"
    )


class CloudAwsGovCloudMigrateToAssumeroleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("arn", "linked_account_id")
    arn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="arn")

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )


class CloudAwsGovCloudUpdateAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "access_key_id",
        "aws_account_id",
        "disabled",
        "linked_account_id",
        "name",
        "secret_access_key",
    )
    access_key_id = sgqlc.types.Field(String, graphql_name="accessKeyId")

    aws_account_id = sgqlc.types.Field(String, graphql_name="awsAccountId")

    disabled = sgqlc.types.Field(Boolean, graphql_name="disabled")

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    secret_access_key = sgqlc.types.Field(SecureValue, graphql_name="secretAccessKey")


class CloudAwsGovcloudDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "alb",
        "apigateway",
        "autoscaling",
        "aws_directconnect",
        "aws_meta_data_gov",
        "aws_ms_elasticache_gov",
        "aws_states",
        "aws_tags_global_gov",
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

    apigateway = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="apigateway",
    )

    autoscaling = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="autoscaling",
    )

    aws_directconnect = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsDirectconnect",
    )

    aws_meta_data_gov = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsMetaDataGov",
    )

    aws_ms_elasticache_gov = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsMsElasticacheGov",
    )

    aws_states = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsStates",
    )

    aws_tags_global_gov = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="awsTagsGlobalGov",
    )

    cloudtrail = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="cloudtrail",
    )

    dynamodb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="dynamodb",
    )

    ebs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="ebs"
    )

    ec2 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="ec2"
    )

    elasticsearch = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="elasticsearch",
    )

    elb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="elb"
    )

    emr = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="emr"
    )

    iam = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="iam"
    )

    lambda_ = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="lambda",
    )

    rds = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="rds"
    )

    redshift = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="redshift",
    )

    route53 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="route53",
    )

    s3 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="s3"
    )

    sns = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="sns"
    )

    sqs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"), graphql_name="sqs"
    )


class CloudAwsGovcloudIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "alb",
        "apigateway",
        "autoscaling",
        "aws_directconnect",
        "aws_metadata_gov",
        "aws_ms_elasticache_gov",
        "aws_states",
        "aws_tags_global_gov",
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

    apigateway = sgqlc.types.Field(
        sgqlc.types.list_of(CloudApigatewayIntegrationInput), graphql_name="apigateway"
    )

    autoscaling = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAutoscalingIntegrationInput),
        graphql_name="autoscaling",
    )

    aws_directconnect = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsDirectconnectIntegrationInput),
        graphql_name="awsDirectconnect",
    )

    aws_metadata_gov = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsMetadataGovIntegrationInput"),
        graphql_name="awsMetadataGov",
    )

    aws_ms_elasticache_gov = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsMsElasticacheGovIntegrationInput"),
        graphql_name="awsMsElasticacheGov",
    )

    aws_states = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsStatesIntegrationInput"), graphql_name="awsStates"
    )

    aws_tags_global_gov = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsTagsGlobalGovIntegrationInput"),
        graphql_name="awsTagsGlobalGov",
    )

    cloudtrail = sgqlc.types.Field(
        sgqlc.types.list_of("CloudCloudtrailIntegrationInput"),
        graphql_name="cloudtrail",
    )

    dynamodb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDynamodbIntegrationInput"), graphql_name="dynamodb"
    )

    ebs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudEbsIntegrationInput"), graphql_name="ebs"
    )

    ec2 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudEc2IntegrationInput"), graphql_name="ec2"
    )

    elasticsearch = sgqlc.types.Field(
        sgqlc.types.list_of("CloudElasticsearchIntegrationInput"),
        graphql_name="elasticsearch",
    )

    elb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudElbIntegrationInput"), graphql_name="elb"
    )

    emr = sgqlc.types.Field(
        sgqlc.types.list_of("CloudEmrIntegrationInput"), graphql_name="emr"
    )

    iam = sgqlc.types.Field(
        sgqlc.types.list_of("CloudIamIntegrationInput"), graphql_name="iam"
    )

    lambda_ = sgqlc.types.Field(
        sgqlc.types.list_of("CloudLambdaIntegrationInput"), graphql_name="lambda"
    )

    rds = sgqlc.types.Field(
        sgqlc.types.list_of("CloudRdsIntegrationInput"), graphql_name="rds"
    )

    redshift = sgqlc.types.Field(
        sgqlc.types.list_of("CloudRedshiftIntegrationInput"), graphql_name="redshift"
    )

    route53 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudRoute53IntegrationInput"), graphql_name="route53"
    )

    s3 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudS3IntegrationInput"), graphql_name="s3"
    )

    sns = sgqlc.types.Field(
        sgqlc.types.list_of("CloudSnsIntegrationInput"), graphql_name="sns"
    )

    sqs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudSqsIntegrationInput"), graphql_name="sqs"
    )


class CloudAwsIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "alb",
        "apigateway",
        "autoscaling",
        "aws_appsync",
        "aws_athena",
        "aws_auto_discovery",
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
        "aws_ms_elasticache",
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
        "security_hub",
        "ses",
        "sns",
        "sqs",
        "trustedadvisor",
        "vpc",
    )
    alb = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAlbIntegrationInput), graphql_name="alb"
    )

    apigateway = sgqlc.types.Field(
        sgqlc.types.list_of(CloudApigatewayIntegrationInput), graphql_name="apigateway"
    )

    autoscaling = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAutoscalingIntegrationInput),
        graphql_name="autoscaling",
    )

    aws_appsync = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsAppsyncIntegrationInput), graphql_name="awsAppsync"
    )

    aws_athena = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsAthenaIntegrationInput), graphql_name="awsAthena"
    )

    aws_auto_discovery = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsAutoDiscoveryIntegrationInput),
        graphql_name="awsAutoDiscovery",
    )

    aws_cognito = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsCognitoIntegrationInput), graphql_name="awsCognito"
    )

    aws_connect = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsConnectIntegrationInput), graphql_name="awsConnect"
    )

    aws_directconnect = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsDirectconnectIntegrationInput),
        graphql_name="awsDirectconnect",
    )

    aws_docdb = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsDocdbIntegrationInput), graphql_name="awsDocdb"
    )

    aws_fsx = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsFsxIntegrationInput), graphql_name="awsFsx"
    )

    aws_glue = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAwsGlueIntegrationInput), graphql_name="awsGlue"
    )

    aws_kinesisanalytics = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsKinesisanalyticsIntegrationInput"),
        graphql_name="awsKinesisanalytics",
    )

    aws_mediaconvert = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsMediaconvertIntegrationInput"),
        graphql_name="awsMediaconvert",
    )

    aws_mediapackagevod = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsMediapackagevodIntegrationInput"),
        graphql_name="awsMediapackagevod",
    )

    aws_metadata = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsMetadataIntegrationInput"),
        graphql_name="awsMetadata",
    )

    aws_mq = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsMqIntegrationInput"), graphql_name="awsMq"
    )

    aws_ms_elasticache = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsMsElasticacheIntegrationInput"),
        graphql_name="awsMsElasticache",
    )

    aws_msk = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsMskIntegrationInput"), graphql_name="awsMsk"
    )

    aws_neptune = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsNeptuneIntegrationInput"),
        graphql_name="awsNeptune",
    )

    aws_qldb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsQldbIntegrationInput"), graphql_name="awsQldb"
    )

    aws_route53resolver = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsRoute53resolverIntegrationInput"),
        graphql_name="awsRoute53resolver",
    )

    aws_states = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsStatesIntegrationInput"), graphql_name="awsStates"
    )

    aws_tags_global = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsTagsGlobalIntegrationInput"),
        graphql_name="awsTagsGlobal",
    )

    aws_transitgateway = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsTransitgatewayIntegrationInput"),
        graphql_name="awsTransitgateway",
    )

    aws_waf = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsWafIntegrationInput"), graphql_name="awsWaf"
    )

    aws_wafv2 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsWafv2IntegrationInput"), graphql_name="awsWafv2"
    )

    aws_xray = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAwsXrayIntegrationInput"), graphql_name="awsXray"
    )

    billing = sgqlc.types.Field(
        sgqlc.types.list_of("CloudBillingIntegrationInput"), graphql_name="billing"
    )

    cloudfront = sgqlc.types.Field(
        sgqlc.types.list_of("CloudCloudfrontIntegrationInput"),
        graphql_name="cloudfront",
    )

    cloudtrail = sgqlc.types.Field(
        sgqlc.types.list_of("CloudCloudtrailIntegrationInput"),
        graphql_name="cloudtrail",
    )

    dynamodb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDynamodbIntegrationInput"), graphql_name="dynamodb"
    )

    ebs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudEbsIntegrationInput"), graphql_name="ebs"
    )

    ec2 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudEc2IntegrationInput"), graphql_name="ec2"
    )

    ecs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudEcsIntegrationInput"), graphql_name="ecs"
    )

    efs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudEfsIntegrationInput"), graphql_name="efs"
    )

    elasticache = sgqlc.types.Field(
        sgqlc.types.list_of("CloudElasticacheIntegrationInput"),
        graphql_name="elasticache",
    )

    elasticbeanstalk = sgqlc.types.Field(
        sgqlc.types.list_of("CloudElasticbeanstalkIntegrationInput"),
        graphql_name="elasticbeanstalk",
    )

    elasticsearch = sgqlc.types.Field(
        sgqlc.types.list_of("CloudElasticsearchIntegrationInput"),
        graphql_name="elasticsearch",
    )

    elb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudElbIntegrationInput"), graphql_name="elb"
    )

    emr = sgqlc.types.Field(
        sgqlc.types.list_of("CloudEmrIntegrationInput"), graphql_name="emr"
    )

    health = sgqlc.types.Field(
        sgqlc.types.list_of("CloudHealthIntegrationInput"), graphql_name="health"
    )

    iam = sgqlc.types.Field(
        sgqlc.types.list_of("CloudIamIntegrationInput"), graphql_name="iam"
    )

    iot = sgqlc.types.Field(
        sgqlc.types.list_of("CloudIotIntegrationInput"), graphql_name="iot"
    )

    kinesis = sgqlc.types.Field(
        sgqlc.types.list_of("CloudKinesisIntegrationInput"), graphql_name="kinesis"
    )

    kinesis_firehose = sgqlc.types.Field(
        sgqlc.types.list_of("CloudKinesisFirehoseIntegrationInput"),
        graphql_name="kinesisFirehose",
    )

    lambda_ = sgqlc.types.Field(
        sgqlc.types.list_of("CloudLambdaIntegrationInput"), graphql_name="lambda"
    )

    rds = sgqlc.types.Field(
        sgqlc.types.list_of("CloudRdsIntegrationInput"), graphql_name="rds"
    )

    redshift = sgqlc.types.Field(
        sgqlc.types.list_of("CloudRedshiftIntegrationInput"), graphql_name="redshift"
    )

    route53 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudRoute53IntegrationInput"), graphql_name="route53"
    )

    s3 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudS3IntegrationInput"), graphql_name="s3"
    )

    security_hub = sgqlc.types.Field(
        sgqlc.types.list_of("CloudSecurityHubIntegrationInput"),
        graphql_name="securityHub",
    )

    ses = sgqlc.types.Field(
        sgqlc.types.list_of("CloudSesIntegrationInput"), graphql_name="ses"
    )

    sns = sgqlc.types.Field(
        sgqlc.types.list_of("CloudSnsIntegrationInput"), graphql_name="sns"
    )

    sqs = sgqlc.types.Field(
        sgqlc.types.list_of("CloudSqsIntegrationInput"), graphql_name="sqs"
    )

    trustedadvisor = sgqlc.types.Field(
        sgqlc.types.list_of("CloudTrustedadvisorIntegrationInput"),
        graphql_name="trustedadvisor",
    )

    vpc = sgqlc.types.Field(
        sgqlc.types.list_of("CloudVpcIntegrationInput"), graphql_name="vpc"
    )


class CloudAwsKinesisanalyticsIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsLinkAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("arn", "metric_collection_mode", "name")
    arn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="arn")

    metric_collection_mode = sgqlc.types.Field(
        CloudMetricCollectionMode, graphql_name="metricCollectionMode"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class CloudAwsMediaconvertIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsMediapackagevodIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsMetadataGovIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsMetadataIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsMqIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsMsElasticacheGovIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsMsElasticacheIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsMskIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsNeptuneIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsQldbIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsRoute53resolverIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsStatesIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsTagsGlobalGovIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsTagsGlobalIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsTransitgatewayIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsUpdateAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("arn", "disabled", "linked_account_id", "name")
    arn = sgqlc.types.Field(String, graphql_name="arn")

    disabled = sgqlc.types.Field(Boolean, graphql_name="disabled")

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    name = sgqlc.types.Field(String, graphql_name="name")


class CloudAwsWafIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsWafv2IntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsXrayIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureApimanagementIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureAppgatewayIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureAppserviceIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureContainersIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureCosmosdbIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureCostmanagementIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_keys = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="tagKeys")


class CloudAzureDatafactoryIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureDisableIntegrationsInput(sgqlc.types.Input):
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

    azure_appgateway = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureAppgateway",
    )

    azure_appservice = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureAppservice",
    )

    azure_containers = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureContainers",
    )

    azure_cosmosdb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureCosmosdb",
    )

    azure_costmanagement = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureCostmanagement",
    )

    azure_datafactory = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureDatafactory",
    )

    azure_eventhub = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureEventhub",
    )

    azure_expressroute = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureExpressroute",
    )

    azure_firewalls = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureFirewalls",
    )

    azure_frontdoor = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureFrontdoor",
    )

    azure_functions = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureFunctions",
    )

    azure_keyvault = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureKeyvault",
    )

    azure_loadbalancer = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureLoadbalancer",
    )

    azure_logicapps = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureLogicapps",
    )

    azure_machinelearning = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureMachinelearning",
    )

    azure_mariadb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureMariadb",
    )

    azure_monitor = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureMonitor",
    )

    azure_mysql = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureMysql",
    )

    azure_mysqlflexible = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureMysqlflexible",
    )

    azure_postgresql = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azurePostgresql",
    )

    azure_postgresqlflexible = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azurePostgresqlflexible",
    )

    azure_powerbidedicated = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azurePowerbidedicated",
    )

    azure_rediscache = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureRediscache",
    )

    azure_servicebus = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureServicebus",
    )

    azure_sql = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureSql",
    )

    azure_sqlmanaged = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureSqlmanaged",
    )

    azure_storage = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureStorage",
    )

    azure_virtualmachine = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureVirtualmachine",
    )

    azure_virtualnetworks = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureVirtualnetworks",
    )

    azure_vms = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureVms",
    )

    azure_vpngateways = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="azureVpngateways",
    )


class CloudAzureEventhubIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureExpressrouteIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureFirewallsIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureFrontdoorIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureFunctionsIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureIntegrationsInput(sgqlc.types.Input):
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

    azure_appgateway = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureAppgatewayIntegrationInput),
        graphql_name="azureAppgateway",
    )

    azure_appservice = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureAppserviceIntegrationInput),
        graphql_name="azureAppservice",
    )

    azure_containers = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureContainersIntegrationInput),
        graphql_name="azureContainers",
    )

    azure_cosmosdb = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureCosmosdbIntegrationInput),
        graphql_name="azureCosmosdb",
    )

    azure_costmanagement = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureCostmanagementIntegrationInput),
        graphql_name="azureCostmanagement",
    )

    azure_datafactory = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureDatafactoryIntegrationInput),
        graphql_name="azureDatafactory",
    )

    azure_eventhub = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureEventhubIntegrationInput),
        graphql_name="azureEventhub",
    )

    azure_expressroute = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureExpressrouteIntegrationInput),
        graphql_name="azureExpressroute",
    )

    azure_firewalls = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureFirewallsIntegrationInput),
        graphql_name="azureFirewalls",
    )

    azure_frontdoor = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureFrontdoorIntegrationInput),
        graphql_name="azureFrontdoor",
    )

    azure_functions = sgqlc.types.Field(
        sgqlc.types.list_of(CloudAzureFunctionsIntegrationInput),
        graphql_name="azureFunctions",
    )

    azure_keyvault = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureKeyvaultIntegrationInput"),
        graphql_name="azureKeyvault",
    )

    azure_loadbalancer = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureLoadbalancerIntegrationInput"),
        graphql_name="azureLoadbalancer",
    )

    azure_logicapps = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureLogicappsIntegrationInput"),
        graphql_name="azureLogicapps",
    )

    azure_machinelearning = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureMachinelearningIntegrationInput"),
        graphql_name="azureMachinelearning",
    )

    azure_mariadb = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureMariadbIntegrationInput"),
        graphql_name="azureMariadb",
    )

    azure_monitor = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureMonitorIntegrationInput"),
        graphql_name="azureMonitor",
    )

    azure_mysql = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureMysqlIntegrationInput"),
        graphql_name="azureMysql",
    )

    azure_mysqlflexible = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureMysqlflexibleIntegrationInput"),
        graphql_name="azureMysqlflexible",
    )

    azure_postgresql = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzurePostgresqlIntegrationInput"),
        graphql_name="azurePostgresql",
    )

    azure_postgresqlflexible = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzurePostgresqlflexibleIntegrationInput"),
        graphql_name="azurePostgresqlflexible",
    )

    azure_powerbidedicated = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzurePowerbidedicatedIntegrationInput"),
        graphql_name="azurePowerbidedicated",
    )

    azure_rediscache = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureRediscacheIntegrationInput"),
        graphql_name="azureRediscache",
    )

    azure_servicebus = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureServicebusIntegrationInput"),
        graphql_name="azureServicebus",
    )

    azure_sql = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureSqlIntegrationInput"), graphql_name="azureSql"
    )

    azure_sqlmanaged = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureSqlmanagedIntegrationInput"),
        graphql_name="azureSqlmanaged",
    )

    azure_storage = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureStorageIntegrationInput"),
        graphql_name="azureStorage",
    )

    azure_virtualmachine = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureVirtualmachineIntegrationInput"),
        graphql_name="azureVirtualmachine",
    )

    azure_virtualnetworks = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureVirtualnetworksIntegrationInput"),
        graphql_name="azureVirtualnetworks",
    )

    azure_vms = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureVmsIntegrationInput"), graphql_name="azureVms"
    )

    azure_vpngateways = sgqlc.types.Field(
        sgqlc.types.list_of("CloudAzureVpngatewaysIntegrationInput"),
        graphql_name="azureVpngateways",
    )


class CloudAzureKeyvaultIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureLinkAccountInput(sgqlc.types.Input):
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

    client_secret = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="clientSecret"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    subscription_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="subscriptionId"
    )

    tenant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="tenantId")


class CloudAzureLoadbalancerIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureLogicappsIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureMachinelearningIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureMariadbIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureMonitorIntegrationInput(sgqlc.types.Input):
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

    exclude_tags = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="excludeTags"
    )

    include_tags = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="includeTags"
    )

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )

    resource_types = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceTypes"
    )


class CloudAzureMysqlIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureMysqlflexibleIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzurePostgresqlIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzurePostgresqlflexibleIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzurePowerbidedicatedIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureRediscacheIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureServicebusIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureSqlIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureSqlmanagedIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureStorageIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureUpdateAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "application_id",
        "client_secret",
        "disabled",
        "linked_account_id",
        "name",
        "subscription_id",
        "tenant_id",
    )
    application_id = sgqlc.types.Field(String, graphql_name="applicationId")

    client_secret = sgqlc.types.Field(SecureValue, graphql_name="clientSecret")

    disabled = sgqlc.types.Field(Boolean, graphql_name="disabled")

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    subscription_id = sgqlc.types.Field(String, graphql_name="subscriptionId")

    tenant_id = sgqlc.types.Field(String, graphql_name="tenantId")


class CloudAzureVirtualmachineIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureVirtualnetworksIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureVmsIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudAzureVpngatewaysIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    resource_groups = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="resourceGroups"
    )


class CloudBillingIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudCciAwsDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("cci_aws_s3",)
    cci_aws_s3 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="cciAwsS3",
    )


class CloudCciAwsIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("cci_aws_s3",)
    cci_aws_s3 = sgqlc.types.Field(
        sgqlc.types.list_of("CloudCciAwsS3IntegrationInput"), graphql_name="cciAwsS3"
    )


class CloudCciAwsLinkAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("arn", "external_id", "metric_collection_mode", "name")
    arn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="arn")

    external_id = sgqlc.types.Field(String, graphql_name="externalId")

    metric_collection_mode = sgqlc.types.Field(
        CloudMetricCollectionMode, graphql_name="metricCollectionMode"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class CloudCciAwsS3IntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
        "s3_bucket_name",
        "s3_bucket_path",
        "s3_bucket_region",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    s3_bucket_name = sgqlc.types.Field(String, graphql_name="s3BucketName")

    s3_bucket_path = sgqlc.types.Field(String, graphql_name="s3BucketPath")

    s3_bucket_region = sgqlc.types.Field(String, graphql_name="s3BucketRegion")


class CloudCloudfrontIntegrationInput(sgqlc.types.Input):
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

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudCloudtrailIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudConfluentDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "confluent_kafka_connector_resource",
        "confluent_kafka_ksql_resource",
        "confluent_kafka_resource",
    )
    confluent_kafka_connector_resource = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="confluentKafkaConnectorResource",
    )

    confluent_kafka_ksql_resource = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="confluentKafkaKsqlResource",
    )

    confluent_kafka_resource = sgqlc.types.Field(
        sgqlc.types.list_of("CloudDisableAccountIntegrationInput"),
        graphql_name="confluentKafkaResource",
    )


class CloudConfluentIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "confluent_kafka_connector_resource",
        "confluent_kafka_ksql_resource",
        "confluent_kafka_resource",
    )
    confluent_kafka_connector_resource = sgqlc.types.Field(
        sgqlc.types.list_of("CloudConfluentKafkaConnectorResourceIntegrationInput"),
        graphql_name="confluentKafkaConnectorResource",
    )

    confluent_kafka_ksql_resource = sgqlc.types.Field(
        sgqlc.types.list_of("CloudConfluentKafkaKsqlResourceIntegrationInput"),
        graphql_name="confluentKafkaKsqlResource",
    )

    confluent_kafka_resource = sgqlc.types.Field(
        sgqlc.types.list_of("CloudConfluentKafkaResourceIntegrationInput"),
        graphql_name="confluentKafkaResource",
    )


class CloudConfluentKafkaConnectorResourceIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudConfluentKafkaKsqlResourceIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudConfluentKafkaResourceIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudConfluentLinkAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("api_key", "api_secret", "external_id", "name")
    api_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiKey"
    )

    api_secret = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiSecret"
    )

    external_id = sgqlc.types.Field(String, graphql_name="externalId")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class CloudConfluentUpdateAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "api_key",
        "api_secret",
        "disabled",
        "external_id",
        "linked_account_id",
        "name",
    )
    api_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiKey"
    )

    api_secret = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiSecret"
    )

    disabled = sgqlc.types.Field(Boolean, graphql_name="disabled")

    external_id = sgqlc.types.Field(String, graphql_name="externalId")

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    name = sgqlc.types.Field(String, graphql_name="name")


class CloudDisableAccountIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("linked_account_id",)
    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )


class CloudDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "aws",
        "aws_govcloud",
        "azure",
        "cci_aws",
        "confluent",
        "fossa",
        "gcp",
    )
    aws = sgqlc.types.Field(CloudAwsDisableIntegrationsInput, graphql_name="aws")

    aws_govcloud = sgqlc.types.Field(
        CloudAwsGovcloudDisableIntegrationsInput, graphql_name="awsGovcloud"
    )

    azure = sgqlc.types.Field(CloudAzureDisableIntegrationsInput, graphql_name="azure")

    cci_aws = sgqlc.types.Field(
        CloudCciAwsDisableIntegrationsInput, graphql_name="cciAws"
    )

    confluent = sgqlc.types.Field(
        CloudConfluentDisableIntegrationsInput, graphql_name="confluent"
    )

    fossa = sgqlc.types.Field(
        "CloudFossaDisableIntegrationsInput", graphql_name="fossa"
    )

    gcp = sgqlc.types.Field("CloudGcpDisableIntegrationsInput", graphql_name="gcp")


class CloudDynamodbIntegrationInput(sgqlc.types.Input):
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

    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudEbsIntegrationInput(sgqlc.types.Input):
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

    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudEc2IntegrationInput(sgqlc.types.Input):
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

    duplicate_ec2_tags = sgqlc.types.Field(Boolean, graphql_name="duplicateEc2Tags")

    fetch_ip_addresses = sgqlc.types.Field(Boolean, graphql_name="fetchIpAddresses")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudEcsIntegrationInput(sgqlc.types.Input):
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

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudEfsIntegrationInput(sgqlc.types.Input):
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

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudElasticacheIntegrationInput(sgqlc.types.Input):
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

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudElasticbeanstalkIntegrationInput(sgqlc.types.Input):
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

    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudElasticsearchIntegrationInput(sgqlc.types.Input):
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

    fetch_nodes = sgqlc.types.Field(Boolean, graphql_name="fetchNodes")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudElbIntegrationInput(sgqlc.types.Input):
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

    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudEmrIntegrationInput(sgqlc.types.Input):
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

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudFossaDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("fossa_issues",)
    fossa_issues = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="fossaIssues",
    )


class CloudFossaIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("fossa_issues",)
    fossa_issues = sgqlc.types.Field(
        sgqlc.types.list_of("CloudFossaIssuesIntegrationInput"),
        graphql_name="fossaIssues",
    )


class CloudFossaIssuesIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudFossaLinkAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("api_key", "external_id", "name")
    api_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiKey"
    )

    external_id = sgqlc.types.Field(String, graphql_name="externalId")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class CloudFossaUpdateAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "api_key",
        "disabled",
        "external_id",
        "linked_account_id",
        "name",
    )
    api_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiKey"
    )

    disabled = sgqlc.types.Field(Boolean, graphql_name="disabled")

    external_id = sgqlc.types.Field(String, graphql_name="externalId")

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    name = sgqlc.types.Field(String, graphql_name="name")


class CloudGcpAiplatformIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpAlloydbIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpAppengineIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpBigqueryIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_table_metrics",
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    fetch_table_metrics = sgqlc.types.Field(Boolean, graphql_name="fetchTableMetrics")

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpBigtableIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpComposerIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpDataflowIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpDataprocIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpDatastoreIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "gcp_aiplatform",
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
    gcp_aiplatform = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpAiplatform",
    )

    gcp_alloydb = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpAlloydb",
    )

    gcp_appengine = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpAppengine",
    )

    gcp_bigquery = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpBigquery",
    )

    gcp_bigtable = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpBigtable",
    )

    gcp_composer = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpComposer",
    )

    gcp_dataflow = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpDataflow",
    )

    gcp_dataproc = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpDataproc",
    )

    gcp_datastore = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpDatastore",
    )

    gcp_firebasedatabase = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpFirebasedatabase",
    )

    gcp_firebasehosting = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpFirebasehosting",
    )

    gcp_firebasestorage = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpFirebasestorage",
    )

    gcp_firestore = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpFirestore",
    )

    gcp_functions = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpFunctions",
    )

    gcp_interconnect = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpInterconnect",
    )

    gcp_kubernetes = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpKubernetes",
    )

    gcp_loadbalancing = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpLoadbalancing",
    )

    gcp_memcache = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpMemcache",
    )

    gcp_pubsub = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpPubsub",
    )

    gcp_redis = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpRedis",
    )

    gcp_router = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpRouter",
    )

    gcp_run = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name="gcpRun"
    )

    gcp_spanner = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpSpanner",
    )

    gcp_sql = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name="gcpSql"
    )

    gcp_storage = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpStorage",
    )

    gcp_vms = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name="gcpVms"
    )

    gcp_vpcaccess = sgqlc.types.Field(
        sgqlc.types.list_of(CloudDisableAccountIntegrationInput),
        graphql_name="gcpVpcaccess",
    )


class CloudGcpFirebasedatabaseIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpFirebasehostingIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpFirebasestorageIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpFirestoreIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpFunctionsIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "gcp_aiplatform",
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
    gcp_aiplatform = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpAiplatformIntegrationInput),
        graphql_name="gcpAiplatform",
    )

    gcp_alloydb = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpAlloydbIntegrationInput), graphql_name="gcpAlloydb"
    )

    gcp_appengine = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpAppengineIntegrationInput),
        graphql_name="gcpAppengine",
    )

    gcp_bigquery = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpBigqueryIntegrationInput),
        graphql_name="gcpBigquery",
    )

    gcp_bigtable = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpBigtableIntegrationInput),
        graphql_name="gcpBigtable",
    )

    gcp_composer = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpComposerIntegrationInput),
        graphql_name="gcpComposer",
    )

    gcp_dataflow = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpDataflowIntegrationInput),
        graphql_name="gcpDataflow",
    )

    gcp_dataproc = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpDataprocIntegrationInput),
        graphql_name="gcpDataproc",
    )

    gcp_datastore = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpDatastoreIntegrationInput),
        graphql_name="gcpDatastore",
    )

    gcp_firebasedatabase = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpFirebasedatabaseIntegrationInput),
        graphql_name="gcpFirebasedatabase",
    )

    gcp_firebasehosting = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpFirebasehostingIntegrationInput),
        graphql_name="gcpFirebasehosting",
    )

    gcp_firebasestorage = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpFirebasestorageIntegrationInput),
        graphql_name="gcpFirebasestorage",
    )

    gcp_firestore = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpFirestoreIntegrationInput),
        graphql_name="gcpFirestore",
    )

    gcp_functions = sgqlc.types.Field(
        sgqlc.types.list_of(CloudGcpFunctionsIntegrationInput),
        graphql_name="gcpFunctions",
    )

    gcp_interconnect = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpInterconnectIntegrationInput"),
        graphql_name="gcpInterconnect",
    )

    gcp_kubernetes = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpKubernetesIntegrationInput"),
        graphql_name="gcpKubernetes",
    )

    gcp_loadbalancing = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpLoadbalancingIntegrationInput"),
        graphql_name="gcpLoadbalancing",
    )

    gcp_memcache = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpMemcacheIntegrationInput"),
        graphql_name="gcpMemcache",
    )

    gcp_pubsub = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpPubsubIntegrationInput"), graphql_name="gcpPubsub"
    )

    gcp_redis = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpRedisIntegrationInput"), graphql_name="gcpRedis"
    )

    gcp_router = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpRouterIntegrationInput"), graphql_name="gcpRouter"
    )

    gcp_run = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpRunIntegrationInput"), graphql_name="gcpRun"
    )

    gcp_spanner = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpSpannerIntegrationInput"),
        graphql_name="gcpSpanner",
    )

    gcp_sql = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpSqlIntegrationInput"), graphql_name="gcpSql"
    )

    gcp_storage = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpStorageIntegrationInput"),
        graphql_name="gcpStorage",
    )

    gcp_vms = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpVmsIntegrationInput"), graphql_name="gcpVms"
    )

    gcp_vpcaccess = sgqlc.types.Field(
        sgqlc.types.list_of("CloudGcpVpcaccessIntegrationInput"),
        graphql_name="gcpVpcaccess",
    )


class CloudGcpInterconnectIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpKubernetesIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpLinkAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "project_id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    project_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="projectId"
    )


class CloudGcpLoadbalancingIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpMemcacheIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpPubsubIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpRedisIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpRouterIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpRunIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpSpannerIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpSqlIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpStorageIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_tags",
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpUpdateAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("disabled", "linked_account_id", "name", "project_id")
    disabled = sgqlc.types.Field(Boolean, graphql_name="disabled")

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    project_id = sgqlc.types.Field(String, graphql_name="projectId")


class CloudGcpVmsIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpVpcaccessIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudHealthIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudIamIntegrationInput(sgqlc.types.Input):
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

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudIntegrationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "aws",
        "aws_govcloud",
        "azure",
        "cci_aws",
        "confluent",
        "fossa",
        "gcp",
    )
    aws = sgqlc.types.Field(CloudAwsIntegrationsInput, graphql_name="aws")

    aws_govcloud = sgqlc.types.Field(
        CloudAwsGovcloudIntegrationsInput, graphql_name="awsGovcloud"
    )

    azure = sgqlc.types.Field(CloudAzureIntegrationsInput, graphql_name="azure")

    cci_aws = sgqlc.types.Field(CloudCciAwsIntegrationsInput, graphql_name="cciAws")

    confluent = sgqlc.types.Field(
        CloudConfluentIntegrationsInput, graphql_name="confluent"
    )

    fossa = sgqlc.types.Field(CloudFossaIntegrationsInput, graphql_name="fossa")

    gcp = sgqlc.types.Field(CloudGcpIntegrationsInput, graphql_name="gcp")


class CloudIotIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudKinesisFirehoseIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudKinesisIntegrationInput(sgqlc.types.Input):
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

    fetch_shards = sgqlc.types.Field(Boolean, graphql_name="fetchShards")

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudLambdaIntegrationInput(sgqlc.types.Input):
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

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudLinkCloudAccountsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "aws",
        "aws_govcloud",
        "azure",
        "cci_aws",
        "confluent",
        "fossa",
        "gcp",
    )
    aws = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudAwsLinkAccountInput)),
        graphql_name="aws",
    )

    aws_govcloud = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudAwsGovCloudLinkAccountInput)),
        graphql_name="awsGovcloud",
    )

    azure = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudAzureLinkAccountInput)),
        graphql_name="azure",
    )

    cci_aws = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudCciAwsLinkAccountInput)),
        graphql_name="cciAws",
    )

    confluent = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudConfluentLinkAccountInput)),
        graphql_name="confluent",
    )

    fossa = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudFossaLinkAccountInput)),
        graphql_name="fossa",
    )

    gcp = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudGcpLinkAccountInput)),
        graphql_name="gcp",
    )


class CloudRdsIntegrationInput(sgqlc.types.Input):
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

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudRedshiftIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudRenameAccountsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("linked_account_id", "name")
    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class CloudRoute53IntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudS3IntegrationInput(sgqlc.types.Input):
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

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudSecurityHubIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudSesIntegrationInput(sgqlc.types.Input):
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

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudSnsIntegrationInput(sgqlc.types.Input):
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

    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudSqsIntegrationInput(sgqlc.types.Input):
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

    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )

    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    queue_prefixes = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="queuePrefixes"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CloudTrustedadvisorIntegrationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "inventory_polling_interval",
        "linked_account_id",
        "metrics_polling_interval",
    )
    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudUnlinkAccountsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("linked_account_id",)
    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )


class CloudUpdateCloudAccountsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("aws", "aws_govcloud", "azure", "confluent", "fossa", "gcp")
    aws = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudAwsUpdateAccountInput)),
        graphql_name="aws",
    )

    aws_govcloud = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudAwsGovCloudUpdateAccountInput)),
        graphql_name="awsGovcloud",
    )

    azure = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudAzureUpdateAccountInput)),
        graphql_name="azure",
    )

    confluent = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudConfluentUpdateAccountInput)),
        graphql_name="confluent",
    )

    fossa = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudFossaUpdateAccountInput)),
        graphql_name="fossa",
    )

    gcp = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CloudGcpUpdateAccountInput)),
        graphql_name="gcp",
    )


class CloudVpcIntegrationInput(sgqlc.types.Input):
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

    fetch_nat_gateway = sgqlc.types.Field(Boolean, graphql_name="fetchNatGateway")

    fetch_vpn = sgqlc.types.Field(Boolean, graphql_name="fetchVpn")

    inventory_polling_interval = sgqlc.types.Field(
        Int, graphql_name="inventoryPollingInterval"
    )

    linked_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="linkedAccountId"
    )

    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )

    tag_key = sgqlc.types.Field(String, graphql_name="tagKey")

    tag_value = sgqlc.types.Field(String, graphql_name="tagValue")


class CollaborationAssistantConfigInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "value")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class CustomRoleContainerInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    type = sgqlc.types.Field(String, graphql_name="type")


class DashboardAreaWidgetConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardBarWidgetConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardBillboardWidgetConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries", "thresholds")
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )

    thresholds = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("DashboardBillboardWidgetThresholdInput")
        ),
        graphql_name="thresholds",
    )


class DashboardBillboardWidgetThresholdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("alert_severity", "value")
    alert_severity = sgqlc.types.Field(
        DashboardAlertSeverity, graphql_name="alertSeverity"
    )

    value = sgqlc.types.Field(Float, graphql_name="value")


class DashboardInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "pages", "permissions", "variables")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    pages = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("DashboardPageInput"))
        ),
        graphql_name="pages",
    )

    permissions = sgqlc.types.Field(
        sgqlc.types.non_null(DashboardPermissions), graphql_name="permissions"
    )

    variables = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardVariableInput")),
        graphql_name="variables",
    )


class DashboardLineWidgetConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardLiveUrlAuthCreationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("factors",)
    factors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("DashboardLiveUrlAuthFactorInput"))
        ),
        graphql_name="factors",
    )


class DashboardLiveUrlAuthFactorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(
        sgqlc.types.non_null(DashboardLiveUrlAuthType), graphql_name="type"
    )


class DashboardLiveUrlAuthUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("factors",)
    factors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(DashboardLiveUrlAuthFactorInput))
        ),
        graphql_name="factors",
    )


class DashboardLiveUrlCreationPoliciesFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="accountIds"
    )


class DashboardLiveUrlOptionsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("ttl",)
    ttl = sgqlc.types.Field(Seconds, graphql_name="ttl")


class DashboardLiveUrlsFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("cursor", "entity_guid", "type", "uuid")
    cursor = sgqlc.types.Field(String, graphql_name="cursor")

    entity_guid = sgqlc.types.Field(EntityGuid, graphql_name="entityGuid")

    type = sgqlc.types.Field(DashboardLiveUrlType, graphql_name="type")

    uuid = sgqlc.types.Field(ID, graphql_name="uuid")


class DashboardMarkdownWidgetConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("text",)
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="text")


class DashboardPageInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "guid", "name", "widgets")
    description = sgqlc.types.Field(String, graphql_name="description")

    guid = sgqlc.types.Field(EntityGuid, graphql_name="guid")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    widgets = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetInput"))
        ),
        graphql_name="widgets",
    )


class DashboardPieWidgetConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardSnapshotUrlInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("time_window",)
    time_window = sgqlc.types.Field(
        "DashboardSnapshotUrlTimeWindowInput", graphql_name="timeWindow"
    )


class DashboardSnapshotUrlTimeWindowInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("begin_time", "duration", "end_time")
    begin_time = sgqlc.types.Field(EpochMilliseconds, graphql_name="beginTime")

    duration = sgqlc.types.Field(Milliseconds, graphql_name="duration")

    end_time = sgqlc.types.Field(EpochMilliseconds, graphql_name="endTime")


class DashboardTableWidgetConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetNrqlQueryInput")),
        graphql_name="nrqlQueries",
    )


class DashboardUpdateLiveUrlCreationPoliciesInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "live_url_creation_allowed")
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )

    live_url_creation_allowed = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="liveUrlCreationAllowed"
    )


class DashboardUpdatePageInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "widgets")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    widgets = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("DashboardWidgetInput"))
        ),
        graphql_name="widgets",
    )


class DashboardUpdateWidgetInput(sgqlc.types.Input):
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

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    layout = sgqlc.types.Field("DashboardWidgetLayoutInput", graphql_name="layout")

    linked_entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="linkedEntityGuids",
    )

    raw_configuration = sgqlc.types.Field(
        DashboardWidgetRawConfiguration, graphql_name="rawConfiguration"
    )

    title = sgqlc.types.Field(String, graphql_name="title")

    visualization = sgqlc.types.Field(
        "DashboardWidgetVisualizationInput", graphql_name="visualization"
    )


class DashboardVariableDefaultItemInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("value",)
    value = sgqlc.types.Field(
        sgqlc.types.non_null("DashboardVariableDefaultValueInput"), graphql_name="value"
    )


class DashboardVariableDefaultValueInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("string",)
    string = sgqlc.types.Field(String, graphql_name="string")


class DashboardVariableEnumItemInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("title", "value")
    title = sgqlc.types.Field(String, graphql_name="title")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class DashboardVariableInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "default_value",
        "default_values",
        "is_multi_selection",
        "items",
        "name",
        "nrql_query",
        "options",
        "replacement_strategy",
        "title",
        "type",
    )
    default_value = sgqlc.types.Field(
        DashboardVariableDefaultValueInput, graphql_name="defaultValue"
    )

    default_values = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(DashboardVariableDefaultItemInput)),
        graphql_name="defaultValues",
    )

    is_multi_selection = sgqlc.types.Field(Boolean, graphql_name="isMultiSelection")

    items = sgqlc.types.Field(
        sgqlc.types.list_of(DashboardVariableEnumItemInput), graphql_name="items"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    nrql_query = sgqlc.types.Field(
        "DashboardVariableNrqlQueryInput", graphql_name="nrqlQuery"
    )

    options = sgqlc.types.Field("DashboardVariableOptionsInput", graphql_name="options")

    replacement_strategy = sgqlc.types.Field(
        DashboardVariableReplacementStrategy, graphql_name="replacementStrategy"
    )

    title = sgqlc.types.Field(String, graphql_name="title")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(DashboardVariableType), graphql_name="type"
    )


class DashboardVariableNrqlQueryInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "query")
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )

    query = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="query")


class DashboardVariableOptionsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("excluded", "ignore_time_range", "show_apply_action")
    excluded = sgqlc.types.Field(Boolean, graphql_name="excluded")

    ignore_time_range = sgqlc.types.Field(Boolean, graphql_name="ignoreTimeRange")

    show_apply_action = sgqlc.types.Field(Boolean, graphql_name="showApplyAction")


class DashboardWidgetConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("area", "bar", "billboard", "line", "markdown", "pie", "table")
    area = sgqlc.types.Field(DashboardAreaWidgetConfigurationInput, graphql_name="area")

    bar = sgqlc.types.Field(DashboardBarWidgetConfigurationInput, graphql_name="bar")

    billboard = sgqlc.types.Field(
        DashboardBillboardWidgetConfigurationInput, graphql_name="billboard"
    )

    line = sgqlc.types.Field(DashboardLineWidgetConfigurationInput, graphql_name="line")

    markdown = sgqlc.types.Field(
        DashboardMarkdownWidgetConfigurationInput, graphql_name="markdown"
    )

    pie = sgqlc.types.Field(DashboardPieWidgetConfigurationInput, graphql_name="pie")

    table = sgqlc.types.Field(
        DashboardTableWidgetConfigurationInput, graphql_name="table"
    )


class DashboardWidgetInput(sgqlc.types.Input):
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

    id = sgqlc.types.Field(ID, graphql_name="id")

    layout = sgqlc.types.Field("DashboardWidgetLayoutInput", graphql_name="layout")

    linked_entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="linkedEntityGuids",
    )

    raw_configuration = sgqlc.types.Field(
        DashboardWidgetRawConfiguration, graphql_name="rawConfiguration"
    )

    title = sgqlc.types.Field(String, graphql_name="title")

    visualization = sgqlc.types.Field(
        "DashboardWidgetVisualizationInput", graphql_name="visualization"
    )


class DashboardWidgetLayoutInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("column", "height", "row", "width")
    column = sgqlc.types.Field(Int, graphql_name="column")

    height = sgqlc.types.Field(Int, graphql_name="height")

    row = sgqlc.types.Field(Int, graphql_name="row")

    width = sgqlc.types.Field(Int, graphql_name="width")


class DashboardWidgetNrqlQueryInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "query")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    query = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="query")


class DashboardWidgetVisualizationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(String, graphql_name="id")


class DataManagementAccountFeatureSettingInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled", "feature_setting", "locked")
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    feature_setting = sgqlc.types.Field(
        "DataManagementFeatureSettingLookup", graphql_name="featureSetting"
    )

    locked = sgqlc.types.Field(Boolean, graphql_name="locked")


class DataManagementAccountLimitInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("limit", "override_reason", "override_value", "qualifier")
    limit = sgqlc.types.Field(
        sgqlc.types.non_null("DataManagementLimitLookupInput"), graphql_name="limit"
    )

    override_reason = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="overrideReason"
    )

    override_value = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="overrideValue"
    )

    qualifier = sgqlc.types.Field(String, graphql_name="qualifier")


class DataManagementFeatureSettingLookup(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key",)
    key = sgqlc.types.Field(String, graphql_name="key")


class DataManagementLimitLookupInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name",)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class DataManagementRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("namespace", "retention_in_days")
    namespace = sgqlc.types.Field(String, graphql_name="namespace")

    retention_in_days = sgqlc.types.Field(Int, graphql_name="retentionInDays")


class DataSourceGapsGapsQuery(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "entity_guids", "gap_type_ids")
    account_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="accountIds"
    )

    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )

    gap_type_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(DataSourceGapsGapTypeIdentifier)),
        graphql_name="gapTypeIds",
    )


class DateTimeWindowInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("end_time", "start_time")
    end_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name="endTime")

    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(DateTime), graphql_name="startTime"
    )


class DomainTypeInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("domain", "type")
    domain = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="domain")

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")


class EdgeCreateSpanAttributeRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("action", "key", "key_operator", "value", "value_operator")
    action = sgqlc.types.Field(
        sgqlc.types.non_null(EdgeTraceFilterAction), graphql_name="action"
    )

    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    key_operator = sgqlc.types.Field(
        sgqlc.types.non_null(EdgeSpanAttributeKeyOperator), graphql_name="keyOperator"
    )

    value = sgqlc.types.Field(String, graphql_name="value")

    value_operator = sgqlc.types.Field(
        sgqlc.types.non_null(EdgeSpanAttributeValueOperator),
        graphql_name="valueOperator",
    )


class EdgeCreateTraceFilterRulesInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("span_attribute_rules",)
    span_attribute_rules = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EdgeCreateSpanAttributeRuleInput)),
        graphql_name="spanAttributeRules",
    )


class EdgeCreateTraceObserverInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("compliance_types", "monitoring", "name", "provider_region")
    compliance_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EdgeComplianceTypeCode)),
        graphql_name="complianceTypes",
    )

    monitoring = sgqlc.types.Field(Boolean, graphql_name="monitoring")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    provider_region = sgqlc.types.Field(
        sgqlc.types.non_null(EdgeProviderRegion), graphql_name="providerRegion"
    )


class EdgeDataSourceGroupInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("guids", "update_type")
    guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)), graphql_name="guids"
    )

    update_type = sgqlc.types.Field(
        sgqlc.types.non_null(EdgeDataSourceGroupUpdateType), graphql_name="updateType"
    )


class EdgeDeleteTraceFilterRulesInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("span_attribute_rule_ids",)
    span_attribute_rule_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)),
        graphql_name="spanAttributeRuleIds",
    )


class EdgeDeleteTraceObserverInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")


class EdgeRandomTraceFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("percent_kept",)
    percent_kept = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="percentKept"
    )


class EdgeUpdateTraceObserverInput(sgqlc.types.Input):
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

    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")

    monitoring = sgqlc.types.Field(Boolean, graphql_name="monitoring")

    name = sgqlc.types.Field(String, graphql_name="name")

    random_trace_filter_config = sgqlc.types.Field(
        EdgeRandomTraceFilterInput, graphql_name="randomTraceFilterConfig"
    )


class EntityGoldenContextInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account", "guid")
    account = sgqlc.types.Field(Int, graphql_name="account")

    guid = sgqlc.types.Field(EntityGuid, graphql_name="guid")


class EntityGoldenMetricInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("event_id", "facet", "from_", "name", "select", "title", "where")
    event_id = sgqlc.types.Field(String, graphql_name="eventId")

    facet = sgqlc.types.Field(String, graphql_name="facet")

    from_ = sgqlc.types.Field(String, graphql_name="from")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    select = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="select")

    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="title")

    where = sgqlc.types.Field(String, graphql_name="where")


class EntityGoldenNrqlTimeWindowInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("since", "until")
    since = sgqlc.types.Field(Nrql, graphql_name="since")

    until = sgqlc.types.Field(Nrql, graphql_name="until")


class EntityGoldenTagInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key",)
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class EntityManagementAiAgentEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "agents_id",
        "category",
        "description",
        "llm_config",
        "name",
        "prompt",
        "scope",
        "tags",
        "tools",
    )
    agents_id = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="agentsId"
    )

    category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="category")

    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )

    llm_config = sgqlc.types.Field(
        "EntityManagementLlmConfigCreateInput", graphql_name="llmConfig"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    prompt = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="prompt",
    )

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    tools = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("EntityManagementAiAgentToolConfigCreateInput")
        ),
        graphql_name="tools",
    )


class EntityManagementAiAgentEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "agents_id",
        "category",
        "description",
        "llm_config",
        "name",
        "prompt",
        "tags",
        "tools",
    )
    agents_id = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="agentsId"
    )

    category = sgqlc.types.Field(String, graphql_name="category")

    description = sgqlc.types.Field(String, graphql_name="description")

    llm_config = sgqlc.types.Field(
        "EntityManagementLlmConfigUpdateInput", graphql_name="llmConfig"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    prompt = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="prompt"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    tools = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("EntityManagementAiAgentToolConfigUpdateInput")
        ),
        graphql_name="tools",
    )


class EntityManagementAiAgentToolConfigCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("exclude_tools", "include_tools", "tool_id")
    exclude_tools = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="excludeTools"
    )

    include_tools = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="includeTools"
    )

    tool_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="toolId")


class EntityManagementAiAgentToolConfigUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("exclude_tools", "include_tools", "tool_id")
    exclude_tools = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="excludeTools"
    )

    include_tools = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="includeTools"
    )

    tool_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="toolId")


class EntityManagementAiToolEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "parameters", "scope", "tags", "url")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    parameters = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("EntityManagementAiToolParameterCreateInput")
        ),
        graphql_name="parameters",
    )

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class EntityManagementAiToolEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "parameters", "tags", "url")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(String, graphql_name="name")

    parameters = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("EntityManagementAiToolParameterUpdateInput")
        ),
        graphql_name="parameters",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    url = sgqlc.types.Field(String, graphql_name="url")


class EntityManagementAiToolParameterCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "type")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementAiToolParameterType), graphql_name="type"
    )


class EntityManagementAiToolParameterUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "type")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementAiToolParameterType), graphql_name="type"
    )


class EntityManagementAttributeCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class EntityManagementAttributeUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class EntityManagementCategoryScopeCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementCategoryScopeType), graphql_name="type"
    )


class EntityManagementCategoryScopeUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementCategoryScopeType), graphql_name="type"
    )


class EntityManagementCharacterTextSplitterOptionsCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("is_separator_regex", "separator")
    is_separator_regex = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isSeparatorRegex"
    )

    separator = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="separator"
    )


class EntityManagementCharacterTextSplitterOptionsUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("is_separator_regex", "separator")
    is_separator_regex = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isSeparatorRegex"
    )

    separator = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="separator"
    )


class EntityManagementCollectionElementsFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("collection_id",)
    collection_id = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementCollectionIdFilterArgument"),
        graphql_name="collectionId",
    )


class EntityManagementCollectionEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "scope", "tags")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementCollectionEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "tags")
    name = sgqlc.types.Field(String, graphql_name="name")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementCollectionIdFilterArgument(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class EntityManagementConfigCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attributes", "name")
    attributes = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityManagementAttributeCreateInput)),
        graphql_name="attributes",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class EntityManagementConfigUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attributes", "name")
    attributes = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityManagementAttributeUpdateInput)),
        graphql_name="attributes",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class EntityManagementConfluenceIntegrationCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "confluence_user_id",
        "name",
        "scope",
        "secret_key",
        "tags",
        "url",
    )
    confluence_user_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="confluenceUserId"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    secret_key = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="secretKey"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class EntityManagementConfluenceIntegrationUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("confluence_user_id", "name", "secret_key", "tags", "url")
    confluence_user_id = sgqlc.types.Field(String, graphql_name="confluenceUserId")

    name = sgqlc.types.Field(String, graphql_name="name")

    secret_key = sgqlc.types.Field(String, graphql_name="secretKey")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    url = sgqlc.types.Field(String, graphql_name="url")


class EntityManagementConfluenceRagSettingsEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "character_text_splitter_options",
        "chunk_overlap",
        "chunk_size",
        "confluence_integration_id",
        "confluence_query",
        "interval_seconds",
        "markdown_text_splitter_options",
        "name",
        "scope",
        "tags",
        "text_splitter_type",
        "token_text_splitter_options",
    )
    character_text_splitter_options = sgqlc.types.Field(
        EntityManagementCharacterTextSplitterOptionsCreateInput,
        graphql_name="characterTextSplitterOptions",
    )

    chunk_overlap = sgqlc.types.Field(Int, graphql_name="chunkOverlap")

    chunk_size = sgqlc.types.Field(Int, graphql_name="chunkSize")

    confluence_integration_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="confluenceIntegrationId"
    )

    confluence_query = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="confluenceQuery"
    )

    interval_seconds = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="intervalSeconds"
    )

    markdown_text_splitter_options = sgqlc.types.Field(
        "EntityManagementMarkdownTextSplitterOptionsCreateInput",
        graphql_name="markdownTextSplitterOptions",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    text_splitter_type = sgqlc.types.Field(
        EntityManagementTextSplitterType, graphql_name="textSplitterType"
    )

    token_text_splitter_options = sgqlc.types.Field(
        "EntityManagementTokenTextSplitterOptionsCreateInput",
        graphql_name="tokenTextSplitterOptions",
    )


class EntityManagementConfluenceRagSettingsEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "character_text_splitter_options",
        "chunk_overlap",
        "chunk_size",
        "confluence_integration_id",
        "confluence_query",
        "interval_seconds",
        "markdown_text_splitter_options",
        "name",
        "tags",
        "text_splitter_type",
        "token_text_splitter_options",
    )
    character_text_splitter_options = sgqlc.types.Field(
        EntityManagementCharacterTextSplitterOptionsUpdateInput,
        graphql_name="characterTextSplitterOptions",
    )

    chunk_overlap = sgqlc.types.Field(Int, graphql_name="chunkOverlap")

    chunk_size = sgqlc.types.Field(Int, graphql_name="chunkSize")

    confluence_integration_id = sgqlc.types.Field(
        ID, graphql_name="confluenceIntegrationId"
    )

    confluence_query = sgqlc.types.Field(String, graphql_name="confluenceQuery")

    interval_seconds = sgqlc.types.Field(Int, graphql_name="intervalSeconds")

    markdown_text_splitter_options = sgqlc.types.Field(
        "EntityManagementMarkdownTextSplitterOptionsUpdateInput",
        graphql_name="markdownTextSplitterOptions",
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    text_splitter_type = sgqlc.types.Field(
        EntityManagementTextSplitterType, graphql_name="textSplitterType"
    )

    token_text_splitter_options = sgqlc.types.Field(
        "EntityManagementTokenTextSplitterOptionsUpdateInput",
        graphql_name="tokenTextSplitterOptions",
    )


class EntityManagementDiscoverySettingsUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled", "tag_keys")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    tag_keys = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="tagKeys",
    )


class EntityManagementEntityReferenceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "scope")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    scope = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementEntityScope), graphql_name="scope"
    )


class EntityManagementExternalOwnerCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementExternalOwnerType), graphql_name="type"
    )


class EntityManagementExternalOwnerUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementExternalOwnerType), graphql_name="type"
    )


class EntityManagementGenericEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "tags")
    name = sgqlc.types.Field(String, graphql_name="name")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementGitRepositoryEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "closed_pull_request_count",
        "description",
        "external_created_at",
        "external_id",
        "external_last_deployed_at",
        "external_owner",
        "external_updated_at",
        "fork_count",
        "hosting_platform",
        "latest_release_version",
        "license",
        "locked_pull_request_count",
        "name",
        "open_pull_request_count",
        "primary_language",
        "scope",
        "tags",
        "url",
    )
    closed_pull_request_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="closedPullRequestCount"
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    external_created_at = sgqlc.types.Field(
        sgqlc.types.non_null(EpochMilliseconds), graphql_name="externalCreatedAt"
    )

    external_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="externalId"
    )

    external_last_deployed_at = sgqlc.types.Field(
        EpochMilliseconds, graphql_name="externalLastDeployedAt"
    )

    external_owner = sgqlc.types.Field(
        EntityManagementExternalOwnerCreateInput, graphql_name="externalOwner"
    )

    external_updated_at = sgqlc.types.Field(
        sgqlc.types.non_null(EpochMilliseconds), graphql_name="externalUpdatedAt"
    )

    fork_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="forkCount")

    hosting_platform = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementHostingPlatform),
        graphql_name="hostingPlatform",
    )

    latest_release_version = sgqlc.types.Field(
        String, graphql_name="latestReleaseVersion"
    )

    license = sgqlc.types.Field(
        "EntityManagementRepositoryLicenseCreateInput", graphql_name="license"
    )

    locked_pull_request_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="lockedPullRequestCount"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    open_pull_request_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="openPullRequestCount"
    )

    primary_language = sgqlc.types.Field(String, graphql_name="primaryLanguage")

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class EntityManagementGitRepositoryEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "closed_pull_request_count",
        "description",
        "external_created_at",
        "external_id",
        "external_last_deployed_at",
        "external_owner",
        "external_updated_at",
        "fork_count",
        "hosting_platform",
        "latest_release_version",
        "license",
        "locked_pull_request_count",
        "name",
        "open_pull_request_count",
        "primary_language",
        "tags",
        "url",
    )
    closed_pull_request_count = sgqlc.types.Field(
        Int, graphql_name="closedPullRequestCount"
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    external_created_at = sgqlc.types.Field(
        EpochMilliseconds, graphql_name="externalCreatedAt"
    )

    external_id = sgqlc.types.Field(String, graphql_name="externalId")

    external_last_deployed_at = sgqlc.types.Field(
        EpochMilliseconds, graphql_name="externalLastDeployedAt"
    )

    external_owner = sgqlc.types.Field(
        EntityManagementExternalOwnerUpdateInput, graphql_name="externalOwner"
    )

    external_updated_at = sgqlc.types.Field(
        EpochMilliseconds, graphql_name="externalUpdatedAt"
    )

    fork_count = sgqlc.types.Field(Int, graphql_name="forkCount")

    hosting_platform = sgqlc.types.Field(
        EntityManagementHostingPlatform, graphql_name="hostingPlatform"
    )

    latest_release_version = sgqlc.types.Field(
        String, graphql_name="latestReleaseVersion"
    )

    license = sgqlc.types.Field(
        "EntityManagementRepositoryLicenseUpdateInput", graphql_name="license"
    )

    locked_pull_request_count = sgqlc.types.Field(
        Int, graphql_name="lockedPullRequestCount"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    open_pull_request_count = sgqlc.types.Field(
        Int, graphql_name="openPullRequestCount"
    )

    primary_language = sgqlc.types.Field(String, graphql_name="primaryLanguage")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    url = sgqlc.types.Field(String, graphql_name="url")


class EntityManagementInboxIssueCategoryEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "category_scope",
        "category_type",
        "issue_type",
        "message_attributes",
        "name",
        "name_attributes",
        "scope",
        "tags",
    )
    category_scope = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementCategoryScopeCreateInput),
        graphql_name="categoryScope",
    )

    category_type = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="categoryType"
    )

    issue_type = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementIssueType), graphql_name="issueType"
    )

    message_attributes = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="messageAttributes"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    name_attributes = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name="nameAttributes"
    )

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementInboxIssueCategoryEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "category_scope",
        "category_type",
        "issue_type",
        "message_attributes",
        "name",
        "name_attributes",
        "tags",
    )
    category_scope = sgqlc.types.Field(
        EntityManagementCategoryScopeUpdateInput, graphql_name="categoryScope"
    )

    category_type = sgqlc.types.Field(String, graphql_name="categoryType")

    issue_type = sgqlc.types.Field(EntityManagementIssueType, graphql_name="issueType")

    message_attributes = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="messageAttributes"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    name_attributes = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="nameAttributes"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementLlmConfigCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("cache_seed", "temperature")
    cache_seed = sgqlc.types.Field(String, graphql_name="cacheSeed")

    temperature = sgqlc.types.Field(Float, graphql_name="temperature")


class EntityManagementLlmConfigUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("cache_seed", "temperature")
    cache_seed = sgqlc.types.Field(String, graphql_name="cacheSeed")

    temperature = sgqlc.types.Field(Float, graphql_name="temperature")


class EntityManagementMarkdownTextSplitterOptionsCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("headers_to_split_on", "return_each_line")
    headers_to_split_on = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(String)),
        graphql_name="headersToSplitOn",
    )

    return_each_line = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="returnEachLine"
    )


class EntityManagementMarkdownTextSplitterOptionsUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("headers_to_split_on", "return_each_line")
    headers_to_split_on = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(String)),
        graphql_name="headersToSplitOn",
    )

    return_each_line = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="returnEachLine"
    )


class EntityManagementNrqlRuleEngineCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("accounts", "join_accounts", "query")
    accounts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accounts",
    )

    join_accounts = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="joinAccounts"
    )

    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="query")


class EntityManagementNrqlRuleEngineUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("accounts", "join_accounts", "query")
    accounts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accounts",
    )

    join_accounts = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="joinAccounts"
    )

    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="query")


class EntityManagementPerformanceInboxSettingEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("config", "name", "scope", "tags")
    config = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityManagementConfigCreateInput)),
        graphql_name="config",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementPerformanceInboxSettingEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("config", "name", "tags")
    config = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityManagementConfigUpdateInput)),
        graphql_name="config",
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementPipelineCloudRuleEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "nrql", "scope", "tags")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    nrql = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="nrql")

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementPipelineCloudRuleEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "nrql", "tags")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(String, graphql_name="name")

    nrql = sgqlc.types.Field(Nrql, graphql_name="nrql")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementRagToolEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "scope", "tags")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    scope = sgqlc.types.Field(
        sgqlc.types.non_null("EntityManagementScopedReferenceInput"),
        graphql_name="scope",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementRagToolEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "tags")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(String, graphql_name="name")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementRelationshipCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("source", "tags", "target", "type")
    source = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementEntityReferenceInput),
        graphql_name="source",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )

    target = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementEntityReferenceInput),
        graphql_name="target",
    )

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")


class EntityManagementRelationshipUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("tags",)
    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementRepositoryLicenseCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "url")
    name = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementLicenseName), graphql_name="name"
    )

    url = sgqlc.types.Field(String, graphql_name="url")


class EntityManagementRepositoryLicenseUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "url")
    name = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementLicenseName), graphql_name="name"
    )

    url = sgqlc.types.Field(String, graphql_name="url")


class EntityManagementScheduleCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("cron_expression", "enabled", "period", "schedule_at")
    cron_expression = sgqlc.types.Field(String, graphql_name="cronExpression")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    period = sgqlc.types.Field(Int, graphql_name="period")

    schedule_at = sgqlc.types.Field(String, graphql_name="scheduleAt")


class EntityManagementScheduleUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("cron_expression", "enabled", "period", "schedule_at")
    cron_expression = sgqlc.types.Field(String, graphql_name="cronExpression")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    period = sgqlc.types.Field(Int, graphql_name="period")

    schedule_at = sgqlc.types.Field(String, graphql_name="scheduleAt")


class EntityManagementScopedReferenceInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementEntityScope), graphql_name="type"
    )


class EntityManagementScorecardEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "scope", "tags")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    scope = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementScopedReferenceInput), graphql_name="scope"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementScorecardEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "tags")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(String, graphql_name="name")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementScorecardRuleEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "enabled",
        "name",
        "nrql_engine",
        "schedule",
        "scope",
        "tags",
    )
    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    nrql_engine = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementNrqlRuleEngineCreateInput),
        graphql_name="nrqlEngine",
    )

    schedule = sgqlc.types.Field(
        EntityManagementScheduleCreateInput, graphql_name="schedule"
    )

    scope = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementScopedReferenceInput), graphql_name="scope"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementScorecardRuleEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "enabled",
        "name",
        "nrql_engine",
        "schedule",
        "tags",
    )
    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    name = sgqlc.types.Field(String, graphql_name="name")

    nrql_engine = sgqlc.types.Field(
        EntityManagementNrqlRuleEngineUpdateInput, graphql_name="nrqlEngine"
    )

    schedule = sgqlc.types.Field(
        EntityManagementScheduleUpdateInput, graphql_name="schedule"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntityManagementTagInput")),
        graphql_name="tags",
    )


class EntityManagementSyncGroupRuleConditionUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("type", "value")
    type = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementSyncGroupRuleConditionType),
        graphql_name="type",
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class EntityManagementSyncGroupRuleUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("conditions",)
    conditions = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(EntityManagementSyncGroupRuleConditionUpdateInput)
            )
        ),
        graphql_name="conditions",
    )


class EntityManagementSyncGroupsSettingsUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled", "rules")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    rules = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(EntityManagementSyncGroupRuleUpdateInput)
        ),
        graphql_name="rules",
    )


class EntityManagementTagInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "values")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    values = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="values",
    )


class EntityManagementTeamEntityCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "aliases",
        "description",
        "external_integration",
        "name",
        "resources",
        "scope",
        "tags",
    )
    aliases = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="aliases"
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    external_integration = sgqlc.types.Field(
        "EntityManagementTeamExternalIntegrationCreateInput",
        graphql_name="externalIntegration",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    resources = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("EntityManagementTeamResourceCreateInput")
        ),
        graphql_name="resources",
    )

    scope = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementScopedReferenceInput), graphql_name="scope"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityManagementTagInput)),
        graphql_name="tags",
    )


class EntityManagementTeamEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "aliases",
        "description",
        "external_integration",
        "name",
        "resources",
        "tags",
    )
    aliases = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="aliases"
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    external_integration = sgqlc.types.Field(
        "EntityManagementTeamExternalIntegrationUpdateInput",
        graphql_name="externalIntegration",
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    resources = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("EntityManagementTeamResourceUpdateInput")
        ),
        graphql_name="resources",
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityManagementTagInput)),
        graphql_name="tags",
    )


class EntityManagementTeamExternalIntegrationCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("external_id", "type")
    external_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="externalId")

    type = sgqlc.types.Field(
        EntityManagementTeamExternalIntegrationType, graphql_name="type"
    )


class EntityManagementTeamExternalIntegrationUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("external_id", "type")
    external_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="externalId")

    type = sgqlc.types.Field(
        EntityManagementTeamExternalIntegrationType, graphql_name="type"
    )


class EntityManagementTeamResourceCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("content", "title", "type")
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="content")

    title = sgqlc.types.Field(String, graphql_name="title")

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")


class EntityManagementTeamResourceUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("content", "title", "type")
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="content")

    title = sgqlc.types.Field(String, graphql_name="title")

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")


class EntityManagementTeamsOrganizationSettingsEntityUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("discovery", "name", "sync_groups", "tags")
    discovery = sgqlc.types.Field(
        EntityManagementDiscoverySettingsUpdateInput, graphql_name="discovery"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    sync_groups = sgqlc.types.Field(
        EntityManagementSyncGroupsSettingsUpdateInput, graphql_name="syncGroups"
    )

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityManagementTagInput)),
        graphql_name="tags",
    )


class EntityManagementTokenTextSplitterOptionsCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("encoding_name",)
    encoding_name = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementEncodingName), graphql_name="encodingName"
    )


class EntityManagementTokenTextSplitterOptionsUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("encoding_name",)
    encoding_name = sgqlc.types.Field(
        sgqlc.types.non_null(EntityManagementEncodingName), graphql_name="encodingName"
    )


class EntityRelationshipEdgeFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "entity_domain_types", "relationship_types")
    direction = sgqlc.types.Field(
        EntityRelationshipEdgeDirection, graphql_name="direction"
    )

    entity_domain_types = sgqlc.types.Field(
        "EntityRelationshipEntityDomainTypeFilter", graphql_name="entityDomainTypes"
    )

    relationship_types = sgqlc.types.Field(
        "EntityRelationshipEdgeTypeFilter", graphql_name="relationshipTypes"
    )


class EntityRelationshipEdgeTypeFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("exclude", "include")
    exclude = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityRelationshipEdgeType)),
        graphql_name="exclude",
    )

    include = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityRelationshipEdgeType)),
        graphql_name="include",
    )


class EntityRelationshipEntityDomainTypeFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("exclude", "include")
    exclude = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(DomainTypeInput)),
        graphql_name="exclude",
    )

    include = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(DomainTypeInput)),
        graphql_name="include",
    )


class EntityRelationshipFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("entity_type", "infrastructure_integration_type")
    entity_type = sgqlc.types.Field(
        sgqlc.types.list_of(EntityType), graphql_name="entityType"
    )

    infrastructure_integration_type = sgqlc.types.Field(
        sgqlc.types.list_of(EntityInfrastructureIntegrationType),
        graphql_name="infrastructureIntegrationType",
    )


class EntitySearchOptions(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("case_sensitive_tag_matching", "limit", "tag_filter")
    case_sensitive_tag_matching = sgqlc.types.Field(
        Boolean, graphql_name="caseSensitiveTagMatching"
    )

    limit = sgqlc.types.Field(Int, graphql_name="limit")

    tag_filter = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="tagFilter"
    )


class EntitySearchQueryBuilder(sgqlc.types.Input):
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

    alertable = sgqlc.types.Field(Boolean, graphql_name="alertable")

    domain = sgqlc.types.Field(EntitySearchQueryBuilderDomain, graphql_name="domain")

    infrastructure_integration_type = sgqlc.types.Field(
        EntityInfrastructureIntegrationType,
        graphql_name="infrastructureIntegrationType",
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    reporting = sgqlc.types.Field(Boolean, graphql_name="reporting")

    tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EntitySearchQueryBuilderTag")),
        graphql_name="tags",
    )

    type = sgqlc.types.Field(EntitySearchQueryBuilderType, graphql_name="type")


class EntitySearchQueryBuilderTag(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class ErrorsInboxAssignErrorGroupInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("user_email", "user_id")
    user_email = sgqlc.types.Field(String, graphql_name="userEmail")

    user_id = sgqlc.types.Field(Int, graphql_name="userId")


class ErrorsInboxAssignmentSearchFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("user_email", "user_id")
    user_email = sgqlc.types.Field(String, graphql_name="userEmail")

    user_id = sgqlc.types.Field(Int, graphql_name="userId")


class ErrorsInboxErrorEventInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("entity_guid", "event", "message", "name", "source")
    entity_guid = sgqlc.types.Field(
        sgqlc.types.non_null(EntityGuid), graphql_name="entityGuid"
    )

    event = sgqlc.types.Field(ErrorsInboxRawEvent, graphql_name="event")

    message = sgqlc.types.Field(String, graphql_name="message")

    name = sgqlc.types.Field(String, graphql_name="name")

    source = sgqlc.types.Field(ErrorsInboxEventSource, graphql_name="source")


class ErrorsInboxErrorGroupSearchFilterInput(sgqlc.types.Input):
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

    application_versions = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="applicationVersions",
    )

    assignment = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(ErrorsInboxAssignmentSearchFilterInput)
        ),
        graphql_name="assignment",
    )

    ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="ids"
    )

    is_assigned = sgqlc.types.Field(Boolean, graphql_name="isAssigned")

    states = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ErrorsInboxErrorGroupState)),
        graphql_name="states",
    )


class ErrorsInboxErrorGroupSortOrderInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "field")
    direction = sgqlc.types.Field(
        sgqlc.types.non_null(ErrorsInboxDirection), graphql_name="direction"
    )

    field = sgqlc.types.Field(
        sgqlc.types.non_null(ErrorsInboxErrorGroupSortOrderField), graphql_name="field"
    )


class ErrorsInboxResourceFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("types",)
    types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ErrorsInboxResourceType)),
        graphql_name="types",
    )


class ErrorsInboxStateVersionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("values",)
    values = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="values"
    )


class EventsToMetricsCreateRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "description", "name", "nrql")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    nrql = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="nrql")


class EventsToMetricsDeleteRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "rule_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    rule_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="ruleId")


class EventsToMetricsUpdateRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "enabled", "rule_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    rule_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="ruleId")


class InstallationInstallStatusInput(sgqlc.types.Input):
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

    deployed_by = sgqlc.types.Field(String, graphql_name="deployedBy")

    enabled_proxy = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="enabledProxy"
    )

    error = sgqlc.types.Field(
        sgqlc.types.non_null("InstallationStatusErrorInput"), graphql_name="error"
    )

    host_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="hostName")

    install_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="installId")

    install_library_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="installLibraryVersion"
    )

    is_unsupported = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isUnsupported"
    )

    kernel_arch = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="kernelArch"
    )

    kernel_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="kernelVersion"
    )

    log_file_path = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="logFilePath"
    )

    os = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="os")

    platform = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="platform")

    platform_family = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="platformFamily"
    )

    platform_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="platformVersion"
    )

    redirect_url = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="redirectUrl"
    )

    state = sgqlc.types.Field(
        sgqlc.types.non_null(InstallationInstallStateType), graphql_name="state"
    )

    targeted_install = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="targetedInstall"
    )

    timestamp = sgqlc.types.Field(EpochSeconds, graphql_name="timestamp")


class InstallationRecipeStatus(sgqlc.types.Input):
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

    complete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="complete")

    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )

    entity_guid = sgqlc.types.Field(
        sgqlc.types.non_null(EntityGuid), graphql_name="entityGuid"
    )

    error = sgqlc.types.Field(
        sgqlc.types.non_null("InstallationStatusErrorInput"), graphql_name="error"
    )

    host_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="hostName")

    install_id = sgqlc.types.Field(ID, graphql_name="installId")

    install_library_version = sgqlc.types.Field(
        SemVer, graphql_name="installLibraryVersion"
    )

    kernel_arch = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="kernelArch"
    )

    kernel_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="kernelVersion"
    )

    log_file_path = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="logFilePath"
    )

    metadata = sgqlc.types.Field(InstallationRawMetadata, graphql_name="metadata")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    os = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="os")

    platform = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="platform")

    platform_family = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="platformFamily"
    )

    platform_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="platformVersion"
    )

    redirect_url = sgqlc.types.Field(String, graphql_name="redirectUrl")

    status = sgqlc.types.Field(
        sgqlc.types.non_null(InstallationRecipeStatusType), graphql_name="status"
    )

    targeted_install = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="targetedInstall"
    )

    task_path = sgqlc.types.Field(String, graphql_name="taskPath")

    validation_duration_milliseconds = sgqlc.types.Field(
        sgqlc.types.non_null(EpochMilliseconds),
        graphql_name="validationDurationMilliseconds",
    )


class InstallationStatusErrorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("details", "message", "optimized_message")
    details = sgqlc.types.Field(String, graphql_name="details")

    message = sgqlc.types.Field(String, graphql_name="message")

    optimized_message = sgqlc.types.Field(String, graphql_name="optimizedMessage")


class LogConfigurationsCreateDataPartitionRuleInput(sgqlc.types.Input):
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

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    matching_criteria = sgqlc.types.Field(
        "LogConfigurationsDataPartitionRuleMatchingCriteriaInput",
        graphql_name="matchingCriteria",
    )

    nrql = sgqlc.types.Field(Nrql, graphql_name="nrql")

    retention_policy = sgqlc.types.Field(
        sgqlc.types.non_null(LogConfigurationsDataPartitionRuleRetentionPolicyType),
        graphql_name="retentionPolicy",
    )

    target_data_partition = sgqlc.types.Field(
        sgqlc.types.non_null(LogConfigurationsLogDataPartitionName),
        graphql_name="targetDataPartition",
    )


class LogConfigurationsCreateObfuscationActionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attributes", "expression_id", "method")
    attributes = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="attributes",
    )

    expression_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="expressionId"
    )

    method = sgqlc.types.Field(
        sgqlc.types.non_null(LogConfigurationsObfuscationMethod), graphql_name="method"
    )


class LogConfigurationsCreateObfuscationExpressionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "regex")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    regex = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="regex")


class LogConfigurationsCreateObfuscationRuleInput(sgqlc.types.Input):
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

    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    filter = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="filter")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class LogConfigurationsDataPartitionRuleMatchingCriteriaInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attribute_name", "matching_expression", "matching_method")
    attribute_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attributeName"
    )

    matching_expression = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="matchingExpression"
    )

    matching_method = sgqlc.types.Field(
        sgqlc.types.non_null(LogConfigurationsDataPartitionRuleMatchingOperator),
        graphql_name="matchingMethod",
    )


class LogConfigurationsParsingRuleConfiguration(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attribute", "description", "enabled", "grok", "lucene", "nrql")
    attribute = sgqlc.types.Field(String, graphql_name="attribute")

    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    grok = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="grok")

    lucene = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="lucene")

    nrql = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="nrql")


class LogConfigurationsPipelineConfigurationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "enrichment_disabled",
        "json_parsing_disabled",
        "obfuscation_disabled",
        "parsing_disabled",
        "patterns_enabled",
        "plugin_attributes_cleanup_enabled",
        "recursive_json_parsing_disabled",
        "transformation_disabled",
    )
    enrichment_disabled = sgqlc.types.Field(Boolean, graphql_name="enrichmentDisabled")

    json_parsing_disabled = sgqlc.types.Field(
        Boolean, graphql_name="jsonParsingDisabled"
    )

    obfuscation_disabled = sgqlc.types.Field(
        Boolean, graphql_name="obfuscationDisabled"
    )

    parsing_disabled = sgqlc.types.Field(Boolean, graphql_name="parsingDisabled")

    patterns_enabled = sgqlc.types.Field(Boolean, graphql_name="patternsEnabled")

    plugin_attributes_cleanup_enabled = sgqlc.types.Field(
        Boolean, graphql_name="pluginAttributesCleanupEnabled"
    )

    recursive_json_parsing_disabled = sgqlc.types.Field(
        Boolean, graphql_name="recursiveJsonParsingDisabled"
    )

    transformation_disabled = sgqlc.types.Field(
        Boolean, graphql_name="transformationDisabled"
    )


class LogConfigurationsUpdateDataPartitionRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "enabled", "id", "matching_criteria", "nrql")
    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    matching_criteria = sgqlc.types.Field(
        LogConfigurationsDataPartitionRuleMatchingCriteriaInput,
        graphql_name="matchingCriteria",
    )

    nrql = sgqlc.types.Field(Nrql, graphql_name="nrql")


class LogConfigurationsUpdateObfuscationActionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attributes", "expression_id", "method")
    attributes = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="attributes",
    )

    expression_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="expressionId"
    )

    method = sgqlc.types.Field(
        sgqlc.types.non_null(LogConfigurationsObfuscationMethod), graphql_name="method"
    )


class LogConfigurationsUpdateObfuscationExpressionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "id", "name", "regex")
    description = sgqlc.types.Field(String, graphql_name="description")

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    name = sgqlc.types.Field(String, graphql_name="name")

    regex = sgqlc.types.Field(String, graphql_name="regex")


class LogConfigurationsUpdateObfuscationRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("actions", "description", "enabled", "filter", "id", "name")
    actions = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(LogConfigurationsUpdateObfuscationActionInput)
        ),
        graphql_name="actions",
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")

    filter = sgqlc.types.Field(Nrql, graphql_name="filter")

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    name = sgqlc.types.Field(String, graphql_name="name")


class MachineLearningAddDocumentIndexConfiguration(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "character_text_splitter_options",
        "chunk_overlap",
        "chunk_size",
        "markdown_text_splitter_options",
        "text_splitter_type",
        "token_text_splitter_options",
    )
    character_text_splitter_options = sgqlc.types.Field(
        "MachineLearningCharacterTextSplitterOptionsInput",
        graphql_name="characterTextSplitterOptions",
    )

    chunk_overlap = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="chunkOverlap"
    )

    chunk_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="chunkSize")

    markdown_text_splitter_options = sgqlc.types.Field(
        "MachineLearningMarkdownTextSplitterOptionsInput",
        graphql_name="markdownTextSplitterOptions",
    )

    text_splitter_type = sgqlc.types.Field(
        MachineLearningTextSplitterType, graphql_name="textSplitterType"
    )

    token_text_splitter_options = sgqlc.types.Field(
        "MachineLearningTokenTextSplitterOptionsInput",
        graphql_name="tokenTextSplitterOptions",
    )


class MachineLearningCharacterTextSplitterOptionsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("is_separator_regex", "separator")
    is_separator_regex = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isSeparatorRegex"
    )

    separator = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="separator"
    )


class MachineLearningFilterBy(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "operator", "value")
    key = sgqlc.types.Field(
        sgqlc.types.non_null(MachineLearningFilterByKeys), graphql_name="key"
    )

    operator = sgqlc.types.Field(
        sgqlc.types.non_null(MachineLearningOperator), graphql_name="operator"
    )

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class MachineLearningIndexOptions(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("index_all", "knowledge_category")
    index_all = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="indexAll"
    )

    knowledge_category = sgqlc.types.Field(String, graphql_name="knowledgeCategory")


class MachineLearningMarkdownTextSplitterOptionsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("headers_to_split_on", "return_each_line")
    headers_to_split_on = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(String)),
        graphql_name="headersToSplitOn",
    )

    return_each_line = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="returnEachLine"
    )


class MachineLearningTokenTextSplitterOptionsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("encoding_name",)
    encoding_name = sgqlc.types.Field(
        sgqlc.types.non_null(MachineLearningEncodingName), graphql_name="encodingName"
    )


class MetricNormalizationCreateRuleInput(sgqlc.types.Input):
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

    application_guid = sgqlc.types.Field(EntityGuid, graphql_name="applicationGuid")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    eval_order = sgqlc.types.Field(Int, graphql_name="evalOrder")

    match_expression = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="matchExpression"
    )

    notes = sgqlc.types.Field(String, graphql_name="notes")

    replacement = sgqlc.types.Field(String, graphql_name="replacement")

    terminate_chain = sgqlc.types.Field(Boolean, graphql_name="terminateChain")


class MetricNormalizationEditRuleInput(sgqlc.types.Input):
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

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    eval_order = sgqlc.types.Field(Int, graphql_name="evalOrder")

    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")

    match_expression = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="matchExpression"
    )

    notes = sgqlc.types.Field(String, graphql_name="notes")

    replacement = sgqlc.types.Field(String, graphql_name="replacement")

    terminate_chain = sgqlc.types.Field(Boolean, graphql_name="terminateChain")


class MultiTenantAuthorizationGrantAuthenticationDomainIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="in"
    )


class MultiTenantAuthorizationGrantFilterInputExpression(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "authentication_domain_id",
        "grantee",
        "group_id",
        "id",
        "organization_id",
        "role_id",
        "scope_id",
        "scope_type",
        "scope_v2_type",
    )
    authentication_domain_id = sgqlc.types.Field(
        MultiTenantAuthorizationGrantAuthenticationDomainIdInputFilter,
        graphql_name="authenticationDomainId",
    )

    grantee = sgqlc.types.Field(
        "MultiTenantAuthorizationGranteeInputFilter", graphql_name="grantee"
    )

    group_id = sgqlc.types.Field(
        "MultiTenantAuthorizationGrantGroupIdInputFilter", graphql_name="groupId"
    )

    id = sgqlc.types.Field(
        "MultiTenantAuthorizationGrantIdInputFilter", graphql_name="id"
    )

    organization_id = sgqlc.types.Field(
        sgqlc.types.non_null("MultiTenantAuthorizationGrantOrganizationIdInputFilter"),
        graphql_name="organizationId",
    )

    role_id = sgqlc.types.Field(
        "MultiTenantAuthorizationGrantRoleIdInputFilter", graphql_name="roleId"
    )

    scope_id = sgqlc.types.Field(
        "MultiTenantAuthorizationGrantScopeIdInputFilter", graphql_name="scopeId"
    )

    scope_type = sgqlc.types.Field(
        "MultiTenantAuthorizationGrantScopeTypeInputFilter", graphql_name="scopeType"
    )

    scope_v2_type = sgqlc.types.Field(
        "MultiTenantAuthorizationGrantScopeTypeV2InputFilter",
        graphql_name="scopeV2Type",
    )


class MultiTenantAuthorizationGrantGroupIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="in"
    )


class MultiTenantAuthorizationGrantIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(Int, graphql_name="eq")


class MultiTenantAuthorizationGrantOrganizationIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class MultiTenantAuthorizationGrantRoleIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(Int, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="in"
    )


class MultiTenantAuthorizationGrantScopeIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(String, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="in"
    )


class MultiTenantAuthorizationGrantScopeTypeInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(MultiTenantAuthorizationGrantScopeEnum, graphql_name="eq")


class MultiTenantAuthorizationGrantScopeTypeV2InputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(String, graphql_name="eq")


class MultiTenantAuthorizationGrantSortInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(
        MultiTenantAuthorizationSortDirectionEnum, graphql_name="direction"
    )

    key = sgqlc.types.Field(
        sgqlc.types.non_null(MultiTenantAuthorizationGrantSortEnum), graphql_name="key"
    )


class MultiTenantAuthorizationGranteeIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="in"
    )


class MultiTenantAuthorizationGranteeInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("grantee_id", "grantee_type")
    grantee_id = sgqlc.types.Field(
        MultiTenantAuthorizationGranteeIdInputFilter, graphql_name="granteeId"
    )

    grantee_type = sgqlc.types.Field(
        "MultiTenantAuthorizationGranteeTypeInputFilter", graphql_name="granteeType"
    )


class MultiTenantAuthorizationGranteeTypeInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(MultiTenantAuthorizationGranteeTypeEnum, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(MultiTenantAuthorizationGranteeTypeEnum)
        ),
        graphql_name="in",
    )


class MultiTenantAuthorizationPermissionFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("role_id", "scope")
    role_id = sgqlc.types.Field(
        "MultiTenantAuthorizationPermissionFilterRoleIdInput", graphql_name="roleId"
    )

    scope = sgqlc.types.Field(
        "MultiTenantAuthorizationPermissionFilterScopeInput", graphql_name="scope"
    )


class MultiTenantAuthorizationPermissionFilterRoleIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(ID, graphql_name="eq")


class MultiTenantAuthorizationPermissionFilterScopeInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(String, graphql_name="eq")


class MultiTenantAuthorizationRoleFilterInputExpression(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "group_id",
        "id",
        "name",
        "organization_id",
        "scope",
        "scope_v2",
        "type",
    )
    group_id = sgqlc.types.Field(
        "MultiTenantAuthorizationRoleGroupIdInputFilter", graphql_name="groupId"
    )

    id = sgqlc.types.Field(
        "MultiTenantAuthorizationRoleIdInputFilter", graphql_name="id"
    )

    name = sgqlc.types.Field(
        "MultiTenantAuthorizationRoleNameInputFilter", graphql_name="name"
    )

    organization_id = sgqlc.types.Field(
        sgqlc.types.non_null("MultiTenantAuthorizationRoleOrganizationIdInputFilter"),
        graphql_name="organizationId",
    )

    scope = sgqlc.types.Field(
        "MultiTenantAuthorizationRoleScopeInputFilter", graphql_name="scope"
    )

    scope_v2 = sgqlc.types.Field(
        "MultiTenantAuthorizationRoleScopeV2InputFilter", graphql_name="scopeV2"
    )

    type = sgqlc.types.Field(
        "MultiTenantAuthorizationRoleTypeInputFilter", graphql_name="type"
    )


class MultiTenantAuthorizationRoleGroupIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="in"
    )


class MultiTenantAuthorizationRoleIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(Int, graphql_name="eq")


class MultiTenantAuthorizationRoleNameInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class MultiTenantAuthorizationRoleOrganizationIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class MultiTenantAuthorizationRoleScopeInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(MultiTenantAuthorizationRoleScopeEnum, graphql_name="eq")


class MultiTenantAuthorizationRoleScopeV2InputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(String, graphql_name="eq")


class MultiTenantAuthorizationRoleSortInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(
        MultiTenantAuthorizationSortDirectionEnum, graphql_name="direction"
    )

    key = sgqlc.types.Field(
        sgqlc.types.non_null(MultiTenantAuthorizationRoleSortEnum), graphql_name="key"
    )


class MultiTenantAuthorizationRoleTypeInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(MultiTenantAuthorizationRoleTypeEnum, graphql_name="eq")


class MultiTenantIdentityAllowsCapabilityInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("in_",)
    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(MultiTenantIdentityCapability)),
        graphql_name="in",
    )


class MultiTenantIdentityAuthenticationDomainIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(ID, graphql_name="eq")


class MultiTenantIdentityEmailVerificationStateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("pending",)
    pending = sgqlc.types.Field(Boolean, graphql_name="pending")


class MultiTenantIdentityGroupFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "allows_capability",
        "authentication_domain_id",
        "id",
        "members",
        "name",
        "organization_id",
    )
    allows_capability = sgqlc.types.Field(
        MultiTenantIdentityAllowsCapabilityInput, graphql_name="allowsCapability"
    )

    authentication_domain_id = sgqlc.types.Field(
        MultiTenantIdentityAuthenticationDomainIdInput,
        graphql_name="authenticationDomainId",
    )

    id = sgqlc.types.Field("MultiTenantIdentityGroupIdInput", graphql_name="id")

    members = sgqlc.types.Field(
        "MultiTenantIdentityGroupMemberIdInput", graphql_name="members"
    )

    name = sgqlc.types.Field("MultiTenantIdentityGroupNameInput", graphql_name="name")

    organization_id = sgqlc.types.Field(
        sgqlc.types.non_null("MultiTenantIdentityOrganizationIdInput"),
        graphql_name="organizationId",
    )


class MultiTenantIdentityGroupIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(ID, graphql_name="eq")


class MultiTenantIdentityGroupMemberIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "excludes")
    contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="contains"
    )

    excludes = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="excludes"
    )


class MultiTenantIdentityGroupNameInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class MultiTenantIdentityGroupSortInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(
        MultiTenantIdentitySortDirection, graphql_name="direction"
    )

    key = sgqlc.types.Field(MultiTenantIdentitySortKeyEnum, graphql_name="key")


class MultiTenantIdentityGroupUserFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field("MultiTenantIdentityUserIdInput", graphql_name="id")


class MultiTenantIdentityOrganizationIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class MultiTenantIdentityPendingUpgradeRequestInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("exists",)
    exists = sgqlc.types.Field(Boolean, graphql_name="exists")


class MultiTenantIdentityUserEmailInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class MultiTenantIdentityUserFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "authentication_domain_id",
        "email",
        "email_verification_state",
        "group_id",
        "id",
        "name",
        "pending_upgrade_request",
    )
    authentication_domain_id = sgqlc.types.Field(
        sgqlc.types.non_null(MultiTenantIdentityAuthenticationDomainIdInput),
        graphql_name="authenticationDomainId",
    )

    email = sgqlc.types.Field(MultiTenantIdentityUserEmailInput, graphql_name="email")

    email_verification_state = sgqlc.types.Field(
        MultiTenantIdentityEmailVerificationStateInput,
        graphql_name="emailVerificationState",
    )

    group_id = sgqlc.types.Field(
        "MultiTenantIdentityUserGroupIdInput", graphql_name="groupId"
    )

    id = sgqlc.types.Field("MultiTenantIdentityUserIdInput", graphql_name="id")

    name = sgqlc.types.Field("MultiTenantIdentityUserNameInput", graphql_name="name")

    pending_upgrade_request = sgqlc.types.Field(
        MultiTenantIdentityPendingUpgradeRequestInput,
        graphql_name="pendingUpgradeRequest",
    )


class MultiTenantIdentityUserGroupIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_", "not_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="in"
    )

    not_ = sgqlc.types.Field(
        "MultiTenantIdentityUserNotGroupIdInput", graphql_name="not"
    )


class MultiTenantIdentityUserIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="in"
    )


class MultiTenantIdentityUserNameInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class MultiTenantIdentityUserNotGroupIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class MultiTenantIdentityUserSortInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(
        MultiTenantIdentitySortDirection, graphql_name="direction"
    )

    key = sgqlc.types.Field(MultiTenantIdentityUserSortKey, graphql_name="key")


class NerdStorageScopeInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")

    name = sgqlc.types.Field(
        sgqlc.types.non_null(NerdStorageScope), graphql_name="name"
    )


class NerdStorageVaultScope(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("actor",)
    actor = sgqlc.types.Field(NerdStorageVaultActorScope, graphql_name="actor")


class NerdStorageVaultWriteSecretInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(sgqlc.types.non_null(SecureValue), graphql_name="value")


class NerdpackAllowListInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name="accountIds"
    )


class NerdpackCreationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("owner_account",)
    owner_account = sgqlc.types.Field(Int, graphql_name="ownerAccount")


class NerdpackDataFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "subscription_model", "tag")
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")

    subscription_model = sgqlc.types.Field(
        NerdpackSubscriptionModel, graphql_name="subscriptionModel"
    )

    tag = sgqlc.types.Field(NerdpackTagName, graphql_name="tag")


class NerdpackOverrideVersionRules(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("nerdpack_id", "tag", "version")
    nerdpack_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="nerdpackId")

    tag = sgqlc.types.Field(NerdpackTagName, graphql_name="tag")

    version = sgqlc.types.Field(SemVer, graphql_name="version")


class NerdpackRemoveVersionTagInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("tag",)
    tag = sgqlc.types.Field(NerdpackTagName, graphql_name="tag")


class NerdpackSubscribeAccountsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "tag")
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )

    tag = sgqlc.types.Field(sgqlc.types.non_null(NerdpackTagName), graphql_name="tag")


class NerdpackTagVersionInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("tag", "version")
    tag = sgqlc.types.Field(NerdpackTagName, graphql_name="tag")

    version = sgqlc.types.Field(SemVer, graphql_name="version")


class NerdpackUnsubscribeAccountsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )


class NerdpackVersionFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("fallback", "tag", "tags", "version")
    fallback = sgqlc.types.Field(NerdpackVersionFilterFallback, graphql_name="fallback")

    tag = sgqlc.types.Field(NerdpackTagName, graphql_name="tag")

    tags = sgqlc.types.Field(sgqlc.types.list_of(NerdpackTagName), graphql_name="tags")

    version = sgqlc.types.Field(SemVer, graphql_name="version")


class Nr1CatalogCommunityContactChannelInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogEmailContactChannelInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("address",)
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="address")


class Nr1CatalogIssuesContactChannelInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogSearchFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "categories",
        "category",
        "components",
        "keywords",
        "recipe_names",
        "types",
    )
    categories = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="categories"
    )

    category = sgqlc.types.Field(String, graphql_name="category")

    components = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogSearchComponentType)),
        graphql_name="components",
    )

    keywords = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="keywords"
    )

    recipe_names = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="recipeNames"
    )

    types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogSearchResultType)),
        graphql_name="types",
    )


class Nr1CatalogSubmitMetadataInput(sgqlc.types.Input):
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

    category_terms = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="categoryTerms"
    )

    details = sgqlc.types.Field(String, graphql_name="details")

    documentation = sgqlc.types.Field(String, graphql_name="documentation")

    keywords = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="keywords"
    )

    repository = sgqlc.types.Field(String, graphql_name="repository")

    support = sgqlc.types.Field("Nr1CatalogSupportInput", graphql_name="support")

    tagline = sgqlc.types.Field(String, graphql_name="tagline")

    version = sgqlc.types.Field(sgqlc.types.non_null(SemVer), graphql_name="version")

    whats_new = sgqlc.types.Field(String, graphql_name="whatsNew")


class Nr1CatalogSupportInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("community", "email", "issues")
    community = sgqlc.types.Field(
        Nr1CatalogCommunityContactChannelInput, graphql_name="community"
    )

    email = sgqlc.types.Field(Nr1CatalogEmailContactChannelInput, graphql_name="email")

    issues = sgqlc.types.Field(
        Nr1CatalogIssuesContactChannelInput, graphql_name="issues"
    )


class NrqlDropRulesCreateDropRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("action", "description", "nrql")
    action = sgqlc.types.Field(
        sgqlc.types.non_null(NrqlDropRulesAction), graphql_name="action"
    )

    description = sgqlc.types.Field(String, graphql_name="description")

    nrql = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="nrql")


class NrqlQueryOptions(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("event_namespaces",)
    event_namespaces = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="eventNamespaces",
    )


class OrganizationAccountFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "name", "organization_id", "sharing_mode", "status")
    id = sgqlc.types.Field("OrganizationAccountIdFilterInput", graphql_name="id")

    name = sgqlc.types.Field("OrganizationAccountNameFilterInput", graphql_name="name")

    organization_id = sgqlc.types.Field(
        sgqlc.types.non_null("OrganizationAccountOrganizationIdFilterInput"),
        graphql_name="organizationId",
    )

    sharing_mode = sgqlc.types.Field(
        "OrganizationAccountSharingModeFilterInput", graphql_name="sharingMode"
    )

    status = sgqlc.types.Field(
        "OrganizationAccountStatusFilterInput", graphql_name="status"
    )


class OrganizationAccountIdFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(Int, graphql_name="eq")


class OrganizationAccountIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="eq")


class OrganizationAccountNameFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains",)
    contains = sgqlc.types.Field(String, graphql_name="contains")


class OrganizationAccountOrganizationIdFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class OrganizationAccountShareFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "target_id")
    account_id = sgqlc.types.Field(
        sgqlc.types.non_null(OrganizationAccountIdInput), graphql_name="accountId"
    )

    target_id = sgqlc.types.Field("OrganizationTargetIdInput", graphql_name="targetId")


class OrganizationAccountShareSortInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(
        OrganizationAccountShareSortDirectionEnum, graphql_name="direction"
    )

    key = sgqlc.types.Field(OrganizationAccountShareSortKeyEnum, graphql_name="key")


class OrganizationAccountSharingModeFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(OrganizationSharingMode, graphql_name="eq")


class OrganizationAccountSortInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(
        OrganizationAccountSortDirectionEnum, graphql_name="direction"
    )

    key = sgqlc.types.Field(OrganizationAccountSortKeyEnum, graphql_name="key")


class OrganizationAccountStatusFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(OrganizationAccountStatus, graphql_name="eq")


class OrganizationAuthenticationDomainFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "name", "organization_id")
    id = sgqlc.types.Field("OrganizationIdInput", graphql_name="id")

    name = sgqlc.types.Field("OrganizationNameInput", graphql_name="name")

    organization_id = sgqlc.types.Field(
        sgqlc.types.non_null("OrganizationOrganizationIdInput"),
        graphql_name="organizationId",
    )


class OrganizationAuthenticationDomainSortInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(
        OrganizationSortDirectionEnum, graphql_name="direction"
    )

    key = sgqlc.types.Field(OrganizationSortKeyEnum, graphql_name="key")


class OrganizationContractCustomerIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(String, graphql_name="eq")


class OrganizationContractOrganizationIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(ID, graphql_name="eq")


class OrganizationCreateOrganizationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name",)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class OrganizationCreateSharedAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "limiting_role_id",
        "name",
        "target_organization_id",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    limiting_role_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="limitingRoleId"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    target_organization_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="targetOrganizationId"
    )


class OrganizationCustomerContractFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("customer_id", "organization_id")
    customer_id = sgqlc.types.Field(
        OrganizationContractCustomerIdInputFilter, graphql_name="customerId"
    )

    organization_id = sgqlc.types.Field(
        OrganizationContractOrganizationIdInputFilter, graphql_name="organizationId"
    )


class OrganizationCustomerOrganizationFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "authentication_domain_id",
        "customer_id",
        "id",
        "name",
    )
    account_id = sgqlc.types.Field(
        "OrganizationOrganizationAccountIdInputFilter", graphql_name="accountId"
    )

    authentication_domain_id = sgqlc.types.Field(
        "OrganizationOrganizationAuthenticationDomainIdInputFilter",
        graphql_name="authenticationDomainId",
    )

    customer_id = sgqlc.types.Field(
        "OrganizationOrganizationCustomerIdInputFilter", graphql_name="customerId"
    )

    id = sgqlc.types.Field("OrganizationOrganizationIdInputFilter", graphql_name="id")

    name = sgqlc.types.Field(
        "OrganizationOrganizationNameInputFilter", graphql_name="name"
    )


class OrganizationIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(ID, graphql_name="eq")


class OrganizationMembersOrganizationMemberAuthenticationDomainIdFilter(
    sgqlc.types.Input
):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class OrganizationMembersOrganizationMemberFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("authentication_domain_id", "organization_id", "search", "type")
    authentication_domain_id = sgqlc.types.Field(
        OrganizationMembersOrganizationMemberAuthenticationDomainIdFilter,
        graphql_name="authenticationDomainId",
    )

    organization_id = sgqlc.types.Field(
        sgqlc.types.non_null(
            "OrganizationMembersOrganizationMemberOrganizationIdFilter"
        ),
        graphql_name="organizationId",
    )

    search = sgqlc.types.Field(
        "OrganizationMembersOrganizationMemberSearchFilter", graphql_name="search"
    )

    type = sgqlc.types.Field(
        "OrganizationMembersOrganizationMemberTypeFilter", graphql_name="type"
    )


class OrganizationMembersOrganizationMemberOrganizationIdFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class OrganizationMembersOrganizationMemberSearchFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains",)
    contains = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="contains")


class OrganizationMembersOrganizationMemberTypeFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("in_",)
    in_ = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(OrganizationMembersOrganizationMemberType)
            )
        ),
        graphql_name="in",
    )


class OrganizationNameInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class OrganizationNewManagedAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "region_code")
    name = sgqlc.types.Field(String, graphql_name="name")

    region_code = sgqlc.types.Field(
        OrganizationRegionCodeEnum, graphql_name="regionCode"
    )


class OrganizationOrganizationAccountIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(Int, graphql_name="eq")


class OrganizationOrganizationAuthenticationDomainIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(ID, graphql_name="eq")


class OrganizationOrganizationCreateAsyncResultFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("customer_id", "job_id", "status")
    customer_id = sgqlc.types.Field(
        "OrganizationOrganizationCreateJobCustomerIdInput", graphql_name="customerId"
    )

    job_id = sgqlc.types.Field(
        "OrganizationOrganizationCreateJobIdInput", graphql_name="jobId"
    )

    status = sgqlc.types.Field(
        "OrganizationOrganizationCreateJobStatusInput", graphql_name="status"
    )


class OrganizationOrganizationCreateJobCustomerIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(String, graphql_name="eq")


class OrganizationOrganizationCreateJobIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="in"
    )


class OrganizationOrganizationCreateJobStatusInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(
        OrganizationOrganizationCreateJobStatusEnum, graphql_name="eq"
    )

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(OrganizationOrganizationCreateJobStatusEnum)
        ),
        graphql_name="in",
    )


class OrganizationOrganizationCustomerIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(String, graphql_name="eq")


class OrganizationOrganizationGroupFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "name", "organization_id")
    id = sgqlc.types.Field(
        "OrganizationOrganizationGroupIdInputFilter", graphql_name="id"
    )

    name = sgqlc.types.Field(
        "OrganizationOrganizationGroupNameInputFilter", graphql_name="name"
    )

    organization_id = sgqlc.types.Field(
        "OrganizationOrganizationGroupOrganizationIdInputFilter",
        graphql_name="organizationId",
    )


class OrganizationOrganizationGroupIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class OrganizationOrganizationGroupNameInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class OrganizationOrganizationGroupOrganizationIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class OrganizationOrganizationIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class OrganizationOrganizationIdInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(ID, graphql_name="eq")


class OrganizationOrganizationNameInputFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class OrganizationProvisioningProductInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "name", "units_of_measure")
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")

    name = sgqlc.types.Field(String, graphql_name="name")

    units_of_measure = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("OrganizationProvisioningUnitOfMeasureInput")
        ),
        graphql_name="unitsOfMeasure",
    )


class OrganizationProvisioningUnitOfMeasureInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("quantity", "unit")
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="quantity")

    unit = sgqlc.types.Field(
        sgqlc.types.non_null(OrganizationProvisioningUnit), graphql_name="unit"
    )


class OrganizationRevokeSharedAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")


class OrganizationSharedAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "limiting_role_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    limiting_role_id = sgqlc.types.Field(Int, graphql_name="limitingRoleId")


class OrganizationTargetIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(ID, graphql_name="eq")


class OrganizationUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class OrganizationUpdateSharedAccountInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "limiting_role_id")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")

    limiting_role_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="limitingRoleId"
    )


class QueryHistoryQueryHistoryOptionsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("limit",)
    limit = sgqlc.types.Field(Int, graphql_name="limit")


class ReferenceEntityCreateRepositoryInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "name", "url")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class SecretsManagementBooleanFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(Boolean, graphql_name="eq")


class SecretsManagementScope(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(SecretsManagementScopeType), graphql_name="type"
    )


class SecretsManagementScopeFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(
        sgqlc.types.non_null(SecretsManagementScope), graphql_name="eq"
    )


class SecretsManagementSecretsCollectionFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("deleted", "namespace", "scope")
    deleted = sgqlc.types.Field(SecretsManagementBooleanFilter, graphql_name="deleted")

    namespace = sgqlc.types.Field(
        "SecretsManagementStringFilter", graphql_name="namespace"
    )

    scope = sgqlc.types.Field(
        sgqlc.types.non_null(SecretsManagementScopeFilter), graphql_name="scope"
    )


class SecretsManagementSecretsCollectionSort(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(
        sgqlc.types.non_null(SecretsManagementSortDirection), graphql_name="direction"
    )

    key = sgqlc.types.Field(
        sgqlc.types.non_null(SecretsManagementSortKey), graphql_name="key"
    )


class SecretsManagementStringFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(String, graphql_name="eq")


class SecretsManagementTagInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class ServiceLevelEventsCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_id", "bad_events", "good_events", "valid_events")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")

    bad_events = sgqlc.types.Field(
        "ServiceLevelEventsQueryCreateInput", graphql_name="badEvents"
    )

    good_events = sgqlc.types.Field(
        "ServiceLevelEventsQueryCreateInput", graphql_name="goodEvents"
    )

    valid_events = sgqlc.types.Field(
        sgqlc.types.non_null("ServiceLevelEventsQueryCreateInput"),
        graphql_name="validEvents",
    )


class ServiceLevelEventsQueryCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("from_", "select", "where")
    from_ = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="from")

    select = sgqlc.types.Field(
        "ServiceLevelEventsQuerySelectCreateInput", graphql_name="select"
    )

    where = sgqlc.types.Field(Nrql, graphql_name="where")


class ServiceLevelEventsQuerySelectCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attribute", "function", "threshold")
    attribute = sgqlc.types.Field(String, graphql_name="attribute")

    function = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelEventsQuerySelectFunction),
        graphql_name="function",
    )

    threshold = sgqlc.types.Field(Float, graphql_name="threshold")


class ServiceLevelEventsQuerySelectUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attribute", "function", "threshold")
    attribute = sgqlc.types.Field(String, graphql_name="attribute")

    function = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelEventsQuerySelectFunction),
        graphql_name="function",
    )

    threshold = sgqlc.types.Field(Float, graphql_name="threshold")


class ServiceLevelEventsQueryUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("from_", "select", "where")
    from_ = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="from")

    select = sgqlc.types.Field(
        ServiceLevelEventsQuerySelectUpdateInput, graphql_name="select"
    )

    where = sgqlc.types.Field(Nrql, graphql_name="where")


class ServiceLevelEventsUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("bad_events", "good_events", "valid_events")
    bad_events = sgqlc.types.Field(
        ServiceLevelEventsQueryUpdateInput, graphql_name="badEvents"
    )

    good_events = sgqlc.types.Field(
        ServiceLevelEventsQueryUpdateInput, graphql_name="goodEvents"
    )

    valid_events = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelEventsQueryUpdateInput),
        graphql_name="validEvents",
    )


class ServiceLevelIndicatorCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "events", "name", "objectives", "slug")
    description = sgqlc.types.Field(String, graphql_name="description")

    events = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelEventsCreateInput), graphql_name="events"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    objectives = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("ServiceLevelObjectiveCreateInput")),
        graphql_name="objectives",
    )

    slug = sgqlc.types.Field(String, graphql_name="slug")


class ServiceLevelIndicatorUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "events", "name", "objectives")
    description = sgqlc.types.Field(String, graphql_name="description")

    events = sgqlc.types.Field(ServiceLevelEventsUpdateInput, graphql_name="events")

    name = sgqlc.types.Field(String, graphql_name="name")

    objectives = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("ServiceLevelObjectiveUpdateInput")),
        graphql_name="objectives",
    )


class ServiceLevelObjectiveCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "target", "time_window")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(String, graphql_name="name")

    target = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="target")

    time_window = sgqlc.types.Field(
        sgqlc.types.non_null("ServiceLevelObjectiveTimeWindowCreateInput"),
        graphql_name="timeWindow",
    )


class ServiceLevelObjectiveRollingTimeWindowCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("count", "unit")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")

    unit = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelObjectiveRollingTimeWindowUnit),
        graphql_name="unit",
    )


class ServiceLevelObjectiveRollingTimeWindowUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("count", "unit")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")

    unit = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelObjectiveRollingTimeWindowUnit),
        graphql_name="unit",
    )


class ServiceLevelObjectiveTimeWindowCreateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("rolling",)
    rolling = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelObjectiveRollingTimeWindowCreateInput),
        graphql_name="rolling",
    )


class ServiceLevelObjectiveTimeWindowUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("rolling",)
    rolling = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelObjectiveRollingTimeWindowUpdateInput),
        graphql_name="rolling",
    )


class ServiceLevelObjectiveUpdateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "target", "time_window")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(String, graphql_name="name")

    target = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="target")

    time_window = sgqlc.types.Field(
        sgqlc.types.non_null(ServiceLevelObjectiveTimeWindowUpdateInput),
        graphql_name="timeWindow",
    )


class SessionsClientTypeFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(SessionsClientType, graphql_name="eq")


class SessionsSessionFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("client_type",)
    client_type = sgqlc.types.Field(SessionsClientTypeFilter, graphql_name="clientType")


class SortCriterionWithDirection(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("attribute", "direction", "tag")
    attribute = sgqlc.types.Field(EntitySearchSortCriteria, graphql_name="attribute")

    direction = sgqlc.types.Field(SortBy, graphql_name="direction")

    tag = sgqlc.types.Field(String, graphql_name="tag")


class StreamingExportAwsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("aws_account_id", "delivery_stream_name", "region", "role")
    aws_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="awsAccountId"
    )

    delivery_stream_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="deliveryStreamName"
    )

    region = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="region")

    role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="role")


class StreamingExportAzureInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("event_hub_connection_string", "event_hub_name")
    event_hub_connection_string = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="eventHubConnectionString"
    )

    event_hub_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="eventHubName"
    )


class StreamingExportGcpInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("gcp_project_id", "pubsub_topic_id")
    gcp_project_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="gcpProjectId"
    )

    pubsub_topic_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="pubsubTopicId"
    )


class StreamingExportRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "nrql", "payload_compression")
    description = sgqlc.types.Field(String, graphql_name="description")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    nrql = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="nrql")

    payload_compression = sgqlc.types.Field(
        StreamingExportPayloadCompression, graphql_name="payloadCompression"
    )


class SyntheticsCreateBrokenLinksMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "locations",
        "name",
        "period",
        "runtime",
        "status",
        "tags",
        "uri",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    locations = sgqlc.types.Field(
        sgqlc.types.non_null("SyntheticsLocationsInput"), graphql_name="locations"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    period = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorPeriod), graphql_name="period"
    )

    runtime = sgqlc.types.Field(
        "SyntheticsExtendedTypeMonitorRuntimeInput", graphql_name="runtime"
    )

    status = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorStatus), graphql_name="status"
    )

    tags = sgqlc.types.Field(sgqlc.types.list_of("SyntheticsTag"), graphql_name="tags")

    uri = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="uri")


class SyntheticsCreateCertCheckMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "domain",
        "locations",
        "name",
        "number_days_to_fail_before_cert_expires",
        "period",
        "runtime",
        "status",
        "tags",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    domain = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="domain")

    locations = sgqlc.types.Field(
        sgqlc.types.non_null("SyntheticsLocationsInput"), graphql_name="locations"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    number_days_to_fail_before_cert_expires = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="numberDaysToFailBeforeCertExpires"
    )

    period = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorPeriod), graphql_name="period"
    )

    runtime = sgqlc.types.Field(
        "SyntheticsExtendedTypeMonitorRuntimeInput", graphql_name="runtime"
    )

    status = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorStatus), graphql_name="status"
    )

    tags = sgqlc.types.Field(sgqlc.types.list_of("SyntheticsTag"), graphql_name="tags")


class SyntheticsCreateScriptApiMonitorInput(sgqlc.types.Input):
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

    locations = sgqlc.types.Field(
        sgqlc.types.non_null("SyntheticsScriptedMonitorLocationsInput"),
        graphql_name="locations",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    period = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorPeriod), graphql_name="period"
    )

    runtime = sgqlc.types.Field("SyntheticsRuntimeInput", graphql_name="runtime")

    script = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="script")

    status = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorStatus), graphql_name="status"
    )

    tags = sgqlc.types.Field(sgqlc.types.list_of("SyntheticsTag"), graphql_name="tags")


class SyntheticsCreateScriptBrowserMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "browsers",
        "devices",
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

    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    browsers = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsBrowser), graphql_name="browsers"
    )

    devices = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsDevice), graphql_name="devices"
    )

    locations = sgqlc.types.Field(
        sgqlc.types.non_null("SyntheticsScriptedMonitorLocationsInput"),
        graphql_name="locations",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    period = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorPeriod), graphql_name="period"
    )

    runtime = sgqlc.types.Field("SyntheticsRuntimeInput", graphql_name="runtime")

    script = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="script")

    status = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorStatus), graphql_name="status"
    )

    tags = sgqlc.types.Field(sgqlc.types.list_of("SyntheticsTag"), graphql_name="tags")


class SyntheticsCreateSimpleBrowserMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "browsers",
        "devices",
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

    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    browsers = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsBrowser), graphql_name="browsers"
    )

    devices = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsDevice), graphql_name="devices"
    )

    locations = sgqlc.types.Field(
        sgqlc.types.non_null("SyntheticsLocationsInput"), graphql_name="locations"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    period = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorPeriod), graphql_name="period"
    )

    runtime = sgqlc.types.Field("SyntheticsRuntimeInput", graphql_name="runtime")

    status = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorStatus), graphql_name="status"
    )

    tags = sgqlc.types.Field(sgqlc.types.list_of("SyntheticsTag"), graphql_name="tags")

    uri = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="uri")


class SyntheticsCreateSimpleMonitorInput(sgqlc.types.Input):
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

    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    locations = sgqlc.types.Field(
        sgqlc.types.non_null("SyntheticsLocationsInput"), graphql_name="locations"
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    period = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorPeriod), graphql_name="period"
    )

    status = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorStatus), graphql_name="status"
    )

    tags = sgqlc.types.Field(sgqlc.types.list_of("SyntheticsTag"), graphql_name="tags")

    uri = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="uri")


class SyntheticsCreateStepMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "browsers",
        "devices",
        "locations",
        "name",
        "period",
        "runtime",
        "status",
        "steps",
        "tags",
    )
    advanced_options = sgqlc.types.Field(
        "SyntheticsStepMonitorAdvancedOptionsInput", graphql_name="advancedOptions"
    )

    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    browsers = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsBrowser), graphql_name="browsers"
    )

    devices = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsDevice), graphql_name="devices"
    )

    locations = sgqlc.types.Field(
        sgqlc.types.non_null("SyntheticsScriptedMonitorLocationsInput"),
        graphql_name="locations",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    period = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorPeriod), graphql_name="period"
    )

    runtime = sgqlc.types.Field(
        "SyntheticsExtendedTypeMonitorRuntimeInput", graphql_name="runtime"
    )

    status = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorStatus), graphql_name="status"
    )

    steps = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("SyntheticsStepInput"))
        ),
        graphql_name="steps",
    )

    tags = sgqlc.types.Field(sgqlc.types.list_of("SyntheticsTag"), graphql_name="tags")


class SyntheticsCustomHeaderInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name", "value")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class SyntheticsDateWindowEndConfig(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("on_date", "on_repeat")
    on_date = sgqlc.types.Field(Date, graphql_name="onDate")

    on_repeat = sgqlc.types.Field(Int, graphql_name="onRepeat")


class SyntheticsDaysOfWeek(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("ordinal_day_of_month", "week_day")
    ordinal_day_of_month = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorDowntimeDayOfMonthOrdinal),
        graphql_name="ordinalDayOfMonth",
    )

    week_day = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsMonitorDowntimeWeekDays), graphql_name="weekDay"
    )


class SyntheticsDeviceEmulationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("device_orientation", "device_type")
    device_orientation = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsDeviceOrientation),
        graphql_name="deviceOrientation",
    )

    device_type = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsDeviceType), graphql_name="deviceType"
    )


class SyntheticsExtendedTypeMonitorRuntimeInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("runtime_type", "runtime_type_version")
    runtime_type = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="runtimeType"
    )

    runtime_type_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="runtimeTypeVersion"
    )


class SyntheticsLocationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("private", "public")
    private = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="private")

    public = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="public")


class SyntheticsMonitorDowntimeDailyConfig(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("end_repeat", "end_time", "start_time", "timezone")
    end_repeat = sgqlc.types.Field(
        SyntheticsDateWindowEndConfig, graphql_name="endRepeat"
    )

    end_time = sgqlc.types.Field(NaiveDateTime, graphql_name="endTime")

    start_time = sgqlc.types.Field(NaiveDateTime, graphql_name="startTime")

    timezone = sgqlc.types.Field(String, graphql_name="timezone")


class SyntheticsMonitorDowntimeMonthlyConfig(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("end_repeat", "end_time", "frequency", "start_time", "timezone")
    end_repeat = sgqlc.types.Field(
        SyntheticsDateWindowEndConfig, graphql_name="endRepeat"
    )

    end_time = sgqlc.types.Field(NaiveDateTime, graphql_name="endTime")

    frequency = sgqlc.types.Field(
        "SyntheticsMonitorDowntimeMonthlyFrequency", graphql_name="frequency"
    )

    start_time = sgqlc.types.Field(NaiveDateTime, graphql_name="startTime")

    timezone = sgqlc.types.Field(String, graphql_name="timezone")


class SyntheticsMonitorDowntimeMonthlyFrequency(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("days_of_month", "days_of_week")
    days_of_month = sgqlc.types.Field(
        sgqlc.types.list_of(Int), graphql_name="daysOfMonth"
    )

    days_of_week = sgqlc.types.Field(SyntheticsDaysOfWeek, graphql_name="daysOfWeek")


class SyntheticsMonitorDowntimeOnceConfig(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("end_time", "start_time", "timezone")
    end_time = sgqlc.types.Field(NaiveDateTime, graphql_name="endTime")

    start_time = sgqlc.types.Field(NaiveDateTime, graphql_name="startTime")

    timezone = sgqlc.types.Field(String, graphql_name="timezone")


class SyntheticsMonitorDowntimeWeeklyConfig(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "end_repeat",
        "end_time",
        "maintenance_days",
        "start_time",
        "timezone",
    )
    end_repeat = sgqlc.types.Field(
        SyntheticsDateWindowEndConfig, graphql_name="endRepeat"
    )

    end_time = sgqlc.types.Field(NaiveDateTime, graphql_name="endTime")

    maintenance_days = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsMonitorDowntimeWeekDays),
        graphql_name="maintenanceDays",
    )

    start_time = sgqlc.types.Field(NaiveDateTime, graphql_name="startTime")

    timezone = sgqlc.types.Field(String, graphql_name="timezone")


class SyntheticsPrivateLocationInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("guid", "vse_password")
    guid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="guid")

    vse_password = sgqlc.types.Field(SecureValue, graphql_name="vsePassword")


class SyntheticsRuntimeInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("runtime_type", "runtime_type_version", "script_language")
    runtime_type = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="runtimeType"
    )

    runtime_type_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="runtimeTypeVersion"
    )

    script_language = sgqlc.types.Field(String, graphql_name="scriptLanguage")


class SyntheticsScriptBrowserMonitorAdvancedOptionsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("device_emulation", "enable_screenshot_on_failure_and_script")
    device_emulation = sgqlc.types.Field(
        SyntheticsDeviceEmulationInput, graphql_name="deviceEmulation"
    )

    enable_screenshot_on_failure_and_script = sgqlc.types.Field(
        Boolean, graphql_name="enableScreenshotOnFailureAndScript"
    )


class SyntheticsScriptedMonitorLocationsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("private", "public")
    private = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(SyntheticsPrivateLocationInput)),
        graphql_name="private",
    )

    public = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="public"
    )


class SyntheticsSimpleBrowserMonitorAdvancedOptionsInput(sgqlc.types.Input):
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

    device_emulation = sgqlc.types.Field(
        SyntheticsDeviceEmulationInput, graphql_name="deviceEmulation"
    )

    enable_screenshot_on_failure_and_script = sgqlc.types.Field(
        Boolean, graphql_name="enableScreenshotOnFailureAndScript"
    )

    response_validation_text = sgqlc.types.Field(
        String, graphql_name="responseValidationText"
    )

    use_tls_validation = sgqlc.types.Field(Boolean, graphql_name="useTlsValidation")


class SyntheticsSimpleMonitorAdvancedOptionsInput(sgqlc.types.Input):
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

    redirect_is_failure = sgqlc.types.Field(Boolean, graphql_name="redirectIsFailure")

    response_validation_text = sgqlc.types.Field(
        String, graphql_name="responseValidationText"
    )

    should_bypass_head_request = sgqlc.types.Field(
        Boolean, graphql_name="shouldBypassHeadRequest"
    )

    use_tls_validation = sgqlc.types.Field(Boolean, graphql_name="useTlsValidation")


class SyntheticsStepInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("ordinal", "type", "values")
    ordinal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="ordinal")

    type = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsStepType), graphql_name="type"
    )

    values = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="values"
    )


class SyntheticsStepMonitorAdvancedOptionsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enable_screenshot_on_failure_and_script",)
    enable_screenshot_on_failure_and_script = sgqlc.types.Field(
        Boolean, graphql_name="enableScreenshotOnFailureAndScript"
    )


class SyntheticsTag(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "values")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    values = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name="values"
    )


class SyntheticsUpdateBrokenLinksMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "locations",
        "name",
        "period",
        "runtime",
        "status",
        "tags",
        "uri",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    locations = sgqlc.types.Field(SyntheticsLocationsInput, graphql_name="locations")

    name = sgqlc.types.Field(String, graphql_name="name")

    period = sgqlc.types.Field(SyntheticsMonitorPeriod, graphql_name="period")

    runtime = sgqlc.types.Field(
        SyntheticsExtendedTypeMonitorRuntimeInput, graphql_name="runtime"
    )

    status = sgqlc.types.Field(SyntheticsMonitorStatus, graphql_name="status")

    tags = sgqlc.types.Field(sgqlc.types.list_of(SyntheticsTag), graphql_name="tags")

    uri = sgqlc.types.Field(String, graphql_name="uri")


class SyntheticsUpdateCertCheckMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "domain",
        "locations",
        "name",
        "number_days_to_fail_before_cert_expires",
        "period",
        "runtime",
        "status",
        "tags",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    domain = sgqlc.types.Field(String, graphql_name="domain")

    locations = sgqlc.types.Field(SyntheticsLocationsInput, graphql_name="locations")

    name = sgqlc.types.Field(String, graphql_name="name")

    number_days_to_fail_before_cert_expires = sgqlc.types.Field(
        Int, graphql_name="numberDaysToFailBeforeCertExpires"
    )

    period = sgqlc.types.Field(SyntheticsMonitorPeriod, graphql_name="period")

    runtime = sgqlc.types.Field(
        SyntheticsExtendedTypeMonitorRuntimeInput, graphql_name="runtime"
    )

    status = sgqlc.types.Field(SyntheticsMonitorStatus, graphql_name="status")

    tags = sgqlc.types.Field(sgqlc.types.list_of(SyntheticsTag), graphql_name="tags")


class SyntheticsUpdateScriptApiMonitorInput(sgqlc.types.Input):
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

    locations = sgqlc.types.Field(
        SyntheticsScriptedMonitorLocationsInput, graphql_name="locations"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    period = sgqlc.types.Field(SyntheticsMonitorPeriod, graphql_name="period")

    runtime = sgqlc.types.Field(SyntheticsRuntimeInput, graphql_name="runtime")

    script = sgqlc.types.Field(String, graphql_name="script")

    status = sgqlc.types.Field(SyntheticsMonitorStatus, graphql_name="status")

    tags = sgqlc.types.Field(sgqlc.types.list_of(SyntheticsTag), graphql_name="tags")


class SyntheticsUpdateScriptBrowserMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "browsers",
        "devices",
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

    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    browsers = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsBrowser), graphql_name="browsers"
    )

    devices = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsDevice), graphql_name="devices"
    )

    locations = sgqlc.types.Field(
        SyntheticsScriptedMonitorLocationsInput, graphql_name="locations"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    period = sgqlc.types.Field(SyntheticsMonitorPeriod, graphql_name="period")

    runtime = sgqlc.types.Field(SyntheticsRuntimeInput, graphql_name="runtime")

    script = sgqlc.types.Field(String, graphql_name="script")

    status = sgqlc.types.Field(SyntheticsMonitorStatus, graphql_name="status")

    tags = sgqlc.types.Field(sgqlc.types.list_of(SyntheticsTag), graphql_name="tags")


class SyntheticsUpdateSimpleBrowserMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "browsers",
        "devices",
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

    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    browsers = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsBrowser), graphql_name="browsers"
    )

    devices = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsDevice), graphql_name="devices"
    )

    locations = sgqlc.types.Field(SyntheticsLocationsInput, graphql_name="locations")

    name = sgqlc.types.Field(String, graphql_name="name")

    period = sgqlc.types.Field(SyntheticsMonitorPeriod, graphql_name="period")

    runtime = sgqlc.types.Field(SyntheticsRuntimeInput, graphql_name="runtime")

    status = sgqlc.types.Field(SyntheticsMonitorStatus, graphql_name="status")

    tags = sgqlc.types.Field(sgqlc.types.list_of(SyntheticsTag), graphql_name="tags")

    uri = sgqlc.types.Field(String, graphql_name="uri")


class SyntheticsUpdateSimpleMonitorInput(sgqlc.types.Input):
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

    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    locations = sgqlc.types.Field(SyntheticsLocationsInput, graphql_name="locations")

    name = sgqlc.types.Field(String, graphql_name="name")

    period = sgqlc.types.Field(SyntheticsMonitorPeriod, graphql_name="period")

    status = sgqlc.types.Field(SyntheticsMonitorStatus, graphql_name="status")

    tags = sgqlc.types.Field(sgqlc.types.list_of(SyntheticsTag), graphql_name="tags")

    uri = sgqlc.types.Field(String, graphql_name="uri")


class SyntheticsUpdateStepMonitorInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "apdex_target",
        "browsers",
        "devices",
        "locations",
        "name",
        "period",
        "runtime",
        "status",
        "steps",
        "tags",
    )
    advanced_options = sgqlc.types.Field(
        SyntheticsStepMonitorAdvancedOptionsInput, graphql_name="advancedOptions"
    )

    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")

    browsers = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsBrowser), graphql_name="browsers"
    )

    devices = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsDevice), graphql_name="devices"
    )

    locations = sgqlc.types.Field(
        SyntheticsScriptedMonitorLocationsInput, graphql_name="locations"
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    period = sgqlc.types.Field(SyntheticsMonitorPeriod, graphql_name="period")

    runtime = sgqlc.types.Field(
        SyntheticsExtendedTypeMonitorRuntimeInput, graphql_name="runtime"
    )

    status = sgqlc.types.Field(SyntheticsMonitorStatus, graphql_name="status")

    steps = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsStepInput), graphql_name="steps"
    )

    tags = sgqlc.types.Field(sgqlc.types.list_of(SyntheticsTag), graphql_name="tags")


class SystemIdentityClientIdFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(ID, graphql_name="eq")


class SystemIdentityGroupFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "name", "organization_id")
    id = sgqlc.types.Field("SystemIdentityGroupIdFilter", graphql_name="id")

    name = sgqlc.types.Field("SystemIdentityGroupNameFilter", graphql_name="name")

    organization_id = sgqlc.types.Field(
        sgqlc.types.non_null("SystemIdentityOrganizationIdFilter"),
        graphql_name="organizationId",
    )


class SystemIdentityGroupIdFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(String, graphql_name="eq")

    in_ = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="in")


class SystemIdentityGroupNameFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class SystemIdentityIdentityFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("client_id", "id", "name", "organization_id")
    client_id = sgqlc.types.Field(SystemIdentityClientIdFilter, graphql_name="clientId")

    id = sgqlc.types.Field("SystemIdentityIdentityIdFilter", graphql_name="id")

    name = sgqlc.types.Field("SystemIdentityNameFilter", graphql_name="name")

    organization_id = sgqlc.types.Field(
        sgqlc.types.non_null("SystemIdentityOrganizationIdFilter"),
        graphql_name="organizationId",
    )


class SystemIdentityIdentityIdFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="in")


class SystemIdentityIdentitySort(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("field",)
    field = sgqlc.types.Field("SystemIdentityIdentitySortField", graphql_name="field")


class SystemIdentityIdentitySortField(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(SystemIdentitySortOrder, graphql_name="direction")

    key = sgqlc.types.Field(SystemIdentityIdentitySortFieldKey, graphql_name="key")


class SystemIdentityNameFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class SystemIdentityOrganizationIdFilter(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="eq")


class TaggingTagInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "values")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    values = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="values")


class TaggingTagValueInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="value")


class TimeWindowInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("end_time", "start_time")
    end_time = sgqlc.types.Field(
        sgqlc.types.non_null(EpochMilliseconds), graphql_name="endTime"
    )

    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(EpochMilliseconds), graphql_name="startTime"
    )


class UserManagementCreateGroup(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("authentication_domain_id", "display_name")
    authentication_domain_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="authenticationDomainId"
    )

    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )


class UserManagementCreateUser(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("authentication_domain_id", "email", "name", "user_type")
    authentication_domain_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="authenticationDomainId"
    )

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="email")

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    user_type = sgqlc.types.Field(
        UserManagementRequestedTierName, graphql_name="userType"
    )


class UserManagementDeleteGroup(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")


class UserManagementDeleteUser(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class UserManagementDisplayNameInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class UserManagementEmailInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class UserManagementEmailVerificationStateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("pending",)
    pending = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="pending")


class UserManagementGroupFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("display_name", "id")
    display_name = sgqlc.types.Field(
        UserManagementDisplayNameInput, graphql_name="displayName"
    )

    id = sgqlc.types.Field("UserManagementGroupIdInput", graphql_name="id")


class UserManagementGroupIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="in"
    )


class UserManagementGroupSortInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("direction", "key")
    direction = sgqlc.types.Field(UserManagementSortDirection, graphql_name="direction")

    key = sgqlc.types.Field(UserManagementGroupSortKey, graphql_name="key")


class UserManagementNameInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("contains", "eq")
    contains = sgqlc.types.Field(String, graphql_name="contains")

    eq = sgqlc.types.Field(String, graphql_name="eq")


class UserManagementPendingUpgradeRequestInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("exists",)
    exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="exists")


class UserManagementTypeInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq",)
    eq = sgqlc.types.Field(
        sgqlc.types.non_null(UserManagementTypeEnum), graphql_name="eq"
    )


class UserManagementUpdateGroup(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("display_name", "id")
    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class UserManagementUpdateUser(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("email", "id", "name", "time_zone", "user_type")
    email = sgqlc.types.Field(String, graphql_name="email")

    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")

    name = sgqlc.types.Field(String, graphql_name="name")

    time_zone = sgqlc.types.Field(String, graphql_name="timeZone")

    user_type = sgqlc.types.Field(
        UserManagementRequestedTierName, graphql_name="userType"
    )


class UserManagementUserFilterInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = (
        "email",
        "email_verification_state",
        "id",
        "name",
        "pending_upgrade_request",
        "type",
    )
    email = sgqlc.types.Field(UserManagementEmailInput, graphql_name="email")

    email_verification_state = sgqlc.types.Field(
        UserManagementEmailVerificationStateInput, graphql_name="emailVerificationState"
    )

    id = sgqlc.types.Field("UserManagementUserIdInput", graphql_name="id")

    name = sgqlc.types.Field(UserManagementNameInput, graphql_name="name")

    pending_upgrade_request = sgqlc.types.Field(
        UserManagementPendingUpgradeRequestInput, graphql_name="pendingUpgradeRequest"
    )

    type = sgqlc.types.Field(UserManagementTypeInput, graphql_name="type")


class UserManagementUserIdInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("eq", "in_")
    eq = sgqlc.types.Field(ID, graphql_name="eq")

    in_ = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="in"
    )


class UserManagementUsersGroupsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("group_ids", "user_ids")
    group_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))),
        graphql_name="groupIds",
    )

    user_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))),
        graphql_name="userIds",
    )


class UsersUserSearchQuery(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("scope",)
    scope = sgqlc.types.Field("UsersUserSearchScope", graphql_name="scope")


class UsersUserSearchScope(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("email", "name", "search", "user_ids")
    email = sgqlc.types.Field(String, graphql_name="email")

    name = sgqlc.types.Field(String, graphql_name="name")

    search = sgqlc.types.Field(String, graphql_name="search")

    user_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="userIds"
    )


class WhatsNewContentSearchQuery(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("content_type", "unread_only")
    content_type = sgqlc.types.Field(WhatsNewContentType, graphql_name="contentType")

    unread_only = sgqlc.types.Field(Boolean, graphql_name="unreadOnly")


class WorkloadAutomaticStatusInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled", "remaining_entities_rule", "rules")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    remaining_entities_rule = sgqlc.types.Field(
        "WorkloadRemainingEntitiesRuleInput", graphql_name="remainingEntitiesRule"
    )

    rules = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("WorkloadRegularRuleInput")),
        graphql_name="rules",
    )


class WorkloadCreateInput(sgqlc.types.Input):
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

    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )

    entity_search_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("WorkloadEntitySearchQueryInput")),
        graphql_name="entitySearchQueries",
    )

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")

    scope_accounts = sgqlc.types.Field(
        "WorkloadScopeAccountsInput", graphql_name="scopeAccounts"
    )

    status_config = sgqlc.types.Field(
        "WorkloadStatusConfigInput", graphql_name="statusConfig"
    )


class WorkloadDuplicateInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class WorkloadEntitySearchQueryInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("query",)
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="query")


class WorkloadRegularRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_search_queries", "rollup")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )

    entity_search_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(WorkloadEntitySearchQueryInput)),
        graphql_name="entitySearchQueries",
    )

    rollup = sgqlc.types.Field(
        sgqlc.types.non_null("WorkloadRollupInput"), graphql_name="rollup"
    )


class WorkloadRemainingEntitiesRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("rollup",)
    rollup = sgqlc.types.Field(
        sgqlc.types.non_null("WorkloadRemainingEntitiesRuleRollupInput"),
        graphql_name="rollup",
    )


class WorkloadRemainingEntitiesRuleRollupInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("group_by", "strategy", "threshold_type", "threshold_value")
    group_by = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadGroupRemainingEntitiesRuleBy),
        graphql_name="groupBy",
    )

    strategy = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadRollupStrategy), graphql_name="strategy"
    )

    threshold_type = sgqlc.types.Field(
        WorkloadRuleThresholdType, graphql_name="thresholdType"
    )

    threshold_value = sgqlc.types.Field(Int, graphql_name="thresholdValue")


class WorkloadRollupInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("strategy", "threshold_type", "threshold_value")
    strategy = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadRollupStrategy), graphql_name="strategy"
    )

    threshold_type = sgqlc.types.Field(
        WorkloadRuleThresholdType, graphql_name="thresholdType"
    )

    threshold_value = sgqlc.types.Field(Int, graphql_name="thresholdValue")


class WorkloadScopeAccountsInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )


class WorkloadStaticStatusInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "enabled", "status", "summary")
    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    status = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadStatusValueInput), graphql_name="status"
    )

    summary = sgqlc.types.Field(String, graphql_name="summary")


class WorkloadStatusConfigInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("automatic", "static")
    automatic = sgqlc.types.Field(
        WorkloadAutomaticStatusInput, graphql_name="automatic"
    )

    static = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(WorkloadStaticStatusInput)),
        graphql_name="static",
    )


class WorkloadUpdateAutomaticStatusInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("enabled", "remaining_entities_rule", "rules")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    remaining_entities_rule = sgqlc.types.Field(
        WorkloadRemainingEntitiesRuleInput, graphql_name="remainingEntitiesRule"
    )

    rules = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("WorkloadUpdateRegularRuleInput")),
        graphql_name="rules",
    )


class WorkloadUpdateCollectionEntitySearchQueryInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("id", "query")
    id = sgqlc.types.Field(Int, graphql_name="id")

    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="query")


class WorkloadUpdateInput(sgqlc.types.Input):
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

    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )

    entity_search_queries = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(WorkloadUpdateCollectionEntitySearchQueryInput)
        ),
        graphql_name="entitySearchQueries",
    )

    name = sgqlc.types.Field(String, graphql_name="name")

    scope_accounts = sgqlc.types.Field(
        WorkloadScopeAccountsInput, graphql_name="scopeAccounts"
    )

    status_config = sgqlc.types.Field(
        "WorkloadUpdateStatusConfigInput", graphql_name="statusConfig"
    )


class WorkloadUpdateRegularRuleInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("entity_guids", "entity_search_queries", "id", "rollup")
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid)),
        graphql_name="entityGuids",
    )

    entity_search_queries = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(WorkloadUpdateCollectionEntitySearchQueryInput)
        ),
        graphql_name="entitySearchQueries",
    )

    id = sgqlc.types.Field(Int, graphql_name="id")

    rollup = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadRollupInput), graphql_name="rollup"
    )


class WorkloadUpdateStaticStatusInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("description", "enabled", "id", "status", "summary")
    description = sgqlc.types.Field(String, graphql_name="description")

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")

    id = sgqlc.types.Field(Int, graphql_name="id")

    status = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadStatusValueInput), graphql_name="status"
    )

    summary = sgqlc.types.Field(String, graphql_name="summary")


class WorkloadUpdateStatusConfigInput(sgqlc.types.Input):
    __schema__ = nerdgraph
    __field_names__ = ("automatic", "static")
    automatic = sgqlc.types.Field(
        WorkloadUpdateAutomaticStatusInput, graphql_name="automatic"
    )

    static = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(WorkloadUpdateStaticStatusInput)),
        graphql_name="static",
    )
