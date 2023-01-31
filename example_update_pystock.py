"""
      Author:  sml2h3                              
      Date:    2023/1/28                             
      File:    example_install_stockman
      Project: PyCharm                     
"""
import stockman

with open("sample.yaml", "r") as f:
    res = f.read()
stock = stockman.Stock(res)


def update_daily_k_data():
    stock.update_daily_k_data()


def update_stock_list_data():
    stock.update_stock_list_data()


if __name__ == '__main__':
    update_stock_list_data()
    nums = update_daily_k_data()

