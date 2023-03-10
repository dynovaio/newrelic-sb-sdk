__all__ = [
    "AiIssuesIIncident",
    "AiWorkflowsResponseError",
    "AlertableEntity",
    "AlertableEntityOutline",
    "AlertsNotificationChannel",
    "AlertsNrqlCondition",
    "ApiAccessKey",
    "ApiAccessKeyError",
    "ApmBrowserApplicationEntity",
    "ApmBrowserApplicationEntityOutline",
    "CloudIntegration",
    "CloudProvider",
    "CollectionEntity",
    "EdgeEndpointDetail",
    "EntityRelationshipEdge",
    "ErrorsInboxResource",
    "ErrorsInboxResponseError",
    "InfrastructureIntegrationEntity",
    "InfrastructureIntegrationEntityOutline",
    "Nr1CatalogInstallPlanDirective",
    "Nr1CatalogInstaller",
    "Nr1CatalogNerdpackItem",
    "Nr1CatalogNerdpackItemMetadata",
    "Nr1CatalogPreview",
    "Nr1CatalogQuickstartComponent",
    "Nr1CatalogQuickstartComponentMetadata",
    "Nr1CatalogSupportedEntityTypes",
    "SuggestedNrqlQuery",
    "WhatsNewContent",
    "WorkloadStatusResult",
    "Entity",
    "EntityOutline",
    "Account",
    "AccountManagementCreateResponse",
    "AccountManagementManagedAccount",
    "AccountManagementOrganizationStitchedFields",
    "AccountManagementUpdateResponse",
    "AccountOutline",
    "AccountReference",
    "Actor",
    "AgentApplicationApmBrowserSettings",
    "AgentApplicationBrowserSettings",
    "AgentApplicationCreateBrowserResult",
    "AgentApplicationCreateMobileResult",
    "AgentApplicationDeleteResult",
    "AgentApplicationEnableBrowserResult",
    "AgentApplicationSettingsApmBase",
    "AgentApplicationSettingsApmConfig",
    "AgentApplicationSettingsBrowserAjax",
    "AgentApplicationSettingsBrowserBase",
    "AgentApplicationSettingsBrowserConfig",
    "AgentApplicationSettingsBrowserDistributedTracing",
    "AgentApplicationSettingsBrowserMonitoring",
    "AgentApplicationSettingsBrowserPrivacy",
    "AgentApplicationSettingsBrowserProperties",
    "AgentApplicationSettingsErrorCollector",
    "AgentApplicationSettingsIgnoredStatusCodeRule",
    "AgentApplicationSettingsJfr",
    "AgentApplicationSettingsMobileBase",
    "AgentApplicationSettingsMobileNetworkSettings",
    "AgentApplicationSettingsMobileProperties",
    "AgentApplicationSettingsNetworkAlias",
    "AgentApplicationSettingsSlowSql",
    "AgentApplicationSettingsThreadProfiler",
    "AgentApplicationSettingsTransactionTracer",
    "AgentApplicationSettingsUpdateError",
    "AgentApplicationSettingsUpdateResult",
    "AgentEnvironmentAccountApplicationLoadedModules",
    "AgentEnvironmentAccountApplicationLoadedModulesResults",
    "AgentEnvironmentAccountEnvironmentAttributesResults",
    "AgentEnvironmentAccountStitchedFields",
    "AgentEnvironmentApplicationEnvironmentAttributes",
    "AgentEnvironmentApplicationInstance",
    "AgentEnvironmentApplicationInstanceDetails",
    "AgentEnvironmentApplicationInstancesResult",
    "AgentEnvironmentApplicationLoadedModule",
    "AgentEnvironmentAttribute",
    "AgentEnvironmentLoadedModuleAttribute",
    "AgentFeatures",
    "AgentRelease",
    "AiDecisionsAccountStitchedFields",
    "AiDecisionsAnnotationEntry",
    "AiDecisionsApplicableIncidentSearch",
    "AiDecisionsDecision",
    "AiDecisionsDecisionListing",
    "AiDecisionsMergeFeedback",
    "AiDecisionsOperationResult",
    "AiDecisionsOpinionEntry",
    "AiDecisionsOverrideConfiguration",
    "AiDecisionsRule",
    "AiDecisionsRuleMetadata",
    "AiDecisionsSelectorApplicability",
    "AiDecisionsSelectorExamples",
    "AiDecisionsSimulation",
    "AiDecisionsSuggestion",
    "AiIssuesAccountStitchedFields",
    "AiIssuesConfigurationByEnvironment",
    "AiIssuesConfigurationOverrideResponse",
    "AiIssuesEnvironmentConfiguration",
    "AiIssuesGracePeriodConfig",
    "AiIssuesIncidentData",
    "AiIssuesIssue",
    "AiIssuesIssueData",
    "AiIssuesIssueUserActionResponse",
    "AiIssuesIssueUserActionResult",
    "AiIssuesKeyValue",
    "AiIssuesKeyValues",
    "AiNotificationsAccountStitchedFields",
    "AiNotificationsBasicAuth",
    "AiNotificationsChannel",
    "AiNotificationsChannelResponse",
    "AiNotificationsChannelSchemaResult",
    "AiNotificationsChannelTestResponse",
    "AiNotificationsChannelsResponse",
    "AiNotificationsConstraintError",
    "AiNotificationsConstraintsError",
    "AiNotificationsDataValidationError",
    "AiNotificationsDeleteResponse",
    "AiNotificationsDestination",
    "AiNotificationsDestinationResponse",
    "AiNotificationsDestinationTestResponse",
    "AiNotificationsDestinationsResponse",
    "AiNotificationsFieldError",
    "AiNotificationsOAuth2Auth",
    "AiNotificationsOAuthUrlResponse",
    "AiNotificationsProperty",
    "AiNotificationsResponseError",
    "AiNotificationsSchema",
    "AiNotificationsSchemaField",
    "AiNotificationsSelectComponentOptions",
    "AiNotificationsSuggestion",
    "AiNotificationsSuggestionError",
    "AiNotificationsSuggestionsResponse",
    "AiNotificationsTokenAuth",
    "AiNotificationsUiComponent",
    "AiNotificationsVariable",
    "AiNotificationsVariableResult",
    "AiTopologyAccountStitchedFields",
    "AiTopologyCollectorOperationResult",
    "AiTopologyDefiningAttribute",
    "AiTopologyEdge",
    "AiTopologyEdgeListing",
    "AiTopologyGraph",
    "AiTopologyVertex",
    "AiTopologyVertexListing",
    "AiWorkflowsAccountStitchedFields",
    "AiWorkflowsCreateWorkflowResponse",
    "AiWorkflowsDeleteWorkflowResponse",
    "AiWorkflowsDestinationConfiguration",
    "AiWorkflowsEnrichment",
    "AiWorkflowsFilter",
    "AiWorkflowsNrqlConfiguration",
    "AiWorkflowsPredicate",
    "AiWorkflowsTestNotificationResponse",
    "AiWorkflowsTestWorkflowResponse",
    "AiWorkflowsUpdateWorkflowResponse",
    "AiWorkflowsWorkflow",
    "AiWorkflowsWorkflows",
    "AlertsAccountStitchedFields",
    "AlertsCampfireNotificationChannelConfig",
    "AlertsConditionDeleteResponse",
    "AlertsEmailNotificationChannelConfig",
    "AlertsHipChatNotificationChannelConfig",
    "AlertsMutingRule",
    "AlertsMutingRuleCondition",
    "AlertsMutingRuleConditionGroup",
    "AlertsMutingRuleDeleteResponse",
    "AlertsMutingRuleSchedule",
    "AlertsNotificationChannelCreateError",
    "AlertsNotificationChannelCreateResponse",
    "AlertsNotificationChannelDeleteError",
    "AlertsNotificationChannelDeleteResponse",
    "AlertsNotificationChannelId",
    "AlertsNotificationChannelPoliciesResultSet",
    "AlertsNotificationChannelPolicy",
    "AlertsNotificationChannelUpdateError",
    "AlertsNotificationChannelUpdateResponse",
    "AlertsNotificationChannelsAddToPolicyError",
    "AlertsNotificationChannelsAddToPolicyResponse",
    "AlertsNotificationChannelsRemoveFromPolicyError",
    "AlertsNotificationChannelsRemoveFromPolicyResponse",
    "AlertsNotificationChannelsResultSet",
    "AlertsNrqlConditionExpiration",
    "AlertsNrqlConditionQuery",
    "AlertsNrqlConditionSignal",
    "AlertsNrqlConditionTerms",
    "AlertsNrqlConditionsSearchResultSet",
    "AlertsOpsGenieNotificationChannelConfig",
    "AlertsPagerDutyNotificationChannelConfig",
    "AlertsPoliciesSearchResultSet",
    "AlertsPolicy",
    "AlertsPolicyDeleteResponse",
    "AlertsSlackNotificationChannelConfig",
    "AlertsUserNotificationChannelConfig",
    "AlertsVictorOpsNotificationChannelConfig",
    "AlertsWebhookBasicAuthInput",
    "AlertsWebhookCustomHeaderInput",
    "AlertsWebhookNotificationChannelConfig",
    "AlertsXMattersNotificationChannelConfig",
    "ApiAccessActorStitchedFields",
    "ApiAccessCreateKeyResponse",
    "ApiAccessDeleteKeyResponse",
    "ApiAccessDeletedKey",
    "ApiAccessKeySearchResult",
    "ApiAccessUpdateKeyResponse",
    "ApmApplicationDeployment",
    "ApmApplicationEntitySettingsResult",
    "ApmApplicationRunningAgentVersions",
    "ApmApplicationSettings",
    "ApmApplicationSummaryData",
    "ApmBrowserApplicationSummaryData",
    "ApmExternalServiceSummaryData",
    "AuthorizationManagementAuthenticationDomain",
    "AuthorizationManagementAuthenticationDomainSearch",
    "AuthorizationManagementGrantAccessPayload",
    "AuthorizationManagementGrantedRole",
    "AuthorizationManagementGrantedRoleSearch",
    "AuthorizationManagementGroup",
    "AuthorizationManagementGroupSearch",
    "AuthorizationManagementOrganizationStitchedFields",
    "AuthorizationManagementRevokeAccessPayload",
    "AuthorizationManagementRole",
    "AuthorizationManagementRoleSearch",
    "BrowserApplicationRunningAgentVersions",
    "BrowserApplicationSettings",
    "BrowserApplicationSummaryData",
    "ChangeTrackingDeployment",
    "ChangeTrackingDeploymentSearchResult",
    "CloudAccountFields",
    "CloudAccountMutationError",
    "CloudActorFields",
    "CloudConfigureIntegrationPayload",
    "CloudDisableIntegrationPayload",
    "CloudIntegrationMutationError",
    "CloudLinkAccountPayload",
    "CloudLinkedAccount",
    "CloudMigrateAwsGovCloudToAssumeRolePayload",
    "CloudRenameAccountPayload",
    "CloudService",
    "CloudUnlinkAccountPayload",
    "CrossAccountNrdbResultContainer",
    "DashboardActorStitchedFields",
    "DashboardAddWidgetsToPageError",
    "DashboardAddWidgetsToPageResult",
    "DashboardAreaWidgetConfiguration",
    "DashboardBarWidgetConfiguration",
    "DashboardBillboardWidgetConfiguration",
    "DashboardBillboardWidgetThreshold",
    "DashboardCreateError",
    "DashboardCreateResult",
    "DashboardDeleteError",
    "DashboardDeleteResult",
    "DashboardEntityOwnerInfo",
    "DashboardEntityResult",
    "DashboardLineWidgetConfiguration",
    "DashboardLiveUrl",
    "DashboardLiveUrlError",
    "DashboardLiveUrlResult",
    "DashboardMarkdownWidgetConfiguration",
    "DashboardOwnerInfo",
    "DashboardPage",
    "DashboardPieWidgetConfiguration",
    "DashboardRevokeLiveUrlResult",
    "DashboardTableWidgetConfiguration",
    "DashboardUndeleteError",
    "DashboardUndeleteResult",
    "DashboardUpdateError",
    "DashboardUpdatePageError",
    "DashboardUpdatePageResult",
    "DashboardUpdateResult",
    "DashboardUpdateWidgetsInPageError",
    "DashboardUpdateWidgetsInPageResult",
    "DashboardVariable",
    "DashboardVariableDefaultItem",
    "DashboardVariableDefaultValue",
    "DashboardVariableEnumItem",
    "DashboardVariableNrqlQuery",
    "DashboardWidget",
    "DashboardWidgetConfiguration",
    "DashboardWidgetLayout",
    "DashboardWidgetNrqlQuery",
    "DashboardWidgetVisualization",
    "DataDictionaryAttribute",
    "DataDictionaryDataSource",
    "DataDictionaryDocsStitchedFields",
    "DataDictionaryEvent",
    "DataDictionaryUnit",
    "DataManagementAccountLimit",
    "DataManagementAccountStitchedFields",
    "DataManagementAppliedRules",
    "DataManagementBulkCopyResult",
    "DataManagementCustomizableRetention",
    "DataManagementEventNamespaces",
    "DataManagementFeatureSetting",
    "DataManagementNamespaceLevelRetention",
    "DataManagementRenderedRetention",
    "DataManagementRetention",
    "DataManagementRetentionValues",
    "DataManagementRule",
    "DateTimeWindow",
    "DistributedTracingActorStitchedFields",
    "DistributedTracingEntityTracingSummary",
    "DistributedTracingSpan",
    "DistributedTracingSpanAnomaly",
    "DistributedTracingSpanConnection",
    "DistributedTracingTrace",
    "DocumentationFields",
    "DomainType",
    "EdgeAccountStitchedFields",
    "EdgeCreateSpanAttributeRuleResponseError",
    "EdgeCreateSpanAttributeRulesResponse",
    "EdgeCreateTraceFilterRuleResponses",
    "EdgeCreateTraceObserverResponse",
    "EdgeCreateTraceObserverResponseError",
    "EdgeCreateTraceObserverResponses",
    "EdgeDataSource",
    "EdgeDataSourceGroup",
    "EdgeDeleteSpanAttributeRuleResponse",
    "EdgeDeleteSpanAttributeRuleResponseError",
    "EdgeDeleteTraceFilterRuleResponses",
    "EdgeDeleteTraceObserverResponse",
    "EdgeDeleteTraceObserverResponseError",
    "EdgeDeleteTraceObserverResponses",
    "EdgeEndpoint",
    "EdgeRandomTraceFilter",
    "EdgeSpanAttributeRule",
    "EdgeSpanAttributesTraceFilter",
    "EdgeTraceFilters",
    "EdgeTraceObserver",
    "EdgeTracing",
    "EdgeUpdateTraceObserverResponse",
    "EdgeUpdateTraceObserverResponseError",
    "EdgeUpdateTraceObserverResponses",
    "EntityAlertViolation",
    "EntityCollection",
    "EntityCollectionDefinition",
    "EntityCollectionScopeAccounts",
    "EntityDeleteError",
    "EntityDeleteResult",
    "EntityGoldenContext",
    "EntityGoldenContextScopedGoldenMetrics",
    "EntityGoldenContextScopedGoldenTags",
    "EntityGoldenGoldenMetricsError",
    "EntityGoldenMetric",
    "EntityGoldenMetricDefinition",
    "EntityGoldenMetricsDomainTypeScoped",
    "EntityGoldenMetricsDomainTypeScopedResponse",
    "EntityGoldenTag",
    "EntityGoldenTagsDomainTypeScoped",
    "EntityGoldenTagsDomainTypeScopedResponse",
    "EntityRelationship",
    "EntityRelationshipNode",
    "EntityRelationshipRelatedEntitiesResult",
    "EntityRelationshipUserDefinedCreateOrReplaceResult",
    "EntityRelationshipUserDefinedCreateOrReplaceResultError",
    "EntityRelationshipUserDefinedDeleteResult",
    "EntityRelationshipUserDefinedDeleteResultError",
    "EntityRelationshipVertex",
    "EntitySearch",
    "EntitySearchCounts",
    "EntitySearchResult",
    "EntitySearchTypes",
    "EntityTag",
    "EntityTagValueWithMetadata",
    "EntityTagWithMetadata",
    "ErrorsInboxActorStitchedFields",
    "ErrorsInboxAssignErrorGroupResponse",
    "ErrorsInboxAssignment",
    "ErrorsInboxDeleteErrorGroupResourceResponse",
    "ErrorsInboxErrorGroup",
    "ErrorsInboxErrorGroupStateTypeResult",
    "ErrorsInboxErrorGroupsResponse",
    "ErrorsInboxResourcesResponse",
    "ErrorsInboxUpdateErrorGroupStateResponse",
    "EventAttributeDefinition",
    "EventDefinition",
    "EventsToMetricsAccountStitchedFields",
    "EventsToMetricsCreateRuleFailure",
    "EventsToMetricsCreateRuleResult",
    "EventsToMetricsCreateRuleSubmission",
    "EventsToMetricsDeleteRuleFailure",
    "EventsToMetricsDeleteRuleResult",
    "EventsToMetricsDeleteRuleSubmission",
    "EventsToMetricsError",
    "EventsToMetricsListRuleResult",
    "EventsToMetricsRule",
    "EventsToMetricsUpdateRuleFailure",
    "EventsToMetricsUpdateRuleResult",
    "EventsToMetricsUpdateRuleSubmission",
    "HistoricalDataExportAccountStitchedFields",
    "HistoricalDataExportCustomerExportResponse",
    "IncidentIntelligenceEnvironmentAccountStitchedFields",
    "IncidentIntelligenceEnvironmentActorStitchedFields",
    "IncidentIntelligenceEnvironmentConsentAccounts",
    "IncidentIntelligenceEnvironmentConsentAuthorizedAccounts",
    "IncidentIntelligenceEnvironmentConsentedAccount",
    "IncidentIntelligenceEnvironmentCreateEnvironment",
    "IncidentIntelligenceEnvironmentCurrentEnvironmentResult",
    "IncidentIntelligenceEnvironmentDeleteEnvironment",
    "IncidentIntelligenceEnvironmentDissentAccounts",
    "IncidentIntelligenceEnvironmentEnvironmentAlreadyExists",
    "IncidentIntelligenceEnvironmentEnvironmentCreated",
    "IncidentIntelligenceEnvironmentIncidentIntelligenceEnvironment",
    "IncidentIntelligenceEnvironmentMultipleEnvironmentsAvailable",
    "IncidentIntelligenceEnvironmentUserNotAuthorizedForAccount",
    "IncidentIntelligenceEnvironmentUserNotCapableToOperateOnAccount",
    "InfrastructureHostSummaryData",
    "InstallationAccountStitchedFields",
    "InstallationInstallStatus",
    "InstallationInstallStatusResult",
    "InstallationRecipeEvent",
    "InstallationRecipeEventResult",
    "InstallationStatusError",
    "JavaFlightRecorderFlamegraph",
    "JavaFlightRecorderStackFrame",
    "KeyTransactionApplication",
    "KeyTransactionCreateResult",
    "KeyTransactionDeleteResult",
    "KeyTransactionUpdateResult",
    "LogConfigurationsAccountStitchedFields",
    "LogConfigurationsCreateDataPartitionRuleError",
    "LogConfigurationsCreateDataPartitionRuleResponse",
    "LogConfigurationsCreateParsingRuleResponse",
    "LogConfigurationsDataPartitionRule",
    "LogConfigurationsDataPartitionRuleMatchingCriteria",
    "LogConfigurationsDataPartitionRuleMutationError",
    "LogConfigurationsDeleteDataPartitionRuleResponse",
    "LogConfigurationsDeleteParsingRuleResponse",
    "LogConfigurationsGrokTestExtractedAttribute",
    "LogConfigurationsGrokTestResult",
    "LogConfigurationsObfuscationAction",
    "LogConfigurationsObfuscationExpression",
    "LogConfigurationsObfuscationRule",
    "LogConfigurationsParsingRule",
    "LogConfigurationsParsingRuleMutationError",
    "LogConfigurationsPipelineConfiguration",
    "LogConfigurationsUpdateDataPartitionRuleResponse",
    "LogConfigurationsUpdateParsingRuleResponse",
    "LogConfigurationsUpsertPipelineConfigurationResponse",
    "MetricNormalizationAccountStitchedFields",
    "MetricNormalizationRule",
    "MetricNormalizationRuleMetricGroupingIssue",
    "MetricNormalizationRuleMutationError",
    "MetricNormalizationRuleMutationResponse",
    "MobileAppSummaryData",
    "MobilePushNotificationActorStitchedFields",
    "MobilePushNotificationDevice",
    "MobilePushNotificationRemoveDeviceResult",
    "MobilePushNotificationSendPushResult",
    "NerdStorageAccountScope",
    "NerdStorageActorScope",
    "NerdStorageCollectionMember",
    "NerdStorageDeleteResult",
    "NerdStorageEntityScope",
    "NerdStorageVaultActorStitchedFields",
    "NerdStorageVaultDeleteSecretResult",
    "NerdStorageVaultResultError",
    "NerdStorageVaultSecret",
    "NerdStorageVaultWriteSecretResult",
    "NerdpackAllowListResult",
    "NerdpackAllowedAccount",
    "NerdpackAssetInfo",
    "NerdpackData",
    "NerdpackMutationResultPerAccount",
    "NerdpackNerdpacks",
    "NerdpackRemovedTagInfo",
    "NerdpackRemovedTagResponse",
    "NerdpackSubscribeResult",
    "NerdpackSubscription",
    "NerdpackUnsubscribeResult",
    "NerdpackVersion",
    "NerdpackVersionsResult",
    "Nr1CatalogActorStitchedFields",
    "Nr1CatalogAlertConditionOutline",
    "Nr1CatalogAlertConditionTemplate",
    "Nr1CatalogAlertConditionTemplateMetadata",
    "Nr1CatalogAlertPolicyOutline",
    "Nr1CatalogAlertPolicyTemplate",
    "Nr1CatalogAlertPolicyTemplateMetadata",
    "Nr1CatalogAuthor",
    "Nr1CatalogCategory",
    "Nr1CatalogCategoryFacet",
    "Nr1CatalogCommunityContactChannel",
    "Nr1CatalogComponentFacet",
    "Nr1CatalogDashboardOutline",
    "Nr1CatalogDashboardTemplate",
    "Nr1CatalogDashboardTemplateMetadata",
    "Nr1CatalogDataSource",
    "Nr1CatalogDataSourceInstall",
    "Nr1CatalogDataSourceMetadata",
    "Nr1CatalogEmailContactChannel",
    "Nr1CatalogIcon",
    "Nr1CatalogInstallAlertPolicyTemplateResult",
    "Nr1CatalogInstallDashboardTemplateResult",
    "Nr1CatalogInstallPlanStep",
    "Nr1CatalogInstallPlanTarget",
    "Nr1CatalogIssuesContactChannel",
    "Nr1CatalogLinkInstallDirective",
    "Nr1CatalogNerdletInstallDirective",
    "Nr1CatalogNerdpack",
    "Nr1CatalogNerdpackMetadata",
    "Nr1CatalogQuickstart",
    "Nr1CatalogQuickstartMetadata",
    "Nr1CatalogQuickstartsListing",
    "Nr1CatalogReleaseNote",
    "Nr1CatalogSearchFacets",
    "Nr1CatalogSearchResponse",
    "Nr1CatalogSearchResultTypeFacet",
    "Nr1CatalogSubmitMetadataError",
    "Nr1CatalogSubmitMetadataResult",
    "Nr1CatalogSupportChannels",
    "NrdbMetadata",
    "NrdbMetadataTimeWindow",
    "NrdbQueryProgress",
    "NrdbResultContainer",
    "NrqlDropRulesAccountStitchedFields",
    "NrqlDropRulesCreateDropRuleFailure",
    "NrqlDropRulesCreateDropRuleResult",
    "NrqlDropRulesCreateDropRuleSubmission",
    "NrqlDropRulesDeleteDropRuleFailure",
    "NrqlDropRulesDeleteDropRuleResult",
    "NrqlDropRulesDeleteDropRuleSubmission",
    "NrqlDropRulesDropRule",
    "NrqlDropRulesError",
    "NrqlDropRulesListDropRulesResult",
    "NrqlFacetSuggestion",
    "NrqlHistoricalQuery",
    "Organization",
    "OrganizationAccountShares",
    "OrganizationCreateSharedAccountResponse",
    "OrganizationCustomerOrganization",
    "OrganizationCustomerOrganizationWrapper",
    "OrganizationError",
    "OrganizationInformation",
    "OrganizationOrganizationAdministrator",
    "OrganizationProvisioningUpdateSubscriptionResult",
    "OrganizationProvisioningUserError",
    "OrganizationRevokeSharedAccountResponse",
    "OrganizationSharedAccount",
    "OrganizationUpdateResponse",
    "OrganizationUpdateSharedAccountResponse",
    "PixieAccountStitchedFields",
    "PixieActorStitchedFields",
    "PixieLinkPixieProjectError",
    "PixieLinkPixieProjectResult",
    "PixieLinkedPixieProject",
    "PixiePixieProject",
    "PixieRecordPixieTosAcceptanceError",
    "PixieRecordPixieTosAcceptanceResult",
    "QueryHistoryActorStitchedFields",
    "QueryHistoryNrqlHistoryResult",
    "ReferenceEntityCreateRepositoryError",
    "ReferenceEntityCreateRepositoryResult",
    "RequestContext",
    "RootMutationType",
    "RootQueryType",
    "SecureCredentialSummaryData",
    "ServiceLevelDefinition",
    "ServiceLevelEvents",
    "ServiceLevelEventsQuery",
    "ServiceLevelEventsQuerySelect",
    "ServiceLevelIndicator",
    "ServiceLevelIndicatorResultQueries",
    "ServiceLevelObjective",
    "ServiceLevelObjectiveResultQueries",
    "ServiceLevelObjectiveRollingTimeWindow",
    "ServiceLevelObjectiveTimeWindow",
    "ServiceLevelResultQuery",
    "StackTraceApmException",
    "StackTraceApmStackTrace",
    "StackTraceApmStackTraceFrame",
    "StackTraceBrowserException",
    "StackTraceBrowserStackTrace",
    "StackTraceBrowserStackTraceFrame",
    "StackTraceMobileCrash",
    "StackTraceMobileCrashStackTrace",
    "StackTraceMobileCrashStackTraceFrame",
    "StackTraceMobileException",
    "StackTraceMobileExceptionStackTrace",
    "StackTraceMobileExceptionStackTraceFrame",
    "StreamingExportAccountStitchedFields",
    "StreamingExportAwsDetails",
    "StreamingExportAzureDetails",
    "StreamingExportRule",
    "SuggestedNrqlQueryAnomaly",
    "SuggestedNrqlQueryResponse",
    "SyntheticMonitorSummaryData",
    "SyntheticsAccountStitchedFields",
    "SyntheticsBrokenLinksMonitor",
    "SyntheticsBrokenLinksMonitorCreateMutationResult",
    "SyntheticsBrokenLinksMonitorUpdateMutationResult",
    "SyntheticsCertCheckMonitor",
    "SyntheticsCertCheckMonitorCreateMutationResult",
    "SyntheticsCertCheckMonitorUpdateMutationResult",
    "SyntheticsCustomHeader",
    "SyntheticsDeviceEmulation",
    "SyntheticsError",
    "SyntheticsLocations",
    "SyntheticsMonitorCreateError",
    "SyntheticsMonitorDeleteMutationResult",
    "SyntheticsMonitorScriptQueryResponse",
    "SyntheticsMonitorUpdateError",
    "SyntheticsPrivateLocationDeleteResult",
    "SyntheticsPrivateLocationMutationError",
    "SyntheticsPrivateLocationMutationResult",
    "SyntheticsPrivateLocationPurgeQueueResult",
    "SyntheticsRuntime",
    "SyntheticsScriptApiMonitor",
    "SyntheticsScriptApiMonitorCreateMutationResult",
    "SyntheticsScriptApiMonitorUpdateMutationResult",
    "SyntheticsScriptBrowserMonitor",
    "SyntheticsScriptBrowserMonitorAdvancedOptions",
    "SyntheticsScriptBrowserMonitorCreateMutationResult",
    "SyntheticsScriptBrowserMonitorUpdateMutationResult",
    "SyntheticsSecureCredentialMutationResult",
    "SyntheticsSimpleBrowserMonitor",
    "SyntheticsSimpleBrowserMonitorAdvancedOptions",
    "SyntheticsSimpleBrowserMonitorCreateMutationResult",
    "SyntheticsSimpleBrowserMonitorUpdateMutationResult",
    "SyntheticsSimpleMonitor",
    "SyntheticsSimpleMonitorAdvancedOptions",
    "SyntheticsSimpleMonitorUpdateMutationResult",
    "SyntheticsStep",
    "SyntheticsStepMonitor",
    "SyntheticsStepMonitorAdvancedOptions",
    "SyntheticsStepMonitorCreateMutationResult",
    "SyntheticsStepMonitorUpdateMutationResult",
    "SyntheticsSyntheticMonitorAsset",
    "TaggingMutationError",
    "TaggingMutationResult",
    "TimeWindow",
    "TimeZoneInfo",
    "User",
    "UserManagementAddUsersToGroupsPayload",
    "UserManagementAuthenticationDomain",
    "UserManagementAuthenticationDomains",
    "UserManagementCreateGroupPayload",
    "UserManagementCreateUserPayload",
    "UserManagementCreatedUser",
    "UserManagementDeleteGroupPayload",
    "UserManagementDeleteUserPayload",
    "UserManagementDeletedUser",
    "UserManagementGroup",
    "UserManagementGroupUser",
    "UserManagementGroupUsers",
    "UserManagementGroups",
    "UserManagementOrganizationStitchedFields",
    "UserManagementOrganizationUserType",
    "UserManagementRemoveUsersFromGroupsPayload",
    "UserManagementUpdateGroupPayload",
    "UserManagementUpdateUserPayload",
    "UserManagementUser",
    "UserManagementUserGroup",
    "UserManagementUserGroups",
    "UserManagementUserType",
    "UserManagementUsers",
    "UserReference",
    "UsersActorStitchedFields",
    "UsersUserSearch",
    "UsersUserSearchResult",
    "WhatsNewDocsStitchedFields",
    "WhatsNewSearchResult",
    "WorkloadAccountStitchedFields",
    "WorkloadAutomaticStatus",
    "WorkloadCollection",
    "WorkloadCollectionWithoutStatus",
    "WorkloadEntityRef",
    "WorkloadEntitySearchQuery",
    "WorkloadRegularRule",
    "WorkloadRemainingEntitiesRule",
    "WorkloadRemainingEntitiesRuleRollup",
    "WorkloadRollup",
    "WorkloadRollupRuleDetails",
    "WorkloadScopeAccounts",
    "WorkloadStaticStatus",
    "WorkloadStatus",
    "WorkloadStatusConfig",
    "WorkloadValidAccounts",
    "WorkloadWorkloadStatus",
    "AiIssuesAnomalyIncident",
    "AiIssuesNewRelicIncident",
    "AiIssuesRestIncident",
    "AiWorkflowsCreateResponseError",
    "AiWorkflowsDeleteResponseError",
    "AiWorkflowsTestResponseError",
    "AiWorkflowsUpdateResponseError",
    "AlertsCampfireNotificationChannel",
    "AlertsEmailNotificationChannel",
    "AlertsHipChatNotificationChannel",
    "AlertsNrqlBaselineCondition",
    "AlertsNrqlOutlierCondition",
    "AlertsNrqlStaticCondition",
    "AlertsOpsGenieNotificationChannel",
    "AlertsPagerDutyNotificationChannel",
    "AlertsSlackNotificationChannel",
    "AlertsUserNotificationChannel",
    "AlertsVictorOpsNotificationChannel",
    "AlertsWebhookNotificationChannel",
    "AlertsXMattersNotificationChannel",
    "ApiAccessIngestKey",
    "ApiAccessIngestKeyError",
    "ApiAccessUserKey",
    "ApiAccessUserKeyError",
    "ApmApplicationEntity",
    "ApmApplicationEntityOutline",
    "ApmDatabaseInstanceEntity",
    "ApmDatabaseInstanceEntityOutline",
    "ApmExternalServiceEntity",
    "ApmExternalServiceEntityOutline",
    "BrowserApplicationEntity",
    "BrowserApplicationEntityOutline",
    "CloudAlbIntegration",
    "CloudApigatewayIntegration",
    "CloudAutoscalingIntegration",
    "CloudAwsAppsyncIntegration",
    "CloudAwsAthenaIntegration",
    "CloudAwsCognitoIntegration",
    "CloudAwsConnectIntegration",
    "CloudAwsDirectconnectIntegration",
    "CloudAwsDocdbIntegration",
    "CloudAwsFsxIntegration",
    "CloudAwsGlueIntegration",
    "CloudAwsGovCloudProvider",
    "CloudAwsKinesisanalyticsIntegration",
    "CloudAwsMediaconvertIntegration",
    "CloudAwsMediapackagevodIntegration",
    "CloudAwsMetadataIntegration",
    "CloudAwsMqIntegration",
    "CloudAwsMskIntegration",
    "CloudAwsNeptuneIntegration",
    "CloudAwsProvider",
    "CloudAwsQldbIntegration",
    "CloudAwsRoute53resolverIntegration",
    "CloudAwsStatesIntegration",
    "CloudAwsTagsGlobalIntegration",
    "CloudAwsTransitgatewayIntegration",
    "CloudAwsWafIntegration",
    "CloudAwsWafv2Integration",
    "CloudAwsXrayIntegration",
    "CloudAzureApimanagementIntegration",
    "CloudAzureAppgatewayIntegration",
    "CloudAzureAppserviceIntegration",
    "CloudAzureContainersIntegration",
    "CloudAzureCosmosdbIntegration",
    "CloudAzureCostmanagementIntegration",
    "CloudAzureDatafactoryIntegration",
    "CloudAzureEventhubIntegration",
    "CloudAzureExpressrouteIntegration",
    "CloudAzureFirewallsIntegration",
    "CloudAzureFrontdoorIntegration",
    "CloudAzureFunctionsIntegration",
    "CloudAzureKeyvaultIntegration",
    "CloudAzureLoadbalancerIntegration",
    "CloudAzureLogicappsIntegration",
    "CloudAzureMachinelearningIntegration",
    "CloudAzureMariadbIntegration",
    "CloudAzureMonitorIntegration",
    "CloudAzureMysqlIntegration",
    "CloudAzureMysqlflexibleIntegration",
    "CloudAzurePostgresqlIntegration",
    "CloudAzurePostgresqlflexibleIntegration",
    "CloudAzurePowerbidedicatedIntegration",
    "CloudAzureRediscacheIntegration",
    "CloudAzureServicebusIntegration",
    "CloudAzureSqlIntegration",
    "CloudAzureSqlmanagedIntegration",
    "CloudAzureStorageIntegration",
    "CloudAzureVirtualmachineIntegration",
    "CloudAzureVirtualnetworksIntegration",
    "CloudAzureVmsIntegration",
    "CloudAzureVpngatewaysIntegration",
    "CloudBaseIntegration",
    "CloudBaseProvider",
    "CloudBillingIntegration",
    "CloudCloudfrontIntegration",
    "CloudCloudtrailIntegration",
    "CloudDynamodbIntegration",
    "CloudEbsIntegration",
    "CloudEc2Integration",
    "CloudEcsIntegration",
    "CloudEfsIntegration",
    "CloudElasticacheIntegration",
    "CloudElasticbeanstalkIntegration",
    "CloudElasticsearchIntegration",
    "CloudElbIntegration",
    "CloudEmrIntegration",
    "CloudGcpAlloydbIntegration",
    "CloudGcpAppengineIntegration",
    "CloudGcpBigqueryIntegration",
    "CloudGcpBigtableIntegration",
    "CloudGcpComposerIntegration",
    "CloudGcpDataflowIntegration",
    "CloudGcpDataprocIntegration",
    "CloudGcpDatastoreIntegration",
    "CloudGcpFirebasedatabaseIntegration",
    "CloudGcpFirebasehostingIntegration",
    "CloudGcpFirebasestorageIntegration",
    "CloudGcpFirestoreIntegration",
    "CloudGcpFunctionsIntegration",
    "CloudGcpInterconnectIntegration",
    "CloudGcpKubernetesIntegration",
    "CloudGcpLoadbalancingIntegration",
    "CloudGcpMemcacheIntegration",
    "CloudGcpProvider",
    "CloudGcpPubsubIntegration",
    "CloudGcpRedisIntegration",
    "CloudGcpRouterIntegration",
    "CloudGcpRunIntegration",
    "CloudGcpSpannerIntegration",
    "CloudGcpSqlIntegration",
    "CloudGcpStorageIntegration",
    "CloudGcpVmsIntegration",
    "CloudGcpVpcaccessIntegration",
    "CloudHealthIntegration",
    "CloudIamIntegration",
    "CloudIotIntegration",
    "CloudKinesisFirehoseIntegration",
    "CloudKinesisIntegration",
    "CloudLambdaIntegration",
    "CloudRdsIntegration",
    "CloudRedshiftIntegration",
    "CloudRoute53Integration",
    "CloudS3Integration",
    "CloudSesIntegration",
    "CloudSnsIntegration",
    "CloudSqsIntegration",
    "CloudTrustedadvisorIntegration",
    "CloudVpcIntegration",
    "DashboardEntity",
    "DashboardEntityOutline",
    "EdgeAgentEndpointDetail",
    "EdgeHttpsEndpointDetail",
    "EntityRelationshipDetectedEdge",
    "EntityRelationshipUserDefinedEdge",
    "ErrorsInboxAssignErrorGroupError",
    "ErrorsInboxJiraIssue",
    "ErrorsInboxUpdateErrorGroupStateError",
    "ExternalEntity",
    "ExternalEntityOutline",
    "GenericEntity",
    "GenericEntityOutline",
    "GenericInfrastructureEntity",
    "GenericInfrastructureEntityOutline",
    "InfrastructureAwsLambdaFunctionEntity",
    "InfrastructureAwsLambdaFunctionEntityOutline",
    "InfrastructureHostEntity",
    "InfrastructureHostEntityOutline",
    "KeyTransactionEntity",
    "KeyTransactionEntityOutline",
    "MobileApplicationEntity",
    "MobileApplicationEntityOutline",
    "Nr1CatalogAllSupportedEntityTypes",
    "Nr1CatalogInstallPlan",
    "Nr1CatalogLauncher",
    "Nr1CatalogLauncherMetadata",
    "Nr1CatalogLinkInstallPlanDirective",
    "Nr1CatalogNerdlet",
    "Nr1CatalogNerdletInstallPlanDirective",
    "Nr1CatalogNerdletMetadata",
    "Nr1CatalogNoSupportedEntityTypes",
    "Nr1CatalogQuickstartAlert",
    "Nr1CatalogQuickstartAlertCondition",
    "Nr1CatalogQuickstartAlertConditionMetadata",
    "Nr1CatalogQuickstartAlertMetadata",
    "Nr1CatalogQuickstartDashboard",
    "Nr1CatalogQuickstartDashboardMetadata",
    "Nr1CatalogQuickstartDocumentation",
    "Nr1CatalogQuickstartDocumentationMetadata",
    "Nr1CatalogQuickstartInstallPlan",
    "Nr1CatalogQuickstartInstallPlanMetadata",
    "Nr1CatalogScreenshot",
    "Nr1CatalogSpecificSupportedEntityTypes",
    "Nr1CatalogTargetedInstallPlanDirective",
    "Nr1CatalogVisualization",
    "Nr1CatalogVisualizationMetadata",
    "SecureCredentialEntity",
    "SecureCredentialEntityOutline",
    "SuggestedAnomalyBasedNrqlQuery",
    "SuggestedHistoryBasedNrqlQuery",
    "SyntheticMonitorEntity",
    "SyntheticMonitorEntityOutline",
    "ThirdPartyServiceEntity",
    "ThirdPartyServiceEntityOutline",
    "UnavailableEntity",
    "UnavailableEntityOutline",
    "WhatsNewAnnouncementContent",
    "WorkloadEntity",
    "WorkloadEntityOutline",
    "WorkloadRollupRuleStatusResult",
    "WorkloadStaticStatusResult",
    "AiNotificationsAuth",
    "AiNotificationsError",
    "AiWorkflowsConfiguration",
    "AlertsNotificationChannelMutation",
    "IncidentIntelligenceEnvironmentCreateEnvironmentResultDetails",
    "IncidentIntelligenceEnvironmentCurrentEnvironmentResultReasonDetails",
    "Nr1CatalogDataSourceInstallDirective",
    "Nr1CatalogSearchResult",
]


