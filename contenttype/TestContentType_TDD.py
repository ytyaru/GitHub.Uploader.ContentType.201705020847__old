import unittest
from ContentType import ContentType
from MimeType import MimeType
from SubType import SubType
class TestContentType_TDD(unittest.TestCase):
    def test_HasAttribute(self):
        self.assertTrue(hasattr(ContentType, 'String'))
        self.assertTrue(hasattr(ContentType, 'MimeType'))
        self.assertTrue(hasattr(ContentType, 'Parameters'))

