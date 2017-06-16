import unittest
from SubTypeTree import SubTypeTreeFactory
from SubTypeTree import VenderTreeFactory
from SubTypeTree import SubTypeTree
from SubTypeTree import VenderTree
from SubTypeTree import GitHubVenderTree
from SubTypeTree import StandardTree
from SubTypeTree import ParsonalTree
from SubTypeTree import UnregisteredTree
class TestVenderTreeFactory_BlackBox(unittest.TestCase):
    # VenderTree, GitHubVenderTree
    def test_Create_UnRegisteredVenderTree(self):
        facet = 'vnd'
        tree = '?????'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, VenderTree))
    def test_Create_GitHubVenderTree(self):
        facet = 'vnd'
        tree = 'github'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, GitHubVenderTree))

