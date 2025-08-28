# Changelog

## [Unreleased]

## [0.38.0] - 2025-08-28

* Add new scalar: `AgentApplicationSettingsCustomJsConfiguration`.

* Add new enums:
  `AiWorkflowsBatchCreateMigratedWorkflowsErrorType`,
  `AiWorkflowsBatchDeleteMigratedWorkflowsErrorType`,
  `AiWorkflowsFetchWorkflowsByIssuesFilterErrorType`,
  `MachineLearningEncodingName`, `MachineLearningFilterByKeys`,
  `MachineLearningOperator`, `MachineLearningTextSplitterType`.

* Add new input objects:
  `AgentApplicationSettingsMobileSessionReplayInput`,
  `MachineLearningAddDocumentIndexConfiguration`,
  `MachineLearningCharacterTextSplitterOptionsInput`,
  `MachineLearningFilterBy`,
  `MachineLearningMarkdownTextSplitterOptionsInput`,
  `MachineLearningTokenTextSplitterOptionsInput`.

* Add new objects:
  `AgentApplicationSettingsMobileSessionReplay`,
  `AiWorkflowsBatchCreateMigratedWorkflowsResponseError`,
  `AiWorkflowsBatchDeleteMigratedWorkflowsResponseError`,
  `AiWorkflowsFetchWorkflowsByIssuesFilterResponseError`,
  `MachineLearningAccountStitchedFields`,
  `MachineLearningActorStitchedFields`,
  `MachineLearningExperiment`, `MachineLearningExperimentConnection`,
  `MachineLearningFileDataSource`, `MachineLearningFileDataSourceConnection`,
  `MachineLearningModel`, `MachineLearningModelConnection`,
  `MachineLearningProject`, `MachineLearningProjectConnection`,
  `MachineLearningRagQueryDataResponse`,
  `MachineLearningStreamDataSource`, `MachineLearningStreamDataSourceConnection`,
  `MachineLearningTag`, `MachineLearningTagConnection`,
  `MachineLearningTransactionResponse`.

* Update existing enums:
  * Add `WORKFLOW_AUTOMATION` value to `AiWorkflowsDestinationType`.

* Add fields to existing types:
  * `Account`: add `machine_learning` field
    (`MachineLearningAccountStitchedFields`).
  * `Actor`: add `machine_learning` field
    (`MachineLearningActorStitchedFields`).
  * `AgentApplicationSettingsMobileBase`:
    * Add `mobile_session_replay` field
      (`AgentApplicationSettingsMobileSessionReplay`).
    * Update `__field_names__` to include `mobile_session_replay`.
  * `AgentApplicationSettingsMobileSettingsInput`:
    * Add `mobile_session_replay` field
      (`AgentApplicationSettingsMobileSessionReplayInput`).
    * Update `__field_names__` to include `mobile_session_replay`.

* Add multiple Machine Learning mutations to `RootMutationType`:
  `machine_learning_add_document_index`,
  `machine_learning_add_file_data_source`,
  `machine_learning_add_stream_data_source`,
  `machine_learning_create_file_data_source`,
  `machine_learning_create_project`,
  `machine_learning_create_stream_data_source`,
  `machine_learning_delete_file_data_source`,
  `machine_learning_delete_project`,
  `machine_learning_delete_stream_data_source`,
  `machine_learning_halt_stream_data_source`,
  `machine_learning_remove_document_index`,
  `machine_learning_remove_file_data_source`,
  `machine_learning_remove_stream_data_source`,
  `machine_learning_start_stream_data_source`,
  `machine_learning_update_file_data_source`,
  `machine_learning_update_project`,
  `machine_learning_update_stream_data_source`.

* Add Collaboration mutations to `RootMutationType`:
  `collaboration_create_context`, `collaboration_create_email`,
  `collaboration_create_external_service_connection`,
  `collaboration_create_mention`,
  `collaboration_create_thread`, `collaboration_deactivate_code_mark`,
  `collaboration_deactivate_comment`, `collaboration_deactivate_context`,
  `collaboration_deactivate_external_service_connection`,
  `collaboration_deactivate_file`, `collaboration_deactivate_mention`,
  `collaboration_deactivate_thread`, `collaboration_feedback_on_bot_response`,
  `collaboration_get_upload_url`, `collaboration_register_email`,
  `collaboration_send_message`,
  `collaboration_set_external_service_connection_channel`,
  `collaboration_socket_subscribe`, `collaboration_subscribe_to_thread`,
  `collaboration_unsubscribe_from_thread`, `collaboration_update_comment`,
  `collaboration_update_context_add_comment`,
  `collaboration_update_context_add_thread`,
  `collaboration_update_subscription_read_info`,
  `collaboration_update_thread_add_comment`,
  `collaboration_update_thread_status`.

* Add Dashboard mutations to `RootMutationType`:
  `dashboard_add_widgets_to_page`, `dashboard_create`,
  `dashboard_create_live_url`,
  `dashboard_create_snapshot_url`, `dashboard_delete`,
  `dashboard_revoke_live_url`,
  `dashboard_undelete`, `dashboard_update`, `dashboard_update_live_url`,
  `dashboard_update_live_url_creation_policies`, `dashboard_update_page`,
  `dashboard_update_widgets_in_page`, `dashboard_widget_revoke_live_url`.

* Add Data Management mutations to `RootMutationType`:
  `data_management_copy_retentions`, `data_management_create_account_limit`,
  `data_management_create_event_retention_rule`,
  `data_management_create_retention_rules`,
  `data_management_delete_event_retention_rule`,
  `data_management_update_feature_settings`.

* Add Edge (trace) mutations to `RootMutationType`:
  `edge_create_trace_filter_rules`, `edge_delete_trace_filter_rules`,
  `edge_create_trace_observer`, `edge_delete_trace_observers`,
  `edge_update_trace_observers`.

* Add Entity mutations to `RootMutationType`:
  `entity_delete`, `entity_golden_metrics_override`, `entity_golden_metrics_reset`,
  `entity_golden_tags_override`, `entity_golden_tags_reset`.

