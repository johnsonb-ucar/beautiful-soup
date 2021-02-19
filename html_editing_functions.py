#!/usr/bin/python

# Import python standard libraries.

import os

# Import third-party libraries.

from bs4 import Tag, NavigableString, BeautifulSoup, Comment

# Declare user-defined functions.


def convert_relative_path_to_absolute_path(this_file_path, relative_path,
                                           doc_root):
    """Sphinx expects paths to be defined as absolute paths in which the path
    root is the ``doc_root``. This function takes three arguments:

    1. the path of the file being edited
    2. the relative path from the file being edited to the linked file
    3. the doc_root used by Sphinx

    It returns the absolute path to the linked file.

    In order for this function to work as intented, both the file being edited
    and the linked file must be contained within ``doc_root``.
    """

    # Find how many parent directories have to be traversed by first splitting
    # the ``../`` out of the string.
    split_parents_out_of_path = relative_path.split('../')
    # Each ``../`` in the original string creates a empty list element in the
    # split string list. Count how many empty list elements there are.
    number_of_parent_directories = split_parents_out_of_path.count('')

    # Split the original file path by slashes.
    this_file_path = this_file_path.split('/')
    # pop off the number of parent_directories plus one (for the filename)
    # from the original filepath's split list.
    for ipop in range(0, number_of_parent_directories+1):
        this_file_path.pop()

    # Append the last list item from split_parents_out_of_path to the
    # this_file_path list.
    this_file_path.append(split_parents_out_of_path[-1])

    # Define an absolute path string to use as the basis of joining the split
    # list contained in this_file_path.
    absolute_path = '/'
    absolute_path = absolute_path.join(this_file_path)

    # Remove the path to the doc_root from the absolute path.
    absolute_path = absolute_path.replace(doc_root, '')

    return absolute_path


def convert_string_to_sentence_case(string):
    """This function does not operate on the soup. It takes a string and
    converts it to sentence case using rules of American English. The
    function contains three lists that words are compared against so that it
    can recognize whether a word is:

    1. an acronym or initialism,
    2. a proper noun,
    3. a name that is never capitalized, such as mkmf.

    These lists enable the function to treat the words contained therein
    appropriately.
    """

    all_caps = [
        '1D', '3DVAR', '3DVAR/4DVAR', '4DVAR', 'AIRS', 'AIX', 'AMSR-E',
        'AQUA', 'ASCII', 'ATCF', 'ATM', 'CAM', 'CAM-FV', 'CAM-SE', 'CESM',
        'CESM', 'CESM+DART' 'CESM1', 'CESM2', 'CLM', 'CM1', 'COAMPS', 'COSMIC',
        'DART', 'DMSP', 'EDR-DSK', 'F16', 'F90', 'GHRSST', 'GITM', 'GPS',
        'GTSPP', 'GUI', 'HRLDAS', 'HRLDAS-V3.3', 'L63', 'LANL', 'LANL/POP',
        'MADIS', 'MDF', 'MIDAS', 'MODIS', 'MODULE', 'MPAS', 'MPAS_ATM',
        'MPAS_OCN', 'MPI', 'NCO', 'NCOMMAS', 'NOAH', 'NOAHLSM_OFFLINE', 'OCN',
        'OSX', 'POP', 'POP2', 'PROGRAM', 'QC', 'RINEX', 'RMA', 'ROMS', 'SGI',
        'SQG', 'SSEC', 'SSUSI', 'TERRA', 'TIEGCM', 'TPW', 'WACCM', 'WOD',
        'WRF', 'WRF/DART'
    ]

    proper_nouns = [
        'Absoft', 'AmeriFlux', 'Convert all netCDF variations',
        'DEFAULT_obs_def_mod', 'Easter', 'Fiji', 'Fortran', 'Guam', 'Hawaii',
        'Iceland', 'Ikeda', 'Jamaica', 'Kodiak', 'Lanai', 'Lorenz',
        'Lorenz_04', 'Lorenz_63', 'Lorenz_84', 'Lorenz_96', 'Lorenz_96',
        'Manhattan', 'Matlab', 'Matlab®', 'Mesonet', 'MITgcm_ocean', 'netCDF',
        'NetCDF', 'Oklahoma', 'PowerPC', 'PrecisionCheck', 'Pro', 'QuikSCAT',
        'SeaWinds'
    ]

    # Preserving lower case only matters for the first word of the string,
    # since it would otherwise be capitalized.
    lower_case = [
        'atmos_tracer_utilities_mod', 'convert_L2b.f90', 'dart_to_cam', 'mkmf',
        'model_mod', 'model_to_dart', 'mpas_dart_obs_preprocess',
        'obs_to_table.f90', 'pe2lyr', 'perfect_model_obs_nml',
        'plot_wind_vectors.m', 'replace_wrf_fields', 'utilities_nml'
    ]

    # To keep the logic simple, this boolean gets set to true when the first
    # word is a numeral or other punctuation. In that case, the second word in
    # the sentence should be capitalized.
    capitalize_second_word = False

    if string is not None:
        for iword, word in enumerate(string.split(' ')):

            if iword == 0:
                # First check to see if the word is a numeral identifying a
                # list, such as 1. or 2.1. A succinct way to check this is to
                # convert the string to lowercase and then check if the
                # resulting string is actually lowercase. If it is not
                # lowercase, then the string contains no characters and only
                # contains numerals or punctuation.
                if not word.lower().islower():
                    # The first word is a numeral or other punctuation.
                    capitalize_second_word = True
                elif (word not in all_caps and word not in proper_nouns and
                      word not in lower_case):
                    word = word.capitalize()
                sentence_case_string = word
            # If the first word was a numeral or punctuation, apply the
            # capitalization logic to the second word.
            elif capitalize_second_word:
                if (word not in all_caps and word not in proper_nouns and
                        word not in lower_case):
                    word = word.capitalize()
                sentence_case_string = sentence_case_string + ' ' + word
                capitalize_second_word = False
            # Otherwise, apply the lowercase logic to the word.
            else:
                if (word not in all_caps and word not in proper_nouns and
                        word not in lower_case):
                    word = word.lower()
                sentence_case_string = sentence_case_string + ' ' + word

        # Some of the headers end with a period. Remove it.
        if sentence_case_string[-1] == '.':
            sentence_case_string = sentence_case_string[:-1]
    else:
        sentence_case_string = ''

    return sentence_case_string


