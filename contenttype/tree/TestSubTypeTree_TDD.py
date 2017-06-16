import unittest
from SubTypeTree import SubTypeTreeFactory
from SubTypeTree import VenderTreeFactory
from SubTypeTree import SubTypeTree
from SubTypeTree import VenderTree
from SubTypeTree import GitHubVenderTree
from SubTypeTree import StandardTree
from SubTypeTree import ParsonalTree
from SubTypeTree import UnregisteredTree
class TestSubTypeTree_TDD(unittest.TestCase):
    def test_SubTypeTreeFactory(self):
        self.assertTrue(hasattr(SubTypeTreeFactory, 'Create'))
    def test_VenderTreeFactory(self):
        self.assertTrue(hasattr(VenderTreeFactory, 'Create'))
    def test_SubTypeTree(self):
        self.assertTrue(hasattr(SubTypeTree, 'TreeList'))
        self.assertTrue(hasattr(SubTypeTree, 'GetFacet'))
    def test_StandardTree(self):
        self.assertTrue(hasattr(StandardTree, 'GetFacet'))
    def test_ParsonalTree(self):
        self.assertTrue(hasattr(ParsonalTree, 'GetFacet'))
    def test_UnregisteredTree(self):
        self.assertTrue(hasattr(UnregisteredTree, 'GetFacet'))
    def test_VenderTree(self):
        self.assertTrue(hasattr(VenderTree, 'TreeList'))
        self.assertTrue(hasattr(GitHubVenderTree, 'VenderName'))
    def test_GitHubVenderTree(self):
        self.assertTrue(hasattr(GitHubVenderTree, 'GetFacet'))
        self.assertTrue(hasattr(GitHubVenderTree, 'GetVenderName'))
        self.assertTrue(hasattr(GitHubVenderTree, 'Version'))
        self.assertTrue(hasattr(GitHubVenderTree, 'Parameter'))
