# 超时机制

Request 设置 -> Client 设置 -> 默认，优先级依次降低； 默认连接超时为5秒，读超时为10秒；

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest
# Client超时设置，对当前所有request有效
client = AcsClient(
  '<access_key_id>',
  '<access_secret>',
  '<region_id>"',
  connect_timeout=10, # 连接超时
  timeout=15 # 读超时时间
)

request = AcceptInquiredSystemEventRequest()
# request超时设置，仅对当前请求有效
request.set_connect_timeout(10)
request.set_read_timeout(15)
```
