"""
      Author:  sml2h3                              
      Date:    2023/1/18                             
      File:    __init__.py                             
      Project: PyCharm                     
"""

import os
import yaml
from ..utils import exceptions
from . import dbconfig
from . import apis


config_types = {
    "dbconfig": dbconfig.DbConfig,
    "apis": apis.Apis
}


def make_config():
    configs = {}
    for key in config_types:
        configs[key.upper()] = get_obj_attr(config_types[key].__dict__)
    with open('sample.yaml', 'w', encoding="utf-8") as f:
        yaml.dump(configs, f, sort_keys=False)


def init_config(config_str):
    obj = yaml.load(config_str, Loader=yaml.FullLoader)
    if obj is not None:
        for key in obj:
            set_config(key.lower(), obj[key])


def set_config(config_type: str, args: dict):
    if config_type in config_types:
        config = config_types[config_type]
        _module = config.__module__
        _module_path = _module.split(".")
        if len(_module_path) == 3:
            config_type = _module_path[-1]
            if config_type in config_types:
                config_attr = get_obj_attr(config.__dict__)
                if type(args) == dict:
                    for key in config_attr:
                        if key in args:
                            config_attr[key] = args[key]
                    config_attr = {
                        config_type.upper(): config_attr
                    }
                    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'settings',
                                           '{}.yaml'.format(config_type)), 'w', encoding="utf-8") as f:
                        yaml.dump(config_attr, f, default_flow_style=False)
            else:
                raise exceptions.ConfigNotFound("配置对象未找到，请确认为stockman.configs.xxx")
        else:
            raise exceptions.ConfigNotFound("配置对象未找到，请确认为stockman.configs.xxx")
    else:
        raise exceptions.ConfigNotFound("配置对象未找到，请确认为stockman.configs.xxx")


def read_config(config_type: str):
    if config_type in config_types:
        config_obj = config_types[config_type]
        config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'settings',
                                        '{}.yaml'.format(config_type))
        if os.path.exists(config_file_path):
            with open(config_file_path, 'r', encoding="utf-8") as f:
                config_attr = yaml.load(f, yaml.FullLoader)
                if config_type.upper() in config_attr:
                    config_attr = config_attr[config_type.upper()]
                    for key in config_attr:
                        setattr(config_obj, key, config_attr[key])
                    return config_obj
                else:
                    raise exceptions.ConfigTypeError("配置数据类型出错")
        else:
            raise exceptions.ConfigFileNotFound("配置文件未找到")
    else:
        raise exceptions.ConfigNotFound("配置对象未找到，请确认为stockman.configs.xxx")


def get_obj_attr(obj: dict):
    ignore_list = [
        '_module_',
        '__doc__',
        '__weakref__',
        '__dict__',
        '__module__'
    ]
    nd = {}
    for key in obj:
        if key in ignore_list:
            continue
        else:
            if type(obj[key]) == type:
                nd[key] = get_obj_attr(obj[key].__dict__)
            else:
                nd[key] = obj[key]
    return nd
