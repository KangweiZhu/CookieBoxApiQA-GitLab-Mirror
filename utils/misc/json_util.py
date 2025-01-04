from typing import Optional
from jsonpath import jsonpath
from exception.yaml_exceptions import YamlJsonpathStrParsingException
from modal.test_case import ApiTestCase


class JsonUtil:

    @staticmethod
    def default_serializer(obj):
        if isinstance(obj, ApiTestCase):
            return obj.beautifier()
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    @staticmethod
    def parse_jsonpath(json_obj, s, error_identifier):
        values = jsonpath(json_obj, s)
        if values is False:
            raise YamlJsonpathStrParsingException(error_identifier, s)
        return values