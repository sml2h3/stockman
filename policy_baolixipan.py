"""
      Author:  sml2h3
      Date:    2023/1/31
      File:    example_stock_data_operator_pystock
      Project: PyCharm
"""
import stockman
from feishu_robot import send_msg
from stockman.policies.custom import *

with open("sample.yaml", "r") as f:
    res = f.read()
stock = stockman.Stock(res)

if __name__ == '__main__':
    result = stock.select_stock(blxp)
    content = ""
    for item in result:
        content += f"{item[0]}  于 {item[1][0]} 疑似发生暴力洗盘\n"
    content += "【暴力洗盘】：常见于行情即将启动，超短主力通过短期（通常为2日）大幅度极致波动进行震仓获取大量筹码的行为，常见结构为首日大阳线涨停，次日高开后早盘快速拉高后大幅度回落并进行横盘震仓且收盘实际跌幅很小甚至收涨，形成一根放倍量的大阴线，后市可能会在接触到5-20日均线后快速启动"

    send_msg("暴力洗盘形态", content)