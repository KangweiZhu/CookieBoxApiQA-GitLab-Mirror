# -*- encoding: utf-8 -*-
'''
@File    :   gen_util.py.py
@Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
@Description: 

@Modify Time      @Author               @Version    @Desciption
------------      -------------------   --------    -----------
12/29/24 09:52    Anicaa (Kangwei Zhu)  1.0         None
'''
from case_script import testcase_bus


def load_identifier(project_name, module_name):
    identifiers = list(testcase_bus[project_name][module_name].keys())
    return identifiers

def load_test_case(project_name, module_name):
    cases = list(testcase_bus[project_name][module_name].values())
    return cases