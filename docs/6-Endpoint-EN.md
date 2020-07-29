# Endpoint

Endpoint is the domain name of the service API. like `ecs.cn-hangzhou.aliyuncs.com`

### Search Endpoint

[Related source code](https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-core/aliyunsdkcore/endpoint/default_endpoint_resolver.py)

1. User custom defined

`User custom defined` is the highest-priority logic to search endpoint and allows you to specify endpoint specifics directly.

```python
# Global effect
client = AcsClient()
client.add_endpoint("<region_id>", "<product>", "<endpoint>")


# Only works for the current request
request = DescribeRegionsRequest()
request.set_endpoint("<endpoint>")
```

2. Endpoint Splicing Rules

`Endpoint Splicing Rules` does not take effect until the vpc network is enabled or the product SDK has an Endpoint data file. Endpoint Data File Example : ([Ecs Endpoint Data File](https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-ecs/aliyunsdkecs/endpoint.py))

```python
# Public network request(default)
request.request_network = "public" # Since the default value of `network` is `public`, there is no need to configure `network` by default.

# Share-domain request
request.request_network = "share"

# Ipv6 network request
request.request_network = "ipv6"

# Proxy network request
request.request_network = "proxy"

# Internal network request
request.request_network = "inner"

# Ipv4/Ipv6 Dual Stack
request.request_network = "dualstack"

# Vpc network request
request.request_network = "vpc"
```

3. Search endpoint from the [endpoints.json](https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-core/aliyunsdkcore/data/endpoints.json) endpoint data file in the Java SDK Core Internal operation, no additional configuration required.

4. Request Location Service API to get `Endpoint` from the remote end.

Requires product SDK with `ServiceCode`.