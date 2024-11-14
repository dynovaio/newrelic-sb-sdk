# Changelog

## [Unreleased]

## [0.22.0] - 2024-11-14

* Include property `schema` in `NewRelicGqlClient` to store the schema of
  the GraphQL API.
* Include `User-Agent` header in `NewRelicGqlClient` and `NewRelicRestClient`
  to identify the client making the request.
* Specify version typle in `version.py` file.
* Add class `NewRelicError` to handle errors from `NewRelicGqlClient`.
* Add function `raise_response_errors`ro raise errors for responses
  obtained from `NewRelicGqlClient`.
* Add `shortcuts` submodule.

## [0.21.0] - 2024-11-14

* Update development dependencies.
* Update GraphQL submodule with a fresh schema version.
* Add `CollaborationRawContextMetadata` scalar type.
* Add `CollaborationExternalApplicationType`, `CollaborationStatus`,
  `EntityManagementSyncGroupRuleConditionType` enum types.
* Add `OTHER` value to `MultiTenantAuthorizationRoleScopeEnum` choices.
* Add `CollaborationAssistantConfigInput`,
  `EntityManagementCollectionElementsFilter`,
  `EntityManagementCollectionIdFilterArgument`,
  `MultiTenantAuthorizationGrantScopeTypeV2InputFilter`,
  `MultiTenantAuthorizationRoleScopeV2InputFilter` input types.
* Add `optimized_message` field to `InstallationStatusErrorInput` input type.
* Add `scope_v2_type` field to
  `MultiTenantAuthorizationGrantFilterInputExpression` input type.
* Add `scope_v2` field to
  `MultiTenantAuthorizationRoleFilterInputExpression` input type.
* Add `AgentApplicationSettingsApplicationLogging`,
  `AgentApplicationSettingsForwarding`,
  `AgentApplicationSettingsLocalDecorating`,
  `AgentApplicationSettingsMetrics`,
  `CollaborationActorStitchedFields`,
  `CollaborationBotResponse`,
  `CollaborationBotResponseFeedback`,
  `CollaborationCodeMark`,
  `CollaborationComment`,
  `CollaborationCommentConnection`,
  `CollaborationCommentCreator`,
  `CollaborationCommentSyncStatus`,
  `CollaborationContext`,
  `CollaborationEmail`,
  `CollaborationExternalCommentCreator`,
  `CollaborationExternalServiceConnection`,
  `CollaborationExternalServiceConnectionGroup`,
  `CollaborationFile`,
  `CollaborationGrokMessage`,
  `CollaborationLinkedContexts`,
  `CollaborationMention`,
  `CollaborationMessageSent`,
  `CollaborationSocketConnection`,
  `CollaborationSubscriber`,
  `CollaborationSubscriberConnection`,
  `CollaborationSubscriptionsWithUnread`,
  `CollaborationThread`,
  `CollaborationThreadConnection`,
  `CollaborationThreadsCount`,
  `EntityManagementCollectionElementsResult`,
  `EntityManagementSyncGroupRule`,
  `EntityManagementSyncGroupRuleCondition`,
  `EntityManagementSyncGroupsSettings` object types.
* Add `created_at` and `created_by` fields to `AlertsNrqlCondition` interface
  type.
* Add `collaboration` field to `Actor` type.
* Add `application_logging` field to `AgentApplicationSettingsApmBase` type.
* Add `application_logging` field to
  `AgentApplicationSettingsUpdateResult` type.
* Add `collection_elements` field to `EntityManagementActorStitchedFields`
  type.
* Add `configuration_versions`, `description` and `name` field to
  `EntityManagementFleetDeployment` type.
* Add `optimized_message` field to `InstallationStatusError` type.
* Add `collaboration_create_code_mark`,
  `collaboration_create_comment`,
  `collaboration_create_context`,
  `collaboration_create_email`,
  `collaboration_create_external_service_connection`,
  `collaboration_create_mention`,
  `collaboration_create_thread`,
  `collaboration_deactivate_code_mark`,
  `collaboration_deactivate_comment`,
  `collaboration_deactivate_context`,
  `collaboration_deactivate_external_service_connection`,
  `collaboration_deactivate_file`,
  `collaboration_deactivate_mention`,
  `collaboration_deactivate_thread`,
  `collaboration_feedback_on_bot_response`,
  `collaboration_get_upload_url`,
  `collaboration_register_email`,
  `collaboration_send_message`,
  `collaboration_set_external_service_connection_channel`,
  `collaboration_socket_subscribe`,
  `collaboration_subscribe_to_thread`,
  `collaboration_unsubscribe_from_thread`,
  `collaboration_update_comment`,
  `collaboration_update_context_add_comment`,
  `collaboration_update_context_add_thread`,
  `collaboration_update_subscription_read_info`,
  `collaboration_update_thread_add_comment` and
  `collaboration_update_thread_status` fields to `RootMutationType` type.
