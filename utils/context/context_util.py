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


class ContextUtil:

    @staticmethod
    def get_value_from_jsonpath(context, path):
        json_context = json.dumps(context)
        return jsonpath.jsonpath(json_context, path)