def decompose_anchors_providing_navigation_near_top_of_file(soup):
    """Each of the original HTML files has a nagivation list near the top of
    the page. The anchors in these navigation lists do not have a systematic
    relationship between their link text and ``href`` values. Sometimes the
    link text matches the ``href`` values and sometimes it does not.
    Text and ``href`` match: ``<a href="#Namelist">NAMELIST</a>``
    Text and ``href`` don't match:  ``<a href="#Legalese">TERMS OF USE</a>``
    This causes many problems for the automatic pandoc conversion, thus this
    function simply removes these navigation anchors and another function,
    ``replace_headers_and_compose_content_list``, creates a content list that
    will be reliably translated to reStructuredText.
    """
    # 'DART project logo' is the alt text for the DART logo image.
    logo_string = 'DART project logo'
    header_types = ['h1', 'h2', 'h3', 'h4', 'h5', 'p']

    # This function has the most comments because its logic is seemingly
    # circuitous. Removing the navigation list is a delicate process because
    # the original navigation list intersperses Tags and NavigableStrings.
    # It isn't possible to traverse the section and remove objects from it by
    # alternating the next_element and extract() because the next elements of
    # Tags **are** their content strings. Thus extracting a tag precludes
    # next_element from iterating through the elements, since the next element
    # was the content string that was just extracted.

    # Thus, the function uses the DART logo table to locate the navigation
    # list and makes a first pass through the list while removing the Tags.
    # The function then uses the DART logo table again to locate the navigation
    # list and makes a second pass through the list while removing the
    # NavigableStrings.

    # This is the first pass.
    for table in soup('table'):
        # table.contents returns a list of the rows in the table. Iterate
        # through the rows.
        # Type cast the row as a str in order to use the substring in string
        # syntax to check if any row contains the 'DART project logo' string.
        # If the table contains the logo string, then start traversing the
        # document and removing rows until the next header is reached.

        # Find the logo table.
        if any(logo_string in str(row) for row in table.contents):
            # The navigation table can't be traversed using next_siblings
            # because there are strings outside of tags, for example:
            # ``<a href="#Namelist">NAMELIST</a> /``
            # ``<a href="#DataSources">DATA SOURCES</a> /``
            # the `` /`` is not a sibling of the table.
            # Use next_sibling once to skip over the table and get the tag for
            # the first navigation anchor.

            in_section = True
            for next_sibling in table.find_next_siblings():
                if in_section:
                    # Check if the next_sibling is a Tag object.
                    if isinstance(next_sibling, Tag):
                        # If it is a tag, it will nave a name. Check to see if
                        # the name is h1, h2, h3, h4, or h5.
                        if next_sibling.name in header_types:
                            # If so, the section has been traversed.
                            in_section = False
                        else:
                            # Otherwise, the sibling is still in the section,
                            # so remove it.
                            next_sibling.decompose()

    # This is the second pass.
    for table in soup('table'):
        # Find the logo table.
        if any(logo_string in str(row) for row in table.contents):
            # Get the table's next sibling. Using next_element on the table
            # itself is undesirable because that would require iterating
            # through the table elements. next_sibling skips the table to the
            # next Tag or, in this case, NavigableString.
            next_sibling = table.next_sibling
            # Get the next_element of the next_sibling.
            next_element = next_sibling.next_element

            # Use a boolean to keep the logic simple in a while loop.
            in_section = True
            while in_section and next_element is not None:
                # If the next_element is header tag, the section has been
                # traversed.
                if (isinstance(next_element, Tag) and next_element.name in
                        header_types):
                    in_section = False
                # Otherwise, get the next element and delete this one.
                else:
                    this_element = next_element
                    next_element = this_element.next_element
                    this_element.extract()

    return soup