* Update `agent_type` field type from `ID` to `String` in
  `EntityManagementAgentConfigurationEntity` type.
* Update `agent_type` field type from `ID` to `String` in
  `EntityManagementAgentEntity` type.
* Add `rules` field to `EntityManagementScorecardEntity` type.
* Add `sync_groups` filed to `EntityManagementTeamsOrganizationSettingsEntity`
  type.

## [0.20.0] - 2024-10-25

* Update GraphQL submodule with a fresh schema version.
* Update dependencies
* Add `AlertsActionOnMutingRuleWindowEnded`,
  `EntityManagementEntityScope`,
  `EntityManagementManagedEntityType`,
  `EntityManagementTeamExternalIntegrationType`,
  `SyntheticsBrowser` and `SyntheticsDevice` enum types.
* Add `FIRST_SEEN` value to `ErrorsInboxErrorGroupSortOrderField` choices.
* Change `MUTED` by `ENABLED` value in `SyntheticsMonitorStatus` choices.
* Add `AgentApplicationSettingsApplicationExitInfoInput`,
  `AlertsMutingRulesFilterCriteriaInput`,
  `CloudConfluentDisableIntegrationsInput`,
  `CloudConfluentIntegrationsInput`,
  `CloudConfluentKafkaResourceIntegrationInput`,
  `CloudConfluentLinkAccountInput`,
  `CloudConfluentUpdateAccountInput`,
  `CloudFossaDisableIntegrationsInput`,
  `CloudFossaIntegrationsInput`,
  `CloudFossaIssuesIntegrationInput`,
  `CloudFossaLinkAccountInput`,
  `CloudFossaUpdateAccountInput`,
  `DataManagementAccountLimitInput`,
  `DataManagementLimitLookupInput` and
  `StreamingExportGcpInpu` input types.
* Add `application_exit_info` field to
  `AgentApplicationSettingsMobileSettingsInput` input type.
* Add `exact_name` field to
  `AiNotificationsDestinationFilte` input type.
* Add `update_original_message` field to
  `AiWorkflowsDestinationConfigurationInput` input type.
* Add `action_on_muting_rule_window_ende` field to
  `AlertsMutingRuleInput` input type.
* Add `action_on_muting_rule_window_ende` field to
  `AlertsMutingRuleUpdateInput` input type.
* Add `title_template` field to `AlertsNrqlConditionBaselineInput` input type.
* Add `ignore_on_expected_terminatio` field to
  `AlertsNrqlConditionExpirationInput` input type.
* Add `title_template` field to `AlertsNrqlConditionOutlierInput` input type.
  `AlertsNrqlConditionExpirationInput` input type.
* Add `title_template` field to `AlertsNrqlConditionStaticInput` input type.
* Add `title_template` field to
  `AlertsNrqlConditionUpdateBaselineInput` input type.
* Add `title_template` field to
  `AlertsNrqlConditionUpdateOutlierInput` input type.
* Add `title_template` field to
  `AlertsNrqlConditionUpdateStaticInput` input type.
* Add `confluent` and `foss` fields to
  `CloudDisableIntegrationsInput` input type.
* Add `confluent` and `foss` fields to
  `CloudIntegrationsInput` input type.
* Add `confluent` and `foss` fields to
  `CloudLinkCloudAccountsInput` input type.
* Add `confluent` and `foss` fields to
  `CloudUpdateCloudAccountsInput` input type.
* Add `excluded` field to `DashboardVariableOptionsInput` input type.
* Add `browsers` and `device` fields to
  `SyntheticsCreateScriptBrowserMonitorInput` input type.
* Add `browsers` and `device` fields to
  `SyntheticsCreateSimpleBrowserMonitorInput` input type.
* Add `browsers` and `device` fields to
  `SyntheticsCreateStepMonitorInput` input type.
* Add `browsers` and `device` fields to
  `SyntheticsUpdateScriptBrowserMonitorInput` input type.
* Add `browsers` and `device` fields to
  `SyntheticsUpdateSimpleBrowserMonitorInput` input type.
* Add `browsers` and `device` fields to
  `SyntheticsUpdateStepMonitorInput` input type.
