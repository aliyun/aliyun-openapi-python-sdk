# 域名

Endpoint 是请求接口服务的网络域名，如 `ecs.cn-hangzhou.aliyuncs.com`

### Endpoint 寻址

[相关源码](https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-core/aliyunsdkcore/endpoint/default_endpoint_resolver.py)

1. 用户自定义

`用户自定义`是优先级最高的寻址逻辑，可以直接指定 endpoint 的具体内容。

```python
# 全局生效
client = AcsClient()
client.add_endpoint("<region_id>", "<product>", "<endpoint>")

# 只对当前 Request 生效
request = DescribeRegionsRequest()
request.set_endpoint("<endpoint>")
```

2. Endpoint 拼接规则

在请求 vpc 网络时或产品 SDK 具有 Endpoint 数据文件时，当前寻址逻辑才会生效。 Endpoint 数据文件示例 ([Ecs Endpoint Data File](https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-ecs/aliyunsdkecs/endpoint.py))

```python
# 公网请求
request.request_network = "public" # 因为 `network` 的默认值为 `public`，所以默认情况下不需要配置 `network`

# 跨域请求
request.request_network = "share"

# Ipv6 请求
request.request_network = "ipv6"

# 代理请求
request.request_network = "proxy"

# 内部请求
request.request_network = "inner"

# Ipv4/Ipv6 双协议栈
request.request_network = "dualstack"

# vpc 请求
request.request_network = "vpc"
```

3. 根据 Python SDK Core 中的 [endpoints.json](https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-core/aliyunsdkcore/data/endpoints.json) 数据文件进行寻址

内部操作，无需额外配置。

4. 请求 Location 服务接口，从远端获取

需要产品 SDK 具备 `ServiceCode`