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

from case_script import apitestcase
from modal.test_case import ApiTestCase

class Assertion:

    def __init__(self, apitestcase: ApiTestCase):
        self.apitestcase = apitestcase

    @staticmethod
    def error_message_formatter(apitestcase: ApiTestCase, assertionKey, actual, expected):
        return f"{apitestcase.identifier}: {assertionKey} 断言失败。期望：{expected}, 实际: {actual}"

    @staticmethod
    def correct_message_formatter(apitestcase: ApiTestCase, assertionKey):
        return f"{apitestcase.identifier}: {assertionKey} 断言成功"

    def multi_assert(self):
        assertion_dict = apitestcase.assertion
        if assertion_dict:
            for assertion_key, assertion_attrs in assertion_dict.items():
                actual = assertion_attrs.get('actual')
                expected = assertion_attrs.get('expected')
                expected_type = expected.get('type')
                expected_value = expected.get('value')
                error_message = assertion_attrs.get('error_message')
                correct_message = assertion_attrs['correct_message']
                if not actual or not expected:
                    logging.warn("assertion为空")
                    return
                if not error_message:
                    error_message = Assertion.error_message_formatter(apitestcase, assertion_key, actual, expected)
                if not correct_message:
                    correct_message = Assertion.correct_message_formatter(apitestcase, assertion_key)
                if expected_type == 'not':
                    assert


