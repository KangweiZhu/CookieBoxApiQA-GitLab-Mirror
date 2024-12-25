# -*- encoding: utf-8 -*-
"""
    @File    :   test_case.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: Test Case Modal. Parse the test case written in yaml。



    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/23/24 09:25    Anicaa (Kangwei Zhu)  1.0
"""
from dataclasses import dataclass

@dataclass
class ApiTestCase:

    def __init__(self, project: str, module: str, identifier: str, protocol: str, host: str, method: str, api: str,
                 params: dict[any, any], headers: dict[any, any],
                 data: dict[any, any], description: str):
        self.project = project
        self.module = module
        self.identifier = identifier
        self.protocol = protocol
        self.host = host
        self.method = method
        self.api = api
        self.params = params
        self.headers = headers
        self.data = data
        self.description = description

    def beautifier(self) -> dict:
        return {
            "Project": self.project,
            "Module": self.module,
            "Identifier": self.identifier,
            "Protocol": self.protocol,
            "Host": self.host,
            "Method": self.method,
            "Api": self.api,
            "Params": self.params,
            "Headers": self.headers,
            "Data": self.data,
            "Description": self.description
        }

    def __str__(self):
        return (f"ApiTestCase(Project: {self.project}, Module: {self.module}, Identifier: {self.identifier}, "
                f"Protocol: {self.protocol}, Host: {self.host}, Method: {self.method}, Api: {self.api}, "
                f"Params: {self.params}, Headers: {self.headers}, Data: {self.data}, "
                f"Description: {self.description})")

    def __repr__(self):
        return str(self.beautifier())
