import os
import configparser
from aliyunsdkcore.request import RpcRequest
from aliyunsdkcore import client

cf = configparser.ConfigParser()
config_file = os.path.expanduser('~') + "/aliyun-sdk.ini"
cf.read(config_file)

clt = client.AcsClient(cf.get("daily_access_key", "id"), cf.get("daily_access_key", "secret"), 'cn-zhangjiakou')
clt2 = client.AcsClient(cf.get("daily_access_key", "id"), cf.get("daily_access_key", "secret"), 'cn-zhangjiakou')


class TestEndpoint(object):
    def test_resolve_endpoint1(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions')
        request.set_accept_format('JSON')
        endpoint = clt._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou.aliyuncs.com'

    def test_resolve_endpoint2(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions', 'ecs')
        request.set_accept_format('JSON')
        endpoint = clt._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou.aliyuncs.com'

    def test_resolve_endpoint3(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions', 'ecs')
        request.set_accept_format('JSON')
        client.region_provider.add_endpoint("Ecs", 'cn-zhangjiakou', 'ecs.cn-zhangjiakou123.aliyuncs.com')
        endpoint = clt2._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou123.aliyuncs.com'

    def test_resolve_endpoint4(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions')
        request.set_accept_format('JSON')
        endpoint = clt2._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou123.aliyuncs.com'

    def test_resolve_endpoint5(self):
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions', 'ecs')
        request.set_accept_format('JSON')
        endpoint = clt2._resolve_endpoint(request)
        print(endpoint)
        assert endpoint == 'ecs.cn-zhangjiakou123.aliyuncs.com'
