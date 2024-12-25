# -*- encoding: utf-8 -*-
"""
    @File    :   test_case.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: Test Case Modal. Parse the test case written in yaml。



    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/23/24 09:25   Anicaa (Kangwei Zhu)  1.0      
"""
from dataclasses import dataclass

@dataclass
class ApiTestCase:

    def __init__(self, project: str, module: str, identifier: str, hosts: list[str], method: str, url: str,
                 params: dict[any, any], headers: dict[any, any],
                 data: dict[any, any], description: str):
        self.project = project
        self.module = module
        self.identifier = identifier
        self.hosts = hosts
        self.method = method
        self.url = url
        self.params = params
        self.headers = headers
        self.data = data
        self.description = description

    def beautifier(self) -> dict:
        return {
            "Project": self.project,
            "Module": self.module,
            "Identifier": self.identifier,
            "Hosts": self.hosts,
            "Method": self.method,
            "URL": self.url,
            "Params": self.params,
            "Headers": self.headers,
            "Data": self.data,
            "Description": self.description
        }

    def __str__(self):
        return (f"ApiTestCase(Project: {self.project}, Module: {self.module}, Identifier: {self.identifier}, "
                f"Hosts: {self.hosts}, Method: {self.method}, URL: {self.url}, "
                f"Params: {self.params}, Headers: {self.headers}, Data: {self.data}, "
                f"Description: {self.description})")

    def __repr__(self):
        return str(self.beautifier())
