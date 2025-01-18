# -*- encoding: utf-8 -*-
'''
@File    :   assertion.py
@Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
@Description: 

@Modify Time      @Author               @Version    @Desciption
------------      -------------------   --------    -----------
1/17/25 05:15    Anicaa (Kangwei Zhu)  1.0         None
'''
import logging

from context.context import application_context
from modal.test_case import ApiTestCase
from utils.assertion import assertion_func
from utils.case.gen_util import load_module_func
from utils.misc.string_util import StringUtil


class Assertion:

    def __init__(self, apitestcase: ApiTestCase):
        self.apitestcase = apitestcase
        self.assertion_funcs = load_module_func(assertion_func)

    @staticmethod
    def error_message_formatter(apitestcase: ApiTestCase, assertionKey, actual, expected):
        return f"{apitestcase.identifier}: {assertionKey} 断言失败。期望：{expected}, 实际: {actual}"

    @staticmethod
    def correct_message_formatter(apitestcase: ApiTestCase, assertionKey):
        return f"{apitestcase.identifier}: {assertionKey} 断言成功"

    def do_assert(self):
        apitestcase = self.apitestcase
        assertion_dict = apitestcase.assertion
        if assertion_dict:
            for assertion_key, assertion_attrs in assertion_dict.items():
                actual = assertion_attrs.get('actual')
                expected = assertion_attrs.get('expected')
                if not actual or not expected:
                    logging.warn("assertion为空")
                    return
                expected_type = expected.get('type')
                expected_value = expected.get('value')
                actual = StringUtil.replace_jsonpath_in_string(application_context, actual, apitestcase.identifier)
                expected_value = StringUtil.replace_jsonpath_in_string(application_context, expected_value, apitestcase.identifier)
                error_message = assertion_attrs.get('error_message')
                if not error_message:
                    error_message = Assertion.error_message_formatter(apitestcase, assertion_key, actual, expected_value)
                self.assertion_funcs[expected_type](actual, expected_value, error_message)