* Add `EntityManagementActor`,
  `EntityManagementEntity`,
  `AgentApplicationSettingsApplicationExitInfo`,
  `AuthenticationDomainType`,
  `EntityManagementActorStitchedFields`,
  `EntityManagementAgentDeployment`,
  `EntityManagementBlob`,
  `EntityManagementDiscoverySettings`,
  `EntityManagementEntityDeleteResult`,
  `EntityManagementEntitySearchResult`,
  `EntityManagementFleetControlProperties`,
  `EntityManagementFleetDeployment`,
  `EntityManagementMetadata`,
  `EntityManagementNrqlRuleEngine`,
  `EntityManagementScopedReference`,
  `EntityManagementTag`,
  `EntityManagementTeamEntities`,
  `EntityManagementTeamExternalIntegration`,
  `EntityManagementTeamMember`,
  `EntityManagementTeamResource`,
  `StreamingExportGcpDetails`,
  `CloudConfluentKafkaResourceIntegration`,
  `CloudFossaIssuesIntegration`,
  `EntityManagementAgentConfigurationEntity`,
  `EntityManagementAgentConfigurationVersionEntity`,
  `EntityManagementAgentEffectiveConfigurationEntity`,
  `EntityManagementAgentEntity`,
  `EntityManagementAgentTypeDefinitionEntity`,
  `EntityManagementCollectionEntity`,
  `EntityManagementFleetEntity`,
  `EntityManagementGenericEntity`,
  `EntityManagementScorecardEntity`,
  `EntityManagementScorecardRuleEntity`,
  `EntityManagementSystemActor`,
  `EntityManagementTeamEntity`,
  `EntityManagementTeamsOrganizationSettingsEntity`,
  `EntityManagementUserActor` and
  `EntityManagementUserEntity` types
* Add `entity_managemen` field to `Actor` type.
* Add `application_exit_info` field to
  `AgentApplicationSettingsMobileSettings` type.
* Add `update_original_messag` field to
  `AiWorkflowsDestinationConfiguration` type.
* Add `args` argument for `muting_rules` firled from
  `AlertsAccountStitchedFields` type.
* Add `action_on_muting_rule_window_ended` and
  `muting_rule_lifecycle_event_published_at` fields to
  `AlertsMutingRule` type.
* Add `ignore_on_expected_termination` field to
  `AlertsNrqlConditionExpiration` type.
* Add `data_account_id` field to `AlertsNrqlConditionQuery` type.
* Add `expires_on` field to `DashboardLiveUrl` type.
* Add `next_curso` and `total_count` fields to `DashboardLiveUrlResult` type.
* Add `excluded` field to `DashboardVariableOptions` type.
* Add `total_count` field to `MultiTenantAuthorizationGrantCollection` type.
* Update `name` and `size_in_bytes` field from `NerdpackAssetInfo` type to be
  `non null`.
* Update fields `assets`, `cli_version`, `description`, `display_name`,
  `nerdpack_id`, `repository_url`, `tags` from `NerdpackVersion` type to be
  `non null`.
* Add `account_management_cancel_account`, `authentication_domain_delete`,
  `data_management_create_account_limit` and `entity_management_delete`
   fields to `RootMutationType` type.
* Add `gcp` field to `StreamingExportRule` type.
* Add `browsers` and `devices` fields to `SyntheticsScriptBrowserMonitor` type.
* Add `browsers` and `devices` fields to `SyntheticsSimpleBrowserMonitor` type.
* Add `browsers` and `devices` fields to `SyntheticsStepMonitor` type.

## [0.19.0] - 2024-06-15

* Update GraphQL submodule with a fresh schema version.
* Add `AgentApplicationSettingsSessionTraceMode`,
  `AgentApplicationSettingsSessionTraceModeInput`,
  `DataSourceGapsGapTypeIdentifier` and
  `LogConfigurationsLiveArchiveRetentionPolicyType` to enum types.
* Add `CUSTOM_HEADERS` value to `AiNotificationsAuthType` choices.
* Add `BROWSERAPPLICATION` and `MONITOR` values to
  `AiTopologyCollectorVertexClass` choices.
* Add `BROWSERAPPLICATION` and `MONITOR` values to
  `AiTopologyVertexClass` choices.
* Add `MONITORS` and `TRIGGERS` values to `EntityRelationshipEdgeType`
  choices.
