#!/usr/bin/python

# Import python standard libraries

import os
import glob
import shutil

# User-defined functions


def get_list_of_files_with_suffix(original_root, suffix):
    """Given a root directory, this function searches subdirectories and
    returns a list of files with a specified suffix.
    """
    list_of_files = []
    for name in glob.glob(original_root + '/**/*' + suffix, recursive=True):
        # Check if the name is actually a directory. If not, append it to the
        # list of files.
        if not os.path.isdir(name):
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


# Body of the script
# This script copies HTML files from a DART repository into the docs/html
# directory of this beautiful-soup repository.

if __name__ == "__main__":

    # Get the directory in which this script resides.
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Declare the original_root, desination_root and the desired file suffix.

    # This script assumes the DART directory is a sibling directory of the
    # beautiful-soup directory
    original_root = current_directory+'/../DART'
    print(original_root)
    suffix = 'html'
    destination_root = current_directory + '/docs/html'

    origin_list = sorted(get_list_of_files_with_suffix(original_root, suffix))
    destination_list = sorted(get_list_of_destination_files(origin_list,
                              original_root, destination_root))

    # Use the sorted lists to copy the files
    for ifile in range(0, len(origin_list)):
        print('Copy ' + origin_list[ifile], '\nto ' + destination_list[ifile] +
              '\n')
        # Make the destination directory, if it doesn't already exist.
        os.makedirs(os.path.dirname(destination_list[ifile]), exist_ok=True)
        # Copy the file from the source to the destination
        shutil.copy(origin_list[ifile], destination_list[ifile])
