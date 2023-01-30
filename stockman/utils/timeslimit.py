"""
      Author:  sml2h3                              
      Date:    2023/1/28                             
      File:    timeslimit                             
      Project: PyCharm                     
"""
import time
from threading import Lock
from .exceptions import *
from . import db as dbutil
from .. import configs

lock1 = Lock()


def func_param():
    def outter(func):
        class inner2:
            def __init__(self, func):
                self.history = []
                self.api_source = func.__module__.split('.')[-1]
                self.func_name = func.__name__
                db_config = configs.read_config("dbconfig")
                db = dbutil.Db(config=db_config)
                times_limits = db.get_func_limits(self.api_source, self.func_name)
                if times_limits is None:
                    raise FuncTimesLimitsNotFound("接口调用频率限制数据未找到")
                self.run.__dict__.setdefault('stock_times', times_limits['stock_times'])
                self.run.__dict__.setdefault('stock_times_time', times_limits['stock_times_time'])

            def run(self, *args_i, **kwargs_i):
                now_time = time.time()
                lock1.acquire()
                stock_times = self.run.__dict__['stock_times']
                stock_times_time = self.run.__dict__['stock_times_time']
                noreturn = 0
                max_time = 0
                if len(self.history) == stock_times:
                    max_time = now_time - self.history[0]
                    if max_time < stock_times_time:
                        noreturn = 1
                    self.history.pop(0)
                self.history.append(now_time)
                lock1.release()
                if noreturn == 1:
                    self.history = []
                    raise OverTimesLimits(str(stock_times_time - int(max_time)))
                re = func(*args_i)
                return re

        i = inner2(func)
        return i.run

    return outter


