# AGENTS.md - New Relic SB SDK

## Project Overview

**New Relic SB SDK** is a robust, typed Python client for the New Relic NerdGraph API, built on top of `sgqlc`. It simplifies querying and mutating New Relic data, making it ideal for automation, monitoring, and custom dashboards.

### Architecture

- **nbdev Philosophy**: This project uses `nbdev`. The source of truth for the codebase is the Jupyter Notebooks located in the `notebooks/` directory. The Python package in `src/newrelic_sb_sdk/` is automatically generated from these notebooks.
- **Core Technology Stack**:
  - **Python**: 3.10+
  - **GraphQL Client**: `sgqlc` (Simple GraphQL Client)
  - **Package Management**: `uv`
  - **Code Generation/Docs**: `nbdev`
  - **Task Runner**: `poethepoet` (aliased as `poe`)
  - **Linting/Formatting**: `ruff` and `pre-commit`
  - **Testing**: `pytest` and `tox`

## Building and Running

The project uses `uv` and `poe` (Poe the Poet) for task management.

### Essential Commands

- **Install Dependencies**: `uv sync --all-groups`
- **Linting**: `uv run poe lint`
- **Testing**: `uv run poe test` (runs pytest with coverage)
- **Code Generation (Notebooks to Source)**: `uv run poe package:update` (exports code from `notebooks/` to `src/`)
- **Schema Update**: `uv run poe schema:update` (executes `notebooks/Generator/NerdGraph Schema to Notebooks.ipynb`)
- **Version Management**: `uv run tbump [version]`

## Development Conventions

### Generator Notebook

The notebook `notebooks/Generator/NerdGraph Schema to Notebooks.ipynb` is used to generate the notebooks inside `notebooks/GraphQL/` based on the New Relic GraphQL schema.

### nbdev Workflow

1. **Modify Notebooks**: Always make changes in the `.ipynb` files within the `notebooks/` directory.
1. **Export Code**: Run `uv run poe package:update` to synchronize the changes to the `src/` directory.
1. **DO NOT Edit `src/` directly**: Any changes made directly in `src/` will be overwritten the next time notebooks are exported.

### Coding Style

- Follows **Google Style Guide** for docstrings (configured via `ruff`).
- **Formatting**: Handled by `ruff` (88 line length).
- **Type Safety**: Heavily leverages `sgqlc` for typed GraphQL interactions.

### Testing

- Tests are also typically defined in notebooks or in the `tests/` directory.
- Use `uv run poe test` for a full test suite run with coverage reporting.
- VCR is used for mocking API responses (see `tests/cassettes/`).

### Versioning

- Uses `tbump` for consistent version updates across multiple files (`pyproject.toml`, `settings.ini`, etc.).
- Follows Semantic Versioning.
