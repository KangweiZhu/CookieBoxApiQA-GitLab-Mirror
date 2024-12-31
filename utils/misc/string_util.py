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


class StringUtil(object):

    @staticmethod
    def is_null(s: Optional[str]) -> bool:
        return s is None or s.strip() == ""

    @staticmethod
    def replace_jsonpath_in_string(s:str, context: dict) -> str:
        while '{$' in s and '}' in s:
            start = s.find('{$')
            end = s.find('}', start)
            jsonpath_expr = s[start+1:end]
            value = jsonpath.jsonpath(context, jsonpath_expr)
            if value is False:
                raise YamlJsonpathStrParsingException(s)
            s = s.replace(s[start:end+1], value[0], 1)
        return s


if __name__ == '__main__':
    context = defaultdict(DictUtil.dict_recursive_init)
    context['response']['global']['token'] = 'haha'
    context['data'] = 'queshi'
    print(StringUtil.replace_jsonpath_in_string('Bearer {$.response.global.token} woshizhu{ {$.data}', context))