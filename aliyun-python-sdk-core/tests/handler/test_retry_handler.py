# coding=utf-8

from alibabacloud.request import APIRequest
from alibabacloud.retry.retry_policy import get_default_retry_policy, NO_RETRY_POLICY
from alibabacloud.retry.retry_policy_context import RetryPolicyContext
from tests import unittest


class TestRetryHandler(unittest.TestCase):

    def test_handle_request(self):
        product_code = "ecs"
        product_version = "2014-05-26"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        retry_policy_context = RetryPolicyContext(api_request, None, 0, None, product_code,
                                                  product_version)
        policy_context = get_default_retry_policy().should_retry(retry_policy_context)
        self.assertEqual(policy_context, 3)

        policy_context = NO_RETRY_POLICY.should_retry(retry_policy_context)
        self.assertEqual(policy_context, 1)

    def test_handle_response(self):
        product_code = "ecs"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        retry_policy_context = RetryPolicyContext(api_request, None, 0, 200, product_code, "2014-05-26")
        should_retry = get_default_retry_policy().should_retry(retry_policy_context)
        retry_policy_context.retryable = should_retry
        retry_backoff = get_default_retry_policy().compute_delay_before_next_retry(retry_policy_context)
        self.assertEqual(retry_backoff, 100)

        should_retry = NO_RETRY_POLICY.should_retry(retry_policy_context)
        retry_policy_context.retryable = should_retry
        retry_backoff = NO_RETRY_POLICY.compute_delay_before_next_retry(retry_policy_context)
        self.assertEqual(retry_backoff, 0)