* Add Entity Management mutations to `RootMutationType`:
  * Collections & membership: `entity_management_create_collection`,
    `entity_management_add_collection_members`,
    `entity_management_remove_collection_members`,
    `entity_management_update_collection`, `entity_management_delete`.
  * AI entities: `entity_management_create_ai_agent`,
    `entity_management_update_ai_agent`, `entity_management_create_ai_tool`,
    `entity_management_update_ai_tool`.
  * Confluence: `entity_management_create_confluence_integration`,
    `entity_management_update_confluence_integration`,
    `entity_management_create_confluence_rag_settings`,
    `entity_management_update_confluence_rag_settings`.
  * Git repositories: `entity_management_create_git_repository`,
    `entity_management_update_git_repository`.
  * Inbox: `entity_management_create_inbox_issue_category`,
    `entity_management_update_inbox_issue_category`,
    `entity_management_create_performance_inbox_setting`,
    `entity_management_update_performance_inbox_setting`.
  * Pipelines: `entity_management_create_pipeline_cloud_rule`.
  * RAG tools: `entity_management_create_rag_tool`,
    `entity_management_update_rag_tool`.
  * Scorecards: `entity_management_create_scorecard`,
    `entity_management_update_scorecard`,
    `entity_management_create_scorecard_rule`,
    `entity_management_update_scorecard_rule`.
  * Teams & org settings: `entity_management_create_team`,
    `entity_management_update_team`,
    `entity_management_update_teams_organization_settings`.
  * Relationships: `entity_management_create_relationship`,
    `entity_management_delete_relationship`.
  * Generic update: `entity_management_update`.

* Add Entity Relationship (user-defined) mutations to `RootMutationType`:
  `entity_relationship_user_defined_create_or_replace`,
  `entity_relationship_user_defined_delete`.

* Add Errors Inbox mutations to `RootMutationType`:
  `errors_inbox_assign_error_group`, `errors_inbox_delete_error_group_resource`,
  `errors_inbox_update_error_group_state`.

* Add Events to Metrics mutations to `RootMutationType`:
  `events_to_metrics_create_rule`, `events_to_metrics_delete_rule`,
  `events_to_metrics_update_rule`.

* Add Historical Data Export mutations to `RootMutationType`:
  `historical_data_export_cancel_export`,
  `historical_data_export_create_export`.

* Add Incident Intelligence Environment mutations to `RootMutationType`:
  `incident_intelligence_environment_consent_accounts`,
  `incident_intelligence_environment_consent_authorized_accounts`,
  `incident_intelligence_environment_delete_environment`,
  `incident_intelligence_environment_dissent_accounts`.

* Add Installation mutations to `RootMutationType`:
  `installation_create_install_status`, `installation_create_recipe_event`,
  `installation_delete_install`.

* Add Key Transactions mutations to `RootMutationType`:
  `key_transaction_create`, `key_transaction_delete`, `key_transaction_update`.

* Add Log Configurations mutations to `RootMutationType`:
  `log_configurations_create_data_partition_rule`,
  `log_configurations_delete_data_partition_rule`,
  `log_configurations_update_data_partition_rule`,
  `log_configurations_create_obfuscation_expression`,
  `log_configurations_update_obfuscation_expression`,
  `log_configurations_delete_obfuscation_expression`,
  `log_configurations_create_obfuscation_rule`,
  `log_configurations_update_obfuscation_rule`,
  `log_configurations_delete_obfuscation_rule`,
  `log_configurations_create_parsing_rule`,
  `log_configurations_update_parsing_rule`,
  `log_configurations_delete_parsing_rule`,
  `log_configurations_update_live_archive_configuration`,
  `log_configurations_upsert_pipeline_configuration`.

## [0.37.0] - 2025-06-20

* Add new enums: `AiWorkflowsBatchCreateMigratedWorkflowsErrorType`,
  `AiWorkflowsBatchDeleteMigratedWorkflowsErrorType`,
  `AiWorkflowsFetchWorkflowsByIssuesFilterErrorType`,
  `MachineLearningEncodingName`, `MachineLearningFilterByKeys`,
  `MachineLearningOperator`, `MachineLearningTextSplitterType`.
* Add new input objects: `AgentApplicationSettingsMobileSessionReplayInput`,
  `MachineLearningAddDocumentIndexConfiguration`,
  `MachineLearningCharacterTextSplitterOptionsInput`,
  `MachineLearningFilterBy`, `MachineLearningMarkdownTextSplitterOptionsInput`,
  `MachineLearningTokenTextSplitterOptionsInput`.
* Add new objects: `AgentApplicationSettingsMobileSessionReplay`,
  `AiWorkflowsBatchCreateMigratedWorkflowsResponseError`,
  `AiWorkflowsBatchDeleteMigratedWorkflowsResponseError`,
  `AiWorkflowsFetchWorkflowsByIssuesFilterResponseError`,
  `MachineLearningAccountStitchedFields`, `MachineLearningActorStitchedFields`,
  `MachineLearningExperiment`, `MachineLearningExperimentConnection`,
  `MachineLearningFileDataSource`, `MachineLearningFileDataSourceConnection`,
  `MachineLearningModel`, `MachineLearningModelConnection`,
  `MachineLearningProject`, `MachineLearningProjectConnection`,
  `MachineLearningRagQueryDataResponse`, `MachineLearningStreamDataSource`,
  `MachineLearningStreamDataSourceConnection`, `MachineLearningTag`,
  `MachineLearningTagConnection`, `MachineLearningTransactionResponse`.
* Add new scalar: `AgentApplicationSettingsCustomJsConfiguration`.
* Add `WORKFLOW_AUTOMATION` value to `AiWorkflowsDestinationType` enum.
* Add `mobile_session_replay` field to `AgentApplicationSettingsMobileBase`
  and `AgentApplicationSettingsMobileSettingsInput`.
