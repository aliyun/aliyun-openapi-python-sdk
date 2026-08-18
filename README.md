# Alibaba Cloud Developer Python Toolkit (V1.0 - Deprecated)

[![PyPI version](https://badge.fury.io/py/aliyun-python-sdk-core.svg)](https://badge.fury.io/py/aliyun-python-sdk-core)
[![Python test](https://github.com/aliyun/aliyun-openapi-python-sdk/actions/workflows/test.yml/badge.svg)](https://github.com/aliyun/aliyun-openapi-python-sdk/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk/graph/badge.svg?token=qmWxah6dPs)](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk)
[![python](https://img.shields.io/pypi/pyversions/aliyun-python-sdk-core.svg)](https://img.shields.io/pypi/pyversions/aliyun-python-sdk-core.svg)

⚠️ **Important Notice**: Alibaba Cloud Python SDK V1.0 has entered the basic security maintenance phase and is no longer recommended for use. It is **strongly recommended** to use the [V2.0 SDK](https://github.com/aliyun/alibabacloud-python-sdk).

## 🚨 Important Statement

**V1.0 SDK Status**:
- Currently in basic security maintenance phase
- No new features will be added

**Migration Recommendations**:
- New projects should directly use the [V2.0 SDK](https://github.com/aliyun/alibabacloud-python-sdk)
- Existing V1.0 projects are advised to migrate to V2.0 as soon as possible
- V2.0 provides better performance, a more concise API, and more complete documentation

## 🔗 V2.0 SDK Resources

**GitHub Repository**: [https://github.com/aliyun/alibabacloud-python-sdk](https://github.com/aliyun/alibabacloud-python-sdk)

**Official Documentation**: [https://help.aliyun.com/zh/sdk/developer-reference/v2-python-integrated-sdk](https://help.aliyun.com/zh/sdk/developer-reference/v2-python-integrated-sdk)

**Developer Portal**: [https://api.aliyun.com](https://api.aliyun.com)

## 🛠 Instructions for Continuing to Use V1.0 SDK

If you still need to use the V1.0 SDK, please continue reading the following content:

## Troubleshooting

[Troubleshoot](https://api.aliyun.com/troubleshoot?source=github_sdk) provides OpenAPI usage diagnostics. By entering the `RequestID` or `error message`, it helps developers quickly locate issues and provides corresponding solutions.

## Online Examples

The **[Developer Portal](https://api.aliyun.com)** provides capabilities such as invoking cloud product OpenAPIs online, dynamically generating SDK example code, and quickly searching for APIs. This can significantly reduce the difficulty of using cloud APIs and is highly recommended.

<a href="https://api.aliyun.com" target="api_explorer">
  <img src="https://img.alicdn.com/tfs/TB12GX6zW6qK1RjSZFmXXX0PFXa-744-122.png" width="180" />
</a>

## Important Updates

- Starting from version 2.16.0, the core library of Alibaba Cloud Python SDK, `aliyun-python-sdk-core`, only supports Python 3.7 and above.
- The V1.0 SDK will no longer receive new feature updates.
- It is recommended to migrate to the V2.0 SDK as soon as possible to gain better support and features.

## Documentation

- [Environment Requirements](./docs/0-Requirement-CN.md)
- [Installation](./docs/1-Installation-CN.md)
- [Client and Credentials](./docs/2-Client-CN.md)
- [Timeout Mechanism](./docs/3-Timeout-CN.md)
- [Proxy Configuration](./docs/4-Proxy-CN.md)
- [Logging](./docs/5-Log-CN.md)
- [Endpoints](./docs/6-Endpoint-CN.md)
- [HTTPS Configuration](./docs/7-Https-CN.md)
- [Debugging](./docs/8-Debug-CN.md)
- [Exceptions](./docs/9-Exception-CN.md)

## Environment Preparation

1. To use the Alibaba Cloud Python SDK, you need a cloud account and a pair of `Access Key ID` and `Access Key Secret`. Please create and view your Access Keys on the [AccessKey management page](https://usercenter.console.aliyun.com/?spm=5176.doc52740.2.3.QKZk8w#/manage/ak) in the Alibaba Cloud console, or contact your system administrator.
2. To use the Alibaba Cloud SDK to access the API of a specific product, you must first activate that product in the [Alibaba Cloud Console](https://home.console.aliyun.com/?spm=5176.doc52740.2.4.QKZk8w).

## Getting and Installing the SDK

### Install via pip (Recommended)

```bash
pip install aliyun-python-sdk-core # Install the Alibaba Cloud SDK core library
pip install aliyun-python-sdk-ecs  # Install the ECS management SDK
```

## Getting Started

The following code example demonstrates the three main steps for calling the Alibaba Cloud Python SDK:

1. Create a Client instance
2. Create an API request and set parameters
3. Send the request and handle exceptions

```python
# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest

# Create an AcsClient instance
client = AcsClient(
   "<your-access-key-id>",
   "<your-access-key-secret>",
   "<your-region-id>"
)

# Create a request and set parameters
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)

# Send the API request and print the response
response = client.do_action_with_exception(request)
print response
```

When creating the Client instance, you need to provide three parameters: Region ID, Access Key ID, and Access Key Secret. Access Key ID and Access Key Secret can be obtained from the console, and Region ID can be found in the [Region List](https://help.aliyun.com/document_detail/40654.html).

## HTTP DEBUG

To use the HTTP DEBUG feature, you need to set the `DEBUG` environment variable in your environment. Its value can be either `sdk` or `SDK`.

**HTTP DEBUG** displays the following information to help you debug your code:

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

## Contributing

Please make sure to read the [Contributing Guide](CONTRIBUTING.md) before submitting a pull request.

## License

[Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0)

---

**We recommend using the [V2.0 SDK](https://github.com/aliyun/alibabacloud-python-sdk) for a better development experience!** 🚀
