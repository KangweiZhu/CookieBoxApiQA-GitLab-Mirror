# -*- encoding: utf-8 -*-
"""
    @File    :   yaml_util.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 读yaml文件

    @Modify Time      @Author               @Version
    ------------      -------------------   --------
    12/20/24 07:55    Anicaa (Kangwei Zhu)  1.0
"""
import os
import yaml

from os import DirEntry
from typing import Optional, Dict
from exception.yaml_exceptions import YamlDataFieldMissingException, YamlSummaryMissingException
from modal.test_case import ApiTestCase


class YamlUtil:

    def __init__(self):
        pass

    @staticmethod
    def read_yaml_data(filepath) -> dict:
        """
        读取原始的yaml数据

        :param filepath: 相对路径，以 / 开头
        :return: 处理好的，dict类型的yaml数据
        """
        with open(filepath, 'r') as test_case_file:
            raw_data = yaml.safe_load(test_case_file)
        return raw_data

    @staticmethod
    def validate_case_data_yaml(raw_data: dict[str, any]):
        """
        校验yaml测试用例，注意只有被validated的才需要被教研

        :param raw_data:
        :return:
        """
        pass

    @staticmethod
    def extract_case_data_yaml(raw_data: dict[str, any], yaml_filepath: str) -> dict[str, dict[str, dict[str, ApiTestCase]]]:
        """
        从yaml文件中提取项目，模块信息，以及封装每个testcase对象，存储到testcase容器中.
        TestCase容器中存放：项目名: 模块名：ApiTestCase的list

        :param raw_data: 被解析好的单个yaml文件
        :return: 返回一个
        """

        def get_summary(yaml_data) -> dict[str, any]:
            summary = yaml_data.get('summary')
            if summary is None:
                raise YamlSummaryMissingException(yaml_filepath)
            else:
                return summary

        def get_project(summary) -> str:
            project = summary.get('project')
            if project is None:
                raise YamlSummaryMissingException(yaml_filepath)
            return project

        def get_module(summary) -> str:
            module = summary.get('module')
            if module is None:
                raise YamlSummaryMissingException(yaml_filepath)
            return module

        def get_protocol(case_data, **kwargs) -> str:
            protocol = case_data.get('protocol')
            if protocol is None:
                kwargs['field'] = 'protocol'
                raise YamlDataFieldMissingException(**kwargs)
            return protocol

        def get_host(case_data, **kwargs) -> list[str]:
            hosts = case_data.get('hosts')
            if hosts is None:
                kwargs['field'] = 'host'
                raise YamlDataFieldMissingException(**kwargs)
            return [ip.strip() for ip in hosts.split(',')]

        def get_method(case_data, **kwargs) -> str:
            method: str = case_data.get('method')
            if method is None:
                kwargs['field'] = 'method'
                raise YamlDataFieldMissingException(**kwargs)
            return method.strip().upper()

        def get_api(case_data, **kwargs) -> str:
            api = case_data.get('api')
            if api is None:
                kwargs['field'] = 'api'
                raise YamlDataFieldMissingException(**kwargs)
            return api.strip()

        def get_params(case_data) -> dict[any, any]:
            params = case_data.get('params')
            return params

        def get_headers(case_data) -> dict[any, any]:
            header = case_data.get('headers')
            return header

        def get_data(case_data) -> dict[any, any]:
            data = case_data.get('data')
            return data

        def get_context(case_data, **kwargs) -> dict[str, dict[str, dict[any, any]]]:
            context = case_data.get('context')
            return context

        def get_description(case_data) -> any:
            description = case_data.get('description')
            return description

        def get_sql(case_data) -> Optional[Dict[str, any]]:
            sql = case_data.get('sql')
            return sql

        summary = get_summary(raw_data)
        project = get_project(summary)
        module = get_module(summary)
        exception_message_fields = {'project': project, 'module': module}
        testcase_container = {project: {module: {}}}
        for key in raw_data:
            if key != 'summary':
                identifier = key
                case_data = raw_data[key]
                exception_message_fields['identifier'] = identifier
                hosts = get_host(case_data, **exception_message_fields)
                num_hosts = len(hosts)
                for host in hosts:
                    identifier = f'{identifier}-{host}' if num_hosts > 1 else identifier
                    testcase = ApiTestCase(
                        project=project,
                        module=module,
                        identifier=identifier,
                        protocol=get_protocol(case_data, **exception_message_fields),
                        host=host,
                        method=get_method(case_data, **exception_message_fields),
                        api=get_api(case_data, **exception_message_fields),
                        params=get_params(case_data),
                        headers=get_headers(case_data),
                        data=get_data(case_data),
                        context=get_context(case_data, **exception_message_fields),
                        description=get_description(case_data),
                        sql=get_sql(case_data)
                    )
                    testcase_container[project][module][identifier] = testcase
                    identifier = key
        return testcase_container

    @staticmethod
    def scan_yaml_file(dirpath: str) -> list[DirEntry[str]]:
        """
        扫描一个目录下的所有yaml文件

        :param dirpath: 要扫描的目录
        :return: list[str] 所有yaml文件
        """
        scan_result = []
        for entry in os.scandir(dirpath):
            if entry.is_dir():
                scan_result.extend(YamlUtil.scan_yaml_file(entry.path))
            else:
                if entry.is_file() and entry.name.endswith('.yaml'):
                    scan_result.append(entry)
        return scan_result


if __name__ == '__main__':
    pass
