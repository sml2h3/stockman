"""
      Author:  sml2h3
      Date:    2023/1/18
      File:    db
      Project: PyCharm
"""
import pymysql
from collections import namedtuple
from ..configs import dbconfig
from .contants import *
from .exceptions import *


class Db:

    def __init__(self, config: dbconfig):
        self.__host = config.host
        self.__username = config.username
        self.__password = config.password
        self.__dbname = config.dbname
        self.__port = config.port
        self.__charset = config.charset
        self.__prefix = config.prefix
        self.__install_sql_list = [
            create_stock_list_table_sql,  # 创建stock_list表
            create_stock_daily_k_table_sql,  # 创建日线数据表
            create_stock_cal_table_sql,  # 创建交易日历表
            create_stock_func_limits_table_sql,  # 创建函数频率限制数据
            init_stock_func_limits_data_sql,  # 初始化函数频率限制数据
        ]
        self.__conn = pymysql.connect(host=self.__host, user=self.__username, password=self.__password, port=self.__port
                                      , db=self.__dbname, charset=self.__charset,
                                      cursorclass=pymysql.cursors.DictCursor)

    def get_conn(self):
        return self.__conn

    def install_check(self):
        cursor = self.__conn.cursor(cursor=pymysql.cursors.Cursor)
        cursor.execute(show_tables_sql)
        tables = cursor.fetchall()
        for item in tables:
            if item[0].startswith(self.__prefix):
                return True
        return False

    def install(self):
        if not self.install_check():
            cursor = self.__conn.cursor()
            for sql in self.__install_sql_list:
                self.create_table(cursor, sql.format(self.__prefix))
            self.__conn.commit()
            cursor.close()
        else:
            raise InstallDuplicated("数据库之前已经安装成功，如需重装请清空 {} 库".format(self.__dbname))

    def stock_list_insert_or_update(self, data):
        sql = stock_list_insert_or_update_sql.format(self.__prefix, ", ".join(stock_list_col_names),
                                                     ", ".join(["%s" for _ in stock_list_col_names]), ", ".join(
                ["{}={}".format(item2, "%s") for item2 in stock_list_col_names]))
        if self.install_check():
            cursor = self.__conn.cursor()
            for item in data:
                item = [n if n is not None else "" for n in item]
                item[-3] = int(item[-3]) if item[-3] else 0  # 上市时间
                item[-2] = int(item[-2]) if item[-2] else 0  # 退市时间
                cursor.execute(sql, item + item)
            self.__conn.commit()
            cursor.close()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")

    def stock_daily_insert_or_update(self, data):
        sql = stock_daily_insert_or_update_sql.format(self.__prefix, ", ".join(stock_daily_col_names),
                                                      ", ".join(["%s" for _ in stock_daily_col_names]), ", ".join(
                ["{}={}".format(item2, "%s") for item2 in stock_daily_col_names]))
        if self.install_check():
            cursor = self.__conn.cursor()
            for item in data:
                cursor.execute(sql, item + item)
            self.__conn.commit()
            cursor.close()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")

    def stock_trade_cal_insert_or_update(self, data):
        sql = stock_trade_cal_insert_sql.format(self.__prefix)
        if self.install_check():
            cursor = self.__conn.cursor()
            for item in data:
                try:
                    cursor.execute(sql, item)
                except pymysql.err.IntegrityError:
                    continue
            self.__conn.commit()
            cursor.close()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")

    def check_trade_date(self, trade_date):
        sql = stock_check_trade_date_sql.format(self.__prefix, trade_date)
        if self.install_check():
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchone()
            cursor.close()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")
        if data:
            return data['stock_is_open']
        else:
            return 0

    def get_daily_last_trade_date(self):
        sql = stock_daily_get_last_trade_date_sql.format(self.__prefix)
        if self.install_check():
            cursor = self.__conn.cursor(cursor=pymysql.cursors.Cursor)
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")
        if len(data) == 0:
            return None
        data = [item[0] for item in data]
        data = sorted(data, reverse=True)
        return data[0]

    def get_trade_cal_from_now(self, end_date, start_date=None):
        sql = stock_get_trade_cal_from_now_sql.format(self.__prefix, end_date)
        if start_date is not None:
            sql += stock_get_trade_cal_from_now_sql_fix.format(start_date)
        if self.install_check():
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")
        return data

    def get_func_limits(self, api_source, func_name):
        sql = stock_get_func_times_limits_sql.format(self.__prefix)
        if self.install_check():
            cursor = self.__conn.cursor()
            cursor.execute(sql, [api_source, func_name])
            data = cursor.fetchone()
            cursor.close()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")
        return data

    def set_func_limits(self, api_source, func_name, stock_times, stock_times_time):
        sql = stock_set_func_times_limits_sql.format(self.__prefix)
        if self.install_check():
            cursor = self.__conn.cursor()
            result = cursor.execute(sql, [stock_times, stock_times_time, api_source, func_name])
            cursor.close()
            self.__conn.commit()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")
        return result

    @staticmethod
    def create_table(cursor, sql):
        cursor.execute(sql)

    def get_all_stock_list(self):
        sql = stock_get_all_stock_list_sql.format(self.__prefix)
        if self.install_check():
            cursor = self.__conn.cursor()
            cursor.execute(sql, [])
            cursor.close()
            self.__conn.commit()
            result = cursor.fetchall()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")
        return result

    def get_single_stock_daily_k_data(self, code):
        sql = stock_get_single_stock_daily_k_sql.format(self.__prefix)
        if self.install_check():
            cursor = self.__conn.cursor()
            cursor.execute(sql, [code])
            cursor.close()
            self.__conn.commit()
            result = cursor.fetchall()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")
        return result

    def get_single_stock_stock_list_data(self, code):
        sql = stock_get_single_stock_list_sql.format(self.__prefix)
        if self.install_check():
            cursor = self.__conn.cursor()
            cursor.execute(sql, [code])
            cursor.close()
            self.__conn.commit()
            result = cursor.fetchall()
        else:
            raise NotInstalled("数据库尚未安装，请先安装数据库")
        return result
