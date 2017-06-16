"""
SubTypeクラスの設計テスト。
"""
import unittest
from SubType import SubType
from tree.SubTypeTree import SubTypeTreeFactory
from tree.SubTypeTree import VenderTreeFactory
from tree.SubTypeTree import SubTypeTree
from tree.SubTypeTree import VenderTree
from tree.SubTypeTree import GitHubVenderTree
from tree.SubTypeTree import StandardTree
from tree.SubTypeTree import ParsonalTree
from tree.SubTypeTree import UnregisteredTree
class TestSubType(unittest.TestCase):
    # application/vnd.github.v3.raw+json
    def test_HasMember(self):
        subtype = SubType("vnd.github.v3")
        self.assertTrue(hasattr(subtype, 'String'))
        self.assertTrue(hasattr(subtype, 'Facet'))
        self.assertTrue(hasattr(subtype, 'Tree'))
        self.assertTrue(hasattr(subtype, 'MediaType'))
        self.assertTrue(hasattr(subtype, 'Suffix'))

