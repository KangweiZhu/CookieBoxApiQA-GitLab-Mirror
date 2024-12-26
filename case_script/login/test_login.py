# -*- encoding: utf-8 -*-
"""
    @File    :   test_login.py.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/25/24 09:36    Anicaa (Kangwei Zhu)  1.0      
"""
import json

import jsonpath
import pytest

from case_script import testcase_bus
from context.response_context import context
from modal.test_case import ApiTestCase
from utils.request.http_request_util import HttpRequestUtil

project_name = '饼盒App'
module_name = '登陆模块'

def load_identifier(project_name, module_name):
    identifiers = list(testcase_bus[project_name][module_name].keys())
    return identifiers

def load_test_case(project_name, module_name):
    cases = list(testcase_bus[project_name][module_name].values())
    return cases

class TestLogin:

    @pytest.mark.parametrize(argnames="apitestcase", argvalues=load_test_case(project_name, module_name), ids=load_identifier(project_name, module_name))
    def test_login(self, apitestcase: ApiTestCase):
        resp = HttpRequestUtil(apitestcase).send_request()
        HttpRequestUtil.teardown_request(resp, apitestcase)
        print(json.dumps(context, indent=4, ensure_ascii=False))

