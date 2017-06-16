import unittest
from SubTypeTree import SubTypeTreeFactory
from SubTypeTree import VenderTreeFactory
from SubTypeTree import SubTypeTree
from SubTypeTree import VenderTree
from SubTypeTree import GitHubVenderTree
from SubTypeTree import StandardTree
from SubTypeTree import ParsonalTree
from SubTypeTree import UnregisteredTree
class TestSubType(unittest.TestCase):
    # application/vnd.github.v3
    def test_GitHubVenderTree1(self):
        facet = 'vnd'
        vender_name = 'github'
        version = 'v3'
        sub_type_string = "{facet}.{vender_name}.{version}".format(facet=facet, vender_name=vender_name, version=version)
#        subtype = SubTypeTreeFactory.Create(facet, sub_type_string.split('.')[1:-1])
        subtype = SubTypeTreeFactory.Create(facet, sub_type_string.split('.')[1:])
        self.assertTrue(isinstance(subtype, (SubTypeTree, VenderTree, GitHubVenderTree)))
        self.assertEqual(facet, GitHubVenderTree.GetFacet())
#        print("TreeList={0}".format(subtype.TreeList))
        self.assertEqual(vender_name, subtype.VenderName)
        self.assertEqual(facet, subtype.GetFacet())
        self.assertTrue(isinstance(subtype, (SubTypeTree, VenderTree, GitHubVenderTree)))
