#!/usr/bin/python

# This script iterates over all of the HTML files contained in a specified
# directory and runs them through the all of the functions contained within
# ``html_editing_functions.py``.

# Import python standard libraries.

import os
import glob
import shutil

# Import user-defined functions.

from file_system_functions import *
from html_editing_functions import *

# Get the directory in which this script resides.
current_directory = os.path.dirname(os.path.realpath(__file__))

# Declare the original_root, desination_root and the desired file suffix.
# This script assumes the DART directory is a sibling directory of the
# beautiful-soup directory.

suffix = 'html'
doc_root = current_directory + '/docs/html'
rst_root = current_directory + '/docs/rst'

doc_list = sorted(get_list_of_files_with_suffix(doc_root, suffix))

docs_html_files_with_navigation_anchors = [
    'Manhattan_release.html',
    'Manhattan_getting_started.html',
    'Manhattan_diffs_from_Lanai.html',
    'Lanai_release.html',
    'Lanai_diffs_from_Kodiak.html'
]

mitgcm_files_with_no_dart_logo = [
    'trans_sv_pv.html',
    'trans_pv_sv.html',
    'create_ocean_obs.html'
]

# Use the sorted doc_list to iterate over the html files.
for ifile, this_file in enumerate(doc_list):
    
    # Open the input page.
    with open(this_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    
    # print(this_file, '\n')
    filename = this_file.split('/')[-1]

    # ``decompose_anchors_providing_navigation_near_top_of_file`` shouldn't be
    # run on certain files because they don't have navigation anchors an thus
    # the function doesn't work as intended.

    if ('docs/html/docs/html' in this_file and
            filename not in docs_html_files_with_navigation_anchors):
        # The files in the docs/html directory do not have navigation anchors.
        print(filename, 'does not have navigation anchors.')
        print('Skip decompose_anchors_providing_navigation_near_top_of_file.')
    elif 'html/docs/tutorial/index.html' in this_file:
        # The tutorial/index.html does not have navigation anchors.
        print('The tutorial\'s', filename, 'does not have navigation anchors.')
        print('Skip decompose_anchors_providing_navigation_near_top_of_file.')
    elif ('bgrid_solo/fms_src' in this_file or
            filename in mitgcm_files_with_no_dart_logo):
        # The bgrid_solo and most of the MITgcm_ocean HTML files do not have
        # the DART logo, so they must be treated with a different function. 
        print(this_file)
        decompose_anchors_providing_navigation_in_bgrid_and_mitgcm_pages(soup)
        print('\n')
    else:
        soup = decompose_anchors_providing_navigation_near_top_of_file(soup)
        
    soup = decompose_anchors_with_name_and_no_string(soup)
    soup = decompose_legalese_links(soup)
    soup = decompose_logo_main_index_table(soup)
    soup = decompose_obsolete_sections(soup)
    soup = decompose_top_links(soup)
    soup = extract_comments(soup)
    soup = replace_anchors_within_body_text_with_their_contents(soup)
    soup = replace_ems_with_classes(soup)
    soup = replace_headers_and_compose_content_list(soup)
    soup = replace_namelist_divs(soup)
    soup = rewrite_lesser_headers_than_h2_as_sentence_case(soup)
    soup = rewrite_relative_paths_as_absolute_in_hrefs(soup,
                                                       this_file,
                                                       doc_root)

    # Save the output.
    with open(this_file, 'w') as fp:
        fp.write(str(soup))

    rst_file = this_file.replace(doc_root, rst_root)
    rst_file = rst_file.replace('.html', '.rst')
    print(this_file)
    print(rst_file)
    os.makedirs(os.path.dirname(rst_file), exist_ok=True)
    command = 'mv '+this_file+' '+rst_file
    print(command)
    os.system(command)
    second_command = 'pandoc --columns=120 -f html -t rst '+rst_file+' -o '+rst_file
    print(second_command)
    os.system(second_command)
    print('\n\n\n\n')