* Add `machine_learning` field to `Account` and `Actor` objects.
* Add multiple Machine Learning mutations to `RootMutationType`:
  `machine_learning_add_document_index`,
  `machine_learning_add_file_data_source`,
  `machine_learning_add_stream_data_source`,
  `machine_learning_create_file_data_source`,
  `machine_learning_create_project`,
  `machine_learning_create_stream_data_source`,
  `machine_learning_delete_file_data_source`,
  `machine_learning_delete_project`,
  `machine_learning_delete_stream_data_source`,
  `machine_learning_halt_stream_data_source`,
  `machine_learning_remove_document_index`,
  `machine_learning_remove_file_data_source`,
  `machine_learning_remove_stream_data_source`,
  `machine_learning_start_stream_data_source`,
  `machine_learning_update_file_data_source`,
  `machine_learning_update_project`,
  `machine_learning_update_stream_data_source`.

## [0.36.0] - 2025-06-07

* Add new scalar: `ChangeTrackingRawCustomAttributesMap`.
* Add new enums: `ChangeTrackingCategoryType`,
  `EntityManagementAiToolParameterType`, `EntityManagementAssignmentType`,
  `EntityManagementCategory`, `EntityManagementConnectionType`,
  `EntityManagementDirection`, `EntityManagementEncodingType`,
  `EntityManagementExecutionStatus`, `EntityManagementInstallationStatus`,
  `EntityManagementJiraIssueType`, `EntityManagementKeyType`,
  `EntityManagementMessageType`, `EntityManagementPriority`,
  `EntityManagementSigningAlgorithm`, `EntityManagementStatusCode`,
  `EntityManagementSyncConfigurationMode`, `KnowledgePublishStatus`.
* Add new interface types: `ChangeTrackingEvent`.
* Add new input types: `ChangeTrackingCategoryAndTypeInput`,
  `ChangeTrackingCategoryFieldsInput`, `ChangeTrackingCategoryRelatedInput`,
  `ChangeTrackingChangeTrackingSearchFilter`, `ChangeTrackingCreateEventInput`,
  `ChangeTrackingDeploymentFieldsInput`, `ChangeTrackingEntitySearchInput`,
  `ChangeTrackingFeatureFlagFieldsInput`,
  `CloudAwsMetadataGovIntegrationInput`,
  `CloudAwsMsElasticacheGovIntegrationInput`,
  `CloudAwsTagsGlobalGovIntegrationInput`,
  `CloudConfluentKafkaConnectorResourceIntegrationInput`,
  `CloudConfluentKafkaKsqlResourceIntegrationInput`,
  `CloudSecurityHubIntegrationInput`,
  `EntityManagementAiAgentEntityCreateInput`,
  `EntityManagementAiAgentEntityUpdateInput`,
  `EntityManagementAiToolEntityCreateInput`,
  `EntityManagementAiToolEntityUpdateInput`,
  `EntityManagementAiToolParameterCreateInput`,
  `EntityManagementAiToolParameterUpdateInput`,
  `EntityManagementLlmConfigCreateInput`,
  `EntityManagementLlmConfigUpdateInput`.
* Add new object types: `AgentReleasesOperatingSystem`,
  `AgentReleasesOsVersion`, `ChangeTrackingActorStitchedFields`,
  `ChangeTrackingChangeTrackingEvent`,
  `ChangeTrackingChangeTrackingSearchResult`,
  `ChangeTrackingCreateEventResponse`, `ChangeTrackingDeploymentEvent`,
  `ChangeTrackingFeatureFlagEvent`, `ChangeTrackingGenericEvent`,
  `CloudAwsMetadataGovIntegration`, `CloudAwsMsElasticacheGovIntegration`,
  `CloudAwsTagsGlobalGovIntegration`,
  `CloudConfluentKafkaConnectorResourceIntegration`,
  `CloudConfluentKafkaKsqlResourceIntegration`, `CloudSecurityHubIntegration`,
  `EntityManagementAiAgentEntity`, `EntityManagementAiAgentEntityCreateResult`,
  `EntityManagementAiAgentEntityUpdateResult`, `EntityManagementAiToolEntity`,
  `EntityManagementAiToolEntityCreateResult`,
  `EntityManagementAiToolEntityUpdateResult`,
  `EntityManagementAiToolParameter`, `EntityManagementConnectionReference`,
  `EntityManagementConnectionSettings`, `EntityManagementCount`,
  `EntityManagementExecutionIssue`, `EntityManagementGithubAppTokenCredential`,
  `EntityManagementGithubConnection`, `EntityManagementGithubCredentials`,
  `EntityManagementJiraBasicAuthCredential`, `EntityManagementJiraConnection`,
  `EntityManagementJiraCredentials`, `EntityManagementJiraOAuthCredential`,
  `EntityManagementJiraSyncConfiguration`, `EntityManagementLlmConfig`,
  `EntityManagementNewRelicBasicAuthCredential`,
  `EntityManagementNewRelicConnection`, `EntityManagementNotebookEntity`,
  `EntityManagementRuleExecutionStatus`, `EntityManagementSecretReference`,
  `EntityManagementTemplateField`, `EntityManagementWorkItem`,
  `EntityManagementWorkItemAssignment`, `EntityManagementWorkItemAttribute`,
  `EntityManagementWorkItemMessage`, `KnowledgeTag`, `KnowledgeTagsResponse`.
* Add `ALLOW_CUSTOM_CATEGORY_OR_TYPE` value to `ChangeTrackingValidationFlag`
  enum type.
* Add `SERVICENOW_TEAM` value to `EntityManagementTeamExternalIntegrationType`
  enum type.
* Add `ALL` value to `KnowledgeSearchSources` enum type.
* Add `disable_health_status_reporting` field to
  `AlertsNrqlConditionTermsInput` input type.
* Add `disable_health_status_reporting` field to
  `AlertsNrqlDynamicConditionTermsInput` input type.
* Add `security_hub` field to `CloudAwsDisableIntegrationsInput` input type.
* Add `aws_meta_data_gov`, `aws_ms_elasticache_gov` and `aws_tags_global_gov`
  fields to `CloudAwsGovcloudDisableIntegrationsInput` input type.
* Add `aws_metadata_gov`, `aws_ms_elasticache_gov` and `aws_tags_global_gov`
  fields to `CloudAwsGovcloudIntegrationsInput` input type.
* Add `security_hub` field to `CloudAwsIntegrationsInput` input type.
* Add `confluent_kafka_connector_resource` and `confluent_kafka_ksql_resource`
  fields to `CloudConfluentDisableIntegrationsInput` input type.
