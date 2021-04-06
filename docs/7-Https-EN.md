# HTTPS Configurations

## Use HTTPS Protocol

SDK uses http protocol as default

```python
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # Region ID
)

request = DescribeInstancesRequest()
request.set_protocol_type('https')  # Use https

client.do_action_with_exception(request)
```

## Ignore certificate 

```python
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # Region ID
    verify=False  # Ignore verifying the SSL certificate
)
```

## Specify CA certificate

```python
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # Region ID
    verify='./cacert.pem'  # Path to certificates of trusted CA
)
```
