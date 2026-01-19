#! /bin/sh
BASE_DIR="$( cd "$( dirname "$0" )" > /dev/null 2>&1 && pwd )"

. "$BASE_DIR/setup_variables.sh"
echo "JB_ALLOW_NODEENV: $JB_ALLOW_NODEENV"
echo "SoftButterfly CI: Build docs for version ${CI_COMMIT_TAG}"

echo "* Building docs"
uv run jupyter book build --html --ci
