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

# identifiers = list(testcase_bus['饼盒App']['登陆模块'].keys())
project_name = '饼盒App'
module_name = '登陆模块'
# identifiers = [identifier for identifier in testcase_bus[project_name][module_name]]
# cases = [testcase_bus[project_name][module_name][identifier_name] for identifier_name in identifiers]


def load_identifier(project_name, module_name):
    identifiers = list(testcase_bus[project_name][module_name].keys())
    return identifiers

def load_test_case(project_name, module_name):
    cases = list(testcase_bus[project_name][module_name].values())
    return cases

class TestLogin:

    @pytest.mark.parametrize(argnames="test_case", argvalues=load_test_case(project_name, module_name), ids=load_identifier(project_name, module_name))
    def test_login(self, test_case):
        pass
