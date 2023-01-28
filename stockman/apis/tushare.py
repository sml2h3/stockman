"""
      Author:  sml2h3                              
      Date:    2023/1/20                             
      File:    tushare                             
      Project: PyCharm                     
"""
from . import BaseApi
from ..utils import contants
import tushare as ts


class Tushare(BaseApi):
    def __init__(self, token: str = None):
        super(Tushare, self)
        self.__token = token
        self.__stock_list_filed = contants.stock_list_fields
        ts.set_token('635ef021ba199c188116ac5465039f409565454cf3be74feaf94cf6f')

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
        }, fields=self.__stock_list_filed)
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

