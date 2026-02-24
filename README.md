# Alibaba Cloud Python Software Development Kit (V1.0 - Deprecated)

[![PyPI version](https://badge.fury.io/py/aliyun-python-sdk-core.svg)](https://badge.fury.io/py/aliyun-python-sdk-core)
[![Python test](https://github.com/aliyun/aliyun-openapi-python-sdk/actions/workflows/test.yml/badge.svg)](https://github.com/aliyun/aliyun-openapi-python-sdk/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk/graph/badge.svg?token=qmWxah6dPs)](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk)
[![python](https://img.shields.io/pypi/pyversions/aliyun-python-sdk-core.svg)](https://img.shields.io/pypi/pyversions/aliyun-python-sdk-core.svg)

[English](./README.md) | [中文文档](./README_zh.md)

⚠️ **重要通知**: 阿里云 Python SDK V1.0 已进入基础安全维护阶段，不再推荐使用。**强烈建议**使用 [V2.0 SDK](https://github.com/aliyun/alibabacloud-python-sdk)。

## 🚨 重要声明

**V1.0 SDK状态**: 
- 当前处于基础安全维护阶段
- 不再添加新功能

**迁移建议**:
- 新项目请直接使用 [V2.0 SDK](https://github.com/aliyun/alibabacloud-python-sdk)
- 现有V1.0项目建议尽快迁移至V2.0
- V2.0提供更好的性能、更简洁的API和更完善的文档

## 🔗 V2.0 SDK 资源

**GitHub仓库**: [https://github.com/aliyun/alibabacloud-python-sdk](https://github.com/aliyun/alibabacloud-python-sdk)

**官方文档**: [https://help.aliyun.com/zh/sdk/developer-reference/v2-python-integrated-sdk](https://help.aliyun.com/zh/sdk/developer-reference/v2-python-integrated-sdk)

**开发者门户**: [https://api.aliyun.com](https://api.aliyun.com)

## 🛠 V1.0 SDK 继续使用说明

如果您仍需要使用V1.0 SDK，请继续阅读以下内容：

## 🆘 故障诊断

[Troubleshoot](https://api.aliyun.com/troubleshoot?source=github_sdk) 提供OpenAPI使用诊断服务，通过 `RequestID` 或 `报错信息` 帮助开发者快速定位问题并提供解决方案。

## 🌐 在线示例

**[开发者门户](https://api.aliyun.com)** 提供在线调用云产品OpenAPI、动态生成SDK示例代码和快速检索接口等功能，能显著降低使用云API的难度。**强烈推荐使用**。

## ⚠️ 重要更新

- 从版本2.16.0开始，阿里云Python SDK核心库 `aliyun-python-sdk-core` 仅支持Python 3.7及以上版本
- V1.0 SDK将不再接收新功能更新
- 建议尽快迁移到V2.0 SDK以获得更好的支持和功能

## 📚 V1.0 文档

- [环境要求](docs/0-Requirement-EN.md)
- [安装](./docs/1-Installation-EN.md)
- [客户端与凭证](./docs/2-Client-EN.md)
- [超时机制](./docs/3-Timeout-EN.md)
- [代理配置](./docs/4-Proxy-EN.md)
- [日志](./docs/5-Log-EN.md)
- [域名](./docs/6-Endpoint-EN.md)
- [Https配置](./docs/7-Https-EN.md)
- [调试](./docs/8-Debug-EN.md)
- [异常处理](./docs/9-Exception-EN.md)

## 📋 前提条件

- 使用阿里云Python SDK需要拥有阿里云账号以及AccessKey

	初始化 `AcsClient` 时需要AccessKey。您可以在阿里云控制台创建AccessKey。更多信息请参见[创建AccessKey](https://usercenter.console.aliyun.com/?spm=5176.doc52740.2.3.QKZk8w#/manage/ak)。

	> **注意：** 为了提高账号安全性，建议使用RAM用户的AccessKey访问阿里云服务。

- 使用阿里云Python SDK访问产品API前，如需要请先在[阿里云控制台](https://home.console.aliyun.com/?spm=5176.doc52740.2.4.QKZk8w)开通该产品。

- 阿里云Python SDK要求Python 3.7.x及以上版本。

## 📦 安装Python SDK

阿里云Python SDK支持Python 3.7.x及以上版本。运行 ``python --version`` 检查您的Python版本。

您可以使用以下两种方法安装阿里云Python SDK。无论使用哪种方法和云服务，都必须安装核心库 `aliyun-python-sdk-core`。

- **使用pip安装（推荐）**

	Python SDK使用名为 `pip` 的通用包管理工具。如果未安装pip，请参见[pip用户指南](https://pip.pypa.io/en/stable/installing/?spm=5176.doc53090.2.7.zHDiNV "pip User Guide")安装pip。

	运行以下命令安装阿里云服务的各个库：

	```bash
	# 安装核心库
	pip install aliyun-python-sdk-core
	# 安装ECS管理库
	pip install aliyun-python-sdk-ecs
	# 安装RDS管理库
	pip install aliyun-python-sdk-rds
	```

## 🚀 使用Python SDK

1. 导入所需模块：

    ```python
    from aliyunsdkcore.client import AcsClient
    from aliyunsdkcore.acs_exception.exceptions import ClientException
    from aliyunsdkcore.acs_exception.exceptions import ServerException
    from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
    from aliyunsdkecs.request.v20140526 import StopInstanceRequest
    ```
2. 初始化 `AcsClient` 实例：

    ```python
    client = AcsClient(
        "<access-key-id>",
        "<access-key-secret>",
        "<region-id>"
    )
    ```

	其中：

	- `access-key-id` 是您账号的AccessKey ID。
	- `access-key-secret` 是您账号的AccessKey Secret。
	- `region-id` 是调用服务的区域ID。区域ID列表请参见[地域和可用区](https://www.alibabacloud.com/help/doc-detail/40654.html)。

	> **注意：** 这些参数的顺序不能更改。

3. 初始化请求并打印响应：

	```python
	# 初始化请求并设置参数
	request = DescribeInstancesRequest.DescribeInstancesRequest()
	request.set_PageSize(10)
	# 打印响应
	response = client.do_action_with_exception(request)
	print response
	```

## 💻 代码示例

以下示例展示了如何使用[DescribeInstances](~~25506~~)查询特定区域的ECS实例列表。请替换 `your-access-key-id`、`your-access-key-secret` 和 `your-region-id` 的值。

```python
# -*- coding: utf8 -*-

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest

# 初始化AcsClient实例
client = AcsClient(
  "<your-access-key-id>",
  "<your-access-key-secret>",
  "<your-region-id>"
)

# 初始化请求并设置参数
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)

# 打印响应
response = client.do_action_with_exception(request)
print response
```

## 🐛 HTTP调试

要使用 `HTTP DEBUG` 功能，您必须在环境变量中设置 `DEBUG`，对应的值可以是 `sdk` 或 `SDK`。

以下示例展示了 `HTTP DEBUG` 的作用，这将帮助您调试代码：

```plaintext
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

## 🤝 贡献

请确保在提交pull request之前阅读[贡献指南](CONTRIBUTING.md)。

## 📄 许可证

[Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0)

---

**推荐使用 [V2.0 SDK](https://github.com/aliyun/alibabacloud-python-sdk) 获得更好的开发体验！** 🚀
