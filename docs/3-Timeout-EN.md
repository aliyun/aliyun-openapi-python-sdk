# Timeout

Request Settings -> Client Settings -> Default Settings, priority from high to low; The default ConnectTimeout is 5 seconds and the ReadTimeout is 10 seconds.

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest
# The client setting is valid for all requests
client = AcsClient(
  '<access_key_id>',
  '<access_secret>',
  '<region_id>"',
  connect_timeout=10, # connect timeout
  timeout=15 # read timeout
)

request = AcceptInquiredSystemEventRequest()
# The request setting, valid only for the current request
request.set_connect_timeout(10)
request.set_read_timeout(15)
```