def decompose_anchors_providing_navigation_in_bgrid_and_mitgcm_pages(soup):
    """Each of the bgrid_solo and three out of the four MITgcm_ocean HTML files
    has a nagivation list near the top of the page. The anchors in these
    navigation lists do not have a systematic relationship between their link
    text and ``href`` values. Thus this function simply removes these
    navigation anchors and another function,
    ``replace_headers_and_compose_content_list``, creates a content list that
    will be reliably translated to reStructuredText.
    """
    header_types = ['h1', 'h2', 'h3', 'h4', 'h5', 'p']

    # This function has a lot of comments because its logic is seemingly
    # circuitous. Removing the navigation list is a delicate process because
    # the original navigation list intersperses Tags and NavigableStrings.
    # It isn't possible to traverse the section and remove objects from it by
    # alternating the next_element and extract() because the next elements of
    # Tags **are** their content strings. Thus extracting a tag precludes
    # next_element from iterating through the elements, since the next element
    # was the content string that was just extracted.

    # This function uses the soup.body tag locate the top of the page, where
    # navigation list exists and makes a first pass through the list while
    # removing the Tags. The function then uses soup.body tag again to locate
    # the navigation list and makes a second pass through the list while
    # removing the NavigableStrings.

    # This is the first pass.

    # Use a boolean to keep the logic simple in a while loop.
    first_anchor = soup.a

    in_section = True
    for next_sibling in first_anchor.find_next_siblings():
        print('next_sibling.content', next_sibling.content)
        if in_section:
            # Check if the next_sibling is a Tag object.
            if isinstance(next_sibling, Tag):
                # If it is a tag, it will nave a name. Check to see if
                # the name is h1, h2, h3, h4, or h5.
                if next_sibling.name in header_types:
                    # If so, the section has been traversed.
                    in_section = False
                else:
                    # Otherwise, the sibling is still in the section,
                    # so remove it.
                    next_sibling.decompose()
    first_anchor.decompose()

    # This is the second pass.
    
    # Get the next_element of the next_sibling.
    next_element = soup.body.next_element

    # Use a boolean to keep the logic simple in a while loop.
    in_section = True
    while in_section and next_element is not None:
        # If the next_element is header tag, the section has been
        # traversed.
        if (isinstance(next_element, Tag) and next_element.name in
                header_types):
            in_section = False
        # Otherwise, get the next element and delete this one.
        else:
            this_element = next_element
            next_element = this_element.next_element
            this_element.extract()

    return soup