# pylint: disable=duplicate-code,unused-import,too-many-lines


import sgqlc.types
import sgqlc.types.datetime

from newrelic_sb_sdk.graphql.enums import (
    AgentApplicationBrowserLoader,
    AgentApplicationSettingsBrowserLoader,
    AgentApplicationSettingsNetworkFilterMode,
    AgentApplicationSettingsRecordSqlEnum,
    AgentApplicationSettingsThresholdTypeEnum,
    AgentApplicationSettingsTracer,
    AgentApplicationSettingsUpdateErrorClass,
    AgentFeaturesFilter,
    AgentReleasesFilter,
    AiDecisionsDecisionSortMethod,
    AiDecisionsDecisionState,
    AiDecisionsDecisionType,
    AiDecisionsIncidentSelect,
    AiDecisionsIssuePriority,
    AiDecisionsOpinion,
    AiDecisionsResultType,
    AiDecisionsRuleSource,
    AiDecisionsRuleState,
    AiDecisionsRuleType,
    AiDecisionsSuggestionState,
    AiIssuesIncidentState,
    AiIssuesIssueMutingState,
    AiIssuesIssueState,
    AiIssuesIssueUserAction,
    AiIssuesPriority,
    AiNotificationsAuthType,
    AiNotificationsChannelStatus,
    AiNotificationsChannelType,
    AiNotificationsDestinationStatus,
    AiNotificationsDestinationType,
    AiNotificationsErrorType,
    AiNotificationsProduct,
    AiNotificationsResult,
    AiNotificationsUiComponentType,
    AiNotificationsUiComponentValidation,
    AiNotificationsVariableCategory,
    AiNotificationsVariableType,
    AiTopologyCollectorResultType,
    AiTopologyVertexClass,
    AiWorkflowsCreateErrorType,
    AiWorkflowsDeleteErrorType,
    AiWorkflowsDestinationType,
    AiWorkflowsEnrichmentType,
    AiWorkflowsFilterType,
    AiWorkflowsMutingRulesHandling,
    AiWorkflowsNotificationTrigger,
    AiWorkflowsOperator,
    AiWorkflowsTestErrorType,
    AiWorkflowsTestNotificationResponseStatus,
    AiWorkflowsTestResponseStatus,
    AiWorkflowsUpdateErrorType,
    AlertsDayOfWeek,
    AlertsFillOption,
    AlertsIncidentPreference,
    AlertsMutingRuleConditionGroupOperator,
    AlertsMutingRuleConditionOperator,
    AlertsMutingRuleScheduleRepeat,
    AlertsMutingRuleStatus,
    AlertsNotificationChannelCreateErrorType,
    AlertsNotificationChannelDeleteErrorType,
    AlertsNotificationChannelsAddToPolicyErrorType,
    AlertsNotificationChannelsRemoveFromPolicyErrorType,
    AlertsNotificationChannelType,
    AlertsNotificationChannelUpdateErrorType,
    AlertsNrqlBaselineDirection,
    AlertsNrqlConditionPriority,
    AlertsNrqlConditionTermsOperator,
    AlertsNrqlConditionThresholdOccurrences,
    AlertsNrqlConditionType,
    AlertsOpsGenieDataCenterRegion,
    AlertsSignalAggregationMethod,
    AlertsWebhookCustomPayloadType,
    ApiAccessIngestKeyErrorType,
    ApiAccessIngestKeyType,
    ApiAccessKeyType,
    ApiAccessUserKeyErrorType,
    BrowserAgentInstallType,
    ChangeTrackingDeploymentType,
    ChartFormatType,
    ChartImageType,
    CloudMetricCollectionMode,
    DashboardAddWidgetsToPageErrorType,
    DashboardAlertSeverity,
    DashboardCreateErrorType,
    DashboardDeleteErrorType,
    DashboardDeleteResultStatus,
    DashboardEntityPermissions,
    DashboardLiveUrlErrorType,
    DashboardLiveUrlType,
    DashboardPermissions,
    DashboardUndeleteErrorType,
    DashboardUpdateErrorType,
    DashboardUpdatePageErrorType,
    DashboardUpdateWidgetsInPageErrorType,
    DashboardVariableReplacementStrategy,
    DashboardVariableType,
    DataDictionaryTextFormat,
    DataManagementCategory,
    DataManagementUnit,
    DistributedTracingSpanAnomalyType,
    DistributedTracingSpanClientType,
    DistributedTracingSpanProcessBoundary,
    EdgeComplianceTypeCode,
    EdgeCreateSpanAttributeRuleResponseErrorType,
    EdgeCreateTraceObserverResponseErrorType,
    EdgeDataSourceStatusType,
    EdgeDeleteSpanAttributeRuleResponseErrorType,
    EdgeDeleteTraceObserverResponseErrorType,
    EdgeEndpointStatus,
    EdgeEndpointType,
    EdgeProviderRegion,
    EdgeSpanAttributeKeyOperator,
    EdgeSpanAttributeValueOperator,
    EdgeTraceFilterAction,
    EdgeTraceObserverStatus,
    EdgeUpdateTraceObserverResponseErrorType,
    EmbeddedChartType,
    EntityAlertSeverity,
    EntityCollectionType,
    EntityDeleteErrorType,
    EntityGoldenEventObjectId,
    EntityGoldenGoldenMetricsErrorType,
    EntityGoldenMetricUnit,
    EntityRelationshipEdgeType,
    EntityRelationshipType,
    EntityRelationshipUserDefinedCreateOrReplaceErrorType,
    EntityRelationshipUserDefinedDeleteErrorType,
    EntitySearchCountsFacet,
    EntitySearchSortCriteria,
    EntityType,
    ErrorsInboxAssignErrorGroupErrorType,
    ErrorsInboxErrorGroupState,
    ErrorsInboxUpdateErrorGroupStateErrorType,
    EventsToMetricsErrorReason,
    HistoricalDataExportStatus,
    IncidentIntelligenceEnvironmentConsentAccountsResult,
    IncidentIntelligenceEnvironmentCreateEnvironmentResult,
    IncidentIntelligenceEnvironmentCurrentEnvironmentResultReason,
    IncidentIntelligenceEnvironmentDeleteEnvironmentResult,
    IncidentIntelligenceEnvironmentDissentAccountsResult,
    IncidentIntelligenceEnvironmentEnvironmentKind,
    IncidentIntelligenceEnvironmentSupportedEnvironmentKind,
    InstallationInstallStateType,
    InstallationRecipeStatusType,
    LogConfigurationsCreateDataPartitionRuleErrorType,
    LogConfigurationsDataPartitionRuleMatchingOperator,
    LogConfigurationsDataPartitionRuleMutationErrorType,
    LogConfigurationsDataPartitionRuleRetentionPolicyType,
    LogConfigurationsObfuscationMethod,
    LogConfigurationsParsingRuleMutationErrorType,
    MetricNormalizationRuleAction,
    MetricNormalizationRuleErrorType,
    NerdpackMutationErrorType,
    NerdpackMutationResult,
    NerdpackRemovedTagResponseType,
    NerdpackSubscriptionAccessType,
    NerdpackSubscriptionModel,
    NerdStorageVaultErrorType,
    NerdStorageVaultResultStatus,
    Nr1CatalogAlertConditionType,
    Nr1CatalogInstallerType,
    Nr1CatalogInstallPlanDestination,
    Nr1CatalogInstallPlanDirectiveMode,
    Nr1CatalogInstallPlanOperatingSystem,
    Nr1CatalogInstallPlanTargetType,
    Nr1CatalogMutationResult,
    Nr1CatalogNerdpackVisibility,
    Nr1CatalogQuickstartAlertConditionType,
    Nr1CatalogRenderFormat,
    Nr1CatalogSearchComponentType,
    Nr1CatalogSearchResultType,
    Nr1CatalogSearchSortOption,
    Nr1CatalogSubmitMetadataErrorType,
    Nr1CatalogSupportedEntityTypesMode,
    Nr1CatalogSupportLevel,
    NrqlDropRulesAction,
    NrqlDropRulesErrorReason,
    OrganizationUpdateErrorType,
    PixieLinkPixieProjectErrorType,
    PixieRecordPixieTosAcceptanceErrorType,
    ReferenceEntityCreateRepositoryErrorType,
    RegionScope,
    ServiceLevelEventsQuerySelectFunction,
    ServiceLevelObjectiveRollingTimeWindowUnit,
    StreamingExportStatus,
    SyntheticMonitorStatus,
    SyntheticMonitorType,
    SyntheticsDeviceOrientation,
    SyntheticsDeviceType,
    SyntheticsMonitorCreateErrorType,
    SyntheticsMonitorPeriod,
    SyntheticsMonitorStatus,
    SyntheticsMonitorUpdateErrorType,
    SyntheticsPrivateLocationMutationErrorType,
    SyntheticsStepType,
    TaggingMutationErrorType,
    WhatsNewContentType,
    WorkloadGroupRemainingEntitiesRuleBy,
    WorkloadResultingGroupType,
    WorkloadRollupStrategy,
    WorkloadRuleThresholdType,
    WorkloadStatusSource,
    WorkloadStatusValue,
)
from newrelic_sb_sdk.graphql.input_objects import (
    AccountManagementCreateInput,
    AccountManagementUpdateInput,
    AgentApplicationBrowserSettingsInput,
    AgentApplicationSettingsUpdateInput,
    AgentEnvironmentFilter,
    AiDecisionsRuleBlueprint,
    AiDecisionsSearchBlueprint,
    AiDecisionsSimulationBlueprint,
    AiDecisionsSuggestionBlueprint,
    AiIssuesFilterIncidents,
    AiIssuesFilterIncidentsEvents,
    AiIssuesFilterIssues,
    AiIssuesFilterIssuesEvents,
    AiIssuesGracePeriodConfigurationInput,
    AiNotificationsChannelFilter,
    AiNotificationsChannelInput,
    AiNotificationsChannelSorter,
    AiNotificationsChannelUpdate,
    AiNotificationsConstraint,
    AiNotificationsDestinationFilter,
    AiNotificationsDestinationInput,
    AiNotificationsDestinationSorter,
    AiNotificationsDestinationUpdate,
    AiNotificationsDynamicVariable,
    AiNotificationsSuggestionFilter,
    AiNotificationsVariableFilter,
    AiNotificationsVariableSorter,
    AiTopologyCollectorEdgeBlueprint,
    AiTopologyCollectorVertexBlueprint,
    AiWorkflowsCreateWorkflowInput,
    AiWorkflowsFilters,
    AiWorkflowsTestWorkflowInput,
    AiWorkflowsUpdateWorkflowInput,
    AlertsMutingRuleInput,
    AlertsMutingRuleUpdateInput,
    AlertsNotificationChannelCreateConfiguration,
    AlertsNotificationChannelUpdateConfiguration,
    AlertsNrqlConditionBaselineInput,
    AlertsNrqlConditionsSearchCriteriaInput,
    AlertsNrqlConditionStaticInput,
    AlertsNrqlConditionUpdateBaselineInput,
    AlertsNrqlConditionUpdateStaticInput,
    AlertsPoliciesSearchCriteriaInput,
    AlertsPolicyInput,
    AlertsPolicyUpdateInput,
    ApiAccessCreateInput,
    ApiAccessDeleteInput,
    ApiAccessKeySearchQuery,
    ApiAccessUpdateInput,
    AuthorizationManagementGrantAccess,
    AuthorizationManagementRevokeAccess,
    ChangeTrackingDeploymentInput,
    ChangeTrackingSearchFilter,
    CloudAwsGovCloudMigrateToAssumeroleInput,
    CloudDisableIntegrationsInput,
    CloudIntegrationsInput,
    CloudLinkCloudAccountsInput,
    CloudRenameAccountsInput,
    CloudUnlinkAccountsInput,
    DashboardInput,
    DashboardLiveUrlsFilterInput,
    DashboardSnapshotUrlInput,
    DashboardUpdatePageInput,
    DashboardUpdateWidgetInput,
    DashboardWidgetInput,
    DataManagementAccountFeatureSettingInput,
    DataManagementRuleInput,
    DomainTypeInput,
    EdgeCreateTraceFilterRulesInput,
    EdgeCreateTraceObserverInput,
    EdgeDeleteTraceFilterRulesInput,
    EdgeDeleteTraceObserverInput,
    EdgeUpdateTraceObserverInput,
    EntityGoldenContextInput,
    EntityGoldenMetricInput,
    EntityGoldenNrqlTimeWindowInput,
    EntityGoldenTagInput,
    EntityRelationshipEdgeFilter,
    EntitySearchOptions,
    EntitySearchQueryBuilder,
    ErrorsInboxAssignErrorGroupInput,
    ErrorsInboxErrorEventInput,
    ErrorsInboxErrorGroupSearchFilterInput,
    ErrorsInboxErrorGroupSortOrderInput,
    ErrorsInboxResourceFilterInput,
    EventsToMetricsCreateRuleInput,
    EventsToMetricsDeleteRuleInput,
    EventsToMetricsUpdateRuleInput,
    InstallationInstallStatusInput,
    InstallationRecipeStatus,
    LogConfigurationsCreateDataPartitionRuleInput,
    LogConfigurationsCreateObfuscationExpressionInput,
    LogConfigurationsCreateObfuscationRuleInput,
    LogConfigurationsParsingRuleConfiguration,
    LogConfigurationsPipelineConfigurationInput,
    LogConfigurationsUpdateDataPartitionRuleInput,
    LogConfigurationsUpdateObfuscationExpressionInput,
    LogConfigurationsUpdateObfuscationRuleInput,
    MetricNormalizationCreateRuleInput,
    MetricNormalizationEditRuleInput,
    NerdpackAllowListInput,
    NerdpackCreationInput,
    NerdpackDataFilter,
    NerdpackOverrideVersionRules,
    NerdpackRemoveVersionTagInput,
    NerdpackSubscribeAccountsInput,
    NerdpackTagVersionInput,
    NerdpackUnsubscribeAccountsInput,
    NerdpackVersionFilter,
    NerdStorageScopeInput,
    NerdStorageVaultScope,
    NerdStorageVaultWriteSecretInput,
    Nr1CatalogSearchFilter,
    Nr1CatalogSubmitMetadataInput,
    NrqlDropRulesCreateDropRuleInput,
    NrqlQueryOptions,
    OrganizationCreateSharedAccountInput,
    OrganizationProvisioningProductInput,
    OrganizationRevokeSharedAccountInput,
    OrganizationUpdateInput,
    OrganizationUpdateSharedAccountInput,
    QueryHistoryQueryHistoryOptionsInput,
    ReferenceEntityCreateRepositoryInput,
    ServiceLevelIndicatorCreateInput,
    ServiceLevelIndicatorUpdateInput,
    SortCriterionWithDirection,
    StreamingExportAwsInput,
    StreamingExportAzureInput,
    StreamingExportRuleInput,
    SyntheticsCreateBrokenLinksMonitorInput,
    SyntheticsCreateCertCheckMonitorInput,
    SyntheticsCreateScriptApiMonitorInput,
    SyntheticsCreateScriptBrowserMonitorInput,
    SyntheticsCreateSimpleBrowserMonitorInput,
    SyntheticsCreateSimpleMonitorInput,
    SyntheticsCreateStepMonitorInput,
    SyntheticsUpdateBrokenLinksMonitorInput,
    SyntheticsUpdateCertCheckMonitorInput,
    SyntheticsUpdateScriptApiMonitorInput,
    SyntheticsUpdateScriptBrowserMonitorInput,
    SyntheticsUpdateSimpleBrowserMonitorInput,
    SyntheticsUpdateSimpleMonitorInput,
    SyntheticsUpdateStepMonitorInput,
    TaggingTagInput,
    TaggingTagValueInput,
    TimeWindowInput,
    UserManagementCreateGroup,
    UserManagementCreateUser,
    UserManagementDeleteGroup,
    UserManagementDeleteUser,
    UserManagementUpdateGroup,
    UserManagementUpdateUser,
    UserManagementUsersGroupsInput,
    UsersUserSearchQuery,
    WhatsNewContentSearchQuery,
    WorkloadCreateInput,
    WorkloadDuplicateInput,
    WorkloadUpdateInput,
)
from newrelic_sb_sdk.graphql.scalars import (
    ID,
    AgentApplicationSettingsErrorCollectorHttpStatus,
    AiDecisionsRuleExpression,
    AttributeMap,
    Boolean,
    DashboardWidgetRawConfiguration,
    Date,
    DateTime,
    DistributedTracingSpanAttributes,
    EntityAlertViolationInt,
    EntityGuid,
    EpochMilliseconds,
    EpochSeconds,
    Float,
    InstallationRawMetadata,
    Int,
    LogConfigurationsLogDataPartitionName,
    Milliseconds,
    Minutes,
    NerdpackTagName,
    NerdStorageDocument,
    Nr1CatalogRawNerdletState,
    NrdbRawResults,
    NrdbResult,
    Nrql,
    Seconds,
    SecureValue,
    SemVer,
    String,
)

from . import nerdgraph

__docformat__ = "markdown"


class AiIssuesIIncident(sgqlc.types.Interface):
    """Class for AiIssuesIIncident.

    Incident interface.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_ids",
        "closed_at",
        "created_at",
        "description",
        "entity_guids",
        "entity_names",
        "entity_types",
        "environment_id",
        "incident_id",
        "priority",
        "state",
        "timestamp",
        "title",
        "updated_at",
    )
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="accountIds"
    )


class AiWorkflowsResponseError(sgqlc.types.Interface):
    """Class for AiWorkflowsResponseError.

    Error description.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description",)
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class AlertableEntity(sgqlc.types.Interface):
    __schema__ = nerdgraph
    __field_names__ = ("alert_severity", "alert_violations", "recent_alert_violations")
    alert_severity = sgqlc.types.Field(
        EntityAlertSeverity, graphql_name="alertSeverity"
    )


class AlertableEntityOutline(sgqlc.types.Interface):
    __schema__ = nerdgraph
    __field_names__ = ("alert_severity",)
    alert_severity = sgqlc.types.Field(
        EntityAlertSeverity, graphql_name="alertSeverity"
    )


class AlertsNotificationChannel(sgqlc.types.Interface):
    """Class for AlertsNotificationChannel.

    A notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("associated_policies", "id", "name", "type")
    associated_policies = sgqlc.types.Field(
        sgqlc.types.non_null("AlertsNotificationChannelPoliciesResultSet"),
        graphql_name="associatedPolicies",
    )


class AlertsNrqlCondition(sgqlc.types.Interface):
    """Class for AlertsNrqlCondition.

    A New Relic Alerts condition that uses a NRQL query to determine
    violations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "enabled",
        "entity",
        "entity_guid",
        "expiration",
        "id",
        "name",
        "nrql",
        "policy_id",
        "runbook_url",
        "signal",
        "terms",
        "type",
        "violation_time_limit_seconds",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class ApiAccessKey(sgqlc.types.Interface):
    """Class for ApiAccessKey.

    A key for accessing New Relic APIs.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_at", "id", "key", "name", "notes", "type")
    created_at = sgqlc.types.Field(EpochSeconds, graphql_name="createdAt")


class ApiAccessKeyError(sgqlc.types.Interface):
    """Class for ApiAccessKeyError.

    A key error. Each error maps to a single key input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class ApmBrowserApplicationEntity(sgqlc.types.Interface):
    """Class for ApmBrowserApplicationEntity.

    The `ApmBrowserApplicationEntity` interface provides detailed
    information for the Browser App injected by an APM Application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apm_browser_summary",)
    apm_browser_summary = sgqlc.types.Field(
        "ApmBrowserApplicationSummaryData", graphql_name="apmBrowserSummary"
    )


class ApmBrowserApplicationEntityOutline(sgqlc.types.Interface):
    """Class for ApmBrowserApplicationEntityOutline.

    The `ApmBrowserApplicationEntityOutline` interface provides
    detailed information for the Browser App injected by an APM
    Application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apm_browser_summary",)
    apm_browser_summary = sgqlc.types.Field(
        "ApmBrowserApplicationSummaryData", graphql_name="apmBrowserSummary"
    )


class CloudIntegration(sgqlc.types.Interface):
    """Class for CloudIntegration.

    The configuration of a cloud service integration for a linked
    account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "id",
        "linked_account",
        "name",
        "nr_account_id",
        "service",
        "updated_at",
    )
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(EpochSeconds), graphql_name="createdAt"
    )


class CloudProvider(sgqlc.types.Interface):
    """Class for CloudProvider.

    A cloud services provider.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "icon",
        "id",
        "name",
        "service",
        "services",
        "slug",
        "updated_at",
    )
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(EpochSeconds), graphql_name="createdAt"
    )


class CollectionEntity(sgqlc.types.Interface):
    """Class for CollectionEntity.

    A group of entities defined by entity search queries and specific
    GUIDs.
    """

    __schema__ = nerdgraph
    __field_names__ = ("collection", "guid")
    collection = sgqlc.types.Field(
        "EntityCollection",
        graphql_name="collection",
        args=sgqlc.types.ArgDict(
            (
                (
                    "name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="name", default=None
                    ),
                ),
            )
        ),
    )


class EdgeEndpointDetail(sgqlc.types.Interface):
    """Class for EdgeEndpointDetail.

    The information common to all endpoints.
    """

    __schema__ = nerdgraph
    __field_names__ = ("host", "port")
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="host")


class EntityRelationshipEdge(sgqlc.types.Interface):
    """Class for EntityRelationshipEdge.

    An entity relationship.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_at", "source", "target", "type")
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(EpochMilliseconds), graphql_name="createdAt"
    )


class ErrorsInboxResource(sgqlc.types.Interface):
    """Class for ErrorsInboxResource.

    Basic external resource.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "url")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class ErrorsInboxResponseError(sgqlc.types.Interface):
    """Class for ErrorsInboxResponseError.

    Response error interface.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description",)
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class InfrastructureIntegrationEntity(sgqlc.types.Interface):
    __schema__ = nerdgraph
    __field_names__ = ("integration_type_code",)
    integration_type_code = sgqlc.types.Field(
        String, graphql_name="integrationTypeCode"
    )


class InfrastructureIntegrationEntityOutline(sgqlc.types.Interface):
    __schema__ = nerdgraph
    __field_names__ = ("integration_type_code",)
    integration_type_code = sgqlc.types.Field(
        String, graphql_name="integrationTypeCode"
    )


class Nr1CatalogInstallPlanDirective(sgqlc.types.Interface):
    """Class for Nr1CatalogInstallPlanDirective.

    Information about an install plan directive.
    """

    __schema__ = nerdgraph
    __field_names__ = ("mode",)
    mode = sgqlc.types.Field(
        sgqlc.types.non_null(Nr1CatalogInstallPlanDirectiveMode), graphql_name="mode"
    )


class Nr1CatalogInstaller(sgqlc.types.Interface):
    """Class for Nr1CatalogInstaller.

    Information about how a quickstart is installed.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(
        sgqlc.types.non_null(Nr1CatalogInstallerType), graphql_name="type"
    )


class Nr1CatalogNerdpackItem(sgqlc.types.Interface):
    """Class for Nr1CatalogNerdpackItem.

    Information about an item in a Nerdpack.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "metadata")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class Nr1CatalogNerdpackItemMetadata(sgqlc.types.Interface):
    """Class for Nr1CatalogNerdpackItemMetadata.

    Metadata information for an item in a Nerdpack.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "display_name", "previews")
    description = sgqlc.types.Field(String, graphql_name="description")


class Nr1CatalogPreview(sgqlc.types.Interface):
    """Class for Nr1CatalogPreview.

    Specifies fields required for types that implement the ability to
    display a media preview in the New Relic One Catalog.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogQuickstartComponent(sgqlc.types.Interface):
    """Class for Nr1CatalogQuickstartComponent.

    Information about a component in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metadata",)
    metadata = sgqlc.types.Field(
        sgqlc.types.non_null("Nr1CatalogQuickstartComponentMetadata"),
        graphql_name="metadata",
    )


class Nr1CatalogQuickstartComponentMetadata(sgqlc.types.Interface):
    """Class for Nr1CatalogQuickstartComponentMetadata.

    Information related to the metadata attached to a quickstart
    component.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "display_name")
    description = sgqlc.types.Field(String, graphql_name="description")


class Nr1CatalogSupportedEntityTypes(sgqlc.types.Interface):
    """Class for Nr1CatalogSupportedEntityTypes.

    Specifies fields required for types that implement the ability to
    determine the level of supported entity types.
    """

    __schema__ = nerdgraph
    __field_names__ = ("mode",)
    mode = sgqlc.types.Field(
        sgqlc.types.non_null(Nr1CatalogSupportedEntityTypesMode), graphql_name="mode"
    )


class SuggestedNrqlQuery(sgqlc.types.Interface):
    """Class for SuggestedNrqlQuery.

    Interface type representing a query suggestion.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql", "title")
    nrql = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="nrql")


class WhatsNewContent(sgqlc.types.Interface):
    """Class for WhatsNewContent.

    Represents the details in common between all types of news.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "content_type",
        "context",
        "id",
        "publish_date",
        "summary",
        "title",
    )
    content_type = sgqlc.types.Field(
        sgqlc.types.non_null(WhatsNewContentType), graphql_name="contentType"
    )


class WorkloadStatusResult(sgqlc.types.Interface):
    """Class for WorkloadStatusResult.

    The details of a status that was involved in the calculation of
    the workload status.
    """

    __schema__ = nerdgraph
    __field_names__ = ("source", "value")
    source = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadStatusSource), graphql_name="source"
    )


class Entity(sgqlc.types.Interface):
    """Class for Entity.

    The `Entity` interface allows fetching detailed entity information
    for a single entity.  To understand more about entities and entity
    types, look at [our docs](https://docs.newrelic.com/docs/what-are-
    new-relic-entities).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account",
        "account_id",
        "alert_severity",
        "alert_violations",
        "deployment_search",
        "domain",
        "entity_type",
        "first_indexed_at",
        "golden_metrics",
        "golden_tags",
        "guid",
        "indexed_at",
        "last_reporting_change_at",
        "name",
        "nerd_storage",
        "nrdb_query",
        "permalink",
        "recent_alert_violations",
        "related_entities",
        "reporting",
        "service_level",
        "tags",
        "tags_with_metadata",
        "tracing_summary",
        "type",
    )
    account = sgqlc.types.Field("AccountOutline", graphql_name="account")

    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class EntityOutline(sgqlc.types.Interface):
    """Class for EntityOutline.

    The `EntityOutline` interface object allows fetching basic entity
    data for many entities at a time.  To understand more about
    entities and entity types, look at [our
    docs](https://docs.newrelic.com/docs/what-are-new-relic-entities).
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account",
        "account_id",
        "alert_severity",
        "domain",
        "entity_type",
        "first_indexed_at",
        "golden_metrics",
        "golden_tags",
        "guid",
        "indexed_at",
        "last_reporting_change_at",
        "name",
        "permalink",
        "reporting",
        "service_level",
        "tags",
        "type",
    )
    account = sgqlc.types.Field("AccountOutline", graphql_name="account")

    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class Account(sgqlc.types.Type):
    """Class for Account.

    The `Account` object provides general data about the account, as
    well as being the entry point into more detailed data about a
    single account.  Account configuration data is queried through
    this object, as well as telemetry data that is specific to a
    single account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "agent_environment",
        "ai_decisions",
        "ai_issues",
        "ai_notifications",
        "ai_topology",
        "ai_workflows",
        "alerts",
        "cloud",
        "data_management",
        "edge",
        "events_to_metrics",
        "historical_data_export",
        "id",
        "incident_intelligence_environment",
        "installation",
        "log_configurations",
        "metric_normalization",
        "name",
        "nerd_storage",
        "nrql",
        "nrql_drop_rules",
        "pixie",
        "streaming_export",
        "synthetics",
        "workload",
    )
    agent_environment = sgqlc.types.Field(
        "AgentEnvironmentAccountStitchedFields", graphql_name="agentEnvironment"
    )


class AccountManagementCreateResponse(sgqlc.types.Type):
    """Class for AccountManagementCreateResponse.

    The return object for a create-account mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("managed_account",)
    managed_account = sgqlc.types.Field(
        "AccountManagementManagedAccount", graphql_name="managedAccount"
    )


class AccountManagementManagedAccount(sgqlc.types.Type):
    """Class for AccountManagementManagedAccount.

    Account data view for administration tasks.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "name", "region_code")
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")


class AccountManagementOrganizationStitchedFields(sgqlc.types.Type):
    """Class for AccountManagementOrganizationStitchedFields.

    The field type for stitching into the NerdGraph schema.
    """

    __schema__ = nerdgraph
    __field_names__ = ("managed_accounts",)
    managed_accounts = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AccountManagementManagedAccount)),
        graphql_name="managedAccounts",
    )


class AccountManagementUpdateResponse(sgqlc.types.Type):
    """Class for AccountManagementUpdateResponse.

    The return object for an update-account mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("managed_account",)
    managed_account = sgqlc.types.Field(
        AccountManagementManagedAccount, graphql_name="managedAccount"
    )


class AccountOutline(sgqlc.types.Type):
    """Class for AccountOutline.

    The `AccountOutline` object provides basic data about an account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "name", "reporting_event_types")
    id = sgqlc.types.Field(Int, graphql_name="id")

    name = sgqlc.types.Field(String, graphql_name="name")

    reporting_event_types = sgqlc.types.Field(
        sgqlc.types.list_of(String),
        graphql_name="reportingEventTypes",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filter",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String), graphql_name="filter", default=None
                    ),
                ),
                (
                    "time_window",
                    sgqlc.types.Arg(
                        TimeWindowInput, graphql_name="timeWindow", default=None
                    ),
                ),
            )
        ),
    )


class AccountReference(sgqlc.types.Type):
    """Class for AccountReference.

    The `AccountReference` object provides basic identifying
    information about the account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(Int, graphql_name="id")

    name = sgqlc.types.Field(String, graphql_name="name")


class Actor(sgqlc.types.Type):
    """Class for Actor.

    The `Actor` object contains fields that are scoped to the API
    user's access level.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account",
        "accounts",
        "api_access",
        "cloud",
        "dashboard",
        "distributed_tracing",
        "entities",
        "entity",
        "entity_search",
        "errors_inbox",
        "incident_intelligence_environment",
        "mobile_push_notification",
        "nerd_storage",
        "nerd_storage_vault",
        "nerdpacks",
        "nr1_catalog",
        "nrql",
        "organization",
        "pixie",
        "query_history",
        "user",
        "users",
    )
    account = sgqlc.types.Field(
        Account,
        graphql_name="account",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )


class AgentApplicationApmBrowserSettings(sgqlc.types.Type):
    """Class for AgentApplicationApmBrowserSettings.

    The settings of a browser application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("cookies_enabled", "distributed_tracing_enabled", "loader_type")
    cookies_enabled = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="cookiesEnabled"
    )


class AgentApplicationBrowserSettings(sgqlc.types.Type):
    """Class for AgentApplicationBrowserSettings.

    The settings of a browser application. Includes loader script.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "cookies_enabled",
        "distributed_tracing_enabled",
        "loader_script",
        "loader_type",
    )
    cookies_enabled = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="cookiesEnabled"
    )


class AgentApplicationCreateBrowserResult(sgqlc.types.Type):
    """Class for AgentApplicationCreateBrowserResult.

    The result of creating a browser application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("guid", "name", "settings")
    guid = sgqlc.types.Field(sgqlc.types.non_null(EntityGuid), graphql_name="guid")


class AgentApplicationCreateMobileResult(sgqlc.types.Type):
    """Class for AgentApplicationCreateMobileResult.

    The result of creating a mobile application.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "application_token",
        "entity_outline",
        "guid",
        "name",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AgentApplicationDeleteResult(sgqlc.types.Type):
    """Class for AgentApplicationDeleteResult.

    The result of deleting an application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("success",)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="success")


class AgentApplicationEnableBrowserResult(sgqlc.types.Type):
    """Class for AgentApplicationEnableBrowserResult.

    The result of enabling browser monitoring for an APM-monitored
    application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "settings")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AgentApplicationSettingsApmBase(sgqlc.types.Type):
    """Class for AgentApplicationSettingsApmBase.

    Settings that are applicable to APM applications and their agents.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "alias",
        "apm_config",
        "error_collector",
        "jfr",
        "original_name",
        "slow_sql",
        "thread_profiler",
        "tracer_type",
        "transaction_tracer",
    )
    alias = sgqlc.types.Field(String, graphql_name="alias")


class AgentApplicationSettingsApmConfig(sgqlc.types.Type):
    """Class for AgentApplicationSettingsApmConfig.

    General settings related to APM applications.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apdex_target", "use_server_side_config")
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class AgentApplicationSettingsBrowserAjax(sgqlc.types.Type):
    """Class for AgentApplicationSettingsBrowserAjax.

    Browser Ajax.
    """

    __schema__ = nerdgraph
    __field_names__ = ("deny_list",)
    deny_list = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="denyList"
    )


class AgentApplicationSettingsBrowserBase(sgqlc.types.Type):
    """Class for AgentApplicationSettingsBrowserBase.

    Settings that are applicable to browser applications.
    """

    __schema__ = nerdgraph
    __field_names__ = ("browser_config", "browser_monitoring")
    browser_config = sgqlc.types.Field(
        sgqlc.types.non_null("AgentApplicationSettingsBrowserConfig"),
        graphql_name="browserConfig",
    )


class AgentApplicationSettingsBrowserConfig(sgqlc.types.Type):
    """Class for AgentApplicationSettingsBrowserConfig.

    General settings related to APM applications.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apdex_target",)
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class AgentApplicationSettingsBrowserDistributedTracing(sgqlc.types.Type):
    """Class for AgentApplicationSettingsBrowserDistributedTracing.

    Distributed tracing type. See
    [documentation](https://docs.newrelic.com/docs/browser/new-relic-
    browser/browser-pro-features/browser-data-distributed-tracing/)
    for further information.
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


class AgentApplicationSettingsBrowserMonitoring(sgqlc.types.Type):
    """Class for AgentApplicationSettingsBrowserMonitoring.

    Browser monitoring.
    """

    __schema__ = nerdgraph
    __field_names__ = ("ajax", "distributed_tracing", "loader", "privacy")
    ajax = sgqlc.types.Field(AgentApplicationSettingsBrowserAjax, graphql_name="ajax")


class AgentApplicationSettingsBrowserPrivacy(sgqlc.types.Type):
    """Class for AgentApplicationSettingsBrowserPrivacy.

    Browser privacy. See
    [documentation](https://docs.newrelic.com/docs/browser/browser-
    monitoring/page-load-timing-resources/cookie-collection-session-
    tracking/) for further information.
    """

    __schema__ = nerdgraph
    __field_names__ = ("cookies_enabled",)
    cookies_enabled = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="cookiesEnabled"
    )


class AgentApplicationSettingsBrowserProperties(sgqlc.types.Type):
    """Class for AgentApplicationSettingsBrowserProperties.

    General Properties related to browser applications.
    """

    __schema__ = nerdgraph
    __field_names__ = ("js_loader_script",)
    js_loader_script = sgqlc.types.Field(String, graphql_name="jsLoaderScript")


class AgentApplicationSettingsErrorCollector(sgqlc.types.Type):
    """Class for AgentApplicationSettingsErrorCollector.

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


class AgentApplicationSettingsIgnoredStatusCodeRule(sgqlc.types.Type):
    """Class for AgentApplicationSettingsIgnoredStatusCodeRule.

    A configuration setting used ignore status codes associated with
    different hosts.
    """

    __schema__ = nerdgraph
    __field_names__ = ("hosts", "status_codes")
    hosts = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="hosts"
    )


class AgentApplicationSettingsJfr(sgqlc.types.Type):
    """Class for AgentApplicationSettingsJfr.

    Access to the enabled state of the Java Flight Recorder. This
    feature only available on the Java language agent version 8.0.0 or
    later.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsMobileBase(sgqlc.types.Type):
    """Class for AgentApplicationSettingsMobileBase.

    Settings that are applicable to mobile applications.
    """

    __schema__ = nerdgraph
    __field_names__ = ("network_settings", "use_crash_reports")
    network_settings = sgqlc.types.Field(
        "AgentApplicationSettingsMobileNetworkSettings", graphql_name="networkSettings"
    )


class AgentApplicationSettingsMobileNetworkSettings(sgqlc.types.Type):
    """Class for AgentApplicationSettingsMobileNetworkSettings.

    An object containing your network settings.
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
            sgqlc.types.non_null("AgentApplicationSettingsNetworkAlias")
        ),
        graphql_name="aliases",
    )


class AgentApplicationSettingsMobileProperties(sgqlc.types.Type):
    """Class for AgentApplicationSettingsMobileProperties.

    General properties related to mobile applications.
    """

    __schema__ = nerdgraph
    __field_names__ = ("application_token",)
    application_token = sgqlc.types.Field(SecureValue, graphql_name="applicationToken")


class AgentApplicationSettingsNetworkAlias(sgqlc.types.Type):
    """Class for AgentApplicationSettingsNetworkAlias.

    A configuration setting that maps hosts to alias names for
    grouping and identification purposes.
    """

    __schema__ = nerdgraph
    __field_names__ = ("alias", "hosts")
    alias = sgqlc.types.Field(String, graphql_name="alias")


class AgentApplicationSettingsSlowSql(sgqlc.types.Type):
    """Class for AgentApplicationSettingsSlowSql.

    In APM, when transaction traces are collected, there may be
    additional Slow query data available.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsThreadProfiler(sgqlc.types.Type):
    """Class for AgentApplicationSettingsThreadProfiler.

    Measures wall clock time, CPU time, and method call counts in your
    application's threads as they run.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled",)
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class AgentApplicationSettingsTransactionTracer(sgqlc.types.Type):
    """Class for AgentApplicationSettingsTransactionTracer.

    Transaction tracer settings related to APM applications. For more
    information about what these settings do and which ones are
    applicable for your application, please see
    https://docs.newrelic.com for more information about agent
    configuration for your language agent.
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


