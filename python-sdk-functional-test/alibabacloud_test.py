# encoding:utf-8

import os

from alibabacloud.client import ClientConfig, AlibabaCloudClient
from alibabacloud.credentials import AccessKeyCredentials
from alibabacloud.credentials.provider import RamRoleCredentialsProvider
from alibabacloud.request import APIRequest
from aliyunsdksts.request.v20150401.AssumeRoleRequest import AssumeRoleRequest
from base import SDKTestBase

from aliyunsdkcore.auth.credentials import RamRoleArnCredential
from aliyunsdkcore.client import AcsClient


class AlibabaCloudClientTest(SDKTestBase):

    def test_call_rpc_request_with_client_introduction(self):
        client_config = ClientConfig(access_key_id = self.access_key_id,
                                     access_key_secret = self.access_key_secret,
                                     region_id = self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)

        response_key_id = response.http_request.credentials.access_key_id
        response_key_secret = response.http_request.credentials.access_key_secret
        self.assertEqual(self.access_key_id, response_key_id)
        self.assertEqual(self.access_key_secret, response_key_secret)

        response =response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_client_introduction(self):
        client_config = ClientConfig(access_key_id = self.access_key_id,
                                     access_key_secret = self.access_key_secret,
                                     region_id = self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        api_request.uri_pattern = '/resource_types'
        api_request.path_params = None
        response = client._handle_request(api_request)

        response_key_id = response.http_request.credentials.access_key_id
        response_key_secret = response.http_request.credentials.access_key_secret
        self.assertEqual(self.access_key_id, response_key_id)
        self.assertEqual(self.access_key_secret, response_key_secret)

        response =response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_request_with_client_ram_role(self):
        self._create_default_ram_user()
        # self._attach_default_policy()
        self._create_access_key()
        self._create_default_ram_role()

        acs_client = ClientConfig(region_id = self.region_id)
        ram_role_arn_credential = RamRoleCredentialsProvider(
            acs_client,
            AccessKeyCredentials(self.ram_user_access_key_id,
                                 self.ram_user_access_key_secret),
            self.ram_role_arn,
            "alice_test")
        client = AlibabaCloudClient(acs_client, ram_role_arn_credential)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)

        response_credentials = response.http_request.credentials
        self.assertTrue(response_credentials.access_key_id.startswith("STS."))

        response =response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_client_ram_role(self):
        self._create_default_ram_user()
        # self._attach_default_policy()
        self._create_access_key()
        self._create_default_ram_role()

        roa_client = ClientConfig(region_id = self.region_id)
        ram_role_arn_credential = RamRoleCredentialsProvider(
            roa_client,
            AccessKeyCredentials(self.ram_user_access_key_id,
                                 self.ram_user_access_key_secret),
            self.ram_role_arn,
            "alice_test")
        client = AlibabaCloudClient(roa_client, ram_role_arn_credential)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        api_request.uri_pattern = '/resource_types'
        api_request.path_params = None
        response = client._handle_request(api_request)

        response_credentials = response.http_request.credentials
        self.assertTrue(response_credentials.access_key_id.startswith("STS."))

        response =response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_request_with_client_env_ak(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret

        client_config = ClientConfig(region_id = self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)

        response_key_id = response.http_request.credentials.access_key_id
        response_key_secret = response.http_request.credentials.access_key_secret
        self.assertEqual(self.access_key_id, response_key_id)
        self.assertEqual(self.access_key_secret, response_key_secret)

        response =response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_client_env_ak(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret

        client_config = ClientConfig(region_id = self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        api_request.uri_pattern = '/resource_types'
        api_request.path_params = None
        response = client._handle_request(api_request)

        response_key_id = response.http_request.credentials.access_key_id
        response_key_secret = response.http_request.credentials.access_key_secret
        self.assertEqual(self.access_key_id, response_key_id)
        self.assertEqual(self.access_key_secret, response_key_secret)

        response =response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_request_with_client_config_default(self):
        client_config = ClientConfig(region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)

        response =response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_client_config_default(self):
        client_config = ClientConfig(region_id = self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        api_request.uri_pattern = '/resource_types'
        api_request.path_params = None
        response = client._handle_request(api_request)

        response =response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))
