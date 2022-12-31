from typing import List
import sys
import os
import filecmp

from Levenshtein import distance

def main():
    """
    DEPENDENCIES:
    
    This script requires python-Levenshtein, installed via:
        pip install python-Levenshtein
    This is installed automatically by the install.sh script in the
    java-code-quality library.
    

    FUNCTIONALITY:
    
    This script checks whether student code is correctly formatted using
    the `format` command implemented in this library.

    It accepts a list of files as parameters and formats each of them.
    Then it computes the Levenshtein distance between the formatted and
    unformatted versions of each file and sums the total distance.

    Finally, a float from 0 to 1 (representing a grade) is output
    according to the following table:

     Total Levenshtein Distance | Grade
    ----------------------------+-------
                              0 | 100%
                            1-3 | 70%
                            4-7 | 50%
                             8+ | 0%
    

    Args:
        None, except command line arguments.
    
    Returns:
        None, prints float.

    """

    sys.argv = sys.argv[1:]

    files = resolvePaths(sys.argv)

    if not sys.argv:
        print("ERR: No .java files provided. Specify one or more " +
                "files/directories on which to check formatting.")
        sys.exit(1)

    total_levenshtein = 0

    for file in files:
        total_levenshtein += levenshtein_format(file)
    
    if total_levenshtein == 0:
        print(1)
    elif total_levenshtein <= 3:
        print(0.7)
    elif total_levenshtein <= 7:
        print(0.5)
    else:
        print(0)


def levenshtein_format(file: str) -> int:
    """
    Format a file using the custom `format` terminal command within the
    java-code-quality library.

    Determine the Levenshtein distance between the formatted file and the
    original, and return that number. The result 0 indicates that the
    file was already formattedd.

    Note: The Levenshtein distance is not calculated when the formatted
    file is more than 100000 characters. In that case, if the files are
    the same, 0 is returned. Otherwise, 5 is naively returned.

    Args:
        file: The path to the file to format.
    
    Returns:
        The Levenshtein distance between the formatted and unformatted
        files.
    """

    formatted = file + ".TMP_FORMAT.java"

    # Create a copy of the file to format
    os.system(f'cp "{file}" "{formatted}"')

    # Format the copy
    os.system(f'format "{formatted}" > /dev/null')

    try:
        f1_txt = open(file).read()
        f2_txt = open(formatted).read()
    finally:
        # Delete the copy
        os.system(f'rm "{formatted}"')

    if len(f2_txt) > 100000:
        if filecmp.cmp(file, formatted):
            return 0
        else:
            return 5
    else:
        return distance(f1_txt, f2_txt)


def resolvePaths(paths: List[str]) -> List[str]:
    """
    Given a list of paths pointing to files and directories, return
    a list of paths to all .java files.

    Args:
        paths: A list of paths.
    
    Returns:
        A list of unique paths to .java files.
    """

    files = []

    for p in paths:
        if os.path.isfile(p):
            files.append(p)
        elif os.path.isdir(p):
            for f in getSubFiles(p):
                files.append(f)

    files = [f for f in files if f.endswith(".java")]
    
    return list(set(files))


def getSubFiles(directory: str) -> List[str]:
    """
    Given a directory, return a list of paths to every file in it
    and its subdirectories.

    Args:
        directory: The path to a directory.
    
    Returns:
        A list of file paths.
    """

    paths = []

    for (root, dirs, files) in os.walk(directory):
        for f in files:
            paths.append(os.path.join(root, f))
    
    return paths
    

if __name__ == '__main__':
    main()
