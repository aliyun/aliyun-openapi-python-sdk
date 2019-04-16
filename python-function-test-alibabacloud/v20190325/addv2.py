from aliyunsdkcore.client import AcsClient
import base64
import AddImageRequest as AddImageRequest
import DeleteImageRequest as DeleteImageRequest
import SearchImageRequest as SearchImageRequest


# 创建 AcsClient 实例
client = AcsClient("LTAIWVkXC2eFGQ9p", "fAY7arkVlwmfxzI4WnrUCQwustXWCz", "cn-shanghai")

# 删除图片
# request = DeleteImageRequest.DeleteImageRequest()
# request.set_endpoint("imagesearch.cn-shanghai.aliyuncs.com")
# request.set_InstanceName("support")
# request.set_ProductId("100003")

# response = client.do_action_with_exception(request)
# print(response)


# # 添加图片
# request = AddImageRequest.AddImageRequest()
# request.set_endpoint("imagesearch.cn-shanghai.aliyuncs.com")
# request.set_InstanceName("support")
# request.set_ProductId("100003")
# request.set_PicName("test")

# with open('/Users/hq90172/ic01700856.jpg', 'rb') as file1:
# 	encoded_pic_content = base64.b64encode(file1.read())
# 	request.set_PicContent(encoded_pic_content)

# response = client.do_action_with_exception(request)
# print(response)


# 搜索图片
request = SearchImageRequest.SearchImageRequest()

request.set_endpoint("imagesearch.cn-shanghai.aliyuncs.com")
request.set_InstanceName("yuanshoutest2")
request.set_Start(0)
request.set_Num(10)
# with open('/Users/hq90172/ic01700856.jpg', 'rb') as file1:
with open('01.jpg', 'rb') as file1:
	encoded_pic_content = base64.b64encode(file1.read())
	request.set_PicContent(str(encoded_pic_content))

response = client.do_action_with_exception(request)
print(response)
