# -*- encoding: utf-8 -*-
"""
    @File    :   __init__.py.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/20/24 12:16    Anicaa (Kangwei Zhu)  1.0
"""
import json
from os import DirEntry

from utils.file.yaml_util import YamlUtil
from utils.misc.json_util import default_serializer
from utils.misc.path_exporter import data_dir

# Retrieve all the yaml files under a given directory
yaml_file_entries: list[DirEntry[str]] = YamlUtil.scan_yaml_file(data_dir)

testcase_bus = {}
for yaml_file_entry in yaml_file_entries:
    yaml_file_path = yaml_file_entry.path
    yaml_data = YamlUtil.read_yaml_data(yaml_file_path)
    if yaml_data:
        testcase_container = YamlUtil.extract_case_data_yaml(yaml_data, yaml_file_path)
        for project, modules in testcase_container.items():
            if project not in testcase_bus:
                testcase_bus[project] = modules
            else:
                for module, identifiers in modules.items():
                    if module not in testcase_bus[project]:
                        testcase_bus[project][module] = identifiers
                    else:
                        for identifier, apitestcase in identifiers.items():
                            if identifier not in testcase_bus[project][module]:
                                testcase_bus[project][module][identifier] = apitestcase

testcase_bus_json = json.dumps(testcase_bus, indent=4, ensure_ascii=False, default=default_serializer)
print(testcase_bus_json)

# 只导出这两个
__all__ = ['testcase_bus', 'testcase_bus_json']