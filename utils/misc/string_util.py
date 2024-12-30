# -*- encoding: utf-8 -*-
'''
@File    :   string_util.py
@Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
@Description: 

@Modify Time      @Author               @Version    @Desciption
------------      -------------------   --------    -----------
12/29/24 13:19    Anicaa (Kangwei Zhu)  1.0         None
'''
from typing import Optional


class StringUtil(object):

    @staticmethod
    def is_null(s: Optional[str]) -> bool:
        return s is None or s.strip() == ""

    @staticmethod
    def replace_jsonpath_in_string(s:str, context: dict) -> str:
        while '{$' in s and '}' in s:
            start = s.find('{$')
            end = s.find('}', start)
            jsonpath_expr = s[start+2:end]

