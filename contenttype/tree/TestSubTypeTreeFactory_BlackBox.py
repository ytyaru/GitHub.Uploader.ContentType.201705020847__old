import unittest
from SubTypeTree import SubTypeTreeFactory
from SubTypeTree import VenderTreeFactory
from SubTypeTree import SubTypeTree
from SubTypeTree import VenderTree
from SubTypeTree import GitHubVenderTree
from SubTypeTree import StandardTree
from SubTypeTree import ParsonalTree
from SubTypeTree import UnregisteredTree
class TestSubTypeTreeFactory_BlackBox(unittest.TestCase):
    # StandardTree, VenderTree(GitHubVenderTree), ParsonalTree, UnregisteredTree
    def test_Create_StandardTree_FacetNone_TreeNone(self):
        media_type = 'html'
        subtype = SubTypeTreeFactory.Create(None, None)
        self.assertTrue(isinstance(subtype, StandardTree))
    def test_Create_StandardTree_FacetNone_TreeBlank(self):
        media_type = 'html'
        subtype = SubTypeTreeFactory.Create(None, [])
        self.assertTrue(isinstance(subtype, StandardTree))        
    def test_Create_StandardTree_FacetNone_TreeBlankString(self):
        media_type = 'html'
        subtype = SubTypeTreeFactory.Create(None, [''])
        self.assertTrue(isinstance(subtype, StandardTree))
    def test_Create_StandardTree_FacetBlank_TreeNone(self):
        subtype = SubTypeTreeFactory.Create('', None)
        self.assertTrue(isinstance(subtype, StandardTree))
    def test_Create_StandardTree_FacetBlank_TreeBlank(self):
        subtype = SubTypeTreeFactory.Create('', [])
        self.assertTrue(isinstance(subtype, StandardTree))
    def test_Create_StandardTree_FacetBlank_TreeBlankString(self):
        subtype = SubTypeTreeFactory.Create('', [''])
        self.assertTrue(isinstance(subtype, StandardTree))

    def test_Create_UnregisteredTree_Tree1(self):
        facet = 'x'
        tree = 'tree1'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, UnregisteredTree))
    def test_Create_UnregisteredTree_Tree2(self):
        facet = 'x'
        tree = 'tree1.tree2'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, UnregisteredTree))
    def test_Create_UnregisteredTree_Tree3(self):
        facet = 'x'
        tree = 'tree1.tree2.tree3'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, UnregisteredTree))
    def test_Create_UnregisteredTree_Tree4(self):
        facet = 'x'
        tree = 'tree1.tree2.tree3.tree4'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, UnregisteredTree))
    def test_Create_UnregisteredTree_TreeBlank(self):
        facet = 'x'
        tree = '....'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, UnregisteredTree))
    
    def test_Create_ParsonalTree_Tree1(self):
        facet = 'prs'
        tree = 'tree1'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, ParsonalTree))
    def test_Create_ParsonalTree_Tree2(self):
        facet = 'prs'
        tree = 'tree1.tree2'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, ParsonalTree))
    def test_Create_ParsonalTree_Tree3(self):
        facet = 'prs'
        tree = 'tree1.tree2.tree3'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, ParsonalTree))
    def test_Create_ParsonalTree_Tree4(self):
        facet = 'prs'
        tree = 'tree1.tree2.tree3.tree4'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, ParsonalTree))
    def test_Create_ParsonalTree_TreeBlank(self):
        facet = 'prs'
        tree = '....'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, ParsonalTree))

    def test_Create_VenderTree_Tree1(self):
        facet = 'vnd'
        tree = 'tree1'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, VenderTree))
    def test_Create_VenderTree_Tree2(self):
        facet = 'vnd'
        tree = 'tree1.tree2'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, VenderTree))
    def test_Create_VenderTree_Tree3(self):
        facet = 'vnd'
        tree = 'tree1.tree2.tree3'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, VenderTree))
    def test_Create_VenderTree_Tree4(self):
        facet = 'vnd'
        tree = 'tree1.tree2.tree3.tree4'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, VenderTree))
    def test_Create_VenderTree_TreeBlank(self):
        facet = 'vnd'
        tree = '....'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, VenderTree))

    def test_Create_GitHubVenderTree_Tree1(self):
        facet = 'vnd'
        tree = 'github'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, GitHubVenderTree))
    def test_Create_GitHubVenderTree_Tree2(self):
        facet = 'vnd'
        tree = 'github.tree2'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, GitHubVenderTree))
    def test_Create_GitHubVenderTree_Tree3(self):
        facet = 'vnd'
        tree = 'github.tree2.tree3'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, GitHubVenderTree))
    def test_Create_GitHubVenderTree_Tree4(self):
        facet = 'vnd'
        tree = 'github.tree2.tree3.tree4'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, GitHubVenderTree))
    def test_Create_GitHubVenderTree_TreeBlank(self):
        facet = 'vnd'
        tree = 'github....'
        subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
        self.assertTrue(isinstance(subtype, GitHubVenderTree))
    
    def test_Create_UnDefinedFacet_Tree1(self):
        facet = '?????'
        tree = 'tree1'
        with self.assertRaises(Exception) as e:
            subtype = SubTypeTreeFactory.Create(facet, tree.split('.'))
            self.assertEqual(e.msg, '未定義のファセットです。ファセットは {facets} のうちのどれかにしてください。入力値: {facet}'.format('vnd,prs,x', facet))
