# -*- encoding: utf-8 -*-
"""
    @File    :   playground.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/25/24 21:25    Anicaa (Kangwei Zhu)  1.0      
"""
import json

import requests
from jsonpath import jsonpath

from utils.file.yaml_util import YamlUtil
from utils.misc.path_exporter import data_dir

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
# json_resp = json.loads(resp.text)
# jsonpathdata = jsonpath(json_resp, '$.data.token')
# print(jsonpathdata)
# yaml_file = YamlUtil.read_yaml_data(data_dir + '/aaa.yaml')
# print(yaml_file)