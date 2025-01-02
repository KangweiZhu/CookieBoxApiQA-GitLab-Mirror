# -*- encoding: utf-8 -*-
"""
    @File    :   json_exception.py.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    1/1/25 19:55    Anicaa (Kangwei Zhu)  1.0      
"""
class JsonpathMismatchException(Exception):
    def __init__(self, **kwargs):
        super().__init__('测试用例{identifier}中的{key}字段在解析jsonpath时出现异常'.format(**kwargs))
