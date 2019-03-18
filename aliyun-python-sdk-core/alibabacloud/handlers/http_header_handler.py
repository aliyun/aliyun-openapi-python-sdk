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
from aliyunsdkcore.vendored.http_requests.structures import CaseInsensitiveDict
from aliyunsdkcore.vendored.http_requests.structures import OrderedDict
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode


class HttpHeaderHandler(RequestHandler):
    """
    处理http_request的header的内容,便于后续
    """

    def handle_http_request(self, context):
        http_request = context.http_request
        http_request.accept_format = 'JSON'

        if http_request.body_params is not None:
            body = urlencode(http_request.body_params)
            # 把这个URL编码的值赋给content，设置content-type

            # FIXME body is the final bytes to be sent to the server via HTTP
            # content is an application level concept
            http_request.body = body
            http_request.content = content
            http_request.content_type = format_type.APPLICATION_FORM
        elif http_request.content and "Content-Type" not in http_request.headers:
            http_request.content_type = format_type.APPLICATION_OCTET_STREAM

        user_agent = self.modify_user_agent(context.config.user_agent, http_request)
        http_request.headers['User-Agent'] = user_agent
        http_request.headers['x-sdk-client'] = 'python/2.0.0'
        http_request.headers['Accept-Encoding'] = 'identity'

        context.http_request = http_request

    def handle_response(self, context):
        # context 实际是http_request
        pass

    # UA 开始
    @staticmethod
    def user_agent_header():
        base = '%s (%s %s;%s)' \
               % ('AlibabaCloud',
                  platform.system(),
                  platform.release(),
                  platform.machine()
                  )
        return base

    @staticmethod
    def default_user_agent():
        default_agent = OrderedDict()
        default_agent['Python'] = platform.python_version()
        default_agent['Core'] = __import__('aliyunsdkcore').__version__
        default_agent['python-http_requests'] = __import__(
            'aliyunsdkcore.vendored.http_requests.__version__', globals(), locals(),
            ['vendored', 'http_requests', '__version__'], 0).__version__

        return CaseInsensitiveDict(default_agent)

    @staticmethod
    def handle_extra_agent(client_user_agent, http_request):
        http_request_agent = http_request.http_request_user_agent()

        if client_user_agent is None:
            return http_request_agent

        if http_request_agent is None:
            return client_user_agent
        # http_request 覆盖client的设置
        for key in http_request_agent:
            if key in client_user_agent:
                client_user_agent.pop(key)
        client_user_agent.update(http_request_agent)
        return client_user_agent

    @staticmethod
    def merge_user_agent(default_agent, extra_agent):
        if default_agent is None:
            return extra_agent

        if extra_agent is None:
            return default_agent
        user_agent = default_agent.copy()
        for key, value in extra_agent.items():
            if key not in default_agent:
                user_agent[key] = value
        return user_agent

    def _modify_user_agent(self, client_user_agent, http_request):
        base = self.user_agent_header()  # 默认的user-agent 的头部
        extra_agent = self.handle_extra_agent(client_user_agent, http_request)  # client 和http_request的UA
        default_agent = self.default_user_agent()  # 默认的UA
        # 合并默认的UA 和extra_UA
        user_agent = self.merge_user_agent(default_agent, extra_agent)
        for key, value in user_agent.items():
            base += ' %s/%s' % (key, value)
        return base
    # UA 结束
