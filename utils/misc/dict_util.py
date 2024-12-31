# -*- encoding: utf-8 -*-
"""
    @File    :   dict_util.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/30/24 14:42    Anicaa (Kangwei Zhu)  1.0      
"""
from collections import defaultdict


class DictUtil:

    @staticmethod
    def dict_recursive_init():
        return defaultdict(DictUtil.dict_recursive_init)