class AgentApplicationSettingsUpdateError(sgqlc.types.Type):
    """Class for AgentApplicationSettingsUpdateError.

    Information about any errors encountered while updating values.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "error_class", "field")
    description = sgqlc.types.Field(String, graphql_name="description")


class AgentApplicationSettingsUpdateResult(sgqlc.types.Type):
    """Class for AgentApplicationSettingsUpdateResult.

    The result of updating application settings.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "alias",
        "apm_settings",
        "browser_properties",
        "browser_settings",
        "errors",
        "guid",
        "mobile_settings",
    )
    alias = sgqlc.types.Field(String, graphql_name="alias")


class AgentEnvironmentAccountApplicationLoadedModules(sgqlc.types.Type):
    """Class for AgentEnvironmentAccountApplicationLoadedModules.

    Data found for one application instance's loaded modules.
    """

    __schema__ = nerdgraph
    __field_names__ = ("application_guids", "details", "loaded_modules")
    application_guids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid))),
        graphql_name="applicationGuids",
    )


class AgentEnvironmentAccountApplicationLoadedModulesResults(sgqlc.types.Type):
    """Class for AgentEnvironmentAccountApplicationLoadedModulesResults.

    Results for loaded modules search. This list is paginated. Use the
    cursor to go through all the available results.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "results")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class AgentEnvironmentAccountEnvironmentAttributesResults(sgqlc.types.Type):
    """Class for AgentEnvironmentAccountEnvironmentAttributesResults.

    Results for environment attributes search. This list is paginated.
    Use the cursor to go through all the available results.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "results")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class AgentEnvironmentAccountStitchedFields(sgqlc.types.Type):
    """Class for AgentEnvironmentAccountStitchedFields.

    account-scope schemas.
    """

    __schema__ = nerdgraph
    __field_names__ = ("agent_settings_attributes", "environment_attributes", "modules")
    agent_settings_attributes = sgqlc.types.Field(
        AgentEnvironmentAccountEnvironmentAttributesResults,
        graphql_name="agentSettingsAttributes",
        args=sgqlc.types.ArgDict(
            (
                (
                    "cursor",
                    sgqlc.types.Arg(String, graphql_name="cursor", default=None),
                ),
                (
                    "filter",
                    sgqlc.types.Arg(
                        AgentEnvironmentFilter, graphql_name="filter", default=None
                    ),
                ),
            )
        ),
    )


class AgentEnvironmentApplicationEnvironmentAttributes(sgqlc.types.Type):
    """Class for AgentEnvironmentApplicationEnvironmentAttributes.

    Environment data found for one application instance.
    """

    __schema__ = nerdgraph
    __field_names__ = ("application_guids", "attributes", "details")
    application_guids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid))),
        graphql_name="applicationGuids",
    )


class AgentEnvironmentApplicationInstance(sgqlc.types.Type):
    """Class for AgentEnvironmentApplicationInstance.

    Representation of the New Relic agent collecting data.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "agent_settings_attributes",
        "details",
        "environment_attributes",
        "modules",
    )
    agent_settings_attributes = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("AgentEnvironmentAttribute")),
        graphql_name="agentSettingsAttributes",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filter",
                    sgqlc.types.Arg(
                        AgentEnvironmentFilter, graphql_name="filter", default=None
                    ),
                ),
            )
        ),
    )


class AgentEnvironmentApplicationInstanceDetails(sgqlc.types.Type):
    """Class for AgentEnvironmentApplicationInstanceDetails.

    Details of an application instance such as host and language.
    """

    __schema__ = nerdgraph
    __field_names__ = ("host", "id", "language", "name")
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="host")


class AgentEnvironmentApplicationInstancesResult(sgqlc.types.Type):
    """Class for AgentEnvironmentApplicationInstancesResult.

    List of APM application instances with pagination data.
    """

    __schema__ = nerdgraph
    __field_names__ = ("application_instances", "next_cursor")
    application_instances = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AgentEnvironmentApplicationInstance)),
        graphql_name="applicationInstances",
    )


class AgentEnvironmentApplicationLoadedModule(sgqlc.types.Type):
    """Class for AgentEnvironmentApplicationLoadedModule.

    Represents a module loaded by the apm application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attributes", "name", "version")
    attributes = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of("AgentEnvironmentLoadedModuleAttribute")
        ),
        graphql_name="attributes",
    )


class AgentEnvironmentAttribute(sgqlc.types.Type):
    """Class for AgentEnvironmentAttribute.

    Represents one attribute from within the environment on which an
    agent is running.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "value")
    attribute = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attribute"
    )


class AgentEnvironmentLoadedModuleAttribute(sgqlc.types.Type):
    """Class for AgentEnvironmentLoadedModuleAttribute.

    Attribute belonging to a loaded module.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "value")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AgentFeatures(sgqlc.types.Type):
    """Class for AgentFeatures.

    Features of the Agent.
    """

    __schema__ = nerdgraph
    __field_names__ = ("min_version", "name")
    min_version = sgqlc.types.Field(String, graphql_name="minVersion")


class AgentRelease(sgqlc.types.Type):
    """Class for AgentRelease.

    Information about an Agent release.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "bugs",
        "date",
        "download_link",
        "features",
        "security",
        "version",
    )
    bugs = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="bugs")


class AiDecisionsAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("decision", "decisions")
    decision = sgqlc.types.Field(
        "AiDecisionsDecision",
        graphql_name="decision",
        args=sgqlc.types.ArgDict(
            (
                (
                    "decision_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="decisionId",
                        default=None,
                    ),
                ),
            )
        ),
    )


class AiDecisionsAnnotationEntry(sgqlc.types.Type):
    """Class for AiDecisionsAnnotationEntry.

    A key-value entry.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class AiDecisionsApplicableIncidentSearch(sgqlc.types.Type):
    """Class for AiDecisionsApplicableIncidentSearch.

    A search for a subset of incidents that may be relevant for a
    given rule expression.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "completed_at",
        "created_at",
        "error_message",
        "id",
        "incidents_scanned",
        "results",
        "updated_at",
    )
    completed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name="completedAt")


class AiDecisionsDecision(sgqlc.types.Type):
    """Class for AiDecisionsDecision.

    A decision used to compare incidents and subsequently merge
    issues.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "annotations",
        "correlation_window_length",
        "created_at",
        "creator",
        "decision_expression",
        "decision_type",
        "description",
        "id",
        "metadata",
        "min_correlation_threshold",
        "name",
        "override_configuration",
        "source",
        "state",
        "updated_at",
    )
    annotations = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiDecisionsAnnotationEntry))
        ),
        graphql_name="annotations",
    )


class AiDecisionsDecisionListing(sgqlc.types.Type):
    """Class for AiDecisionsDecisionListing.

    Windowed view of an account's decisions.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "decisions", "next_cursor", "prev_cursor")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class AiDecisionsMergeFeedback(sgqlc.types.Type):
    """Class for AiDecisionsMergeFeedback.

    Represents a piece of user feedback for a merge.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "child_issue_id",
        "opinion",
        "parent_issue_id",
        "rule_id",
        "user_id",
    )
    child_issue_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="childIssueId"
    )


class AiDecisionsOperationResult(sgqlc.types.Type):
    """Class for AiDecisionsOperationResult.

    Result of an operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("result",)
    result = sgqlc.types.Field(
        sgqlc.types.non_null(AiDecisionsResultType), graphql_name="result"
    )


class AiDecisionsOpinionEntry(sgqlc.types.Type):
    """Class for AiDecisionsOpinionEntry.

    Represents a number of opinions.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "opinion")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class AiDecisionsOverrideConfiguration(sgqlc.types.Type):
    """Class for AiDecisionsOverrideConfiguration.

    Configuration for overriding properties of issues created by
    merges.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "priority", "title")
    description = sgqlc.types.Field(String, graphql_name="description")


class AiDecisionsRule(sgqlc.types.Type):
    """Class for AiDecisionsRule.

    A correlation rule used to compare incidents and subsequently
    merge issues.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "annotations",
        "correlation_window_length",
        "created_at",
        "creator",
        "description",
        "id",
        "metadata",
        "min_correlation_threshold",
        "name",
        "override_configuration",
        "rule_expression",
        "rule_type",
        "source",
        "state",
        "updated_at",
    )
    annotations = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiDecisionsAnnotationEntry))
        ),
        graphql_name="annotations",
    )


class AiDecisionsRuleMetadata(sgqlc.types.Type):
    """Class for AiDecisionsRuleMetadata.

    Metadata about a decision.
    """

    __schema__ = nerdgraph
    __field_names__ = ("merge_opinion_count",)
    merge_opinion_count = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiDecisionsOpinionEntry))
        ),
        graphql_name="mergeOpinionCount",
    )


class AiDecisionsSelectorApplicability(sgqlc.types.Type):
    """Class for AiDecisionsSelectorApplicability.

    Number of incidents applicable for a selector.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "select")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class AiDecisionsSelectorExamples(sgqlc.types.Type):
    """Class for AiDecisionsSelectorExamples.

    Example subset of incidents applicable for a selector.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incidents", "select")
    incidents = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))),
        graphql_name="incidents",
    )


class AiDecisionsSimulation(sgqlc.types.Type):
    """Class for AiDecisionsSimulation.

    Simulation of a rule expression for a certain period of time.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "candidate_incidents",
        "completed_at",
        "created_at",
        "error_message",
        "id",
        "incidents_applicable",
        "incidents_correlated",
        "incidents_ingested",
        "incidents_processed",
        "progress",
        "updated_at",
    )
    candidate_incidents = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID)))
            )
        ),
        graphql_name="candidateIncidents",
    )


class AiDecisionsSuggestion(sgqlc.types.Type):
    """Class for AiDecisionsSuggestion.

    A suggested correlation rule.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "correlation_window_length",
        "created_at",
        "description",
        "hash",
        "id",
        "min_correlation_threshold",
        "name",
        "override_configuration",
        "rule_expression",
        "state",
        "suggester",
        "support",
    )
    correlation_window_length = sgqlc.types.Field(
        Milliseconds, graphql_name="correlationWindowLength"
    )


class AiIssuesAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = (
        "config_by_environment",
        "incidents",
        "incidents_events",
        "issues",
        "issues_events",
    )
    config_by_environment = sgqlc.types.Field(
        "AiIssuesConfigurationByEnvironment", graphql_name="configByEnvironment"
    )


class AiIssuesConfigurationByEnvironment(sgqlc.types.Type):
    """Class for AiIssuesConfigurationByEnvironment.

    Configuration per environment.
    """

    __schema__ = nerdgraph
    __field_names__ = ("config",)
    config = sgqlc.types.Field(
        "AiIssuesEnvironmentConfiguration", graphql_name="config"
    )


class AiIssuesConfigurationOverrideResponse(sgqlc.types.Type):
    """Class for AiIssuesConfigurationOverrideResponse.

    Response for configuration override.
    """

    __schema__ = nerdgraph
    __field_names__ = ("config", "error")
    config = sgqlc.types.Field(
        "AiIssuesEnvironmentConfiguration", graphql_name="config"
    )


class AiIssuesEnvironmentConfiguration(sgqlc.types.Type):
    """Class for AiIssuesEnvironmentConfiguration.

    Environment configuration object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "flapping_interval",
        "grace_period",
        "inactive_period",
        "incident_timeout",
        "issue_ttl",
        "max_issue_size",
    )
    flapping_interval = sgqlc.types.Field(Seconds, graphql_name="flappingInterval")


class AiIssuesGracePeriodConfig(sgqlc.types.Type):
    """Class for AiIssuesGracePeriodConfig.

    Grace period config per priority.
    """

    __schema__ = nerdgraph
    __field_names__ = ("period", "priority")
    period = sgqlc.types.Field(sgqlc.types.non_null(Seconds), graphql_name="period")


class AiIssuesIncidentData(sgqlc.types.Type):
    """Class for AiIssuesIncidentData.

    Incidents data.
    """

    __schema__ = nerdgraph
    __field_names__ = ("incidents", "next_cursor")
    incidents = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiIssuesIIncident))
        ),
        graphql_name="incidents",
    )


class AiIssuesIssue(sgqlc.types.Type):
    """Class for AiIssuesIssue.

    Issue.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_ids",
        "acknowledged_at",
        "acknowledged_by",
        "activated_at",
        "closed_at",
        "closed_by",
        "condition_family_id",
        "condition_name",
        "condition_product",
        "correlation_rule_descriptions",
        "correlation_rule_ids",
        "correlation_rule_names",
        "created_at",
        "data_ml_modules",
        "deep_link_url",
        "description",
        "entity_guids",
        "entity_names",
        "entity_types",
        "environment_id",
        "event_type",
        "incident_ids",
        "is_correlated",
        "is_idle",
        "issue_id",
        "merge_reason",
        "muting_state",
        "origins",
        "parent_merge_id",
        "policy_ids",
        "policy_name",
        "priority",
        "sources",
        "state",
        "title",
        "total_incidents",
        "un_acknowledged_at",
        "un_acknowledged_by",
        "updated_at",
        "wildcard",
    )
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )


class AiIssuesIssueData(sgqlc.types.Type):
    """Class for AiIssuesIssueData.

    Issues data.
    """

    __schema__ = nerdgraph
    __field_names__ = ("issues", "next_cursor")
    issues = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AiIssuesIssue))),
        graphql_name="issues",
    )


class AiIssuesIssueUserActionResponse(sgqlc.types.Type):
    """Class for AiIssuesIssueUserActionResponse.

    Response for user action.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "result")
    error = sgqlc.types.Field(String, graphql_name="error")


class AiIssuesIssueUserActionResult(sgqlc.types.Type):
    """Class for AiIssuesIssueUserActionResult.

    User action for issue.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "action", "issue_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AiIssuesKeyValue(sgqlc.types.Type):
    """Class for AiIssuesKeyValue.

    Key value type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class AiIssuesKeyValues(sgqlc.types.Type):
    """Class for AiIssuesKeyValues.

    Key to values type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class AiNotificationsAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = (
        "channel_schema",
        "channel_suggestions",
        "channels",
        "destination_suggestions",
        "destinations",
        "o_auth_url",
        "variables",
    )
    channel_schema = sgqlc.types.Field(
        "AiNotificationsChannelSchemaResult",
        graphql_name="channelSchema",
        args=sgqlc.types.ArgDict(
            (
                (
                    "channel_type",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(AiNotificationsChannelType),
                        graphql_name="channelType",
                        default=None,
                    ),
                ),
                (
                    "constraints",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(
                            sgqlc.types.non_null(AiNotificationsConstraint)
                        ),
                        graphql_name="constraints",
                        default=None,
                    ),
                ),
                (
                    "destination_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="destinationId",
                        default=None,
                    ),
                ),
                (
                    "product",
                    sgqlc.types.Arg(
                        AiNotificationsProduct, graphql_name="product", default=None
                    ),
                ),
            )
        ),
    )


class AiNotificationsBasicAuth(sgqlc.types.Type):
    """Class for AiNotificationsBasicAuth.

    Basic user and password authentication.
    """

    __schema__ = nerdgraph
    __field_names__ = ("auth_type", "user")
    auth_type = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsAuthType), graphql_name="authType"
    )


class AiNotificationsChannel(sgqlc.types.Type):
    """Class for AiNotificationsChannel.

    Channel object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "active",
        "created_at",
        "destination_id",
        "id",
        "name",
        "product",
        "properties",
        "status",
        "type",
        "updated_at",
        "updated_by",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AiNotificationsChannelResponse(sgqlc.types.Type):
    """Class for AiNotificationsChannelResponse.

    Response for all channel related mutations. Includes relevant
    channel and/or errors.
    """

    __schema__ = nerdgraph
    __field_names__ = ("channel", "error")
    channel = sgqlc.types.Field(AiNotificationsChannel, graphql_name="channel")


class AiNotificationsChannelSchemaResult(sgqlc.types.Type):
    """Class for AiNotificationsChannelSchemaResult.

    Channel schema object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "result", "schema")
    error = sgqlc.types.Field("AiNotificationsError", graphql_name="error")


class AiNotificationsChannelTestResponse(sgqlc.types.Type):
    """Class for AiNotificationsChannelTestResponse.

    Result of a notification test.
    """

    __schema__ = nerdgraph
    __field_names__ = ("details", "error", "evidence", "result")
    details = sgqlc.types.Field(String, graphql_name="details")


class AiNotificationsChannelsResponse(sgqlc.types.Type):
    """Class for AiNotificationsChannelsResponse.

    Channel result object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entities", "error", "next_cursor", "total_count")
    entities = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiNotificationsChannel))
        ),
        graphql_name="entities",
    )


class AiNotificationsConstraintError(sgqlc.types.Type):
    """Class for AiNotificationsConstraintError.

    Missing constraint error. Constraints can be retrieved using
    suggestion api.
    """

    __schema__ = nerdgraph
    __field_names__ = ("dependencies", "name")
    dependencies = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="dependencies",
    )


class AiNotificationsConstraintsError(sgqlc.types.Type):
    """Class for AiNotificationsConstraintsError.

    Object for constraints errors.
    """

    __schema__ = nerdgraph
    __field_names__ = ("constraints",)
    constraints = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiNotificationsConstraintError))
        ),
        graphql_name="constraints",
    )


class AiNotificationsDataValidationError(sgqlc.types.Type):
    """Class for AiNotificationsDataValidationError.

    Object for validation errors.
    """

    __schema__ = nerdgraph
    __field_names__ = ("details", "fields")
    details = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="details")


class AiNotificationsDeleteResponse(sgqlc.types.Type):
    """Class for AiNotificationsDeleteResponse.

    Delete response object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "ids")
    error = sgqlc.types.Field("AiNotificationsResponseError", graphql_name="error")


class AiNotificationsDestination(sgqlc.types.Type):
    """Class for AiNotificationsDestination.

    Destination Object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "active",
        "auth",
        "created_at",
        "id",
        "is_user_authenticated",
        "last_sent",
        "name",
        "properties",
        "status",
        "type",
        "updated_at",
        "updated_by",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AiNotificationsDestinationResponse(sgqlc.types.Type):
    """Class for AiNotificationsDestinationResponse.

    Response for all destinations related mutation. Includes relevant
    destination and/or errors.
    """

    __schema__ = nerdgraph
    __field_names__ = ("destination", "error")
    destination = sgqlc.types.Field(
        AiNotificationsDestination, graphql_name="destination"
    )


class AiNotificationsDestinationTestResponse(sgqlc.types.Type):
    """Class for AiNotificationsDestinationTestResponse.

    Result of a connection test.
    """

    __schema__ = nerdgraph
    __field_names__ = ("details", "error", "result")
    details = sgqlc.types.Field(String, graphql_name="details")


class AiNotificationsDestinationsResponse(sgqlc.types.Type):
    """Class for AiNotificationsDestinationsResponse.

    Destinations result object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entities", "error", "next_cursor", "total_count")
    entities = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiNotificationsDestination))
        ),
        graphql_name="entities",
    )


class AiNotificationsFieldError(sgqlc.types.Type):
    """Class for AiNotificationsFieldError.

    Invalid field object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("field", "message")
    field = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="field")


class AiNotificationsOAuth2Auth(sgqlc.types.Type):
    """Class for AiNotificationsOAuth2Auth.

    OAuth2 based authentication.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "access_token_url",
        "auth_type",
        "authorization_url",
        "client_id",
        "prefix",
        "refresh_interval",
        "refreshable",
        "scope",
    )
    access_token_url = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="accessTokenUrl"
    )


class AiNotificationsOAuthUrlResponse(sgqlc.types.Type):
    """Class for AiNotificationsOAuthUrlResponse.

    OAuth URL response.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "transaction_id", "url")
    error = sgqlc.types.Field("AiNotificationsResponseError", graphql_name="error")


class AiNotificationsProperty(sgqlc.types.Type):
    """Class for AiNotificationsProperty.

    Channel property Object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_value", "key", "label", "value")
    display_value = sgqlc.types.Field(String, graphql_name="displayValue")


class AiNotificationsResponseError(sgqlc.types.Type):
    """Class for AiNotificationsResponseError.

    Response error object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "details", "type")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class AiNotificationsSchema(sgqlc.types.Type):
    """Class for AiNotificationsSchema.

    Channel schema object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("fields",)
    fields = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiNotificationsSchemaField"))
        ),
        graphql_name="fields",
    )


class AiNotificationsSchemaField(sgqlc.types.Type):
    """Class for AiNotificationsSchemaField.

    Schema field object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("component", "key", "label", "mandatory")
    component = sgqlc.types.Field(
        sgqlc.types.non_null("AiNotificationsUiComponent"), graphql_name="component"
    )


class AiNotificationsSelectComponentOptions(sgqlc.types.Type):
    """Class for AiNotificationsSelectComponentOptions.

    Additional options for SELECT type components.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "creatable",
        "dependent_on",
        "filtered_by",
        "label",
        "multiple",
        "searchable",
        "suggestions",
    )
    creatable = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="creatable"
    )


class AiNotificationsSuggestion(sgqlc.types.Type):
    """Class for AiNotificationsSuggestion.

    Suggestion object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_value", "icon", "value")
    display_value = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayValue"
    )


class AiNotificationsSuggestionError(sgqlc.types.Type):
    """Class for AiNotificationsSuggestionError.

    Object for suggestion errors.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class AiNotificationsSuggestionsResponse(sgqlc.types.Type):
    """Class for AiNotificationsSuggestionsResponse.

    Possible values for a field by its key.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entities", "error", "next_cursor", "result", "total_count")
    entities = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiNotificationsSuggestion))
        ),
        graphql_name="entities",
    )


class AiNotificationsTokenAuth(sgqlc.types.Type):
    """Class for AiNotificationsTokenAuth.

    Token based authentication.
    """

    __schema__ = nerdgraph
    __field_names__ = ("auth_type", "prefix")
    auth_type = sgqlc.types.Field(
        sgqlc.types.non_null(AiNotificationsAuthType), graphql_name="authType"
    )


class AiNotificationsUiComponent(sgqlc.types.Type):
    """Class for AiNotificationsUiComponent.

    UI component object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "allow_template_variables",
        "data_validation",
        "default_value",
        "select_options",
        "type",
        "visible_by_default",
    )
    allow_template_variables = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="allowTemplateVariables"
    )


class AiNotificationsVariable(sgqlc.types.Type):
    """Class for AiNotificationsVariable.

    Variable object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "active",
        "category",
        "created_at",
        "description",
        "example",
        "id",
        "key",
        "label",
        "name",
        "product",
        "type",
        "updated_at",
        "updated_by",
    )
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="active")


class AiNotificationsVariableResult(sgqlc.types.Type):
    """Class for AiNotificationsVariableResult.

    Channel result object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entities", "next_cursor", "total_count")
    entities = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiNotificationsVariable))
        ),
        graphql_name="entities",
    )


class AiTopologyAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("edges", "graph", "vertices")
    edges = sgqlc.types.Field(
        sgqlc.types.non_null("AiTopologyEdgeListing"),
        graphql_name="edges",
        args=sgqlc.types.ArgDict(
            (
                (
                    "cursor",
                    sgqlc.types.Arg(String, graphql_name="cursor", default=None),
                ),
                (
                    "edge_ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                        graphql_name="edgeIds",
                        default=None,
                    ),
                ),
            )
        ),
    )


class AiTopologyCollectorOperationResult(sgqlc.types.Type):
    """Class for AiTopologyCollectorOperationResult.

    Result of an operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("result",)
    result = sgqlc.types.Field(
        sgqlc.types.non_null(AiTopologyCollectorResultType), graphql_name="result"
    )


class AiTopologyDefiningAttribute(sgqlc.types.Type):
    """Class for AiTopologyDefiningAttribute.

    A key-value entry representing an attribute name and value.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class AiTopologyEdge(sgqlc.types.Type):
    """Class for AiTopologyEdge.

    A connection between two vertices within a graph.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "directed",
        "from_vertex_id",
        "from_vertex_name",
        "id",
        "to_vertex_id",
        "to_vertex_name",
        "updated_at",
    )
    directed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="directed")


class AiTopologyEdgeListing(sgqlc.types.Type):
    """Class for AiTopologyEdgeListing.

    Listing of edges in a graph.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "cursor", "edges")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class AiTopologyGraph(sgqlc.types.Type):
    """Class for AiTopologyGraph.

    Overview of a graph; all edges and vertices.
    """

    __schema__ = nerdgraph
    __field_names__ = ("edges", "vertices")
    edges = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AiTopologyEdge))),
        graphql_name="edges",
    )


class AiTopologyVertex(sgqlc.types.Type):
    """Class for AiTopologyVertex.

    A vertex is a representation of a node in a graph: a host; an
    application; etc.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "defining_attributes",
        "id",
        "name",
        "updated_at",
        "vertex_class",
    )
    defining_attributes = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiTopologyDefiningAttribute))
        ),
        graphql_name="definingAttributes",
    )


class AiTopologyVertexListing(sgqlc.types.Type):
    """Class for AiTopologyVertexListing.

    Listing of vertices in a graph.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "cursor", "vertices")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class AiWorkflowsAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("workflows",)
    workflows = sgqlc.types.Field(
        "AiWorkflowsWorkflows",
        graphql_name="workflows",
        args=sgqlc.types.ArgDict(
            (
                (
                    "cursor",
                    sgqlc.types.Arg(String, graphql_name="cursor", default=None),
                ),
                (
                    "filters",
                    sgqlc.types.Arg(
                        AiWorkflowsFilters, graphql_name="filters", default=None
                    ),
                ),
            )
        ),
    )


class AiWorkflowsCreateWorkflowResponse(sgqlc.types.Type):
    """Class for AiWorkflowsCreateWorkflowResponse.

    Create workflow mutation response including errors.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "workflow")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiWorkflowsCreateResponseError"))
        ),
        graphql_name="errors",
    )


class AiWorkflowsDeleteWorkflowResponse(sgqlc.types.Type):
    """Class for AiWorkflowsDeleteWorkflowResponse.

    Delete workflow mutation response including errors.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "id")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiWorkflowsDeleteResponseError"))
        ),
        graphql_name="errors",
    )


class AiWorkflowsDestinationConfiguration(sgqlc.types.Type):
    """Class for AiWorkflowsDestinationConfiguration.

    Destination Configuration Object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("channel_id", "name", "notification_triggers", "type")
    channel_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="channelId")


class AiWorkflowsEnrichment(sgqlc.types.Type):
    """Class for AiWorkflowsEnrichment.

    Makes it possible to augment the notification with additional data
    from the New Relic platform.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "configurations",
        "created_at",
        "id",
        "name",
        "type",
        "updated_at",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AiWorkflowsFilter(sgqlc.types.Type):
    """Class for AiWorkflowsFilter.

    Filter Object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "id", "name", "predicates", "type")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AiWorkflowsNrqlConfiguration(sgqlc.types.Type):
    """Class for AiWorkflowsNrqlConfiguration.

    NRQL enrichment configuration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("query",)
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="query")


class AiWorkflowsPredicate(sgqlc.types.Type):
    """Class for AiWorkflowsPredicate.

    Predicate Object.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "operator", "values")
    attribute = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attribute"
    )


class AiWorkflowsTestNotificationResponse(sgqlc.types.Type):
    """Class for AiWorkflowsTestNotificationResponse.

    Notification response according to channel id.
    """

    __schema__ = nerdgraph
    __field_names__ = ("channel_id", "evidence", "status")
    channel_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="channelId")


class AiWorkflowsTestWorkflowResponse(sgqlc.types.Type):
    """Class for AiWorkflowsTestWorkflowResponse.

    Test workflow mutation response including errors.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "notification_responses", "status")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("AiWorkflowsTestResponseError")),
        graphql_name="errors",
    )


class AiWorkflowsUpdateWorkflowResponse(sgqlc.types.Type):
    """Class for AiWorkflowsUpdateWorkflowResponse.

    Update workflow mutation response including errors.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "workflow")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AiWorkflowsUpdateResponseError"))
        ),
        graphql_name="errors",
    )


class AiWorkflowsWorkflow(sgqlc.types.Type):
    """Class for AiWorkflowsWorkflow.

    Workflow object.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "created_at",
        "destination_configurations",
        "destinations_enabled",
        "enrichments",
        "enrichments_enabled",
        "guid",
        "id",
        "issues_filter",
        "last_run",
        "muting_rules_handling",
        "name",
        "updated_at",
        "workflow_enabled",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AiWorkflowsWorkflows(sgqlc.types.Type):
    """Class for AiWorkflowsWorkflows.

    Workflows query response.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entities", "next_cursor", "total_count")
    entities = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AiWorkflowsWorkflow))
        ),
        graphql_name="entities",
    )


class AlertsAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = (
        "muting_rule",
        "muting_rules",
        "notification_channel",
        "notification_channels",
        "nrql_condition",
        "nrql_conditions_search",
        "policies_search",
        "policy",
    )
    muting_rule = sgqlc.types.Field(
        "AlertsMutingRule",
        graphql_name="mutingRule",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )


class AlertsCampfireNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsCampfireNotificationChannelConfig.

    Configuration for Campfire notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class AlertsConditionDeleteResponse(sgqlc.types.Type):
    """Class for AlertsConditionDeleteResponse.

    Success response for deleting an Alerts condition.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class AlertsEmailNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsEmailNotificationChannelConfig.

    Configuration for Email notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("emails", "include_json")
    emails = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="emails",
    )


class AlertsHipChatNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsHipChatNotificationChannelConfig.

    Configuration for HipChat notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class AlertsMutingRule(sgqlc.types.Type):
    """Class for AlertsMutingRule.

    A MutingRule for New Relic Alerts Violations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "condition",
        "created_at",
        "created_by_user",
        "description",
        "enabled",
        "id",
        "name",
        "schedule",
        "status",
        "updated_at",
        "updated_by_user",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AlertsMutingRuleCondition(sgqlc.types.Type):
    """Class for AlertsMutingRuleCondition.

    A condition which describes how to target a New Relic Alerts
    Violation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "operator", "values")
    attribute = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attribute"
    )


class AlertsMutingRuleConditionGroup(sgqlc.types.Type):
    """Class for AlertsMutingRuleConditionGroup.

    A group of MutingRuleConditions combined by an operator.
    """

    __schema__ = nerdgraph
    __field_names__ = ("conditions", "operator")
    conditions = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AlertsMutingRuleCondition))
        ),
        graphql_name="conditions",
    )


class AlertsMutingRuleDeleteResponse(sgqlc.types.Type):
    """Class for AlertsMutingRuleDeleteResponse.

    The success response for deleting a MutingRule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class AlertsMutingRuleSchedule(sgqlc.types.Type):
    """Class for AlertsMutingRuleSchedule.

    The time window when the MutingRule should actively mute
    violations.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "end_repeat",
        "end_time",
        "next_end_time",
        "next_start_time",
        "repeat",
        "repeat_count",
        "start_time",
        "time_zone",
        "weekly_repeat_days",
    )
    end_repeat = sgqlc.types.Field(DateTime, graphql_name="endRepeat")


class AlertsNotificationChannelCreateError(sgqlc.types.Type):
    """Class for AlertsNotificationChannelCreateError.

    The error for creating a notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "error_type")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class AlertsNotificationChannelCreateResponse(sgqlc.types.Type):
    """Class for AlertsNotificationChannelCreateResponse.

    The response for creating a notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "notification_channel")
    error = sgqlc.types.Field(
        AlertsNotificationChannelCreateError, graphql_name="error"
    )


class AlertsNotificationChannelDeleteError(sgqlc.types.Type):
    """Class for AlertsNotificationChannelDeleteError.

    The error for deleting a notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "error_type", "notification_channel_id")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class AlertsNotificationChannelDeleteResponse(sgqlc.types.Type):
    """Class for AlertsNotificationChannelDeleteResponse.

    The response for deleting a notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "id")
    error = sgqlc.types.Field(
        AlertsNotificationChannelDeleteError, graphql_name="error"
    )


class AlertsNotificationChannelId(sgqlc.types.Type):
    """Class for AlertsNotificationChannelId.

    A notification channel ID - temporarily until addToPolicy will
    support returning full notification channels.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class AlertsNotificationChannelPoliciesResultSet(sgqlc.types.Type):
    """Class for AlertsNotificationChannelPoliciesResultSet.

    A result set containing associated policies information for a
    notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("policies", "total_count")
    policies = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("AlertsNotificationChannelPolicy"))
        ),
        graphql_name="policies",
    )


class AlertsNotificationChannelPolicy(sgqlc.types.Type):
    """Class for AlertsNotificationChannelPolicy.

    Information about a policy associated with a notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class AlertsNotificationChannelUpdateError(sgqlc.types.Type):
    """Class for AlertsNotificationChannelUpdateError.

    The error for updating a notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "error_type", "notification_channel_id")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class AlertsNotificationChannelUpdateResponse(sgqlc.types.Type):
    """Class for AlertsNotificationChannelUpdateResponse.

    The response for updating a notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "notification_channel")
    error = sgqlc.types.Field(
        AlertsNotificationChannelUpdateError, graphql_name="error"
    )


class AlertsNotificationChannelsAddToPolicyError(sgqlc.types.Type):
    """Class for AlertsNotificationChannelsAddToPolicyError.

    The error for associating notification channels with a policy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "error_type", "notification_channel_id")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class AlertsNotificationChannelsAddToPolicyResponse(sgqlc.types.Type):
    """Class for AlertsNotificationChannelsAddToPolicyResponse.

    The response for associating notification channels with a policy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "notification_channels", "policy_id")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(AlertsNotificationChannelsAddToPolicyError)
            )
        ),
        graphql_name="errors",
    )


class AlertsNotificationChannelsRemoveFromPolicyError(sgqlc.types.Type):
    """Class for AlertsNotificationChannelsRemoveFromPolicyError.

    The error for dissociating notification channels from a policy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "error_type", "notification_channel_id")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class AlertsNotificationChannelsRemoveFromPolicyResponse(sgqlc.types.Type):
    """Class for AlertsNotificationChannelsRemoveFromPolicyResponse.

    The response for dissociating notification channels from a policy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "notification_channels", "policy_id")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(AlertsNotificationChannelsRemoveFromPolicyError)
            )
        ),
        graphql_name="errors",
    )


class AlertsNotificationChannelsResultSet(sgqlc.types.Type):
    """Class for AlertsNotificationChannelsResultSet.

    A result set containing multiple notification channels and
    pagination info.
    """

    __schema__ = nerdgraph
    __field_names__ = ("channels", "next_cursor", "total_count")
    channels = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AlertsNotificationChannel))
        ),
        graphql_name="channels",
    )


class AlertsNrqlConditionExpiration(sgqlc.types.Type):
    """Class for AlertsNrqlConditionExpiration.

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


class AlertsNrqlConditionQuery(sgqlc.types.Type):
    """Class for AlertsNrqlConditionQuery.

    Information for generating the condition NRQL query. Output from
    the evaluated NRQL query will be compared to the condition terms
    to detect violations.
    """

    __schema__ = nerdgraph
    __field_names__ = ("query",)
    query = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="query")


class AlertsNrqlConditionSignal(sgqlc.types.Type):
    """Class for AlertsNrqlConditionSignal.

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
        "fill_option",
        "fill_value",
        "slide_by",
    )
    aggregation_delay = sgqlc.types.Field(Seconds, graphql_name="aggregationDelay")


class AlertsNrqlConditionTerms(sgqlc.types.Type):
    """Class for AlertsNrqlConditionTerms.

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


class AlertsNrqlConditionsSearchResultSet(sgqlc.types.Type):
    """Class for AlertsNrqlConditionsSearchResultSet.

    A collection of NRQL conditions with pagination information.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "nrql_conditions", "total_count")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class AlertsOpsGenieNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsOpsGenieNotificationChannelConfig.

    Configuration for OpsGenie notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("api_key", "data_center_region", "recipients", "tags", "teams")
    api_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiKey"
    )


class AlertsPagerDutyNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsPagerDutyNotificationChannelConfig.

    Configuration for PagerDuty notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("api_key",)
    api_key = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="apiKey"
    )


class AlertsPoliciesSearchResultSet(sgqlc.types.Type):
    """Class for AlertsPoliciesSearchResultSet.

    Collection of policies with pagination information.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "policies", "total_count")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class AlertsPolicy(sgqlc.types.Type):
    """Class for AlertsPolicy.

    Container for conditions with associated notifications channels.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "id", "incident_preference", "name")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class AlertsPolicyDeleteResponse(sgqlc.types.Type):
    """Class for AlertsPolicyDeleteResponse.

    Success response when deleting an Alerts policy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class AlertsSlackNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsSlackNotificationChannelConfig.

    Configuration for Slack notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("team_channel", "url")
    team_channel = sgqlc.types.Field(String, graphql_name="teamChannel")


class AlertsUserNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsUserNotificationChannelConfig.

    Configuration for user notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class AlertsVictorOpsNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsVictorOpsNotificationChannelConfig.

    Configuration for VictorOps notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "route_key")
    key = sgqlc.types.Field(sgqlc.types.non_null(SecureValue), graphql_name="key")


class AlertsWebhookBasicAuthInput(sgqlc.types.Type):
    """Class for AlertsWebhookBasicAuthInput.

    Webhook basic auth.
    """

    __schema__ = nerdgraph
    __field_names__ = ("password", "username")
    password = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="password"
    )


class AlertsWebhookCustomHeaderInput(sgqlc.types.Type):
    """Class for AlertsWebhookCustomHeaderInput.

    Webhook header.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "value")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class AlertsWebhookNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsWebhookNotificationChannelConfig.

    Configuration for Webhook notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "base_url",
        "basic_auth",
        "custom_http_headers",
        "custom_payload_body",
        "custom_payload_type",
    )
    base_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="baseUrl")


class AlertsXMattersNotificationChannelConfig(sgqlc.types.Type):
    """Class for AlertsXMattersNotificationChannelConfig.

    Configuration for xMatters notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("integration_url",)
    integration_url = sgqlc.types.Field(
        sgqlc.types.non_null(SecureValue), graphql_name="integrationUrl"
    )


class ApiAccessActorStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("key", "key_search")
    key = sgqlc.types.Field(
        ApiAccessKey,
        graphql_name="key",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "key_type",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ApiAccessKeyType),
                        graphql_name="keyType",
                        default=None,
                    ),
                ),
            )
        ),
    )


