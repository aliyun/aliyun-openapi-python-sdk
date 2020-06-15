# Client

## Using AccessKey call

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest

# Create and initialize a AcsClient instance
client = AcsClient(
  '<access_key_id>', # The AccessKey ID of the RAM account
  '<access_secret>', # The AccessKey Secret of the RAM account
  '<region_id>' # The region ID
)

# Create an API request and set parameters
request = AcceptInquiredSystemEventRequest()
request.set_accept_format('json')
# Initiate the request and handle the response or exceptions
response = client.do_action_with_exception(request)

print(str(response, encoding='utf-8'))
```

## Use the default credential provider chain

1. Environment Credentials

Look for environment credentials in environment variable. If the `ALIYUN_ACCESS_KEY_ID` and `ALIYUN_ACCESS_KEY_SECRET` environment variables are defined and are not empty, the program will use them to create default credentials.

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

2. Instance RAM Role

When instantiating Esc Ram role credentials, the program will carry the specified role name and request http://100.100.100.200/latest/meta-data/ram/security-credentials/ to obtain temporary security credentials.

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