* Add `GROUP` value to `MultiTenantAuthorizationRoleScopeEnum` choices.
* Add `TYPE` value to `MultiTenantIdentityUserSortKey` choices.
* Remove `ENABLED` value from `SyntheticsMonitorStatus` choices.
* Add `AgentApplicationSettingsMaskInputOptionsInput`,
  `AgentApplicationSettingsSessionReplayInput`,
  `AgentApplicationSettingsSessionTraceInput`,
  `AiNotificationsCustomHeaderInput`,
  `AiNotificationsCustomHeadersAuthInput`,
  `AiNotificationsSecureUrlInput`,
  `AiNotificationsSecureUrlUpdate`,
  `CloudAwsGovCloudUpdateAccountInput`,
  `CloudAwsMsElasticacheIntegrationInput`,
  `CloudAwsUpdateAccountInput`,
  `CloudAzureUpdateAccountInput`,
  `CloudGcpUpdateAccountInput`,
  `CloudUpdateCloudAccountsInput`,
  `DataSourceGapsGapsQuery`,
  `ErrorsInboxStateVersionInput`,
  `MultiTenantAuthorizationGrantAuthenticationDomainIdInputFilter`,
  `MultiTenantAuthorizationRoleGroupIdInputFilter`,
  `MultiTenantIdentityEmailVerificationStateInput`,
  `MultiTenantIdentityUserGroupIdInput`,
  `MultiTenantIdentityUserNotGroupIdInput` and
  `SyntheticsExtendedTypeMonitorRuntimeInput` to input types.
* Add `custom_headers` field to `AiNotificationsCredentialsInput` input type.
* Update in `terms` field type in `AlertsNrqlConditionStaticInput` input type.
* Add `aws_ms_elasticache` field to `CloudAwsDisableIntegrationsInput` input
  type.
* Add `aws_ms_elasticache` field to `CloudAwsIntegrationsInput` input
  type.
* Add `authentication_domain_id` field to
  `MultiTenantAuthorizationGrantFilterInputExpression` input type.
* Allow null values for `eq` field in
  `MultiTenantAuthorizationGrantScopeTypeInputFilter` input type.
* Allow null values for `eq` field in
  `MultiTenantAuthorizationPermissionFilterRoleIdInput` input type.
* Add `group_id` field to
  `MultiTenantAuthorizationRoleFilterInputExpression` input type.
* Allow null values for `eq` field in
  `MultiTenantAuthorizationRoleIdInputFilter` input type.
* Allow null values for `eq` field in
  `MultiTenantAuthorizationRoleNameInputFilter` input type.
* Add `contains` field to
  `MultiTenantAuthorizationRoleNameInputFilter` input type.
* Allow null values for `eq` field in
  `MultiTenantAuthorizationRoleScopeInputFilter` input type.
* Allow null values for `eq` field in
  `MultiTenantAuthorizationRoleTypeInputFilter` input type.
* Allow null values for `eq` field in
  `MultiTenantIdentityEmailVerificationStateInput` input type.
* Allow null values for `eq` field in
  `MultiTenantIdentityGroupIdInput` input type.
* Add `excludes` field to
  `MultiTenantIdentityGroupMemberIdInput` input type.
* Allow null values for `contains` field in
  `MultiTenantIdentityGroupMemberIdInput` input type.
* Allow null values for `exists` field in
  `MultiTenantIdentityPendingUpgradeRequestInput` input type.
* Add `email_verification_state` and `group_id` fields to
  `MultiTenantIdentityUserFilterInput` input type.
* Allow null values for `eq` field in
  `OrganizationAccountIdFilterInput` input type.
* Allow null values for `contains` field in
  `OrganizationAccountNameFilterInput` input type.
* Allow null values for `eq` field in
  `OrganizationAccountSharingModeFilterInput` input type.
* Allow null values for `eq` field in
  `OrganizationAccountStatusFilterInput` input type.
* Allow null values for `eq` field in
  `OrganizationContractCustomerIdInputFilter` input type.
* Allow null values for `eq` field in
  `OrganizationContractOrganizationIdInputFilter` input type.
* Allow null values for `eq` field in
  `OrganizationIdInput` input type.
* Allow null values for `eq` field in
  `OrganizationOrganizationAccountIdInputFilter` input type.
* Allow null values for `eq` field in
  `OrganizationOrganizationAuthenticationDomainIdInputFilter` input type.
* Allow null values for `eq` field in
  `OrganizationOrganizationCreateJobCustomerIdInput` input type.
* Allow null values for `eq` field in
  `OrganizationOrganizationCustomerIdInputFilter` input type.
* Allow null values for `eq` field in
  `OrganizationOrganizationIdInputFilter` input type.
* Allow null values for `eq` field in
  `OrganizationTargetIdInput` input type.
* Add `runtime` field to
  `SyntheticsCreateBrokenLinksMonitorInput` input type.
* Add `runtime` field to
  `SyntheticsCreateCertCheckMonitorInput` input type.
* Add `runtime` field to
  `SyntheticsCreateStepMonitorInput` input type.
* Add `runtime` field to
  `SyntheticsUpdateBrokenLinksMonitorInput` input type.
* Add `runtime` field to
  `SyntheticsUpdateCertCheckMonitorInput` input type.
