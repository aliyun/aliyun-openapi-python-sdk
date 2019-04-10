# encoding:utf-8

from alibabacloud.exceptions import ClientException, ServerException
from aliyunsdkcore.client import AcsClient

from base import SDKTestBase


class ErrorHandleTest(SDKTestBase):

    # TODO make these test stronger with a mock server

    def test_server_timeout(self):
        acs_client = AcsClient(self.access_key_id, self.access_key_secret,
                               "cn-hangzhou", connect_timeout=0.001)
        from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
        request = CreateInstanceRequest()
        request.set_ImageId("coreos_1745_7_0_64_30G_alibase_20180705.vhd")
        request.set_InstanceType('ecs.n2.valid')
        request.set_SystemDiskCategory("cloud_ssd")
        try:
            response = acs_client.do_action_with_exception(request)
            assert False
        except ClientException as e:
            
            self.assertEqual("SDK.HttpError", e.error_code)
            self.assertTrue(e.error_message.startswith("HTTPConnectionPool(host='ecs-cn-hangzhou.aliyuncs.com', port=80): Max retries exceeded with url"))
            self.assertTrue(e.error_message.endswith("'Connection to ecs-cn-hangzhou.aliyuncs.com timed out. (connect timeout=0.001)'))"))
            # self.assertEqual("HTTPConnectionPool(host='ecs-cn-hangzhou.aliyuncs.com',"
            #                  " port=80):  Max retries exceeded with url)", e.error_message)

    def test_server_unreachable(self):
        from aliyunsdkcore.request import CommonRequest
        request = CommonRequest(domain="www.aliyun-hangzhou.com", version="2014-05-26",
                                action_name="DescribeRegions")
        try:
            response = self.client.do_action_with_exception(request)
            assert False
        except ClientException as e:
            self.assertEqual("SDK.HttpError", e.error_code)
            self.assertTrue(e.error_message.startswith(
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
            self.assertEqual("InvalidInstanceId.NotFound", e.error_code)
            self.assertEqual("The specified InstanceId does not exist.", e.error_message)

    # def test_server_error_with_a_bad_json(self):
    #     from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest
    #
    #     request = DeleteInstanceRequest()
    #     request.set_InstanceId("blah")
    #     client = self.init_client()
    #     original_get_response_object = HttpResponse.get_response_object
    #
    #     # test invalid json format
    #     def get_response_object(inst):
    #         return 400, {}, b"bad-json"
    #     HttpResponse.get_response_object = get_response_object
    #     try:
    #         client.do_action_with_exception(request)
    #         assert False
    #     except ServerException as e:
    #         self.assertEqual("SDK.UnknownServerError", e.error_code)
    #         # self.assertEqual("ServerResponseBody: 'bad-json'", e.error_message)
    #         self.assertEqual("ServerResponseBody: bad-json", e.error_message)
    #
    #     # test valid json format but no Code or Message
    #     def get_response_object(inst):
    #         return 400, {}, b"""{"key" : "this is a valid json string"}"""
    #     HttpResponse.get_response_object = get_response_object
    #     try:
    #         client.do_action_with_exception(request)
    #         assert False
    #     except ServerException as e:
    #         self.assertEqual("SDK.UnknownServerError", e.error_code)
    #         self.assertEqual("""ServerResponseBody: {"key" : "this is a valid json string"}""",
    #                          e.error_message)
    #
    #     # test missing Code in response
    #     def get_response_object(inst):
    #         return 400, {}, b"{\"Message\": \"Some message\"}"
    #     HttpResponse.get_response_object = get_response_object
    #     try:
    #         client.do_action_with_exception(request)
    #         assert False
    #     except ServerException as e:
    #         self.assertEqual("SDK.UnknownServerError", e.error_code)
    #         self.assertEqual("""Some message""", e.error_message)
    #
    #     # test missing Code in response
    #     def get_response_object(inst):
    #         return 400, {}, b"{\"Code\": \"YouMessedSomethingUp\"}"
    #     HttpResponse.get_response_object = get_response_object
    #     try:
    #         client.do_action_with_exception(request)
    #         assert False
    #     except ServerException as e:
    #         self.assertEqual("YouMessedSomethingUp", e.error_code)
    #         self.assertEqual("""ServerResponseBody: {"Code": "YouMessedSomethingUp"}""",
    #                          e.error_message)
    #
    #     HttpResponse.get_response_object = original_get_response_object
