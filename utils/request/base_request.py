import json
import logging
from typing import Optional, Dict, Any

import requests
from jsonpath import jsonpath

from modal.test_case import ApiTestCase
from context.response_context import context
from utils.misc.string_util import StringUtil


def url_formatter(**kwargs) -> str:
    return "{protocol}://{host}{api}".format(**kwargs)

class BaseRequest:

    def __init__(self, apitestcase: ApiTestCase):
        self.apitestcase = apitestcase

    @staticmethod
    def sanitize_data_fields(json_obj: Dict[str, Any], field: Optional[Dict[str, str]]) -> Optional[Dict[str, str]]:
        if not field or not json_obj:
            return field

        for key, path in field.items():
            value = StringUtil.replace_jsonpath_in_string(json_obj, path)
            if value:
                field[key] = value
        return field

    def teardown_request(self, resp: requests.Response):
        apitestcase = self.apitestcase
        if not resp or not resp.text:
            return

        try:
            json_resp = resp.json()
            context[apitestcase.identifier] = json_resp

            if not apitestcase.context:
                return

            for context_type, context_scopes in apitestcase.context.items():
                context.setdefault(context_type, {})
                for scope, attributes in context_scopes.items():
                    context[context_type].setdefault(scope, {})
                    for name, value in attributes.items():
                        extracted_value = ContextUtil.get_value_from_jsonpath(json_resp, value)
                        if extracted_value:
                            context[context_type][scope][name] = extracted_value
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode response JSON: {e}")
        except Exception as e:
            logging.error(f"Unexpected error in teardown_request: {e}")