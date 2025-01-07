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
        """
        尝试对字符串进行解析
        如果字符串是空，直接返回。如果字符串以$开头，直接解析。如果字符串没有$，那直接返回，没有解析的必要，避免raise error。
        :param json_obj:
        :param s:
        :param error_identifier:
        :return:
        """
        if StringUtil.is_null(s):
            return s
        if s.strip().startswith('$'):
            return JsonUtil.parse_jsonpath(json_obj, s, error_identifier)
        if '$' not in s:
            return s
        stack = []
        stringbuilder = ""
        for ch in s:
            if ch == '{':
                stack.append(stringbuilder)
                stringbuilder = ""
            elif ch == '}':
                value = JsonUtil.parse_jsonpath(json_obj, stringbuilder, error_identifier)
                prev_stringbuilder = stack.pop()
                stringbuilder = prev_stringbuilder + value
            else:
                stringbuilder += ch
        if stringbuilder and stringbuilder.startswith('$'):
            value = JsonUtil.parse_jsonpath(json_obj, stringbuilder, error_identifier)
            stringbuilder = value
        return stringbuilder

if __name__ == '__main__':
    context = defaultdict(DictUtil.dict_recursive_init)
    context['response']['global']['token'] = 'haha'
    context['data'] = 'queshi'
    print(StringUtil.replace_jsonpath_in_string(context, 'Bearer {$.response.global.token} woshizhu{ {$.data}', 1))