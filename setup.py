"""
      Author:  sml2h3                              
      Date:    2023/1/29                             
      File:    setup                             
      Project: PyCharm                     
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="stockman",
    version="0.0.1",
    author="sml2h3",
    description="A股量化数据工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sml2h3/stockman",
    packages=find_packages(where='.', exclude=(), include=('*',)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pymysql', 'pyyaml', 'tushare'],
    python_requires='<=3.11',
    include_package_data=True,
    install_package_data=True,
)