* Add `runtime` field to
  `SyntheticsUpdateStepMonitorInput` input type.
* Rename `AgentRelease` to `AgentReleasesAgentRelease` object type.
* Add `AgentApplicationSettingsMaskInputOptions`,
  `AgentApplicationSettingsSessionReplay`,
  `AgentApplicationSettingsSessionTrace`,
  `AiNotificationsCustomHeader`,
  `AiNotificationsCustomHeadersAuth`,
  `AiNotificationsSecureUrl`,
  `ApiAccessNrPlatformStitchedFields`,
  `ApiAccessValidateUserKeyResult`,
  `CloudTemplateParam`,
  `CloudUpdateAccountPayload`,
  `DataSourceGapsActorStitchedFields`,
  `DataSourceGapsGap`,
  `DataSourceGapsGapType`,
  `DataSourceGapsGapsResult`,
  `LogConfigurationsLiveArchiveConfiguration`,
  `SyntheticsExtendedTypeMonitorRuntime`,
  `CloudAwsMsElasticacheIntegration` to object types.
* Add `template_params` field to `CloudProvider` object type.
* Add `data_source_gaps` field to `Actor` object type.
* Add `session_replay` and `session_trace` fields to
  `AgentApplicationSettingsBrowserBase` object type.
* Add `host_display_name` and `instance_name` fields to
  `AgentEnvironmentApplicationInstanceDetails` object type.
* Remove all fields from `AiTopologyAccountStitchedFields` object type.
* Add `created_by` field to `DashboardLiveUrl` object type.
* Add `current_agent_release` field to `DocumentationFields` object type.
* Add `resolve_in_next_version` and `versions` fields to
  `ErrorsInboxUpdateErrorGroupStateResponse` object type.
* Add `live_archive_configurations` field to
  `LogConfigurationsAccountStitchedFields` object type.
* Add `created_at`, `parent_id`, `partnership_id`, `partnership_name`
  and `pay_method` fields to `OrganizationAccount` object type.
* Add `cloud_update_account` and
  `log_configurations_update_live_archive_configuration` fields to
  `RootMutationType` object type.
* Remove `ai_topology_collector_create_edges`,
  `ai_topology_collector_create_vertices`,
  `ai_topology_collector_delete_edges` and
  `ai_topology_collector_delete_vertices` fields from
  `RootMutationType` object type.
* Allow null values in `nerdpack_create` field in
  `RootMutationType` object type.
* Add `runtime` field to
  `SyntheticsStepMonitor` object type.
* Add `AiNotificationsCustomHeadersAuth` item to
  `AiNotificationsAuth` union type.

## [0.18.0] - 2024-02-04

* Update GraphQL submodule with a fresh schema version.
* Add `DataManagementType` and `MultiTenantAuthorizationPermissionCategoryEnum`
  enum types.
* Add `OIDC_SSO` choice to `OrganizationAuthenticationTypeEnum`.
* Add `DashboardVariableOptionsInput`,
  `MultiTenantAuthorizationPermissionFilter`,
  `MultiTenantAuthorizationPermissionFilterRoleIdInput` and
  `MultiTenantIdentityPendingUpgradeRequestInput` input types.
* Add field `organization_id` to `AccountManagementCreateInput` input type.
* Add field `options` to `DashboardVariableInput` input type.
* Add field `plugin_attributes_cleanup_enabled` to
  `LogConfigurationsPipelineConfigurationInput` input type.
* Add field `pending_upgrade_request` to
  `MultiTenantIdentityUserFilterInput` input type.
* Drop `DateTimeWindow` object type.
* Add `DashboardVariableOptions`, `MultiTenantAuthorizationPermission`,
  `MultiTenantAuthorizationPermissionCollection`,
  `MultiTenantIdentityPendingUpgradeRequest` object types.
* Add fields `updated_at` and `updated_by` to `AlertsNrqlCondition` object
  type.
* Add field `obfuscated_key` to `ApiAccessKey` object type.
* Add field `permissions` to `CustomerAdministration` object type.
* Add field `options` to `DashboardVariable` object type.
* Add field `type` to `DataManagementAccountLimit` object type.
* Add field `name` to `MultiTenantAuthorizationGrantRole` object type.
* Add field `total_count` to `MultiTenantAuthorizationRoleCollection` object
  type.
* Add field `total_count` to `MultiTenantIdentityGroupCollection` object
  type.
* Add field `total_count` to `MultiTenantIdentityUserCollection` object
  type.
* Add field `total_count` to `OrganizationAccountCollection` object
  type.
