# encoding:utf-8

from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from base import SDKTestBase
from aliyunsdkcore.acs_exception.exceptions import ServerException


class ROABodyTest(SDKTestBase):

    def test_roa_body_params_with_get(self):
        from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest

        request = DescribeRegionsRequest()
        request.add_body_params('key', 'value')
        response = self.client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        self.assertTrue(response.get("Regions"))

    def test_roa_body_params_with_put(self):
        from aliyunsdkcr.request.v20160607.CreateNamespaceRequest import CreateNamespaceRequest
        request = CreateNamespaceRequest()
        request.add_body_params('key', 'value')
        try:
            response = self.client.do_action_with_exception(request)
            assert False

        except ServerException as e:
            self.assertEqual("SDK.UnknownServerError", e.error_code)

    def test_roa_body_params_with_delete(self):
        from aliyunsdkros.request.v20150901.AbandonStackRequest import AbandonStackRequest

        request = AbandonStackRequest()
        request.add_body_params('key', 'value')
        try:
            response = self.client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("InvalidUrl", e.error_code)

    def test_roa_body_params_with_post(self):

        from aliyunsdkros.request.v20150901.PreviewStackRequest import PreviewStackRequest
        request = PreviewStackRequest()
        request.add_body_params('key', 'value')
        try:
            response = self.client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("MissingParameter", e.error_code)

    def test_roa_content_with_get(self):
        from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest

        request = DescribeRegionsRequest()
        request.set_content("helloworld")
        response = self.client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        self.assertTrue(response.get("Regions"))

    def test_roa_content_with_put(self):
        from aliyunsdkcr.request.v20160607.CreateNamespaceRequest import CreateNamespaceRequest
        request = CreateNamespaceRequest()
        request.add_body_params('key', 'value')
        try:
            response = self.client.do_action_with_exception(request)
            assert False

        except ServerException as e:
            self.assertEqual("SDK.UnknownServerError", e.error_code)

    def test_roa_content_with_delete(self):
        from aliyunsdkros.request.v20150901.AbandonStackRequest import AbandonStackRequest

        request = AbandonStackRequest()
        request.add_body_params('key', 'value')
        try:
            response = self.client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("InvalidUrl", e.error_code)

    def test_roa_content_with_post(self):

        from aliyunsdkros.request.v20150901.PreviewStackRequest import PreviewStackRequest
        request = PreviewStackRequest()
        request.add_body_params('key', 'value')
        try:
            response = self.client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("MissingParameter", e.error_code)