# -*- encoding: utf-8 -*-
'''
@File    :   assertion_func.py.py
@Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
@Description: 

@Modify Time      @Author               @Version    @Desciption
------------      -------------------   --------    -----------
1/17/25 11:03    Anicaa (Kangwei Zhu)  1.0         None
'''
def not_equals(actual, expected, error_message):
    assert actual != expected, error_message

def equals(actual, expected, error_message):
    assert actual == expected, error_message

def inside(actual, expected, error_mesage):
    assert actual in expected, error_mesage

def include(actual, expected, error_message):
    assert expected in actual, error_message