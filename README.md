# java-code-quality

This library manages the formatter and linter CLI for Java on numbers. It allows students to format their code according to Google's [Java style guide](https://google.github.io/styleguide/javaguide.html).

## Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Formatter](#formatter)
4. [Linter](#linter)
5. [Updating](#updating)
   1. [google-java-format](#google-java-format)
   2. [Checkstyle](#checkstyle)
   3. [Checkstyle Google configuration](#checkstyle-google-configuration)
6. [Release New Version](#releasing-new-versions)
7. [Format Checker](#format-checker)
8. [Credits](#credits)

## Introduction

The purpose of this library is to help students understand the importance of code style. It shows them how to properly format Java code, and teaches them to lint their code to identify a variety of infelicities.

## Installation

Installing the latest version of `java-code-quality` simply requires downloading the latest release and running the `install.sh` file with `bash`. Any previous versions are automatically removed by the installer.

Note that the [format checker](#format-checker) script depends on a Python3 and pip installation. The installation script will attempt to globally install a package with `pip3`. If this script is not necessary, any errors pertaining to this step may be safely ignored.

The latest version may be installed with the following steps:

1. Download the `zip` file from the [latest release](https://github.com/EasternUniversity/java-code-quality/releases/latest).

2. Transfer the `zip` file to the server where it will be installed.

3. In a terminal, unzip the file using the following command:

```sh
unzip java-code-quality-x.y.z.zip
```

4. Enter the new `java-code-quality` directory:

```sh
cd java-code-quality
```

5. Make the `install.sh` file executable, and then run it as the superuser:

```sh
sudo bash install.sh
```

6. You may now safely delete the `java-code-quality` directory and the `zip` file. The latest version has been installed.

## Formatter

Eastern University defaults to Google's [style guide](https://google.github.io/styleguide/javaguide.html) for Java with the exception of using four-space indentation.

Google provides a [Java program](https://github.com/google/google-java-format) that automatically formats a given Java file to their standards. (When run with the `--aosp` flag, it uses four-space indentation).

Since this script requires a number of flags to account for, among other things, modern Java versions and the indentation exception, it is encased in a custom `format` command added to numbers. Students can thus format their code with the following command:

```
format [file]
```

## Linter

Linting of Java files is done through [Checkstyle](https://checkstyle.org/). From their website:

> Checkstyle is a development tool to help programmers write Java code that adheres to a coding standard. It automates the process of checking Java code to spare humans of this boring (but important) task. This makes it ideal for projects that want to enforce a coding standard.

Checkstyle [supports](https://checkstyle.org/google_style.html) Google's style guide through the use of a custom [configuration file](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml).

Similar to Google's formatter, Checkstyle is packaged in a `jar` file that can be manually executed on student's code. Again, to avoid having students memorize a series of flags to run Checkstyle, it is packaged in the custom `lint` command added to numbers. Students can thus lint their code with the following command:

```
lint [file]
```

## Updating

The following versions of the formatter and linter are currently in use:

- [google-java-format](https://github.com/google/google-java-format): 1.15.0
- [Checkstyle](https://github.com/checkstyle/checkstyle): 10.5.0
- [Checkstyle Google configuration](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml): Last updated 2022-12-30

To update these files, simply download them from the links below and overwrite the current versions in the [data](data) directory. Make sure to name them appropriately.

### google-java-format

Download from the GitHub repo [releases page](https://github.com/google/google-java-format/releases/tag/v1.15.0). Make sure to get the "all-deps" version.

Remove the version number from the file name to allow the `format` command to identify it. Name it `google-java-format-all-deps.jar`.

### Checkstyle

Download from the GitHub repo [releases page](https://github.com/checkstyle/checkstyle/releases).

Remove the version number from the file name to allow the `lint` command to identify it. Name it `checkstyle.jar`.

### Checkstyle Google configuration

The [`google_checks.xml`](data/google_checks.xml) file was originally [downloaded](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) from the Checkstyle GitHub repository, as linked from the [Google support page](https://checkstyle.org/google_style.html). At the time of download, it was last updated 2022-08-15.

However, this file has since underwent significant modification to reflect the style conventions used at Eastern University. Therefore, it is inappropriate to simply download an updated version and replace the current copy.

Instead, see the [style guide changes](docs/style_guide_changes.md) document for detailed information about what elements of the `xml` were changed and why. In the event that updates are pushed to the source file in Checkstyle's repository, those changes should be individually applied to the local `google_checks.xml` file with appropriate documentation in the style guide changes document.

## Releasing New Versions

After updating one or more of the above dependencies (or anything else in this library), complete the following steps in order:

1.  Update the [version number](data/version) according to [semantic versioning](https://semver.org/). Note that dependency updates are considered minor changes.

2.  Commit all changes to GitHub.

3.  Next, run the [`package.sh`](package.sh) script to create a zip package with the following commands:

_Note: You must run the script from within its parent directory._

```sh
cd java-code-quality/
bash package.sh
```

4. Upload the created zip file to GitHub as a new release.

5. [Install](#installation) the new package on numbers.

## Format Checker

This library also comes with another utility, [`format_checker.py`](/format-checker/format-checker.py). This is a Python script that can validate the formatting of student code.

It works by making a temporary copy of the student's code and [formatting](#formatter) the copy. Then, the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between the unformatted and formatted code is calculated. Finally, a grade between 0 and 1 is output based on the number of changes the formatter made to the code, as indicated by the Levenshtein distance.

This script accepts any number of files or directories as parameters. Directories are indexed and all .java files are tested. When testing multiple files, the total Levenshtein distance for all files is computed, and the grade is assigned based on this number as it would be for a single file.

The script is automatically installed in the `java-code-quality` directory by the [installer](#installation). Note that it requires the [`python-Levenshtein`](https://pypi.org/project/python-Levenshtein/) package, which is automatically installed **globally** using `pip3`.

To call the script on `Foobar.java`, use the following command:

```sh
python3 /opt/java-code-quality/format-checker.py Foobar.java
```

## Credits

Created by: Simon Kwilinski

Last updated: 2022-12-30
