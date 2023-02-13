"""
      Author:  sml2h3
      Date:    2023/1/18
      File:    __init__
      Project: PyCharm
"""
from __future__ import annotations

from . import configs
from .tasks import init_data
from .tasks import install_db
from .tasks import update
from .tasks import stock_data
from .tasks import set_times_limit as stl
from .utils import exceptions
from inspect import isfunction


class Stock:
    def __init__(self, config: str = ""):
        configs.init_config(config)

    @staticmethod
    def generate_config():
        configs.make_config()

    @staticmethod
    def install():
        install_db()

    @staticmethod
    def init():
        init_data()

    '''
    更新日K线到最近一个交易日数据
    '''

    @staticmethod
    def update_daily_k_data():
        update.update_daily_k_data()

    '''
        更新股票列表数据到最近一个交易日数据
    '''

    @staticmethod
    def update_stock_list_data():
        update.update_stock_list_data()

    @staticmethod
    def set_times_limit(feature: str = "tushare.stock_daily_sub",
                        limit_time: [tuple[int, int] | list[int]] = (100, 60)):
        if "." in feature and len(feature.split('.')) == 2 \
                and list(set([type(item) for item in feature.split('.')]))[0] == str:
            if type(limit_time) in [tuple, list] and len(limit_time) == 2 and \
                    list(set([type(item) for item in limit_time]))[0] == int:
                stl.set_func_times_limit(feature, limit_time)
            else:
                raise exceptions.NotAllowedFormat("不合法的limit_time参数格式，参考(100, 60)")
        else:
            raise exceptions.NotAllowedFormat("不合法的feature名称格式，参考tushare.stock_daily_sub")

    @staticmethod
    def get_single_stock_history_daily_k(self, code="000001"):
        return stock_data.get_single_stock_history_daily_k_local(code)

    @staticmethod
    def get_single_stock_history_stock_list(self, code="000001"):
        return stock_data.get_single_stock_history_stock_list_local(code)

    def select_stock(self, func):
        if isfunction(func):
            stock_data.select_stock(func)