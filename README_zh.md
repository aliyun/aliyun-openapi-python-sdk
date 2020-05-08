# 阿里云开发者 Python 工具套件

[![PyPI version](https://badge.fury.io/py/aliyun-python-sdk-core.svg)](https://badge.fury.io/py/aliyun-python-sdk-core)
[![Build Status](https://travis-ci.org/aliyun/aliyun-openapi-python-sdk.svg?branch=master)](https://travis-ci.org/aliyun/aliyun-openapi-python-sdk)
[![Build status](https://ci.appveyor.com/api/projects/status/ddq0kwqqbep9jasi/branch/master?svg=true)](https://ci.appveyor.com/project/aliyun/aliyun-openapi-python-sdk/branch/master)
[![codecov](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk/branch/master/graph/badge.svg)](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk)

欢迎使用阿里云开发者工具套件（SDK）。阿里云 Python SDK 让您不用复杂编程即可访问云服务器、云监控等多个阿里云服务。这里向您介绍如何获取阿里云 Python SDK 并开始调用。

如果您在使用 SDK 的过程中遇到任何问题，欢迎前往 [阿里云 SDK 问答社区](https://yq.aliyun.com/tags/type_ask-tagid_23350) 提问，提问前请阅读 [提问引导](https://help.aliyun.com/document_detail/93957.html) 。亦可在当前 GitHub 提交 Issues。

## 在线示例

**[API Explorer](https://api.aliyun.com)** 提供在线调用云产品 OpenAPI、并动态生成 SDK Example 代码和快速检索接口等能力，能显著降低使用云 API 的难度，强烈推荐使用

<a href="https://api.aliyun.com" target="api_explorer">
  <img src="https://img.alicdn.com/tfs/TB12GX6zW6qK1RjSZFmXXX0PFXa-744-122.png" width="180" />
</a>

## 文档

- [环境要求](./docs/0-Requirement-CN.md)
- [安装](./docs/1-Installation-CN.md)
- [客户端](./docs/2-Client-CN.md)
- [超时机制](./docs/3-Timeout-CN.md)
- [代理配置](./docs/4-Proxy-CN.md)
- [日志](./docs/5-Log-CN.md)

## 环境准备

1. 要使用阿里云 Python SDK ，您需要一个云账号以及一对`Access Key ID`和`Access Key Secret`。 请在阿里云控制台中的 [AccessKey管理页面](https://usercenter.console.aliyun.com/?spm=5176.doc52740.2.3.QKZk8w#/manage/ak) 上创建和查看您的 Access Key，或者联系您的系统管理员
2. 要使用阿里云 SDK 访问某个产品的 API，您需要事先在 [阿里云控制台](https://home.console.aliyun.com/?spm=5176.doc52740.2.4.QKZk8w) 中开通这个产品。

## SDK 获取和安装

### 使用 pip 安装(推荐)

```bash
pip install aliyun-python-sdk-core # 安装阿里云 SDK 核心库
pip install aliyun-python-sdk-ecs # 安装管理 ECS SDK
```

## 开始调用

以下这个代码示例向您展示了调用阿里云 Python SDK 的3个主要步骤：

1. 创建 Client 实例
2. 创建 API 请求并设置参数
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

在创建 Client 实例时，您需要填写 3 个参数：Region ID、Access Key ID 和 Access Key Secret。Access Key ID 和 Access Key Secret 可以从控制台获得；而 Region ID 可以从 [地域列表](https://help.aliyun.com/document_detail/40654.html) 中获得

## HTTP DEBUG
要使用 HTTP DEBUG 功能，需要在您的环境变量配置`DEBUG`，其对应的值可以为`sdk`或`SDK`。

**HTTP DEBUG**展现如下信息，帮助您调试代码：

```
> GET /databases?RegionId=cn-hangzhou HTTP/1.1
> Host : ads.cn-hangzhou.aliyuncs.com
> User-Agent : AlibabaCloud (Windows 10;AMD64) Python/3.7.1 Core/2.13.1 python-requests/2.18.1
> accept-encoding : *
> Accept : application/json
> Connection : keep-alive
> x-sdk-invoke-type : normal
> x-acs-version : 2019-01-22
> x-acs-region-id : cn-hangzhou
> Date : Thu, 21 Feb 2019 08:00:50 GMT
> x-acs-signature-method : HMAC-SHA1
> x-acs-signature-version : 1.0
> Authorization : acs ...
> x-sdk-client : python/2.0.0

< HTTP/1.1 503 SERVICE_UNAVAILABLE
< Date : Thu, 21 Feb 2019 08:00:50 GMT
< Content-Type : application/json; charset=UTF-8
< Content-Length : 297
< Connection : keep-alive
< Access-Control-Allow-Origin : *
< Access-Control-Allow-Methods : POST, GET, OPTIONS
< Access-Control-Allow-Headers : X-Requested-With, X-Sequence, _aop_secret, _aop_signature
< Access-Control-Max-Age : 172800
< x-acs-request-id : 670F3D09-F8E7-4144-83C3-B56C35DA35ED
< Server : Jetty(7.2.2.v20101205)
```
