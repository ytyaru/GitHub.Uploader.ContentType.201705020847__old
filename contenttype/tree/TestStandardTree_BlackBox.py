import unittest
from SubTypeTree import SubTypeTreeFactory
from SubTypeTree import VenderTreeFactory
from SubTypeTree import SubTypeTree
from SubTypeTree import VenderTree
from SubTypeTree import GitHubVenderTree
from SubTypeTree import StandardTree
from SubTypeTree import ParsonalTree
from SubTypeTree import UnregisteredTree
class TestStandardTree_BlackBox(unittest.TestCase):
    def test_Values(self):
        tree_list = ['html']
        tree = StandardTree(tree_list)
        self.assertEqual(None, tree.GetFacet())
        self.assertEqual(tree_list, tree.TreeList)

