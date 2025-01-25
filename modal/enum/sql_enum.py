# -*- encoding: utf-8 -*-
"""
    @File    :   sql_enum.py.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description: 

    @Modify Time      @Author               @Version 
    ------------      -------------------   -------- 
    1/7/25 20:37    Anicaa (Kangwei Zhu)  1.0      
"""
from enum import Enum

class SQLEnum(Enum):
    SQL_TYPE_SELECT = 'select'
    SQL_TYPE_INSERT = 'insert'
    SQL_TYPE_UPDATE = 'update'
    SQL_TYPE_DELETE = 'delete'
    SQL_EXECUTION_TIMING_TEARDOWN = 'teardown'
    SQL_EXECUTION_TIMING_SETUP = 'setup'