# 客户端与凭证

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

2. STS 凭证

通过安全令牌服务（Security Token Service，简称 STS），申请临时安全凭证（Temporary Security Credentials，简称 TSC），创建临时安全客户端。

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest

cred = StsTokenCredential(
    sts_access_key_id = '<sts_access_key_id>',
    sts_access_key_secret = '<sts_access_key_secret>',
    sts_token = '<sts_token>'
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

3. RamRoleArn 凭证

通过指定RAM角色，让客户端在发起请求前自动申请维护 STS Token，自动转变为一个有时限性的STS客户端。您也可以自行申请维护 STS Token，再创建 STS客户端。

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import RamRoleArnCredential
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest

cred = RamRoleArnCredential(
    sts_access_key_id='<sts_access_key_id>',
    sts_access_key_secret='<sts_access_key_secret>',
    role_arn='<role_arn>',
    session_role_name='<session_role_name>'
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

4. EcsRamRole 凭证

实例化Esc Ram角色凭据时，该程序将携带指定的角色名称并请求http://100.100.100.200/latest/meta-data/ram/security-credentials/ 以获得临时安全凭据。

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
