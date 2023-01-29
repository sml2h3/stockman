![header.png](https://cdn.wenanzhe.com/img/68747470733a2f2f7a332e617831782e636f6d2f323032312f30372f30322f5236496832382e6a7067.jfif)

# Stockman

友好的A股量化数据包，支持tushare等多数据渠道（其他渠道开发中）收集，自带常用和非常用数据指标（开发中）

----

## 一、使用方式

### 1、生成配置文件清单

```python
import stockman

stock = stockman.Stock()
stock.generate_config()
```

上述代码将会在项目当前目录生成 <b>sample.yaml</b> 配置文件， 请根据实际情况进行填写

```yaml
DBCONFIG:                           # MYSQL数据库配置
  host: 127.0.0.1                   # MYSQL数据库主机地址
  dbname: stock_db                  # MYSQL数据库名称，需要自己创建该名称数据库
  username: root                    # MYSQL数据库用户名
  password: stock_db                # MYSQL数据库密码
  port: 3306                        # MYSQL数据库端口
  charset: utf8                     # MYSQL数据库默认字符集
  prefix: stockman_                 # MYSQL数据库表前缀
APIS:                               # 数据渠道配置
  Tushare:                          # Tushare 数据渠道
    Params:                         # Tushare 数据渠道配置
      token: ''                     # Tushare 数据渠道TOKEN，请于Tushare个人中心获取
    Permissions:                    # Tushare 数据功能权限配置
      stock_list: true              # 是否使用Tushare渠道进行股票列表数据权限获取
      stock_daily: true             # 是否使用Tushare渠道进行股票日线数据权限获取
      stock_trade_cal: true         # 是否使用Tushare渠道进行股票交易日历数据获取
```

### 2、自动安装数据表

```python
import stockman

with open("sample.yaml", "r") as f:
    res = f.read()
stock = stockman.Stock(res)
stock.install()
```

上述代码将会根据配置文件 <b>sample.yaml</b> 的数据库部分配置，生成各项数据表

### 3、初始化数据

```python
import stockman

with open("sample.yaml", "r") as f:
    res = f.read()
stock = stockman.Stock(res)
stock.init()
```

上述代码将会自动依次根据配置文件 <b>sample.yaml</b> 中的数据渠道部分中的权限配置去导入历史数据，目前包含有交易日历、股票列表、历史日K线数据等。
