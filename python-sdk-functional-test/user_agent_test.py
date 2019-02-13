# encoding:utf-8

from base import SDKTestBase
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest

import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from aliyunsdkcore.client import AcsClient


class UserAgentTest(SDKTestBase):

    def start_mock_server(self):

        self.exact_headers = None

        class MySimpleHttpServer(SimpleHTTPRequestHandler):
            def do_GET(self_):
                self_.protocol_version = 'HTTP/1.1'
                self.exact_headers = self_.headers
                self_.send_response(200)
                self_.send_header("Content-type", "application/json")
                self_.end_headers()
                self_.wfile.write(b"{}")

        self.server = HTTPServer(("", 51352), MySimpleHttpServer)

        def thread_func():
            self.server.serve_forever()

        thread = threading.Thread(target=thread_func)
        thread.start()

    def tearDown(self):
        if self.server:
            self.server.shutdown()
            self.server = None

    @staticmethod
    def joint_default_user_agent():
        import platform
        base = '%s (%s %s;%s) Python/%s Core/%s python-requests/%s' \
               % ('AlibabaCloud',
                  platform.system(),
                  platform.release(),
                  platform.machine(),
                  platform.python_version(),
                  __import__('aliyunsdkcore').__version__,
                  __import__('aliyunsdkcore.vendored.requests').__version__)
        return base

    @staticmethod
    def get_headers(client, request):
        header = {}
        default_user_agent = client.default_user_agent()

        if client.get_user_agent() is not None:
            header['User-Agent'] = default_user_agent + ' extra/%s' % client.get_user_agent()
        elif 'User-Agent' in request.get_headers():
            header['User-Agent'] = \
                default_user_agent + ' extra/%s' % request.get_headers().get('User-Agent')
        else:
            if client._extra_user_agent:
                default_user_agent += ' %s' % client._extra_user_agent

            if 'extra' in request.get_headers():
                default_user_agent += ' %s' % request.get_headers().get('extra')

            header['User-Agent'] = default_user_agent
        return header

    def test_user_agent_in_mock_server(self):
        client = AcsClient(self.access_key_id, self.access_key_secret, self.region_id,
                           timeout=120, port=51352)
        request = DescribeRegionsRequest()
        request.set_endpoint("localhost")

        self.start_mock_server()
        client.do_action_with_exception(request)
        self.stop_mock_server()

        self.assertTrue('User-Agent' in self.exact_headers)
        user_agent = self.exact_headers.get('User-Agent')
        self.assertEqual(self.joint_default_user_agent(), user_agent)

    def test_agent_append(self):
        default_user_agent = self.joint_default_user_agent()

        request = DescribeRegionsRequest()
        headers = self.get_headers(self.client, request)
        self.assertEqual(default_user_agent, headers.get('User-Agent'))

        self.client.append_user_agent('group', 'ali')
        request = DescribeRegionsRequest()
        request.append_user_agent('cli', '1.0.0')
        headers = self.get_headers(self.client, request)
        self.assertEqual(default_user_agent + ' group/ali' + ' cli/1.0.0',
                         headers.get('User-Agent'))

        request = DescribeRegionsRequest()
        request.set_user_agent('ali')
        request.append_user_agent('cli', '1.0.0')
        self.client.append_user_agent('group', 'ali')
        headers = self.get_headers(self.client, request)
        self.assertEqual(default_user_agent + ' extra/ali', headers.get('User-Agent'))

        request = DescribeRegionsRequest()
        request.set_user_agent('alicloud')
        request.append_user_agent('cli', '1.0.0')
        self.client.set_user_agent('alibaba')
        self.client.append_user_agent('group', 'ali')
        headers = self.get_headers(self.client, request)
        self.assertEqual(default_user_agent + ' extra/alibaba', headers.get('User-Agent'))

