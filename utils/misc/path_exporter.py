# -*- encoding: utf-8 -*-
"""
    @File    :   path_exporter.py
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description:

    @Modify Time      @Author               @Version
    ------------      -------------------   --------
    12/20/24 07:55    Anicaa (Kangwei Zhu)  1.0
"""
import os.path

project_root_path = os.path.abspath(os.path.dirname(__file__))[:-10]
data_dir = project_root_path + 'case_data'
config_dir = project_root_path + 'config'
