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

from context.context import application_context


def run():
    pytest.main()

if __name__ == '__main__':
    cache = {}
    run()
    print(json.dumps(application_context, indent=4, ensure_ascii=False))