def decompose_anchors_with_name_and_no_string(soup):
    """The HTML documentation contains anchors with name attributes of the form
    ``<a name="Decisions"></a>``. These anchors are used as link targets
    elsewhere in each page. Pandoc converts these tags more predictably when
    they are replaced with id attributes within header tags. For example,
    ``<h2 id="decisions">Decisions</h2>``. This function decomposes all of the
    named anchors in a page that don't have link text.
    """
    for a in soup('a'):
        # If the anchor does not have a name, a KeyError will be returned. The
        # code will try checking the name attribute. Since most anchors in the
        # DART documentation do not have a name. Thus nothing happens in the
        # except case.
        try:
            if a['name'] and a.string is None:
                a.decompose()
                print('Removing named anchor with no string.')
        except (KeyError, TypeError):
            pass

    return soup


def decompose_legalese_links(soup):
    """Each page in the HTML documentation has a Legalese link and target that
    takes the user to the bottom of the page. This function removes them.
    """
    # Construct lists of the variations of legalese names and targets.
    variations = ['LEGALESE', 'Legalese', 'legalese']
    target_variations = ['#'+element for element in variations]

    for a in soup('a'):
        # If an anchor doesn't have a name, a KeyError will be returned.
        # Therefore, use try & except.
        # Type cast the anchor's name list as a set and check if it shares
        # common elements with the variations set.
        try:
            if a['name'] in variations:
                a.decompose()
                print('Removing legalese target.')
        except KeyError:
            pass

        # If an anchor doesn't have a href, an AttributeError will be returned.
        # Therefore, use try & except.
        try:
            if a.get('href') in target_variations:
                a.decompose()
                print('Removing legalese link.')
        except AttributeError:
            pass

    return soup


def decompose_logo_main_index_table(soup):
    """Each page in the HTML documentation has a table near the top of the page
    with two cells: one with the DART logo and another with a link that says
    'Jump to DART Documentation Main Index'. This function removes the table,
    since its functionality will be replaced by the logo and navigation table
    created by Sphinx/ReadTheDocs.
    """
    # 'DART project logo' is the alt text for the DART logo image.
    logo_string = 'DART project logo'

    for table in soup('table'):
        # table.contents returns a list of the rows in the table. Iterate
        # through the rows.
        # Type cast the row as a str in order to use the substring in string
        # syntax to check if any row contains the 'DART project logo' string.
        # If so, delete the table.
        if any(logo_string in str(row) for row in table.contents):
            table.decompose()
            print('Removing logo table.')

    return soup


def decompose_obsolete_sections(soup):
    """Certain sections of the existing documentation should be removed from
    the current documentation. This function identifies a section using the
    ``<h2>`` tag and then traverses the document, removing all content
    including and after the specified ``<h2>`` tag until either the next
    ``<h2>`` tag or the end of the file is reached.
    """
    # Construct a list of headers that should be removed. This list might
    # become long.
    sections_to_remove = [
        'KNOWN BUGS',
        'FUTURE PLANS',
        'Terms of Use'
    ]

    # Find all the h2 tags in the page.
    for h2 in soup('h2'):
        # Check if the string in the h2 tag is in sections_to_remove.
        if h2.string in sections_to_remove:
            # If it matches, traverse the section.
            in_section = True
            for next_sibling in h2.find_next_siblings():
                if in_section:
                    # Check if the next_sibling is a Tag object.
                    if isinstance(next_sibling, Tag):
                        # If it is a tag, it will nave a name. Check to see if
                        # the name is h2.
                        if next_sibling.name == 'h2':
                            # If so, the section has been traversed.
                            in_section = False
                        else:
                            # Otherwise, the sibling is still in the section,
                            # so remove it.
                            next_sibling.decompose()
            # Lastly, remove the h2 tag at the start of the section.
            h2.decompose()

    return soup