* Add `confluent_kafka_connector_resource` and `confluent_kafka_ksql_resource`
  fields to `CloudConfluentIntegrationsInput` input type.
* Add `disable_health_status_reporting` field to `AlertsNrqlTerms` interface
  type.
* Add `change_tracking` field to `Actor` object type.
* Add `supported_operating_systems` field to `AgentReleasesAgentRelease` object
  type.
* Add `count` and `installation_status` fields to
  `EntityManagementGitHubIntegrationEntity` object type.
* Add `last_execution_status` field to `EntityManagementScorecardRuleEntity`
  object type.
* Add `tags` field to `KnowledgeDocsStitchedFields` object type.
* Add `publish_status` and `tags` fields to `KnowledgeSearchResult` object type.
* Remove `ai_issues_mark_as_investigating` field from `RootMutationType` object
  type.
* Add `change_tracking_create_event`, `entity_management_create_ai_agent`,
  `entity_management_create_ai_tool`, `entity_management_update_ai_agent`, and
  `entity_management_update_ai_tool` fields to `RootMutationType` object type.

## [0.35.0] - 2025-05-23

* Add new enums: `ChangeTrackingCategoryType`,
  `EntityManagementAiToolParameterType`, `EntityManagementAssignmentType`,
  `EntityManagementCategory`, `EntityManagementConnectionType`,
  `EntityManagementDirection`, `EntityManagementEncodingType`,
  `EntityManagementExecutionStatus`, `EntityManagementInstallationStatus`,
  `EntityManagementJiraIssueType`, `EntityManagementKeyType`,
  `EntityManagementMessageType`, `EntityManagementPriority`,
  `EntityManagementSigningAlgorithm`, `EntityManagementStatusCode`,
  `EntityManagementSyncConfigurationMode`, `KnowledgePublishStatus`.
* Add new input types: `ChangeTrackingCategoryAndTypeInput`,
  `ChangeTrackingCategoryFieldsInput`, `ChangeTrackingCategoryRelatedInput`,
  `ChangeTrackingChangeTrackingSearchFilter`,
  `ChangeTrackingCreateEventInput`, `ChangeTrackingDeploymentFieldsInput`,
  `ChangeTrackingEntitySearchInput`, `ChangeTrackingFeatureFlagFieldsInput`,
  `CloudAwsMetadataGovIntegrationInput`,
  `CloudAwsMsElasticacheGovIntegrationInput`,
  `CloudAwsTagsGlobalGovIntegrationInput`,
  `CloudConfluentKafkaConnectorResourceIntegrationInput`,
  `CloudConfluentKafkaKsqlResourceIntegrationInput`,
  `CloudSecurityHubIntegrationInput`,
  `EntityManagementAiAgentEntityCreateInput`,
  `EntityManagementAiAgentEntityUpdateInput`,
  `EntityManagementAiToolEntityCreateInput`,
  `EntityManagementAiToolEntityUpdateInput`,
  `EntityManagementAiToolParameterCreateInput`,
  `EntityManagementAiToolParameterUpdateInput`,
  `EntityManagementLlmConfigCreateInput`,
  `EntityManagementLlmConfigUpdateInput`.
* Add new object types: `AgentReleasesOperatingSystem`,
  `AgentReleasesOsVersion`, `ChangeTrackingActorStitchedFields`,
  `ChangeTrackingChangeTrackingEvent`,
  `ChangeTrackingChangeTrackingSearchResult`,
  `ChangeTrackingCreateEventResponse`, `ChangeTrackingDeploymentEvent`,
  `ChangeTrackingFeatureFlagEvent`, `ChangeTrackingGenericEvent`,
  `CloudAwsMetadataGovIntegration`, `CloudAwsMsElasticacheGovIntegration`,
  `CloudAwsTagsGlobalGovIntegration`,
  `CloudConfluentKafkaConnectorResourceIntegration`,
  `CloudConfluentKafkaKsqlResourceIntegration`,
  `CloudSecurityHubIntegration`, `EntityManagementAiAgentEntity`,
  `EntityManagementAiAgentEntityCreateResult`,
  `EntityManagementAiAgentEntityUpdateResult`,
  `EntityManagementAiToolEntity`,
  `EntityManagementAiToolEntityCreateResult`,
  `EntityManagementAiToolEntityUpdateResult`,
  `EntityManagementAiToolParameter`, `EntityManagementConnectionReference`,
  `EntityManagementConnectionSettings`, `EntityManagementCount`,
  `EntityManagementExecutionIssue`, `EntityManagementGithubAppTokenCredential`,
  `EntityManagementGithubConnection`, `EntityManagementGithubCredentials`,
  `EntityManagementJiraBasicAuthCredential`, `EntityManagementJiraConnection`,
  `EntityManagementJiraCredentials`, `EntityManagementJiraOAuthCredential`,
  `EntityManagementJiraSyncConfiguration`, `EntityManagementLlmConfig`,
  `EntityManagementNewRelicBasicAuthCredential`,
  `EntityManagementNewRelicConnection`, `EntityManagementNotebookEntity`,
  `EntityManagementRuleExecutionStatus`, `EntityManagementSecretReference`,
  `EntityManagementTemplateField`, `EntityManagementWorkItem`,
  `EntityManagementWorkItemAssignment`, `EntityManagementWorkItemAttribute`,
  `EntityManagementWorkItemMessage`, `KnowledgeTag`,
  `KnowledgeTagsResponse`.
* Add new scalar: `ChangeTrackingRawCustomAttributesMap`.
* Add new fields and arguments to existing types, including support for change
  tracking, AI agent/tool management, and knowledge tags.
* Add new mutations: `change_tracking_create_event`,
  `entity_management_create_ai_agent`, `entity_management_create_ai_tool`,
  `entity_management_update_ai_agent`, `entity_management_update_ai_tool`.
* Add new fields to existing objects, such as `supported_operating_systems` to
  `AgentReleasesAgentRelease`, `change_tracking` to `Actor`, and
  `tags`/`publish_status` to knowledge search results.
