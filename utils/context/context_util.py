# -*- encoding: utf-8 -*-
'''
@File    :   context_util.py
@Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
@Description: 

@Modify Time      @Author               @Version    @Desciption
------------      -------------------   --------    -----------
12/29/24 11:00    Anicaa (Kangwei Zhu)  1.0         None
'''
import json

import jsonpath

from exception.yaml_exceptions import YamlJsonpathIncorrectException
from utils.misc.string_util import StringUtil


class ContextUtil:

    @staticmethod
    def get_value_from_jsonpath(json, path: str):
        if path.startswith('$'):
            value = jsonpath.jsonpath(json, path)
            if value is False:
                raise YamlJsonpathIncorrectException(path)
            return value[0]
        else:
            return StringUtil.replace_jsonpath_in_string(path, json)