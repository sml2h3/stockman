"""
      Author:  sml2h3                              
      Date:    2023/1/31                             
      File:    stock_data                             
      Project: PyCharm                     
"""
import numpy as np

from ..utils import contants
from ..utils import db as dbutil
from ..utils import exceptions
from .. import configs
from ..utils import data_factory


def select_stock(func):
    args = []
    args_keys = func.__annotations__.keys()
    keys_types = {}
    for k in args_keys:
        t = func.__annotations__[k].__qualname__
        if '.' in t:
            t = t.split('.')
            args.append(t)
            if len(t) != 2:
                raise exceptions.NotAllowedFormat("未被允许的参数声明方式")
            if t[0] not in keys_types:
                keys_types[t[0]] = []
            if t[1] not in keys_types[t[0]]:
                keys_types[t[0]].append(t[1])
        else:
            raise exceptions.NotAllowedFormat("未被允许的参数声明方式")
    data_type = [item for item in keys_types.keys()]
    eval_funcs = {}
    for item in data_type:
        eval_funcs[eval("get_single_stock_history_{}_local".format(item))] = item
    all_stocks_list = get_all_stock_list()
    all_stocks_codes = all_stocks_list.stock_code.values
    result = []
    for stock_code in all_stocks_codes:
        datas = {}
        for ef in eval_funcs:
            data = ef(stock_code)
            datas[eval_funcs[ef]] = data
        arguments = []
        for arg in args:
            arguments.append(datas[arg[0]][arg[1]].values)
        res = func(*arguments)
        if type(res) == np.ndarray:
            res = res.tolist()
            if len(res) > 0:
                res = res[-1]
            else:
                res = False
        elif type(res) == bool:
            pass
        else:
            raise exceptions.NotAllowedFormat("公式返回了非Bool类型结果")
        if res:
            result.append(stock_code)
    return result



def get_all_stock_list():
    db_config = configs.read_config("dbconfig")
    db = dbutil.Db(config=db_config)
    datas = db.get_all_stock_list()
    datas = data_factory.to_data_frame(datas, ["Id"])
    return datas

# 从本地数据库中取单个股票的日K线数据
def get_single_stock_history_daily_k_local(code):
    db_config = configs.read_config("dbconfig")
    db = dbutil.Db(config=db_config)
    datas = db.get_single_stock_daily_k_data(code)
    datas = data_factory.to_data_frame(datas, ["Id"])
    return datas


# 从本地数据库中取单个股票的日K线数据
def get_single_stock_history_stock_list_local(code):
    db_config = configs.read_config("dbconfig")
    db = dbutil.Db(config=db_config)
    datas = db.get_single_stock_stock_list_data(code)
    datas = data_factory.to_data_frame(datas, ["Id"])
    return datas
