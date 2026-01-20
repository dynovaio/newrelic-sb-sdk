# New Relic SB SDK

**Automate your SRE tasks with ease using the New Relic SB SDK.**

![Community-Project][repository:banner]

![PyPI - Supported versions][pypi:badge:python]
![PyPI - Package version][pypi:badge:version]
![PyPI - Downloads][pypi:badge:downloads]
![PyPI - License][pypi:badge:license]
[![Codacy Grade Badge][codacy:grade]][codacy:dashboard]
[![Codacy Coverage Badge][codacy:coverage]][codacy:dashboard]
[![Gitlab Pipeline Status][repository:pipeline]][repository:commits]

This library provides a robust, typed Python client for the New Relic NerdGraph
API, built on top of `sgqlc`. It simplifies the process of querying and
mutating New Relic data, making it easier to build automation tools, monitoring
scripts, and custom dashboards.

## ✨ Features

- **Typed Interactions**: Leveraging `sgqlc` for type-safe GraphQL queries.
- **Easy Configuration**: Simple setup with environment variables or direct
  initialization.
- **Comprehensive Coverage**: Designed to support key SRE workflows.
- **Modern Stack**: Built with Python 3.10+ and modern tooling.

## 📋 Requirements

- Python 3.10.0 or higher

## 📦 Installation

### Using pip

```bash
pip install newrelic-sb-sdk
```

### Using uv

```bash
uv add newrelic-sb-sdk
```

## 🚀 Usage

Here is a simple example of how to use the `NewRelicGqlClient` to query the
current user's information from New Relic.

```python
import os
from newrelic_sb_sdk.client import NewRelicGqlClient
from sgqlc.operation import Operation

# Initialize the client
# Ensure NEW_RELIC_USER_KEY is set in your environment or pass it directly
client = NewRelicGqlClient(new_relic_user_key=os.getenv("NEW_RELIC_USER_KEY"))

# Create an operation based on the New Relic schema
op = Operation(client.schema.query_type)

# Select fields to query
op.actor.user.__fields__(
    "name",
    "email",
    "id"
)

# Execute the query
response = client.execute(op)

# Access the data as native Python objects
data = op + response.json()
user = data.actor.user

print(f"User: {user.name} <{user.email}> (ID: {user.id})")
```

For more advanced usage and examples, check out our [Documentation][repository]
and [Playground][repository:playground].

## 🛠️ Development

We welcome contributions! Please see our [Contribution Guide](./CONTRIBUTING.md)
for details on setting up your development environment, running tests, and
submitting pull requests.

The project uses `uv` for dependency management and `ruff` for linting.

## 📜 Changelog

See the [CHANGELOG.md](./CHANGELOG.md) for a history of changes.

## 👥 Contributors

See our [list of contributors][repository:contributors].

## 📄 License

This project is licensed under the Apache License 2.0. See the
[LICENSE.txt](./LICENSE.txt) file for details.

[repository]: https://gitlab.com/softbutterfly/open-source/newrelic-sb-sdk
[repository:banner]: https://gitlab.com/softbutterfly/open-source/open-source-office/-/raw/master/assets/dynova/dynova-open-source--banner--community-project.png
[repository:playground]: https://gitlab.com/softbutterfly/open-source/newrelic-sb-sdk-playground
[repository:pipeline]: https://gitlab.com/softbutterfly/open-source/newrelic-sb-sdk/badges/master/pipeline.svg
[repository:commits]: https://gitlab.com/softbutterfly/open-source/newrelic-sb-sdk/-/commits/master
[repository:contributors]: https://gitlab.com/softbutterfly/open-source/newrelic-sb-sdk/-/graphs/master

[pypi:badge:python]: https://img.shields.io/pypi/pyversions/newrelic-sb-sdk
[pypi:badge:version]: https://img.shields.io/pypi/v/newrelic-sb-sdk
[pypi:badge:downloads]: https://img.shields.io/pypi/dm/newrelic-sb-sdk
[pypi:badge:license]: https://img.shields.io/pypi/l/newrelic-sb-sdk

[codacy:grade]: https://app.codacy.com/project/badge/Grade/1c25dec51e1c4a719be4c2d4ebe7eef6
[codacy:coverage]: https://app.codacy.com/project/badge/Coverage/1c25dec51e1c4a719be4c2d4ebe7eef6
[codacy:dashboard]: https://app.codacy.com/gl/softbutterfly/newrelic-sb-sdk/dashboard
