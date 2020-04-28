# Log

## Logger configuration

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
    stream=sys.stderr, # output stream
    format_string='%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s' # log format
)

client.set_file_logger(
    path='<file_path>' # log file path
)
```
