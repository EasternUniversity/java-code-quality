# java-code-quality

This library manages the formatter and linter CLI for Java on numbers. It allows students to format their code according to Google's [Java style guide](https://google.github.io/styleguide/javaguide.html).

## Contents

1. [Introduction](#introduction)
2. [Formatting](#formatting)
3. [Linting](#linting)
4. [Installation](#installation)
5. [Updating](#updating)
   1. [google-java-format](#google-java-format)
   2. [checkstyle](#checkstyle)
   3. [checkstyle Google configuration](#checkstyle-google-configuration)
6. [Release New Version](#release-new-version)
7. [Credits](#credits)

## Introduction

The purpose of this library is to help students understand the importance of code style. It shows them how to properly format Java code, and teaches them to lint their code to identify a variety of infelicities.

## Formatting

Eastern University defaults to Google's style guide for Java with the exception of using four-space indentation.

Google provides a [Java program](https://github.com/google/google-java-format) that automatically formats a given Java file to their standards. (When run with the `--aosp` flag, it uses four-space indentation).

Since this script requires a number of flags to account for, among other things, modern Java versions and the indentation exception, it is encased in a custom `format` command added to numbers. Students can thus format their code with the following command:

```
format [file]
```

## Linting

Linting of Java files is done through [checkstyle](https://checkstyle.org/). From their website:

> Checkstyle is a development tool to help programmers write Java code that adheres to a coding standard. It automates the process of checking Java code to spare humans of this boring (but important) task. This makes it ideal for projects that want to enforce a coding standard.

Checkstyle [supports](https://checkstyle.org/google_style.html) Google's style guide through the use of a custom [configuration file](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml).

Similar to Google's formatter, checkstyle is packaged in a `jar` file that can be manually executed on student's code. Again, to avoid having students memorize a series of flags to run checkstyle, it is packaged in the custom `lint` command added to numbers. Students can thus lint their code with the following command:

```
lint [file]
```

## Installation

Instructions pending...

## Updating

The following versions of the formatter and linter are currently in use:

- [google-java-format](https://github.com/google/google-java-format): 1.15.0
- [checkstyle](https://github.com/checkstyle/checkstyle): 10.5.0
- [checkstyle Google configuration](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml): Last commit 2022-08-15

To update these files, simply download them from the links below and overwrite the current versions in the [data](data) directory. Make sure to name them appropriately.

### google-java-format

Download from the GitHub repo [releases page](https://github.com/google/google-java-format/releases/tag/v1.15.0). Make sure to get the "all-deps" version.

Remove the version number from the file name to allow the `format` command to identify it. Name it `google-java-format-all-deps.jar`.

### checkstyle

Download from the GitHub repo [releases page](https://github.com/checkstyle/checkstyle/releases).

Remove the version number from the file name to allow the `lint` command to identify it. Name it `checkstyle.jar`.

### checkstyle Google configuration

Download [google_checks.xml](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) in the checkstyle repository. Also see [this page](https://checkstyle.org/google_style.html).

Use the default name `google_checks.xml`.

## Release New Version

After updating one or more of the above dependencies (or anything else in this library), update the [version number](data/version) according to [semantic versioning[(https://semver.org/)], where dependency updates are considered minor changes. Commit all changes to GitHub.

Next, run the [`package.sh`](package.sh) script to create a zip package with the following commands:

```shell
cd java-code-quality/
```

**Note: You must run the script from within its parent directory.**

```shell
bash package.sh
```

Upload the created zip file to GitHub as a new release. Then, [install](#installation) the new package on numbers.

## Credits

Created by: Simon Kwilinski

Last updated: 2022-12-30
