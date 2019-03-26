import json
import os

from aliyunsdkcore.acs_exception.exceptions import ServerException, ClientException
from aliyunsdkcore.request import CommonRequest
# from aliyunsdkcore.credentials.credentials import StsTokenCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdkram.request.v20150501.AttachPolicyToUserRequest import AttachPolicyToUserRequest
from aliyunsdkram.request.v20150501.CreateUserRequest import CreateUserRequest
from aliyunsdkram.request.v20150501.ListUsersRequest import ListUsersRequest
from base import SDKTestBase, TestCase
from aliyunsdkros.request.v20150901.DescribeResourceTypesRequest import DescribeResourceTypesRequest

from aliyunsdksts.request.v20150401.AssumeRoleRequest import AssumeRoleRequest
from alibabacloud.client import AlibabaCloudClient, ClientConfig
from aliyunsdkcore.vendored.six import iteritems
from base import find_in_response

def request_helper(client, request, **params):
    for key, value in iteritems(params):
        set_name = 'set_' + key
        if hasattr(request, set_name):
            func = getattr(request, set_name)
            func(value)
        else:
            raise Exception(
                "{0} has no parameter named {1}.".format(request.__class__.__name__, key))
    response = client.handle_request(request).content
    return json.loads(response.decode('utf-8'))

sdk_config_path = os.path.join(
    os.path.expanduser("~"),
    "aliyun_sdk_config.json")
with open(sdk_config_path) as fp:
    config = json.loads(fp.read())
    access_key_id = config['access_key_id']
    access_key_secret = config['access_key_secret']
    region_id = config['region_id']

def get_client():
    # 接受AK和token的方式传递
    client_config = ClientConfig()
    client_config.access_key_id = access_key_id
    client_config.access_key_secret = access_key_secret
    client_config.region_id = 'cn-hangzhou'
    client = AlibabaCloudClient(client_config)
    return client

