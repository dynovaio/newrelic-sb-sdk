#! /bin/sh
BASE_DIR="$( cd "$( dirname "$0" )" > /dev/null 2>&1 && pwd )"

. "$BASE_DIR/setup_variables.sh"

echo "SoftButterfly CI: Install dependencies for docs"

echo "* Update system packages"
apt-get update

echo "* Install system dependencies"
apt-get install -y curl default-jre rsync

echo "* Install NodeJS"
curl -fsSL "https://deb.nodesource.com/setup_${NODE_VERSION%%.*}.x" | bash -
apt-get install -y nodejs

echo "* Verify NodeJS installation"
node --version
npm --version
