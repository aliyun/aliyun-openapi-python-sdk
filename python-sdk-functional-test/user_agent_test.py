# encoding:utf-8

from base import SDKTestBase
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest


class UserAgentTest(SDKTestBase):

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

