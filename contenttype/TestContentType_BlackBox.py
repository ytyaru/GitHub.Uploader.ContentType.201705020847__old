import unittest
from ContentType import ContentType
from requests.structures import CaseInsensitiveDict
from MimeType import MimeType
from SubType import SubType
class TestContentType_BlackBox(unittest.TestCase):
    # text/plain; charset=iso-2022-jp; format=flowed; delsp=yes
    def test_MultiParameters(self):
        mime_type_string = 'text/plain'
        p_charset = 'charset=iso-2022-jp'
        p_format = 'format=flowed'
        p_delsp = 'delsp=yes'
        content_type_string = '{mime_type_string}; {p_charset}; {p_format}; {p_delsp}'.format(mime_type_string=mime_type_string, p_charset=p_charset, p_format=p_format, p_delsp=p_delsp)
#        content_type_string = 'text/plain; charset=iso-2022-jp; format=flowed; delsp=yes'
        c = ContentType(content_type_string)
        self.assertEqual(content_type_string, c.String)
        self.assertEqual(mime_type_string, c.MimeType.String)
        self.assertTrue(p_charset.split('=')[0] in c.Parameters)
        self.assertTrue(p_format.split('=')[0] in c.Parameters)
        self.assertTrue(p_delsp.split('=')[0] in c.Parameters)
        self.assertEqual(p_charset.split('=')[1], c.Parameters[p_charset.split('=')[0]])
        self.assertEqual(p_format.split('=')[1], c.Parameters[p_format.split('=')[0]])
        self.assertEqual(p_delsp.split('=')[1], c.Parameters[p_delsp.split('=')[0]])
    def test_CharsetParameters(self):
        mime_type_string = 'application/vnd.github.v3+json'
        p_charset = 'charset=utf-8'
        content_type_string = '{mime_type_string}; {p_charset}'.format(mime_type_string=mime_type_string, p_charset=p_charset)
        c = ContentType(content_type_string)
        self.assertEqual(content_type_string, c.String)
        self.assertEqual(mime_type_string, c.MimeType.String)
        self.assertTrue(p_charset.split('=')[0] in c.Parameters)
        self.assertEqual(p_charset.split('=')[1], c.Parameters[p_charset.split('=')[0]])
    def test_NoneParameters(self):
        mime_type_string = 'application/vnd.github.v3'
        content_type_string = '{mime_type_string}'.format(mime_type_string=mime_type_string)
        c = ContentType(content_type_string)
        self.assertEqual(content_type_string, c.String)
        self.assertEqual(mime_type_string, c.MimeType.String)
        self.assertEqual(None, c.Parameters)
    def test_BlankParameters(self):
        mime_type_string = 'application/vnd.github.v3'
        content_type_string = '{mime_type_string};'.format(mime_type_string=mime_type_string)
        c = ContentType(content_type_string)
        self.assertEqual(content_type_string, c.String)
        self.assertEqual(mime_type_string, c.MimeType.String)
        self.assertTrue(isinstance(c.Parameters, CaseInsensitiveDict))
        self.assertEqual(0, len(c.Parameters))
    def test_MultiBlankParameters(self):
        mime_type_string = 'application/vnd.github.v3'
        content_type_string = '{mime_type_string};; ; ;;'.format(mime_type_string=mime_type_string)
        c = ContentType(content_type_string)
        self.assertEqual(content_type_string, c.String)
        self.assertEqual(mime_type_string, c.MimeType.String)
        self.assertTrue(isinstance(c.Parameters, CaseInsensitiveDict))
        self.assertEqual(0, len(c.Parameters))
    def test_BrakeParameters(self):
        mime_type_string = 'application/vnd.github.v3'
        # parameterのうち'='区切りでない文字列は無視する
        content_type_string = '{mime_type_string}; BrakeParameter;'.format(mime_type_string=mime_type_string)
        c = ContentType(content_type_string)
        self.assertEqual(content_type_string, c.String)
        self.assertEqual(mime_type_string, c.MimeType.String)
        self.assertTrue(isinstance(c.Parameters, CaseInsensitiveDict))
        self.assertEqual(0, len(c.Parameters))
    def test_MixtureParameters_Blank_Brake_True(self):
        mime_type_string = 'application/vnd.github.v3'
        # parameterのうち'='区切りでない文字列は無視する
        content_type_string = '{mime_type_string}; ;; BrakeParameter;;charset=utf-8;'.format(mime_type_string=mime_type_string)
        c = ContentType(content_type_string)
        self.assertEqual(content_type_string, c.String)
        self.assertEqual(mime_type_string, c.MimeType.String)
        self.assertTrue(isinstance(c.Parameters, CaseInsensitiveDict))
        self.assertEqual(1, len(c.Parameters))
        self.assertTrue('charset' in c.Parameters)
        self.assertEqual('utf-8', c.Parameters['charset'])

