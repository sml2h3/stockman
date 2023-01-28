"""
      Author:  sml2h3
      Date:    2023/1/18
      File:    db
      Project: PyCharm
"""
import pymysql
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
            create_stock_list_table_sql.format(self.__prefix),  # 创建stock_list表
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
                self.create_table(cursor, sql)
            self.__conn.commit()
            cursor.close()
        else:
            raise InstallDuplicated("数据库之前已经安装成功，如需重装请清空 {} 库".format(self.__dbname))

    def stock_list_insert_or_update(self, data):
        sql = stock_list_insert_or_update_sql.format(self.__prefix, ", ".join(stock_list_col_names), ", ".join(["%s" for _ in stock_list_col_names]), ", ".join(["{}={}".format(item2, "%s") for item2 in stock_list_col_names]))
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

    @staticmethod
    def create_table(cursor, sql):
        cursor.execute(sql)