* Add field `pending_upgrade_request` to `MultiTenantIdentityUser` object type.
* Drop support for python 3.8.
* Update development dependencies.
* Update .pre-commit-config.yaml.

## [0.17.0] - 2023-11-26

* Update GraphQL submodule with a fresh schema version.
* Add `OrganizationBillingStructure`,
  `OrganizationOrganizationCreateJobResultStatusEnum`,
  `OrganizationOrganizationCreateJobStatusEnum`,
  `SyntheticsMonitorDowntimeDayOfMonthOrdinal` and
  `SyntheticsMonitorDowntimeWeekDays` enum types.
* Add `CloudGcpAiplatformIntegrationInput`,
  `MultiTenantAuthorizationGrantFilterInputExpression`,
  `MultiTenantAuthorizationGrantGroupIdInputFilter`,
  `MultiTenantAuthorizationGrantIdInputFilter`,
  `MultiTenantAuthorizationGrantOrganizationIdInputFilter`,
  `MultiTenantAuthorizationGrantRoleIdInputFilter`,
  `MultiTenantAuthorizationGrantScopeIdInputFilter`,
  `MultiTenantAuthorizationGrantScopeTypeInputFilter`,
  `MultiTenantAuthorizationGrantSortInput`,
  `MultiTenantAuthorizationRoleFilterInputExpression`,
  `MultiTenantAuthorizationRoleIdInputFilter`,
  `MultiTenantAuthorizationRoleNameInputFilter`,
  `MultiTenantAuthorizationRoleOrganizationIdInputFilter`,
  `MultiTenantAuthorizationRoleScopeInputFilter`,
  `MultiTenantAuthorizationRoleSortInput`,
  `MultiTenantAuthorizationRoleTypeInputFilter`,
  `OrganizationContractCustomerIdInputFilter`,
  `OrganizationContractOrganizationIdInputFilter`,
  `OrganizationCustomerContractFilterInput`,
  `OrganizationOrganizationCreateAsyncResultFilterInput`,
  `OrganizationOrganizationCreateJobCustomerIdInput`,
  `OrganizationOrganizationCreateJobIdInput`,
  `OrganizationOrganizationCreateJobStatusInput`,
  `OrganizationOrganizationGroupFilterInput`,
  `OrganizationOrganizationGroupIdInputFilter`,
  `OrganizationOrganizationGroupNameInputFilter`,
  `OrganizationOrganizationGroupOrganizationIdInputFilter`,
  `SyntheticsDateWindowEndConfig`,
  `SyntheticsDaysOfWeek`,
  `SyntheticsMonitorDowntimeDailyConfig`,
  `SyntheticsMonitorDowntimeMonthlyConfig`,
  `SyntheticsMonitorDowntimeMonthlyFrequency`,
  `SyntheticsMonitorDowntimeOnceConfig` and
  `SyntheticsMonitorDowntimeWeeklyConfig` input types.
* Add field `gcp_aiplatform` to `CloudGcpDisableIntegrationsInput` input type.
* Add field `gcp_aiplatform` to `CloudGcpIntegrationsInput` input type.
* Add `Consumption`, `CustomerAdministration`, `CustomerAdministrationJobs`,
  `ErrorsInboxVersion`, `MultiTenantAuthorizationGrant`,
  `MultiTenantAuthorizationGrantCollection`,
  `MultiTenantAuthorizationGrantGroup`,
  `MultiTenantAuthorizationGrantRole`, `MultiTenantAuthorizationGrantScope`,
  `MultiTenantAuthorizationRole`, `MultiTenantAuthorizationRoleCollection`,
  `OrganizationCustomerContract`, `OrganizationCustomerContractWrapper`,
  `OrganizationOrganizationCreateAsyncCustomerResult`,
  `OrganizationOrganizationCreateAsyncJobResult`,
  `OrganizationOrganizationCreateAsyncOrganizationResult`,
  `OrganizationOrganizationCreateAsyncResult`,
  `OrganizationOrganizationCreateAsyncResultCollection`,
  `OrganizationOrganizationGroup`, `OrganizationOrganizationGroupWrapper`,
  `SyntheticsDailyMonitorDowntimeMutationResult`,
  `SyntheticsDateWindowEndOutput`, `SyntheticsDaysOfWeekOutput`,
  `SyntheticsDailyMonitorDowntimeMutationResult`,
  `SyntheticsDateWindowEndOutput`, `SyntheticsDaysOfWeekOutput`,
  `SyntheticsMonthlyMonitorDowntimeMutationResult`,
  `SyntheticsOnceMonitorDowntimeMutationResult`,
  `SyntheticsWeeklyMonitorDowntimeMutationResult` and
  `CloudGcpAiplatformIntegration` object types.