class ApiAccessCreateKeyResponse(sgqlc.types.Type):
    """Class for ApiAccessCreateKeyResponse.

    The response of the create keys mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_keys", "errors")
    created_keys = sgqlc.types.Field(
        sgqlc.types.list_of(ApiAccessKey), graphql_name="createdKeys"
    )


class ApiAccessDeleteKeyResponse(sgqlc.types.Type):
    """Class for ApiAccessDeleteKeyResponse.

    The response of the key delete mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("deleted_keys", "errors")
    deleted_keys = sgqlc.types.Field(
        sgqlc.types.list_of("ApiAccessDeletedKey"), graphql_name="deletedKeys"
    )


class ApiAccessDeletedKey(sgqlc.types.Type):
    """Class for ApiAccessDeletedKey.

    The deleted key response of the key delete mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(String, graphql_name="id")


class ApiAccessKeySearchResult(sgqlc.types.Type):
    """Class for ApiAccessKeySearchResult.

    A list of all keys scoped to the current actor.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "keys", "next_cursor")
    count = sgqlc.types.Field(Int, graphql_name="count")


class ApiAccessUpdateKeyResponse(sgqlc.types.Type):
    """Class for ApiAccessUpdateKeyResponse.

    The response of the update keys mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "updated_keys")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(ApiAccessKeyError), graphql_name="errors"
    )


class ApmApplicationDeployment(sgqlc.types.Type):
    """Class for ApmApplicationDeployment.

    An APM application deployment marker.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "changelog",
        "description",
        "permalink",
        "revision",
        "timestamp",
        "user",
    )
    changelog = sgqlc.types.Field(String, graphql_name="changelog")


class ApmApplicationEntitySettingsResult(sgqlc.types.Type):
    """Class for ApmApplicationEntitySettingsResult.

    The updated settings of an ApmApplicationEntity.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity",)
    entity = sgqlc.types.Field("ApmApplicationEntity", graphql_name="entity")


class ApmApplicationRunningAgentVersions(sgqlc.types.Type):
    """Class for ApmApplicationRunningAgentVersions.

    Represents the currently running agent versions in an APM
    Application. An application could be running multiple versions of
    an agent (across different hosts, for example).
    """

    __schema__ = nerdgraph
    __field_names__ = ("max_version", "min_version")
    max_version = sgqlc.types.Field(String, graphql_name="maxVersion")


class ApmApplicationSettings(sgqlc.types.Type):
    """Class for ApmApplicationSettings.

    Configuration settings for the APM Application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apdex_target", "server_side_config")
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class ApmApplicationSummaryData(sgqlc.types.Type):
    """Class for ApmApplicationSummaryData.

    Summary statistics about the APM App.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_score",
        "error_rate",
        "host_count",
        "instance_count",
        "non_web_response_time_average",
        "non_web_throughput",
        "response_time_average",
        "throughput",
        "web_response_time_average",
        "web_throughput",
    )
    apdex_score = sgqlc.types.Field(Float, graphql_name="apdexScore")


class ApmBrowserApplicationSummaryData(sgqlc.types.Type):
    """Class for ApmBrowserApplicationSummaryData.

    Summary statistics about the Browser App injected by the APM
    Application.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "ajax_request_throughput",
        "ajax_response_time_average",
        "js_error_rate",
        "page_load_throughput",
        "page_load_time_average",
    )
    ajax_request_throughput = sgqlc.types.Field(
        Float, graphql_name="ajaxRequestThroughput"
    )


class ApmExternalServiceSummaryData(sgqlc.types.Type):
    """Class for ApmExternalServiceSummaryData.

    Summary statistics about an External Service called by an APM App.
    """

    __schema__ = nerdgraph
    __field_names__ = ("response_time_average", "throughput")
    response_time_average = sgqlc.types.Field(
        Seconds, graphql_name="responseTimeAverage"
    )


class AuthorizationManagementAuthenticationDomain(sgqlc.types.Type):
    """Class for AuthorizationManagementAuthenticationDomain.

    An "authentication domain" is a grouping of New Relic users
    governed by the same user management settings, like how they're
    provisioned (added and updated), how they're authenticated (logged
    in), session settings, and how user upgrades are managed.
    """

    __schema__ = nerdgraph
    __field_names__ = ("groups", "id", "name")
    groups = sgqlc.types.Field(
        sgqlc.types.non_null("AuthorizationManagementGroupSearch"),
        graphql_name="groups",
        args=sgqlc.types.ArgDict(
            (
                (
                    "cursor",
                    sgqlc.types.Arg(String, graphql_name="cursor", default=None),
                ),
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                        graphql_name="id",
                        default=None,
                    ),
                ),
            )
        ),
    )


class AuthorizationManagementAuthenticationDomainSearch(sgqlc.types.Type):
    """Class for AuthorizationManagementAuthenticationDomainSearch.

    container for authentication domains enabling cursor based
    pagination.
    """

    __schema__ = nerdgraph
    __field_names__ = ("authentication_domains", "next_cursor", "total_count")
    authentication_domains = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(AuthorizationManagementAuthenticationDomain)
            )
        ),
        graphql_name="authenticationDomains",
    )


class AuthorizationManagementGrantAccessPayload(sgqlc.types.Type):
    """Class for AuthorizationManagementGrantAccessPayload.

    Autogenerated return type of GrantAccess.
    """

    __schema__ = nerdgraph
    __field_names__ = ("roles",)
    roles = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null("AuthorizationManagementGrantedRole")
            )
        ),
        graphql_name="roles",
    )


class AuthorizationManagementGrantedRole(sgqlc.types.Type):
    """Class for AuthorizationManagementGrantedRole.

    A Granted Role represents the access given to a group.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "display_name",
        "id",
        "name",
        "organization_id",
        "role_id",
        "type",
    )
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class AuthorizationManagementGrantedRoleSearch(sgqlc.types.Type):
    """Class for AuthorizationManagementGrantedRoleSearch.

    container for roles enabling cursor based pagination.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "roles", "total_count")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class AuthorizationManagementGroup(sgqlc.types.Type):
    """Class for AuthorizationManagementGroup.

    For users on our New Relic One user model, a "group" represents a
    group of users. Putting users in a group allows the managing of
    permissions for multiple users at the same time.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_name", "id", "roles")
    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )


class AuthorizationManagementGroupSearch(sgqlc.types.Type):
    """Class for AuthorizationManagementGroupSearch.

    container for groups enabling cursor based pagination.
    """

    __schema__ = nerdgraph
    __field_names__ = ("groups", "next_cursor", "total_count")
    groups = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(AuthorizationManagementGroup))
        ),
        graphql_name="groups",
    )


class AuthorizationManagementOrganizationStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("authentication_domains", "roles")
    authentication_domains = sgqlc.types.Field(
        AuthorizationManagementAuthenticationDomainSearch,
        graphql_name="authenticationDomains",
        args=sgqlc.types.ArgDict(
            (
                (
                    "cursor",
                    sgqlc.types.Arg(String, graphql_name="cursor", default=None),
                ),
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                        graphql_name="id",
                        default=None,
                    ),
                ),
            )
        ),
    )


class AuthorizationManagementRevokeAccessPayload(sgqlc.types.Type):
    """Class for AuthorizationManagementRevokeAccessPayload.

    Autogenerated return type of RevokeAccess.
    """

    __schema__ = nerdgraph
    __field_names__ = ("roles",)
    roles = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(AuthorizationManagementGrantedRole)
            )
        ),
        graphql_name="roles",
    )


class AuthorizationManagementRole(sgqlc.types.Type):
    """Class for AuthorizationManagementRole.

    a role grants access on an account or organization to groups of
    users.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_name", "id", "name", "scope", "type")
    display_name = sgqlc.types.Field(String, graphql_name="displayName")


class AuthorizationManagementRoleSearch(sgqlc.types.Type):
    """Class for AuthorizationManagementRoleSearch.

    container for roles enabling cursor based pagination.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "roles", "total_count")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class BrowserApplicationRunningAgentVersions(sgqlc.types.Type):
    """Class for BrowserApplicationRunningAgentVersions.

    Represents the currently running agent versions in a Browser App.
    An app could be running multiple versions of an agent (across
    different browsers, for example).
    """

    __schema__ = nerdgraph
    __field_names__ = ("max_version", "min_version")
    max_version = sgqlc.types.Field(Int, graphql_name="maxVersion")


class BrowserApplicationSettings(sgqlc.types.Type):
    """Class for BrowserApplicationSettings.

    Configuration settings for the Browser App.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apdex_target",)
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class BrowserApplicationSummaryData(sgqlc.types.Type):
    """Class for BrowserApplicationSummaryData.

    Summary statistics about the Browser App.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "ajax_request_throughput",
        "ajax_response_time_average",
        "js_error_rate",
        "page_load_throughput",
        "page_load_time_average",
        "page_load_time_median",
        "spa_response_time_average",
        "spa_response_time_median",
    )
    ajax_request_throughput = sgqlc.types.Field(
        Float, graphql_name="ajaxRequestThroughput"
    )


class ChangeTrackingDeployment(sgqlc.types.Type):
    """Class for ChangeTrackingDeployment.

    A deployment.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "changelog",
        "commit",
        "deep_link",
        "deployment_id",
        "deployment_type",
        "description",
        "entity_guid",
        "group_id",
        "timestamp",
        "user",
        "version",
    )
    changelog = sgqlc.types.Field(String, graphql_name="changelog")


class ChangeTrackingDeploymentSearchResult(sgqlc.types.Type):
    """Class for ChangeTrackingDeploymentSearchResult.

    The result of the deployment search query.
    """

    __schema__ = nerdgraph
    __field_names__ = ("results",)
    results = sgqlc.types.Field(
        sgqlc.types.list_of(ChangeTrackingDeployment), graphql_name="results"
    )


class CloudAccountFields(sgqlc.types.Type):
    """Class for CloudAccountFields.

    Cloud integrations related data, including configured integrations
    and all available cloud provider service integrations.
    """

    __schema__ = nerdgraph
    __field_names__ = ("linked_account", "linked_accounts", "provider", "providers")
    linked_account = sgqlc.types.Field(
        "CloudLinkedAccount",
        graphql_name="linkedAccount",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(Int, graphql_name="id", default=None)),)
        ),
    )


class CloudAccountMutationError(sgqlc.types.Type):
    """Class for CloudAccountMutationError.

    Account Mutation Error.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "linked_account_id",
        "message",
        "nr_account_id",
        "provider_slug",
        "type",
    )
    linked_account_id = sgqlc.types.Field(Int, graphql_name="linkedAccountId")


class CloudActorFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("linked_accounts",)
    linked_accounts = sgqlc.types.Field(
        sgqlc.types.list_of("CloudLinkedAccount"),
        graphql_name="linkedAccounts",
        args=sgqlc.types.ArgDict(
            (
                (
                    "provider",
                    sgqlc.types.Arg(String, graphql_name="provider", default=None),
                ),
            )
        ),
    )


class CloudConfigureIntegrationPayload(sgqlc.types.Type):
    """Class for CloudConfigureIntegrationPayload.

    Autogenerated return type of ConfigureIntegration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "integrations")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("CloudIntegrationMutationError"))
        ),
        graphql_name="errors",
    )


class CloudDisableIntegrationPayload(sgqlc.types.Type):
    """Class for CloudDisableIntegrationPayload.

    Autogenerated return type of DisableIntegration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("disabled_integrations", "errors")
    disabled_integrations = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(CloudIntegration))
        ),
        graphql_name="disabledIntegrations",
    )


class CloudIntegrationMutationError(sgqlc.types.Type):
    """Class for CloudIntegrationMutationError.

    Integration Mutation Error.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "integration_slug",
        "linked_account_id",
        "message",
        "nr_account_id",
        "type",
    )
    integration_slug = sgqlc.types.Field(String, graphql_name="integrationSlug")


class CloudLinkAccountPayload(sgqlc.types.Type):
    """Class for CloudLinkAccountPayload.

    Autogenerated return type of LinkAccount.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "linked_accounts")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(CloudAccountMutationError))
        ),
        graphql_name="errors",
    )


class CloudLinkedAccount(sgqlc.types.Type):
    """Class for CloudLinkedAccount.

    A cloud account linked to a NewRelic account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "auth_label",
        "created_at",
        "disabled",
        "external_id",
        "id",
        "integration",
        "integrations",
        "metric_collection_mode",
        "name",
        "nr_account_id",
        "provider",
        "updated_at",
    )
    auth_label = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="authLabel"
    )


class CloudMigrateAwsGovCloudToAssumeRolePayload(sgqlc.types.Type):
    """Class for CloudMigrateAwsGovCloudToAssumeRolePayload.

    Autogenerated return type of MigrateAwsGovCloudToAssumeRole.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "linked_accounts")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(CloudAccountMutationError))
        ),
        graphql_name="errors",
    )


class CloudRenameAccountPayload(sgqlc.types.Type):
    """Class for CloudRenameAccountPayload.

    Autogenerated return type of RenameAccount.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "linked_accounts")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(CloudAccountMutationError))
        ),
        graphql_name="errors",
    )


class CloudService(sgqlc.types.Type):
    """Class for CloudService.

    A Cloud Provider service available for monitoring.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "icon",
        "id",
        "is_enabled",
        "name",
        "provider",
        "slug",
        "updated_at",
    )
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(EpochSeconds), graphql_name="createdAt"
    )


class CloudUnlinkAccountPayload(sgqlc.types.Type):
    """Class for CloudUnlinkAccountPayload.

    Autogenerated return type of UnlinkAccount.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "unlinked_accounts")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(CloudAccountMutationError))
        ),
        graphql_name="errors",
    )


class CrossAccountNrdbResultContainer(sgqlc.types.Type):
    """Class for CrossAccountNrdbResultContainer.

    A data structure that contains the results of the multi account
    NRDB query along with other capabilities that enhance those
    results.  Direct query results are available through `results`,
    `totalResult` and `otherResult`. The query you made is accessible
    through `nrql`, along with `metadata` about the query itself.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "current_results",
        "metadata",
        "nrql",
        "other_result",
        "previous_results",
        "query_progress",
        "raw_response",
        "results",
        "total_result",
    )
    current_results = sgqlc.types.Field(
        sgqlc.types.list_of(NrdbResult), graphql_name="currentResults"
    )


class DashboardActorStitchedFields(sgqlc.types.Type):
    """Class for DashboardActorStitchedFields.

    Type defined so its fields will be merged directly into
    NerdGraph's Actor type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("live_urls",)
    live_urls = sgqlc.types.Field(
        "DashboardLiveUrlResult",
        graphql_name="liveUrls",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filter",
                    sgqlc.types.Arg(
                        DashboardLiveUrlsFilterInput,
                        graphql_name="filter",
                        default=None,
                    ),
                ),
            )
        ),
    )


class DashboardAddWidgetsToPageError(sgqlc.types.Type):
    """Class for DashboardAddWidgetsToPageError.

    Expected errors that can be returned by addWidgetsToPage
    operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardAddWidgetsToPageResult(sgqlc.types.Type):
    """Class for DashboardAddWidgetsToPageResult.

    Result of addWidgetsToPage operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(DashboardAddWidgetsToPageError), graphql_name="errors"
    )


class DashboardAreaWidgetConfiguration(sgqlc.types.Type):
    """Class for DashboardAreaWidgetConfiguration.

    Configuration for visualization type 'viz.area'.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of("DashboardWidgetNrqlQuery"), graphql_name="nrqlQueries"
    )


class DashboardBarWidgetConfiguration(sgqlc.types.Type):
    """Class for DashboardBarWidgetConfiguration.

    Configuration for visualization type 'viz.bar'.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of("DashboardWidgetNrqlQuery"), graphql_name="nrqlQueries"
    )


class DashboardBillboardWidgetConfiguration(sgqlc.types.Type):
    """Class for DashboardBillboardWidgetConfiguration.

    Configuration for visualization type 'viz.billboard'.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries", "thresholds")
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of("DashboardWidgetNrqlQuery"), graphql_name="nrqlQueries"
    )


class DashboardBillboardWidgetThreshold(sgqlc.types.Type):
    """Class for DashboardBillboardWidgetThreshold.

    Billboard widget threshold.
    """

    __schema__ = nerdgraph
    __field_names__ = ("alert_severity", "value")
    alert_severity = sgqlc.types.Field(
        DashboardAlertSeverity, graphql_name="alertSeverity"
    )


class DashboardCreateError(sgqlc.types.Type):
    """Class for DashboardCreateError.

    Expected errors that can be returned by create operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardCreateResult(sgqlc.types.Type):
    """Class for DashboardCreateResult.

    Result of create operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_result", "errors")
    entity_result = sgqlc.types.Field(
        "DashboardEntityResult", graphql_name="entityResult"
    )


class DashboardDeleteError(sgqlc.types.Type):
    """Class for DashboardDeleteError.

    Expected error types that can be returned by delete operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardDeleteResult(sgqlc.types.Type):
    """Class for DashboardDeleteResult.

    Result of delete operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "status")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(DashboardDeleteError), graphql_name="errors"
    )


class DashboardEntityOwnerInfo(sgqlc.types.Type):
    """Class for DashboardEntityOwnerInfo.

    Dashboard owner.
    """

    __schema__ = nerdgraph
    __field_names__ = ("email", "user_id")
    email = sgqlc.types.Field(String, graphql_name="email")


class DashboardEntityResult(sgqlc.types.Type):
    """Class for DashboardEntityResult.

    Public schema - `DashboardEntity` result representation for
    mutations. It's a subset of the `DashboardEntity` that inherits
    from the Entity type, but a complete different type.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "created_at",
        "description",
        "guid",
        "name",
        "owner",
        "pages",
        "permissions",
        "updated_at",
        "variables",
    )
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class DashboardLineWidgetConfiguration(sgqlc.types.Type):
    """Class for DashboardLineWidgetConfiguration.

    Configuration for visualization type 'viz.line'.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of("DashboardWidgetNrqlQuery"), graphql_name="nrqlQueries"
    )


class DashboardLiveUrl(sgqlc.types.Type):
    """Class for DashboardLiveUrl.

    Live URL.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_at", "title", "type", "url", "uuid")
    created_at = sgqlc.types.Field(EpochMilliseconds, graphql_name="createdAt")


class DashboardLiveUrlError(sgqlc.types.Type):
    """Class for DashboardLiveUrlError.

    Live URL error.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardLiveUrlResult(sgqlc.types.Type):
    """Class for DashboardLiveUrlResult.

    Live URL result.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "live_urls")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(DashboardLiveUrlError), graphql_name="errors"
    )


class DashboardMarkdownWidgetConfiguration(sgqlc.types.Type):
    """Class for DashboardMarkdownWidgetConfiguration.

    Configuration for visualization type 'viz.markdown'.
    """

    __schema__ = nerdgraph
    __field_names__ = ("text",)
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="text")


class DashboardOwnerInfo(sgqlc.types.Type):
    """Class for DashboardOwnerInfo.

    Information on the owner of a dashboard or page.
    """

    __schema__ = nerdgraph
    __field_names__ = ("email", "user_id")
    email = sgqlc.types.Field(String, graphql_name="email")


class DashboardPage(sgqlc.types.Type):
    """Class for DashboardPage.

    Page in a dashboard entity.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "description",
        "guid",
        "name",
        "owner",
        "updated_at",
        "widgets",
    )
    created_at = sgqlc.types.Field(DateTime, graphql_name="createdAt")


class DashboardPieWidgetConfiguration(sgqlc.types.Type):
    """Class for DashboardPieWidgetConfiguration.

    Configuration for visualization type 'viz.pie'.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of("DashboardWidgetNrqlQuery"), graphql_name="nrqlQueries"
    )


class DashboardRevokeLiveUrlResult(sgqlc.types.Type):
    """Class for DashboardRevokeLiveUrlResult.

    Revoke live URL result.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "uuid")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(DashboardLiveUrlError), graphql_name="errors"
    )


class DashboardTableWidgetConfiguration(sgqlc.types.Type):
    """Class for DashboardTableWidgetConfiguration.

    Configuration for visualization type 'viz.table'.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql_queries",)
    nrql_queries = sgqlc.types.Field(
        sgqlc.types.list_of("DashboardWidgetNrqlQuery"), graphql_name="nrqlQueries"
    )


class DashboardUndeleteError(sgqlc.types.Type):
    """Class for DashboardUndeleteError.

    Expected error types that can be returned by undelete operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardUndeleteResult(sgqlc.types.Type):
    """Class for DashboardUndeleteResult.

    Result of undelete operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(DashboardUndeleteError), graphql_name="errors"
    )


class DashboardUpdateError(sgqlc.types.Type):
    """Class for DashboardUpdateError.

    Expected errors that can be returned by update operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardUpdatePageError(sgqlc.types.Type):
    """Class for DashboardUpdatePageError.

    Expected errors that can be returned by updatePage operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardUpdatePageResult(sgqlc.types.Type):
    """Class for DashboardUpdatePageResult.

    Result of updatePage operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(DashboardUpdatePageError), graphql_name="errors"
    )


class DashboardUpdateResult(sgqlc.types.Type):
    """Class for DashboardUpdateResult.

    Result of update operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_result", "errors")
    entity_result = sgqlc.types.Field(
        DashboardEntityResult, graphql_name="entityResult"
    )


class DashboardUpdateWidgetsInPageError(sgqlc.types.Type):
    """Class for DashboardUpdateWidgetsInPageError.

    Expected errors that can be returned by updateWidgetsInPage
    operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(String, graphql_name="description")


class DashboardUpdateWidgetsInPageResult(sgqlc.types.Type):
    """Class for DashboardUpdateWidgetsInPageResult.

    Result of updateWidgetsInPage operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(DashboardUpdateWidgetsInPageError), graphql_name="errors"
    )


class DashboardVariable(sgqlc.types.Type):
    """Class for DashboardVariable.

    Definition of a variable that is local to this dashboard.
    Variables are placeholders for dynamic values in widget NRQLs.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "default_values",
        "is_multi_selection",
        "items",
        "name",
        "nrql_query",
        "replacement_strategy",
        "title",
        "type",
    )
    default_values = sgqlc.types.Field(
        sgqlc.types.list_of("DashboardVariableDefaultItem"),
        graphql_name="defaultValues",
    )


class DashboardVariableDefaultItem(sgqlc.types.Type):
    """Class for DashboardVariableDefaultItem.

    Represents a possible default value item.
    """

    __schema__ = nerdgraph
    __field_names__ = ("value",)
    value = sgqlc.types.Field("DashboardVariableDefaultValue", graphql_name="value")


class DashboardVariableDefaultValue(sgqlc.types.Type):
    """Class for DashboardVariableDefaultValue.

    Specifies a default value for variables.
    """

    __schema__ = nerdgraph
    __field_names__ = ("string",)
    string = sgqlc.types.Field(String, graphql_name="string")


class DashboardVariableEnumItem(sgqlc.types.Type):
    """Class for DashboardVariableEnumItem.

    Represents a possible value for a variable of type ENUM.
    """

    __schema__ = nerdgraph
    __field_names__ = ("title", "value")
    title = sgqlc.types.Field(String, graphql_name="title")


class DashboardVariableNrqlQuery(sgqlc.types.Type):
    """Class for DashboardVariableNrqlQuery.

    Configuration for variables of type NRQL.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "query")
    account_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="accountIds")


class DashboardWidget(sgqlc.types.Type):
    """Class for DashboardWidget.

    Widgets in a Dashboard Page.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "configuration",
        "id",
        "layout",
        "linked_entities",
        "raw_configuration",
        "title",
        "visualization",
    )
    configuration = sgqlc.types.Field(
        "DashboardWidgetConfiguration", graphql_name="configuration"
    )


class DashboardWidgetConfiguration(sgqlc.types.Type):
    """Class for DashboardWidgetConfiguration.

    Typed configuration for known visualizations. Only one (at most)
    will be populated for a given widget.
    """

    __schema__ = nerdgraph
    __field_names__ = ("area", "bar", "billboard", "line", "markdown", "pie", "table")
    area = sgqlc.types.Field(DashboardAreaWidgetConfiguration, graphql_name="area")


class DashboardWidgetLayout(sgqlc.types.Type):
    """Class for DashboardWidgetLayout.

    Widget layout.
    """

    __schema__ = nerdgraph
    __field_names__ = ("column", "height", "row", "width")
    column = sgqlc.types.Field(Int, graphql_name="column")


class DashboardWidgetNrqlQuery(sgqlc.types.Type):
    """Class for DashboardWidgetNrqlQuery.

    Single NRQL query for a widget.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "query")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class DashboardWidgetVisualization(sgqlc.types.Type):
    """Class for DashboardWidgetVisualization.

    Visualization configuration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(String, graphql_name="id")


class DataDictionaryAttribute(sgqlc.types.Type):
    """Class for DataDictionaryAttribute.

    Attribute object that contains data about the attribute.
    """

    __schema__ = nerdgraph
    __field_names__ = ("definition", "docs_url", "name", "units")
    definition = sgqlc.types.Field(
        sgqlc.types.non_null(String),
        graphql_name="definition",
        args=sgqlc.types.ArgDict(
            (
                (
                    "format",
                    sgqlc.types.Arg(
                        DataDictionaryTextFormat, graphql_name="format", default="PLAIN"
                    ),
                ),
            )
        ),
    )


class DataDictionaryDataSource(sgqlc.types.Type):
    """Class for DataDictionaryDataSource.

    The source generating the event data.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name",)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class DataDictionaryDocsStitchedFields(sgqlc.types.Type):
    """Class for DataDictionaryDocsStitchedFields.

    Event data definitions, where they come from, and information
    about the attributes they contain.
    """

    __schema__ = nerdgraph
    __field_names__ = ("events",)
    events = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("DataDictionaryEvent"))
        ),
        graphql_name="events",
        args=sgqlc.types.ArgDict(
            (
                (
                    "names",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String), graphql_name="names", default=None
                    ),
                ),
            )
        ),
    )


class DataDictionaryEvent(sgqlc.types.Type):
    """Class for DataDictionaryEvent.

    Event object that contains data about the event and its attributes.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attributes", "data_sources", "definition", "name")
    attributes = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(DataDictionaryAttribute))
        ),
        graphql_name="attributes",
    )


class DataDictionaryUnit(sgqlc.types.Type):
    """Class for DataDictionaryUnit.

    The unit of measurement.
    """

    __schema__ = nerdgraph
    __field_names__ = ("label",)
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="label")


class DataManagementAccountLimit(sgqlc.types.Type):
    """Class for DataManagementAccountLimit.

    Account Limit.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "category",
        "description",
        "documentation_link",
        "limit_reached_behavior_description",
        "name",
        "time_interval",
        "unit",
        "value",
    )
    category = sgqlc.types.Field(DataManagementCategory, graphql_name="category")


class DataManagementAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = (
        "customizable_retention",
        "event_retention_policies",
        "event_retention_rule",
        "event_retention_rules",
        "feature_settings",
        "limits",
        "retention_audit",
        "retentions",
    )
    customizable_retention = sgqlc.types.Field(
        "DataManagementCustomizableRetention", graphql_name="customizableRetention"
    )


class DataManagementAppliedRules(sgqlc.types.Type):
    """Class for DataManagementAppliedRules.

    Applied rules.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "retention_in_days")
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class DataManagementBulkCopyResult(sgqlc.types.Type):
    """Class for DataManagementBulkCopyResult.

    Result for bulk retention copy to an account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("failure", "success")
    failure = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="failure")


class DataManagementCustomizableRetention(sgqlc.types.Type):
    """Class for DataManagementCustomizableRetention.

    Wrapper object for customizable retention namespaces.
    """

    __schema__ = nerdgraph
    __field_names__ = ("event_namespaces",)
    event_namespaces = sgqlc.types.Field(
        sgqlc.types.list_of("DataManagementEventNamespaces"),
        graphql_name="eventNamespaces",
    )


class DataManagementEventNamespaces(sgqlc.types.Type):
    """Class for DataManagementEventNamespaces.

    Event namespace.
    """

    __schema__ = nerdgraph
    __field_names__ = ("max_retention_in_days", "min_retention_in_days", "namespace")
    max_retention_in_days = sgqlc.types.Field(Int, graphql_name="maxRetentionInDays")


class DataManagementFeatureSetting(sgqlc.types.Type):
    """Class for DataManagementFeatureSetting.

    Feature Setting.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled", "key", "locked", "name")
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class DataManagementNamespaceLevelRetention(sgqlc.types.Type):
    """Class for DataManagementNamespaceLevelRetention.

    Namespace level retention.
    """

    __schema__ = nerdgraph
    __field_names__ = ("retention_in_days",)
    retention_in_days = sgqlc.types.Field(Int, graphql_name="retentionInDays")


class DataManagementRenderedRetention(sgqlc.types.Type):
    """Class for DataManagementRenderedRetention.

    An account's current retention values for a namespace.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "namespace",
        "namespace_level_retention",
        "updated_at",
    )
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class DataManagementRetention(sgqlc.types.Type):
    """Class for DataManagementRetention.

    Wrapper object for retention namespaces.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "customizable",
        "max_retention_in_days",
        "min_retention_in_days",
        "namespace",
        "source",
    )
    customizable = sgqlc.types.Field(Boolean, graphql_name="customizable")


class DataManagementRetentionValues(sgqlc.types.Type):
    """Class for DataManagementRetentionValues.

    Wrapper object for namespace retention values.
    """

    __schema__ = nerdgraph
    __field_names__ = ("applied_rules", "namespace", "subscription_retention_in_days")
    applied_rules = sgqlc.types.Field(
        sgqlc.types.list_of(DataManagementAppliedRules), graphql_name="appliedRules"
    )


class DataManagementRule(sgqlc.types.Type):
    """Class for DataManagementRule.

    A rule for setting a data retention value for a particular event
    namespace on an account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "created_by_id",
        "deleted_at",
        "deleted_by_id",
        "id",
        "namespace",
        "retention_in_days",
    )
    created_at = sgqlc.types.Field(EpochSeconds, graphql_name="createdAt")


class DateTimeWindow(sgqlc.types.Type):
    """Class for DateTimeWindow.

    Represents a date time window.
    """

    __schema__ = nerdgraph
    __field_names__ = ("end_time", "start_time")
    end_time = sgqlc.types.Field(DateTime, graphql_name="endTime")


class DistributedTracingActorStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("trace",)
    trace = sgqlc.types.Field(
        "DistributedTracingTrace",
        graphql_name="trace",
        args=sgqlc.types.ArgDict(
            (
                (
                    "timestamp",
                    sgqlc.types.Arg(
                        EpochMilliseconds, graphql_name="timestamp", default=None
                    ),
                ),
                (
                    "trace_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="traceId",
                        default=None,
                    ),
                ),
            )
        ),
    )


class DistributedTracingEntityTracingSummary(sgqlc.types.Type):
    """Class for DistributedTracingEntityTracingSummary.

    Details tracing summary data for the provided `EntityGuid` that
    occurred during the provided `startTime` and `endTime`.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error_trace_count", "percent_of_all_error_traces")
    error_trace_count = sgqlc.types.Field(Int, graphql_name="errorTraceCount")


class DistributedTracingSpan(sgqlc.types.Type):
    """Class for DistributedTracingSpan.

    The primary building block of a distributed trace.  An individual
    unit of work.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "attributes",
        "client_type",
        "duration_ms",
        "entity_guid",
        "id",
        "name",
        "parent_id",
        "process_boundary",
        "span_anomalies",
        "timestamp",
        "trace_id",
    )
    attributes = sgqlc.types.Field(
        DistributedTracingSpanAttributes, graphql_name="attributes"
    )


class DistributedTracingSpanAnomaly(sgqlc.types.Type):
    """Class for DistributedTracingSpanAnomaly.

    An anomaly detected with respect to an attribute of a span.
    """

    __schema__ = nerdgraph
    __field_names__ = ("anomalous_value", "anomaly_type", "average_measure")
    anomalous_value = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="anomalousValue"
    )


class DistributedTracingSpanConnection(sgqlc.types.Type):
    """Class for DistributedTracingSpanConnection.

    A relationship between a parent and child span.
    """

    __schema__ = nerdgraph
    __field_names__ = ("child", "parent")
    child = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="child")


class DistributedTracingTrace(sgqlc.types.Type):
    """Class for DistributedTracingTrace.

    A collection of spans with context describing those spans.  The
    trace represents the complete processing of a request.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "backend_duration_ms",
        "duration_ms",
        "entities",
        "entity_count",
        "id",
        "span_connections",
        "spans",
        "timestamp",
    )
    backend_duration_ms = sgqlc.types.Field(
        Milliseconds, graphql_name="backendDurationMs"
    )


class DocumentationFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = (
        "agent_features",
        "agent_releases",
        "data_dictionary",
        "time_zones",
        "whats_new",
    )
    agent_features = sgqlc.types.Field(
        sgqlc.types.list_of(AgentFeatures),
        graphql_name="agentFeatures",
        args=sgqlc.types.ArgDict(
            (
                (
                    "agent_name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(AgentFeaturesFilter),
                        graphql_name="agentName",
                        default=None,
                    ),
                ),
            )
        ),
    )


class DomainType(sgqlc.types.Type):
    """Class for DomainType.

    Details about an entity type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("domain", "type")
    domain = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="domain")


class EdgeAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("tracing",)
    tracing = sgqlc.types.Field("EdgeTracing", graphql_name="tracing")


class EdgeCreateSpanAttributeRuleResponseError(sgqlc.types.Type):
    """Class for EdgeCreateSpanAttributeRuleResponseError.

    Description of errors that may occur while attempting to create a
    span attribute trace filter rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class EdgeCreateSpanAttributeRulesResponse(sgqlc.types.Type):
    """Class for EdgeCreateSpanAttributeRulesResponse.

    Successfully created span attribute trace filter rule, or one or
    more error responses if there were issues.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "rules")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(EdgeCreateSpanAttributeRuleResponseError),
        graphql_name="errors",
    )


class EdgeCreateTraceFilterRuleResponses(sgqlc.types.Type):
    """Class for EdgeCreateTraceFilterRuleResponses.

    Array of responses, one for each span attribute trace filter rule
    creation request.
    """

    __schema__ = nerdgraph
    __field_names__ = ("span_attribute_rules",)
    span_attribute_rules = sgqlc.types.Field(
        sgqlc.types.non_null(EdgeCreateSpanAttributeRulesResponse),
        graphql_name="spanAttributeRules",
    )


class EdgeCreateTraceObserverResponse(sgqlc.types.Type):
    """Class for EdgeCreateTraceObserverResponse.

    Successfully created trace observers, or one or more error
    responses if there were issues.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "trace_observer")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of("EdgeCreateTraceObserverResponseError"),
        graphql_name="errors",
    )


class EdgeCreateTraceObserverResponseError(sgqlc.types.Type):
    """Class for EdgeCreateTraceObserverResponseError.

    Description of errors that may occur while attempting to create a
    trace observer.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class EdgeCreateTraceObserverResponses(sgqlc.types.Type):
    """Class for EdgeCreateTraceObserverResponses.

    Array of responses, one for each trace observer creation request.
    """

    __schema__ = nerdgraph
    __field_names__ = ("responses",)
    responses = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(EdgeCreateTraceObserverResponse))
        ),
        graphql_name="responses",
    )


class EdgeDataSource(sgqlc.types.Type):
    """Class for EdgeDataSource.

    A data source (i.e., New Relic entity) that is associated with
    this trace observer. Currently, we support adding Browser, Lambda,
    and Mobile entities as data sources.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity", "status")
    entity = sgqlc.types.Field(EntityOutline, graphql_name="entity")


class EdgeDataSourceGroup(sgqlc.types.Type):
    """Class for EdgeDataSourceGroup.

    A group of data sources that are associated with this trace
    observer.
    """

    __schema__ = nerdgraph
    __field_names__ = ("data_sources",)
    data_sources = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EdgeDataSource))),
        graphql_name="dataSources",
    )


class EdgeDeleteSpanAttributeRuleResponse(sgqlc.types.Type):
    """Class for EdgeDeleteSpanAttributeRuleResponse.

    Successfully deleted span attribute trace filter rule, or one or
    more error responses if there were issues.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "rule")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of("EdgeDeleteSpanAttributeRuleResponseError"),
        graphql_name="errors",
    )


class EdgeDeleteSpanAttributeRuleResponseError(sgqlc.types.Type):
    """Class for EdgeDeleteSpanAttributeRuleResponseError.

    Description of errors that may occur while attempting to delete a
    span attribute trace filter.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class EdgeDeleteTraceFilterRuleResponses(sgqlc.types.Type):
    """Class for EdgeDeleteTraceFilterRuleResponses.

    Array of responses, one for each trace filter rule deletion
    request.
    """

    __schema__ = nerdgraph
    __field_names__ = ("span_attribute_rules",)
    span_attribute_rules = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(EdgeDeleteSpanAttributeRuleResponse)
            )
        ),
        graphql_name="spanAttributeRules",
    )


class EdgeDeleteTraceObserverResponse(sgqlc.types.Type):
    """Class for EdgeDeleteTraceObserverResponse.

    Successfully deleted trace observers, or one or more error
    responses if there were issues.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "trace_observer")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of("EdgeDeleteTraceObserverResponseError"),
        graphql_name="errors",
    )


class EdgeDeleteTraceObserverResponseError(sgqlc.types.Type):
    """Class for EdgeDeleteTraceObserverResponseError.

    Description of errors that may occur while attempting to delete a
    trace observer.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class EdgeDeleteTraceObserverResponses(sgqlc.types.Type):
    """Class for EdgeDeleteTraceObserverResponses.

    Array of responses, one for each trace observer deletion request.
    """

    __schema__ = nerdgraph
    __field_names__ = ("responses",)
    responses = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(EdgeDeleteTraceObserverResponse))
        ),
        graphql_name="responses",
    )


class EdgeEndpoint(sgqlc.types.Type):
    """Class for EdgeEndpoint.

    An `Endpoint` describes access to an endpoint pointing to a trace
    observer. Currently, only one endpoint per trace observer is
    supported.
    """

    __schema__ = nerdgraph
    __field_names__ = ("agent", "endpoint_type", "https", "status")
    agent = sgqlc.types.Field(
        sgqlc.types.non_null("EdgeAgentEndpointDetail"), graphql_name="agent"
    )


class EdgeRandomTraceFilter(sgqlc.types.Type):
    """Class for EdgeRandomTraceFilter.

    Contains all of the data that is used to sample traces based on
    random selection.
    """

    __schema__ = nerdgraph
    __field_names__ = ("percent_kept",)
    percent_kept = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="percentKept"
    )


class EdgeSpanAttributeRule(sgqlc.types.Type):
    """Class for EdgeSpanAttributeRule.

    A `SpanAttributeRule` applies a filtering rule (keep or discard)
    to traces within a particular `TraceObserver`.
    """

    __schema__ = nerdgraph
    __field_names__ = ("action", "id", "key", "key_operator", "value", "value_operator")
    action = sgqlc.types.Field(
        sgqlc.types.non_null(EdgeTraceFilterAction), graphql_name="action"
    )


class EdgeSpanAttributesTraceFilter(sgqlc.types.Type):
    """Class for EdgeSpanAttributesTraceFilter.

    Contains all of the data that is used to sample traces based on
    their attributes.
    """

    __schema__ = nerdgraph
    __field_names__ = ("span_attribute_rules",)
    span_attribute_rules = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(EdgeSpanAttributeRule))
        ),
        graphql_name="spanAttributeRules",
    )


class EdgeTraceFilters(sgqlc.types.Type):
    """Class for EdgeTraceFilters.

    A container for all trace filter rule types.
    """

    __schema__ = nerdgraph
    __field_names__ = ("random_trace_filter", "span_attributes_trace_filter")
    random_trace_filter = sgqlc.types.Field(
        sgqlc.types.non_null(EdgeRandomTraceFilter), graphql_name="randomTraceFilter"
    )


class EdgeTraceObserver(sgqlc.types.Type):
    """Class for EdgeTraceObserver.

    A `TraceObserver` handles a group of tracing services for an
    account family.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "compliance_types",
        "data_source_group",
        "endpoints",
        "id",
        "monitoring_account_id",
        "name",
        "provider_region",
        "status",
        "trace_filters",
    )
    compliance_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EdgeComplianceTypeCode)),
        graphql_name="complianceTypes",
    )


