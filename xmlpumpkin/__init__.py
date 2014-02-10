# encoding: utf-8

from .runner import (
    cabocha,
)
from .tree import (
    Tree,
)

__version__ = '0.1'


def parse_to_tree(text):
    """Parse text using CaboCha, then return Tree instance."""
    xml_text = cabocha.as_xml(text)
    tree = Tree(xml_text)
    return tree