def decompose_top_links(soup):
    """The HTML documentation contains links that take the user back to the top
    of the page. In order to simplify the link navigation, since Sphinx
    provides its own navigation structure, this function removes the top links.
    Note: the structure of top links are inconsistent throughout the
    documentation. This function works on the ``MOD15A2_to_obs.html`` top link
    structure but will be extended so it works on other pages.
    """
    # Construct lists of the variations of top names and targets.
    variations = ['TOP', 'Top', 'top']
    target_variations = ['#'+element for element in variations]

    for div in soup('div'):
        try:
            # Each div can have zero or more classes assigned to it. Check if
            # union of its set of classes and the variations of top have any
            # shared elements. If so, remove the div.
            if set(div['class']) & set(variations):
                div.decompose()
                print('Removing top link.')
        except KeyError:
            pass

    for a in soup('a'):
        # If the anchor does not have a name, a KeyError will be returned. The
        # code will try checking the name attribute and delete the tag if the
        # name is Top. Most anchors in the DART documentation do not have a
        # name. Thus nothing happens in the except case.
        try:
            if a['name'] in variations:
                a.decompose()
                print('Removing top target.')
        except KeyError:
            pass

    return soup


def extract_comments(soup):
    """The HTML templates used to construct the documention contain comments
    that give the documentation writer hints and reminders as to which section
    goes where. These comments will become unnecessary in the converted files,
    thus this function removes all of them.
    """
    # Find all the comments.
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    # find_all returns a list. Iterate through it and remove each element.
    for comment in comments:
        comment.extract()

    return soup


def replace_anchors_within_body_text_with_their_contents(soup):
    """The HTML documentation contains anchors with name attributes of the form
    ``<a href="#DataSources"></a>``. These anchors are used as link targets
    elsewhere in each page. Pandoc converts documents more cleanly when id tags
    are used in structural elements such as ``<h*>`` tags instead. This latter
    syntax is implemented in the ``replace_headers_and_compose_content_list``
    function. Thus this function simply replaces anchors with ``href="#*"`` and
    strings with the string they contain. This is an imperfect solution but
    the alternative is having internal links with missing targets.
    """
    for a in soup('a'):
        # If an anchor doesn't have a href, an AttributeError will be returned.
        # Therefore, use try & except.
        try:
            href = a.get('href')

            if (href is not None and len(href) > 0 and href[0] == '#' and
                    len(a.contents) > 0):
                a.unwrap()
        except AttributeError:
            pass

    return soup


def replace_ems_with_classes(soup):
    """The filepaths and environmental variables in the HTML documentation are
    represented using ``<em>`` tags with unix and file classes. Pandoc needs
    these to be represented using ``<code>`` tags in order to be rendered as
    string literals in reStructuredText.
    """
    # Construct a set rather than a list.
    classes_to_remove = {'file', 'unix', 'mono', 'program', 'class', 'code'}

    for em in soup('em'):
        # Only replace the <em> tags with <code> tags if the em has the file,
        # unix, mono, program, class or code class.
        try:
            # Each em can have zero or more classes assigned to it. Check if
            # union of its set of classes and the classes to remove have any
            # shared elements. If so, replace the em tag with a code tag.
            if classes_to_remove & set(em['class']) and em.string is not None:
                code_tag = soup.new_tag('code')
                code_tag.string = em.string
                em.replace_with(code_tag)
                print('Replacing classed em tag with code tag.')
            else:
                print('Not replacing unclassed em tag.')
        except KeyError:
            pass

    return soup


