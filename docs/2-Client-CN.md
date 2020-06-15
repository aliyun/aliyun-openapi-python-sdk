# 客户端

## 使用 AccessKey 调用

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest

# 实例化Client
client = AcsClient(
    '<access_key_id>', # RAM账号的AccessKey ID
    '<access_secret>', # RAM账号Access Key Secret
    '<region_id>' # 地域ID
)

# 创建API请求并设置参数
request = AcceptInquiredSystemEventRequest()
request.set_accept_format('json')
# 发起请求并处理应答或异常
response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))
```

## 使用默认凭证提供链

1. 环境凭证

在环境变量里寻找环境凭证，如果定义了 `ALIYUN_ACCESS_KEY_ID` 和 `ALIYUN_ACCESS_KEY_SECRET` 环境变量且不为空，程序将使用它们创建默认凭证。

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest

client = AcsClient(
    region_id='<region_id>'
)

request = AcceptInquiredSystemEventRequest()
request.set_accept_format('json')
response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))
```

2. 实例 RAM 角色

实例化Esc Ram角色凭据时，该程序将携带指定的角色名称并请求http://100.100.100.200/latest/meta-data/ram/security-credentials/以获得临时安全凭据。

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import EcsRamRoleCredential
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest

cred = EcsRamRoleCredential(
    role_name='<role name>'
)

client = AcsClient(
    region_id='<region_id>',
    credential=cred
)

request = AcceptInquiredSystemEventRequest()
request.set_accept_format('json')
response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))
```