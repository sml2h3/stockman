"""
      Author:  sml2h3                              
      Date:    2023/1/20                             
      File:    tushare                             
      Project: PyCharm                     
"""
import datetime
import math
import time

import tushare as ts
from . import BaseApi
from ..utils import contants
from ..utils import exceptions
from ..utils import db as dbutil
from ..utils import timeslimit
from .. import configs


class Tushare(BaseApi):
    def __init__(self, token: str = None):
        super(Tushare, self)
        self.__token = token
        ts.set_token(self.__token)

    def stock_list(self):
        data = []
        for s in contants.stock_list_status:
            data = data + self.stock_list_sub(list_status=s)
        return data

    def stock_list_sub(self, list_status="L"):
        data = []
        pro = ts.pro_api()
        # 拉取数据
        df = pro.stock_basic(**{
            "ts_code": "",
            "name": "",
            "exchange": "",
            "market": "",
            "is_hs": "",
            "list_status": list_status,
            "limit": "",
            "offset": ""
        }, fields=contants.stock_list_fields)
        nums = df.shape[0]
        for i in range(nums):
            item = df.loc[i]
            if item is not None:
                item = item.to_dict()
                data_item = [item[key] for key in item]
                if len(data_item) > 1:
                    data_item = data_item[1:]
                    data.append(data_item)
        return data


    def stock_daily(self, not_init=False):
        if not_init:
            pass
        else:
            db_config = configs.read_config("dbconfig")
            db = dbutil.Db(config=db_config)
            now = datetime.datetime.now()
            end_date = int(now.strftime("%Y%m%d"))
            is_open = db.check_trade_date(end_date)
            if is_open:
                now_h = now.strftime("%H")
                if int(now_h) < 18:
                    end_date = end_date - 1
            last_trade_date = db.get_daily_last_trade_date()
            history_trade_cal = db.get_trade_cal_from_now(end_date, start_date=last_trade_date)
            for trade_cal_item in history_trade_cal:
                date = trade_cal_item['stock_cal_date']
                try:
                    data = self.stock_daily_sub(date)
                except exceptions.OverTimesLimits as e:
                    print(int(str(e)))
                    time.sleep(int(str(e)))
                    data = self.stock_daily_sub(date)
                for item in data:
                    item[0] = item[0][:-3]
                    for idx, n in enumerate(item):
                        if idx > 1:
                            if math.isnan(item[idx]):
                                item[idx] = float(0)
                            else:
                                item[idx] = float(n)
                db.stock_daily_insert_or_update(data)
        return []

    @timeslimit.func_param(60, 100)
    def stock_daily_sub(self, trade_date=""):
        print(trade_date, datetime.datetime.now())
        data = []
        pro = ts.pro_api()
        df = pro.stk_factor(**{
            "ts_code": "",
            "start_date": "",
            "end_date": "",
            "trade_date": trade_date,
            "limit": "",
            "offset": ""
        }, fields=contants.stock_daily_fields)
        nums = df.shape[0]
        for i in range(nums):
            item = df.loc[i]
            item = item.tolist()
            item = [n if n is not None else float(0) for n in item]
            data.append(item)
        return data

    def stock_trade_cal(self):
        data = []
        start_date = ""
        while True:
            data = data + self.stock_trade_cal_sub(start_date)
            if len(data) == 12000:
                start_date = data[-1][0] + 1
            else:
                break
        return data

    def stock_trade_cal_sub(self, start_date=""):
        data = []
        pro = ts.pro_api()
        # 拉取数据
        df = pro.trade_cal(**{
            "exchange": "",
            "cal_date": "",
            "start_date": start_date,
            "end_date": "",
            "is_open": "",
            "limit": "",
            "offset": ""
        }, fields=contants.stock_trade_cal_fields)
        nums = df.shape[0]
        for i in range(nums):
            item = df.loc[i]
            if item is not None:
                item = item.tolist()
                item = [int(n) if n is not None else 0 for n in item]
                data.append(item)
        return data
