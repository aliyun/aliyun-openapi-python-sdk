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
import json

from alibabacloud.handlers import RequestHandler
from alibabacloud.utils import format_type
from alibabacloud.vendored.requests.structures import CaseInsensitiveDict
from alibabacloud.vendored.requests.structures import OrderedDict
from alibabacloud.compat import urlencode
from alibabacloud.utils.parameter_helper import md5_sum


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


def _modify_user_agent(client_user_agent):
    base = _user_agent_header()
    default_agent = _default_user_agent()
    # 合并默认的UA 和client_UA
    user_agent = _merge_user_agent(default_agent, client_user_agent)
    for key, value in user_agent.items():
        base += ' %s/%s' % (key, value)
    return base


class PrepareHandler(RequestHandler):

    def handle_request(self, context):
        http_request = context.http_request
        api_request = context.api_request
        http_request.accept_format = 'JSON'
        allow_methods = ['POST', 'PUT']

        # handle params to body_params or query_params
        if api_request.params:
            if api_request.method in allow_methods:
                api_request.body_params.update(api_request.params)
            else:
                api_request.query_params.update(api_request.params)

        # handle api_request region_id, rpc and roa must
        if 'RegionId' not in api_request.query_params.keys():
            api_request.query_params['RegionId'] = context.config.region_id

        # handle headers
        body_params = api_request.body_params

        if body_params:
            body = urlencode(body_params)
            api_request.content = body
            api_request.headers["Content-Type"] = format_type.APPLICATION_FORM

        elif api_request.content and "Content-Type" not in api_request.headers:
            api_request.headers["Content-Type"] = format_type.APPLICATION_OCTET_STREAM

        # 从容器服务的案例说明，content是为了弥补body的不足，弥补发布json 的不足，so 正确用法是用户设置content-type 就是
        http_request.body = api_request.content

        user_agent = _modify_user_agent(context.config.user_agent)

        api_request.headers['User-Agent'] = user_agent
        api_request.headers['x-acs-region-id'] = str(context.config.region_id)
        api_request.headers['x-sdk-client'] = 'python/2.0.0'
        api_request.headers['Accept-Encoding'] = 'identity'

        # handle other attr
        http_request.method = api_request.method
        http_request.proxy = context.config.proxy  # {}

        http_request.protocol = api_request.protocol  # http|https
        if http_request.protocol == 'https':
            http_request.port = context.config.https_port
        else:
            http_request.port = context.config.http_port

    def handle_response(self, context):
        pass
