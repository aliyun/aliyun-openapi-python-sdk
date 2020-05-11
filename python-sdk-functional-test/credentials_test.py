# encoding:utf-8
import json
import os

from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential

from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdksts.request.v20150401.AssumeRoleRequest import AssumeRoleRequest

from base import SDKTestBase
from base import disabled


class CredentialsTest(SDKTestBase):
    __name__ = 'CredentialsTest'

    def get_http_request(self, client, request, specific_signer=None):
        signer = client._signer if specific_signer is None else specific_signer
        _, url = signer.sign(client.get_region_id(), request)
        return url

    def test_call_rpc_request_with_sts_token(self):
        client = self.init_sub_client()
        self._create_default_ram_role()

        request = AssumeRoleRequest()
        request.set_RoleArn(self.ram_role_arn)
        request.set_RoleSessionName(self.default_role_session_name)
        response = client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        credentials = response.get("Credentials")

        # Using temporary AK + STS for authentication
        sts_token_credential = StsTokenCredential(
            credentials.get("AccessKeyId"),
            credentials.get("AccessKeySecret"),
            credentials.get("SecurityToken")
        )
        acs_client = AcsClient(
            region_id=self.region_id,
            credential=sts_token_credential)
        request = DescribeRegionsRequest()
        url = self.get_http_request(acs_client, request)
        self.assertTrue(url.find("AccessKeyId=STS."))
        response = acs_client.do_action_with_exception(request)
        ret = self.get_dict_response(response)

        self._delete_default_ram_role()
        self._delete_access_key()
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_sts_token(self):
        from aliyunsdkcore.auth.credentials import RamRoleArnCredential
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
        url = self.get_http_request(acs_client, request)
        self.assertTrue(url.find("AccessKeyId=STS."))
        response = acs_client.do_action_with_exception(request)
        ret = self.get_dict_response(response)

        self._delete_default_ram_role()
        self._delete_access_key()
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    @disabled
    def test_ecs_ram_role(self):
        # push ecs
        from aliyunsdkcore.auth.credentials import EcsRamRoleCredential
        ecs_ram_role_credential = EcsRamRoleCredential("EcsRamRoleTest")
        acs_client = AcsClient(region_id="cn-hangzhou", credential=ecs_ram_role_credential)
        request = DescribeRegionsRequest()
        response = acs_client.do_action_with_exception(request)
