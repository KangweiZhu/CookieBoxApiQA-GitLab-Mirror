# -*- encoding: utf-8 -*-
"""
    @File    :   cookie_box_api_qa.py.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/25/24 15:25    Anicaa (Kangwei Zhu)  1.0      
"""
import json

import pytest

from context.response_context import context


def run():
    pytest.main()


if __name__ == '__main__':
    cache = {}
    run()
    print(json.dumps(context, indent=4, ensure_ascii=False))


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