* Remove the `ai_issues_mark_as_investigating` mutation from
  `RootMutationType`.

## [0.34.0] - 2025-04-28

* Add `EntityManagementFleetDeploymentPhase`, `EntityManagementRiskSeverity`,
  `EntityManagementSecurityFindingSubType`,
  `EntityManagementSecurityFindingType`, and
  `EntityManagementVulnerabilityStatus` enum types.
* Add `OPT_OUT` value to `AgentApplicationSettingsTracer` enum type.
* Add `FLUENTBIT`, `NRDOT`, `PIPELINE_CONTROL_GATEWAY`, and `PROMETHEUS`
  values to `AgentReleasesFilter` enum type.
* Add `INVESTIGATING` value to `AiWorkflowsNotificationTrigger` enum type.
* Add `CloudAwsAutoDiscoveryIntegrationInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionQueryInput` and
  `AlertsNrqlConditionUpdateQueryInput` input types.
* Add `aws_auto_discovery` field to `CloudAwsDisableIntegrationsInput` and
  `CloudAwsIntegrationsInput` input types.
* Add `metric_collection_mode` field to `CloudCciAwsLinkAccountInput` input
  type.
* Add `AlertsCrossAccountElectionStatus` and `AlertsCrossAccountParticipant`
  object types.
* Add `cross_account_election` and `cross_account_participants` fields to
  `AlertsAccountStitchedFields` object type.
* Add `EntityManagementAgentDeployment`, `EntityManagementBlobSignature`
  `EntityManagementCve`, `EntityManagementImpactedEntityReference`,
  `EntityManagementInfrastructureManager`,
  `EntityManagementManagedEntitiesRing`,
  `EntityManagementRingDeploymentTracker`,
  `EntityManagementSecurityFindingPackage`,
  `EntityManagementSecurityFindingRemediation`,
  `EntityManagementSignatureDetails`, `EntityManagementVulnerabilityUiUrls`,
  `EntityManagementFleetDeploymentEntity`, and
  `EntityManagementSecurityFindingEntity` object types.
* Add `applied_deployment` and `version` fields to
  `EntityManagementFleetControlProperties` object type.
* Add `infrastructure_managers` and `version` fields to
  `EntityManagementAgentEntity` object type.
* Add `managed_entities_rings` field to `EntityManagementFleetEntity` object
  type.
* Add `alerts_update_cross_account_election` and
  `alerts_update_cross_account_elections` fields to `RootMutationType` object
  type.
* Add `created_at` and `time_zone_name` fields to `User` object type.
* Add `CloudAwsAutoDiscoveryIntegration` object type.
* Remove `active_deployment`, `draft_deployment`, `in_progress_deployment`, and
  `proposed_deployment` fields from `EntityManagementFleetEntity` object type.
* Remove `entities` and `members` fields from `EntityManagementTeamEntity`
  object type.

## [0.33.0] - 2025-04-15

* Add `EntityManagementFleetDeploymentPhase`, `EntityManagementRiskSeverity`,
  `EntityManagementSecurityFindingSubType`,
  `EntityManagementSecurityFindingType` and
  `EntityManagementVulnerabilityStatus` enum types.
* Add `OPT_OUT` value to `AgentApplicationSettingsTracer` enum type.
* Add `FLUENTBIT`, `NRDOT`, `PIPELINE_CONTROL_GATEWAY` and `PROMETHEUS` values
  to `AgentReleasesFilter` enum type.
* Add `INVESTIGATING` value to `AiWorkflowsNotificationTrigger` enum type.
* Add `CloudAwsAutoDiscoveryIntegrationInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionQueryInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionUpdateQueryInput` input
  type.
* Add `aws_auto_discovery` field to `CloudAwsDisableIntegrationsInput` input
  type.
* Add `aws_auto_discovery` field to `CloudAwsIntegrationsInput` input type.
* Add `metric_collection_mode` field to `CloudCciAwsLinkAccountInput` input
  type.
* Add `AlertsCrossAccountElectionStatus`, `AlertsCrossAccountParticipant`,
  `EntityManagementAgentDeployment`, `EntityManagementBlobSignature`,
  `EntityManagementCve`, `EntityManagementImpactedEntityReference`,
  `EntityManagementInfrastructureManager`,
  `EntityManagementManagedEntitiesRing`,
  `EntityManagementRingDeploymentTracker`,
  `EntityManagementSecurityFindingPackage`,
  `EntityManagementSecurityFindingRemediation`,
  `EntityManagementSignatureDetails`, `EntityManagementVulnerabilityUiUrls`,
  `CloudAwsAutoDiscoveryIntegration`, `EntityManagementFleetDeploymentEntity`
  and `EntityManagementSecurityFindingEntity` object types.
* Add `cross_account_election` and `cross_account_participants` fields to
  `AlertsAccountStitchedFields` object type.
* Add `blob_signature` field to `EntityManagementBlob` object type.
* Add `applied_deployment` and `version` fields to
  `EntityManagementFleetControlProperties` object type.
* Add `alerts_update_cross_account_election` and
  `alerts_update_cross_account_elections` fields to `RootMutationType` object
  type.
* Add `created_at` and `time_zone_name` fields to `User` object type.
* Add `infrastructure_managers` and `version` fields to
  `EntityManagementAgentEntity` object type.
* Remove `active_deployment`, `draft_deployment` and `in_progress_deployment`
  fields from `EntityManagementFleetEntity` object type.
* Add `description` and `managed_entities_rings` fields to
  `EntityManagementFleetEntity` object type.
* Remove `entities` and `members` fields from `EntityManagementTeamEntity`
  object type.
* Add new `_get_variable_from_env` and `get_new_relic_account_id_from_env`,
  refactor `get_new_relic_user_key_from_env` using `_get_variable_from_env`.
* Add new `nrql` function, update retry logic in `perform_nrql_query`, deprecate
  `max_retry` in favor of `max_retries` in `perform_nrql_query`.
* Add Download notebook for utility functions for download files from
  historical data export.
* Add Dashboards notebook for shortcut functions related to dashboards
* Update rename `variable_values` to `variables` param in
  `_check_nrql_query_progress`,
