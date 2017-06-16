import unittest
from SubTypeTree import SubTypeTreeFactory
from SubTypeTree import VenderTreeFactory
from SubTypeTree import SubTypeTree
from SubTypeTree import VenderTree
from SubTypeTree import GitHubVenderTree
from SubTypeTree import StandardTree
from SubTypeTree import ParsonalTree
from SubTypeTree import UnregisteredTree
class TestVenderTree_BlackBox(unittest.TestCase):
    def test_Values(self):
        vender_name = 'tree1'
        tree_list = [vender_name]
        tree = VenderTree(tree_list)
        self.assertEqual('vnd', tree.GetFacet())
        self.assertEqual(tree_list, tree.TreeList)
        self.assertEqual(vender_name, tree.VenderName)
