#! /bin/sh
echo "SoftButterfly CI: Setup global variables"

export UV_INSTALL_DIR="/opt/uv"
export UV_CACHE_DIR="$CI_PROJECT_DIR/.cache/uv"
export UV_PYTHON_BIN_DIR="$UV_INSTALL_DIR"
export JB_ALLOW_NODEENV="yes"
export BASE_URL="${JB_BASE_URL}"
export NODE_VERSION="${JB_NODE_VERSION}"
export NODE_OPTIONS="${JB_NODE_OPTIONS}"

if ! command -v uv > /dev/null 2>&1 ; then
    export PATH="$UV_INSTALL_DIR:$PATH"
fi

for line in $(env | grep DOTENV_); do
    echo "${line#DOTENV_}" >> .env;
done
