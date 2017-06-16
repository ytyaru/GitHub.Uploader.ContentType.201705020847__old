import unittest
from MimeType import MimeType
from SubType import SubType
from tree.SubTypeTree import SubTypeTreeFactory
from tree.SubTypeTree import VenderTreeFactory
from tree.SubTypeTree import SubTypeTree
from tree.SubTypeTree import VenderTree
from tree.SubTypeTree import GitHubVenderTree
from tree.SubTypeTree import StandardTree
from tree.SubTypeTree import ParsonalTree
from tree.SubTypeTree import UnregisteredTree
class TestMimeType_TDD(unittest.TestCase):
    def test_HasAttribute(self):
        self.assertTrue(hasattr(MimeType, 'String'))
        self.assertTrue(hasattr(MimeType, 'TopLevelType'))
        self.assertTrue(hasattr(MimeType, 'SubType'))

