#! /bin/sh
BASE_DIR="$( cd "$( dirname "$0" )" > /dev/null 2>&1 && pwd )"

. "$BASE_DIR/setup_variables.sh"

echo "SoftButterfly CI: Install dependencies"

echo "* UV install python"
uv python install "$(cat .python-version)"

echo "* UV install dependencies"
uv sync
