"""
      Author:  sml2h3
      Date:    2023/1/31
      Project: PyCharm
      高量缩倍阴
"""
import stockman
from feishu_robot import send_msg
from stockman.policies.custom import *

with open("sample.yaml", "r") as f:
    res = f.read()
stock = stockman.Stock(res)

if __name__ == '__main__':
    result = stock.select_stock(glsby)
    content = ""
    for item in result:
        content += f"{item[0]}  于 {item[1][0]} 疑似发生高量缩倍阴\n"
    content += "【高量缩倍阴】：常见于大跌中末期，出现高量（不分阴阳）后，第二天出现缩倍阴（一定要阴线），就是当天尾盘买 ，比如14：50分左右，我们为什么总是强调尾盘买 ，因为尾盘才可以确定当天是不是缩倍量，是不是阴线，因为尾盘量价基本定型，这样才不会模棱两可。如果缩倍量当天是跌停，买点推迟一天，第二天开盘买 ，如果跌停，再往后推迟一天。"

    send_msg("高量缩倍阴形态", content)