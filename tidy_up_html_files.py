#!/usr/bin/python

# This script iterates over all of the HTML files contained in a specified
# directory and runs the ``tidy`` program on them to clean up their html.

# Import python standard libraries.

import os
import glob
import shutil

# Import user-defined functions.

from file_system_functions import *
from html_editing_functions import *

# Get the directory in which this script resides.
current_directory = os.path.dirname(os.path.realpath(__file__))

# This script assumes the DART directory is a sibling directory of the
# beautiful-soup directory

suffix = 'html'
doc_root = original_root = current_directory+'/../DART'

doc_list = sorted(get_list_of_files_with_suffix(doc_root, suffix))

# Use the sorted doc_list to iterate over the html files.
for ifile, this_file in enumerate(doc_list):
    
    command = 'tidy -f errs.txt -m '+this_file
    print(command)
    os.system(command)
