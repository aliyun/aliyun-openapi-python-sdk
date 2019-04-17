# coding=utf-8

from alibabacloud.vendored.requests import codes
from tests import unittest
from alibabacloud.handlers.server_error_handler import ServerErrorHandler


class TestServerErrorHandler(unittest.TestCase):

    def test_handle_response(self):
        server_error_code = "SDK.UnknownServerError"
        server_error_message = "ServerResponseBody:NoPermission You are not authorized " \
                               "to do this action. You should be authorized by RAM."
        from alibabacloud.exceptions import ServerException
        exception = ServerException(server_error_code, server_error_message,
                                    None, 403, None)
        self.assertEqual(exception.error_code, "SDK.UnknownServerError")
        self.assertEqual(exception.error_message, "ServerResponseBody:NoPermission You are "
                                                  "not authorized to do this action. You "
                                                  "should be authorized by RAM.")
        self.assertEqual(exception.http_status, 403)
        self.assertFalse(exception.endpoint)
        self.assertFalse(exception.request_id)

        server_error_code = "IncompleteSignature"
        server_error_message = "IncompleteSignature:NoPermission You are not authorized " \
                               "to do this action. You should be authorized by RAM."
        status_code = 400
        special_error_codes = ['IncompleteSignature', 'SignatureDoesNotMatch']
        if status_code == codes.BAD_REQUEST and \
                server_error_code in special_error_codes:
            if server_error_message.split(':', 1)[1] == "IncompleteSignature" or "SignatureDoesNotMatch":
                server_error_code = 'InvalidAccessKeySecret'
                server_error_message = 'The AccessKeySecret is incorrect. ' \
                                       'Please check your AccessKeyId and AccessKeySecret.'
        from alibabacloud.exceptions import ServerException
        exception = ServerException(server_error_code, server_error_message,
                                    None, status_code, None)
        self.assertEqual(exception.error_code, "InvalidAccessKeySecret")
        self.assertEqual(exception.error_message, "The AccessKeySecret is incorrect. "
                                                  "Please check your AccessKeyId and AccessKeySecret.")
        self.assertEqual(exception.http_status, 400)
        self.assertFalse(exception.endpoint)
        self.assertFalse(exception.request_id)


    def test_parse_error_info_from_response_body(self):
        server_error = ServerErrorHandler()
        _json = '{"Code":"SDK.InvalidParameter", ' \
                '"Message":"NoPermission You are not authorized to do this action. ' \
                'You should be authorized by RAM."}'
        error_code, error_message = server_error._parse_error_info_from_response_body(_json)
        self.assertEqual(error_code, "SDK.InvalidParameter")
        self.assertEqual(error_message, "NoPermission You are not authorized to"
                                        " do this action. You should be authorized by RAM.")

        _error = "NoPermission You are not authorized to do this action. You should be authorized by RAM."
        error_code, error_message = server_error._parse_error_info_from_response_body(_error)
        self.assertEqual(error_code, "SDK.UnknownServerError")
        self.assertEqual(error_message, "ServerResponseBody: NoPermission You are not authorized "
                                        "to do this action. You should be authorized by RAM.")