#        print(subtype.mro())
#        self.assertTrue(hasattr('Version', subtype))
        self.assertEqual(version, subtype.Version)
        self.assertEqual(None, subtype.Parameter)
        self.assertEqual(vender_name, subtype.VenderName)
        self.assertEqual(facet, subtype.GetFacet())
    # application/vnd.github.v3.raw+json (suffixはSubTypeクラスで取得する。facetのプロパティはSubTypeクラスで実装する)
    def test_GitHubVenderTree2(self):
        facet = 'vnd'
        vender_name = 'github'
        version = 'v3'
        param = 'raw'
        sub_type_string = "{facet}.{vender_name}.{version}.{param}".format(facet=facet, vender_name=vender_name, version=version, param=param)
        subtype = SubTypeTreeFactory.Create(facet, sub_type_string.split('.')[1:])
        self.assertTrue(isinstance(subtype, (SubTypeTree, VenderTree, GitHubVenderTree)))
        self.assertEqual(facet, GitHubVenderTree.GetFacet())
        self.assertEqual(vender_name, subtype.VenderName)
        self.assertEqual(version, subtype.Version)
        self.assertEqual(param, subtype.Parameter)

    # vnd.github+json
    def test_GitHubVenderTree3(self):
        facet = 'vnd'
        vender_name = 'github'
        sub_type_string = "{facet}.{vender_name}".format(facet=facet, vender_name=vender_name)
        subtype = SubTypeTreeFactory.Create(facet, sub_type_string.split('.')[1:])
        self.assertTrue(isinstance(subtype, (SubTypeTree, VenderTree, GitHubVenderTree)))
        self.assertEqual(facet, GitHubVenderTree.GetFacet())
        self.assertEqual(vender_name, subtype.VenderName)
        self.assertEqual(None, subtype.Version)
        self.assertEqual(None, subtype.Parameter)

    # applicaiton/json
    def test_StandardTree1(self):
        facet = 'json'
        subtype = SubTypeTreeFactory.Create(facet, None)
        self.assertTrue(isinstance(subtype, StandardTree))
        self.assertEqual(None, StandardTree.GetFacet())
    def test_StandardTree2(self):
        facet = 'json'
        subtype = SubTypeTreeFactory.Create(facet, [])
        self.assertTrue(isinstance(subtype, StandardTree))
        self.assertEqual(None, StandardTree.GetFacet())
    def test_StandardTree3(self):
        subtype = SubTypeTreeFactory.Create(None, None)
        self.assertTrue(isinstance(subtype, StandardTree))
        self.assertEqual(None, StandardTree.GetFacet())
    def test_StandardTree4(self):
        subtype = SubTypeTreeFactory.Create(None, [])
        self.assertTrue(isinstance(subtype, StandardTree))
        self.assertEqual(None, StandardTree.GetFacet())
    def test_StandardTree3(self):
        subtype = SubTypeTreeFactory.Create("", None)
        self.assertTrue(isinstance(subtype, StandardTree))
        self.assertEqual(None, StandardTree.GetFacet())
    def test_StandardTree4(self):
        subtype = SubTypeTreeFactory.Create("", [])
        self.assertTrue(isinstance(subtype, StandardTree))
        self.assertEqual(None, StandardTree.GetFacet())

    # prs.tree1.tree2
    def test_ParsonalTree(self):
        facet = 'prs'
        tree_list_string = 'tree1.tree2'
        sub_type_string = '{facet}.{tree_list_string}'.format(facet=facet, tree_list_string=tree_list_string)
        split = sub_type_string.split('.')
        subtype = SubTypeTreeFactory.Create(split[0], split[1:])
        self.assertTrue(isinstance(subtype, ParsonalTree))
        self.assertEqual('prs', ParsonalTree.GetFacet())
    
        """
        top_level_type = 'application'
        sub_type = 'json'
        mime_type = '{top_level_type}/{sub_type}'.format(top_level_type=top_level_type, sub_type=sub_type)
        char_set = 'utf-8'
        content_type = '{mime_type}; charset={char_set}'.format(mime_type=mime_type, char_set=char_set)
        response = Response()
#        c = Response.__Headers.__ContentType(content_type)

        res = requests.Response()
        res.headers = {}
        res.headers['Content-Type'] = '{mime_type}; charset={char_set};'.format(mime_type=mime_type, char_set=char_set)
        h = response._Response__Headers(res)
        c = h._Headers__ContentType(content_type)
        self.assertEqual(content_type, c.String)
        print(c.String)
        print(c.MimeType.TopLevelType)
        print(c.MimeType.String)
        self.assertEqual(mime_type, c.MimeType.String)
        self.assertTrue('charset' in c.Parameters.keys())
        self.assertEqual(char_set, c.Parameters['charset'])
        self.assertEqual(top_level_type, c.MimeType.TopLevelType)
        self.assertEqual(sub_type, c.MimeType.SubType.String)
        self.assertEqual(None, c.MimeType.SubType.Facet)
        self.assertEqual(None, c.MimeType.SubType.Suffix)
        self.assertEqual(sub_type, c.MimeType.SubType.MediaType)

    def test_MultiParameter(self):
        # https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E3%82%BF%E3%82%A4%E3%83%97#.E5.91.BD.E5.90.8D.E8.A6.8F.E5.89.87
        top_level_type = 'text'
        sub_type = 'plain'
        mime_type = '{top_level_type}/{sub_type}'.format(top_level_type=top_level_type, sub_type=sub_type)
        char_set = 'iso-2022-jp'
        res = requests.Response()
        res.headers = {}
        res.headers['Content-Type'] = '{mime_type}; charset={char_set}; format=flowed; delsp=yes'.format(mime_type=mime_type, char_set=char_set)
        c = Response.Headers.ContentType()
        c.Split(res)
        self.assertEqual(mime_type, c.mime_type)
        self.assertEqual(top_level_type, c.top_level_type)
        self.assertEqual(sub_type, c.sub_type)
        self.assertEqual(char_set, c.char_set)
        self.assertTrue('charset' in c.parameters.keys())
        self.assertEqual(char_set, c.parameters['charset'])
        self.assertTrue('format' in c.parameters.keys())
        self.assertEqual('flowed', c.parameters['format'])
        self.assertTrue('delsp' in c.parameters.keys())
        self.assertEqual('yes', c.parameters['delsp'])
        self.assertEqual(None, c.suffix)

    # バグ発見。suffixが取得できていなかった。
    def test_Suffix(self):
        # https://developer.github.com/v3/media/
        top_level_type = 'application'
        suffix = 'json'
        # サブタイプ名はツリー、サブタイプ名、サフィックスに分けられるらしい。が、細かすぎるのでまとめてサブタイプ名とした。
        # https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E3%82%BF%E3%82%A4%E3%83%97#.E5.91.BD.E5.90.8D.E8.A6.8F.E5.89.87
        sub_type = 'vnd.github.v3+{suffix}'.format(suffix=suffix)
        mime_type = '{top_level_type}/{sub_type}'.format(top_level_type=top_level_type, sub_type=sub_type)
        char_set = 'utf-8'
        res = requests.Response()
        res.headers = {}
        res.headers['Content-Type'] = '{mime_type}; charset={char_set}'.format(mime_type=mime_type, char_set=char_set)
        c = Response.Headers.ContentType()
        c.Split(res)
        self.assertEqual(mime_type, c.mime_type)
        self.assertEqual(top_level_type, c.top_level_type)
        self.assertEqual(sub_type, c.sub_type)
        self.assertEqual(char_set, c.char_set)
        self.assertTrue('charset' in c.parameters.keys())
        self.assertEqual(char_set, c.parameters['charset'])
        self.assertEqual(suffix, c.suffix)
"""
