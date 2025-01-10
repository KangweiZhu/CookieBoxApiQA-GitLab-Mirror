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
import re
from collections import defaultdict
from typing import Optional, Tuple

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

    @staticmethod
    def sanitize_sql(sql: str) -> Tuple[list, str]:
        """

        例如
            sql = "insert into post (post_id, comment_id) values (%s, %s) [(1, one), (2,two), (3,three), (4,four)]"

        我们会将其进行拆分，分为两个部分。
            1. SQL部分: insert into post (post_id, comment_id) values (%s, %s)
            2. 数据部分: [(1, one), (2,two), (3,three), (4,four)]

        数据部分可以只有一个，也可以有多个。通过这种拆分，我们就可以直接用executemany，来方便地执行测试用例

        :param sql:
        :return:
        """
        final_datas = list()
        match = re.search('\[\((.*)\)\]', sql)
        if match:
            group1 = match.group(1).strip()
            group1 = group1.replace(' ', '')
            datas = group1.split('),(')

            for data in datas:
                elements = data.split(',')
                for index, element in enumerate(elements):
                    if element.isnumeric():
                        elements[index] = int(element)
                final_datas.append(elements)
        else:
            pass #raise exception

        sql_end_index = sql.find('[')
        if sql_end_index == -1:
            pass #raise exception
        else:
            sql = sql[:sql_end_index - 1]

        return final_datas, sql


if __name__ == '__main__':
    context = defaultdict(DictUtil.dict_recursive_init)
    context['response']['global']['token'] = 'haha'
    context['data'] = 'queshi'
    print(StringUtil.replace_jsonpath_in_string(context, 'Bearer {$.response.global.token} woshizhu{ {$.data}', 1))