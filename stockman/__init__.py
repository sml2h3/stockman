"""
      Author:  sml2h3
      Date:    2023/1/18
      File:    __init__
      Project: PyCharm
"""
from . import configs
from .tasks import init_data
from .tasks import install_db


class Stock:
    def __init__(self, config: str = ""):
        configs.init_config(config)

    @staticmethod
    def generate_config():
        configs.make_config()

    @staticmethod
    def install():
        install_db()

    @staticmethod
    def init():
        init_data()
