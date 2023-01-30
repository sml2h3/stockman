"""
      Author:  sml2h3                              
      Date:    2023/1/19                             
      File:    exceptions                             
      Project: PyCharm                     
"""


class ConfigTypeError(BaseException):
    pass


class ConfigNotFound(BaseException):
    pass


class ConfigFileNotFound(BaseException):
    pass


class NotInstalled(BaseException):
    pass


class InstallDuplicated(BaseException):
    pass


class OverTimesLimits(BaseException):
    pass


class FuncTimesLimitsNotFound(BaseException):
    pass


class NotAllowedFormat(BaseException):
    pass