* Add new Historical Data Export notebook for hsitorical data export operations.

## [0.32.0] - 2025-04-08

* Add `EntityManagementFleetDeploymentPhase`, `EntityManagementRiskSeverity`,
  `EntityManagementSecurityFindingSubType`,
  `EntityManagementSecurityFindingType` and
  `EntityManagementVulnerabilityStatus` enum types.
* Add `OPT_OUT` value to `AgentApplicationSettingsTracer` enum type.
* Add `FLUENTBIT`, `NRDOT`, `PIPELINE_CONTROL_GATEWAY` and `PROMETHEUS` values
  to `AgentReleasesFilter` enum type.
* Add `INVESTIGATING` value to `AiWorkflowsNotificationTrigger` enum type.
* Add `CloudAwsAutoDiscoveryIntegrationInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionQueryInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionUpdateQueryInput` input
  type.
* Add `aws_auto_discovery` field to `CloudAwsDisableIntegrationsInput` input
  type.
* Add `aws_auto_discovery` field to `CloudAwsIntegrationsInput` input type.
* Add `metric_collection_mode` field to `CloudCciAwsLinkAccountInput` input
  type.
* Add `AlertsCrossAccountElectionStatus`, `AlertsCrossAccountParticipant`,
  `EntityManagementAgentDeployment`, `EntityManagementBlobSignature`,
  `EntityManagementCve`, `EntityManagementImpactedEntityReference`,
  `EntityManagementInfrastructureManager`,
  `EntityManagementManagedEntitiesRing`,
  `EntityManagementRingDeploymentTracker`,
  `EntityManagementSecurityFindingPackage`,
  `EntityManagementSecurityFindingRemediation`,
  `EntityManagementSignatureDetails`, `EntityManagementVulnerabilityUiUrls`,
  `CloudAwsAutoDiscoveryIntegration`, `EntityManagementFleetDeploymentEntity`
  and `EntityManagementSecurityFindingEntity` object types.
* Add `cross_account_election` and `cross_account_participants` fields to
  `AlertsAccountStitchedFields` object type.
* Add `blob_signature` field to `EntityManagementBlob` object type.
* Add `applied_deployment` and `version` fields to
  `EntityManagementFleetControlProperties` object type.
* Add `alerts_update_cross_account_election` and
  `alerts_update_cross_account_elections` fields to `RootMutationType` object
  type.
* Add `created_at` and `time_zone_name` fields to `User` object type.
* Add `infrastructure_managers` and `version` fields to
  `EntityManagementAgentEntity` object type.
* Remove `active_deployment`, `draft_deployment` and `in_progress_deployment`
  fields from `EntityManagementFleetEntity` object type.
* Add `description` and `managed_entities_rings` fields to
  `EntityManagementFleetEntity` object type.
* Remove `entities` and `members` fields from `EntityManagementTeamEntity`
  object type.

## [0.31.0] - 2025-03-23

* Add `EntityManagementFleetDeploymentPhase`, `EntityManagementRiskSeverity`,
  `EntityManagementSecurityFindingSubType`,
  `EntityManagementSecurityFindingType` and
  `EntityManagementVulnerabilityStatus` enum types.
* Add `OPT_OUT` value to `AgentApplicationSettingsTracer` enum type.
* Add `FLUENTBIT`, `NRDOT`, `PIPELINE_CONTROL_GATEWAY` and `PROMETHEUS` values
  to `AgentReleasesFilter` enum type.
* Add `INVESTIGATING` value to `AiWorkflowsNotificationTrigger` enum type.
* Add `CloudAwsAutoDiscoveryIntegrationInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionQueryInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionUpdateQueryInput` object
  type.
* Add `aws_auto_discovery` field to `CloudAwsDisableIntegrationsInput` input
  type.
* Add `aws_auto_discovery` field to `CloudAwsIntegrationsInput` input
  type.
* Add `metric_collection_mode` field to `CloudCciAwsLinkAccountInput` input
  type.
* Add `AlertsCrossAccountElectionStatus`, `AlertsCrossAccountParticipant`,
  `EntityManagementAgentDeployment`, `EntityManagementBlobSignature`,
  `EntityManagementCve`, `EntityManagementImpactedEntityReference`,
  `EntityManagementInfrastructureManager`,
  `EntityManagementManagedEntitiesRing`,
  `EntityManagementRingDeploymentTracker`,
  `EntityManagementSecurityFindingPackage`,
  `EntityManagementSecurityFindingRemediation`,
  `EntityManagementSignatureDetails`, `EntityManagementVulnerabilityUiUrls`,
  `CloudAwsAutoDiscoveryIntegration`, `EntityManagementFleetDeploymentEntity`
  and `EntityManagementSecurityFindingEntity` object types.
* Add `cross_account_election` and `cross_account_participants` fields to
  `AlertsAccountStitchedFields` object type.
* Add `blob_signature` field to `EntityManagementBlob` object type.
* Add `applied_deployment` and `version` fields to
  `EntityManagementFleetControlProperties` object type.
* Add `alerts_update_cross_account_election` and
  `alerts_update_cross_account_elections` fields to `RootMutationType` object
  type.
* Add `created_at` and `time_zone_name` fields to `User` object type.
* Add `infrastructure_managers` and `version` fields to
  `EntityManagementAgentEntity` object type.
* Remove `active_deployment`, `draft_deployment` and `in_progress_deployment`
  fields from `EntityManagementFleetEntity` object type.
* Add `description` and `managed_entities_rings` fields to
  `EntityManagementFleetEntity` object type.
* Remove `entities` and `members` fields from `EntityManagementTeamEntity`
  object type.

## [0.30.0] - 2025-03-05

* Add `EntityManagementFleetDeploymentPhase`, `EntityManagementRiskSeverity`,
  `EntityManagementSecurityFindingSubType`,
  `EntityManagementSecurityFindingType` and
  `EntityManagementVulnerabilityStatus` enum types.
* Add `OPT_OUT` value to `AgentApplicationSettingsTracer` enum type.
* Add `FLUENTBIT`, `NRDOT`, `PIPELINE_CONTROL_GATEWAY` and `PROMETHEUS` values
  to `AgentReleasesFilter` enum type.
