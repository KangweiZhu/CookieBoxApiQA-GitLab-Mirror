# -*- encoding: utf-8 -*-
'''
@File    :   string_util.py
@Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
@Description: 

@Modify Time      @Author               @Version    @Desciption
------------      -------------------   --------    -----------
12/29/24 13:19    Anicaa (Kangwei Zhu)  1.0         None
'''
import json
from collections import defaultdict
from typing import Optional

import jsonpath

from exception.yaml_exceptions import YamlJsonpathStrParsingException
from utils.misc.dict_util import DictUtil
from utils.misc.json_util import JsonUtil


def parse_jsonpath(json_obj, s, error_identifier):
    values = jsonpath.jsonpath(json_obj, s)
    if values is False:
        raise YamlJsonpathStrParsingException(s, error_identifier)
    return values

class StringUtil(object):

    @staticmethod
    def is_null(s: Optional[str]) -> bool:
        return s is None or s.strip() == ""

    @staticmethod
    def replace_jsonpath_in_string(json_obj: dict, s: Optional[str], error_identifier) -> Optional[str]:
        if StringUtil.is_null(s):
            return s
        stack = []
        stringbuilder = ""
        for ch in s:
            if ch == '{':
                stack.append(stringbuilder)
                stringbuilder = ""
            elif ch == '}':
                values = JsonUtil.parse_jsonpath(json_obj, s, error_identifier)
                prev_stringbuilder = stack.pop()
                stringbuilder = prev_stringbuilder + values[0]
            else:
                stringbuilder += ch
        if stringbuilder and stringbuilder.startswith('$'):
            values = JsonUtil.parse_jsonpath(json_obj, s, error_identifier)
            stringbuilder = values[0]
        return stringbuilder

if __name__ == '__main__':
    context = defaultdict(DictUtil.dict_recursive_init)
    context['response']['global']['token'] = 'haha'
    context['data'] = 'queshi'
    print(StringUtil.replace_jsonpath_in_string(context, 'Bearer {$.response.global.token} woshizhu{ {$.data}', 1))