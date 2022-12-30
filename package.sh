#!/bin/sh

# Package the java-code-quality library into a zip file and save it in the parent directory
# of java-code-quality.

# Note: this MUST be run from within the java-code-quality directory.

version=$(cat data/version)
path=$(readlink -f ../java-code-quality-$version.zip)

zip -rq $path data/* cli/* install.sh

echo -e "Packaged to $path"
