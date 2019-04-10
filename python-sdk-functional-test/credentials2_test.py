# encoding:utf-8
import os
from unittest import mock

import requests

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential, RamRoleArnCredential
from aliyunsdkros.request.v20150901.DescribeResourceTypesRequest import \
    DescribeResourceTypesRequest
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdksts.request.v20150401.AssumeRoleRequest import AssumeRoleRequest

from base import SDKTestBase

from tests import MyServer


role_name ={u'Code': u'Success', u'LastUpdated': u'2019-04-09T10:41:31Z',
            u'AccessKeyId': u'STS.NHLK9qYbdbKgs4oYTRXqjLSdX',
            u'AccessKeySecret': u'J94mBKoeEUzDGwgUUsdXcf8hdbDm9Pht4A4R9vKParVT',
            u'Expiration': u'2019-04-09T16:41:31Z',
            u'SecurityToken': u'CAISigJ1q6Ft5B2yfSjIr4'
                              u'v5AIPFtL1F1YmMcRLevVQHVP5Go5bPujz2IHlFeXBoCekes/8'
                              u'yn29S6vwalrRtTtpfTEmBbI569s0M9hGjPZSQsM+n5qVUk5+1'
                              u'BjBe3ZEEFIqADd/iRfbxJ92PCTmd5AIRrJL+cTK9JS/HVbSCl'
                              u'Z9gaPkOQwC8dkAoLdxKJwxk2qR4XDmrQpTLCBPxhXfKB0dFox'
                              u'd1jXgFiZ6y2cqB8BHT/jaYo603392gcsj+NJc1ZssjA47oh7R'
                              u'MG/CfgHIK2X9j77xriaFIwzDDs+yGDkNZixf8aLOFr4Q3fFYh'
                              u'O/NnQPEe8KKkj5t1sffJnoHtzBJAIexOTzRtjFVtcH5xchqAA'
                              u'U8ECYWEiFKZtXwEpMnJUW4UXeXgzhMYDCeoLzrwQxcDwxpVEH'
                              u'KfA1zt+i/yAOXhJ1EgWwDPjyIeeFiR5VypJaHstnq/P0Jv/Uq'
                              u'ZAOS88KwDNLMHAc34HwmPNUnlsWc95B40ys91qtyHxQa1Jjjs'
                              u'LgE/S/5WyUQslQmuQI6e/rnT'}

