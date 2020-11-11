__version__ = "2.13.27"


import logging


class NullHandler(logging.Handler):
    def emit(self, record):
        pass


logging.getLogger('aliyunsdkcore').addHandler(NullHandler())