* Update field `items` of `OrganizationCustomerOrganizationWrapper` object type
  to be not null.
* Add field `customer_administration` to `RootQueryType` object type.
* Add fields `first_seen_versions` and `last_seen_versions` to
  `ErrorsInboxErrorGroup` object type.
* Update development dependencies.
* Update .pre-commit-config.yaml.

## [0.16.0] - 2023-10-22

* Update GraphQL submodule with a fresh schema version.
* Add `MultiTenantIdentityCapability`,
  `MultiTenantIdentityEmailVerificationState`,
  `MultiTenantIdentitySortDirection`, `MultiTenantIdentitySortKeyEnum`,
  `MultiTenantIdentitySortKeyEnum`, `OrganizationAccountShareSortDirectionEnum`,
  `OrganizationAccountShareSortKeyEnum`, `OrganizationAccountShareSortKeyEnum`,
  `OrganizationAccountSortKeyEnum`, `OrganizationAccountStatus`,
  `OrganizationRegionCodeEnum`, `OrganizationSharingMode`,
  `OrganizationSharingMode`, `UserManagementGroupSortKey` and
  `UserManagementSortDirection` enum types.
* Add `INVALID_CHANNEL_NAME` as choice option to `AiNotificationsErrorType`
  enum type.
* Add `HEROKU_SSO` as choice option to `OrganizationAuthenticationTypeEnum`
  enum type.
* Add `MultiTenantIdentityGroup`, `MultiTenantIdentityGroupCollection`,
  `MultiTenantIdentityGroupUser`, `MultiTenantIdentityGroupUsers`,
  `MultiTenantIdentityUser`, `MultiTenantIdentityUserCollection`,
  `MultiTenantIdentityUserGroup`, `MultiTenantIdentityUserGroups`,
  `MultiTenantIdentityUserType`, `OrganizationAccount`,
  `OrganizationAccountCollection`, `OrganizationAccountShare`,
  `OrganizationAccountShareCollection`,
  `OrganizationAccountShareLimitingRoleWrapper`,
  `OrganizationAccountShareOrganizationWrapper` and
  `OrganizationCreateOrganizationResponse` types.
* Add `account` field in `AiIssuesIIncident` interface type.
* Remove `environment_id` field in `AiIssuesIIncident` interface type.
* Add `account` field in `AiIssuesIssue` type.
* Remove `environment_id` field in `AiIssuesIssue` type.
* Remove `installer` field from `Nr1CatalogQuickstartMetadata` type.
* Change types of `source_organization_id` and `target_organization_id`
  aguments for `account_shares` field of `Organization` type from `String` to
  `ID`.
* Change types of `source_organization_id` and `target_organization_id` fields
  of `OrganizationSharedAccount` type from `String` to `ID`.
* Add `organization_create` field to `RootMutationType` type.
* Add `payload_compression` field to `StreamingExportRule` type.
* Add `sort` argument for `groups` field of `UserManagementAuthenticationDomain`
  type.
* Add `OrganizationAccountFilterInput`, `OrganizationAccountIdFilterInput`,
  `OrganizationAccountIdInput`, `OrganizationAccountNameFilterInput`,
  `OrganizationAccountOrganizationIdFilterInput`,
  `OrganizationAccountShareFilterInput`, `OrganizationAccountShareSortInput`,
  `OrganizationAccountSharingModeFilterInput`, `OrganizationAccountSortInput`,
  `OrganizationAccountStatusFilterInput`,
  `OrganizationCreateOrganizationInput`, `OrganizationNewManagedAccountInput`,
  `OrganizationSharedAccountInput`, `OrganizationTargetIdInput` and
  `UserManagementGroupSortInput` input type.
* Add `pinned_version` field to `AgentApplicationSettingsBrowserMonitoringInput`
  input type.
* Add `statuses` field to `AiNotificationsChannelFilter` input type.
* Add `guid` field to `AiWorkflowsFilters` input type.
* Add `recipe_names` field to `Nr1CatalogSearchFilter` input type.
* Change type of `target_organization_id` field of
  `OrganizationCreateSharedAccountInput` input type from `String` to `ID`.
* Add field `payload_compression` to `StreamingExportRuleInput` input type.
* Remove `non_null` constraint for `user_type` field from
  `UserManagementCreateUser` input type.
* Update development dependencies.
* Update .pre-commit-config.yaml.

## [0.15.0] - 2023-09-24

* Update GraphQL submodule with a fresh schema version.
* Add object type `ErrorsInboxErrorGroupBase`.
* Update `ErrorsInboxErrorGroup` with `ErrorsInboxErrorGroupBase` as base class.
* Update `ErrorsInboxErrorGroupOutline` with `ErrorsInboxErrorGroupBase` as
  base class.
