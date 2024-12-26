# -*- encoding: utf-8 -*-
"""
    @File    :   base_request_util.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/25/24 21:04    Anicaa (Kangwei Zhu)  1.0      
"""
import json

from jsonpath import jsonpath

from context.response_context import context
from modal.test_case import ApiTestCase


def protocol_formatter(protocol) -> str:
    return protocol + "://"


class BaseRequestUtil:
    @staticmethod
    def teardown_request(resp, apitestcase: ApiTestCase):
        if resp.text and apitestcase.context:
            json_resp = json.loads(resp.text)
            context_2b_set = apitestcase.context
            # for kvs in context_2b_set:
            #     range = kvs.get('range')
            #     if response_cache[range] is None:
            #         response_cache[range] = {}
            #     for key, value in kvs.items():
            #         if key != 'range':
            #             response_cache[range][key] = value
            for context_type, context_scopes in context_2b_set.items():
                context.setdefault(context_type, {})
                for context_scope, attributes in context_scopes.items():
                    context[context_type].setdefault(context_scope, {})
                    for name, value in attributes.items():
                        context[context_type][context_scope].setdefault(name, jsonpath(json_resp, value))