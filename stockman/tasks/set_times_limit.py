"""
      Author:  sml2h3                              
      Date:    2023/1/30                             
      File:    set_times_limit                             
      Project: PyCharm                     
"""
from ..utils import contants
from ..utils import db as dbutil
from ..utils import exceptions
from .. import configs


def set_func_times_limit(feature: str = "tushare.stock_daily_sub", limit_time: [tuple[int, int]|list[int]] = (100, 60)):
    feature_path = feature.split(".")
    api_source = feature_path[0]
    func_name = feature_path[1]
    stock_times = limit_time[0]
    stock_times_time = limit_time[1]
    db_config = configs.read_config("dbconfig")
    db = dbutil.Db(config=db_config)
    if db.get_func_limits(api_source, func_name):
        db.set_func_limits(api_source, func_name, stock_times, stock_times_time)
    else:
        raise exceptions.FuncTimesLimitsNotFound("接口调用频率限制数据未找到")