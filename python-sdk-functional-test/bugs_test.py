# encoding:utf-8
import datetime
import json
import sys
from tests import unittest
import uuid

from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.http import method_type
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.request import CommonRequest, RpcRequest
from base import SDKTestBase


class BugsTest(SDKTestBase):

    def test_bug_with_18034796(self):
        from aliyunsdkgreen.request.v20180509 import ImageAsyncScanRequest
        region_provider.modify_point(
            'Green', 'cn-shanghai', 'green.cn-shanghai.aliyuncs.com')
        request = ImageAsyncScanRequest.ImageAsyncScanRequest()
        image_url = 'https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D790/' \
                    'sign=b51ba990a68b87d65042a91637092860/' \
                    '6c224f4a20a446230ff0bec39f22720e0cf3d75c.jpg'
        task1 = {"dataId": str(uuid.uuid1()),
                 "url": image_url,
                 "time": datetime.datetime.now().microsecond
                 }
        request.set_content(json.dumps({"tasks": [task1], "scenes": ["porn"]}))
        client = self.init_client(region_id="cn-hangzhou")
        response = client.do_action_with_exception(request)
        response = self.get_dict_response(response)
        self.assertEqual(200, response.get("code"))

    def test_bug_with_17661113(self):
        request = CommonRequest()
        request.set_domain("nlp.cn-shanghai.aliyuncs.com")
        request.set_uri_pattern("/nlp/api/reviewanalysis/ecommerce")
        request.set_method(method_type.POST)
        request.add_header("x-acs-signature-method", "HMAC-SHA1")
        request.add_header("x-acs-signature-nonce", uuid.uuid4().hex)
        request.add_header("x-acs-signature-version", "1.0")
        content = '{"text":"裙子穿着很美哦，上身效果也不错，是纯棉的料子，穿着也很舒服。", ' \
                  '"cate":"clothing"}'
        request.set_content_type("application/json;chrset=utf-8")
        request.set_accept_format("application/json;chrset=utf-8")
        if sys.version_info[0] == 2:
            request.set_content(content)
        else:
            request.set_content(content.encode('utf-8'))
        request.set_version('2018-04-08')
        request.set_action_name("None")
        try:
            response = self.client.do_action_with_exception(request)
            assert False
        except ServerException as e:
            self.assertEqual("InvalidApi.NotPurchase", e.error_code)
            self.assertEqual("Specified api is not purchase", e.get_error_msg())

    def test_bug_with_17602976(self):
        from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
        request = DescribeRegionsRequest()
        request.set_accept_format('JSON')
        status, headers, body, exception = self.client._implementation_of_do_action(request)
        try:
            body_obj = ["ecs", "rdm", "roa"]
            request_id = body_obj.get("RequestId")
            assert False
        except (ValueError, TypeError, AttributeError) as e:
            self.assertEqual("'list' object has no attribute 'get'", e.args[0])
