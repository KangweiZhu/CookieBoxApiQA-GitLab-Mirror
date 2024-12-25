# -*- encoding: utf-8 -*-
"""
    @File    :   test_login.py.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/25/24 09:36    Anicaa (Kangwei Zhu)  1.0      
"""
import pytest

from case_script import testcase_bus
from utils.request.http_util import HttpUtil

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
    def test_login(self, apitestcase):
        resp = HttpUtil(apitestcase).send_request()
        print(f'\n{resp}')
        print(resp.text)

