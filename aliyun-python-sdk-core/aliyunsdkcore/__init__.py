__version__ = "2.15.0"


import logging


class NullHandler(logging.Handler):
    def emit(self, record):
        pass


logging.getLogger('aliyunsdkcore').addHandler(NullHandler())
