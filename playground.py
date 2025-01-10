# -*- encoding: utf-8 -*-
"""
    @File    :   playground.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description:

    @Modify Time      @Author               @Version
    ------------      -------------------   --------
    12/25/24 21:25    Anicaa (Kangwei Zhu)  1.0
"""
from collections import defaultdict

from jsonpath import jsonpath

from utils.misc.dict_util import DictUtil

# playground 1: Test sending request
# request_url = 'http://127.0.0.1:8080/api/auth/login'
# resp = requests.request(
#     method='POST',
#     url=request_url,
#     headers={'Content-Type': 'application/json'},
#     params=None,
#     data=json.dumps({'username': 'bakahentai', 'password': 'bakahentai'}),
#     timeout=5
# )
# print(resp.text)
# print(resp)
# json_resp = json.loads(resp.text)
# jsonpathdata = jsonpath(json_resp, '$.data.token')
# print(jsonpathdata)
# yaml_file = YamlUtil.read_yaml_data(data_dir + '/aaa.yaml')
# print(yaml_file)

# playground 2: test our json yaml parser
#
# Bearer {$.{$config.range}.data.token} aaaa
#
# encountered } => $config.range is jsonpath? => get from context => $config.range = global
#
# pop from stack,  $.global.data.token => eWqweqeio1p23123mq
# stringbuilder.append a a a a
# if string is not empty:
#     Bearer eWqweqeio1p23123mq a a a a

# class JsonpathMismatchException(Exception):
#     def __init__(self, **kwargs):
#         super().__init__('测试用例{identifier}中的{key}字段在解析jsonpath时出现异常'.format(**kwargs))
#
# jsonobj = defaultdict(DictUtil.dict_recursive_init)
# jsonobj['config']['range'] = 'global'
# jsonobj['global']['data']['token'] = 'abcd'
# expectedResult = 'Bearer abcd'
# s = 'Bearer {$.{$.config.range}.data.token}'
# stack = []
# stringbuilder = ''
# if s == '':
#      print('')
# for ch in s
#     #print(stringbuilder, stack)
#
#     if ch == '{':
#         stack.append(stringbuilder)
#         stringbuilder = ''
#     elif ch == '}':
#         value = jsonpath(jsonobj, stringbuilder)
#         if value is False:
#             raise JsonpathMismatchException
#         prev_stringbuilder = stack.pop()
#         stringbuilder = prev_stringbuilder + value[0]
#     else:
#         stringbuilder += ch
# if stringbuilder.startswith('$'):
#     value = jsonpath(jsonobj, stringbuilder)
#     if value is False:
#         raise Exception("错啦错啦")
#     stringbuilder = value[0]
# assert stringbuilder == expectedResult


# import re

# from utils.misc.string_util import StringUtil

# sql = "insert into post (post_id, comment_id) values (%s, %s) [(1, one), (2,two), (3,three), (4,four)]"
#
# match = re.search(r'\[\((.*)\)]', sql)
# print(f'Match: {match}')
# if match:
#     group1 = match.group(1).strip() # group0是整个匹配到的字符串的完整输出，而group1是具体的匹配结果
#     group1 = group1.replace(' ', '')
#
#     datas = group1.split('),(')
#     result = list()
#
#     for data in datas:
#         data_list = data.split(',')
#         for i, element in enumerate(data_list):
#             if element.isnumeric():
#                 data_list[i] = int(data_list[i])
#         result.append(data_list)
#     print(result)

# print(StringUtil.sanitize_sql(sql))
# find_result = sql.find('[', 0)
# print(find_result)
# print(sql[:find_result - 1])

