# -*- encoding: utf-8 -*-
"""
    @File    :   __init__.py.py   
    @Contact :   anicaazhu@gmail.com kangwei2@illinois.edu
    @Description:

    @Modify Time      @Author               @Version
    ------------      -------------------   --------
    12/20/24 08:09    Anicaa (Kangwei Zhu)  1.0
"""
from utils.misc.yaml_util import YamlUtil
from utils.misc.path_exporter import config_dir

config_base_path = f'{config_dir}/config'

base_config: dict = YamlUtil.read_yaml_data(f'{config_base_path}.yaml')

if base_config and 'active_config' in base_config:
    additional_config_path = f'{config_base_path}-{base_config["active_config"]}.yaml'
    additionalConfig = YamlUtil.read_yaml_data(additional_config_path)
    for key, value in additionalConfig.items():
        base_config[key] = value

config = base_config
print(f'Configs: {config}')