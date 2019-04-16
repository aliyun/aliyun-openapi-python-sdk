# coding=utf-8

from alibabacloud.request import APIRequest
from alibabacloud.retry.retry_policy import get_default_retry_policy, NO_RETRY_POLICY
from alibabacloud.retry.retry_policy_context import RetryPolicyContext
from tests import unittest


class TestRetryHandler(unittest.TestCase):

    def test_handle_request(self):
        retry_config_prefix = '"{0}"."{1}"'.format("ecs", "2014-05-26")
        self.assertEqual(retry_config_prefix, '"ecs"."2014-05-26"')

        api_request = APIRequest(action_name="DescribeRegions", protocol="HTTP",
                                 method="GET", style="style")
        retry_policy_context = RetryPolicyContext(api_request, None, 0, None, retry_config_prefix)
        retry_policy = get_default_retry_policy(max_retry_times=None)
        retry_condition = retry_policy.should_retry(retry_policy_context)
        self.assertEqual(retry_condition, 3)

        retry_condition = NO_RETRY_POLICY.should_retry(retry_policy_context)
        self.assertEqual(retry_condition, 1)

    def test_handle_response(self):
        retry_config_prefix = '"{0}"."{1}"'.format("ecs", "2014-05-26")
        self.assertEqual(retry_config_prefix, '"ecs"."2014-05-26"')

        api_request = APIRequest(action_name="DescribeRegions", protocol="HTTP",
                                 method="GET", style="style")
        retry_policy_context = RetryPolicyContext(api_request, None, 0, 200, retry_config_prefix)
        retry_policy = get_default_retry_policy(max_retry_times=None)
        retry_backoff = retry_policy.compute_delay_before_next_retry(retry_policy_context)
        self.assertEqual(retry_backoff, 100)

        retry_policy = NO_RETRY_POLICY
        retry_backoff = retry_policy.compute_delay_before_next_retry(retry_policy_context)
        self.assertEqual(retry_backoff, 0)
