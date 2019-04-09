
import json
import os
import uuid

sdk_config_path = os.path.join(
    os.path.expanduser("~"),
    "aliyun_sdk_config.json")
with open(sdk_config_path) as fp:
    config = json.loads(fp.read())
    access_key_id = config['access_key_id']
    access_key_secret = config['access_key_secret']
    region_id = config['region_id']

from aliyunsdkcore.client import AcsClient

# Thu, 28 Mar 2019 03
### test retry
# from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
# client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou', connect_timeout=0.001)
# request = CreateInstanceRequest()
# request.set_ImageId("coreos_1745_7_0_64_30G_alibase_20180705.vhd")
# request.set_InstanceType('ecs.n2.valid')
# request.set_SystemDiskCategory("cloud_ssd")
#
# response = client.do_action_with_exception(request)
# print(response)

################ test roa server error
# from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest
#
# client = AcsClient(access_key_id, 'BadAccessKeySecret', 'cn-hangzhou')
# request = DescribeRegionsRequest()
# response = client.do_action_with_exception(request)
# print(response)

################## test_bug_with_18034796(self):

# client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
#
# from aliyunsdkgreen.request.v20180509 import ImageAsyncScanRequest
# request = ImageAsyncScanRequest.ImageAsyncScanRequest()
# request.set_ClientInfo('123')
# # request.set_endpoint('green.cn-shanghai.aliyuncs.com')
#
# image_url = 'https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D790/' \
#             'sign=b51ba990a68b87d65042a91637092860/' \
#             '6c224f4a20a446230ff0bec39f22720e0cf3d75c.jpg'
# import uuid
# import datetime
# # request.set_accept_format('JSON')
#
# task1 = {"dataId": str(uuid.uuid1()),
#          "url": image_url,
#          "time": datetime.datetime.now().microsecond,
#          'name': 'alice'
#          }
#
# # request.set_content(json.dumps({"tasks": [task1], "scenes": ["porn"]}))
# response = client.do_action_with_exception(request)
# print(response)


###################    def test_bug_with_17661113(self):
# client = AcsClient()
# client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
#
# from aliyunsdkcore.request import CommonRequest
# request = CommonRequest()
# request.set_domain("nlp.cn-shanghai.aliyuncs.com")
# request.set_uri_pattern("/nlp/api/reviewanalysis/ecommerce")
# request.set_method('POST')
# request.add_header("x-acs-signature-method", "HMAC-SHA1")
# request.add_header("x-acs-signature-nonce", uuid.uuid4().hex)
# request.add_header("x-acs-signature-version", "1.0")
# # content = '{"text":"裙子穿着很美哦，上身效果也不错，是纯棉的料子，穿着也很舒服。", ' \
# #           '"cate":"clothing"}'
#
# request.add_body_params('key', 'value')
# # request.set_content(content.encode('utf-8'))
# # task1 = {"dataId": str(uuid.uuid1()),
# #          "url": image_url,
# #          "time": datetime.datetime.now().microsecond,
# #          'name': '颜'
# #          }
# #
# # request.set_content(json.dumps({"tasks": [task1], "scenes": ["porn"]}))
#
# # request.set_content_type("application/json;chrset=utf-8")
# request.set_accept_format("application/json;chrset=utf-8")
#
# # request.set_content(content)
# request.set_version('2018-04-08')
# request.set_action_name("None")
#
# # We have 2 possible situations here: NLP purchased or NLP purchased
# # The test case should be passed in both situations.
# response = client.do_action_with_exception(request)
# print(response)

######### test roa body get 咩关系
# from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest
#
# client = AcsClient()
# request = DescribeRegionsRequest()
# request.add_body_params('key', 'value')
# response = client.do_action_with_exception(request)
# print(response)

# roa post body

# from aliyunsdkros.request.v20150901.PreviewStackRequest import PreviewStackRequest
# from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest
# client = AcsClient()
# request = PreviewStackRequest()
# request.add_body_params('key', 'value')
# response = client.do_action_with_exception(request)
# print(response)

## roa get body
from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdkros.request.v20150901.AbandonStackRequest import AbandonStackRequest
# client = AcsClient()
# request = DescribeRegionsRequest()
# request.add_body_params('key', 'value')
# response = client.do_action_with_exception(request)
# print(response)

## roa put body
# from aliyunsdkcr.request.v20160607.CreateNamespaceRequest import CreateNamespaceRequest
# client = AcsClient()
# request = CreateNamespaceRequest()
# request.add_body_params('key', 'value')
# response = client.do_action_with_exception(request)
# print(response)

# roa delete body
# from aliyunsdkedas.request.v20170801.DeleteDegradeControlRequest import DeleteDegradeControlRequest
# client = AcsClient()
# request = DeleteDegradeControlRequest()
# request.add_body_params('key', 'value')
# response = client.do_action_with_exception(request)
# print(response)


# roa delete body
# from aliyunsdkros.request.v20150901.AbandonStackRequest import AbandonStackRequest
#
# client = AcsClient()
# request = AbandonStackRequest()
# request.add_body_params('key', 'value')
# response = client.do_action_with_exception(request)
# print(response)