class CommonRequestTest(SDKTestBase):
    def setUp(self):
        TestCase.setUp(self)
        self.client = self.init_client()

    def init_client(self, region_id=None):
        if not region_id:
            region_id = config['region_id']
        client_config = ClientConfig()
        client_config.access_key_id = access_key_id
        client_config.access_key_secret = access_key_secret
        client_config.region_id = region_id
        client_config.read_timeout = 120
        client = AlibabaCloudClient(client_config)
        return client

    def test_rpc_with_common_request(self):
        client = get_client()
        # request = CommonRequest(domain="ecs.aliyuncs.com",
        #                         version="2014-05-26",
        #                         action_name="DescribeRegions",
        #                         product='ecs')
        request = DescribeRegionsRequest()
        response = client.handle_request(request)
        ret = self.get_dict_response(response.content)
        self.assertTrue(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_roa_with_common_request(self):
        client = get_client()
        # request = CommonRequest(domain="ros.aliyuncs.com",
        #                         version="2015-09-01",
        #                         action_name="DescribeResourceTypes",
        #                         uri_pattern="/resource_types",
        #                         product="ros")
        request = DescribeResourceTypesRequest()
        response = client.handle_request(request)
        ret = self.get_dict_response(response.content)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_rpc_common_request_with_sts_token(self):
        self._create_default_ram_user()
        self._attach_default_policy()
        self._create_access_key()

        def get_client():
            # 接受AK和token的方式传递
            client_config = ClientConfig()
            client_config.access_key_id = access_key_id
            client_config.access_key_secret = access_key_secret
            client_config.region_id = 'cn-hangzhou'
            client_config.read_timeout = 120
            client = AlibabaCloudClient(client_config)
            return client
        client = get_client()
        self._create_default_ram_role()
        self._attach_default_policy()

        request = AssumeRoleRequest()
        request.set_RoleArn(self.ram_role_arn)
        request.set_RoleSessionName(self.default_role_session_name)
        response = client.handle_request(request)
        print(response)
        response = self.get_dict_response(response.content)
        credentials = response.get("Credentials")

        # Using temporary AK + STS for authentication
        sts_token_credential = StsTokenCredential(
            credentials.get("AccessKeyId"),
            credentials.get("AccessKeySecret"),
            credentials.get("SecurityToken"))
        def get_client():
            # 接受AK和token的方式传递
            client_config = ClientConfig()
            client_config.access_key_id = access_key_id
            client_config.access_key_secret = access_key_secret
            client_config.region_id = 'me-east-1'
            client_config.credential = sts_token_credential
            client = AlibabaCloudClient(client_config)
            return client

        # the common request
        request = CommonRequest(domain="ecs.aliyuncs.com",
                                version="2014-05-26",
                                action_name="DescribeRegions")
        response = get_client.handle_request(request)
        ret = self.get_dict_response(response.content)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_roa_common_request_with_sts_token(self):
        self._create_default_ram_user()
        self._attach_default_policy()
        self._create_access_key()

        def get_client():
            # 接受AK和token的方式传递
            client_config = ClientConfig()
            client_config.access_key_id = access_key_id
            client_config.access_key_secret = access_key_secret
            client_config.region_id = 'cn-hangzhou'
            client_config.timeout = 120
            client = AlibabaCloudClient(client_config)
            return client

        client = get_client()
        self._create_default_ram_role()
        self._attach_default_policy()

        request = AssumeRoleRequest()
        request.set_RoleArn(self.ram_role_arn)
        request.set_RoleSessionName(self.default_role_session_name)
        response = client.handle_request(request)
        response = self.get_dict_response(response)
        credentials = response.get("Credentials")

        # Using temporary AK + STS for authentication
        sts_token_credential = StsTokenCredential(
            credentials.get("AccessKeyId"),
            credentials.get("AccessKeySecret"),
            credentials.get("SecurityToken")
        )
        def get_client():
            # 接受AK和token的方式传递
            client_config = ClientConfig()
            client_config.access_key_id = access_key_id
            client_config.access_key_secret = access_key_secret
            client_config.region_id = 'me-east-1'
            client_config.credential = sts_token_credential
            client = AlibabaCloudClient(client_config)
            return client
        # the common request
        request = CommonRequest(domain="ros.aliyuncs.com",
                                version="2015-09-01",
                                action_name="DescribeResourceTypes",
                                uri_pattern="/resource_types")
        response = client.handle_request(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_common_request_with_https(self):
        client = get_client()
        # request = CommonRequest(domain="ecs.aliyuncs.com",
        #                         version="2014-05-26",
        #                         action_name="DescribeRegions",
        #                         product="ecs")
        request = DescribeRegionsRequest()
        request.set_protocol_type("https")
        self.assertTrue(request.get_protocol_type().lower() == "https")
        response = client.handle_request(request)
        ret = self.get_dict_response(response.content)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_common_request_with_https(self):
        client = get_client()
        # request = CommonRequest(domain="ecs.aliyuncs.com",
        #                         version="2014-05-26",
        #                         action_name="DescribeRegions",
        #                         uri_pattern = "/resource_types"
        #                         product="ros")
        request = DescribeResourceTypesRequest()
        request.set_protocol_type("https")
        self.assertTrue(request.get_protocol_type().lower() == "https")
        response = client.handle_request(request)
        ret = self.get_dict_response(response.content)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_error_testing_error_message_requested(self):
        def get_client():
            # 接受AK和token的方式传递
            client_config = ClientConfig()
            client_config.access_key_id = None
            client_config.access_key_secret = access_key_secret
            client_config.region_id = 'cn-hangzhou'
            client = AlibabaCloudClient(client_config)
            return client
        client = get_client()
        # request = CommonRequest(domain="ecs.aliyuncs.com",
        #                         version="2014-05-26",
        #                         action_name="DescribeRegions",
        #                         product='ecs')
        try:
            request = DescribeRegionsRequest()
            client.get_credentials()
            response = client.handle_request(request)
            assert False
        except ClientException as e:
            self.assertEqual("Credentials", e.get_error_code())
            self.assertEqual("Unable to locate credentials.",
                             e.get_error_msg())



