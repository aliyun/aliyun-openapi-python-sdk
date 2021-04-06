# HTTPS配置
## 使用HTTPS协议

SDK默认使用http协议

```python
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # 地域ID
)

request = DescribeInstancesRequest()
request.set_protocol_type('https')  # 使用https

client.do_action_with_exception(request)
```

## 忽略证书 

```python
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # 地域ID
    verify=False  # 忽略对 SSL 证书的验证
)
```

## 指定CA证书文件

```python
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # 地域ID
    verify='./cacert.pem'  # 证书路径
)
```
