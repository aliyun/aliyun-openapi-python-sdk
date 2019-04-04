# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import platform

from alibabacloud.handlers import RequestHandler
from alibabacloud.utils import format_type
from aliyunsdkcore.vendored.requests.structures import CaseInsensitiveDict
from aliyunsdkcore.vendored.requests.structures import OrderedDict
from aliyunsdkcore.compat import urlencode


# prepare header
def _user_agent_header():
    base = '%s (%s %s;%s)' \
           % ('AlibabaCloud',
              platform.system(),
              platform.release(),
              platform.machine()
              )
    return base


def _default_user_agent():
    default_agent = OrderedDict()
    default_agent['Python'] = platform.python_version()
    # default_agent['Core'] = __import__('aliyunsdkcore').__version__
    # default_agent['python-http_requests'] = __import__(
    #     'aliyunsdkcore.vendored.requests.__version__', globals(), locals(),
    #     ['vendored', 'requests', '__version__'], 0).__version__

    return CaseInsensitiveDict(default_agent)


def _handle_extra_agent(client_user_agent, api_request):
    # http_request_agent = http_request.http_request_user_agent()
    #
    # if client_user_agent is None:
    #     return http_request_agent
    #
    # if http_request_agent is None:
    #     return client_user_agent
    # # http_request 覆盖client的设置
    # for key in http_request_agent:
    #     if key in client_user_agent:
    #         client_user_agent.pop(key)
    # client_user_agent.update(http_request_agent)
    return client_user_agent


def _merge_user_agent(default_agent, extra_agent):
    if default_agent is None:
        return extra_agent

    if extra_agent is None:
        return default_agent
    user_agent = default_agent.copy()
    for key, value in extra_agent.items():
        if key not in default_agent:
            user_agent[key] = value
    return user_agent


def _modify_user_agent(client_user_agent, api_request):
    base = _user_agent_header()  # 默认的user-agent 的头部
    extra_agent = _handle_extra_agent(client_user_agent, api_request)  # client 和http_request的UA
    default_agent = _default_user_agent()  # 默认的UA
    # 合并默认的UA 和extra_UA
    user_agent = _merge_user_agent(default_agent, extra_agent)
    for key, value in user_agent.items():
        base += ' %s/%s' % (key, value)
    return base


class PrepareHandler(RequestHandler):
    """
    准备阶段，accept_format 以及api request的头部
    """
    def handle_request(self, context):
        http_request = context.http_request
        api_request = context.api_request
        http_request.accept_format = 'JSON'
        allow_methods = ['POST', 'PUT']

        # TODO 先组装body params 或者queryparams
        if api_request._params:
            if api_request.method in allow_methods:
                api_request.body_params.update(api_request._params)
            else:
                api_request.query_params.update(api_request._params)

        body_params = api_request.body_params
        if body_params:
            if api_request.method.upper() in allow_methods:
                import json
                body = json.dumps(body_params)
                api_request.content = body
                api_request.headers["Content-Type"] = format_type.APPLICATION_JSON

            else:
                body = urlencode(body_params, doseq=True)
                api_request.content = body
                api_request.headers["Content-Type"] = format_type.APPLICATION_FORM

            # 把这个URL编码的值赋给content，设置content-type
            # FIXME body is the final bytes to be sent to the server via HTTP
            # content is an application level concept
        elif api_request.content and "Content-Type" not in api_request.headers:

            api_request.headers["Content-Type"] = format_type.APPLICATION_OCTET_STREAM

        user_agent = _modify_user_agent(context.config.user_agent, api_request)
        api_request.headers['User-Agent'] = user_agent
        api_request.headers['x-sdk-client'] = 'python/2.0.0'
        api_request.headers['Accept-Encoding'] = 'identity'

        http_request.body = api_request.content

        http_request.method = api_request.method
        http_request.protocol = api_request.protocol  # http|https
        http_request.proxy = context.config._proxy  # {}
        if http_request.protocol == 'https':
            http_request.port = 443


    def handle_response(self, context):
        pass
