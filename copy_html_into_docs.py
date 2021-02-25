#!/usr/bin/python

# This script copies HTML files from a DART repository into the docs/html
# directory of this beautiful-soup repository.

# Import python standard libraries.

import os
import glob
import shutil

# Import user-defined functions.

from file_system_functions import *

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

# Copy the .rst files as well

original_root = current_directory+'/../DART'
print(original_root)
suffix = 'rst'
destination_root = current_directory + '/docs/rst'

# The gitm restart files also have the suffix "rst" so the loop needs to
# exclude files from gitm's test data directory from being copied, since they
# aren't actually reStructuredText files.
exclude_directory = 'models/gitm/testdata1'

origin_list = sorted(get_list_of_files_with_suffix(original_root, suffix))
destination_list = sorted(get_list_of_destination_files(origin_list,
                          original_root, destination_root))

# Use the sorted lists to copy the files
for ifile in range(0, len(origin_list)):
    
    if exclude_directory not in origin_list[ifile]:
        print('Copy ' + origin_list[ifile], '\nto ' + destination_list[ifile] +
              '\n')
        # Make the destination directory, if it doesn't already exist.
        os.makedirs(os.path.dirname(destination_list[ifile]), exist_ok=True)
        # Copy the file from the source to the destination
        shutil.copy(origin_list[ifile], destination_list[ifile])
    else:
        print(origin_list[ifile], "is a gitm restart file so don't copy it.\n")
