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
    def test_SubType1(self):
        facet = 'vnd'
        vender_name = 'github'
        version = 'v3'
        param = 'raw'
        suffix = 'json'
        tree_list = "{vender_name}.{version}.{param}".format(vender_name=vender_name, version=version, param=param)
        sub_type_string = "{facet}.{tree_list}+{suffix}".format(facet=facet, tree_list=tree_list, suffix=suffix)
#        sub_type_string = "{facet}.{vender_name}.{version}.{param}+{suffix}".format(facet=facet, vender_name=vender_name, version=version, param=param, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree_list.split('.')[-1], subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, GitHubVenderTree))
        self.assertEqual(version, subtype.Tree.Version)
        self.assertEqual(param, subtype.Tree.Parameter)
    # application/vnd.github.v3+json
    def test_SubType2(self):
        facet = 'vnd'
        vender_name = 'github'
        version = 'v3'
        suffix = 'json'
        tree_list = "{vender_name}.{version}".format(vender_name=vender_name, version=version)
        sub_type_string = "{facet}.{tree_list}+{suffix}".format(facet=facet, tree_list=tree_list, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree_list.split('.')[-1], subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, GitHubVenderTree))
        self.assertEqual(version, subtype.Tree.Version)
        self.assertEqual(None, subtype.Tree.Parameter)
    # application/vnd.github.v3
    def test_SubType3(self):
        facet = 'vnd'
        vender_name = 'github'
        version = 'v3'
        tree_list = "{vender_name}.{version}".format(vender_name=vender_name, version=version)
        sub_type_string = "{facet}.{tree_list}".format(facet=facet, tree_list=tree_list)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree_list.split('.')[-1], subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, GitHubVenderTree))
        self.assertEqual(version, subtype.Tree.Version)
        self.assertEqual(None, subtype.Tree.Parameter)
    # application/vnd.github+json
    def test_SubType4(self):
        facet = 'vnd'
        vender_name = 'github'
        suffix = 'json'
        tree_list = "{vender_name}".format(vender_name=vender_name)
        sub_type_string = "{facet}.{tree_list}+{suffix}".format(facet=facet, tree_list=tree_list, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree_list.split('.')[-1], subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, GitHubVenderTree))
        self.assertEqual(None, subtype.Tree.Version)
        self.assertEqual(None, subtype.Tree.Parameter)
    # application/json
    def test_SubType5(self):
        sub_type_string = "json"
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertTrue(isinstance(subtype.Tree, StandardTree))
        self.assertTrue(sub_type_string, subtype.MediaType)
        self.assertEqual(None, subtype.Facet)
        self.assertEqual(None, subtype.Suffix)

