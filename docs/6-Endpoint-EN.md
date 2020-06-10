# Endpoint

The endpoint is the domain you want to access

Priority：request > profile > rules

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest

client = AcsClient(
    'ACCESS_KEY_ID',
    'ACCESS_KEY_SECRET',
)
# global
client.add_endpoint("region_id", "product", "your endpoint")

request = DescribeRegionsRequest()
# Only the current request is valid
request.endpoint = 'your endpoint'
# Splicing rules set the network; parameter:share、 inner、 vpc、 public
request.request_network = 'public'
response = client.do_action_with_exception(request)
```

Splicing rules need to be supported by the product side and conform to the specification before they can be used。
