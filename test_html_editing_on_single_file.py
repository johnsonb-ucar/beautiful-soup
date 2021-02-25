#!/usr/bin/python

# This script runs all of the functions contained in html_editing_functions.py
# on an HTML file, ``/observations/obs_converters/MODIS/MOD15A2_to_obs.html``.
# For ease of comparison, the edited HTML is saved as a separate file,
# ``/observations/obs_converters/MODIS/modified_MOD15A2_to_obs.html``.

# Import python standard libraries.

import os

# Import third-party libraries.

from bs4 import BeautifulSoup

# Import user-created libraries.

from html_editing_functions import *

# Get the directory in which this script resides.
current_directory = os.path.dirname(os.path.realpath(__file__))

# Assign the documentation root and paths to the input and output documents.
doc_root = current_directory + '/docs/html'
dart_root = current_directory+ '/../DART'
original_file_path = (dart_root + '/observations/obs_converters/tropical_cyclone/tc_to_obs.html')
modified_file_path = (current_directory + '/test_file.html')

# Open the input page.
with open(original_file_path) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# Pass the soup through the functions.
#
# For the most part, the functions can be run in any order. However, there are
# two exceptions:
#
# 1. ``decompose_anchors_providing_navigation_near_top_of_file`` function won't
#    work as intended if it is run after ``decompose_logo_main_index_table``
#    because the former function uses the logo table to locate where the
#    navigation anchors occur in the document while the latter removes the logo
#    table from the document.
#
# 2. ``replace_anchors_within_body_text_with_their_contents`` will
#    remove the anchors in the list elements of the content list at the
#    beginning of the document, thus it should be run before the content list
#    is created by ``replace_headers_and_compose_content_list``.
#
# If the functions are run in alphabetical order, they will work as intended.


soup = convert_internal_links_to_doc(soup)
# soup = decompose_anchors_providing_navigation_near_top_of_file(soup)
# soup = decompose_anchors_with_name_and_no_string(soup)
# soup = decompose_legalese_links(soup)
# soup = decompose_logo_main_index_table(soup)
# soup = decompose_obsolete_sections(soup)
# soup = decompose_top_links(soup)
# soup = extract_comments(soup)
# soup = replace_anchors_within_body_text_with_their_contents(soup)
# soup = replace_ems_with_classes(soup)
# soup = replace_headers_and_compose_content_list(soup)
# soup = replace_namelist_divs(soup)
# soup = rewrite_lesser_headers_than_h2_as_sentence_case(soup)
# soup = rewrite_relative_paths_as_absolute_in_hrefs(soup, original_file_path,
#                                                    doc_root)

# Save the output.
with open(modified_file_path, 'w') as file:
    file.write(str(soup))
