import stockman

with open("sample.yaml", "r") as f:
    res = f.read()
# res = ""
stock = stockman.Stock(res)
# stock.generate_config()
# stock.install()
stock.init()