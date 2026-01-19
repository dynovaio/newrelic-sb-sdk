#! /bin/sh
BASE_DIR="$( cd "$( dirname "$0" )" > /dev/null 2>&1 && pwd )"

. "$BASE_DIR/setup_variables.sh"

echo "SoftButterfly CI: Tox for environment ${CI_JOB_NAME##*:}"

if [ -n "$TOX_ENVS" ]; then
    echo "* Pytest execution with tox"
    uv run tox -e "$TOX_ENVS"
else
    echo "* Pytest execution with UV"
    uv run pytest --cov="$PACKAGE_NAME" --cov-report xml:cobertura.xml --cov-report term --vcr-record=none
fi