def replace_headers_and_compose_content_list(soup):
    """Each page in the HTML documentation has a collection of h1, h2 and h3
    tags that act as section headers. Typically, the ``<h2>`` tags are used to
    denote sections of the page. Unfortunately ``<h3>`` and ``<h4>`` tags tend
    to be scattered around the documentation pages and are often used out of
    order, failing to respect the expected header hierarchy in an HTML
    document, e.g.:

    .. code-block::

       <h1>
           <h2></h2>
           <h2></h2>
               <h3></h3>
           <h2></h2>
               <h3</h3>
                   <h4></h4>

    This function collects the ``<h2>`` headers in a page and composes a
    content list near the top of the page that will serve as internal
    navigation.
    """

    # Make an empty unordered list.
    content_list = soup.new_tag('ul')

    for h2 in soup('h2'):
        # Use the string methods to modify versions of the header string for
        # use in creating the content list and to assign an id attribute to the
        # tag.

        # Make an empty list item tag to populate with modified versions of the
        # header string.
        list_item = soup.new_tag('li')
        list_item_a = soup.new_tag('a')

        # Convert the header string to sentence case.
        sentence_case_header = convert_string_to_sentence_case(h2.string)

        # Modify the original h2 string to be capitalized.
        h2.string = sentence_case_header
        # Assign the list item string to the same capitalized verison of the h2
        # string.
        list_item_a.string = sentence_case_header

        # Create an id attribute for the original h2 tag and assign it a
        # lowercase, underscored modification of the original h2 tag.
        h2.attrs['id'] = h2.string.lower().replace(" ", "_")
        # Create a href attribute for the list item and assign it the same
        # lowercase, underscored modification of the original h2 tag.
        list_item_a.attrs['href'] = '#'+h2.string.lower().replace(" ", "_")

        # Insert the anchor into the list item.
        list_item.append(list_item_a)
        # Append the list item to the content list.
        content_list.append(list_item)
        content_list.append("\n")

    # Insert the content list after the page title contained in the first <h1>.
    insert_count = 0
    if soup.h1:
        if insert_count == 0:
            soup.h1.insert_after("\n", content_list)
            header_for_content_list = soup.new_tag('h2')
            header_for_content_list.string = 'Contents'
            soup.h1.insert_after("\n", header_for_content_list)
            insert_count += 1
    # Otherwise insert the content list after the first <h2>.
    elif soup.h2:
        if insert_count == 0:
            soup.h2.insert_after("\n", content_list)
            header_for_content_list = soup.new_tag('h3')
            header_for_content_list.string = 'Contents'
            soup.h2.insert_after("\n", header_for_content_list)
            insert_count += 1
    else:
        if insert_count == 0:
            soup.body.insert(0, '\n')
            soup.body.insert(0, content_list)
            header_for_content_list = soup.new_tag('h2')
            header_for_content_list.string = 'Contents'
            soup.body.insert(0, '\n')
            soup.body.insert(0, header_for_content_list)
            insert_count += 1

    return soup


def replace_namelist_divs(soup):
    """Namelists in the HTML documentation are represented using a div with a
    namelist class. Pandoc needs the namelist to be wrapped in ``<pre><code>``
    tags in order to be rendered as a literal block in reStructuredText.
    """
    # Construct a set rather than a list.
    variations = {'NAMELIST', 'Namelist', 'namelist'}

    for div in soup('div'):
        try:
            # Only replace the <div><pre> tags with the <pre><code> tags if the
            # div has the namelist class.
            if set(div['class']) & variations and div.pre.string:
                # Make a code tag and set its string to contain the contents of
                # the namelist div's pre tag. The namelist div's pre tag
                # contains the literal string of the namelist.
                code_tag = soup.new_tag('code')
                code_tag.string = div.pre.string
                div.pre.replace_with(code_tag)

                # Make a pre tag and set it to contain the code tag created
                # above.
                pre_tag = soup.new_tag('pre')
                pre_tag.append(div.code)

                # Replace the namelist div with the new <pre><code> tags and
                # their contents.
                div.replace_with(pre_tag)
                print('Replacing namelist-classed div with <pre><code> tags.')
        except KeyError:
            pass

    return soup


def rewrite_lesser_headers_than_h2_as_sentence_case(soup):
    """The ``replace_headers_and_compose_content_list`` function rewrites all
    of the h2 headers in the document using sentence case. This function
    rewrites the h3, h4, h5 and h6 headers using sentence case.
    """
    # Create a list with the types of headers to rewrite.
    header_types = ['h3', 'h4', 'h5', 'h6']

    # Iterate through the header types.
    for header_type in header_types:
        # Iterate through the actual headers.
        for header in soup(header_type):
            header.string = convert_string_to_sentence_case(header.string)

    return(soup)


def rewrite_relative_paths_as_absolute_in_hrefs(soup, original_file_path,
                                                doc_root):
    """Sphinx expects paths to be defined as absolute paths in which the path
    root is the ``doc_root``. This function checks all of the anchors in a file
    for relative paths and rewrites them as absolute paths, where ``/``
    corresponds to the ``doc_root``.
    """
    # If an anchor doesn't have a href, an AttributeError will be returned.
    # Therefore, use try & except.
    for a in soup('a'):
        try:
            href = a.get('href')

            # Check if the path is a relative path by seeing if the first three
            # characters denote a parent directory.
            if href is not None and len(href) > 2 and href[:3] == '../':
                a.attrs['href'] = convert_relative_path_to_absolute_path(
                    original_file_path, href, doc_root)

        except AttributeError:
            pass

    return soup
