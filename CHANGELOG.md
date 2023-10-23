# Changelog

## [Unreleased]

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
