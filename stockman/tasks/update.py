"""
      Author:  sml2h3                              
      Date:    2023/1/30                             
      File:    update                             
      Project: PyCharm                     
"""
from .. import apis
from ..utils import contants
from ..utils import db as dbutil
from ..utils import exceptions
from .. import configs

premissions_list = contants.permissons_list
'''
更新日K线数据
'''


def update_daily_k_data():
    db_config = configs.read_config("dbconfig")
    db = dbutil.Db(config=db_config)
    if db.install_check():
        op = apis.get_api_op()
        do_stock_daily = op["stock_daily"]
        nums = do_stock_daily.stock_daily(update=True)
        return nums
    else:
        raise exceptions.NotInstalled("数据系统尚未安装，请安装后再进行初始化操作")

'''
更新股票列表数据
'''


def update_stock_list_data():
    db_config = configs.read_config("dbconfig")
    db = dbutil.Db(config=db_config)
    if db.install_check():
        op = apis.get_api_op()
        do_stock_daily = op["stock_list"]
        data = do_stock_daily.stock_list()
        db.stock_list_insert_or_update(data)
        return len(data)
    else:
        raise exceptions.NotInstalled("数据系统尚未安装，请安装后再进行初始化操作")
