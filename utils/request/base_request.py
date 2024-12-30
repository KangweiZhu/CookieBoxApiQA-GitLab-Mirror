import json
import logging
from typing import Optional, Dict, Any

import requests
from jsonpath import jsonpath

from modal.test_case import ApiTestCase
from utils.context.context_util import ContextUtil
from context.response_context import context


def protocol_formatter(protocol: str) -> str:
    return f"{protocol}://"

class BaseRequest:

    def __init__(self, apitestcase: ApiTestCase):
        self.apitestcase = apitestcase

    def sanitize_headers(self, context: Dict[str, Any], header: Optional[Dict[str, str]]) -> Optional[Dict[str, str]]:
        if not header or not context:
            return header

        for key, path in header.items():
            value = ContextUtil.get_value_from_jsonpath(context, path)
            if value:
                header[key] = value
        return header

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
                        extracted_value = jsonpath(json_resp, value)
                        if extracted_value:
                            context[context_type][scope][name] = extracted_value
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode response JSON: {e}")
        except Exception as e:
            logging.error(f"Unexpected error in teardown_request: {e}")