import stockman

with open("sample.yaml", "r") as f:
    res = f.read()
stock = stockman.Stock(res)
stock.init()
