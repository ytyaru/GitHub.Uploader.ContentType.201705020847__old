import unittest
from SubTypeTree import SubTypeTreeFactory
from SubTypeTree import VenderTreeFactory
from SubTypeTree import SubTypeTree
from SubTypeTree import VenderTree
from SubTypeTree import GitHubVenderTree
from SubTypeTree import StandardTree
from SubTypeTree import ParsonalTree
from SubTypeTree import UnregisteredTree
class TestGitHubVenderTree_BlackBox(unittest.TestCase):
    def test_verNone_paramNone(self):
        vender_name = 'github'
        tree_list = [vender_name]
        tree = GitHubVenderTree(tree_list)
        self.assertEqual('vnd', tree.GetFacet())
        self.assertEqual(tree_list, tree.TreeList)
        self.assertEqual(vender_name, tree.VenderName)
        self.assertEqual(None, tree.Version)
        self.assertEqual(None, tree.Parameter)
    def test_verV3_paramNone(self):
        vender_name = 'github'
        version = 'v3'
        tree_list = [vender_name, version]
        tree = GitHubVenderTree(tree_list)
        self.assertEqual('vnd', tree.GetFacet())
        self.assertEqual(tree_list, tree.TreeList)
        self.assertEqual(vender_name, tree.VenderName)
        self.assertEqual(version, tree.Version)
        self.assertEqual(None, tree.Parameter)
    def test_verV3_paramRaw(self):
        vender_name = 'github'
        version = 'v3'
        param = 'raw'
        tree_list = [vender_name, version, param]
        tree = GitHubVenderTree(tree_list)
        self.assertEqual('vnd', tree.GetFacet())
        self.assertEqual(tree_list, tree.TreeList)
        self.assertEqual(vender_name, tree.VenderName)
        self.assertEqual(version, tree.Version)
        self.assertEqual(param, tree.Parameter)
    def test_listNumOver(self):
        vender_name = 'github'
        version = 'v3'
        param = 'raw'
        over = 'some'
        tree_list = [vender_name, version, param, over]
        tree = GitHubVenderTree(tree_list)
        self.assertEqual('vnd', tree.GetFacet())
        self.assertEqual(tree_list, tree.TreeList)
        self.assertEqual(vender_name, tree.VenderName)
        self.assertEqual(version, tree.Version)
        self.assertEqual(param, tree.Parameter)
