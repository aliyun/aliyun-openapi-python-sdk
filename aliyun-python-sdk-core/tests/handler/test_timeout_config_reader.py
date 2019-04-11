# coding=utf-8

import jmespath

from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader
from alibabacloud.utils import load_json_from_data_dir
from tests import unittest

DEFAULT_READ_TIMEOUT = 10
DEFAULT_CONNECTION_TIMEOUT = 5
_api_timeout_config_data = load_json_from_data_dir._load_json_from_data_dir("timeout_config.json")

class TestTimeoutConfigReader(unittest.TestCase):

    def test_timeout_reader_priority(self):
        input_timeout = 20
        file_read_timeout = None
        product_code = "Ecs"
        product_version = "2014-05-26"
        action_name = "DescribeRegions"
        if product_code is not None and product_version is not None \
                and action_name is not None:
            path = '"{0}"."{1}"."{2}"'.format(product_code.lower(), product_version,
                                              action_name)
            file_read_timeout = jmespath.search(path, _api_timeout_config_data)
        self.assertEqual(input_timeout or file_read_timeout or DEFAULT_READ_TIMEOUT, 20)

    def test_timeout_config_default_priority(self):
        file_read_timeout = None
        product_code = "Ecs"
        product_version = "2014-05-26"
        action_name = "DescribeRegions"
        if product_code is not None and product_version is not None \
                and action_name is not None:
            path = '"{0}"."{1}"."{2}"'.format(product_code.lower(), product_version,
                                              action_name)
            file_read_timeout = jmespath.search(path, _api_timeout_config_data)
        self.assertEqual(file_read_timeout or DEFAULT_READ_TIMEOUT, 19)


    def test_timeout_config(self):
        product_code = "Ecs"
        product_version = "2014-05-26"
        action_name = "DescribeRegions"
        path = '"{0}"."{1}"."{2}"'.format(product_code.lower(), product_version,
                                          action_name)
        file_read_timeout = jmespath.search(path, _api_timeout_config_data)
        self.assertEqual(file_read_timeout, 19)

    def test_timeout_input(self):
        file_read_timeout = None
        product_code = None
        product_version = None
        action_name = None
        if product_code is not None and product_version is not None \
                and action_name is not None:
            path = '"{0}"."{1}"."{2}"'.format(product_code.lower(), product_version,
                                              action_name)
            file_read_timeout = jmespath.search(path, _api_timeout_config_data)
        self.assertEqual(file_read_timeout or DEFAULT_READ_TIMEOUT, 10)

    def test_connection_timeout(self):
        timeout_config = TimeoutConfigReader()
        timeout_config.connection_timeout = 10
        timeout = timeout_config._connection_timeout(timeout_config)
        self.assertEqual(timeout, 10)

        timeout_config.connection_timeout = None
        timeout = timeout_config._connection_timeout(timeout_config)
        self.assertEqual(timeout, 5)