class EdgeTracing(sgqlc.types.Type):
    """Class for EdgeTracing.

    This field provides access to Tracing data.
    """

    __schema__ = nerdgraph
    __field_names__ = ("trace_observers",)
    trace_observers = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EdgeTraceObserver)),
        graphql_name="traceObservers",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(sgqlc.types.non_null(Int)),
                        graphql_name="ids",
                        default=None,
                    ),
                ),
            )
        ),
    )


class EdgeUpdateTraceObserverResponse(sgqlc.types.Type):
    """Class for EdgeUpdateTraceObserverResponse.

    Successfully updated trace observers, or one or more error
    responses if there were issues.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "trace_observer")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of("EdgeUpdateTraceObserverResponseError"),
        graphql_name="errors",
    )


class EdgeUpdateTraceObserverResponseError(sgqlc.types.Type):
    """Class for EdgeUpdateTraceObserverResponseError.

    Description of errors that may occur while attempting to update a
    trace observer.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class EdgeUpdateTraceObserverResponses(sgqlc.types.Type):
    """Class for EdgeUpdateTraceObserverResponses.

    Array of responses, one for each trace observer update request.
    """

    __schema__ = nerdgraph
    __field_names__ = ("responses",)
    responses = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(EdgeUpdateTraceObserverResponse))
        ),
        graphql_name="responses",
    )


class EntityAlertViolation(sgqlc.types.Type):
    """Class for EntityAlertViolation.

    The alert violation for an entity.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "agent_url",
        "alert_severity",
        "closed_at",
        "label",
        "level",
        "opened_at",
        "violation_id",
        "violation_url",
    )
    agent_url = sgqlc.types.Field(String, graphql_name="agentUrl")


class EntityCollection(sgqlc.types.Type):
    """Class for EntityCollection.

    A collection of user defined Entities and Entity Search queries.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account",
        "created_by",
        "definition",
        "guid",
        "members",
        "name",
        "type",
    )
    account = sgqlc.types.Field(AccountReference, graphql_name="account")


class EntityCollectionDefinition(sgqlc.types.Type):
    """Class for EntityCollectionDefinition.

    The definition of a collection.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "entity_guids",
        "entity_search_query",
        "scope_accounts",
        "search_queries",
    )
    entity_guids = sgqlc.types.Field(
        sgqlc.types.list_of(EntityGuid), graphql_name="entityGuids"
    )


class EntityCollectionScopeAccounts(sgqlc.types.Type):
    """Class for EntityCollectionScopeAccounts.

    The Accounts used to scope a collection.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="accountIds")


class EntityDeleteError(sgqlc.types.Type):
    """Class for EntityDeleteError.

    Type that wraps the errors from a entity delete operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("guid", "message", "type")
    guid = sgqlc.types.Field(EntityGuid, graphql_name="guid")


class EntityDeleteResult(sgqlc.types.Type):
    """Class for EntityDeleteResult.

    Response type for delete operations over entities.
    """

    __schema__ = nerdgraph
    __field_names__ = ("deleted_entities", "failures")
    deleted_entities = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid))),
        graphql_name="deletedEntities",
    )


class EntityGoldenContext(sgqlc.types.Type):
    """Class for EntityGoldenContext.

    An object that represent the context.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account", "guid")
    account = sgqlc.types.Field(Int, graphql_name="account")


class EntityGoldenContextScopedGoldenMetrics(sgqlc.types.Type):
    """Class for EntityGoldenContextScopedGoldenMetrics.

    An object that represents the golden metrics scoped by context.
    """

    __schema__ = nerdgraph
    __field_names__ = ("context", "metrics")
    context = sgqlc.types.Field(
        sgqlc.types.non_null(EntityGoldenContext), graphql_name="context"
    )


class EntityGoldenContextScopedGoldenTags(sgqlc.types.Type):
    """Class for EntityGoldenContextScopedGoldenTags.

    An object that represents the golden tags scoped by context.
    """

    __schema__ = nerdgraph
    __field_names__ = ("context", "tags")
    context = sgqlc.types.Field(
        sgqlc.types.non_null(EntityGoldenContext), graphql_name="context"
    )


class EntityGoldenGoldenMetricsError(sgqlc.types.Type):
    """Class for EntityGoldenGoldenMetricsError.

    The different error types in golden metrics.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class EntityGoldenMetric(sgqlc.types.Type):
    """Class for EntityGoldenMetric.

    An object that represents a golden metric.
    """

    __schema__ = nerdgraph
    __field_names__ = ("definition", "metric_name", "name", "query", "title", "unit")
    definition = sgqlc.types.Field(
        sgqlc.types.non_null("EntityGoldenMetricDefinition"), graphql_name="definition"
    )


class EntityGoldenMetricDefinition(sgqlc.types.Type):
    """Class for EntityGoldenMetricDefinition.

    The definition of the metric.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "event_id",
        "event_object_id",
        "facet",
        "from_",
        "select",
        "where",
    )
    event_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="eventId")


class EntityGoldenMetricsDomainTypeScoped(sgqlc.types.Type):
    """Class for EntityGoldenMetricsDomainTypeScoped.

    An object that represents the golden metrics scoped by domain and
    type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("context", "domain_type", "metrics")
    context = sgqlc.types.Field(
        sgqlc.types.non_null(EntityGoldenContext), graphql_name="context"
    )


class EntityGoldenMetricsDomainTypeScopedResponse(sgqlc.types.Type):
    """Class for EntityGoldenMetricsDomainTypeScopedResponse.

    An object that represents the golden metrics scoped by domain and
    type mutation result.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "metrics")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGoldenGoldenMetricsError)),
        graphql_name="errors",
    )


class EntityGoldenTag(sgqlc.types.Type):
    """Class for EntityGoldenTag.

    An object that represents a golden tag.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key",)
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class EntityGoldenTagsDomainTypeScoped(sgqlc.types.Type):
    """Class for EntityGoldenTagsDomainTypeScoped.

    An object that represents the golden tags scoped by domain and
    type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("context", "domain_type", "tags")
    context = sgqlc.types.Field(
        sgqlc.types.non_null(EntityGoldenContext), graphql_name="context"
    )


class EntityGoldenTagsDomainTypeScopedResponse(sgqlc.types.Type):
    """Class for EntityGoldenTagsDomainTypeScopedResponse.

    An object that represents the golden tags scoped by domain and
    type mutation result.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "tags")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EntityGoldenGoldenMetricsError)),
        graphql_name="errors",
    )


class EntityRelationship(sgqlc.types.Type):
    """Class for EntityRelationship.

    An entity relationship.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(EntityRelationshipType, graphql_name="type")


class EntityRelationshipNode(sgqlc.types.Type):
    """Class for EntityRelationshipNode.

    A node in an Entity relationship.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity",)
    entity = sgqlc.types.Field(EntityOutline, graphql_name="entity")


class EntityRelationshipRelatedEntitiesResult(sgqlc.types.Type):
    """Class for EntityRelationshipRelatedEntitiesResult.

    Response containing entity relationships.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "results")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class EntityRelationshipUserDefinedCreateOrReplaceResult(sgqlc.types.Type):
    """Class for EntityRelationshipUserDefinedCreateOrReplaceResult.

    The result of the entityRelationshipUserDefinedCreateOrReplace
    mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(
                "EntityRelationshipUserDefinedCreateOrReplaceResultError"
            )
        ),
        graphql_name="errors",
    )


class EntityRelationshipUserDefinedCreateOrReplaceResultError(sgqlc.types.Type):
    """Class for EntityRelationshipUserDefinedCreateOrReplaceResultError.

    The entityRelationshipUserDefinedCreateOrReplace result error.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class EntityRelationshipUserDefinedDeleteResult(sgqlc.types.Type):
    """Class for EntityRelationshipUserDefinedDeleteResult.

    The result of the entityRelationshipUserDefinedDelete mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("EntityRelationshipUserDefinedDeleteResultError")
        ),
        graphql_name="errors",
    )


class EntityRelationshipUserDefinedDeleteResultError(sgqlc.types.Type):
    """Class for EntityRelationshipUserDefinedDeleteResultError.

    The entityRelationshipUserDefinedDelete result error.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class EntityRelationshipVertex(sgqlc.types.Type):
    """Class for EntityRelationshipVertex.

    A vertex in an entity relationship edge.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "entity", "guid")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class EntitySearch(sgqlc.types.Type):
    """Class for EntitySearch.

    A data structure that contains the detailed response of an entity
    search.  The direct search result is available through `results`.
    Information about the query itself is available through `query`,
    `types`, and `count`.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "counts", "query", "results", "types")
    count = sgqlc.types.Field(Int, graphql_name="count")


class EntitySearchCounts(sgqlc.types.Type):
    """Class for EntitySearchCounts.

    The groupings and counts of entities returned for the specified
    criteria.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "facet")
    count = sgqlc.types.Field(Int, graphql_name="count")


class EntitySearchResult(sgqlc.types.Type):
    """Class for EntitySearchResult.

    A section of the entity search results. If there is a `nextCursor`
    present, there are more results available.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entities", "next_cursor")
    entities = sgqlc.types.Field(
        sgqlc.types.list_of(EntityOutline), graphql_name="entities"
    )


class EntitySearchTypes(sgqlc.types.Type):
    """Class for EntitySearchTypes.

    A detailed entity search response object type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "domain", "entity_type", "type")
    count = sgqlc.types.Field(Int, graphql_name="count")


class EntityTag(sgqlc.types.Type):
    """Class for EntityTag.

    A tag that has been applied to an entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "values")
    key = sgqlc.types.Field(String, graphql_name="key")


class EntityTagValueWithMetadata(sgqlc.types.Type):
    """Class for EntityTagValueWithMetadata.

    The value and metadata of a single entity tag.
    """

    __schema__ = nerdgraph
    __field_names__ = ("mutable", "value")
    mutable = sgqlc.types.Field(Boolean, graphql_name="mutable")


class EntityTagWithMetadata(sgqlc.types.Type):
    """Class for EntityTagWithMetadata.

    The tags with metadata of the entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "values")
    key = sgqlc.types.Field(String, graphql_name="key")


class ErrorsInboxActorStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("error_group", "error_group_state_types", "error_groups")
    error_group = sgqlc.types.Field(
        "ErrorsInboxErrorGroup",
        graphql_name="errorGroup",
        args=sgqlc.types.ArgDict(
            (
                (
                    "error_event",
                    sgqlc.types.Arg(
                        ErrorsInboxErrorEventInput,
                        graphql_name="errorEvent",
                        default=None,
                    ),
                ),
                ("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),
            )
        ),
    )


class ErrorsInboxAssignErrorGroupResponse(sgqlc.types.Type):
    """Class for ErrorsInboxAssignErrorGroupResponse.

    Response for error group assignment mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("assignment", "errors")
    assignment = sgqlc.types.Field("ErrorsInboxAssignment", graphql_name="assignment")


class ErrorsInboxAssignment(sgqlc.types.Type):
    """Class for ErrorsInboxAssignment.

    User assigned to an error group.
    """

    __schema__ = nerdgraph
    __field_names__ = ("email", "user_info")
    email = sgqlc.types.Field(String, graphql_name="email")


class ErrorsInboxDeleteErrorGroupResourceResponse(sgqlc.types.Type):
    """Class for ErrorsInboxDeleteErrorGroupResourceResponse.

    Response for delete resource mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("resource_id",)
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="resourceId")


class ErrorsInboxErrorGroup(sgqlc.types.Type):
    """Class for ErrorsInboxErrorGroup.

    A grouping of similar error events.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "assignment",
        "entity_guid",
        "events_query",
        "first_seen_at",
        "id",
        "last_seen_at",
        "message",
        "name",
        "regressed_at",
        "resources",
        "state",
        "url",
    )
    assignment = sgqlc.types.Field(ErrorsInboxAssignment, graphql_name="assignment")


class ErrorsInboxErrorGroupStateTypeResult(sgqlc.types.Type):
    """Class for ErrorsInboxErrorGroupStateTypeResult.

    Information about the error group state type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(ErrorsInboxErrorGroupState, graphql_name="type")


class ErrorsInboxErrorGroupsResponse(sgqlc.types.Type):
    """Class for ErrorsInboxErrorGroupsResponse.

    Response for error groups.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "results", "total_count")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class ErrorsInboxResourcesResponse(sgqlc.types.Type):
    """Class for ErrorsInboxResourcesResponse.

    Response for error group resources.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "results", "total_count")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class ErrorsInboxUpdateErrorGroupStateResponse(sgqlc.types.Type):
    """Class for ErrorsInboxUpdateErrorGroupStateResponse.

    Response for error group state mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("state",)
    state = sgqlc.types.Field(ErrorsInboxErrorGroupState, graphql_name="state")


class EventAttributeDefinition(sgqlc.types.Type):
    """Class for EventAttributeDefinition.

    A human-readable definition of an NRDB Event Type Attribute.
    """

    __schema__ = nerdgraph
    __field_names__ = ("definition", "documentation_url", "label", "name")
    definition = sgqlc.types.Field(String, graphql_name="definition")


class EventDefinition(sgqlc.types.Type):
    """Class for EventDefinition.

    A human-readable definition of an NRDB Event Type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attributes", "definition", "label", "name")
    attributes = sgqlc.types.Field(
        sgqlc.types.list_of(EventAttributeDefinition), graphql_name="attributes"
    )


class EventsToMetricsAccountStitchedFields(sgqlc.types.Type):
    """Class for EventsToMetricsAccountStitchedFields.

    Account stitched fields to enable autostitching in NerdGraph.
    """

    __schema__ = nerdgraph
    __field_names__ = ("all_rules", "rules_by_id")
    all_rules = sgqlc.types.Field(
        "EventsToMetricsListRuleResult", graphql_name="allRules"
    )


class EventsToMetricsCreateRuleFailure(sgqlc.types.Type):
    """Class for EventsToMetricsCreateRuleFailure.

    Error details about the events to metrics rule that failed to be
    created and why.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "submitted")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of("EventsToMetricsError"), graphql_name="errors"
    )


class EventsToMetricsCreateRuleResult(sgqlc.types.Type):
    """Class for EventsToMetricsCreateRuleResult.

    The result of which submitted events to metrics rules were
    successfully and unsuccessfully created.
    """

    __schema__ = nerdgraph
    __field_names__ = ("failures", "successes")
    failures = sgqlc.types.Field(
        sgqlc.types.list_of(EventsToMetricsCreateRuleFailure), graphql_name="failures"
    )


class EventsToMetricsCreateRuleSubmission(sgqlc.types.Type):
    """Class for EventsToMetricsCreateRuleSubmission.

    The details that were submitted when creating an events to metrics
    conversion rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "description", "name", "nrql")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class EventsToMetricsDeleteRuleFailure(sgqlc.types.Type):
    """Class for EventsToMetricsDeleteRuleFailure.

    Error details about the events to metrics rule that failed to be
    deleted and why.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "submitted")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of("EventsToMetricsError"), graphql_name="errors"
    )


class EventsToMetricsDeleteRuleResult(sgqlc.types.Type):
    """Class for EventsToMetricsDeleteRuleResult.

    The result of which submitted events to metrics rules were
    successfully and unsuccessfully deleted.
    """

    __schema__ = nerdgraph
    __field_names__ = ("failures", "successes")
    failures = sgqlc.types.Field(
        sgqlc.types.list_of(EventsToMetricsDeleteRuleFailure), graphql_name="failures"
    )


class EventsToMetricsDeleteRuleSubmission(sgqlc.types.Type):
    """Class for EventsToMetricsDeleteRuleSubmission.

    The details that were submitted when deleteing an events to
    metrics conversion rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "rule_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class EventsToMetricsError(sgqlc.types.Type):
    """Class for EventsToMetricsError.

    Error details when processing events to metrics rule requests.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "reason")
    description = sgqlc.types.Field(String, graphql_name="description")


class EventsToMetricsListRuleResult(sgqlc.types.Type):
    """Class for EventsToMetricsListRuleResult.

    A list of rule details to be returned.
    """

    __schema__ = nerdgraph
    __field_names__ = ("rules",)
    rules = sgqlc.types.Field(
        sgqlc.types.list_of("EventsToMetricsRule"), graphql_name="rules"
    )


class EventsToMetricsRule(sgqlc.types.Type):
    """Class for EventsToMetricsRule.

    Information about an event-to-metric rule which creates metrics
    from events.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "created_at",
        "description",
        "enabled",
        "id",
        "name",
        "nrql",
        "updated_at",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class EventsToMetricsUpdateRuleFailure(sgqlc.types.Type):
    """Class for EventsToMetricsUpdateRuleFailure.

    Error details about the events to metrics rule that failed to be
    updated and why.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "submitted")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(EventsToMetricsError), graphql_name="errors"
    )


class EventsToMetricsUpdateRuleResult(sgqlc.types.Type):
    """Class for EventsToMetricsUpdateRuleResult.

    The result of which submitted events to metrics rules were
    successfully and unsuccessfully update.
    """

    __schema__ = nerdgraph
    __field_names__ = ("failures", "successes")
    failures = sgqlc.types.Field(
        sgqlc.types.list_of(EventsToMetricsUpdateRuleFailure), graphql_name="failures"
    )


class EventsToMetricsUpdateRuleSubmission(sgqlc.types.Type):
    """Class for EventsToMetricsUpdateRuleSubmission.

    The details that were submitted when updating an events to metrics
    conversion rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "enabled", "rule_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class HistoricalDataExportAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("export", "exports")
    export = sgqlc.types.Field(
        "HistoricalDataExportCustomerExportResponse",
        graphql_name="export",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )


class HistoricalDataExportCustomerExportResponse(sgqlc.types.Type):
    """Class for HistoricalDataExportCustomerExportResponse.

    A Historic Export. Contains information about the request and the
    current status of that request.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account",
        "available_until",
        "begin_time",
        "created_at",
        "end_time",
        "event_count",
        "event_types",
        "id",
        "message",
        "nrql",
        "percent_complete",
        "results",
        "status",
        "user",
    )
    account = sgqlc.types.Field(AccountReference, graphql_name="account")


class IncidentIntelligenceEnvironmentAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("current_environment",)
    current_environment = sgqlc.types.Field(
        "IncidentIntelligenceEnvironmentCurrentEnvironmentResult",
        graphql_name="currentEnvironment",
        args=sgqlc.types.ArgDict(
            (
                (
                    "kind",
                    sgqlc.types.Arg(
                        IncidentIntelligenceEnvironmentSupportedEnvironmentKind,
                        graphql_name="kind",
                        default=None,
                    ),
                ),
            )
        ),
    )


class IncidentIntelligenceEnvironmentActorStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = (
        "authorized_environments",
        "consented_accounts",
        "current_environment",
    )
    authorized_environments = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(
                "IncidentIntelligenceEnvironmentIncidentIntelligenceEnvironment"
            )
        ),
        graphql_name="authorizedEnvironments",
        args=sgqlc.types.ArgDict(
            (
                (
                    "kind",
                    sgqlc.types.Arg(
                        IncidentIntelligenceEnvironmentSupportedEnvironmentKind,
                        graphql_name="kind",
                        default=None,
                    ),
                ),
            )
        ),
    )


class IncidentIntelligenceEnvironmentConsentAccounts(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentConsentAccounts.

    Consent accounts to usage of the Incident Intelligence product for
    EU or FedRAMP.
    """

    __schema__ = nerdgraph
    __field_names__ = ("consented_accounts", "result")
    consented_accounts = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("IncidentIntelligenceEnvironmentConsentedAccount")
        ),
        graphql_name="consentedAccounts",
    )


class IncidentIntelligenceEnvironmentConsentAuthorizedAccounts(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentConsentAuthorizedAccounts.

    Consent all the user's authorized accounts for the Incident
    Intelligence product for EU or FedRAMP.
    """

    __schema__ = nerdgraph
    __field_names__ = ("consented_accounts", "result")
    consented_accounts = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null("IncidentIntelligenceEnvironmentConsentedAccount")
        ),
        graphql_name="consentedAccounts",
    )


class IncidentIntelligenceEnvironmentConsentedAccount(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentConsentedAccount.

    Represent an account that is mark with consent for Incident
    Intelligence usage.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account",)
    account = sgqlc.types.Field(AccountReference, graphql_name="account")


class IncidentIntelligenceEnvironmentCreateEnvironment(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentCreateEnvironment.

    Creates a new Incident Intelligence Environment, will fail if an
    environment is already attached to the same parent account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("result", "result_details")
    result = sgqlc.types.Field(
        sgqlc.types.non_null(IncidentIntelligenceEnvironmentCreateEnvironmentResult),
        graphql_name="result",
    )


class IncidentIntelligenceEnvironmentCurrentEnvironmentResult(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentCurrentEnvironmentResult.

    An environment will be populated only if the user is attached to a
    single environment.
    """

    __schema__ = nerdgraph
    __field_names__ = ("environment", "reason", "reason_details")
    environment = sgqlc.types.Field(
        "IncidentIntelligenceEnvironmentIncidentIntelligenceEnvironment",
        graphql_name="environment",
    )


class IncidentIntelligenceEnvironmentDeleteEnvironment(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentDeleteEnvironment.

    Deletes an existing environment.
    """

    __schema__ = nerdgraph
    __field_names__ = ("result",)
    result = sgqlc.types.Field(
        sgqlc.types.non_null(IncidentIntelligenceEnvironmentDeleteEnvironmentResult),
        graphql_name="result",
    )


class IncidentIntelligenceEnvironmentDissentAccounts(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentDissentAccounts.

    Dissent accounts to usage of the Incident Intelligence product in
    the EU/FedRAMP (removes the consent marking).
    """

    __schema__ = nerdgraph
    __field_names__ = ("dissented_accounts", "result")
    dissented_accounts = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(IncidentIntelligenceEnvironmentConsentedAccount)
        ),
        graphql_name="dissentedAccounts",
    )


class IncidentIntelligenceEnvironmentEnvironmentAlreadyExists(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentEnvironmentAlreadyExists.

    Environment already exists detailed result.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "environment", "master_account_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class IncidentIntelligenceEnvironmentEnvironmentCreated(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentEnvironmentCreated.

    Environment created detailed result.
    """

    __schema__ = nerdgraph
    __field_names__ = ("environment",)
    environment = sgqlc.types.Field(
        sgqlc.types.non_null(
            "IncidentIntelligenceEnvironmentIncidentIntelligenceEnvironment"
        ),
        graphql_name="environment",
    )


class IncidentIntelligenceEnvironmentIncidentIntelligenceEnvironment(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentIncidentIntelligenceEnvironment.

    Represents an AI Incident Intelligence environment. An environment
    crosses the account boundary and allows correlating data as long
    as the data's accounts are attached to the same environment.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "associated_authorized_accounts",
        "billing_cycle_quota",
        "created_at",
        "created_by",
        "incident_intelligence_account",
        "is_consent_required",
        "is_entitled_for_ai",
        "is_free_tier",
        "kind",
        "master_account",
        "name",
        "was_consented",
    )
    associated_authorized_accounts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(AccountReference)),
        graphql_name="associatedAuthorizedAccounts",
    )


class IncidentIntelligenceEnvironmentMultipleEnvironmentsAvailable(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentMultipleEnvironmentsAvailable.

    The user has access to more than one environment from the context
    of this account (only one is allowed).
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="accountIds")


class IncidentIntelligenceEnvironmentUserNotAuthorizedForAccount(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentUserNotAuthorizedForAccount.

    The user is not authorized for this account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id",)
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class IncidentIntelligenceEnvironmentUserNotCapableToOperateOnAccount(sgqlc.types.Type):
    """Class for IncidentIntelligenceEnvironmentUserNotCapableToOperateOnAccount.

    The user is not capable to perform an operation on this account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "capability")
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class InfrastructureHostSummaryData(sgqlc.types.Type):
    """Class for InfrastructureHostSummaryData.

    Summary statistics about the Infra Host.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "cpu_utilization_percent",
        "disk_used_percent",
        "memory_used_percent",
        "network_receive_rate",
        "network_transmit_rate",
        "services_count",
    )
    cpu_utilization_percent = sgqlc.types.Field(
        Float, graphql_name="cpuUtilizationPercent"
    )


class InstallationAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("install_status", "recipe_events", "recipes", "statuses")
    install_status = sgqlc.types.Field(
        "InstallationInstallStatus", graphql_name="installStatus"
    )


class InstallationInstallStatus(sgqlc.types.Type):
    """Class for InstallationInstallStatus.

    An object that contains the overall installation status that is
    created from within the newrelic-cli.
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


class InstallationInstallStatusResult(sgqlc.types.Type):
    """Class for InstallationInstallStatusResult.

    A wrapper object that contains paginated install statuses along
    with counts and a pagination cursor.
    """

    __schema__ = nerdgraph
    __field_names__ = ("cursor", "install_statuses", "total_count")
    cursor = sgqlc.types.Field(String, graphql_name="cursor")


class InstallationRecipeEvent(sgqlc.types.Type):
    """Class for InstallationRecipeEvent.

    An object that contains an installation event created from within
    the newrelic-cli.
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
        "timestamp",
        "validation_duration_milliseconds",
    )
    cli_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="cliVersion"
    )


class InstallationRecipeEventResult(sgqlc.types.Type):
    """Class for InstallationRecipeEventResult.

    A wrapper object that contains paginated recipe events along with
    counts and a pagination cursor.
    """

    __schema__ = nerdgraph
    __field_names__ = ("cursor", "recipe_events", "total_count")
    cursor = sgqlc.types.Field(String, graphql_name="cursor")


class InstallationStatusError(sgqlc.types.Type):
    """Class for InstallationStatusError.

    An object that represents a status error whenever an recipe has
    failed to install.
    """

    __schema__ = nerdgraph
    __field_names__ = ("details", "message")
    details = sgqlc.types.Field(String, graphql_name="details")


class JavaFlightRecorderFlamegraph(sgqlc.types.Type):
    """Class for JavaFlightRecorderFlamegraph.

    The flamegraph built from the strack trace samples.
    """

    __schema__ = nerdgraph
    __field_names__ = ("all_frames",)
    all_frames = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("JavaFlightRecorderStackFrame")),
        graphql_name="allFrames",
    )


class JavaFlightRecorderStackFrame(sgqlc.types.Type):
    """Class for JavaFlightRecorderStackFrame.

    A method within the flamegraph.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "id", "name", "parent_id")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class KeyTransactionApplication(sgqlc.types.Type):
    """Class for KeyTransactionApplication.

    The application wrapper.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity", "guid")
    entity = sgqlc.types.Field(EntityOutline, graphql_name="entity")


class KeyTransactionCreateResult(sgqlc.types.Type):
    """Class for KeyTransactionCreateResult.

    The result of creating a key transaction.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "application",
        "browser_apdex_target",
        "guid",
        "metric_name",
        "name",
    )
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class KeyTransactionDeleteResult(sgqlc.types.Type):
    """Class for KeyTransactionDeleteResult.

    The result of deleting a key transaction.
    """

    __schema__ = nerdgraph
    __field_names__ = ("success",)
    success = sgqlc.types.Field(Boolean, graphql_name="success")


class KeyTransactionUpdateResult(sgqlc.types.Type):
    """Class for KeyTransactionUpdateResult.

    The result of updating a key transaction.
    """

    __schema__ = nerdgraph
    __field_names__ = ("apdex_target", "application", "browser_apdex_target", "name")
    apdex_target = sgqlc.types.Field(Float, graphql_name="apdexTarget")


class LogConfigurationsAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = (
        "data_partition_rules",
        "obfuscation_expressions",
        "obfuscation_rules",
        "parsing_rules",
        "pipeline_configuration",
        "test_grok",
    )
    data_partition_rules = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("LogConfigurationsDataPartitionRule")),
        graphql_name="dataPartitionRules",
    )


class LogConfigurationsCreateDataPartitionRuleError(sgqlc.types.Type):
    """Class for LogConfigurationsCreateDataPartitionRuleError.

    Expected errors as a result of creating a new data partition rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class LogConfigurationsCreateDataPartitionRuleResponse(sgqlc.types.Type):
    """Class for LogConfigurationsCreateDataPartitionRuleResponse.

    The result after creating a new data partition rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "rule")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(LogConfigurationsCreateDataPartitionRuleError),
        graphql_name="errors",
    )


class LogConfigurationsCreateParsingRuleResponse(sgqlc.types.Type):
    """Class for LogConfigurationsCreateParsingRuleResponse.

    The result after creating a new parsing rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "rule")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of("LogConfigurationsParsingRuleMutationError"),
        graphql_name="errors",
    )


class LogConfigurationsDataPartitionRule(sgqlc.types.Type):
    """Class for LogConfigurationsDataPartitionRule.

    The data partition rule for an account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "created_by",
        "deleted",
        "description",
        "enabled",
        "id",
        "nrql",
        "retention_policy",
        "target_data_partition",
        "updated_at",
        "updated_by",
    )
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(DateTime), graphql_name="createdAt"
    )


class LogConfigurationsDataPartitionRuleMatchingCriteria(sgqlc.types.Type):
    """Class for LogConfigurationsDataPartitionRuleMatchingCriteria.

    The data partition rule matching criteria.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute_name", "matching_expression", "matching_operator")
    attribute_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="attributeName"
    )


class LogConfigurationsDataPartitionRuleMutationError(sgqlc.types.Type):
    """Class for LogConfigurationsDataPartitionRuleMutationError.

    An object that contains expected errors as a result of mutating an
    existing data partition rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class LogConfigurationsDeleteDataPartitionRuleResponse(sgqlc.types.Type):
    """Class for LogConfigurationsDeleteDataPartitionRuleResponse.

    The result after deleting a data partition rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(LogConfigurationsDataPartitionRuleMutationError),
        graphql_name="errors",
    )


class LogConfigurationsDeleteParsingRuleResponse(sgqlc.types.Type):
    """Class for LogConfigurationsDeleteParsingRuleResponse.

    The result after deleting a parsing rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of("LogConfigurationsParsingRuleMutationError"),
        graphql_name="errors",
    )


class LogConfigurationsGrokTestExtractedAttribute(sgqlc.types.Type):
    """Class for LogConfigurationsGrokTestExtractedAttribute.

    An attribute that was extracted from a Grok test.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "value")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class LogConfigurationsGrokTestResult(sgqlc.types.Type):
    """Class for LogConfigurationsGrokTestResult.

    The result of testing Grok on a log line.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attributes", "log_line", "matched")
    attributes = sgqlc.types.Field(
        sgqlc.types.list_of(
            sgqlc.types.non_null(LogConfigurationsGrokTestExtractedAttribute)
        ),
        graphql_name="attributes",
    )


class LogConfigurationsObfuscationAction(sgqlc.types.Type):
    """Class for LogConfigurationsObfuscationAction.

    Application of an obfuscation expression with specific a
    replacement method.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attributes", "expression", "id", "method")
    attributes = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="attributes",
    )


class LogConfigurationsObfuscationExpression(sgqlc.types.Type):
    """Class for LogConfigurationsObfuscationExpression.

    Reusable obfuscation expression.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "created_by",
        "description",
        "id",
        "name",
        "regex",
        "updated_at",
        "updated_by",
    )
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(DateTime), graphql_name="createdAt"
    )


class LogConfigurationsObfuscationRule(sgqlc.types.Type):
    """Class for LogConfigurationsObfuscationRule.

    Rule for identifying a set of log data to apply specific
    obfuscation actions to.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "actions",
        "created_at",
        "created_by",
        "description",
        "enabled",
        "filter",
        "id",
        "name",
        "updated_at",
        "updated_by",
    )
    actions = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(LogConfigurationsObfuscationAction)),
        graphql_name="actions",
    )


class LogConfigurationsParsingRule(sgqlc.types.Type):
    """Class for LogConfigurationsParsingRule.

    A parsing rule for an account.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "attribute",
        "created_by",
        "deleted",
        "description",
        "enabled",
        "grok",
        "id",
        "lucene",
        "nrql",
        "updated_at",
        "updated_by",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class LogConfigurationsParsingRuleMutationError(sgqlc.types.Type):
    """Class for LogConfigurationsParsingRuleMutationError.

    Expected errors as a result of mutating a parsing rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class LogConfigurationsPipelineConfiguration(sgqlc.types.Type):
    """Class for LogConfigurationsPipelineConfiguration.

    The pipeline configuration for an account, with metadata.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "enrichment_disabled",
        "json_parsing_disabled",
        "obfuscation_disabled",
        "parsing_disabled",
        "patterns_enabled",
        "recursive_json_parsing_disabled",
        "transformation_disabled",
        "updated_at",
        "updated_by",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class LogConfigurationsUpdateDataPartitionRuleResponse(sgqlc.types.Type):
    """Class for LogConfigurationsUpdateDataPartitionRuleResponse.

    An object that represents the result after updating a data
    partition rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "rule")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(LogConfigurationsDataPartitionRuleMutationError),
        graphql_name="errors",
    )


class LogConfigurationsUpdateParsingRuleResponse(sgqlc.types.Type):
    """Class for LogConfigurationsUpdateParsingRuleResponse.

    The result after updating a parsing rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "rule")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(LogConfigurationsParsingRuleMutationError),
        graphql_name="errors",
    )


class LogConfigurationsUpsertPipelineConfigurationResponse(sgqlc.types.Type):
    """Class for LogConfigurationsUpsertPipelineConfigurationResponse.

    The result after upserting pipeline configuration for an account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("pipeline_configuration",)
    pipeline_configuration = sgqlc.types.Field(
        LogConfigurationsPipelineConfiguration, graphql_name="pipelineConfiguration"
    )


class MetricNormalizationAccountStitchedFields(sgqlc.types.Type):
    """Class for MetricNormalizationAccountStitchedFields.

    Return type for queries given an account ID.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metric_normalization_rule", "metric_normalization_rules")
    metric_normalization_rule = sgqlc.types.Field(
        "MetricNormalizationRule",
        graphql_name="metricNormalizationRule",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )


class MetricNormalizationRule(sgqlc.types.Type):
    """Class for MetricNormalizationRule.

    An object that represents a metric rename rule.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "action",
        "application_guid",
        "application_name",
        "created_at",
        "enabled",
        "eval_order",
        "id",
        "match_expression",
        "notes",
        "replacement",
        "terminate_chain",
    )
    action = sgqlc.types.Field(MetricNormalizationRuleAction, graphql_name="action")


class MetricNormalizationRuleMetricGroupingIssue(sgqlc.types.Type):
    """Class for MetricNormalizationRuleMetricGroupingIssue.

    An object that represents a metric grouping issue.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "denied_metrics_count",
        "denied_metrics_rate_per_minute",
        "metric_normalization_rule_id",
        "mitigated",
        "mitigation_rate_threshold",
        "mitigation_rate_window_size",
    )
    denied_metrics_count = sgqlc.types.Field(Int, graphql_name="deniedMetricsCount")


class MetricNormalizationRuleMutationError(sgqlc.types.Type):
    """Class for MetricNormalizationRuleMutationError.

    Error for mutation results.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class MetricNormalizationRuleMutationResponse(sgqlc.types.Type):
    """Class for MetricNormalizationRuleMutationResponse.

    The result of a metric rename rule mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "rule")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(MetricNormalizationRuleMutationError), graphql_name="errors"
    )


class MobileAppSummaryData(sgqlc.types.Type):
    """Class for MobileAppSummaryData.

    Mobile application summary data.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "app_launch_count",
        "crash_count",
        "crash_rate",
        "http_error_rate",
        "http_request_count",
        "http_request_rate",
        "http_response_time_average",
        "mobile_session_count",
        "network_failure_rate",
        "users_affected_count",
    )
    app_launch_count = sgqlc.types.Field(Int, graphql_name="appLaunchCount")


class MobilePushNotificationActorStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("devices",)
    devices = sgqlc.types.Field(
        sgqlc.types.list_of("MobilePushNotificationDevice"), graphql_name="devices"
    )


class MobilePushNotificationDevice(sgqlc.types.Type):
    """Class for MobilePushNotificationDevice.

    Device info used for push notifications.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "app_version",
        "device_id",
        "device_name",
        "operating_system",
        "user_id",
    )
    app_version = sgqlc.types.Field(
        sgqlc.types.non_null(SemVer), graphql_name="appVersion"
    )


class MobilePushNotificationRemoveDeviceResult(sgqlc.types.Type):
    """Class for MobilePushNotificationRemoveDeviceResult.

    Result from removing a device.
    """

    __schema__ = nerdgraph
    __field_names__ = ("device_id", "message")
    device_id = sgqlc.types.Field(String, graphql_name="deviceId")


class MobilePushNotificationSendPushResult(sgqlc.types.Type):
    """Class for MobilePushNotificationSendPushResult.

    Result from sending a test push notification.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message",)
    message = sgqlc.types.Field(String, graphql_name="message")


class NerdStorageAccountScope(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("collection", "document")
    collection = sgqlc.types.Field(
        sgqlc.types.list_of("NerdStorageCollectionMember"),
        graphql_name="collection",
        args=sgqlc.types.ArgDict(
            (
                (
                    "collection",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="collection",
                        default=None,
                    ),
                ),
            )
        ),
    )


class NerdStorageActorScope(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("collection", "document")
    collection = sgqlc.types.Field(
        sgqlc.types.list_of("NerdStorageCollectionMember"),
        graphql_name="collection",
        args=sgqlc.types.ArgDict(
            (
                (
                    "collection",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="collection",
                        default=None,
                    ),
                ),
            )
        ),
    )


