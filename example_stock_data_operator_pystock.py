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


def get_stocks_custom(c: daily_k.stock_close, h: daily_k.stock_high, l: daily_k.stock_low):
    c = c[-38:]
    h = h[-38:]
    l = l[-38:]
    b1 = (HHV(h, 29) - c) / (HHV(h, 29) - LLV(l, 29)) * 100 - 110
    b2 = SMA(b1, 29, 1) + 100
    b3 = (c - LLV(l, 29)) / (HHV(h, 29) - LLV(l, 29)) * 100
    b4 = SMA(b3, 3, 1)
    b5 = SMA(b4, 3, 1) + 100
    b6 = b5 - b2
    if len(b6) > 35 + 2:
        b6 = b6[-2:]
        b7 = (b6 - 60) * 2.5
    else:
        return False

    if b7[-3] > 0 and b7[-2] < 70 and max(b7[-8: -2]) < b7[-1]:
        if b7[-2] < b7[-1]:
            return True
    return False


if __name__ == '__main__':


    result = stock.select_stock(get_stocks_custom)

    print("\n".join(result))
