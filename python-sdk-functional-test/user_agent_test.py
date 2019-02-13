# encoding:utf-8

from base import SDKTestBase
from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest


class UserAgentTest(SDKTestBase):

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
        self.client.append_user_agent('group', 'ali')
        request = DescribeRegionsRequest()
        request.append_user_agent('cli', '1.0.0')
        headers = self.get_headers(self.client, request)
        self.assertTrue('cli/1.0.0' in headers.get('User-Agent'))
        self.assertTrue('group/ali' in headers.get('User-Agent'))

        request = DescribeRegionsRequest()
        request.set_user_agent('ali')
        request.append_user_agent('cli', '1.0.0')
        headers = self.get_headers(self.client, request)
        self.assertTrue('extra/ali' in headers.get('User-Agent'))
        self.assertFalse('cli/1.0.0' in headers.get('User-Agent'))
        self.assertFalse('group/ali' in headers.get('User-Agent'))

        request = DescribeRegionsRequest()
        request.set_user_agent('alicloud')
        request.append_user_agent('cli', '1.0.0')
        self.client.set_user_agent('alibaba')
        headers = self.get_headers(self.client, request)
        self.assertTrue('extra/alibaba' in headers.get('User-Agent'))
        self.assertFalse('alicloud' in headers.get('User-Agent'))
        self.assertFalse('cli/1.0.0' in headers.get('User-Agent'))
        self.assertFalse('group/ali' in headers.get('User-Agent'))