* Update development dependencies.
* Update .pre-commit-config.yaml.

## [0.14.0] - 2023-09-13

* Update GraphQL submodule with a fresh schema version.
* Add `TEAM` as choice option to `EntityCollectionType` enum type.
* Add field `pinned_version` to `AgentApplicationSettingsBrowserMonitoring`
  object type.
* Remove fields `notification_channel` and `notification_channels` from
  `AlertsAccountStitchedFields` object type.
* Remove mutations `alerts_notification_channel_create`,
  `alerts_notification_channel_delete`, `alerts_notification_channel_update`,
  `alerts_notification_channels_add_to_policy`,
  `alerts_notification_channels_remove_from_policy`.
* Add `TeamEntity` object type.

## [0.13.0] - 2023-09-04

* Update GraphQL submodule with a fresh schema version.
* Add `AgentApplicationSegmentsListType` enum type.
* Add `AgentApplicationSegmentsBrowserSegmentAllowListInput` and
  `AgentApplicationSegmentsSegmentAllowListFilters` input object types.
* Add `AgentApplicationSegmentsBrowserSegmentAllowList` and
  `AgentApplicationSegmentsBrowserSegmentAllowListResult` object types.
* Add `agent_application_segments_replace_all_browser_segment_allow_list` to
  `AgentApplicationSettingsApmBase` object type.
* Add `segment_allow_list_aggregate` to `BrowserApplicationEntity` object
  type.
* Add markdownlint to pre-commit.

## [0.12.0] - 2023-08-20

* Update GraphQL submodule with a fresh schema version.
* Add `ErrorsInboxRawEvent` scalar type.
* Add `ErrorsInboxEventSource` enum type.
* Add field `events` to `DataDictionaryAttribute` object type.
* Add field `is_custom` to `ErrorsInboxErrorGroup` object type.
* Add fields `is_acknowledged`, `is_correlated` and `mutting_states` to
  `AiIssuesFilterIssues` input object type.
* Add fields `event` and `source` fields to `ErrorsInboxErrorEventInput` input
  object type.
* Remove `AgentFeaturesFilter` object type.
* Remove field `agent_features` from `DocumentationFields` object type.
* Add tests for newrelic_sb_sdk.utils.query.
* Add tests for newrelic_sb_sdk.utils.response.
* Add shellcheck to pre-commit.
* Fix lint errors in CI/CD scripts.

## [0.11.0] - 2023-07-26

* Update GraphQL submodule with a fresh schema version.
* Update AiNotificationsChannelType, AiNotificationsDestinationType,
  AiWorkflowsDestinationType and AiNotificationsProduct values.
* Update ErrorsInboxErrorEventInput properties.

## [0.10.0] - 2023-07-14

* Update GraphQL submodule with a fresh schema version.
* New Object CloudDashboardTemplate.

## [0.9.0] - 2023-07-02

* Report test execution to Gitlab.
* Update Gitlab CI/CD pipelines.
* Restore docs building and publishing to Gitlab Pages

## [0.8.0] - 2023-07-01

* Update GraphQL submodule with a fresh schema version.
* Update dependencies.
* Add tests.
* Add autopublish with GitLab CI/CD.

## [0.7.0] - 2023-06-12

* Rename arguments in NewRelicGqlClient.build_query method and build_query
  function from `query_params` to `params` and  `query_string` to `template`.
* Update graphql module.
* Add metadata about language info in GraphQL notebook.
* Add new clasifiers for PyPi.
* Add build status badge.
* Update links documentation links.

## [0.6.0] - 2023-06-10

* Make `query_params` optional in `build_query`.
* Fix code generation form nerdgraph schema.
* Fix graphql module.

## [0.5.0] - 2023-06-05

* Replace pipe operator by Union in types annotations to ensure compatibility
  with python 3.8.1 and higer.

## [0.4.0] - 2023-06-05

* Update GraphQL submodule with a fresh schema version.
* Update dependencies.
* Update pre-commit hooks.

## [0.3.0] - 2023-04-16

* Update links to GitLab repository.
* Update tbump config.
* Update contributing guide.

## [0.2.0] - 2023-03-12

* Update NewRelicGqlClient to support GraphQL variables in request body.
* Update NewRelicGqlClient to use `build_query` from `utils.query`.
* Update typing in build_query from utils.query.
* Add tests for `utils.test`.
* Export query and response notebooks to utils submodule.
* Add Alerts submodule.

## [0.1.0] - 2023-03-09

* Complete development with nbdev.
* Complete documentation in Jupyterbook.
* Add Dashboards module.
* Add GraphQL module.
