import unittest
from SubTypeTree import SubTypeTreeFactory
from SubTypeTree import VenderTreeFactory
from SubTypeTree import SubTypeTree
from SubTypeTree import VenderTree
from SubTypeTree import GitHubVenderTree
from SubTypeTree import StandardTree
from SubTypeTree import ParsonalTree
from SubTypeTree import UnregisteredTree
class TestSubTypeTree_BlackBox(unittest.TestCase):
    def test_GetFacet(self):
        self.assertEqual(None, SubTypeTree.GetFacet())

