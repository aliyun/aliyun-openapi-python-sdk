# 域名

Endpoint 是请求访问的域名

优先级：request > profile > rules

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest

client = AcsClient(
    'ACCESS_KEY_ID',
    'ACCESS_KEY_SECRET',
)
# 全局生效
client.add_endpoint("region_id", "product", "your endpoint")

request = DescribeRegionsRequest()
# 只对当前request生效
request.endpoint = 'your endpoint'
# 拼接规则设置网络,参数：share、 inner、 vpc、 public
request.request_network = 'public'
response = client.do_action_with_exception(request)
```

拼接规则方式需要产品端支持并符合规范方可使用。
