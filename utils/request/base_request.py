import json
import logging
from typing import Optional, Dict, Any, Union

import requests
from jsonpath import jsonpath

from modal.test_case import ApiTestCase
from context.response_context import context
from utils.misc.json_util import JsonUtil
from utils.misc.string_util import StringUtil


def url_formatter(**kwargs) -> str:
    return "{protocol}://{host}{api}".format(**kwargs)


class BaseRequest:

    def __init__(self, apitestcase: ApiTestCase):
        self.apitestcase = apitestcase

    @staticmethod
    def sanitize_data_fields(json_obj: dict, field: Union[str, Dict[str, str], None], error_identifier) -> \
    Union[str, Dict, None]:
        if not field or not json_obj:
            return field

        if isinstance(field, Dict):
            print(context)
            for key, s in field.items():
                print(s)
                value = StringUtil.replace_jsonpath_in_string(json_obj, s, error_identifier)
                field[key] = value
        elif isinstance(field, str):
            field = StringUtil.replace_jsonpath_in_string(json_obj, field, error_identifier)

        return field

    def teardown_request(self, resp: requests.Response) -> None:
        """
            request 结束后需要做的事

                1. 将整个resp转换成json，将testcase_id 和 这个json存放到上下文容器中。方便后面别的测试用例，依赖此测试用例的结果时，直接用这个测试用例的id取到json，并配合
                jsonpath拿到数据

                2. 自定义一些context，context可以有范围，比如global-全局，module-模块。这样，context['response']['global']['token'] = xxx; context['response']['module']['token'] = yyy,
                更加灵活一点。这里因为是request，所以context类型只有response。未来也可以自定义context类型，给定作用域以及名称，更灵活地控制上下文存的值。


        :param resp:
        :return:
        """
        apitestcase = self.apitestcase
        if not resp or not resp.text:
            return

        json_resp = resp.json()
        context[apitestcase.identifier] = json_resp
        if not apitestcase.context:
            return
        for context_type, context_scopes in apitestcase.context.items():
            context.setdefault(context_type, {})
            for scope, attributes in context_scopes.items():
                context[context_type].setdefault(scope, {})
                for name, json_expr in attributes.items():
                    extracted_value = JsonUtil.parse_jsonpath(json_resp, json_expr,
                                                              f'{apitestcase.identifier}-{scope}-{name}')
                    context[context_type][scope][name] = extracted_value[0]
