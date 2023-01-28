"""
      Author:  sml2h3                              
      Date:    2023/1/20                             
      File:    __init__.py                             
      Project: PyCharm                     
"""
import importlib
from .. import configs
from ..utils import contants

apis_list = contants.apis_list
permissions_list = contants.permissons_list
apis_objects = dict()


class BaseApi:
    def __init__(self):
        pass

    def stock_list(self):
        pass


def get_api_op() -> dict[BaseApi]:
    # 初始化权限表
    permissions_dict = dict()
    for permission_item in permissions_list:
        permissions_dict.setdefault(permission_item, None)

    apis_config = configs.read_config("apis")
    for api_item in apis_list:
        api_config = getattr(apis_config, api_item)
        module = importlib.import_module(".{}".format(api_item.lower()), package="stockman.apis")
        api_object = getattr(module, api_item)(**api_config['Params'])
        for key in api_config['Permissions']:
            if api_config['Permissions'][key]:
                permissions_dict[key] = api_object
    return permissions_dict
