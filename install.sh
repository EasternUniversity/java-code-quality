#!/bin/sh

# This script installs the java-code-quality package
# to a Debian system. It is intended to be installed
# on Eastern University's 'numbers' server, but it
# may work elsewhere.

# After downloading the latest release from the
# repository, extract the zip and execute this script
# as the superuser with the following commands:

# sudo bash install.sh

# ==============================

remove_if_exists() {
    if [[ -e $1 ]];
    then
        rm -rf $1
    fi
}

echo "Uninstalling old version..."

remove_if_exists /bin/format
remove_if_exists /bin/lint
remove_if_exists /opt/java-code-quality

echo "Installing..."
cp cli/* /bin/
chmod a+x /bin/format
chmod a+x /bin/lint

dir=/opt/java-code-quality/
mkdir $dir
cp -r data/* $dir
cp format-checker.py $dir

echo "Installing python Levenshtein..."

pip3 install levenshtein

echo "Successfully installed java-code-quality"
