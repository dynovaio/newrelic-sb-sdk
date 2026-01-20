#! /bin/sh
BASE_DIR="$( cd "$( dirname "$0" )" > /dev/null 2>&1 && pwd )"

. "$BASE_DIR/setup_variables.sh"

echo "SoftButterfly CI: Install UV"

echo "* Install UV"
curl -LsSf https://astral.sh/uv/install.sh | sh
