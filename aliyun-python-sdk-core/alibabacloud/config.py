def config_from_os():
    http_debug = http_debug
    proxy_https = os.environ.get('HTTPS_PROXY') or os.environ.get(
        'https_proxy')
    proxy_http = os.environ.get(
        'HTTP_PROXY') or os.environ.get('http_proxy')
    os_config = {
        'http_debug': http_debug,
        'proxy_http': proxy_http,
    }
    return os_config


def config_from_ini(profile_name):
    # ini file loads 出来是dict
    ini_config = {}
    return ini_config


def config_from_client(client):
    user_agent = client.user_agent
    connection_timeout = client.connection_timeout
    read_timeout = client.read_timeout
    client_config = {
        'connection_timeout': connection_timeout,
        'read_timeout': read_timeout,
    }
    return client_config


def config_from_request(request):
    user_agent = request.user_agent
    connection_timeout = request.connection_timeout
    read_timeout = request.read_timeout
    request_config = {
        'connection_timeout': connection_timeout,
        'read_timeout': read_timeout,
    }
    return request_config

# config 初始化之后，仅仅保留一个值，已经确定了三级当中的生效的值是什么


class Config:
    """
    处理client级别的所有的参数
    """
    def __init__(self, access_key_id=None, access_key_secret=None, region_id=None,
                 enable_retry_policy=True, max_retry_times=None, user_agent=None,
                 extra_user_agent=None, enable_https=True, http_port=None, https_port=None,
                 connection_timeout=None, read_timeout=None, accept_format=DEFAULT_FORMAT,
                 resolve_endpoint_cls=None, specific_signer=None):

        # 这就覆盖config了,request 不进行覆盖，进行校验
        ini_config = config_from_ini(profile_name)
        for config_key, config_value in ini_config.items():
            setattr(self, config_key, getattr(ini_config, config_key))

        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.region_id = region_id
        self.enable_retry_policy = enable_retry_policy
        self.max_retry_times = max_retry_times
        self.user_agent = user_agent
        self.extra_user_agent = extra_user_agent
        self.enable_https = enable_https
        self.http_port = http_port
        self.https_port = https_port
        self.connection_timeout = connection_timeout
        self.read_timeout = read_timeout
        # yan 添加的
        self.accept_format = accept_format
        self.resolve_endpoint_cls = resolve_endpoint_cls or ResolveEndpointRequest
        self.specific_signer = specific_signer

        # 用户硬编码传参、环境变量、读配置文件的获取参数的方式
        # TODO assign more attributes
