
from abc import ABCMeta, abstractmethod


class Resolver(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def resolve_endpoint(self, resolve_param):
        pass

