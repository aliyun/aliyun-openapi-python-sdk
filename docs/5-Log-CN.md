# 日志

## 设置Logger

```python
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.AcceptInquiredSystemEventRequest import AcceptInquiredSystemEventRequest

import sys

client = AcsClient(
    '<access_key_id>',
    '<access_secret>',
    '<region_id>"'
)
client.set_stream_logger(
    stream=sys.stderr, # 日志输出对象
    format_string='%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s' # 日志输出格式
)

client.set_file_logger(
    path='<file_path>' # 日志文件地址
)

```