class NerdStorageCollectionMember(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("document", "id")
    document = sgqlc.types.Field(NerdStorageDocument, graphql_name="document")


class NerdStorageDeleteResult(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("deleted",)
    deleted = sgqlc.types.Field(Int, graphql_name="deleted")


class NerdStorageEntityScope(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("collection", "document")
    collection = sgqlc.types.Field(
        sgqlc.types.list_of(NerdStorageCollectionMember),
        graphql_name="collection",
        args=sgqlc.types.ArgDict(
            (
                (
                    "collection",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="collection",
                        default=None,
                    ),
                ),
                (
                    "scope_by_actor",
                    sgqlc.types.Arg(Boolean, graphql_name="scopeByActor", default=None),
                ),
            )
        ),
    )


class NerdStorageVaultActorStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("secret", "secrets")
    secret = sgqlc.types.Field(
        "NerdStorageVaultSecret",
        graphql_name="secret",
        args=sgqlc.types.ArgDict(
            (
                (
                    "key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="key", default=None
                    ),
                ),
            )
        ),
    )


class NerdStorageVaultDeleteSecretResult(sgqlc.types.Type):
    """Class for NerdStorageVaultDeleteSecretResult.

    Result of a mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "status")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("NerdStorageVaultResultError")),
        graphql_name="errors",
    )


class NerdStorageVaultResultError(sgqlc.types.Type):
    """Class for NerdStorageVaultResultError.

    Mutation error information.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class NerdStorageVaultSecret(sgqlc.types.Type):
    """Class for NerdStorageVaultSecret.

    Secret key and value.
    """

    __schema__ = nerdgraph
    __field_names__ = ("key", "value")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")


class NerdStorageVaultWriteSecretResult(sgqlc.types.Type):
    """Class for NerdStorageVaultWriteSecretResult.

    Information about the result of the write secret mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "status")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(NerdStorageVaultResultError)),
        graphql_name="errors",
    )


class NerdpackAllowListResult(sgqlc.types.Type):
    """Class for NerdpackAllowListResult.

    Result of an allow list mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nerdpack", "results_per_account")
    nerdpack = sgqlc.types.Field(
        sgqlc.types.non_null("NerdpackData"), graphql_name="nerdpack"
    )


class NerdpackAllowedAccount(sgqlc.types.Type):
    """Class for NerdpackAllowedAccount.

    Information about an account present on the allow-list.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id",)
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class NerdpackAssetInfo(sgqlc.types.Type):
    """Class for NerdpackAssetInfo.

    Info about Nerdpack assets.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "size_in_bytes")
    name = sgqlc.types.Field(String, graphql_name="name")


class NerdpackData(sgqlc.types.Type):
    """Class for NerdpackData.

    The Nerdpack root object. Contains the Nerdpack information
    including the list of versions and subscriptions.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "allowed_accounts",
        "id",
        "subscription_model",
        "subscriptions",
        "versions",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class NerdpackMutationResultPerAccount(sgqlc.types.Type):
    """Class for NerdpackMutationResultPerAccount.

    Mutation result for the given acccount.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "reason", "result")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class NerdpackNerdpacks(sgqlc.types.Type):
    """Class for NerdpackNerdpacks.

    Provides fields to query nerdpacks by different conditions.
    """

    __schema__ = nerdgraph
    __field_names__ = ("effective_subscribed_versions", "nerdpack", "subscribable")
    effective_subscribed_versions = sgqlc.types.Field(
        sgqlc.types.list_of("NerdpackVersion"),
        graphql_name="effectiveSubscribedVersions",
        args=sgqlc.types.ArgDict(
            (
                (
                    "overrides",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(NerdpackOverrideVersionRules),
                        graphql_name="overrides",
                        default=None,
                    ),
                ),
            )
        ),
    )


class NerdpackRemovedTagInfo(sgqlc.types.Type):
    """Class for NerdpackRemovedTagInfo.

    Information about removed tag.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nerdpack_id", "tag_name", "version")
    nerdpack_id = sgqlc.types.Field(ID, graphql_name="nerdpackId")


class NerdpackRemovedTagResponse(sgqlc.types.Type):
    """Class for NerdpackRemovedTagResponse.

    Removed Tag response.
    """

    __schema__ = nerdgraph
    __field_names__ = ("removed_tag_info", "status")
    removed_tag_info = sgqlc.types.Field(
        NerdpackRemovedTagInfo, graphql_name="removedTagInfo"
    )


class NerdpackSubscribeResult(sgqlc.types.Type):
    """Class for NerdpackSubscribeResult.

    Subscription result.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nerdpack", "results_per_account", "tag")
    nerdpack = sgqlc.types.Field(
        sgqlc.types.non_null(NerdpackData), graphql_name="nerdpack"
    )


class NerdpackSubscription(sgqlc.types.Type):
    """Class for NerdpackSubscription.

    Nerdpack subscription information.
    """

    __schema__ = nerdgraph
    __field_names__ = ("access_type", "account_id", "nerdpack_version", "tag")
    access_type = sgqlc.types.Field(
        sgqlc.types.list_of(NerdpackSubscriptionAccessType), graphql_name="accessType"
    )


class NerdpackUnsubscribeResult(sgqlc.types.Type):
    """Class for NerdpackUnsubscribeResult.

    Result of trying to remove the subscription.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nerdpack", "results_per_account")
    nerdpack = sgqlc.types.Field(
        sgqlc.types.non_null(NerdpackData), graphql_name="nerdpack"
    )


class NerdpackVersion(sgqlc.types.Type):
    """Class for NerdpackVersion.

    Contains files and information associated with a specific version
    of a Nerdpack.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "assets",
        "cli_version",
        "created_at",
        "created_by_user",
        "description",
        "display_name",
        "icon",
        "nerdpack_id",
        "repository_url",
        "sdk_version",
        "subscription_model",
        "tags",
        "version",
    )
    assets = sgqlc.types.Field(
        sgqlc.types.list_of(NerdpackAssetInfo), graphql_name="assets"
    )


class NerdpackVersionsResult(sgqlc.types.Type):
    """Class for NerdpackVersionsResult.

    Results of the nerdpack versions query.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "results", "total_count")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class Nr1CatalogActorStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = (
        "alert_policy_template",
        "categories",
        "dashboard_template",
        "data_source",
        "nerdpack",
        "nerdpacks",
        "quickstart",
        "quickstarts",
        "search",
    )
    alert_policy_template = sgqlc.types.Field(
        "Nr1CatalogAlertPolicyTemplate",
        graphql_name="alertPolicyTemplate",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )


class Nr1CatalogAlertConditionOutline(sgqlc.types.Type):
    """Class for Nr1CatalogAlertConditionOutline.

    An outline of a created alert condition.
    """

    __schema__ = nerdgraph
    __field_names__ = ("alert_condition_template", "id")
    alert_condition_template = sgqlc.types.Field(
        sgqlc.types.non_null("Nr1CatalogAlertConditionTemplate"),
        graphql_name="alertConditionTemplate",
    )


class Nr1CatalogAlertConditionTemplate(sgqlc.types.Type):
    """Class for Nr1CatalogAlertConditionTemplate.

    Information about an alert condition template.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "metadata")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class Nr1CatalogAlertConditionTemplateMetadata(sgqlc.types.Type):
    """Class for Nr1CatalogAlertConditionTemplateMetadata.

    Metadata associated with the alert condition template.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "display_name", "type")
    description = sgqlc.types.Field(String, graphql_name="description")


class Nr1CatalogAlertPolicyOutline(sgqlc.types.Type):
    """Class for Nr1CatalogAlertPolicyOutline.

    An outline of a created alert policy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("conditions", "id")
    conditions = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogAlertConditionOutline)),
        graphql_name="conditions",
    )


class Nr1CatalogAlertPolicyTemplate(sgqlc.types.Type):
    """Class for Nr1CatalogAlertPolicyTemplate.

    Information about an alert policy template.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "metadata", "support_level", "updated_at")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class Nr1CatalogAlertPolicyTemplateMetadata(sgqlc.types.Type):
    """Class for Nr1CatalogAlertPolicyTemplateMetadata.

    Metadata associated with the alert policy template.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "authors",
        "categories",
        "category_terms",
        "conditions",
        "display_name",
        "icon",
        "required_data_sources",
    )
    authors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("Nr1CatalogAuthor"))
        ),
        graphql_name="authors",
    )


class Nr1CatalogAuthor(sgqlc.types.Type):
    """Class for Nr1CatalogAuthor.

    Information about an author.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name",)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class Nr1CatalogCategory(sgqlc.types.Type):
    """Class for Nr1CatalogCategory.

    A thematic grouping for catalog items.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_name", "slug", "terms")
    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )


class Nr1CatalogCategoryFacet(sgqlc.types.Type):
    """Class for Nr1CatalogCategoryFacet.

    Information about a facet count on a category.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "display_name")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class Nr1CatalogCommunityContactChannel(sgqlc.types.Type):
    """Class for Nr1CatalogCommunityContactChannel.

    A contact channel where users can get support via the community.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogComponentFacet(sgqlc.types.Type):
    """Class for Nr1CatalogComponentFacet.

    Information about a facet count on a component.
    """

    __schema__ = nerdgraph
    __field_names__ = ("component", "count")
    component = sgqlc.types.Field(
        sgqlc.types.non_null(Nr1CatalogSearchComponentType), graphql_name="component"
    )


class Nr1CatalogDashboardOutline(sgqlc.types.Type):
    """Class for Nr1CatalogDashboardOutline.

    An outline of a created dashboard.
    """

    __schema__ = nerdgraph
    __field_names__ = ("dashboard_guid",)
    dashboard_guid = sgqlc.types.Field(
        sgqlc.types.non_null(EntityGuid), graphql_name="dashboardGuid"
    )


class Nr1CatalogDashboardTemplate(sgqlc.types.Type):
    """Class for Nr1CatalogDashboardTemplate.

    Information about a dashboard template.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "metadata", "support_level", "updated_at")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class Nr1CatalogDashboardTemplateMetadata(sgqlc.types.Type):
    """Class for Nr1CatalogDashboardTemplateMetadata.

    Metadata associated with a dashboard template.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "authors",
        "categories",
        "category_terms",
        "description",
        "display_name",
        "previews",
        "required_data_sources",
    )
    authors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogAuthor))
        ),
        graphql_name="authors",
    )


class Nr1CatalogDataSource(sgqlc.types.Type):
    """Class for Nr1CatalogDataSource.

    Information about a data source.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "metadata")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class Nr1CatalogDataSourceInstall(sgqlc.types.Type):
    """Class for Nr1CatalogDataSourceInstall.

    Information about a data source install.
    """

    __schema__ = nerdgraph
    __field_names__ = ("fallback", "primary")
    fallback = sgqlc.types.Field(
        "Nr1CatalogDataSourceInstallDirective", graphql_name="fallback"
    )


class Nr1CatalogDataSourceMetadata(sgqlc.types.Type):
    """Class for Nr1CatalogDataSourceMetadata.

    Metadata associated with a data source.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "auto_install_alert_policy_templates",
        "auto_install_dashboard_templates",
        "categories",
        "description",
        "display_name",
        "icon",
        "install",
        "keywords",
    )
    auto_install_alert_policy_templates = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogAlertPolicyTemplate))
        ),
        graphql_name="autoInstallAlertPolicyTemplates",
    )


class Nr1CatalogEmailContactChannel(sgqlc.types.Type):
    """Class for Nr1CatalogEmailContactChannel.

    A contact channel where users can get support via email.
    """

    __schema__ = nerdgraph
    __field_names__ = ("address",)
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="address")


class Nr1CatalogIcon(sgqlc.types.Type):
    """Class for Nr1CatalogIcon.

    Information about an icon.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogInstallAlertPolicyTemplateResult(sgqlc.types.Type):
    """Class for Nr1CatalogInstallAlertPolicyTemplateResult.

    Information about the mutation result when installing an alert
    policy template.
    """

    __schema__ = nerdgraph
    __field_names__ = ("alert_policy_template", "created_alert_policy")
    alert_policy_template = sgqlc.types.Field(
        sgqlc.types.non_null(Nr1CatalogAlertPolicyTemplate),
        graphql_name="alertPolicyTemplate",
    )


class Nr1CatalogInstallDashboardTemplateResult(sgqlc.types.Type):
    """Class for Nr1CatalogInstallDashboardTemplateResult.

    Information about the mutation result when installing a dashboard
    template.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_dashboard", "dashboard_template")
    created_dashboard = sgqlc.types.Field(
        sgqlc.types.non_null(Nr1CatalogDashboardOutline),
        graphql_name="createdDashboard",
    )


class Nr1CatalogInstallPlanStep(sgqlc.types.Type):
    """Class for Nr1CatalogInstallPlanStep.

    Information pertaining to a specific step in the installation plan.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "display_name",
        "fallback",
        "heading",
        "id",
        "primary",
        "target",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class Nr1CatalogInstallPlanTarget(sgqlc.types.Type):
    """Class for Nr1CatalogInstallPlanTarget.

    Represents the location of an install.
    """

    __schema__ = nerdgraph
    __field_names__ = ("destination", "os", "type")
    destination = sgqlc.types.Field(
        sgqlc.types.non_null(Nr1CatalogInstallPlanDestination),
        graphql_name="destination",
    )


class Nr1CatalogIssuesContactChannel(sgqlc.types.Type):
    """Class for Nr1CatalogIssuesContactChannel.

    A contact channel where users can get support via the repository
    issues page.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogLinkInstallDirective(sgqlc.types.Type):
    """Class for Nr1CatalogLinkInstallDirective.

    Information about a link install directive.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogNerdletInstallDirective(sgqlc.types.Type):
    """Class for Nr1CatalogNerdletInstallDirective.

    Information about a nerdlet install directive.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nerdlet_id", "nerdlet_state", "requires_account")
    nerdlet_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="nerdletId")


class Nr1CatalogNerdpack(sgqlc.types.Type):
    """Class for Nr1CatalogNerdpack.

    Information about the Nerdpack.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "metadata", "visibility")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class Nr1CatalogNerdpackMetadata(sgqlc.types.Type):
    """Class for Nr1CatalogNerdpackMetadata.

    Metadata associated with the Nerdpack that is available in the New
    Relic One Catalog.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "additional_info",
        "categories",
        "category_terms",
        "description",
        "details",
        "display_name",
        "documentation",
        "icon",
        "included_artifact_types",
        "keywords",
        "nerdpack_items",
        "previews",
        "publish_date",
        "repository",
        "support",
        "tagline",
        "version",
        "whats_new",
    )
    additional_info = sgqlc.types.Field(
        String,
        graphql_name="additionalInfo",
        args=sgqlc.types.ArgDict(
            (
                (
                    "format",
                    sgqlc.types.Arg(
                        Nr1CatalogRenderFormat,
                        graphql_name="format",
                        default="MARKDOWN",
                    ),
                ),
            )
        ),
    )


class Nr1CatalogQuickstart(sgqlc.types.Type):
    """Class for Nr1CatalogQuickstart.

    Information about the quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ("featured", "id", "metadata", "source_url", "support_level")
    featured = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="featured")


class Nr1CatalogQuickstartMetadata(sgqlc.types.Type):
    """Class for Nr1CatalogQuickstartMetadata.

    Metadata associated with the quickstart that is available in New
    Relic I/O.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "authors",
        "categories",
        "category_terms",
        "data_sources",
        "description",
        "display_name",
        "icon",
        "installer",
        "keywords",
        "quickstart_components",
        "slug",
        "summary",
    )
    authors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogAuthor))
        ),
        graphql_name="authors",
    )


class Nr1CatalogQuickstartsListing(sgqlc.types.Type):
    """Class for Nr1CatalogQuickstartsListing.

    Paginated information about Quickstarts.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "results", "total_count")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class Nr1CatalogReleaseNote(sgqlc.types.Type):
    """Class for Nr1CatalogReleaseNote.

    Information about the changes made to the metadata for a version
    of the Nerdpack.
    """

    __schema__ = nerdgraph
    __field_names__ = ("changes", "version")
    changes = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="changes")


class Nr1CatalogSearchFacets(sgqlc.types.Type):
    """Class for Nr1CatalogSearchFacets.

    Information about facets from a search.
    """

    __schema__ = nerdgraph
    __field_names__ = ("categories", "components", "featured", "types")
    categories = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogCategoryFacet))
        ),
        graphql_name="categories",
    )


class Nr1CatalogSearchResponse(sgqlc.types.Type):
    """Class for Nr1CatalogSearchResponse.

    Information about results returned from a search.
    """

    __schema__ = nerdgraph
    __field_names__ = ("facets", "next_cursor", "results", "total_count")
    facets = sgqlc.types.Field(
        sgqlc.types.non_null(Nr1CatalogSearchFacets), graphql_name="facets"
    )


class Nr1CatalogSearchResultTypeFacet(sgqlc.types.Type):
    """Class for Nr1CatalogSearchResultTypeFacet.

    Information about a facet count on a search result type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "type")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class Nr1CatalogSubmitMetadataError(sgqlc.types.Type):
    """Class for Nr1CatalogSubmitMetadataError.

    Information about the error that occurred as a result of
    submitting metadata.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "field", "type")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class Nr1CatalogSubmitMetadataResult(sgqlc.types.Type):
    """Class for Nr1CatalogSubmitMetadataResult.

    Information about the mutation result when submitting metadata.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "nerdpack", "result")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogSubmitMetadataError)),
        graphql_name="errors",
    )


class Nr1CatalogSupportChannels(sgqlc.types.Type):
    """Class for Nr1CatalogSupportChannels.

    A container for the various support channels.
    """

    __schema__ = nerdgraph
    __field_names__ = ("community", "email", "issues")
    community = sgqlc.types.Field(
        Nr1CatalogCommunityContactChannel, graphql_name="community"
    )


class NrdbMetadata(sgqlc.types.Type):
    """Class for NrdbMetadata.

    An object containing metadata about the query and result.
    """

    __schema__ = nerdgraph
    __field_names__ = ("event_types", "facets", "messages", "time_window")
    event_types = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="eventTypes"
    )


class NrdbMetadataTimeWindow(sgqlc.types.Type):
    """Class for NrdbMetadataTimeWindow.

    An object representing details about a query's time window.
    """

    __schema__ = nerdgraph
    __field_names__ = ("begin", "compare_with", "end", "since", "until")
    begin = sgqlc.types.Field(EpochMilliseconds, graphql_name="begin")


class NrdbQueryProgress(sgqlc.types.Type):
    """Class for NrdbQueryProgress.

    An object containing metadata about the execution of an
    asynchronous NRQL query.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "completed",
        "query_id",
        "result_expiration",
        "retry_after",
        "retry_deadline",
    )
    completed = sgqlc.types.Field(Boolean, graphql_name="completed")


class NrdbResultContainer(sgqlc.types.Type):
    """Class for NrdbResultContainer.

    A data structure that contains the results of the NRDB query along
    with other capabilities that enhance those results.  Direct query
    results are available through `results`, `totalResult` and
    `otherResult`. The query you made is accessible through `nrql`,
    along with `metadata` about the query itself. Enhanced
    capabilities include `eventDefinitions`, `suggestedFacets` and
    more.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "current_results",
        "embedded_chart_url",
        "event_definitions",
        "metadata",
        "nrql",
        "other_result",
        "previous_results",
        "query_progress",
        "raw_response",
        "results",
        "static_chart_url",
        "suggested_facets",
        "suggested_queries",
        "total_result",
    )
    current_results = sgqlc.types.Field(
        sgqlc.types.list_of(NrdbResult), graphql_name="currentResults"
    )


class NrqlDropRulesAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("list",)
    list = sgqlc.types.Field("NrqlDropRulesListDropRulesResult", graphql_name="list")


class NrqlDropRulesCreateDropRuleFailure(sgqlc.types.Type):
    """Class for NrqlDropRulesCreateDropRuleFailure.

    Error details about the rule that failed to be created and why.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "submitted")
    error = sgqlc.types.Field(
        sgqlc.types.non_null("NrqlDropRulesError"), graphql_name="error"
    )


class NrqlDropRulesCreateDropRuleResult(sgqlc.types.Type):
    """Class for NrqlDropRulesCreateDropRuleResult.

    The result of which submitted drop rules were successfully and
    unsuccessfully created.
    """

    __schema__ = nerdgraph
    __field_names__ = ("failures", "successes")
    failures = sgqlc.types.Field(
        sgqlc.types.list_of(NrqlDropRulesCreateDropRuleFailure), graphql_name="failures"
    )


class NrqlDropRulesCreateDropRuleSubmission(sgqlc.types.Type):
    """Class for NrqlDropRulesCreateDropRuleSubmission.

    The details that were submitted when creating a drop rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "action", "description", "nrql")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class NrqlDropRulesDeleteDropRuleFailure(sgqlc.types.Type):
    """Class for NrqlDropRulesDeleteDropRuleFailure.

    Error details about the rule that failed to be deleted and why.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "submitted")
    error = sgqlc.types.Field(
        sgqlc.types.non_null("NrqlDropRulesError"), graphql_name="error"
    )


class NrqlDropRulesDeleteDropRuleResult(sgqlc.types.Type):
    """Class for NrqlDropRulesDeleteDropRuleResult.

    The result of which drop rules were successfully and
    unsuccessfully deleted.
    """

    __schema__ = nerdgraph
    __field_names__ = ("failures", "successes")
    failures = sgqlc.types.Field(
        sgqlc.types.list_of(NrqlDropRulesDeleteDropRuleFailure), graphql_name="failures"
    )


class NrqlDropRulesDeleteDropRuleSubmission(sgqlc.types.Type):
    """Class for NrqlDropRulesDeleteDropRuleSubmission.

    The rules that were attempted to be deleted.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "rule_id")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class NrqlDropRulesDropRule(sgqlc.types.Type):
    """Class for NrqlDropRulesDropRule.

    Details of a drop rule.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account",
        "account_id",
        "action",
        "created_at",
        "created_by",
        "creator",
        "description",
        "id",
        "nrql",
        "source",
    )
    account = sgqlc.types.Field(AccountReference, graphql_name="account")


class NrqlDropRulesError(sgqlc.types.Type):
    """Class for NrqlDropRulesError.

    Error details when processing drop rule requests.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "reason")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class NrqlDropRulesListDropRulesResult(sgqlc.types.Type):
    """Class for NrqlDropRulesListDropRulesResult.

    The result of the request to list drop rules for an account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("error", "rules")
    error = sgqlc.types.Field(NrqlDropRulesError, graphql_name="error")


class NrqlFacetSuggestion(sgqlc.types.Type):
    """Class for NrqlFacetSuggestion.

    A suggested NRQL facet. Facet suggestions may be either a single
    attribute, or a list of attributes in the case of multi-attribute
    facet suggestions.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attributes", "nrql")
    attributes = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="attributes"
    )


class NrqlHistoricalQuery(sgqlc.types.Type):
    """Class for NrqlHistoricalQuery.

    An NRQL query executed in the past.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "nrql", "timestamp")
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class Organization(sgqlc.types.Type):
    """Class for Organization.

    The `Organization` object provides basic data about an
    organization.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_management",
        "account_shares",
        "administrator",
        "authorization_management",
        "customer_id",
        "id",
        "name",
        "telemetry_id",
        "user_management",
    )
    account_management = sgqlc.types.Field(
        AccountManagementOrganizationStitchedFields, graphql_name="accountManagement"
    )


class OrganizationAccountShares(sgqlc.types.Type):
    """Class for OrganizationAccountShares.

    An organization's shared accounts, both given and received.
    """

    __schema__ = nerdgraph
    __field_names__ = ("shared_accounts",)
    shared_accounts = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("OrganizationSharedAccount")),
        graphql_name="sharedAccounts",
    )


class OrganizationCreateSharedAccountResponse(sgqlc.types.Type):
    """Class for OrganizationCreateSharedAccountResponse.

    The object that's returned from successfully creating a shared
    account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("shared_account",)
    shared_account = sgqlc.types.Field(
        "OrganizationSharedAccount", graphql_name="sharedAccount"
    )


class OrganizationCustomerOrganization(sgqlc.types.Type):
    """Class for OrganizationCustomerOrganization.

    A customer organization.
    """

    __schema__ = nerdgraph
    __field_names__ = ("contract_id", "customer_id", "id", "name")
    contract_id = sgqlc.types.Field(ID, graphql_name="contractId")


class OrganizationCustomerOrganizationWrapper(sgqlc.types.Type):
    """Class for OrganizationCustomerOrganizationWrapper.

    A customer organization.
    """

    __schema__ = nerdgraph
    __field_names__ = ("items", "next_cursor")
    items = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(OrganizationCustomerOrganization)),
        graphql_name="items",
    )


class OrganizationError(sgqlc.types.Type):
    """Class for OrganizationError.

    A user-readable error.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class OrganizationInformation(sgqlc.types.Type):
    """Class for OrganizationInformation.

    The attributes of an organization.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")


class OrganizationOrganizationAdministrator(sgqlc.types.Type):
    """Class for OrganizationOrganizationAdministrator.

    The organization's administrator.
    """

    __schema__ = nerdgraph
    __field_names__ = ("organization_id", "organization_name")
    organization_id = sgqlc.types.Field(ID, graphql_name="organizationId")


class OrganizationProvisioningUpdateSubscriptionResult(sgqlc.types.Type):
    """Class for OrganizationProvisioningUpdateSubscriptionResult.

    Result of subscription update.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enqueued", "errors")
    enqueued = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enqueued")


class OrganizationProvisioningUserError(sgqlc.types.Type):
    """Class for OrganizationProvisioningUserError.

    A user-readable error.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "path")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class OrganizationRevokeSharedAccountResponse(sgqlc.types.Type):
    """Class for OrganizationRevokeSharedAccountResponse.

    The object that's returned from successfully revoking a shared
    account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("shared_account",)
    shared_account = sgqlc.types.Field(
        "OrganizationSharedAccount", graphql_name="sharedAccount"
    )


class OrganizationSharedAccount(sgqlc.types.Type):
    """Class for OrganizationSharedAccount.

    The attributes of an account share.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "id",
        "limiting_role_id",
        "name",
        "source_organization_id",
        "source_organization_name",
        "target_organization_id",
        "target_organization_name",
    )
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class OrganizationUpdateResponse(sgqlc.types.Type):
    """Class for OrganizationUpdateResponse.

    The return object for an update mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "organization_information")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(OrganizationError))
        ),
        graphql_name="errors",
    )


class OrganizationUpdateSharedAccountResponse(sgqlc.types.Type):
    """Class for OrganizationUpdateSharedAccountResponse.

    The object that's returned from successfully updating a shared
    account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("shared_account",)
    shared_account = sgqlc.types.Field(
        OrganizationSharedAccount, graphql_name="sharedAccount"
    )


class PixieAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("linked_pixie_project", "pixie_access_token")
    linked_pixie_project = sgqlc.types.Field(
        "PixiePixieProject", graphql_name="linkedPixieProject"
    )


class PixieActorStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("linked_pixie_projects",)
    linked_pixie_projects = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("PixieLinkedPixieProject")),
        graphql_name="linkedPixieProjects",
    )


class PixieLinkPixieProjectError(sgqlc.types.Type):
    """Class for PixieLinkPixieProjectError.

    An error object for linking a Pixie project.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class PixieLinkPixieProjectResult(sgqlc.types.Type):
    """Class for PixieLinkPixieProjectResult.

    The response returned when linking a Pixie project to a New Relic
    account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "linked_pixie_project", "success")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(PixieLinkPixieProjectError), graphql_name="errors"
    )


class PixieLinkedPixieProject(sgqlc.types.Type):
    """Class for PixieLinkedPixieProject.

    Pixie Project with the New Relic account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "pixie_project")
    account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="accountId")


class PixiePixieProject(sgqlc.types.Type):
    """Class for PixiePixieProject.

    Pixie Project keys linked to a New Relic account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("api_key", "deploy_key")
    api_key = sgqlc.types.Field(SecureValue, graphql_name="apiKey")


class PixieRecordPixieTosAcceptanceError(sgqlc.types.Type):
    """Class for PixieRecordPixieTosAcceptanceError.

    An error object for recording the Pixie terms of service
    acceptance.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class PixieRecordPixieTosAcceptanceResult(sgqlc.types.Type):
    """Class for PixieRecordPixieTosAcceptanceResult.

    The reponse returned when record the acceptance of the Pixie terms
    of service on a given account.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "success")
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(PixieRecordPixieTosAcceptanceError), graphql_name="errors"
    )


class QueryHistoryActorStitchedFields(sgqlc.types.Type):
    """Class for QueryHistoryActorStitchedFields.

    Type defined so its fields will be merged directly into
    NerdGraph's actor type.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql",)
    nrql = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("QueryHistoryNrqlHistoryResult")),
        graphql_name="nrql",
        args=sgqlc.types.ArgDict(
            (
                (
                    "options",
                    sgqlc.types.Arg(
                        QueryHistoryQueryHistoryOptionsInput,
                        graphql_name="options",
                        default=None,
                    ),
                ),
            )
        ),
    )


class QueryHistoryNrqlHistoryResult(sgqlc.types.Type):
    """Class for QueryHistoryNrqlHistoryResult.

    Represents the result of the query history record.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids", "created_at", "query")
    account_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="accountIds"
    )


class ReferenceEntityCreateRepositoryError(sgqlc.types.Type):
    """Class for ReferenceEntityCreateRepositoryError.

    Type that wraps the errors from a entity create operation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("guid", "message", "type")
    guid = sgqlc.types.Field(EntityGuid, graphql_name="guid")


class ReferenceEntityCreateRepositoryResult(sgqlc.types.Type):
    """Class for ReferenceEntityCreateRepositoryResult.

    Response type for create operations over entities.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created", "failures", "updated")
    created = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EntityGuid))),
        graphql_name="created",
    )


class RequestContext(sgqlc.types.Type):
    """Class for RequestContext.

    This object exposes contextual information about an API request.
    """

    __schema__ = nerdgraph
    __field_names__ = ("api_key", "user_id")
    api_key = sgqlc.types.Field(String, graphql_name="apiKey")


class RootMutationType(sgqlc.types.Type):
    """Class for RootMutationType.

    This is the root of all GraphQL mutations. Unlike queries,
    mutations represent actions that have a side effects, like
    `create` or `update`.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_management_create_account",
        "account_management_update_account",
        "agent_application_create_browser",
        "agent_application_create_mobile",
        "agent_application_delete",
        "agent_application_enable_apm_browser",
        "agent_application_settings_update",
        "ai_decisions_accept_suggestion",
        "ai_decisions_create_implicit_rule",
        "ai_decisions_create_rule",
        "ai_decisions_create_suggestion",
        "ai_decisions_decline_suggestion",
        "ai_decisions_delete_merge_feedback",
        "ai_decisions_delete_rule",
        "ai_decisions_delete_suggestion",
        "ai_decisions_disable_rule",
        "ai_decisions_enable_rule",
        "ai_decisions_find_applicable_incidents",
        "ai_decisions_postpone_suggestion",
        "ai_decisions_record_merge_feedback",
        "ai_decisions_simulate",
        "ai_decisions_update_implicit_rule",
        "ai_decisions_update_rule",
        "ai_issues_ack_issue",
        "ai_issues_resolve_issue",
        "ai_issues_unack_issue",
        "ai_issues_update_grace_period",
        "ai_issues_update_issue_ttl",
        "ai_notifications_create_channel",
        "ai_notifications_create_destination",
        "ai_notifications_delete_channel",
        "ai_notifications_delete_destination",
        "ai_notifications_test_channel",
        "ai_notifications_test_channel_by_id",
        "ai_notifications_test_destination",
        "ai_notifications_test_destination_by_id",
        "ai_notifications_update_channel",
        "ai_notifications_update_destination",
        "ai_topology_collector_create_edges",
        "ai_topology_collector_create_vertices",
        "ai_topology_collector_delete_edges",
        "ai_topology_collector_delete_vertices",
        "ai_workflows_create_workflow",
        "ai_workflows_delete_workflow",
        "ai_workflows_test_workflow",
        "ai_workflows_update_workflow",
        "alerts_condition_delete",
        "alerts_muting_rule_create",
        "alerts_muting_rule_delete",
        "alerts_muting_rule_update",
        "alerts_notification_channel_create",
        "alerts_notification_channel_delete",
        "alerts_notification_channel_update",
        "alerts_notification_channels_add_to_policy",
        "alerts_notification_channels_remove_from_policy",
        "alerts_nrql_condition_baseline_create",
        "alerts_nrql_condition_baseline_update",
        "alerts_nrql_condition_static_create",
        "alerts_nrql_condition_static_update",
        "alerts_policy_create",
        "alerts_policy_delete",
        "alerts_policy_update",
        "api_access_create_keys",
        "api_access_delete_keys",
        "api_access_update_keys",
        "authorization_management_grant_access",
        "authorization_management_revoke_access",
        "change_tracking_create_deployment",
        "cloud_configure_integration",
        "cloud_disable_integration",
        "cloud_link_account",
        "cloud_migrate_aws_gov_cloud_to_assume_role",
        "cloud_rename_account",
        "cloud_unlink_account",
        "dashboard_add_widgets_to_page",
        "dashboard_create",
        "dashboard_create_snapshot_url",
        "dashboard_delete",
        "dashboard_undelete",
        "dashboard_update",
        "dashboard_update_page",
        "dashboard_update_widgets_in_page",
        "dashboard_widget_revoke_live_url",
        "data_management_copy_retentions",
        "data_management_create_event_retention_rule",
        "data_management_create_retention_rules",
        "data_management_delete_event_retention_rule",
        "data_management_update_feature_settings",
        "edge_create_trace_filter_rules",
        "edge_create_trace_observer",
        "edge_delete_trace_filter_rules",
        "edge_delete_trace_observers",
        "edge_update_trace_observers",
        "entity_delete",
        "entity_golden_metrics_override",
        "entity_golden_metrics_reset",
        "entity_golden_tags_override",
        "entity_golden_tags_reset",
        "entity_relationship_user_defined_create_or_replace",
        "entity_relationship_user_defined_delete",
        "errors_inbox_assign_error_group",
        "errors_inbox_delete_error_group_resource",
        "errors_inbox_update_error_group_state",
        "events_to_metrics_create_rule",
        "events_to_metrics_delete_rule",
        "events_to_metrics_update_rule",
        "historical_data_export_cancel_export",
        "historical_data_export_create_export",
        "incident_intelligence_environment_consent_accounts",
        "incident_intelligence_environment_consent_authorized_accounts",
        "incident_intelligence_environment_delete_environment",
        "incident_intelligence_environment_dissent_accounts",
        "installation_create_install_status",
        "installation_create_recipe_event",
        "installation_delete_install",
        "key_transaction_create",
        "key_transaction_delete",
        "key_transaction_update",
        "log_configurations_create_data_partition_rule",
        "log_configurations_create_obfuscation_expression",
        "log_configurations_create_obfuscation_rule",
        "log_configurations_create_parsing_rule",
        "log_configurations_delete_data_partition_rule",
        "log_configurations_delete_obfuscation_expression",
        "log_configurations_delete_obfuscation_rule",
        "log_configurations_delete_parsing_rule",
        "log_configurations_update_data_partition_rule",
        "log_configurations_update_obfuscation_expression",
        "log_configurations_update_obfuscation_rule",
        "log_configurations_update_parsing_rule",
        "log_configurations_upsert_pipeline_configuration",
        "metric_normalization_create_rule",
        "metric_normalization_disable_rule",
        "metric_normalization_edit_rule",
        "metric_normalization_enable_rule",
        "mobile_push_notification_remove_device",
        "mobile_push_notification_send_test_push",
        "mobile_push_notification_send_test_push_to_all",
        "nerd_storage_delete_collection",
        "nerd_storage_delete_document",
        "nerd_storage_vault_delete_secret",
        "nerd_storage_vault_write_secret",
        "nerd_storage_write_document",
        "nerdpack_add_allowed_accounts",
        "nerdpack_create",
        "nerdpack_remove_allowed_accounts",
        "nerdpack_remove_version_tag",
        "nerdpack_subscribe_accounts",
        "nerdpack_tag_version",
        "nerdpack_unsubscribe_accounts",
        "nr1_catalog_install_alert_policy_template",
        "nr1_catalog_install_dashboard_template",
        "nr1_catalog_submit_metadata",
        "nrql_drop_rules_create",
        "nrql_drop_rules_delete",
        "organization_create_shared_account",
        "organization_provisioning_update_partner_subscription",
        "organization_revoke_shared_account",
        "organization_update",
        "organization_update_shared_account",
        "pixie_link_pixie_project",
        "pixie_record_pixie_tos_acceptance",
        "pixie_unlink_pixie_project",
        "reference_entity_create_or_update_repository",
        "service_level_create",
        "service_level_delete",
        "service_level_update",
        "streaming_export_create_rule",
        "streaming_export_delete_rule",
        "streaming_export_disable_rule",
        "streaming_export_enable_rule",
        "streaming_export_update_rule",
        "synthetics_create_broken_links_monitor",
        "synthetics_create_cert_check_monitor",
        "synthetics_create_private_location",
        "synthetics_create_script_api_monitor",
        "synthetics_create_script_browser_monitor",
        "synthetics_create_secure_credential",
        "synthetics_create_simple_browser_monitor",
        "synthetics_create_simple_monitor",
        "synthetics_create_step_monitor",
        "synthetics_delete_monitor",
        "synthetics_delete_private_location",
        "synthetics_delete_secure_credential",
        "synthetics_purge_private_location_queue",
        "synthetics_update_broken_links_monitor",
        "synthetics_update_cert_check_monitor",
        "synthetics_update_private_location",
        "synthetics_update_script_api_monitor",
        "synthetics_update_script_browser_monitor",
        "synthetics_update_secure_credential",
        "synthetics_update_simple_browser_monitor",
        "synthetics_update_simple_monitor",
        "synthetics_update_step_monitor",
        "tagging_add_tags_to_entity",
        "tagging_delete_tag_from_entity",
        "tagging_delete_tag_values_from_entity",
        "tagging_replace_tags_on_entity",
        "user_management_add_users_to_groups",
        "user_management_create_group",
        "user_management_create_user",
        "user_management_delete_group",
        "user_management_delete_user",
        "user_management_remove_users_from_groups",
        "user_management_update_group",
        "user_management_update_user",
        "whats_new_set_last_read_date",
        "workload_create",
        "workload_delete",
        "workload_duplicate",
        "workload_update",
    )
    account_management_create_account = sgqlc.types.Field(
        AccountManagementCreateResponse,
        graphql_name="accountManagementCreateAccount",
        args=sgqlc.types.ArgDict(
            (
                (
                    "managed_account",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(AccountManagementCreateInput),
                        graphql_name="managedAccount",
                        default=None,
                    ),
                ),
            )
        ),
    )


class RootQueryType(sgqlc.types.Type):
    """Class for RootQueryType.

    This is the root of all GraphQL queries. The fields in this object
    are available at the top level of a query.
    """

    __schema__ = nerdgraph
    __field_names__ = ("actor", "docs", "request_context")
    actor = sgqlc.types.Field(Actor, graphql_name="actor")


