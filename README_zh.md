# 阿里云开发者Python工具套件

欢迎使用阿里云开发者工具套件（SDK）。阿里云Python SDK让您不用复杂编程即可访问云服务器、云监控等多个阿里云服务。这里向您介绍如何获取阿里云<span style="background-color:rgb(250, 250, 250);"><span style="color:rgb(89, 89, 89);">Python</span></span> SDK并开始调用。
如果您在使用SDK的过程中遇到任何问题，欢迎前往[阿里云SDK问答社区](https://yq.aliyun.com/tags/type_ask-tagid_23350)提问，提问前请阅读[提问引导](https://help.aliyun.com/document_detail/93957.html)。亦可在当前GitHub提交Issues。

## 环境准备
1. 要使用阿里云<span style="background-color:rgb(250, 250, 250);"><span style="color:rgb(89, 89, 89);">Python</span></span> SDK，您需要一个云账号以及一对`Access Key ID`和`Access Key Secret`。 请在阿里云控制台中的[AccessKey管理页面](https://usercenter.console.aliyun.com/?spm=5176.doc52740.2.3.QKZk8w#/manage/ak)上创建和查看您的Access Key，或者联系您的系统管理员
2. 要使用阿里云SDK访问某个产品的API，您需要事先在[阿里云控制台](https://home.console.aliyun.com/?spm=5176.doc52740.2.4.QKZk8w)中开通这个产品。


## SDK获取和安装
#### 使用pip安装(推荐)
```powershell
pip install aliyun-python-sdk-core # 安装阿里云 SDK 核心库
# 如果您使用的是 python3.x，请将上述命令修改为 pip install aliyun-python-sdk-core-v3
pip install aliyun-python-sdk-ecs # 安装管理 ECS SDK
```

## 开始调用
以下这个代码示例向您展示了调用阿里云Python SDK的3个主要步骤：
1. 创建Client实例
2. 创建API请求并设置参数
3. 发起请求并处理异常


```python
# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
# 创建 AcsClient 实例
client = AcsClient(
   "<your-access-key-id>", 
   "<your-access-key-secret>",
   "<your-region-id>"
);
# 创建 request，并设置参数
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)
# 发起 API 请求并打印返回
response = client.do_action_with_exception(request)
print response
```

在创建Client实例时，您需要填写3个参数：Region ID、Access Key ID和Access Key Secret。Access Key ID和Access Key Secret可以从控制台获得；而Region ID可以从[地域列表](https://help.aliyun.com/document_detail/40654.html?spm=5176.doc52740.2.8.FogWrd)中获得
