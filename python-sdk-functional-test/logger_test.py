# encoding:utf-8
import logging
import os
import tempfile

import mock
from base import SDKTestBase


class LoggerTest(SDKTestBase):

    def test_file_logger(self):
        tempdir = tempfile.mkdtemp()
        temp_file = os.path.join(tempdir, 'file_logger')
        self.client.set_file_logger(log_level=logging.DEBUG, path=temp_file)
        from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
        request = DescribeRegionsRequest()
        self.client.do_action_with_exception(request)
        self.assertTrue(os.path.isfile(temp_file))
        with open(temp_file) as logfile:
            s = logfile.read()
        self.assertTrue('aliyunsdkcore.client DEBUG Request received.' in s)

    @mock.patch('logging.getLogger')
    @mock.patch('logging.StreamHandler')
    @mock.patch('logging.Formatter')
    def test_stream_logger(self, formatter, handler, get_logger):
        self.client.set_stream_logger(logger_name='foo.bar', log_level=40, format_string='foo')
        get_logger.assert_called_with('foo.bar')
        get_logger.return_value.setLevel.assert_called_with(logging.ERROR)
        formatter.assert_called_with('foo')
