# HTTPS Configurations
1. Ignore certificate 

```python
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # Region ID
    verify=False  # Ignore verifying the SSL certificate
)
```

2. Specify CA certificate
```python
from aliyunsdkcore.client import AcsClient

client = AcsClient(
    '<access_key_id>', # AccessKey ID
    '<access_secret>', # Access Key Secret
    '<region_id>', # Region ID
    verify='./cacert.pem'  # Path with certificates of trusted CA
)
```