######### test roa content get 咩关系
# from aliyunsdkros.request.v20150901.DescribeRegionsRequest import DescribeRegionsRequest
# # get 的content 可以为字符串和json
# # client = AcsClient()
# client = AcsClient(access_key_id,access_key_secret, 'cn-hangzhou')
# request = DescribeRegionsRequest()
# # request.set_content('helloworld')
# # request.set_content("helloworld")
# request.set_content(json.dumps({"name":"yan"}))
# request.set_content_type('application/json')
#
# response = client.do_action_with_exception(request)
# print(response)

######### test roa content post

# from aliyunsdkros.request.v20150901.PreviewStackRequest import PreviewStackRequest
# client = AcsClient()
# # post 必须是字典dumps 之后的json的对象
# request = PreviewStackRequest()
# # request.set_content("helloworld")
# # request.set_content_type('application/json;charset=utf-8')
# request.set_content(b'hello')
# # request.set_content(json.dumps({"name": "yan"}))
# response = client.do_action_with_exception(request)
# print(response)


######### test roa content put

# from aliyunsdkcr.request.v20160607.CreateNamespaceRequest import CreateNamespaceRequest
# client = AcsClient()
# request = CreateNamespaceRequest()
# # request.set_content("helloworld")
# request.set_content_type('application/json')
# # request.set_content("helloworld")
# request.set_content(json.dumps({"name": "yan"}))
# response = client.do_action_with_exception(request)
# print(response)
######### test roa content put

# from aliyunsdkcr.request.v20160607.CreateUserSourceAccountRequest import CreateUserSourceAccountRequest
# client = AcsClient()
# request = CreateUserSourceAccountRequest()
# # request.set_content("helloworld")
# request.set_content_type('application/json;charset=utf-8')
# request.set_content_type('application/xml')
# request.set_content_type('application/x-www-form-urlencoded')
# request.set_content("helloworld")
# request.set_content(json.dumps({"name": "yan"}))
# request.add_body_params('name', 'yan')
# response = client.do_action_with_exception(request)
# print(response)

# roa delete body
# from aliyunsdkcr.request.v20160607.DeleteNamespaceRequest import DeleteNamespaceRequest
#
# client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
#
# request = DeleteNamespaceRequest()
# request.add_body_params('key', 'value')
# response = client.do_action_with_exception(request)
# print(response)

####### rpc post
# client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
#
# from aliyunsdkcore.request import CommonRequest
# request = CommonRequest()
# request.set_domain("filetrans.cn-shanghai.aliyuncs.com")
# request.set_version("2018-08-17")
# request.set_product("nls-filetrans")
# request.set_action_name("SubmitTask")
# request.set_method('POST')
# app_key = 'qVwEQ6wIZ9Pxb36t'
# file_link = 'https://aliyun-nls.oss-cn-hangzhou.aliyuncs.com/asr/fileASR/' \
#             'examples/nls-sample-16k.wav'
# task = {"app_key": app_key, "file_link": file_link}
# task = json.dumps(task)
# request.add_body_params("Task", task)
# response = client.do_action_with_exception(request)
# print(response)

############nlp
# client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
#
# from aliyunsdknls_cloud_meta.request.v20180518.CreateTokenRequest import CreateTokenRequest
#
# request = CreateTokenRequest()
# request.set_endpoint('nls-meta.cn-shanghai.aliyuncs.com')
# response = client.do_action_with_exception(request)
# print(response)


#### test ram

# client = AcsClient()
client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
# request = DescribeRegionsRequest()
# response = client.do_action_with_exception(request)
# print(response)
#


########def test_bug_with_17661113(self):
# client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
# from aliyunsdkcore.request import CommonRequest
# request = CommonRequest()
# request.set_domain("nlp.cn-shanghai.aliyuncs.com")
# request.set_uri_pattern("/nlp/api/reviewanalysis/ecommerce")
# request.set_method("POST")
# # request.add_header("x-acs-signature-method", "HMAC-SHA1")
# # request.add_header("x-acs-signature-nonce", uuid.uuid4().hex)
# # request.add_header("x-acs-signature-version", "1.0")
# # content = '{"text":"裙子穿着很美哦，上身效果也不错，是纯棉的料子，穿着也很舒服。", ' \
# #           '"cate":"clothing"}'
# content = "hello"
# request.set_content_type("application/json")
# request.set_accept_format('json')
# request.set_version('2018-04-08')
# # request.set_action_name("None")
# # request.set_content(content)
# response = client.do_action_with_exception(request)
# print(response)


# TODO 04022019
client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
# # client = AcsClient()
# from aliyunsdkcore.request import CommonRequest
# request = CommonRequest()
# request.set_domain("filetrans.cn-shanghai.aliyuncs.com")
# request.set_version("2018-08-17")
# request.set_product("nls-filetrans")
# request.set_action_name("SubmitTask")
# request.set_method('POST')
# app_key = 'qVwEQ6wIZ9Pxb36t'
# file_link = 'https://aliyun-nls.oss-cn-hangzhou.aliyuncs.com/asr/fileASR/' \
#             'examples/nls-sample-16k.wav'
# task = {"app_key": app_key, "file_link": file_link}
# task = json.dumps(task)
# request.add_body_params("Task", task)
# response = client.do_action_with_exception(request)
# print(response)
# client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou', auto_retry=True)

# retry
client = AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')

from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
request = DescribeInstancesRequest()
# request.set_endpoint("somewhere.you.will.never.get")

client.do_action_with_exception(request)


