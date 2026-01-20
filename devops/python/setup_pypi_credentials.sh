#! /bin/sh
BASE_DIR="$( cd "$( dirname "$0" )" > /dev/null 2>&1 && pwd )"

. "$BASE_DIR/setup_variables.sh"

echo "SoftButterfly CI: Setting up Pypi credentials"

echo "* Setting up credentials"
# echo "$PYPI_TOKEN" | uv auth login pypi.org --username __token__ --password -
