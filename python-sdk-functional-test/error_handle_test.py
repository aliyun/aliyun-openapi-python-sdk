# encoding:utf-8

from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.http.http_response import HttpResponse

from base import SDKTestBase


class ErrorHandleTest(SDKTestBase):

    # TODO make these test stronger with a mock server

    def test_server_timeout(self):
        acs_client = AcsClient(self.access_key_id, self.access_key_secret,
                               "cn-hangzhou", timeout=0.001)
        from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
        request = CreateInstanceRequest()
        request.set_ImageId("coreos_1745_7_0_64_30G_alibase_20180705.vhd")
        request.set_InstanceType("ecs.cn-hangzhou.invalid")
        request.set_SystemDiskCategory("cloud_ssd")
        try:
            response = acs_client.do_action_with_exception(request)
            assert False
        except ClientException as e:
            self.assertEqual("SDK.HttpError", e.error_code)
            self.assertEqual("HTTPConnectionPool(host='ecs-cn-hangzhou.aliyuncs.com',"
                             " port=80): Read timed out. (read timeout=0.001)", e.get_error_msg())

    def test_server_unreachable(self):
        from aliyunsdkcore.request import CommonRequest
        request = CommonRequest(domain="www.aliyun-hangzhou.com", version="2014-05-26",
                                action_name="DescribeRegions")
        try:
            response = self.client.do_action_with_exception(request)
            assert False
        except ClientException as e:
            self.assertEqual("SDK.HttpError", e.error_code)
            self.assertTrue(e.get_error_msg().startswith(
                "HTTPConnectionPool(host='www.aliyun-hangzhou.com', port=80): "
                "Max retries exceeded with url:"))

    def test_server_error_normal(self):
        from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest
        request = DeleteInstanceRequest()
        request.set_InstanceId("blah")
        try:
            response = self.client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("InvalidInstanceId.NotFound", e.get_error_code())
            self.assertEqual("The specified InstanceId does not exist.", e.get_error_msg())

    def test_server_error_with_a_bad_json(self):
        from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest

        request = DeleteInstanceRequest()
        request.set_InstanceId("blah")
        client = self.init_client()
        original_get_response_object = HttpResponse.get_response_object

        # test invalid json format
        def get_response_object(inst):
            return 400, {}, b"bad-json"

        HttpResponse.get_response_object = get_response_object
        try:
            client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("SDK.UnknownServerError", e.get_error_code())
            # self.assertEqual("ServerResponseBody: 'bad-json'", e.get_error_msg())
            self.assertEqual("ServerResponseBody: bad-json", e.get_error_msg())

        # test valid json format but no Code or Message
        def get_response_object(inst):
            return 400, {}, b"""{"key" : "this is a valid json string"}"""

        HttpResponse.get_response_object = get_response_object
        try:
            client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("SDK.UnknownServerError", e.get_error_code())
            self.assertEqual("""ServerResponseBody: {"key" : "this is a valid json string"}""",
                             e.get_error_msg())

        # test missing Code in response
        def get_response_object(inst):
            return 400, {}, b"{\"Message\": \"Some message\"}"

        HttpResponse.get_response_object = get_response_object
        try:
            client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("SDK.UnknownServerError", e.get_error_code())
            self.assertEqual("""Some message""", e.get_error_msg())

        # test missing Code in response
        def get_response_object(inst):
            return 400, {}, b"{\"Code\": \"YouMessedSomethingUp\"}"

        HttpResponse.get_response_object = get_response_object
        try:
            client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("YouMessedSomethingUp", e.get_error_code())
            self.assertEqual("""ServerResponseBody: {"Code": "YouMessedSomethingUp"}""",
                             e.get_error_msg())

        HttpResponse.get_response_object = original_get_response_object
