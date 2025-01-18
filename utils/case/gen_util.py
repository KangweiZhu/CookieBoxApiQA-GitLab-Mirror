# -*- encoding: utf-8 -*-
'''
@File    :   gen_util.py.py
@Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
@Description: 

@Modify Time      @Author               @Version    @Desciption
------------      -------------------   --------    -----------
12/29/24 09:52    Anicaa (Kangwei Zhu)  1.0         None
'''
from collections import defaultdict
from types import FunctionType

from case_script import testcase_bus
from utils.assertion import assertion_func
from utils.misc.dict_util import DictUtil


def load_identifier(project_name, module_name):
    identifiers = list(testcase_bus[project_name][module_name].keys())
    return identifiers

def load_test_case(project_name, module_name):
    cases = list(testcase_bus[project_name][module_name].values())
    return cases

def load_module_func(python_module):
    functions = defaultdict(DictUtil.dict_recursive_init)

    for name, attr_type in vars(python_module).items():
        if isinstance(attr_type, FunctionType):
            functions[name] = attr_type

    return functions

# print(vars(assertion_func))
