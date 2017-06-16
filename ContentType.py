#!python3
#encoding:utf-8
import re
from requests.structures import CaseInsensitiveDict
"""
ContentType
{MimeType}; {Parameter}
Parameter = Key1=Value1; Key2=Value2; Key3=Value3; ...
"""
class ContentType(object):
    def __init__(self, content_type_string):
        self.__re_charset = re.compile(r'charset=', re.IGNORECASE)
        self.__string = None # application/json; charset=utf8
        self.__mime_type = None # application/json
        self.__parameters = None # charset=utf-8
        self.__Load(content_type_string)
    @property
    def String(self):
        return self.__string
    @property
    def MimeType(self):
        return self.__mime_type
    @property
    def Parameters(self):
        return self.__parameters
    def __Load(self, content_type_string):
        self.__string = content_type_string
        if None is self.__string:
            self.__mime_type = None
            self.__parameters = None
        content_types = self.__string.split(';')
        self.__mime_type = self._ContentType__MimeType(content_types[0])
        if 1 < len(content_types):
            parameters = content_types[1:]
            self.__parameters = {}
            for p in parameters:
                p = p.strip()
                if 0 == len(p):
                    continue
                key, value = p.split('=')
                self.__parameters.update({key.strip(): value.strip()})
            self.__parameters = CaseInsensitiveDict(self.__parameters)    
    """
    {TopLevelType}/{SubType}
    """
    class __MimeType(object):
        def __init__(self, mime_type_string):
            self.__string = None
            self.__top_level_type = None
            self.__sub_type = None
            self.__Load(mime_type_string)
        @property
        def String(self):
            return self.__string
        @property
        def TopLevelType(self):
            return self.__top_level_type
        @property
        def SubType(self):
            return self.__sub_type
        def __Load(self, mime_type_string):
            self.__string = mime_type_string.strip()
            if None is self.__string:
                self.__top_level_type = None
                self.__sub_type = None
                self.__suffix = None
            else:
                types = self.__string.split('/')
                if 2 != len(types):
                    raise Exception('MimeTypeは {TopLevelType}/{SubType} の書式である必要があります。入力値: ' + self.__string)
                self.__top_level_type = types[0]
                self.__sub_type = self._MimeType__SubType(types[1])
        """
        {Tree}.{MediaType}+{Suffix}
        Tree = {Facet}.{Tree1.Tree2...}。ファセットごとに構成が異なる。https://developer.github.com/v3/media/
        本当は"vnd.github"固有クラスを作って定義するのが理想だが、細かすぎて実装する必要性を見つけられないので見送る。
        """
        class __SubType(object):
            def __init__(self, sub_type_string):
                self.__string = None
                self.__facet = None
                self.__media_type = None
                self.__suffix = None
                self.__Load(sub_type_string)
            @property
            def String(self):
                return self.__string
            @property
            def Facet(self):
                return self.__facet
            @property
            def MediaType(self):
                return self.__media_type
            @property
            def Suffix(self):
                return self.__suffix
            def __Load(self, sub_type_string):
                self.__string = sub_type_string
                tree = sub_type_string
                if '+' in sub_type_string:
                    tree, self.__suffix = self.__tree.split('+')
                else:
                    self.__suffix = None
                breadcrumbs = tree.split('.') # パンくずリスト
                if 1 == len(breadcrumbs):
                    self.__media_type = breadcrumbs[0]
                    self.__facet = None
                else:
                    self.__facet = breadcrumbs[0]
                    self.__media_type = breadcrumbs[-1]
                    
                    
            class __SubTypeTree(metaclass=ABCmeta)
