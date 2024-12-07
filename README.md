![Community-Project](https://gitlab.com/softbutterfly/open-source/open-source-office/-/raw/master/assets/dynova/dynova-open-source--banner--community-project.png)

![PyPI - Supported versions](https://img.shields.io/pypi/pyversions/newrelic-sb-sdk)
![PyPI - Package version](https://img.shields.io/pypi/v/newrelic-sb-sdk)
![PyPI - Downloads](https://img.shields.io/pypi/dm/newrelic-sb-sdk)
![PyPI - MIT License](https://img.shields.io/pypi/l/newrelic-sb-sdk)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1c25dec51e1c4a719be4c2d4ebe7eef6)](https://app.codacy.com/gl/softbutterfly/newrelic-sb-sdk/dashboard?utm_source=gl&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/1c25dec51e1c4a719be4c2d4ebe7eef6)](https://app.codacy.com/gl/softbutterfly/newrelic-sb-sdk/dashboard?utm_source=gl&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)
[![pipeline status](https://gitlab.com/softbutterfly/open-source/newrelic-sb-sdk/badges/master/pipeline.svg)](https://gitlab.com/softbutterfly/open-source/newrelic-sb-sdk/-/commits/master)

# New Relic SB SDK

New Relic SDK built by Dynova to automate common SRE tasks with New Relic API.

## Requirements

* Python 3.9.0 or higher

## Install

Install from PyPI

```bash
pip install newrelic-sb-sdk
```

## Usage

There is an example on how to use this module to make a simple requesto to New
Relic GraphQL API.

```python
from newrelic_sb_sdk.client import NewRelicGqlClient
from newrelic_sb_sdk.utils.response import print_response
from newrelic_sb_sdk.graphql import nerdgraph
from newrelic_sb_sdk.graphql.objects import RootQueryType, RootMutationType

from sgqlc.operation import Operation

nerdgraph.query_type = RootQueryType
nerdgraph.mutation_type = RootMutationType

newrelic = NewRelicGqlClient(new_relic_user_key=YOUR_NEW_RELIC_USER_KEY)

operation = Operation(nerdgraph.query_type)
operation.actor.user()

response = newrelic.execute(operation)

print_response(response)

# Output
# {
#     "data": {
#         "actor": {
#             "user": {
#                 "email": "admin@example.com",
#                 "id": 1234567890,
#                 "name": "Admin User",
#             }
#         }
#     }
# }
```

## Docs

* [Documentación](https://dynovaio.github.io/newrelic-sb-sdk)
* [Ejemplos](https://gitlab.com/softbutterfly/open-source/newrelic-playground)

## Changelog

All changes to versions of this library are listed in the [change history](./CHANGELOG.md).

## Development

Check out our [contribution guide](./CONTRIBUTING.md).

## Contributors

See the list of contributors [here](https://github.com/dynovaio/newrelic-sb-sdk/graphs/contributors).

## License

This project is licensed under the terms of the MIT license. See the
<a href="./LICENSE.txt" download>LICENSE</a> file.