* Add `INVESTIGATING` value to `AiWorkflowsNotificationTrigger` enum type.
* Add `CloudAwsAutoDiscoveryIntegrationInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionQueryInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionUpdateQueryInput` object
  type.
* Add `aws_auto_discovery` field to `CloudAwsDisableIntegrationsInput` input
  type.
* Add `aws_auto_discovery` field to `CloudAwsIntegrationsInput` input
  type.
* Add `metric_collection_mode` field to `CloudCciAwsLinkAccountInput` input
  type.
* Add `AlertsCrossAccountElectionStatus`, `AlertsCrossAccountParticipant`,
  `EntityManagementAgentDeployment`, `EntityManagementBlobSignature`,
  `EntityManagementCve`, `EntityManagementImpactedEntityReference`,
  `EntityManagementInfrastructureManager`,
  `EntityManagementManagedEntitiesRing`,
  `EntityManagementRingDeploymentTracker`,
  `EntityManagementSecurityFindingPackage`,
  `EntityManagementSecurityFindingRemediation`,
  `EntityManagementSignatureDetails`, `EntityManagementVulnerabilityUiUrls`,
  `CloudAwsAutoDiscoveryIntegration`, `EntityManagementFleetDeploymentEntity`
  and `EntityManagementSecurityFindingEntity` object types.
* Add `cross_account_election` and `cross_account_participants` fields to
  `AlertsAccountStitchedFields` object type.
* Add `blob_signature` field to `EntityManagementBlob` object type.
* Add `applied_deployment` and `version` fields to
  `EntityManagementFleetControlProperties` object type.
* Add `alerts_update_cross_account_election` and
  `alerts_update_cross_account_elections` fields to `RootMutationType` object
  type.
* Add `created_at` and `time_zone_name` fields to `User` object type.
* Add `infrastructure_managers` and `version` fields to
  `EntityManagementAgentEntity` object type.
* Remove `active_deployment`, `draft_deployment` and `in_progress_deployment`
  fields from `EntityManagementFleetEntity` object type.
* Add `description` and `managed_entities_rings` fields to
  `EntityManagementFleetEntity` object type.
* Remove `entities` and `members` fields from `EntityManagementTeamEntity`
  object type.

## [0.29.0] - 2025-02-09

* Add `EntityManagementFleetDeploymentPhase`, `EntityManagementRiskSeverity`,
  `EntityManagementSecurityFindingSubType`,
  `EntityManagementSecurityFindingType` and
  `EntityManagementVulnerabilityStatus` enum types.
* Add `OPT_OUT` value to `AgentApplicationSettingsTracer` enum type.
* Add `FLUENTBIT`, `NRDOT`, `PIPELINE_CONTROL_GATEWAY` and `PROMETHEUS` values
  to `AgentReleasesFilter` enum type.
* Add `INVESTIGATING` value to `AiWorkflowsNotificationTrigger` enum type.
* Add `CloudAwsAutoDiscoveryIntegrationInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionQueryInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionUpdateQueryInput` object
  type.
* Add `aws_auto_discovery` field to `CloudAwsDisableIntegrationsInput` input
  type.
* Add `aws_auto_discovery` field to `CloudAwsIntegrationsInput` input
  type.
* Add `metric_collection_mode` field to `CloudCciAwsLinkAccountInput` input
  type.
* Add `AlertsCrossAccountElectionStatus`, `AlertsCrossAccountParticipant`,
  `EntityManagementAgentDeployment`, `EntityManagementBlobSignature`,
  `EntityManagementCve`, `EntityManagementImpactedEntityReference`,
  `EntityManagementInfrastructureManager`,
  `EntityManagementManagedEntitiesRing`,
  `EntityManagementRingDeploymentTracker`,
  `EntityManagementSecurityFindingPackage`,
  `EntityManagementSecurityFindingRemediation`,
  `EntityManagementSignatureDetails`, `EntityManagementVulnerabilityUiUrls`,
  `CloudAwsAutoDiscoveryIntegration`, `EntityManagementFleetDeploymentEntity`
  and `EntityManagementSecurityFindingEntity` object types.
* Add `cross_account_election` and `cross_account_participants` fields to
  `AlertsAccountStitchedFields` object type.
* Add `blob_signature` field to `EntityManagementBlob` object type.
* Add `applied_deployment` and `version` fields to
  `EntityManagementFleetControlProperties` object type.
* Add `alerts_update_cross_account_election` and
  `alerts_update_cross_account_elections` fields to `RootMutationType` object
  type.
* Add `created_at` and `time_zone_name` fields to `User` object type.
* Add `infrastructure_managers` and `version` fields to
  `EntityManagementAgentEntity` object type.
* Remove `active_deployment`, `draft_deployment` and `in_progress_deployment`
  fields from `EntityManagementFleetEntity` object type.
* Add `description` and `managed_entities_rings` fields to
  `EntityManagementFleetEntity` object type.
* Remove `entities` and `members` fields from `EntityManagementTeamEntity`
  object type.

## [0.28.0] - 2025-01-18

* Add `EntityManagementFleetDeploymentPhase`, `EntityManagementRiskSeverity`,
  `EntityManagementSecurityFindingSubType`,
  `EntityManagementSecurityFindingType` and
  `EntityManagementVulnerabilityStatus` enum types.
* Add `OPT_OUT` value to `AgentApplicationSettingsTracer` enum type.
* Add `FLUENTBIT`, `NRDOT`, `PIPELINE_CONTROL_GATEWAY` and `PROMETHEUS` values
  to `AgentReleasesFilter` enum type.
* Add `INVESTIGATING` value to `AiWorkflowsNotificationTrigger` enum type.
* Add `CloudAwsAutoDiscoveryIntegrationInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionQueryInput` input type.
* Add `data_account_id` field to `AlertsNrqlConditionUpdateQueryInput` object
  type.
* Add `aws_auto_discovery` field to `CloudAwsDisableIntegrationsInput` input
  type.
* Add `aws_auto_discovery` field to `CloudAwsIntegrationsInput` input
  type.
