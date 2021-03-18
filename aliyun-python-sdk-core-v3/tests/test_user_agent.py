# encoding:utf-8

from tests import unittest, MyServer

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


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
                  __import__('aliyunsdkcore.vendored.requests.__version__', globals(), locals(),
                             ['vendored', 'requests', '__version__'], 0).__version__)
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

