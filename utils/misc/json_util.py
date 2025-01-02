from typing import Optional
from jsonpath import jsonpath
from exception.yaml_exceptions import YamlJsonpathStrParsingException
from modal.test_case import ApiTestCase
from utils.misc.string_util import StringUtil


class JsonUtil:

    @staticmethod
    def default_serializer(obj):
        if isinstance(obj, ApiTestCase):
            return obj.beautifier()
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    @staticmethod
    def resolve_jsonpath(jsonobj, path, indentifier, key) -> Optional[str]:
        stack = []
        stringbuilder = ''
        if StringUtil.is_null(path):
            return path
        for ch in path:
            if ch == '{':
                stack.append(stringbuilder)
                stringbuilder = ''
            elif ch == '}':
                parsed_value = jsonpath(jsonobj, stringbuilder)
                if parsed_value is None:
                    raise YamlJsonpathStrParsingException(stringbuilder)
                prev_stringbuilder = stack.pop()
