# encoding:utf-8
import sys
import threading

from tests import unittest

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

# the version under py3 use the different package
if sys.version_info[0] == 3:
    from http.server import SimpleHTTPRequestHandler
    from http.server import HTTPServer
else:
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer


class MyServer:
    _headers = {}
    _url = ''

    def __enter__(self):
        class ServerHandler(SimpleHTTPRequestHandler):

            def do_GET(_self):
                _self.protocol_version = 'HTTP/1.1'
                self._headers = _self.headers
                self._url = _self.path
                _self.send_response(200)
                _self.send_header("Content-type", "application/json")
                _self.end_headers()
                _self.wfile.write(b"{}")

        self.server = HTTPServer(("", 51352), ServerHandler)

        def thread_func():
            self.server.serve_forever()

        thread = threading.Thread(target=thread_func)
        thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.server:
            self.server.shutdown()
            self.server = None

    @property
    def headers(self):
        return self._headers

    @property
    def url(self):
        return self._url


class UserAgentTest(unittest.TestCase):

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
    def do_request(client, request):
        with MyServer() as s:
            client.do_action_with_exception(request)
            user_agent = s.headers.get('User-Agent')
            return user_agent

    @staticmethod
    def init_client():
        return AcsClient("access_key_id", "access_key_secret",
                         timeout=120, port=51352)

    def test_default_user_agent(self):
        client = self.init_client()
        request = CommonRequest(
            domain="ecs.aliyuncs.com",
            version="2014-05-26",
            action_name="DescribeRegions")
        request.set_endpoint("localhost")

        self.assertEqual(self.joint_default_user_agent(), self.do_request(client, request))

    def test_append_user_agent(self):
        client = self.init_client()
        request = CommonRequest(
            domain="ecs.aliyuncs.com",
            version="2014-05-26",
            action_name="DescribeRegions")

        client.append_user_agent('group', 'ali')
        request.set_endpoint("localhost")
        request.append_user_agent('cli', '1.0.0')

        self.assertEqual(self.joint_default_user_agent() + ' group/ali cli/1.0.0',
                         self.do_request(client, request))

    def test_request_set_user_agent(self):
        client = self.init_client()
        request = CommonRequest(
            domain="ecs.aliyuncs.com",
            version="2014-05-26",
            action_name="DescribeRegions")

        client.append_user_agent('group', 'ali')
        request.set_endpoint("localhost")
        request.set_user_agent('ali')
        request.append_user_agent('cli', '1.0.0')

        self.assertEqual(self.joint_default_user_agent() + ' group/ali request/ali',
                         self.do_request(client, request))

    def test_client_set_user_agent(self):
        client = self.init_client()
        request = CommonRequest(
            domain="ecs.aliyuncs.com",
            version="2014-05-26",
            action_name="DescribeRegions")

        client.set_user_agent('alibaba')
        client.append_user_agent('group', 'ali')
        request.set_endpoint("localhost")
        request.set_user_agent('ali')
        request.append_user_agent('cli', '1.0.0')

        self.assertEqual(self.joint_default_user_agent() + ' client/alibaba request/ali',
                         self.do_request(client, request))

    def test_repeat_key(self):
        client = self.init_client()
        request = CommonRequest(
            domain="ecs.aliyuncs.com",
            version="2014-05-26",
            action_name="DescribeRegions")

        client.append_user_agent('cORe', 'ali')
        request.set_endpoint("localhost")
        request.append_user_agent('pythON', '1.0.0')

        self.assertEqual(self.joint_default_user_agent(), self.do_request(client, request))

    def test_client_request_repeat_key(self):
        client = self.init_client()
        request = CommonRequest(
            domain="ecs.aliyuncs.com",
            version="2014-05-26",
            action_name="DescribeRegions")

        client.set_user_agent('ali')
        request.set_endpoint("localhost")
        request.append_user_agent('client', '1.0.0')

        self.assertEqual(self.joint_default_user_agent() + ' client/1.0.0',
                         self.do_request(client, request))

