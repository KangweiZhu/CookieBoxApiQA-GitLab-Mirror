# -*- encoding: utf-8 -*-
"""
    @File    :   context.py.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    12/25/24 21:16    Anicaa (Kangwei Zhu)  1.0      
"""
from collections import defaultdict

from utils.misc.dict_util import DictUtil

application_context = defaultdict(DictUtil.dict_recursive_init)