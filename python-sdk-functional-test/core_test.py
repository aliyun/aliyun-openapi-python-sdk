# encoding:utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkcore.request import CommonRequest

from aliyunsdksts.request.v20150401.AssumeRoleRequest import AssumeRoleRequest

from base import SDKTestBase, MyServer


class CoreLevelTest(SDKTestBase):

    def test_rpc_with_common_request(self):
        request = CommonRequest(
            domain="ecs.aliyuncs.com",
            version="2014-05-26",
            action_name="DescribeRegions")
        response = self.client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_roa_with_common_request(self):
        request = CommonRequest(
            domain="ros.aliyuncs.com",
            version="2015-09-01",
            action_name="DescribeResourceTypes",
            uri_pattern="/resource_types")
        response = self.client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_rpc_common_request_with_sts_token(self):
        sub_client = self.init_sub_client()
        self._create_default_ram_role()
        self._attach_default_policy()

        request = AssumeRoleRequest()
        request.set_RoleArn(self.ram_role_arn)
        request.set_RoleSessionName(self.default_role_session_name)
        response = sub_client.do_action_with_exception(request)
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
        # the common request
        request = CommonRequest(
            domain="ecs.aliyuncs.com",
            version="2014-05-26",
            action_name="DescribeRegions")
        response = acs_client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self._delete_default_ram_role()
        self._delete_access_key()
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_rpc_common_request_with_https(self):
        request = CommonRequest(
            domain="ecs.aliyuncs.com",
            version="2014-05-26",
            action_name="DescribeRegions")
        request.set_protocol_type("https")
        self.assertTrue(request.get_protocol_type().lower() == "https")
        response = self.client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_common_request_with_https(self):
        request = CommonRequest(
            domain="ros.aliyuncs.com",
            version="2015-09-01",
            action_name="DescribeResourceTypes",
            uri_pattern="/resource_types")
        request.set_protocol_type("https")
        self.assertTrue(request.get_protocol_type().lower() == "https")
        response = self.client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    @staticmethod
    def get_http_request(client, request, specific_signer=None):
        signer = client._signer if specific_signer is None else specific_signer
        _, url = signer.sign(client.get_region_id(), request)
        return url

    def test_signer_with_unicode_specific_params(self):
        from aliyunsdkcdn.request.v20180510.DescribeCdnCertificateDetailRequest import \
            DescribeCdnCertificateDetailRequest
        request = DescribeCdnCertificateDetailRequest()
        request.set_CertName("sdk&-杭&&&州-test")
        url = self.get_http_request(self.client, request)
        self.assertTrue(url.find("CertName="))
        response = self.client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        self.assertTrue(response.get("RequestId"))

    def test_signer_with_unicode_specific_params_2(self):
        from aliyunsdkcdn.request.v20180510.DescribeCdnCertificateDetailRequest import \
            DescribeCdnCertificateDetailRequest
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           timeout=120, port=51352)
        request = DescribeCdnCertificateDetailRequest()
        request.set_CertName("sdk&-杭&&&州-test")
        request.set_endpoint("localhost")
        request.set_method('GET')
        with MyServer() as s:
            client.do_action_with_exception(request)
            self.assertTrue(s.url.find("CertName="))
