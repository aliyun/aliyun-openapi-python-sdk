__version__ = "2.16.0"


import logging


class NullHandler(logging.Handler):
    def emit(self, record):
        pass


logging.getLogger('aliyunsdkcore').addHandler(NullHandler())
