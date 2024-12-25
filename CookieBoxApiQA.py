# -*- encoding: utf-8 -*-
"""
    @File    :   CookieBoxApiQA.py.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/25/24 15:25    Anicaa (Kangwei Zhu)  1.0      
"""
import json

import pytest
import requests


def run():
    pytest.main()

if __name__ == '__main__':
    run()

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