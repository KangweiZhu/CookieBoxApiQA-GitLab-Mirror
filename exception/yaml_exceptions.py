# -*- encoding: utf-8 -*-
"""
    @File    :   yaml_exceptions.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/24/24 05:28    Anicaa (Kangwei Zhu)  1.0
"""


def generate_data_field_incorrect_message(**kwargs):
    return '[{project}][{module}]异常，原因: 测试用例 [{identifier}] 的 {field} 属性填写错误'.format(**kwargs)


def generate_data_field_missing_message(**kwargs):
    return '[{project}][{module}]异常，原因: 测试用例 [{identifier}] 的 {field} 属性不能为空'.format(**kwargs)


def generate_context_range_missing_message(**kwargs):
    return '[{project}][{module}]异常，原因: 测试用例 [{identifier}] 的第 {count} 个 {field} 属性不存在，而这个属性被要求必须存在。'.format(
        **kwargs)


def generate_summary_missing_message(yaml_filepath: str):
    return f'[{yaml_filepath}]文件 summary 部分异常，请检查summary是否存在，并补全项目名和模块名'


def generate_jsonpath_incorrect_message(jsonpath):
    return f'无法在ApplicationContext中找到 {jsonpath} 对应的值哦，看看是不是写错了？'


def generate_jsonpath_str_parsing_message(error_identifier, str_w_jsonpath):
    return f'{error_identifier}: 这条带有jsonpath的属性解析失败了: {str_w_jsonpath}'


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


class YamlJsonpathIncorrectException(BaseException):

    def __init__(self, json_path: str):
        message = generate_jsonpath_incorrect_message(json_path)
        super().__init__(message)


class YamlJsonpathStrParsingException(BaseException):

    def __init__(self, error_identifier, str_w_jsonpath: str):
        message = generate_jsonpath_str_parsing_message(error_identifier, str_w_jsonpath)
        super().__init__(message)
