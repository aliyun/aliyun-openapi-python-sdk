
from aliyunsdkcore import client
from aliyunsdkcore.request import RpcRequest

clt = client.AcsClient('<your AK>', '<yout Secret>', 'cn-zhangjiakou')

request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions')
request.set_accept_format('JSON')
endpoint = clt._resolve_endpoint(request)
print endpoint
assert endpoint == 'ecs.cn-zhangjiakou.aliyuncs.com'

request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions', 'ecs')
request.set_accept_format('JSON')
endpoint = clt._resolve_endpoint(request)
print endpoint
assert endpoint == 'ecs.cn-zhangjiakou.aliyuncs.com'

client.region_provider.add_endpoint("Ecs", 'cn-zhangjiakou', 'ecs.cn-zhangjiakou123.aliyuncs.com')
clt2 = client.AcsClient('ak', 'secret', 'cn-zhangjiakou')
endpoint = clt2._resolve_endpoint(request)
print endpoint
assert endpoint == 'ecs.cn-zhangjiakou123.aliyuncs.com'

request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions')
request.set_accept_format('JSON')
endpoint = clt2._resolve_endpoint(request)
print endpoint
assert endpoint == 'ecs.cn-zhangjiakou123.aliyuncs.com'

request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions', 'ecs')
request.set_accept_format('JSON')
endpoint = clt2._resolve_endpoint(request)
print endpoint
assert endpoint == 'ecs.cn-zhangjiakou123.aliyuncs.com'