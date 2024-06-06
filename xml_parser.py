"""
@about simple xml parser
@version 0.1
@since 6/5/24
@author lufemoal19

References: 
    https://docs.python.org/3/library/xml.etree.elementtree.html

"""

# Import data reading from file

import xml.etree.ElementTree as ET

# tree = ET.parse('country_data.xml')
# root = tree.getroot()

def show_xml_tree(root) -> str:
    _tree = ''
    for child in root:
        # _tree += f'{child.tag} {child.attrib}\n'
        _tree += f'{child.attrib}\n'

    return _tree

# finding interesting elements
def show_xml_leaf(root) -> str:
    _tree = ''
    for neighbor in root.iter('neighbor'):
        _tree += f'{neighbor.attrib}\n'

    return _tree

# find all
def show_xml_all(root) -> str:
    _tree = ''
    
    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.find('name')
        _tree += f'{name} {rank}\n'        
    
    return _tree


def main() -> None:
    tree = ET.parse('country_data.xml')
    root = tree.getroot()
    result = show_xml_tree(root)
    print(result)

if __name__ == '__main__':
    main()