class SecureCredentialSummaryData(sgqlc.types.Type):
    """Class for SecureCredentialSummaryData.

    Summary statistics for the Synthetic Monitor Secure Credential.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class ServiceLevelDefinition(sgqlc.types.Type):
    """Class for ServiceLevelDefinition.

    The service level defined for a specific entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ("indicators",)
    indicators = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("ServiceLevelIndicator")),
        graphql_name="indicators",
    )


class ServiceLevelEvents(sgqlc.types.Type):
    """Class for ServiceLevelEvents.

    The events that define the SLI.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account", "bad_events", "good_events", "valid_events")
    account = sgqlc.types.Field(AccountReference, graphql_name="account")


class ServiceLevelEventsQuery(sgqlc.types.Type):
    """Class for ServiceLevelEventsQuery.

    The query that represents the events to fetch.
    """

    __schema__ = nerdgraph
    __field_names__ = ("from_", "select", "where")
    from_ = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="from")


class ServiceLevelEventsQuerySelect(sgqlc.types.Type):
    """Class for ServiceLevelEventsQuerySelect.

    The resulting NRQL SELECT clause to aggregate events.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attribute", "function")
    attribute = sgqlc.types.Field(String, graphql_name="attribute")


class ServiceLevelIndicator(sgqlc.types.Type):
    """Class for ServiceLevelIndicator.

    The definition of the SLI.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "created_by",
        "description",
        "entity_guid",
        "events",
        "guid",
        "id",
        "name",
        "objectives",
        "result_queries",
        "updated_at",
        "updated_by",
    )
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(EpochMilliseconds), graphql_name="createdAt"
    )


class ServiceLevelIndicatorResultQueries(sgqlc.types.Type):
    """Class for ServiceLevelIndicatorResultQueries.

    The resulting NRQL queries that help consume the metrics of the
    SLI.
    """

    __schema__ = nerdgraph
    __field_names__ = ("good_events", "indicator", "valid_events")
    good_events = sgqlc.types.Field(
        sgqlc.types.non_null("ServiceLevelResultQuery"), graphql_name="goodEvents"
    )


class ServiceLevelObjective(sgqlc.types.Type):
    """Class for ServiceLevelObjective.

    An objective definition.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "name", "result_queries", "target", "time_window")
    description = sgqlc.types.Field(String, graphql_name="description")


class ServiceLevelObjectiveResultQueries(sgqlc.types.Type):
    """Class for ServiceLevelObjectiveResultQueries.

    The resulting NRQL queries that help consume the metrics of the
    SLO.
    """

    __schema__ = nerdgraph
    __field_names__ = ("attainment",)
    attainment = sgqlc.types.Field(
        sgqlc.types.non_null("ServiceLevelResultQuery"), graphql_name="attainment"
    )


class ServiceLevelObjectiveRollingTimeWindow(sgqlc.types.Type):
    """Class for ServiceLevelObjectiveRollingTimeWindow.

    The rolling time window configuration of the SLO.
    """

    __schema__ = nerdgraph
    __field_names__ = ("count", "unit")
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="count")


class ServiceLevelObjectiveTimeWindow(sgqlc.types.Type):
    """Class for ServiceLevelObjectiveTimeWindow.

    The time window configuration of the SLO.
    """

    __schema__ = nerdgraph
    __field_names__ = ("rolling",)
    rolling = sgqlc.types.Field(
        ServiceLevelObjectiveRollingTimeWindow, graphql_name="rolling"
    )


class ServiceLevelResultQuery(sgqlc.types.Type):
    """Class for ServiceLevelResultQuery.

    A resulting query.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nrql",)
    nrql = sgqlc.types.Field(sgqlc.types.non_null(Nrql), graphql_name="nrql")


class StackTraceApmException(sgqlc.types.Type):
    """Class for StackTraceApmException.

    A structured representation of an exception for an APM
    application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "stack_trace")
    message = sgqlc.types.Field(String, graphql_name="message")


class StackTraceApmStackTrace(sgqlc.types.Type):
    """Class for StackTraceApmStackTrace.

    A structured representation of a stack trace for an APM
    application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("frames",)
    frames = sgqlc.types.Field(
        sgqlc.types.list_of("StackTraceApmStackTraceFrame"), graphql_name="frames"
    )


class StackTraceApmStackTraceFrame(sgqlc.types.Type):
    """Class for StackTraceApmStackTraceFrame.

    An object representing a stack trace segment.
    """

    __schema__ = nerdgraph
    __field_names__ = ("filepath", "formatted", "line", "name")
    filepath = sgqlc.types.Field(String, graphql_name="filepath")


class StackTraceBrowserException(sgqlc.types.Type):
    """Class for StackTraceBrowserException.

    A structured representation of an exception for a Browser
    application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "stack_trace")
    message = sgqlc.types.Field(String, graphql_name="message")


class StackTraceBrowserStackTrace(sgqlc.types.Type):
    """Class for StackTraceBrowserStackTrace.

    A structured representation of a stack trace for a Browser
    application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("frames",)
    frames = sgqlc.types.Field(
        sgqlc.types.list_of("StackTraceBrowserStackTraceFrame"), graphql_name="frames"
    )


class StackTraceBrowserStackTraceFrame(sgqlc.types.Type):
    """Class for StackTraceBrowserStackTraceFrame.

    An object representing a stack trace segment.
    """

    __schema__ = nerdgraph
    __field_names__ = ("column", "formatted", "line", "name")
    column = sgqlc.types.Field(Int, graphql_name="column")


class StackTraceMobileCrash(sgqlc.types.Type):
    """Class for StackTraceMobileCrash.

    A structured representation of a crash occurring in a mobile
    application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("stack_trace",)
    stack_trace = sgqlc.types.Field(
        "StackTraceMobileCrashStackTrace", graphql_name="stackTrace"
    )


class StackTraceMobileCrashStackTrace(sgqlc.types.Type):
    """Class for StackTraceMobileCrashStackTrace.

    A structured representation of a stack trace of a crash in a
    mobile application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("frames",)
    frames = sgqlc.types.Field(
        sgqlc.types.list_of("StackTraceMobileCrashStackTraceFrame"),
        graphql_name="frames",
    )


class StackTraceMobileCrashStackTraceFrame(sgqlc.types.Type):
    """Class for StackTraceMobileCrashStackTraceFrame.

    An object representing a stack trace segment.
    """

    __schema__ = nerdgraph
    __field_names__ = ("filepath", "formatted", "line", "name")
    filepath = sgqlc.types.Field(String, graphql_name="filepath")


class StackTraceMobileException(sgqlc.types.Type):
    """Class for StackTraceMobileException.

    A structured representation of a handled exception occurring in a
    mobile application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("stack_trace",)
    stack_trace = sgqlc.types.Field(
        "StackTraceMobileExceptionStackTrace", graphql_name="stackTrace"
    )


class StackTraceMobileExceptionStackTrace(sgqlc.types.Type):
    """Class for StackTraceMobileExceptionStackTrace.

    A structured representation of a handled exception in a mobile
    application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("frames",)
    frames = sgqlc.types.Field(
        sgqlc.types.list_of("StackTraceMobileExceptionStackTraceFrame"),
        graphql_name="frames",
    )


class StackTraceMobileExceptionStackTraceFrame(sgqlc.types.Type):
    """Class for StackTraceMobileExceptionStackTraceFrame.

    An object representing a stack trace segment.
    """

    __schema__ = nerdgraph
    __field_names__ = ("filepath", "formatted", "line", "name")
    filepath = sgqlc.types.Field(String, graphql_name="filepath")


class StreamingExportAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("streaming_rule", "streaming_rules")
    streaming_rule = sgqlc.types.Field(
        "StreamingExportRule",
        graphql_name="streamingRule",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )


class StreamingExportAwsDetails(sgqlc.types.Type):
    """Class for StreamingExportAwsDetails.

    AWS details about a streaming rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_account_id", "delivery_stream_name", "region", "role")
    aws_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="awsAccountId"
    )


class StreamingExportAzureDetails(sgqlc.types.Type):
    """Class for StreamingExportAzureDetails.

    Azure details about a streaming rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("event_hub_connection_string", "event_hub_name")
    event_hub_connection_string = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="eventHubConnectionString"
    )


class StreamingExportRule(sgqlc.types.Type):
    """Class for StreamingExportRule.

    Details about a streaming rule.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account",
        "aws",
        "azure",
        "created_at",
        "description",
        "id",
        "message",
        "name",
        "nrql",
        "status",
        "updated_at",
    )
    account = sgqlc.types.Field(AccountReference, graphql_name="account")


class SuggestedNrqlQueryAnomaly(sgqlc.types.Type):
    """Class for SuggestedNrqlQueryAnomaly.

    Information about the anomaly upon which this analysis was based.
    """

    __schema__ = nerdgraph
    __field_names__ = ("time_window",)
    time_window = sgqlc.types.Field(
        sgqlc.types.non_null("TimeWindow"), graphql_name="timeWindow"
    )


class SuggestedNrqlQueryResponse(sgqlc.types.Type):
    """Class for SuggestedNrqlQueryResponse.

    A result type encapsulating suggested queries.
    """

    __schema__ = nerdgraph
    __field_names__ = ("suggestions",)
    suggestions = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(SuggestedNrqlQuery)),
        graphql_name="suggestions",
    )


class SyntheticMonitorSummaryData(sgqlc.types.Type):
    """Class for SyntheticMonitorSummaryData.

    Summary statistics for the Synthetic Monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "locations_failing",
        "locations_running",
        "status",
        "success_rate",
    )
    locations_failing = sgqlc.types.Field(Int, graphql_name="locationsFailing")


class SyntheticsAccountStitchedFields(sgqlc.types.Type):
    """Class for SyntheticsAccountStitchedFields.

    Nerdgraph account field.
    """

    __schema__ = nerdgraph
    __field_names__ = ("script", "steps")
    script = sgqlc.types.Field(
        "SyntheticsMonitorScriptQueryResponse",
        graphql_name="script",
        args=sgqlc.types.ArgDict(
            (
                (
                    "monitor_guid",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(EntityGuid),
                        graphql_name="monitorGuid",
                        default=None,
                    ),
                ),
            )
        ),
    )


class SyntheticsBrokenLinksMonitor(sgqlc.types.Type):
    """Class for SyntheticsBrokenLinksMonitor.

    A Broken Links monitor resulting from a Broken Links monitor
    mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "guid",
        "id",
        "locations",
        "modified_at",
        "name",
        "period",
        "status",
        "uri",
    )
    created_at = sgqlc.types.Field(EpochMilliseconds, graphql_name="createdAt")


class SyntheticsBrokenLinksMonitorCreateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsBrokenLinksMonitorCreateMutationResult.

    The result of a Broken Links monitor create mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("SyntheticsMonitorCreateError")),
        graphql_name="errors",
    )


class SyntheticsBrokenLinksMonitorUpdateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsBrokenLinksMonitorUpdateMutationResult.

    The result of a Broken Links monitor update mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("SyntheticsMonitorUpdateError")),
        graphql_name="errors",
    )


class SyntheticsCertCheckMonitor(sgqlc.types.Type):
    """Class for SyntheticsCertCheckMonitor.

    A Cert Check monitor resulting from a Cert Check monitor mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "domain",
        "guid",
        "id",
        "locations",
        "modified_at",
        "name",
        "number_days_to_fail_before_cert_expires",
        "period",
        "status",
    )
    created_at = sgqlc.types.Field(EpochMilliseconds, graphql_name="createdAt")


class SyntheticsCertCheckMonitorCreateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsCertCheckMonitorCreateMutationResult.

    The result of a Cert Check monitor create mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("SyntheticsMonitorCreateError")),
        graphql_name="errors",
    )


class SyntheticsCertCheckMonitorUpdateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsCertCheckMonitorUpdateMutationResult.

    The result of a Cert Check monitor update mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("SyntheticsMonitorUpdateError")),
        graphql_name="errors",
    )


class SyntheticsCustomHeader(sgqlc.types.Type):
    """Class for SyntheticsCustomHeader.

    Custom header for monitor jobs.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "value")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class SyntheticsDeviceEmulation(sgqlc.types.Type):
    """Class for SyntheticsDeviceEmulation.

    Information related to device emulation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("device_orientation", "device_type")
    device_orientation = sgqlc.types.Field(
        sgqlc.types.non_null(SyntheticsDeviceOrientation),
        graphql_name="deviceOrientation",
    )


class SyntheticsError(sgqlc.types.Type):
    """Class for SyntheticsError.

    Error object for Synthetics mutations.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description",)
    description = sgqlc.types.Field(String, graphql_name="description")


class SyntheticsLocations(sgqlc.types.Type):
    """Class for SyntheticsLocations.

    The location(s) from which the monitor runs.
    """

    __schema__ = nerdgraph
    __field_names__ = ("private", "public")
    private = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="private")


class SyntheticsMonitorCreateError(sgqlc.types.Type):
    """Class for SyntheticsMonitorCreateError.

    Error object for Synthetics monitor creation request.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class SyntheticsMonitorDeleteMutationResult(sgqlc.types.Type):
    """Class for SyntheticsMonitorDeleteMutationResult.

    The result of a monitor delete mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("deleted_guid",)
    deleted_guid = sgqlc.types.Field(EntityGuid, graphql_name="deletedGuid")


class SyntheticsMonitorScriptQueryResponse(sgqlc.types.Type):
    """Class for SyntheticsMonitorScriptQueryResponse.

    The script that a monitor runs.
    """

    __schema__ = nerdgraph
    __field_names__ = ("text",)
    text = sgqlc.types.Field(String, graphql_name="text")


class SyntheticsMonitorUpdateError(sgqlc.types.Type):
    """Class for SyntheticsMonitorUpdateError.

    Error object for Synthetics monitor update request.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class SyntheticsPrivateLocationDeleteResult(sgqlc.types.Type):
    """Class for SyntheticsPrivateLocationDeleteResult.

    An array containing errors from the deletion of a private
    location, if any.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of("SyntheticsPrivateLocationMutationError"),
        graphql_name="errors",
    )


class SyntheticsPrivateLocationMutationError(sgqlc.types.Type):
    """Class for SyntheticsPrivateLocationMutationError.

    Error object for Synthetic Private Location mutation request.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "type")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )


class SyntheticsPrivateLocationMutationResult(sgqlc.types.Type):
    """Class for SyntheticsPrivateLocationMutationResult.

    Result of a private location mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account_id",
        "description",
        "domain_id",
        "errors",
        "guid",
        "key",
        "location_id",
        "name",
        "verified_script_execution",
    )
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class SyntheticsPrivateLocationPurgeQueueResult(sgqlc.types.Type):
    """Class for SyntheticsPrivateLocationPurgeQueueResult.

    Result of a Synthetics purge private location queue mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsPrivateLocationMutationError),
        graphql_name="errors",
    )


class SyntheticsRuntime(sgqlc.types.Type):
    """Class for SyntheticsRuntime.

    The runtime that a monitor runs.
    """

    __schema__ = nerdgraph
    __field_names__ = ("runtime_type", "runtime_type_version", "script_language")
    runtime_type = sgqlc.types.Field(String, graphql_name="runtimeType")


class SyntheticsScriptApiMonitor(sgqlc.types.Type):
    """Class for SyntheticsScriptApiMonitor.

    A Script Api monitor resulting from a Script Api mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "guid",
        "id",
        "locations",
        "modified_at",
        "name",
        "period",
        "runtime",
        "status",
    )
    created_at = sgqlc.types.Field(EpochMilliseconds, graphql_name="createdAt")


class SyntheticsScriptApiMonitorCreateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsScriptApiMonitorCreateMutationResult.

    The result of a Script Api monitor create mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(SyntheticsMonitorCreateError)),
        graphql_name="errors",
    )


class SyntheticsScriptApiMonitorUpdateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsScriptApiMonitorUpdateMutationResult.

    The result of a Script Api monitor update mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(SyntheticsMonitorUpdateError)),
        graphql_name="errors",
    )


class SyntheticsScriptBrowserMonitor(sgqlc.types.Type):
    """Class for SyntheticsScriptBrowserMonitor.

    A Script Browser monitor resulting from a Script Browser mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "created_at",
        "guid",
        "id",
        "locations",
        "modified_at",
        "name",
        "period",
        "runtime",
        "status",
    )
    advanced_options = sgqlc.types.Field(
        "SyntheticsScriptBrowserMonitorAdvancedOptions", graphql_name="advancedOptions"
    )


class SyntheticsScriptBrowserMonitorAdvancedOptions(sgqlc.types.Type):
    """Class for SyntheticsScriptBrowserMonitorAdvancedOptions.

    The advanced options available for a Script Browser monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = ("device_emulation", "enable_screenshot_on_failure_and_script")
    device_emulation = sgqlc.types.Field(
        SyntheticsDeviceEmulation, graphql_name="deviceEmulation"
    )


class SyntheticsScriptBrowserMonitorCreateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsScriptBrowserMonitorCreateMutationResult.

    The result of a Script Browser monitor create mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(SyntheticsMonitorCreateError)),
        graphql_name="errors",
    )


class SyntheticsScriptBrowserMonitorUpdateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsScriptBrowserMonitorUpdateMutationResult.

    The result of a Script Browser monitor update mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(SyntheticsMonitorUpdateError)),
        graphql_name="errors",
    )


class SyntheticsSecureCredentialMutationResult(sgqlc.types.Type):
    """Class for SyntheticsSecureCredentialMutationResult.

    The result of a secure credential mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_at", "description", "errors", "key", "last_update")
    created_at = sgqlc.types.Field(EpochMilliseconds, graphql_name="createdAt")


class SyntheticsSimpleBrowserMonitor(sgqlc.types.Type):
    """Class for SyntheticsSimpleBrowserMonitor.

    A Simple Browser monitor resulting from a Simple Browser monitor
    mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "created_at",
        "guid",
        "id",
        "locations",
        "modified_at",
        "name",
        "period",
        "runtime",
        "status",
        "uri",
    )
    advanced_options = sgqlc.types.Field(
        "SyntheticsSimpleBrowserMonitorAdvancedOptions", graphql_name="advancedOptions"
    )


class SyntheticsSimpleBrowserMonitorAdvancedOptions(sgqlc.types.Type):
    """Class for SyntheticsSimpleBrowserMonitorAdvancedOptions.

    The advanced options available for a Simple Browser monitor.
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
        sgqlc.types.list_of(SyntheticsCustomHeader), graphql_name="customHeaders"
    )


class SyntheticsSimpleBrowserMonitorCreateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsSimpleBrowserMonitorCreateMutationResult.

    The result of a Simple Browser monitor create mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(SyntheticsMonitorCreateError)),
        graphql_name="errors",
    )


class SyntheticsSimpleBrowserMonitorUpdateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsSimpleBrowserMonitorUpdateMutationResult.

    The result of a Simple Browser monitor update mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(SyntheticsMonitorUpdateError)),
        graphql_name="errors",
    )


class SyntheticsSimpleMonitor(sgqlc.types.Type):
    """Class for SyntheticsSimpleMonitor.

    A Simple (ping) monitor resulting from a Simple monitor mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "created_at",
        "guid",
        "id",
        "locations",
        "modified_at",
        "name",
        "period",
        "status",
        "uri",
    )
    advanced_options = sgqlc.types.Field(
        "SyntheticsSimpleMonitorAdvancedOptions", graphql_name="advancedOptions"
    )


class SyntheticsSimpleMonitorAdvancedOptions(sgqlc.types.Type):
    """Class for SyntheticsSimpleMonitorAdvancedOptions.

    The advanced options available for a Simple (ping) monitor.
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
        sgqlc.types.list_of(SyntheticsCustomHeader), graphql_name="customHeaders"
    )


class SyntheticsSimpleMonitorUpdateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsSimpleMonitorUpdateMutationResult.

    The result of a Simple (ping) monitor update mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(SyntheticsMonitorUpdateError)),
        graphql_name="errors",
    )


class SyntheticsStep(sgqlc.types.Type):
    """Class for SyntheticsStep.

    A step that will be added to the monitor script.
    """

    __schema__ = nerdgraph
    __field_names__ = ("ordinal", "type", "values")
    ordinal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="ordinal")


class SyntheticsStepMonitor(sgqlc.types.Type):
    """Class for SyntheticsStepMonitor.

    A Step monitor resulting from a Step monitor mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "advanced_options",
        "created_at",
        "guid",
        "id",
        "locations",
        "modified_at",
        "name",
        "period",
        "status",
        "steps",
    )
    advanced_options = sgqlc.types.Field(
        "SyntheticsStepMonitorAdvancedOptions", graphql_name="advancedOptions"
    )


class SyntheticsStepMonitorAdvancedOptions(sgqlc.types.Type):
    """Class for SyntheticsStepMonitorAdvancedOptions.

    The advanced options available for a Step monitor.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enable_screenshot_on_failure_and_script",)
    enable_screenshot_on_failure_and_script = sgqlc.types.Field(
        Boolean, graphql_name="enableScreenshotOnFailureAndScript"
    )


class SyntheticsStepMonitorCreateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsStepMonitorCreateMutationResult.

    The result of a Step monitor create mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(SyntheticsMonitorCreateError)),
        graphql_name="errors",
    )


class SyntheticsStepMonitorUpdateMutationResult(sgqlc.types.Type):
    """Class for SyntheticsStepMonitorUpdateMutationResult.

    The result of a Step monitor update mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors", "monitor")
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(SyntheticsMonitorUpdateError)),
        graphql_name="errors",
    )


class SyntheticsSyntheticMonitorAsset(sgqlc.types.Type):
    """Class for SyntheticsSyntheticMonitorAsset.

    Asset produced during the execution of the check.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type", "url")
    type = sgqlc.types.Field(String, graphql_name="type")


class TaggingMutationError(sgqlc.types.Type):
    """Class for TaggingMutationError.

    An error object for tag mutations.
    """

    __schema__ = nerdgraph
    __field_names__ = ("message", "type")
    message = sgqlc.types.Field(String, graphql_name="message")


class TaggingMutationResult(sgqlc.types.Type):
    """Class for TaggingMutationResult.

    The result of a tag mutation.
    """

    __schema__ = nerdgraph
    __field_names__ = ("errors",)
    errors = sgqlc.types.Field(
        sgqlc.types.list_of(TaggingMutationError), graphql_name="errors"
    )


class TimeWindow(sgqlc.types.Type):
    """Class for TimeWindow.

    Represents a time window.
    """

    __schema__ = nerdgraph
    __field_names__ = ("end_time", "start_time")
    end_time = sgqlc.types.Field(EpochMilliseconds, graphql_name="endTime")


class TimeZoneInfo(sgqlc.types.Type):
    """Class for TimeZoneInfo.

    Information about a Time Zone.
    """

    __schema__ = nerdgraph
    __field_names__ = ("name", "offset")
    name = sgqlc.types.Field(String, graphql_name="name")


class User(sgqlc.types.Type):
    """Class for User.

    The `User` object provides general data about the user.
    """

    __schema__ = nerdgraph
    __field_names__ = ("email", "id", "name")
    email = sgqlc.types.Field(String, graphql_name="email")

    id = sgqlc.types.Field(Int, graphql_name="id")

    name = sgqlc.types.Field(String, graphql_name="name")


class UserManagementAddUsersToGroupsPayload(sgqlc.types.Type):
    """Class for UserManagementAddUsersToGroupsPayload.

    Autogenerated return type of AddUsersToGroups.
    """

    __schema__ = nerdgraph
    __field_names__ = ("groups",)
    groups = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("UserManagementGroup")),
        graphql_name="groups",
    )


class UserManagementAuthenticationDomain(sgqlc.types.Type):
    """Class for UserManagementAuthenticationDomain.

    An "authentication domain" is a grouping of New Relic users
    governed by the same user management settings, like how they're
    provisioned (added and updated), how they're authenticated (logged
    in), session settings, and how user upgrades are managed.
    """

    __schema__ = nerdgraph
    __field_names__ = ("groups", "id", "name", "provisioning_type", "users")
    groups = sgqlc.types.Field(
        "UserManagementGroups",
        graphql_name="groups",
        args=sgqlc.types.ArgDict(
            (
                (
                    "cursor",
                    sgqlc.types.Arg(String, graphql_name="cursor", default=None),
                ),
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                        graphql_name="id",
                        default=None,
                    ),
                ),
            )
        ),
    )


class UserManagementAuthenticationDomains(sgqlc.types.Type):
    """Class for UserManagementAuthenticationDomains.

    container for authentication domains enabling cursor based
    pagination.
    """

    __schema__ = nerdgraph
    __field_names__ = ("authentication_domains", "next_cursor", "total_count")
    authentication_domains = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(
                sgqlc.types.non_null(UserManagementAuthenticationDomain)
            )
        ),
        graphql_name="authenticationDomains",
    )


class UserManagementCreateGroupPayload(sgqlc.types.Type):
    """Class for UserManagementCreateGroupPayload.

    Autogenerated return type of CreateGroup.
    """

    __schema__ = nerdgraph
    __field_names__ = ("group",)
    group = sgqlc.types.Field("UserManagementGroup", graphql_name="group")


class UserManagementCreateUserPayload(sgqlc.types.Type):
    """Class for UserManagementCreateUserPayload.

    Autogenerated return type of CreateUser.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_user",)
    created_user = sgqlc.types.Field(
        "UserManagementCreatedUser", graphql_name="createdUser"
    )


class UserManagementCreatedUser(sgqlc.types.Type):
    """Class for UserManagementCreatedUser.

    A newly created user of New Relic scoped to an authentication
    domain.
    """

    __schema__ = nerdgraph
    __field_names__ = ("authentication_domain_id", "email", "id", "name", "type")
    authentication_domain_id = sgqlc.types.Field(
        ID, graphql_name="authenticationDomainId"
    )


class UserManagementDeleteGroupPayload(sgqlc.types.Type):
    """Class for UserManagementDeleteGroupPayload.

    Autogenerated return type of DeleteGroup.
    """

    __schema__ = nerdgraph
    __field_names__ = ("group",)
    group = sgqlc.types.Field("UserManagementGroup", graphql_name="group")


class UserManagementDeleteUserPayload(sgqlc.types.Type):
    """Class for UserManagementDeleteUserPayload.

    Autogenerated return type of DeleteUser.
    """

    __schema__ = nerdgraph
    __field_names__ = ("deleted_user",)
    deleted_user = sgqlc.types.Field(
        "UserManagementDeletedUser", graphql_name="deletedUser"
    )


class UserManagementDeletedUser(sgqlc.types.Type):
    """Class for UserManagementDeletedUser.

    A user of New Relic to be deleted.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class UserManagementGroup(sgqlc.types.Type):
    """Class for UserManagementGroup.

    For users on our New Relic One user model, a "group" represents a
    group of users. Putting users in a group allows the managing of
    permissions for multiple users at the same time.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_name", "id", "users")
    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )


class UserManagementGroupUser(sgqlc.types.Type):
    """Class for UserManagementGroupUser.

    User information returned within Groups.
    """

    __schema__ = nerdgraph
    __field_names__ = ("email", "id", "name", "time_zone")
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="email")


class UserManagementGroupUsers(sgqlc.types.Type):
    """Class for UserManagementGroupUsers.

    container for users enabling cursor based pagination.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "total_count", "users")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class UserManagementGroups(sgqlc.types.Type):
    """Class for UserManagementGroups.

    container for groups enabling cursor based pagination.
    """

    __schema__ = nerdgraph
    __field_names__ = ("groups", "next_cursor", "total_count")
    groups = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(UserManagementGroup))
        ),
        graphql_name="groups",
    )


class UserManagementOrganizationStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("authentication_domains", "types")
    authentication_domains = sgqlc.types.Field(
        UserManagementAuthenticationDomains,
        graphql_name="authenticationDomains",
        args=sgqlc.types.ArgDict(
            (
                (
                    "cursor",
                    sgqlc.types.Arg(String, graphql_name="cursor", default=None),
                ),
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(sgqlc.types.non_null(ID)),
                        graphql_name="id",
                        default=None,
                    ),
                ),
            )
        ),
    )


class UserManagementOrganizationUserType(sgqlc.types.Type):
    """Class for UserManagementOrganizationUserType.

    A "user type" is what determines the set of New Relic capabilities
    a user can theoretically access.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_name", "id")
    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )


class UserManagementRemoveUsersFromGroupsPayload(sgqlc.types.Type):
    """Class for UserManagementRemoveUsersFromGroupsPayload.

    Autogenerated return type of RemoveUsersFromGroups.
    """

    __schema__ = nerdgraph
    __field_names__ = ("groups",)
    groups = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(UserManagementGroup)),
        graphql_name="groups",
    )


class UserManagementUpdateGroupPayload(sgqlc.types.Type):
    """Class for UserManagementUpdateGroupPayload.

    Autogenerated return type of UpdateGroup.
    """

    __schema__ = nerdgraph
    __field_names__ = ("group",)
    group = sgqlc.types.Field(UserManagementGroup, graphql_name="group")


class UserManagementUpdateUserPayload(sgqlc.types.Type):
    """Class for UserManagementUpdateUserPayload.

    Autogenerated return type of UpdateUser.
    """

    __schema__ = nerdgraph
    __field_names__ = ("user",)
    user = sgqlc.types.Field("UserManagementUser", graphql_name="user")


class UserManagementUser(sgqlc.types.Type):
    """Class for UserManagementUser.

    A user of New Relic scoped to an authentication domain.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "email",
        "email_verification_state",
        "groups",
        "id",
        "last_active",
        "name",
        "time_zone",
        "type",
    )
    email = sgqlc.types.Field(String, graphql_name="email")


class UserManagementUserGroup(sgqlc.types.Type):
    """Class for UserManagementUserGroup.

    For users on our New Relic One user model, a "group" represents a
    group of users. Putting users in a group allows the managing of
    permissions for multiple users at the same time.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_name", "id")
    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )


class UserManagementUserGroups(sgqlc.types.Type):
    """Class for UserManagementUserGroups.

    container for groups enabling cursor based pagination.
    """

    __schema__ = nerdgraph
    __field_names__ = ("groups", "next_cursor", "total_count")
    groups = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(UserManagementUserGroup))
        ),
        graphql_name="groups",
    )


class UserManagementUserType(sgqlc.types.Type):
    """Class for UserManagementUserType.

    A "user type" is what determines the set of New Relic capabilities
    a user can theoretically access.
    """

    __schema__ = nerdgraph
    __field_names__ = ("display_name", "id")
    display_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="displayName"
    )


class UserManagementUsers(sgqlc.types.Type):
    """Class for UserManagementUsers.

    container for users enabling cursor based pagination.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "total_count", "users")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class UserReference(sgqlc.types.Type):
    """Class for UserReference.

    The `UserReference` object provides basic identifying information
    about the user.
    """

    __schema__ = nerdgraph
    __field_names__ = ("email", "gravatar", "id", "name")
    email = sgqlc.types.Field(String, graphql_name="email")

    gravatar = sgqlc.types.Field(String, graphql_name="gravatar")

    id = sgqlc.types.Field(Int, graphql_name="id")

    name = sgqlc.types.Field(String, graphql_name="name")


class UsersActorStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("user_search",)
    user_search = sgqlc.types.Field(
        "UsersUserSearchResult",
        graphql_name="userSearch",
        args=sgqlc.types.ArgDict(
            (
                (
                    "cursor",
                    sgqlc.types.Arg(String, graphql_name="cursor", default=None),
                ),
                (
                    "query",
                    sgqlc.types.Arg(
                        UsersUserSearchQuery, graphql_name="query", default=None
                    ),
                ),
            )
        ),
    )


class UsersUserSearch(sgqlc.types.Type):
    """Class for UsersUserSearch.

    User information returned for UserSearch.
    """

    __schema__ = nerdgraph
    __field_names__ = ("email", "name", "user_id")
    email = sgqlc.types.Field(String, graphql_name="email")


class UsersUserSearchResult(sgqlc.types.Type):
    """Class for UsersUserSearchResult.

    The result object for UserSearch.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "total_count", "users")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class WhatsNewDocsStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ("announcement", "news_search")
    announcement = sgqlc.types.Field(
        "WhatsNewAnnouncementContent",
        graphql_name="announcement",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )


class WhatsNewSearchResult(sgqlc.types.Type):
    """Class for WhatsNewSearchResult.

    Represents the resulting details from a search of news.
    """

    __schema__ = nerdgraph
    __field_names__ = ("next_cursor", "results", "total_count")
    next_cursor = sgqlc.types.Field(String, graphql_name="nextCursor")


class WorkloadAccountStitchedFields(sgqlc.types.Type):
    __schema__ = nerdgraph
    __field_names__ = ()


class WorkloadAutomaticStatus(sgqlc.types.Type):
    """Class for WorkloadAutomaticStatus.

    The automatic status configuration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("enabled", "remaining_entities_rule", "rules")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")


class WorkloadCollection(sgqlc.types.Type):
    """Class for WorkloadCollection.

    A user defined group of entities.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account",
        "created_at",
        "created_by",
        "description",
        "entities",
        "entity_search_queries",
        "entity_search_query",
        "guid",
        "id",
        "name",
        "permalink",
        "scope_accounts",
        "status",
        "status_config",
        "updated_at",
        "updated_by",
    )
    account = sgqlc.types.Field(
        sgqlc.types.non_null(AccountReference), graphql_name="account"
    )


class WorkloadCollectionWithoutStatus(sgqlc.types.Type):
    """Class for WorkloadCollectionWithoutStatus.

    A user defined group of entities without Status.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "account",
        "created_at",
        "created_by",
        "description",
        "entities",
        "entity_search_queries",
        "entity_search_query",
        "guid",
        "id",
        "name",
        "permalink",
        "scope_accounts",
        "status_config",
        "updated_at",
        "updated_by",
    )
    account = sgqlc.types.Field(
        sgqlc.types.non_null(AccountReference), graphql_name="account"
    )


class WorkloadEntityRef(sgqlc.types.Type):
    """Class for WorkloadEntityRef.

    A reference to a New Relic entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ("guid",)
    guid = sgqlc.types.Field(EntityGuid, graphql_name="guid")


class WorkloadEntitySearchQuery(sgqlc.types.Type):
    """Class for WorkloadEntitySearchQuery.

    An entity search query used to dynamically retrieve a group of
    entities.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_at", "created_by", "id", "query", "updated_at")
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(EpochMilliseconds), graphql_name="createdAt"
    )


class WorkloadRegularRule(sgqlc.types.Type):
    """Class for WorkloadRegularRule.

    The definition of a rule, which consists of a group of entities
    and a rollup strategy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entities", "entity_search_queries", "id", "rollup")
    entities = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(WorkloadEntityRef)),
        graphql_name="entities",
    )


class WorkloadRemainingEntitiesRule(sgqlc.types.Type):
    """Class for WorkloadRemainingEntitiesRule.

    The definition of a remaining entities rule.
    """

    __schema__ = nerdgraph
    __field_names__ = ("rollup",)
    rollup = sgqlc.types.Field(
        sgqlc.types.non_null("WorkloadRemainingEntitiesRuleRollup"),
        graphql_name="rollup",
    )


class WorkloadRemainingEntitiesRuleRollup(sgqlc.types.Type):
    """Class for WorkloadRemainingEntitiesRuleRollup.

    The rollup strategy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("group_by", "strategy", "threshold_type", "threshold_value")
    group_by = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadGroupRemainingEntitiesRuleBy),
        graphql_name="groupBy",
    )


class WorkloadRollup(sgqlc.types.Type):
    """Class for WorkloadRollup.

    The rollup strategy.
    """

    __schema__ = nerdgraph
    __field_names__ = ("strategy", "threshold_type", "threshold_value")
    strategy = sgqlc.types.Field(
        sgqlc.types.non_null(WorkloadRollupStrategy), graphql_name="strategy"
    )


class WorkloadRollupRuleDetails(sgqlc.types.Type):
    """Class for WorkloadRollupRuleDetails.

    Represents the details of a rollup rule.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "entity_search_queries",
        "has_individual_entities",
        "not_operational_entities",
        "operational_entities",
        "resulting_group_type",
        "threshold_type",
        "unknown_status_entities",
    )
    entity_search_queries = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="entitySearchQueries",
    )


class WorkloadScopeAccounts(sgqlc.types.Type):
    """Class for WorkloadScopeAccounts.

    Accounts that will be used to get entities from.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_ids",)
    account_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="accountIds",
    )


class WorkloadStaticStatus(sgqlc.types.Type):
    """Class for WorkloadStaticStatus.

    The static status configuration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "enabled", "id", "status", "summary")
    description = sgqlc.types.Field(String, graphql_name="description")


class WorkloadStatus(sgqlc.types.Type):
    """Class for WorkloadStatus.

    Detailed information about the status of a workload.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "status_source", "status_value", "summary")
    description = sgqlc.types.Field(String, graphql_name="description")


class WorkloadStatusConfig(sgqlc.types.Type):
    """Class for WorkloadStatusConfig.

    The configuration that defines how the status of the workload is
    calculated.
    """

    __schema__ = nerdgraph
    __field_names__ = ("automatic", "static")
    automatic = sgqlc.types.Field(WorkloadAutomaticStatus, graphql_name="automatic")


class WorkloadValidAccounts(sgqlc.types.Type):
    """Class for WorkloadValidAccounts.

    All the accounts that user has access to, from the same
    organization.
    """

    __schema__ = nerdgraph
    __field_names__ = ("accounts",)
    accounts = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AccountReference)),
        graphql_name="accounts",
    )


class WorkloadWorkloadStatus(sgqlc.types.Type):
    """Class for WorkloadWorkloadStatus.

    Status of the workload.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "source", "status_details", "summary", "value")
    description = sgqlc.types.Field(String, graphql_name="description")


class AiIssuesAnomalyIncident(sgqlc.types.Type, AiIssuesIIncident):
    """Class for AiIssuesAnomalyIncident.

    Anomaly incident.
    """

    __schema__ = nerdgraph
    __field_names__ = ("anomaly_id",)
    anomaly_id = sgqlc.types.Field(String, graphql_name="anomalyId")


class AiIssuesNewRelicIncident(sgqlc.types.Type, AiIssuesIIncident):
    """Class for AiIssuesNewRelicIncident.

    Newrelic incident.
    """

    __schema__ = nerdgraph
    __field_names__ = ("condition_family_id", "policy_ids")
    condition_family_id = sgqlc.types.Field(String, graphql_name="conditionFamilyId")


class AiIssuesRestIncident(sgqlc.types.Type, AiIssuesIIncident):
    """Class for AiIssuesRestIncident.

    Rest incident.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aggregation_tags",)
    aggregation_tags = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AiIssuesKeyValue)),
        graphql_name="aggregationTags",
    )


class AiWorkflowsCreateResponseError(sgqlc.types.Type, AiWorkflowsResponseError):
    """Class for AiWorkflowsCreateResponseError.

    Create error description.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiWorkflowsCreateErrorType), graphql_name="type"
    )


