#!/usr/bin/python

# Import python standard libraries.

from os import path
from glob import glob

# Declare user-defined functions.


def get_list_of_files_with_suffix(original_root, suffix):
    """Given a root directory, this function searches subdirectories and
    returns a list of files with a specified suffix.
    """
    list_of_files = []
    for name in glob(original_root + '/**/*' + suffix, recursive=True):
        # Check if the name is actually a directory. If not, append it to the
        # list of files.
        if not path.isdir(name):
            list_of_files.append(name)

    return list_of_files


def get_list_of_destination_files(list_of_files, original_root,
                                  destination_root):
    """Given a list_of_files, an original_root directory, and a
    destination_root directory, this function returns a list comprised of the
    original file list, but with the original_root truncated from the filepaths
    and the destination_root replacing the original_root.
    """
    destination_list_of_files = []
    for name in list_of_files:
        name = name.replace(original_root, destination_root)
        destination_list_of_files.append(name)

    return destination_list_of_files
