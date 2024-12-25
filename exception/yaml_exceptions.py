# -*- encoding: utf-8 -*-
"""
    @File    :   yaml_exceptions.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/24/24 05:28   Anicaa (Kangwei Zhu)  1.0      
"""


def generate_data_field_incorrect_message(**kwargs):
    return '[{project}][{module}]异常，原因: 测试用例[{identifier}]的{field}属性填写错误'.format(**kwargs)


def generate_data_field_missing_message(**kwargs):
    return '[{project}][{module}]异常，原因: 测试用例[{identifier}]的{field}属性不能为空'.format(**kwargs)


def generate_summary_missing_message(yaml_filepath: str):
    return f'[{yaml_filepath}]文件summary部分异常，请检查summary是否存在，并补全项目名和模块名'


"""
a = 3
b = 1
if a == b:
    raise YamlDataFieldIncorrectException(project='饼盒项目', module='用户登陆鉴权模块', identifier='auth_login_01', field='data')
"""


class YamlDataFieldIncorrectException(BaseException):

    def __init__(self, **kwargs):
        message = generate_data_field_incorrect_message(**kwargs)
        super().__init__(message)


class YamlDataFieldMissingException(BaseException):

    def __init__(self, **kwargs):
        message = generate_data_field_missing_message(**kwargs)
        super().__init__(message)


class YamlSummaryMissingException(BaseException):

    def __init__(self, yaml_filepath: str):
        message = generate_summary_missing_message(yaml_filepath)
        super().__init__(message)