class AiWorkflowsDeleteResponseError(sgqlc.types.Type, AiWorkflowsResponseError):
    """Class for AiWorkflowsDeleteResponseError.

    Delete error description.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiWorkflowsDeleteErrorType), graphql_name="type"
    )


class AiWorkflowsTestResponseError(sgqlc.types.Type, AiWorkflowsResponseError):
    """Class for AiWorkflowsTestResponseError.

    Test error description.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiWorkflowsTestErrorType), graphql_name="type"
    )


class AiWorkflowsUpdateResponseError(sgqlc.types.Type, AiWorkflowsResponseError):
    """Class for AiWorkflowsUpdateResponseError.

    Update error description.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(
        sgqlc.types.non_null(AiWorkflowsUpdateErrorType), graphql_name="type"
    )


class AlertsCampfireNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsCampfireNotificationChannel.

    Campfire notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class AlertsEmailNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsEmailNotificationChannel.

    Email notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("config",)
    config = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsEmailNotificationChannelConfig),
        graphql_name="config",
    )


class AlertsHipChatNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsHipChatNotificationChannel.

    HipChat notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class AlertsNrqlBaselineCondition(sgqlc.types.Type, AlertsNrqlCondition):
    """Class for AlertsNrqlBaselineCondition.

    A baseline NRQL condition is a self-adjusting condition based on
    the past behavior of a monitored NRQL query.
    """

    __schema__ = nerdgraph
    __field_names__ = ("baseline_direction",)
    baseline_direction = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsNrqlBaselineDirection),
        graphql_name="baselineDirection",
    )


class AlertsNrqlOutlierCondition(sgqlc.types.Type, AlertsNrqlCondition):
    """Class for AlertsNrqlOutlierCondition.

    An outlier NRQL condition looks for group behavior and values that
    are outliers from those groups. Similar to a static NRQL
    condition, but requires a FACET clause.
    """

    __schema__ = nerdgraph
    __field_names__ = ("expected_groups", "open_violation_on_group_overlap")
    expected_groups = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="expectedGroups"
    )


class AlertsNrqlStaticCondition(sgqlc.types.Type, AlertsNrqlCondition):
    """Class for AlertsNrqlStaticCondition.

    A static NRQL condition is the simplest type of NRQL threshold. It
    allows you to create a condition based on a NRQL query that
    returns a numeric value.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class AlertsOpsGenieNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsOpsGenieNotificationChannel.

    OpsGenie notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("config",)
    config = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsOpsGenieNotificationChannelConfig),
        graphql_name="config",
    )


class AlertsPagerDutyNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsPagerDutyNotificationChannel.

    PagerDuty notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("config",)
    config = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsPagerDutyNotificationChannelConfig),
        graphql_name="config",
    )


class AlertsSlackNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsSlackNotificationChannel.

    Slack notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("config",)
    config = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsSlackNotificationChannelConfig),
        graphql_name="config",
    )


class AlertsUserNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsUserNotificationChannel.

    User notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class AlertsVictorOpsNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsVictorOpsNotificationChannel.

    VictorOps notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("config",)
    config = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsVictorOpsNotificationChannelConfig),
        graphql_name="config",
    )


class AlertsWebhookNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsWebhookNotificationChannel.

    Webhook notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("config",)
    config = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsWebhookNotificationChannelConfig),
        graphql_name="config",
    )


class AlertsXMattersNotificationChannel(sgqlc.types.Type, AlertsNotificationChannel):
    """Class for AlertsXMattersNotificationChannel.

    xMatters notification channel.
    """

    __schema__ = nerdgraph
    __field_names__ = ("config",)
    config = sgqlc.types.Field(
        sgqlc.types.non_null(AlertsXMattersNotificationChannelConfig),
        graphql_name="config",
    )


class ApiAccessIngestKey(sgqlc.types.Type, ApiAccessKey):
    """Class for ApiAccessIngestKey.

    An ingest key.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account", "account_id", "ingest_type")
    account = sgqlc.types.Field(AccountReference, graphql_name="account")


class ApiAccessIngestKeyError(sgqlc.types.Type, ApiAccessKeyError):
    """Class for ApiAccessIngestKeyError.

    An ingest key error. Each error maps to a single key input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "error_type", "id", "ingest_type")
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class ApiAccessUserKey(sgqlc.types.Type, ApiAccessKey):
    """Class for ApiAccessUserKey.

    A user key.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account", "account_id", "user", "user_id")
    account = sgqlc.types.Field(AccountReference, graphql_name="account")


class ApiAccessUserKeyError(sgqlc.types.Type, ApiAccessKeyError):
    """Class for ApiAccessUserKeyError.

    A user key error. Each error maps to a single key input.
    """

    __schema__ = nerdgraph
    __field_names__ = ("account_id", "error_type", "id", "user_id")
    account_id = sgqlc.types.Field(Int, graphql_name="accountId")


class ApmApplicationEntity(
    sgqlc.types.Type, AlertableEntity, ApmBrowserApplicationEntity, Entity
):
    """Class for ApmApplicationEntity.

    An APM Application entity.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apm_settings",
        "apm_summary",
        "application_id",
        "application_instances",
        "application_instances_v2",
        "deployments",
        "exception",
        "flamegraph",
        "language",
        "metric_grouping_issues",
        "metric_normalization_rule",
        "metric_normalization_rules",
        "running_agent_versions",
        "settings",
    )
    apm_settings = sgqlc.types.Field(
        AgentApplicationSettingsApmBase, graphql_name="apmSettings"
    )


class ApmApplicationEntityOutline(
    sgqlc.types.Type,
    AlertableEntityOutline,
    ApmBrowserApplicationEntityOutline,
    EntityOutline,
):
    """Class for ApmApplicationEntityOutline.

    An APM Application entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apm_summary",
        "application_id",
        "language",
        "running_agent_versions",
        "settings",
    )
    apm_summary = sgqlc.types.Field(
        ApmApplicationSummaryData, graphql_name="apmSummary"
    )


class ApmDatabaseInstanceEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for ApmDatabaseInstanceEntity.

    A database instance seen by an APM Application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("host", "port_or_path", "vendor")
    host = sgqlc.types.Field(String, graphql_name="host")


class ApmDatabaseInstanceEntityOutline(
    sgqlc.types.Type, AlertableEntityOutline, EntityOutline
):
    """Class for ApmDatabaseInstanceEntityOutline.

    A database instance seen by an APM Application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("host", "port_or_path", "vendor")
    host = sgqlc.types.Field(String, graphql_name="host")


class ApmExternalServiceEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for ApmExternalServiceEntity.

    An external service seen by an APM Application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("host",)
    host = sgqlc.types.Field(String, graphql_name="host")


class ApmExternalServiceEntityOutline(
    sgqlc.types.Type, AlertableEntityOutline, EntityOutline
):
    """Class for ApmExternalServiceEntityOutline.

    An external service seen by an APM Application.
    """

    __schema__ = nerdgraph
    __field_names__ = ("host",)
    host = sgqlc.types.Field(String, graphql_name="host")


class BrowserApplicationEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for BrowserApplicationEntity.

    A Browser Application entity.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "agent_install_type",
        "application_id",
        "browser_properties",
        "browser_settings",
        "browser_summary",
        "exception",
        "metric_grouping_issues",
        "metric_normalization_rule",
        "metric_normalization_rules",
        "running_agent_versions",
        "serving_apm_application_id",
        "settings",
    )
    agent_install_type = sgqlc.types.Field(
        BrowserAgentInstallType, graphql_name="agentInstallType"
    )


class BrowserApplicationEntityOutline(
    sgqlc.types.Type, AlertableEntityOutline, EntityOutline
):
    """Class for BrowserApplicationEntityOutline.

    A Browser Application entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "agent_install_type",
        "application_id",
        "browser_summary",
        "running_agent_versions",
        "serving_apm_application_id",
        "settings",
    )
    agent_install_type = sgqlc.types.Field(
        BrowserAgentInstallType, graphql_name="agentInstallType"
    )


class CloudAlbIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAlbIntegration.

    ALB/NLB Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "load_balancer_prefixes",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudApigatewayIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudApigatewayIntegration.

    API Gateway Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "metrics_polling_interval",
        "stage_prefixes",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAutoscalingIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAutoscalingIntegration.

    AutoScaling Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsAppsyncIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsAppsyncIntegration.

    AppSync Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsAthenaIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsAthenaIntegration.

    Athena Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsCognitoIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsCognitoIntegration.

    Cognito Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsConnectIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsConnectIntegration.

    Connect Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsDirectconnectIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsDirectconnectIntegration.

    Direct Connect Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsDocdbIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsDocdbIntegration.

    DocumentDB Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsFsxIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsFsxIntegration.

    FSx Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsGlueIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsGlueIntegration.

    Glue Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsGovCloudProvider(sgqlc.types.Type, CloudProvider):
    """Class for CloudAwsGovCloudProvider.

    The Amazon Web Services cloud provider (GovCloud).
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_account_id",)
    aws_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="awsAccountId"
    )


class CloudAwsKinesisanalyticsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsKinesisanalyticsIntegration.

    Kinesis Data Analytics Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsMediaconvertIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsMediaconvertIntegration.

    Elemental MediaConvert Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsMediapackagevodIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsMediapackagevodIntegration.

    MediaPackage VOD Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsMetadataIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsMetadataIntegration.

    Fetch Metadata for AWS integrations Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsMqIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsMqIntegration.

    MQ Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsMskIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsMskIntegration.

    Managed Kafka Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsNeptuneIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsNeptuneIntegration.

    Neptune Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsProvider(sgqlc.types.Type, CloudProvider):
    """Class for CloudAwsProvider.

    The Amazon Web Services cloud provider.
    """

    __schema__ = nerdgraph
    __field_names__ = ("role_account_id", "role_external_id")
    role_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="roleAccountId"
    )


class CloudAwsQldbIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsQldbIntegration.

    QLDB Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsRoute53resolverIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsRoute53resolverIntegration.

    Route53 Resolver Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsStatesIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsStatesIntegration.

    Step Functions Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsTagsGlobalIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsTagsGlobalIntegration.

    Fetch tags for all integrations Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAwsTransitgatewayIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsTransitgatewayIntegration.

    Transit Gateway Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsWafIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsWafIntegration.

    WAF Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsWafv2Integration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsWafv2Integration.

    WAFV2 Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAwsXrayIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAwsXrayIntegration.

    X-Ray Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudAzureApimanagementIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureApimanagementIntegration.

    Api Management Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureAppgatewayIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureAppgatewayIntegration.

    App Gateway Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureAppserviceIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureAppserviceIntegration.

    App Service Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureContainersIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureContainersIntegration.

    Containers Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureCosmosdbIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureCosmosdbIntegration.

    Cosmos DB Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureCostmanagementIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureCostmanagementIntegration.

    Cost Management Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "tag_keys")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureDatafactoryIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureDatafactoryIntegration.

    Data Factory Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureEventhubIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureEventhubIntegration.

    Event Hub Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureExpressrouteIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureExpressrouteIntegration.

    Express Route Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureFirewallsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureFirewallsIntegration.

    Firewalls Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureFrontdoorIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureFrontdoorIntegration.

    Front Door Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureFunctionsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureFunctionsIntegration.

    Functions Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureKeyvaultIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureKeyvaultIntegration.

    Key Vault Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureLoadbalancerIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureLoadbalancerIntegration.

    Load Balancer Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureLogicappsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureLogicappsIntegration.

    Logic Apps Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureMachinelearningIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureMachinelearningIntegration.

    Machine Learning Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureMariadbIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureMariadbIntegration.

    Database for MariaDB Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureMonitorIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureMonitorIntegration.

    Azure Monitor metrics Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "enabled",
        "exclude_tags",
        "include_tags",
        "inventory_polling_interval",
        "metrics_polling_interval",
        "resource_groups",
        "resource_types",
    )
    enabled = sgqlc.types.Field(Boolean, graphql_name="enabled")


class CloudAzureMysqlIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureMysqlIntegration.

    Database for MySQL Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureMysqlflexibleIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureMysqlflexibleIntegration.

    MySQL Flexible Server Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzurePostgresqlIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzurePostgresqlIntegration.

    Database for PostgreSQL Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzurePostgresqlflexibleIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzurePostgresqlflexibleIntegration.

    PostgreSQL Flexible Server Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzurePowerbidedicatedIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzurePowerbidedicatedIntegration.

    Power BI Dedicated Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureRediscacheIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureRediscacheIntegration.

    Redis Cache Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureServicebusIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureServicebusIntegration.

    Service Bus Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureSqlIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureSqlIntegration.

    SQL Database Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureSqlmanagedIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureSqlmanagedIntegration.

    SQL Managed Instances Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureStorageIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureStorageIntegration.

    Storage Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureVirtualmachineIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureVirtualmachineIntegration.

    Virtual machine scale sets Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureVirtualnetworksIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureVirtualnetworksIntegration.

    Virtual Network Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureVmsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureVmsIntegration.

    Virtual Machines Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudAzureVpngatewaysIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudAzureVpngatewaysIntegration.

    VPN Gateways Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "resource_groups")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudBaseIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudBaseIntegration.

    Base Integration Object.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class CloudBaseProvider(sgqlc.types.Type, CloudProvider):
    """Class for CloudBaseProvider.

    Base Provider Object.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class CloudBillingIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudBillingIntegration.

    Billing Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudCloudfrontIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudCloudfrontIntegration.

    CloudFront Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_lambdas_at_edge",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    fetch_lambdas_at_edge = sgqlc.types.Field(
        Boolean, graphql_name="fetchLambdasAtEdge"
    )


class CloudCloudtrailIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudCloudtrailIntegration.

    CloudTrail Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudDynamodbIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudDynamodbIntegration.

    DynamoDB Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEbsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudEbsIntegration.

    EBS Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEc2Integration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudEc2Integration.

    EC2 Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "duplicate_ec2_tags",
        "fetch_ip_addresses",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEcsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudEcsIntegration.

    ECS Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEfsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudEfsIntegration.

    EFS Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudElasticacheIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudElasticacheIntegration.

    ElastiCache Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudElasticbeanstalkIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudElasticbeanstalkIntegration.

    Elastic Beanstalk Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudElasticsearchIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudElasticsearchIntegration.

    Elasticsearch Service Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_nodes",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudElbIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudElbIntegration.

    ELB (Classic) Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudEmrIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudEmrIntegration.

    EMR Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudGcpAlloydbIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpAlloydbIntegration.

    AlloyDB Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpAppengineIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpAppengineIntegration.

    App Engine Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpBigqueryIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpBigqueryIntegration.

    BigQuery Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("fetch_table_metrics", "fetch_tags", "metrics_polling_interval")
    fetch_table_metrics = sgqlc.types.Field(Boolean, graphql_name="fetchTableMetrics")


class CloudGcpBigtableIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpBigtableIntegration.

    Bigtable Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpComposerIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpComposerIntegration.

    Composer Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpDataflowIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpDataflowIntegration.

    Dataflow Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpDataprocIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpDataprocIntegration.

    Dataproc Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpDatastoreIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpDatastoreIntegration.

    Datastore Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpFirebasedatabaseIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpFirebasedatabaseIntegration.

    Firebase Database Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpFirebasehostingIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpFirebasehostingIntegration.

    Firebase Hosting Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpFirebasestorageIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpFirebasestorageIntegration.

    Firebase Storage Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpFirestoreIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpFirestoreIntegration.

    Firestore Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpFunctionsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpFunctionsIntegration.

    Cloud Functions Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpInterconnectIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpInterconnectIntegration.

    Interconnect Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpKubernetesIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpKubernetesIntegration.

    Kubernetes Engine Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpLoadbalancingIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpLoadbalancingIntegration.

    Cloud Load Balancing Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpMemcacheIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpMemcacheIntegration.

    Memcache Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpProvider(sgqlc.types.Type, CloudProvider):
    """Class for CloudGcpProvider.

    The Google Cloud Platform cloud provider.
    """

    __schema__ = nerdgraph
    __field_names__ = ("service_account_id",)
    service_account_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="serviceAccountId"
    )


class CloudGcpPubsubIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpPubsubIntegration.

    Cloud Pub/Sub Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("fetch_tags", "metrics_polling_interval")
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")


class CloudGcpRedisIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpRedisIntegration.

    Redis Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpRouterIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpRouterIntegration.

    Router Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpRunIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpRunIntegration.

    Run Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpSpannerIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpSpannerIntegration.

    Cloud Spanner Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("fetch_tags", "metrics_polling_interval")
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")


class CloudGcpSqlIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpSqlIntegration.

    Cloud SQL Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpStorageIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpStorageIntegration.

    Cloud Storage Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("fetch_tags", "metrics_polling_interval")
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name="fetchTags")


class CloudGcpVmsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpVmsIntegration.

    Compute Engine Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudGcpVpcaccessIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudGcpVpcaccessIntegration.

    VPC Access Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudHealthIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudHealthIntegration.

    Health Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudIamIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudIamIntegration.

    IAM Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval", "tag_key", "tag_value")
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudIotIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudIotIntegration.

    IoT Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudKinesisFirehoseIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudKinesisFirehoseIntegration.

    Kinesis Firehose Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudKinesisIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudKinesisIntegration.

    Kinesis Streams Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_shards",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudLambdaIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudLambdaIntegration.

    Lambda Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudRdsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudRdsIntegration.

    RDS Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudRedshiftIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudRedshiftIntegration.

    Redshift Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudRoute53Integration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudRoute53Integration.

    Route 53 Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("fetch_extended_inventory", "metrics_polling_interval")
    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )


class CloudS3Integration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudS3Integration.

    S3 Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "fetch_extended_inventory",
        "fetch_tags",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    fetch_extended_inventory = sgqlc.types.Field(
        Boolean, graphql_name="fetchExtendedInventory"
    )


class CloudSesIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudSesIntegration.

    SES Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("aws_regions", "metrics_polling_interval")
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudSnsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudSnsIntegration.

    SNS Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "metrics_polling_interval",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudSqsIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudSqsIntegration.

    SQS Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_extended_inventory",
        "fetch_tags",
        "metrics_polling_interval",
        "queue_prefixes",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class CloudTrustedadvisorIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudTrustedadvisorIntegration.

    Trusted Advisor Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = ("metrics_polling_interval",)
    metrics_polling_interval = sgqlc.types.Field(
        Int, graphql_name="metricsPollingInterval"
    )


class CloudVpcIntegration(sgqlc.types.Type, CloudIntegration):
    """Class for CloudVpcIntegration.

    VPC Integration.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "aws_regions",
        "fetch_nat_gateway",
        "fetch_vpn",
        "metrics_polling_interval",
        "tag_key",
        "tag_value",
    )
    aws_regions = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="awsRegions"
    )


class DashboardEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for DashboardEntity.

    A Dashboard entity.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "dashboard_parent_guid",
        "description",
        "owner",
        "pages",
        "permissions",
        "updated_at",
        "variables",
    )
    created_at = sgqlc.types.Field(DateTime, graphql_name="createdAt")


class DashboardEntityOutline(sgqlc.types.Type, AlertableEntityOutline, EntityOutline):
    """Class for DashboardEntityOutline.

    A Dashboard entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "created_at",
        "dashboard_parent_guid",
        "owner",
        "permissions",
        "updated_at",
    )
    created_at = sgqlc.types.Field(DateTime, graphql_name="createdAt")


class EdgeAgentEndpointDetail(sgqlc.types.Type, EdgeEndpointDetail):
    """Class for EdgeAgentEndpointDetail.

    All the details necessary to configure an agent to connect to an
    endoint.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class EdgeHttpsEndpointDetail(sgqlc.types.Type, EdgeEndpointDetail):
    """Class for EdgeHttpsEndpointDetail.

    All the details necessary to configure an integration to connect
    to the Infinite Tracing Trace API (HTTP 1.1) endpoint.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class EntityRelationshipDetectedEdge(sgqlc.types.Type, EntityRelationshipEdge):
    """Class for EntityRelationshipDetectedEdge.

    An entity relationship automatically detected by NewRelic.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class EntityRelationshipUserDefinedEdge(sgqlc.types.Type, EntityRelationshipEdge):
    """Class for EntityRelationshipUserDefinedEdge.

    An entity user-defined relationship.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_by_user",)
    created_by_user = sgqlc.types.Field(UserReference, graphql_name="createdByUser")


class ErrorsInboxAssignErrorGroupError(sgqlc.types.Type, ErrorsInboxResponseError):
    """Class for ErrorsInboxAssignErrorGroupError.

    Assign error group error.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(
        sgqlc.types.non_null(ErrorsInboxAssignErrorGroupErrorType), graphql_name="type"
    )


class ErrorsInboxJiraIssue(sgqlc.types.Type, ErrorsInboxResource):
    """Class for ErrorsInboxJiraIssue.

    An single issue in JIRA.
    """

    __schema__ = nerdgraph
    __field_names__ = ("issue_id",)
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="issueId")


class ErrorsInboxUpdateErrorGroupStateError(sgqlc.types.Type, ErrorsInboxResponseError):
    """Class for ErrorsInboxUpdateErrorGroupStateError.

    Configure notification policy error.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(
        sgqlc.types.non_null(ErrorsInboxUpdateErrorGroupStateErrorType),
        graphql_name="type",
    )


class ExternalEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for ExternalEntity.

    An External entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class ExternalEntityOutline(sgqlc.types.Type, AlertableEntityOutline, EntityOutline):
    """Class for ExternalEntityOutline.

    An External entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class GenericEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for GenericEntity.

    A generic entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class GenericEntityOutline(sgqlc.types.Type, AlertableEntityOutline, EntityOutline):
    """Class for GenericEntityOutline.

    A generic entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class GenericInfrastructureEntity(
    sgqlc.types.Type, AlertableEntity, Entity, InfrastructureIntegrationEntity
):
    """Class for GenericInfrastructureEntity.

    An Infrastructure entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class GenericInfrastructureEntityOutline(
    sgqlc.types.Type,
    AlertableEntityOutline,
    EntityOutline,
    InfrastructureIntegrationEntityOutline,
):
    """Class for GenericInfrastructureEntityOutline.

    An Infrastructure entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class InfrastructureAwsLambdaFunctionEntity(
    sgqlc.types.Type, AlertableEntity, Entity, InfrastructureIntegrationEntity
):
    """Class for InfrastructureAwsLambdaFunctionEntity.

    An AWS Lambda Function entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ("runtime",)
    runtime = sgqlc.types.Field(String, graphql_name="runtime")


class InfrastructureAwsLambdaFunctionEntityOutline(
    sgqlc.types.Type,
    AlertableEntityOutline,
    EntityOutline,
    InfrastructureIntegrationEntityOutline,
):
    """Class for InfrastructureAwsLambdaFunctionEntityOutline.

    An AWS Lambda Function entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = ("runtime",)
    runtime = sgqlc.types.Field(String, graphql_name="runtime")


class InfrastructureHostEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for InfrastructureHostEntity.

    An Infrastructure Host entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ("host_summary",)
    host_summary = sgqlc.types.Field(
        InfrastructureHostSummaryData, graphql_name="hostSummary"
    )


class InfrastructureHostEntityOutline(
    sgqlc.types.Type, AlertableEntityOutline, EntityOutline
):
    """Class for InfrastructureHostEntityOutline.

    An Infrastructure Host entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = ("host_summary",)
    host_summary = sgqlc.types.Field(
        InfrastructureHostSummaryData, graphql_name="hostSummary"
    )


class KeyTransactionEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for KeyTransactionEntity.

    A Key Transaction entity.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "apdex_target",
        "application",
        "browser_apdex_target",
        "metric_name",
    )
    apdex_target = sgqlc.types.Field(
        sgqlc.types.non_null(Float), graphql_name="apdexTarget"
    )


class KeyTransactionEntityOutline(
    sgqlc.types.Type, AlertableEntityOutline, EntityOutline
):
    """Class for KeyTransactionEntityOutline.

    A Key Transaction entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class MobileApplicationEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for MobileApplicationEntity.

    A Mobile Application entity.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "application_id",
        "crash",
        "exception",
        "metric_grouping_issues",
        "metric_normalization_rule",
        "metric_normalization_rules",
        "mobile_properties",
        "mobile_settings",
        "mobile_summary",
    )
    application_id = sgqlc.types.Field(Int, graphql_name="applicationId")


class MobileApplicationEntityOutline(
    sgqlc.types.Type, AlertableEntityOutline, EntityOutline
):
    """Class for MobileApplicationEntityOutline.

    A Mobile Application entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = ("application_id", "mobile_summary")
    application_id = sgqlc.types.Field(Int, graphql_name="applicationId")


class Nr1CatalogAllSupportedEntityTypes(
    sgqlc.types.Type, Nr1CatalogSupportedEntityTypes
):
    """Class for Nr1CatalogAllSupportedEntityTypes.

    Specifies the supported entity types to be all entity types.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogInstallPlan(sgqlc.types.Type, Nr1CatalogInstaller):
    """Class for Nr1CatalogInstallPlan.

    An installer that uses install plan steps.
    """

    __schema__ = nerdgraph
    __field_names__ = ("steps",)
    steps = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogInstallPlanStep))
        ),
        graphql_name="steps",
    )


class Nr1CatalogLauncher(sgqlc.types.Type, Nr1CatalogNerdpackItem):
    """Class for Nr1CatalogLauncher.

    Information about a launcher in a Nerdpack.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogLauncherMetadata(sgqlc.types.Type, Nr1CatalogNerdpackItemMetadata):
    """Class for Nr1CatalogLauncherMetadata.

    Metadata information for a launcher.
    """

    __schema__ = nerdgraph
    __field_names__ = ("icon",)
    icon = sgqlc.types.Field(Nr1CatalogIcon, graphql_name="icon")


class Nr1CatalogLinkInstallPlanDirective(
    sgqlc.types.Type, Nr1CatalogInstallPlanDirective
):
    """Class for Nr1CatalogLinkInstallPlanDirective.

    Information about a link install plan directive.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogNerdlet(sgqlc.types.Type, Nr1CatalogNerdpackItem):
    """Class for Nr1CatalogNerdlet.

    Information about a Nerdlet in a Nerdpack.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogNerdletInstallPlanDirective(
    sgqlc.types.Type, Nr1CatalogInstallPlanDirective
):
    """Class for Nr1CatalogNerdletInstallPlanDirective.

    Information about a targeted install plan directive.
    """

    __schema__ = nerdgraph
    __field_names__ = ("nerdlet_id", "nerdlet_state")
    nerdlet_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="nerdletId")


class Nr1CatalogNerdletMetadata(sgqlc.types.Type, Nr1CatalogNerdpackItemMetadata):
    """Class for Nr1CatalogNerdletMetadata.

    Metadata information for a Nerdlet.
    """

    __schema__ = nerdgraph
    __field_names__ = ("supported_entity_types",)
    supported_entity_types = sgqlc.types.Field(
        Nr1CatalogSupportedEntityTypes, graphql_name="supportedEntityTypes"
    )


class Nr1CatalogNoSupportedEntityTypes(
    sgqlc.types.Type, Nr1CatalogSupportedEntityTypes
):
    """Class for Nr1CatalogNoSupportedEntityTypes.

    Specifies the supported entity types to be no entity types.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogQuickstartAlert(sgqlc.types.Type, Nr1CatalogQuickstartComponent):
    """Class for Nr1CatalogQuickstartAlert.

    Information about an alert in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogQuickstartAlertCondition(
    sgqlc.types.Type, Nr1CatalogQuickstartComponent
):
    """Class for Nr1CatalogQuickstartAlertCondition.

    Information about an alert condition in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class Nr1CatalogQuickstartAlertConditionMetadata(
    sgqlc.types.Type, Nr1CatalogQuickstartComponentMetadata
):
    """Class for Nr1CatalogQuickstartAlertConditionMetadata.

    Metadata associated with the alert condition in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ("type",)
    type = sgqlc.types.Field(
        sgqlc.types.non_null(Nr1CatalogQuickstartAlertConditionType),
        graphql_name="type",
    )


class Nr1CatalogQuickstartAlertMetadata(
    sgqlc.types.Type, Nr1CatalogQuickstartComponentMetadata
):
    """Class for Nr1CatalogQuickstartAlertMetadata.

    Metadata associated with the alert in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogQuickstartDashboard(sgqlc.types.Type, Nr1CatalogQuickstartComponent):
    """Class for Nr1CatalogQuickstartDashboard.

    Information about a dashboard in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ("id",)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")


class Nr1CatalogQuickstartDashboardMetadata(
    sgqlc.types.Type, Nr1CatalogQuickstartComponentMetadata
):
    """Class for Nr1CatalogQuickstartDashboardMetadata.

    Metadata associated with the dashboard in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ("previews",)
    previews = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(Nr1CatalogPreview))
        ),
        graphql_name="previews",
    )


class Nr1CatalogQuickstartDocumentation(
    sgqlc.types.Type, Nr1CatalogQuickstartComponent
):
    """Class for Nr1CatalogQuickstartDocumentation.

    Information about a documentation component in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogQuickstartDocumentationMetadata(
    sgqlc.types.Type, Nr1CatalogQuickstartComponentMetadata
):
    """Class for Nr1CatalogQuickstartDocumentationMetadata.

    Metadata associated with the documentation component in a
    quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ("url",)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="url")


class Nr1CatalogQuickstartInstallPlan(sgqlc.types.Type, Nr1CatalogQuickstartComponent):
    """Class for Nr1CatalogQuickstartInstallPlan.

    Information about an install plan component in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogQuickstartInstallPlanMetadata(
    sgqlc.types.Type, Nr1CatalogQuickstartComponentMetadata
):
    """Class for Nr1CatalogQuickstartInstallPlanMetadata.

    Metadata associated with the install plan in a quickstart.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogScreenshot(sgqlc.types.Type, Nr1CatalogPreview):
    """Class for Nr1CatalogScreenshot.

    Information about the publicly accessible screenshot.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogSpecificSupportedEntityTypes(
    sgqlc.types.Type, Nr1CatalogSupportedEntityTypes
):
    """Class for Nr1CatalogSpecificSupportedEntityTypes.

    Specifies the supported entity types to be a specific subset of
    entity types.
    """

    __schema__ = nerdgraph
    __field_names__ = ("entity_types",)
    entity_types = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DomainType))),
        graphql_name="entityTypes",
    )


class Nr1CatalogTargetedInstallPlanDirective(
    sgqlc.types.Type, Nr1CatalogInstallPlanDirective
):
    """Class for Nr1CatalogTargetedInstallPlanDirective.

    Information about a targeted install plan directive.
    """

    __schema__ = nerdgraph
    __field_names__ = ("recipe_name",)
    recipe_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="recipeName"
    )


class Nr1CatalogVisualization(sgqlc.types.Type, Nr1CatalogNerdpackItem):
    """Class for Nr1CatalogVisualization.

    Information about a visualization in a Nerdpack.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class Nr1CatalogVisualizationMetadata(sgqlc.types.Type, Nr1CatalogNerdpackItemMetadata):
    """Class for Nr1CatalogVisualizationMetadata.

    Metadata information for a visualization.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class SecureCredentialEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for SecureCredentialEntity.

    A secure credential entity.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "secure_credential_id",
        "secure_credential_summary",
        "updated_at",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class SecureCredentialEntityOutline(
    sgqlc.types.Type, AlertableEntityOutline, EntityOutline
):
    """Class for SecureCredentialEntityOutline.

    A secure credential entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "description",
        "secure_credential_id",
        "secure_credential_summary",
        "updated_at",
    )
    description = sgqlc.types.Field(String, graphql_name="description")


class SuggestedAnomalyBasedNrqlQuery(sgqlc.types.Type, SuggestedNrqlQuery):
    """Class for SuggestedAnomalyBasedNrqlQuery.

    A query suggestion based on analysis of events within a specific
    anomalous time range vs. nearby events outside of that time range.
    """

    __schema__ = nerdgraph
    __field_names__ = ("anomaly",)
    anomaly = sgqlc.types.Field(
        sgqlc.types.non_null(SuggestedNrqlQueryAnomaly), graphql_name="anomaly"
    )


class SuggestedHistoryBasedNrqlQuery(sgqlc.types.Type, SuggestedNrqlQuery):
    """Class for SuggestedHistoryBasedNrqlQuery.

    A query suggestion based on historical query patterns.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class SyntheticMonitorEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for SyntheticMonitorEntity.

    A Synthetic Monitor entity.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "assets",
        "monitor_id",
        "monitor_summary",
        "monitor_type",
        "monitored_url",
        "period",
    )
    assets = sgqlc.types.Field(
        sgqlc.types.list_of(SyntheticsSyntheticMonitorAsset),
        graphql_name="assets",
        args=sgqlc.types.ArgDict(
            (
                (
                    "check_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="checkId",
                        default=None,
                    ),
                ),
            )
        ),
    )


class SyntheticMonitorEntityOutline(
    sgqlc.types.Type, AlertableEntityOutline, EntityOutline
):
    """Class for SyntheticMonitorEntityOutline.

    A Synthetic Monitor entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "monitor_id",
        "monitor_summary",
        "monitor_type",
        "monitored_url",
        "period",
    )
    monitor_id = sgqlc.types.Field(ID, graphql_name="monitorId")


class ThirdPartyServiceEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for ThirdPartyServiceEntity.

    A third party service entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class ThirdPartyServiceEntityOutline(
    sgqlc.types.Type, AlertableEntityOutline, EntityOutline
):
    """Class for ThirdPartyServiceEntityOutline.

    A third party service entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class UnavailableEntity(sgqlc.types.Type, AlertableEntity, Entity):
    """Class for UnavailableEntity.

    An entity that is unavailable.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class UnavailableEntityOutline(sgqlc.types.Type, AlertableEntityOutline, EntityOutline):
    """Class for UnavailableEntityOutline.

    An entity outline that is unavailable.
    """

    __schema__ = nerdgraph
    __field_names__ = ()


class WhatsNewAnnouncementContent(sgqlc.types.Type, WhatsNewContent):
    """Class for WhatsNewAnnouncementContent.

    Represents the details about an announcement.
    """

    __schema__ = nerdgraph
    __field_names__ = (
        "body",
        "doc_url",
        "getting_started_url",
        "is_featured",
        "learn_more_url",
        "requirements",
    )
    body = sgqlc.types.Field(String, graphql_name="body")


class WorkloadEntity(sgqlc.types.Type, AlertableEntity, CollectionEntity, Entity):
    """Class for WorkloadEntity.

    A workload entity.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_at", "created_by_user", "updated_at", "workload_status")
    created_at = sgqlc.types.Field(EpochMilliseconds, graphql_name="createdAt")


class WorkloadEntityOutline(sgqlc.types.Type, AlertableEntityOutline, EntityOutline):
    """Class for WorkloadEntityOutline.

    A workload entity outline.
    """

    __schema__ = nerdgraph
    __field_names__ = ("created_at", "created_by_user", "updated_at", "workload_status")
    created_at = sgqlc.types.Field(EpochMilliseconds, graphql_name="createdAt")


class WorkloadRollupRuleStatusResult(sgqlc.types.Type, WorkloadStatusResult):
    """Class for WorkloadRollupRuleStatusResult.

    A rollup rule that was involved in the calculation of the workload
    status.
    """

    __schema__ = nerdgraph
    __field_names__ = ("rollup_rule_details",)
    rollup_rule_details = sgqlc.types.Field(
        WorkloadRollupRuleDetails, graphql_name="rollupRuleDetails"
    )


class WorkloadStaticStatusResult(sgqlc.types.Type, WorkloadStatusResult):
    """Class for WorkloadStaticStatusResult.

    A static status that was involved in the calculation of the
    workload status.
    """

    __schema__ = nerdgraph
    __field_names__ = ("description", "summary")
    description = sgqlc.types.Field(String, graphql_name="description")


class AiNotificationsAuth(sgqlc.types.Union):
    """Class for AiNotificationsAuth.

    Authentication interface.
    """

    __schema__ = nerdgraph
    __types__ = (
        AiNotificationsBasicAuth,
        AiNotificationsOAuth2Auth,
        AiNotificationsTokenAuth,
    )


class AiNotificationsError(sgqlc.types.Union):
    """Class for AiNotificationsError.

    Error object.
    """

    __schema__ = nerdgraph
    __types__ = (
        AiNotificationsConstraintsError,
        AiNotificationsDataValidationError,
        AiNotificationsResponseError,
        AiNotificationsSuggestionError,
    )


class AiWorkflowsConfiguration(sgqlc.types.Union):
    """Class for AiWorkflowsConfiguration.

    Enrichment configuration object.
    """

    __schema__ = nerdgraph
    __types__ = (AiWorkflowsNrqlConfiguration,)


class AlertsNotificationChannelMutation(sgqlc.types.Union):
    """Class for AlertsNotificationChannelMutation.

    Notification channel types that are available for create and
    update operations.
    """

    __schema__ = nerdgraph
    __types__ = (
        AlertsEmailNotificationChannel,
        AlertsOpsGenieNotificationChannel,
        AlertsPagerDutyNotificationChannel,
        AlertsSlackNotificationChannel,
        AlertsVictorOpsNotificationChannel,
        AlertsWebhookNotificationChannel,
        AlertsXMattersNotificationChannel,
    )


class IncidentIntelligenceEnvironmentCreateEnvironmentResultDetails(sgqlc.types.Union):
    """Class for IncidentIntelligenceEnvironmentCreateEnvironmentResultDetails.

    Result details union.
    """

    __schema__ = nerdgraph
    __types__ = (
        IncidentIntelligenceEnvironmentEnvironmentAlreadyExists,
        IncidentIntelligenceEnvironmentEnvironmentCreated,
    )


class IncidentIntelligenceEnvironmentCurrentEnvironmentResultReasonDetails(
    sgqlc.types.Union
):
    """Class for IncidentIntelligenceEnvironmentCurrentEnvironmentResultReasonDetails.

    Reason details union.
    """

    __schema__ = nerdgraph
    __types__ = (
        IncidentIntelligenceEnvironmentMultipleEnvironmentsAvailable,
        IncidentIntelligenceEnvironmentUserNotAuthorizedForAccount,
        IncidentIntelligenceEnvironmentUserNotCapableToOperateOnAccount,
    )


class Nr1CatalogDataSourceInstallDirective(sgqlc.types.Union):
    """Class for Nr1CatalogDataSourceInstallDirective.

    Installation information for a data source.
    """

    __schema__ = nerdgraph
    __types__ = (Nr1CatalogLinkInstallDirective, Nr1CatalogNerdletInstallDirective)


class Nr1CatalogSearchResult(sgqlc.types.Union):
    """Class for Nr1CatalogSearchResult.

    A result returned when executing a search.
    """

    __schema__ = nerdgraph
    __types__ = (
        Nr1CatalogAlertPolicyTemplate,
        Nr1CatalogDashboardTemplate,
        Nr1CatalogDataSource,
        Nr1CatalogNerdpack,
        Nr1CatalogQuickstart,
    )
