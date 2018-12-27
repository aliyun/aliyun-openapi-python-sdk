# encoding:utf-8

from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from base import SDKTestBase


class APIEncapsulateTest(SDKTestBase):

    def test_request_with_ecs(self):
        request = DescribeInstancesRequest()
        response = self.client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        self.assertTrue(response.get("Instances"))

    def test_request_with_rds(self):
        from aliyunsdkrds.request.v20140815.DescribeRegionsRequest import DescribeRegionsRequest
        request = DescribeRegionsRequest()
        response = self.client.do_action_with_exception(request)
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))

    def test_request_with_cdn(self):
        from aliyunsdkcdn.request.v20180510.DescribeCdnCertificateDetailRequest import \
            DescribeCdnCertificateDetailRequest
        request = DescribeCdnCertificateDetailRequest()
        request.set_CertName("sdk-test")
        response = self.client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        self.assertTrue(response.get("RequestId"))

    def test_request_with_slb(self):
        from aliyunsdkslb.request.v20140515.DescribeAccessControlListsRequest \
            import DescribeAccessControlListsRequest
        request = DescribeAccessControlListsRequest()
        response = self.client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        self.assertTrue(response.get("Acls"))

    def test_request_with_ram(self):
        from aliyunsdkram.request.v20150501.ListAccessKeysRequest import ListAccessKeysRequest
        request = ListAccessKeysRequest()
        response = self.client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        self.assertTrue(response.get("AccessKeys"))

    def test_request_with_vpc(self):
        from aliyunsdkvpc.request.v20160428.DescribeAccessPointsRequest \
            import DescribeAccessPointsRequest
        request = DescribeAccessPointsRequest()
        response = self.client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        self.assertTrue(response.get("AccessPointSet"))
