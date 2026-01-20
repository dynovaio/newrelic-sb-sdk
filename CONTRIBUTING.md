# How to contribute to this project

> If you are interested in contributing to the development and maintenance of
> this package, it is recommended that you use [uv](https://github.com/astral-sh/uv)
> for dependency and python version management.

## 🌍 Environment

Clone the project

```bash
git clone https://gitlab.com/softbutterfly/open-source/newrelic-sb-sdk.git
cd newrelic-sb-sdk
```

Install the required python versions

```bash
uv python install $(cat .python-version)
```

Install the dependencies

```bash
uv sync --all-groups
```

## 🧪 Testing and coverage

You can run the tests with uv

```bash
uv run pytest \
    --cov newrelic_sb_sdk \
    --cov-report xml:cobertura.xml \
    --cov-report term  \
    --junitxml report.xml

uv run coverage report
```

In case you want to run the tests in all versions you can use [`tox`](https://tox.readthedocs.io/en/latest/)

## 🚀 Do you want to send a PR?

Before making your first commit and submitting your pull request, run

```bash
uv run pre-commit install
```

Then do your commits on a regular basis.

## 🤝 Code of Conduct

> Please note that this project is published with a Code of Conduct for
> collaborators. By participating in this project, you agree to abide by its
> terms.
