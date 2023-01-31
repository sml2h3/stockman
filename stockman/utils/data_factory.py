"""
      Author:  sml2h3                              
      Date:    2023/1/31                             
      File:    data_factory                             
      Project: PyCharm                     
"""
import pandas as pd


def to_data_frame(datas: list, index=None):
    df = pd.DataFrame(datas)
    if index:
        df.set_index(index, inplace=True)
    return df