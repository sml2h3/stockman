"""
      Author:  sml2h3                              
      Date:    2023/1/28                             
      File:    timeslimit                             
      Project: PyCharm                     
"""
import time
from threading import Lock
from .exceptions import *

lock1 = Lock()


def func_param(*args_o, **kwargs_o):
    def outter(func):
        history = []

        def inner(*args_i, **kwargs_i):
            nonlocal history
            now_time = time.time()
            lock1.acquire()
            noreturn = 0
            max_time = 0
            if len(history) == args_o[1]:
                max_time = now_time - history[0]
                if max_time < args_o[0]:
                    noreturn = 1
                history.pop(0)
            history.append(now_time)
            lock1.release()
            if noreturn == 1:
                history = []
                raise OverTimesLimits(str(args_o[0] - int(max_time)))
            re = func(*args_i)
            return re

        return inner

    return outter
