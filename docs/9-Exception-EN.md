# 1Exceptions

## Exception handlers
Use `try...except...` statement to handle server exceptions and client exceptions.
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
    # Client Exception
    print(e)
except ServerException as e:
    # Server Exception
    print(e)
```

## Resolve exception

| Error Code                | Error Message              |   Solutions        |
|----------------------|----------------------|------------------|
| SDK.InvalidRegionID| can not find endpoint to access     | 1.Upgrade `aliyun-python-sdk-core` to the latest version.<br />2.Check whether the correct "aliyun-python-sdk-core" module is installed. |
| SDK.EndpointResolvingError| No such region <region-id>. Please check your region ID. |Check the Region ID, see the list of regions.|
| SDK.EndpointResolvingError| No endpoint for product <product-id>. |1.Upgrade `aliyun-python-sdk-core` and product SDK (such as `aliyun-python-sdk-ecs`) to the latest version.<br />2.Set Endpoint to send request.|