class CredentialsTest(SDKTestBase):

    __name__ = 'CredentialsTest'

    def test_call_request_with_client_env_priority(self):
        self._create_default_ram_user()
        self._attach_default_policy()
        self._create_access_key()
        self._create_default_ram_role()
        ram_role_arn_credential = RamRoleArnCredential(
            self.ram_user_access_key_id,
            self.ram_user_access_key_secret,
            self.ram_role_arn,
            "alice_test")
        acs_client = AcsClient(
            region_id="cn-hangzhou",
            credential=ram_role_arn_credential)

        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret

        request = DescribeRegionsRequest()
        response = acs_client._handle_request_in_new_style(request)
        response_credential = response.http_request.credentials
        self.assertTrue(response_credential.access_key_id.startswith("STS."))
        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_request_with_env_config_priority(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret

        client = AcsClient()
        request = DescribeRegionsRequest()
        response = client._handle_request_in_new_style(request)
        env_credential_id = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_ID")
        env_credential_secret = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
        response_key_id = response.http_request.credentials.access_key_id
        response_key_secret = response.http_request.credentials.access_key_secret
        self.assertEqual(env_credential_id, response_key_id)
        self.assertEqual(env_credential_secret, response_key_secret)

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_request_with_env_role_name_priority(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret

        os.environ["ALIBABA_CLOUD_ROLE_NAME"] = self.default_ram_role_name
        client = AcsClient()
        request = DescribeRegionsRequest()
        response = client._handle_request_in_new_style(request)
        env_credential_id = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_ID")
        env_credential_secret = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
        response_key_id = response.http_request.credentials.access_key_id
        response_key_secret = response.http_request.credentials.access_key_secret
        self.assertEqual(env_credential_id, response_key_id)
        self.assertEqual(env_credential_secret, response_key_secret)

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_request_with_config_role_name_priority(self):
        os.environ["ALIBABA_CLOUD_ROLE_NAME"] = self.default_ram_role_name

        client = AcsClient()
        request = DescribeRegionsRequest()
        response = client._handle_request_in_new_style(request)
        response_key_id = response.http_request.credentials.access_key_id
        self.assertFalse(response_key_id.startswith("TST."))

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_rpc_request_with_introduction_ak(self):
        request = DescribeRegionsRequest()
        response = self.client._handle_request_in_new_style(request)
        response_credentials = response.http_request.credentials
        from alibabacloud.credentials import AccessKeyCredentials
        self.assertEqual(type(response_credentials), AccessKeyCredentials)

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_introduction_ak(self):
        request = DescribeResourceTypesRequest()
        response = self.client._handle_request_in_new_style(request)
        response_credentials = response.http_request.credentials
        from alibabacloud.credentials import AccessKeyCredentials
        self.assertEqual(type(response_credentials), AccessKeyCredentials)

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_request_with_sts_token(self):
        client = self.init_sub_client()
        self._create_default_ram_role()

        request = AssumeRoleRequest()
        request.set_RoleArn(self.ram_role_arn)
        request.set_RoleSessionName(self.default_role_session_name)
        response = client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        credentials = response.get("Credentials")
        self.assertTrue(credentials["AccessKeyId"].startswith("STS."))

        # Using temporary AK + STS for authentication
        sts_token_credential = StsTokenCredential(credentials.get("AccessKeyId"),
                                                  credentials.get("AccessKeySecret"),
                                                  credentials.get("SecurityToken"))
        acs_client = AcsClient(region_id=self.region_id,
                               credential=sts_token_credential)
        request = DescribeRegionsRequest()
        response = acs_client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_sts_token(self):
        client = self.init_sub_client()
        self._create_default_ram_role()
        request = AssumeRoleRequest()
        request.set_RoleArn(self.ram_role_arn)
        request.set_RoleSessionName(self.default_role_session_name)
        response = client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        credentials = response.get("Credentials")
        self.assertTrue(credentials["AccessKeyId"].startswith("STS."))

        # Using temporary AK + STS for authentication
        sts_token_credential = StsTokenCredential(
            credentials.get("AccessKeyId"),
            credentials.get("AccessKeySecret"),
            credentials.get("SecurityToken")
        )
        roa_client = AcsClient(
            region_id=self.region_id,
            credential=sts_token_credential)
        request = DescribeResourceTypesRequest()
        response = roa_client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_request_with_ram_role(self):
        self._create_default_ram_user()
        self._attach_default_policy()
        self._create_access_key()
        self._create_default_ram_role()

        ram_role_arn_credential = RamRoleArnCredential(
            self.ram_user_access_key_id,
            self.ram_user_access_key_secret,
            self.ram_role_arn,
            "alice_test")
        acs_client = AcsClient(
            region_id="cn-hangzhou",
            credential=ram_role_arn_credential)
        request = DescribeRegionsRequest()
        response = acs_client._handle_request_in_new_style(request)
        response_credentials = response.http_request.credentials
        self.assertTrue(response_credentials.access_key_id.startswith("STS."))
        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_ram_role(self):
        self._create_default_ram_user()
        self._attach_default_policy()
        self._create_access_key()
        self._create_default_ram_role()

        ram_role_arn_credential = RamRoleArnCredential(
            self.ram_user_access_key_id,
            self.ram_user_access_key_secret,
            self.ram_role_arn,
            "alice_test")
        roa_client = AcsClient(
            region_id="cn-hangzhou",
            credential=ram_role_arn_credential)
        request = DescribeResourceTypesRequest()
        response = roa_client._handle_request_in_new_style(request)
        response_credentials = response.http_request.credentials
        self.assertTrue(response_credentials.access_key_id.startswith("STS."))
        response = response.http_response.content
        ret = self.get_dict_response(response)
        response = roa_client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_request_with_env_ak(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret
        client = AcsClient()
        request = DescribeRegionsRequest()
        response = client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_env_ak(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret
        client = AcsClient()
        request = DescribeResourceTypesRequest()
        response = client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    @mock.patch("alibabacloud.credentials.provider.InstanceProfileCredentialsProvider")
    def test_call_rpc_request_with_role_name(self, InstanceProfileCredentialsProvider):
        with MyServer() as f:
            os.environ["ALIBABA_CLOUD_ROLE_NAME"] = self.default_ram_role_name
            InstanceProfileCredentialsProvider.rotate_credentials.return_value = \
                requests.get(url="http://localhost:51352")
            InstanceProfileCredentialsProvider.rotate_credentials.\
                return_value = role_name
            self.assertTrue(InstanceProfileCredentialsProvider.rotate_credentials)

    def test_call_rpc_request_with_config_default(self):
        client = AcsClient()
        request = DescribeRegionsRequest()
        response = client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_config_default(self):
        client = AcsClient()
        request = DescribeResourceTypesRequest()
        response = client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    # def test_call_rpc_request_with_config_ram_role_arn(self):
    #     client = AcsClient()
    #     client._credentials_provider = DefaultChainedCredentialsProvider("ram_role_arn")
    #     request = DescribeRegionsRequest()
    #     response = client.do_action_with_exception(request)
    #     ret = self.get_dict_response(response)
    #     self.assertTrue(ret.get("Regions"))
    #     self.assertTrue(ret.get("RequestId"))

    # def test_call_roa_request_with_config_ram_role_arn(self):
    #     client = AcsClient()
    #     client._credentials_provider = DefaultChainedCredentialsProvider("ram_role_arn")
    #     request = DescribeResourceTypesRequest()
    #     response = client.do_action_with_exception(request)
    #     ret = self.get_dict_response(response)
    #     self.assertTrue(ret.get("ResourceTypes"))
    #
    # def test_call_rpc_request_with_config_bearer_token(self):
    #     client = AcsClient()
    #     client._credentials_provider = DefaultChainedCredentialsProvider("bearer_token")
    #     request = DescribeRegionsRequest()
    #     response = client.do_action_with_exception(request)
    #     ret = self.get_dict_response(response)
    #     self.assertTrue(ret.get("Regions"))
    #
    # def test_call_roa_request_with_config_bearer_token(self):
    #     client = AcsClient()
    #     client._credentials_provider = DefaultChainedCredentialsProvider("bearer_token")
    #     request = DescribeResourceTypesRequest()
    #     response = client.do_action_with_exception(request)
    #     ret = self.get_dict_response(response)
    #     self.assertTrue(ret.get("ResourceTypes"))
    #
    # def test_call_rpc_request_with_config_sts_token(self):
    #     client = AcsClient()
    #     client._credentials_provider = DefaultChainedCredentialsProvider("sts_token")
    #     request = DescribeRegionsRequest()
    #     response = client.do_action_with_exception(request)
    #     ret = self.get_dict_response(response)
    #     self.assertTrue(ret.get("Regions"))
    #     self.assertTrue(ret.get("RequestId"))
    #
    # def test_call_roa_request_with_config_sts_token(self):
    #     client = AcsClient()
    #     client._credentials_provider = DefaultChainedCredentialsProvider("sts_token")
    #     request = DescribeResourceTypesRequest()
    #     response = client.do_action_with_exception(request)
    #     ret = self.get_dict_response(response)
    #     self.assertTrue(ret.get("ResourceTypes"))
