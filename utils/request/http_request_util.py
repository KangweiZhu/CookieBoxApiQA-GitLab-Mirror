# -*- encoding: utf-8 -*-
"""
    @File    :   http_request_util.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/25/24 12:01    Anicaa (Kangwei Zhu)  1.0      
"""
import json

import requests

from modal.test_case import ApiTestCase
from utils.request.base_request_util import BaseRequestUtil, protocol_formatter


class HttpRequestUtil(BaseRequestUtil):

    def __init__(self, apitestcase: ApiTestCase):
        self.__apitestcase = apitestcase

    def send_request(self):
        request_url = protocol_formatter(self.__apitestcase.protocol) + self.__apitestcase.host + self.__apitestcase.api

        resp = requests.request(
            method=self.__apitestcase.method,
            url=request_url,
            headers=self.__apitestcase.headers,
            params=self.__apitestcase.params,
            data=json.dumps(self.__apitestcase.data),
            timeout=5
        )

        return resp

