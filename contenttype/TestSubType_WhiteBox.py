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
# https://ja.wikipedia.org/wiki/%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E3%83%86%E3%82%B9%E3%83%88#.E3.83.9B.E3.83.AF.E3.82.A4.E3.83.88.E3.83.9C.E3.83.83.E3.82.AF.E3.82.B9.E3.83.86.E3.82.B9.E3.83.88.E3.81.A8.E3.83.96.E3.83.A9.E3.83.83.E3.82.AF.E3.83.9C.E3.83.83.E3.82.AF.E3.82.B9.E3.83.86.E3.82.B9.E3.83.88
class TestSubType(unittest.TestCase):
    # SubTypeStringに'.'が含まれていない(StandardTree)
    # SubTypeStringに'+'が含まれていない
    def test_Suffix_None(self):
        sub_type_string = 'html'
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(None, subtype.Facet)
        self.assertEqual(sub_type_string, subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, StandardTree))
    # SubTypeStringに'.'が含まれていない(StandardTree)
    # SubTypeStringに'+'が含まれている
    def test_Suffix_In(self):
        media_type = 'xhtml'
        suffix = 'xml'
        sub_type_string = '{media_type}+{suffix}'.format(media_type=media_type, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(None, subtype.Facet)
        self.assertEqual(media_type, subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, StandardTree))

    # SubTypeStringに'.'が含まれている(1つ UnregisteredTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_UnregistedTree1_NoneSuffix(self):
        facet = 'x'
        tree = 'tree1'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree, subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, UnregisteredTree))
    # SubTypeStringに'.'が含まれている(1つ UnregisteredTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれている
    def test_UnregistedTree1_Suffix(self):
        facet = 'x'
        tree = 'tree1'
        suffix = 'xml'
        sub_type_string = '{facet}.{tree}+{suffix}'.format(facet=facet, tree=tree, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree, subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, UnregisteredTree))
    # SubTypeStringに'.'が含まれている(1つ ParsonalTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_ParsonalTree1_NoneSuffix(self):
        facet = 'prs'
        tree = 'tree1'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree, subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, ParsonalTree))
    # SubTypeStringに'.'が含まれている(1つ ParsonalTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれている
    def test_ParsonalTree1_Suffix(self):
        facet = 'prs'
        tree = 'tree1'
        suffix = 'xml'
        sub_type_string = '{facet}.{tree}+{suffix}'.format(facet=facet, tree=tree, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree, subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, ParsonalTree))
    # SubTypeStringに'.'が含まれている(1つ VenderTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_VenderTree1_NoneSuffix(self):
        facet = 'vnd'
        tree = 'tree1'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree, subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, VenderTree))
    # SubTypeStringに'.'が含まれている(1つ VenderTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれている
    def test_VenderTree1_Suffix(self):
        facet = 'vnd'
        tree = 'tree1'
        suffix = 'xml'
        sub_type_string = '{facet}.{tree}+{suffix}'.format(facet=facet, tree=tree, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree, subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, VenderTree))
    # 未定義のファセット [x, prs, vnd]以外
    #   SubTypeStringに'.'が含まれている(1つ ????? [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_UnDefinedTree1_NoneSuffix(self):
        facet = '?????'
        tree = 'tree1'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        with self.assertRaises(Exception) as e:
            c.BoolToInt(value)
            subtype = SubType(sub_type_string)
            self.assertEqual(e.msg, '未定義のファセットです。ファセットは {facets} のうちのどれかにしてください。入力値: {facet}'.format('vnd,prs,x', facet))

    # SubTypeStringに'.'が含まれている(1つ)
    # SubTypeStringに'.'が含まれている(2つ)
    # SubTypeStringに'.'が含まれている(3つ)
    # 未定義のファセット [x, prs, vnd]以外
    
    
    
    # SubTypeStringに'.'が含まれている(2つ UnregisteredTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_UnregistedTree2_NoneSuffix(self):
        facet = 'x'
        tree = 'tree1.tree2'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, UnregisteredTree))
    # SubTypeStringに'.'が含まれている(2つ UnregisteredTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれている
    def test_UnregistedTree2_Suffix(self):
        facet = 'x'
        tree = 'tree1.tree2'
        suffix = 'xml'
        sub_type_string = '{facet}.{tree}+{suffix}'.format(facet=facet, tree=tree, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, UnregisteredTree))
    # SubTypeStringに'.'が含まれている(2つ ParsonalTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_ParsonalTree2_NoneSuffix(self):
        facet = 'prs'
        tree = 'tree1.tree2'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, ParsonalTree))
    # SubTypeStringに'.'が含まれている(2つ ParsonalTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれている
    def test_ParsonalTree2_Suffix(self):
        facet = 'prs'
        tree = 'tree1.tree2'
        suffix = 'xml'
        sub_type_string = '{facet}.{tree}+{suffix}'.format(facet=facet, tree=tree, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, ParsonalTree))
    # SubTypeStringに'.'が含まれている(2つ VenderTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_VenderTree2_NoneSuffix(self):
        facet = 'vnd'
        tree = 'tree1.tree2'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, VenderTree))
    # SubTypeStringに'.'が含まれている(2つ VenderTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれている
    def test_VenderTree2_Suffix(self):
        facet = 'vnd'
        tree = 'tree1.tree2'
        suffix = 'xml'
        sub_type_string = '{facet}.{tree}+{suffix}'.format(facet=facet, tree=tree, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, VenderTree))
    # 未定義のファセット [x, prs, vnd]以外
    #   SubTypeStringに'.'が含まれている(2つ ????? [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_UnDefinedTree2_NoneSuffix(self):
        facet = '?????'
        tree = 'tree1.tree2'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        with self.assertRaises(Exception) as e:
            c.BoolToInt(value)
            subtype = SubType(sub_type_string)
            self.assertEqual(e.msg, '未定義のファセットです。ファセットは {facets} のうちのどれかにしてください。入力値: {facet}'.format('vnd,prs,x', facet))

    
    # SubTypeStringに'.'が含まれている(3つ UnregisteredTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_UnregistedTree3_NoneSuffix(self):
        facet = 'x'
        tree = 'tree1.tree2.tree3'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, UnregisteredTree))
    # SubTypeStringに'.'が含まれている(3つ UnregisteredTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれている
    def test_UnregistedTree3_Suffix(self):
        facet = 'x'
        tree = 'tree1.tree2.tree3'
        suffix = 'xml'
        sub_type_string = '{facet}.{tree}+{suffix}'.format(facet=facet, tree=tree, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, UnregisteredTree))
    # SubTypeStringに'.'が含まれている(3つ ParsonalTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_ParsonalTree3_NoneSuffix(self):
        facet = 'prs'
        tree = 'tree1.tree2.tree3'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, ParsonalTree))
    # SubTypeStringに'.'が含まれている(3つ ParsonalTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれている
    def test_ParsonalTree3_Suffix(self):
        facet = 'prs'
        tree = 'tree1.tree2.tree3'
        suffix = 'xml'
        sub_type_string = '{facet}.{tree}+{suffix}'.format(facet=facet, tree=tree, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, ParsonalTree))
    # SubTypeStringに'.'が含まれている(3つ VenderTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_VenderTree3_NoneSuffix(self):
        facet = 'vnd'
        tree = 'tree1.tree2.tree3'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(None, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, VenderTree))
    # SubTypeStringに'.'が含まれている(3つ VenderTree [x, prs, vnd])
    # SubTypeStringに'+'が含まれている
    def test_VenderTree2_Suffix(self):
        facet = 'vnd'
        tree = 'tree1.tree2'
        suffix = 'xml'
        sub_type_string = '{facet}.{tree}+{suffix}'.format(facet=facet, tree=tree, suffix=suffix)
        subtype = SubType(sub_type_string)
        self.assertEqual(sub_type_string, subtype.String)
        self.assertEqual(facet, subtype.Facet)
        self.assertEqual(tree.split('.')[-1], subtype.MediaType)
        self.assertEqual(suffix, subtype.Suffix)
        self.assertTrue(isinstance(subtype.Tree, VenderTree))
    # 未定義のファセット [x, prs, vnd]以外
    #   SubTypeStringに'.'が含まれている(3つ ????? [x, prs, vnd])
    # SubTypeStringに'+'が含まれていない
    def test_UnDefinedTree3_NoneSuffix(self):
        facet = '?????'
        tree = 'tree1.tree2.tree3'
        sub_type_string = '{facet}.{tree}'.format(facet=facet, tree=tree)
        with self.assertRaises(Exception) as e:
            c.BoolToInt(value)
            subtype = SubType(sub_type_string)
            self.assertEqual(e.msg, '未定義のファセットです。ファセットは {facets} のうちのどれかにしてください。入力値: {facet}'.format('vnd,prs,x', facet))

