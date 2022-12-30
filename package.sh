#!/bin/sh

# Package the java-code-quality library into a zip file and save it in the parent directory
# of java-code-quality.

# Note: this MUST be run from within the java-code-quality directory.

version=$(cat data/version)
path=$(readlink -f ../java-code-quality-$version.zip)

echo "Preparing zip file..."

if [[ -e $path ]];
then
    rm -rf $path
fi

mkdir java-code-quality/
cp -r data/ java-code-quality/
cp -r cli/ java-code-quality/
cp install.sh java-code-quality/

zip -rq $path java-code-quality/

rm -r java-code-quality/

echo -e "Packaged to $path"
