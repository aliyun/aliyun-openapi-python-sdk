# HTTPS配置
1. 忽略证书 

```python
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # 地域ID
    verify=False  # 忽略对 SSL 证书的验证
)
```

2. 指定CA证书文件
```python
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # 地域ID
    verify='./cacert.pem'  # 证书路径
)
```