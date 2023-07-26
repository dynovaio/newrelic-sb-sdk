# Changelog

## [Unreleased]

## [0.11.0] - 2023-07-26

* Update GraphQL submodule with a fresh schema version.
* Update AiNotificationsChannelType, AiNotificationsDestinationType, AiWorkflowsDestinationType and AiNotificationsProduct values.
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

* Rename arguments in NewRelicGqlClient.build_query method and build_query function from `query_params` to `params` and  `query_string` to `template`.
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

* Replace pipe operator by Union in types annotations to ensure compatibility with python 3.8.1 and higer.

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
