# Debugging
If there is an environment variable `DEBUG=sdk`, all requests will enable debug mode.

```bash
# request
> POST /?PageSize=1&Version=2014-05-26&Action=DescribeInstances&Format=JSON&RegionId=cn-hangzhou&Timestamp=2021-02-03T02%3A12%3A32Z&SignatureMethod=HMAC-SHA1&SignatureType=&SignatureVersion=1.0&SignatureNonce=cd8f5036-4818-5775-8555-00579843f220&Signature=z7X%2B0bL9wWZ1WeHzksamtOoanbo%3D HTTP/1.1
> Host : ecs-cn-hangzhou.aliyuncs.com
> User-Agent : AlibabaCloud (Darwin 19.5.0;x86_64) Python/3.7.6 Core/2.13.30 python-requests/2.18.3
> Accept-Encoding : gzip, deflate
> Accept : */*
> Connection : keep-alive
> x-acs-action : DescribeInstances
> x-acs-version : 2014-05-26
> x-sdk-invoke-type : normal
> x-sdk-client : python/2.0.0
> Content-Length : 0

# response
< HTTP/1.1 200 OK
< Date : Wed, 03 Feb 2021 02:12:32 GMT
< Content-Type : application/json;charset=utf-8
< Transfer-Encoding : chunked
< Connection : keep-alive
< Vary : Accept-Encoding
< Access-Control-Allow-Origin : *
< Access-Control-Allow-Methods : POST, GET, OPTIONS
< Access-Control-Allow-Headers : X-Requested-With, X-Sequence, _aop_secret, _aop_signature
< Access-Control-Max-Age : 172800
< Content-Encoding : gzip
```

