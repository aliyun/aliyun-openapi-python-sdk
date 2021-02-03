# 异常

## 异常处理
使用 `try...except...` 处理服务器异常和客户端异常。
```python
#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeImagesRequest import DescribeImagesRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')

request = DescribeImagesRequest()
request.set_ImageOwnerAlias("system")
try:
    response = client.do_action_with_exception(request)
    print(response)
except ClientException as e:
    # 客户端异常
    print(e)
except ServerException as e:
    # 服务端异常
    print(e)
```

## 解决异常

| 错误码                | 异常信息               |   解决办法        |
|----------------------|----------------------|------------------|
| SDK.InvalidRegionID| can not find endpoint to access     | 旧SDK版本的报错，请将`aliyun-python-sdk-core`升级到最新版本，或检查是否安装了正确的`aliyun-python-sdk-core` |
| SDK.EndpointResolvingError| No such region <region-id>. Please check your region ID. |检查Region ID，参见地域列表。|
| SDK.EndpointResolvingError| No endpoint for product <product-id>. |1，将`aliyun-python-sdk-core`，以及产品SDK（例如`aliyun-python-sdk-ecs`）升级到最新版本。<br />2，设置Endpoint来发送请求。|

