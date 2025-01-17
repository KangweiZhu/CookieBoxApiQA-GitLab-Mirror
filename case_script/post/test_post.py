# -*- encoding: utf-8 -*-
'''
@File    :   test_post.py.py
@Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
@Description: 

@Modify Time      @Author               @Version    @Desciption
------------      -------------------   --------    -----------
12/29/24 09:48    Anicaa (Kangwei Zhu)  1.0         None
'''
import json

import pytest

from modal.test_case import ApiTestCase
from utils.case.gen_util import load_test_case, load_identifier
from utils.request.http_request import HttpRequest

project_name = '饼盒App'
module_name = '帖子模块'

class TestPost:

    @pytest.mark.parametrize(argnames='api_test_case', argvalues=load_test_case(project_name, module_name), ids=load_identifier(project_name, module_name))
    def test_post(self, api_test_case: ApiTestCase):
        http_request = HttpRequest(api_test_case)
        http_request.setup_request()
        resp = http_request.send_request()
        http_request.teardown_request(resp)
        Assertion(api_test_case).doAssert()

