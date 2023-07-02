#! /bin/sh
FILE_NAME="$(basename "$0" 2> /dev/null)"
BASE_DIR="$( cd "$( dirname "$0" )" >/dev/null 2>&1 && pwd )"

. $BASE_DIR/setup_variables.sh

echo "SoftButterfly CI: Install dependencies"

echo "* Poetry install dependencies"
/opt/poetry/bin/poetry install
