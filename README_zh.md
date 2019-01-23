# 阿里云开发者 Python 工具套件

[![Build Status](https://travis-ci.org/aliyun/aliyun-openapi-python-sdk.svg?branch=master)](https://travis-ci.org/aliyun/aliyun-openapi-python-sdk)
[![Build status](https://ci.appveyor.com/api/projects/status/ddq0kwqqbep9jasi/branch/master?svg=true)](https://ci.appveyor.com/project/aliyun/aliyun-openapi-python-sdk/branch/master)
[![codecov](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk/branch/master/graph/badge.svg)](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk)

欢迎使用阿里云开发者工具套件（SDK）。阿里云 Python SDK 让您不用复杂编程即可访问云服务器、云监控等多个阿里云服务。这里向您介绍如何获取阿里云 Python SDK 并开始调用。

如果您在使用 SDK 的过程中遇到任何问题，欢迎前往[阿里云 SDK 问答社区](https://yq.aliyun.com/tags/type_ask-tagid_23350)提问，提问前请阅读[提问引导](https://help.aliyun.com/document_detail/93957.html)。亦可在当前 GitHub 提交 Issues。

## 在线示例

**[API Explorer](https://api.aliyun.com)** 提供在线调用云产品 OpenAPI、并动态生成 SDK Example 代码和快速检索接口等能力，能显著降低使用云 API 的难度，强烈推荐使用

<a href="https://api.aliyun.com" target="api_explorer">
  <img src="https://img.alicdn.com/tfs/TB12GX6zW6qK1RjSZFmXXX0PFXa-744-122.png" width="180" />
</a>

## 环境准备

1. 要使用阿里云<span style="background-color:rgb(250, 250, 250);"><span style="color:rgb(89, 89, 89);">Python</span></span> SDK，您需要一个云账号以及一对`Access Key ID`和`Access Key Secret`。 请在阿里云控制台中的[AccessKey管理页面](https://usercenter.console.aliyun.com/?spm=5176.doc52740.2.3.QKZk8w#/manage/ak)上创建和查看您的Access Key，或者联系您的系统管理员
2. 要使用阿里云SDK访问某个产品的API，您需要事先在[阿里云控制台](https://home.console.aliyun.com/?spm=5176.doc52740.2.4.QKZk8w)中开通这个产品。

## SDK 获取和安装

### 使用 pip 安装(推荐)

```bash
pip install aliyun-python-sdk-core # 安装阿里云 SDK 核心库
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

在创建 Client 实例时，您需要填写3个参数：Region ID、Access Key ID和Access Key Secret。Access Key ID和Access Key Secret可以从控制台获得；而 Region ID 可以从[地域列表](https://help.aliyun.com/document_detail/40654.html?spm=5176.doc52740.2.8.FogWrd) 中获得
