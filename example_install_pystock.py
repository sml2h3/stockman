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
stock.install()
