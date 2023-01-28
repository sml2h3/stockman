"""
      Author:  sml2h3                              
      Date:    2023/1/27                             
      File:    init_data                             
      Project: PyCharm                     
"""
from .. import apis
from ..utils import contants
from ..utils import db as dbutil
from ..utils import exceptions
from .. import configs


premissions_list = contants.permissons_list
init_ops = contants.init_ops


def init_data():
    db_config = configs.read_config("dbconfig")
    db = dbutil.Db(config=db_config)
    if db.install_check():
        op = apis.get_api_op()
        for init_op in init_ops:
            do_op = op[init_op]
            data = getattr(do_op, init_op)()
            getattr(db, "{}_insert_or_update".format(init_op))(data)
            exit()
    else:
        raise exceptions.NotInstalled("数据系统尚未安装，请安装后再进行初始化操作")