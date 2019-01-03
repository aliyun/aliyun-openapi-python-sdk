# encoding:utf-8

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
        # create AssumeRole request ,Acquire a temporary ak
        request = AssumeRoleRequest()
        # the role must exist
        # FIXME : the RoleArn must according to user's setting
        request.set_RoleArn("acs:ram::1988236124481530:role/testrole")
        request.set_RoleSessionName("alice_test")
        client = self.init_sub_client()
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
            region_id="me-east-1",
            credential=sts_token_credential)
        request = DescribeRegionsRequest()
        url = self.get_http_request(acs_client, request)
        self.assertTrue(url.find("AccessKeyId=STS."))
        response = acs_client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_sts_token(self):
        from aliyunsdkcore.auth.credentials import RamRoleArnCredential
        # FIXME : the RoleArn must according to user's setting
        ram_role_arn_credential = RamRoleArnCredential(
            self.sub_access_key_id,
            self.sub_access_key_secret,
            "acs:ram::1988236124481530:role/testrole",
            "alice_test")
        acs_client = AcsClient(
            region_id="cn-hangzhou",
            credential=ram_role_arn_credential)
        request = DescribeRegionsRequest()
        url = self.get_http_request(acs_client, request)
        self.assertTrue(url.find("AccessKeyId=STS."))
        response = acs_client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    @disabled
    def test_ecs_ram_role(self):
        # push ecs
        from aliyunsdkcore.auth.credentials import EcsRamRoleCredential
        ecs_ram_role_credential = EcsRamRoleCredential("TestRole")
        acs_client = AcsClient(region_id="cn-hangzhou", credential=ecs_ram_role_credential)
        request = DescribeRegionsRequest()
        response = acs_client.do_action_with_exception(request)

