#!/usr/bin/python

# Import third-party libraries

from bs4 import BeautifulSoup

# User-defined functions

def replace_namelist_divs(soup):
    """Namelists in the HTML documentation are represented using a div with a
    namelist class. Pandoc needs the namelist to be wrapped in  <pre><code>
    tags in order to be rendered as a literal block in reStructuredText.
    """
    # Construct a set rather than a list
    variations = {'NAMELIST', 'Namelist', 'namelist'}

    for div in soup('div'):
        try:
            # Only replace the <div><pre> tags with the <pre><code> tags if the div
            # has the namelist class
            if set(div['class']) & variations:
                # Make a code tag and set its string to contain the contents of the
                # namelist div's pre tag. The namelist div's pre tag contains the
                # literal string of the namelist
                code_tag = soup.new_tag('code')
                code_tag.string = div.pre.string
                div.pre.replace_with(code_tag)

                # Make a pre tag and set it to contain the code tag created above.
                pre_tag = soup.new_tag('pre')
                pre_tag.append(div.code)

                # Replace the namelist div with the new <pre><code> tags and their
                # contents.
                div.replace_with(pre_tag)
                print('Replacing namelist-classed div with <pre><code> tags.')
        except KeyError:
            pass

    return soup

def replace_ems_with_classes(soup):
    """The filepaths and environmental variables in the HTML documentation are
    represented using <em> tags with unix and file classes. Pandoc needs these
    to be represented using <code> tags in order to be rendered as string
    literals in reStructuredText.
    """
    # Construct a set rather than a list
    classes_to_remove = {'file', 'unix', 'mono', 'program', 'class', 'code'}

    for em in soup('em'):
        # Only replace the <em> tags with <code> tags if the em has the file, 
        # unix, mono, program, class or code class.
        try:
            # Each em can have zero or more classes assigned to it. Check if
            # union of its set of classes and the classes to remove have any
            # shared elements. If so, replace the em tag with a code tag.
            if classes_to_remove & set(em['class']):
                code_tag = soup.new_tag('code')
                code_tag.string = em.string
                em.replace_with(code_tag)
                print('Replacing classed em tag with code tag.')
            else:
                print('Not replacing unclassed em tag.')
        except KeyError:
            pass
    
    return soup

def decompose_top_links(soup):
    """The HTML documentation contains links that take the user back to the top
    of the page. In order to simplify the link navigation, since Sphinx
    provides its own navigation structure, this function removes the top links.
    Note: the structure of top links are inconsistent throughout the
    documentation. This function works on the MOD15A2_to_obs.html top link
    structure but will be extended so it works on other pages.
    """
    # Construct lists of the variations of top names and targets
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

def decompose_legalese_links(soup):
    """Each page in the HTML documentation has a Legalese link and target that
    takes the user to the bottom of the page. This function removes them.
    """
    # Construct lists of the variations of legalese names and targets
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

# Open the input page.
input_page = 'original_MOD15A2_to_obs.html'
with open(input_page) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# Pass the soup through the functions.
soup = replace_namelist_divs(soup)
soup = replace_ems_with_classes(soup)
soup = decompose_top_links(soup)
soup = decompose_legalese_links(soup)
soup = decompose_logo_main_index_table(soup)

# Save the output.
output_page = 'modified_MOD15A2_to_obs.html'
with open(output_page, 'w') as file:
    file.write(str(soup))
