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

from alibabacloud.handlers import RequestHandler


class HttpHeaderHandler(RequestHandler):
    """
    处理request的header的内容,便于后续
    """

    def handle_request(self, context):
        request = context.request
        # origin_request_handler 处理了：
        # 1.设置format
        request.set_accept_format('JSON')  # set 可以来自于配置config
        # 2.body_params 部分,body_params 应该是一个字典或者json字符串
        body_params = request.get_body_params()
        if body_params:
            if not isinstance(body_params, dict):
                body_params = json.loads(body_params)
            body = urlencode(body_params)
            # 把这个URL编码的值赋给content，设置content-type
            request.set_content(body)
            request.set_content_type(format_type.APPLICATION_FORM)
        elif request.get_content() and "Content-Type" not in request.get_headers():
            request.set_content_type(format_type.APPLICATION_OCTET_STREAM)

        request.add_header('Accept-Encoding', 'identity')
        user_agent = self.get_user_agent(client, request)
        request.add_header('User-Agent', user_agent)
        request.add_header('x-sdk-client', 'python/2.0.0')

        context.request = request


    def handle_response(self, context, response):
        # context 实际是request
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
        default_agent['python-requests'] = __import__(
            'aliyunsdkcore.vendored.requests.__version__', globals(), locals(),
            ['vendored', 'requests', '__version__'], 0).__version__

        return CaseInsensitiveDict(default_agent)

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

    @staticmethod
    def handle_extra_agent(client, request):
        client_agent = client.client_user_agent()
        request_agent = request.request_user_agent()

        if client_agent is None:
            return request_agent

        if request_agent is None:
            return client_agent
        # request 覆盖client的设置
        for key in request_agent:
            if key in client_agent:
                client_agent.pop(key)
        client_agent.update(request_agent)
        return client_agent

    def get_user_agent(self, client, request):
        base = self.user_agent_header()  # 默认的user-agent 的头部
        extra_agent = self.handle_extra_agent(client, request)  # client 和request的UA
        default_agent = self.default_user_agent()  # 默认的UA
        # 合并默认的UA
        user_agent = self.merge_user_agent(default_agent, extra_agent)
        for key, value in user_agent.items():
            base += ' %s/%s' % (key, value)
        return base
    # UA 结束
