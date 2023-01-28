"""
      Author:  sml2h3                              
      Date:    2023/1/27                             
      File:    install                             
      Project: PyCharm                     
"""
from ..utils import db as dbutil
from .. import configs


def install_db():
    db_config = configs.read_config("dbconfig")
    db = dbutil.Db(config=db_config)
    db.install()
