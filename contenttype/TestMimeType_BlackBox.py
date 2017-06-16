import unittest
from MimeType import MimeType
from SubType import SubType
from tree.SubTypeTree import SubTypeTreeFactory
from tree.SubTypeTree import VenderTreeFactory
from tree.SubTypeTree import SubTypeTree
from tree.SubTypeTree import VenderTree
from tree.SubTypeTree import GitHubVenderTree
from tree.SubTypeTree import StandardTree
from tree.SubTypeTree import ParsonalTree
from tree.SubTypeTree import UnregisteredTree
class TestMimeType_BlackBox(unittest.TestCase):
    def test_Load_Exception_None(self):
        mime_type_string = None
        with self.assertRaises(Exception) as e:
            m = MimeType(mime_type_string)
            self.assertEqual(e.msg, 'MimeTypeは {TopLevelType}/{SubType} の書式である必要があります。' + '入力値: {0}'.format(mime_type_string))
    def test_Load_Exception_Blank(self):
        mime_type_string = ''
        with self.assertRaises(Exception) as e:
            m = MimeType(mime_type_string)
            self.assertEqual(e.msg, 'MimeTypeは {TopLevelType}/{SubType} の書式である必要があります。' + '入力値: {0}'.format(mime_type_string))
    def test_Load_Exception_NoneSlash(self):
        mime_type_string = 'NoneSlash'
        with self.assertRaises(Exception) as e:
            m = MimeType(mime_type_string)
            self.assertEqual(e.msg, 'MimeTypeは {TopLevelType}/{SubType} の書式である必要があります。' + '入力値: {0}'.format(mime_type_string))
    def test_Load_Exception_MultiSlash(self):
        mime_type_string = 'application/json/MultiSlash'
        with self.assertRaises(Exception) as e:
            m = MimeType(mime_type_string)
            self.assertEqual(e.msg, 'MimeTypeは {TopLevelType}/{SubType} の書式である必要があります。' + '入力値: {0}'.format(mime_type_string))
    def test_Load1(self):
        top_level_type = 'application'
        sub_type = 'json'
        mime_type_string = '{top_level_type}/{sub_type}'.format(top_level_type=top_level_type, sub_type=sub_type)
        mimetype = MimeType(mime_type_string)
        self.assertEqual(mime_type_string, mimetype.String)
        self.assertEqual(top_level_type, mimetype.TopLevelType)
        self.assertEqual(sub_type, mimetype.SubType.String)
