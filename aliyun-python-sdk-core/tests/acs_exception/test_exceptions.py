from tests import unittest

from aliyunsdkcore.acs_exception.exceptions import ClientException, ServerException


class TestClientException(unittest.TestCase):
    def test_constructor(self):
        ex = ClientException("code", "message")
        self.assertEqual(ex.get_error_type(), "Client")
        self.assertEqual(ex.get_error_msg(), "message")
        self.assertEqual(ex.get_error_code(), "code")
        self.assertEqual(str(ex), "code message")
        ex.set_error_code("newCode")
        self.assertEqual(ex.get_error_code(), "newCode")
        ex.set_error_msg("new message")
        self.assertEqual(ex.get_error_msg(), "new message")
        self.assertEqual(str(ex), "newCode new message")


class TestServerException(unittest.TestCase):
    def test_constructor(self):
        ex = ServerException("code", "message", 400, "requestid")
        self.assertEqual(ex.get_error_type(), "Server")
        self.assertEqual(ex.get_error_msg(), "message")
        self.assertEqual(ex.get_error_code(), "code")
        self.assertEqual(ex.get_http_status(), 400)
        self.assertEqual(ex.get_request_id(), "requestid")
        self.assertEqual(str(ex), "HTTP Status: 400 Error:code message RequestID: requestid")
        ex.set_error_code("newCode")
        self.assertEqual(ex.get_error_code(), "newCode")
        ex.set_error_msg("new message")
        self.assertEqual(ex.get_error_msg(), "new message")
        self.assertEqual(str(ex), "HTTP Status: 400 Error:newCode new message RequestID: requestid")