* Add `metric_collection_mode` field to `CloudCciAwsLinkAccountInput` input
  type.
* Add `AlertsCrossAccountElectionStatus`, `AlertsCrossAccountParticipant`,
  `EntityManagementAgentDeployment`, `EntityManagementBlobSignature`,
  `EntityManagementCve`, `EntityManagementImpactedEntityReference`,
  `EntityManagementInfrastructureManager`,
  `EntityManagementManagedEntitiesRing`,
  `EntityManagementRingDeploymentTracker`,
  `EntityManagementSecurityFindingPackage`,
  `EntityManagementSecurityFindingRemediation`,
  `EntityManagementSignatureDetails`, `EntityManagementVulnerabilityUiUrls`,
  `CloudAwsAutoDiscoveryIntegration`, `EntityManagementFleetDeploymentEntity`
  and `EntityManagementSecurityFindingEntity` object types.
* Add `cross_account_election_status` and `cross_account_participants` field to
  `AlertsAccountStitchedFields` object type.
* Add `blob_signature` field to `EntityManagementBlob` object type.
* Add `applied_deployment` and `version` fields to
  `EntityManagementFleetControlProperties` object type.
* Add `alerts_update_cross_account_election` and
  `alerts_update_cross_account_elections` fields to `RootMutationType` object
  type.
* Add `created_at` and `time_zone_name` field to `User` object type.
* Add `infrastructure_managers` and `version` fields to
  `EntityManagementAgentEntity` object type.
* Remove `active_deployment`, `draft_deployment` and `in_progress_deployment`
  fields from `EntityManagementFleetEntity` object type.
* Add `description` and `managed_entities_rings` fields to
  `EntityManagementFleetEntity` object type.
* Remove fields `entities` and `members` from `EntityManagementTeamEntity`
  object type.

## [0.27.0] - 2024-12-31

* Add `NrqlCancelQueryMutationRequestStatus` enum type.
* Add `MARK_AS_INVESTIGATING` value to `AiIssuesIssueUserAction` enum type.
* Add `CloudCciAwsDisableIntegrationsInput`, `CloudCciAwsIntegrationsInput`,
  `CloudCciAwsLinkAccountInput`, `CloudCciAwsS3IntegrationInput` input types.
* Add `cci_aws` field to `CloudDisableIntegrationsInput` input type.
* Add `cci_aws` field to `CloudIntegrationsInput` input type.
* Add `cci_aws` field to `CloudLinkCloudAccountsInput` input type.
* Add `NrqlCancelQueryMutationResponse`, `OrganizationNrdbResultContainer`,
  `CloudCciAwsS3Integration`, `NrqlCancelQueryMutationRequestStatus` object
  types.
* Add `investigated_at` and `investigated_by` fields to `AiIssuesIssue` object
  type.
* Add `ai_issues_mark_as_investigating` and `nrql_cancel_query` fields to
  `OrganizationOrganizationAdministrator` object type.

## [0.26.0] - 2024-12-16

* Add `BYPASS_CALLS` value to `EntityRelationshipEdgeType` enum type.
* Add `scope` field to `MultiTenantAuthorizationPermissionFilter` input type.
* Add `MultiTenantAuthorizationPermissionFilterScopeInput` input type.
* Remove `EntityManagementAgentDeployment` object type.
* Remove `current_deployment` field from
  `EntityManagementFleetControlProperties` object type.
* Add `storage_account_id` field to `Organization` object type.
* Add `storage_account_id` field to `OrganizationCustomerOrganization` object
  type.

## [0.25.0] - 2024-12-07

* Fix tests
* Use pytest-vcr with tests
* Update devops scripts
* Update GraphQL submodule with a fresh schema version.
* Add `MICROSOFT_TEAMS` value to `AiWorkflowsDestinationType` enum type.
* Add `GITHUB_TEAM` value to `EntityManagementTeamExternalIntegrationType`
  enum type.
* Add `AuthorizationManagementEntity`,
  `AuthorizationManagementEntityAccessGrants` input types.
* Add `entity_access_grants` field to `AuthorizationManagementGrantAccess`
  object type.
* Add `EntityManagementUserMetadata`,
  `EntityManagementPipelineCloudRuleEntity` object type.
* Update `forwarding`, `local_decorating` and `metrics` fields in
  `AgentApplicationSettingsApplicationLogging` type to be `non null`.
* Allow null values for `enabled` and `max_samples_stored` fields in
  `AgentApplicationSettingsMetrics` type.
* Allow null values for `enabled` field in
  `AgentApplicationSettingsLocalDecorating` type.
* Add `canary_managed_entities`, `managed_entities_changed`,
  `managed_entities_required_to_change`, `supervised_agent_entities_changed`,
  `supervised_agent_entities_required_to_change` fields to
  `EntityManagementFleetDeployment` type.
* Add `active_deployment`, `draft_deployment`, `in_progress_deployment` and
  `proposed_deployment` field to `EntityManagementFleetEntity` type.

## [0.24.0] - 2024-12-03

* Update development dependencies.
* Update GraphQL submodule with a fresh schema version.
* Add logger settings.
* Add poethepoet as task runner.
* Add `KUBERNETES` value to `AgentReleasesFilter` enum type.
* Add `Nrql` to `shortcuts` submodule.

## [0.23.0] - 2024-11-23

* Fix references to github in the documentation.
* Replace `|` with `Union` to avoid breaks with python versions earlier than
  3.10
* Delete unused submodules Core, Dashboards adn Alerts
* Add support for `Operation` type in `query` agument from
  `NewRelicGqlClient.execute`.
* Update GraphQL submodule with a fresh schema version.
* Add `MICROSOFT_TEAMS` value to `AiNotificationsChannelType` enum type.
* Add `MICROSOFT_TEAMS` value to `AiNotificationsDestinationType` enum type.
* Add `AlertsNrqlTerms` object type.
* `AlertsNrqlConditionTerms` inherits from `AlertsNrqlTerms` object type.
* Add `AlertsNrqlConditionTermsWithForecast` inherits from `AlertsNrqlTerms`
  object type.
* Add `typev2` field to `MultiTenantAuthorizationGrantScope` object type.

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
