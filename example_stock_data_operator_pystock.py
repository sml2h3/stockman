"""
      Author:  sml2h3                              
      Date:    2023/1/31                             
      File:    example_stock_data_operator_pystock                             
      Project: PyCharm                     
"""
import stockman
from stockman.policies import *
from stockman.policies.common import *

with open("sample.yaml", "r") as f:
    res = f.read()
stock = stockman.Stock(res)


def get_stocks_custom(c: daily_k.stock_close, h: daily_k.stock_high, o: daily_k.stock_open):
    return (c > MA(c, 10)) & (MA(c, 10) > MA(c, 20))


result = stock.select_stock(get_stocks_custom)

print(result)
