#!/bin/sh

# This script installs the java-code-quality package
# to a Debian system. It is intended to be installed
# on Eastern University's 'numbers' server, but it
# may work elsewhere.

# After downloading the latest release from the
# repository, extract the zip and execute this script
# as the superuser with the following commands:

# chmod a+x install.sh
# ./install.sh

# ==============================

echo "Uninstalling old version..."
rm /bin/format
rm /bin/lint
rm -r /opt/java-code-quality

echo "Installing..."
cp cli/* /bin/
chmod a+x /bin/format
chmod a+x /bin/lint

mkdir /opt/java-code-quality/
cp data/* /opt/java-code-quality/

echo "Successfully installed java-code-quality"
