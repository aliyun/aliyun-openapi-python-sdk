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

import jmespath
from abc import ABCMeta, abstractmethod

import aliyunsdkcore.utils
import aliyunsdkcore.utils.validation as validation
from aliyunsdkcore.acs_exception.exceptions import ClientException, ServerException
import aliyunsdkcore.acs_exception.error_code as error_code


def _find_data_in_retry_config(key_name, request, retry_config):
    if request.get_product() is None:
        return None
    path = '"{0}"."{1}"."{2}"'.format(request.get_product().lower(),
                                      request.get_version(),
                                      key_name)
    return jmespath.search(path, retry_config)


class RetryCondition(metaclass=ABCMeta):

    BLANK_STATUS = 0
    NO_RETRY = 1
    SHOULD_RETRY = 2
    SHOULD_RETRY_WITH_CLIENT_TOKEN = 4
    SHOULD_RETRY_WITH_THROTTLING_BACKOFF = 8

    @abstractmethod
    def should_retry(self, retry_policy_context):
        """Decide whether the previous request should be retried."""
        pass


class NoRetryCondition(RetryCondition):

    def should_retry(self, retry_policy_context):
        return RetryCondition.NO_RETRY


class MaxRetryTimesCondition(RetryCondition):

    def __init__(self, max_retry_times):
        validation.assert_integer_positive(max_retry_times, "max_retry_times")
        self._max_retry_times = max_retry_times

    def should_retry(self, retry_policy_context):
        if retry_policy_context.retries_attempted < self._max_retry_times:
            return RetryCondition.SHOULD_RETRY
        else:
            return RetryCondition.NO_RETRY

    @property
    def max_retry_times(self, value):
        validation.assert_integer_positive(value, "max_retry_times")
        self._max_retry_times = value


class RetryOnExceptionCondition(RetryCondition):

    def __init__(self, retry_config):
        self.retry_config = retry_config

    def should_retry(self, retry_policy_context):
        request = retry_policy_context.original_request
        exception = retry_policy_context.exception

        if isinstance(exception, ClientException):
            if exception.get_error_code() == error_code.SDK_HTTP_ERROR:
                return RetryCondition.SHOULD_RETRY

        if isinstance(exception, ServerException):
            error_code_ = exception.get_error_code()
            normal_errors = _find_data_in_retry_config("RetryableNormalErrors",
                                                       request,
                                                       self.retry_config)
            if isinstance(normal_errors, list) and error_code_ in normal_errors:
                return RetryCondition.SHOULD_RETRY

            throttling_errors = _find_data_in_retry_config("RetryableThrottlingErrors",
                                                           request,
                                                           self.retry_config)
            if isinstance(throttling_errors, list) and error_code_ in throttling_errors:
                return RetryCondition.SHOULD_RETRY | \
                       RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF

        return RetryCondition.NO_RETRY


class RetryOnAPICondition(RetryCondition):

    def __init__(self, retry_config):
        self.retry_config = retry_config

    def should_retry(self, retry_policy_context):
        retryable = self._should_retry(retry_policy_context) | \
                    self._should_retry_with_client_token(retry_policy_context)
        if retryable == RetryCondition.BLANK_STATUS:
            return RetryCondition.NO_RETRY
        else:
            return retryable

    def _should_retry(self, retry_policy_context):
        request = retry_policy_context.original_request
        retryable_apis = _find_data_in_retry_config("RetryableAPIs", request, self.retry_config)
        if isinstance(retryable_apis, list) and request.get_action_name() in retryable_apis:
            return RetryCondition.SHOULD_RETRY
        else:
            return RetryCondition.BLANK_STATUS

    def _should_retry_with_client_token(self, retry_policy_context):
        request = retry_policy_context.original_request
        retryable_apis = _find_data_in_retry_config(
            "RetryableAPIsWithClientToken", request, self.retry_config)
        if isinstance(retryable_apis, list) and request.get_action_name() in retryable_apis:
            return RetryCondition.SHOULD_RETRY | RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF
        else:
            return RetryCondition.BLANK_STATUS


class ChainedRetryCondition(RetryCondition):

    def __init__(self, retry_condition_chain):
        self._retry_condition_chain = retry_condition_chain

    def should_retry(self, retry_policy_context):
        retryable = RetryCondition.BLANK_STATUS
        for condition in self._retry_condition_chain:
            retryable |= condition.should_retry(retry_policy_context)
        return retryable


class MixedRetryCondition(RetryCondition):

    def __init__(self, max_retry_times, retry_config):
        RetryCondition.__init__(self)
        self._chained_retry_condition = ChainedRetryCondition([
            MaxRetryTimesCondition(max_retry_times),
            RetryOnAPICondition(retry_config),
            RetryOnExceptionCondition(retry_config),
        ])

    def should_retry(self, retry_policy_context):
        return self._chained_retry_condition.should_retry(retry_policy_context)


class DefaultConfigRetryCondition(MixedRetryCondition):

    DEFAULT_MAX_RETRY_TIMES = 3
    RETRY_CONFIG_FILE = "retry_config.json"
    _loaded_retry_config = None

    def __init__(self, max_retry_times=None):
        if not self._loaded_retry_config:
            self._loaded_retry_config = aliyunsdkcore.utils._load_json_from_data_dir(
                self.RETRY_CONFIG_FILE)

        if max_retry_times is None:
            max_retry_times = self.DEFAULT_MAX_RETRY_TIMES
        MixedRetryCondition.__init__(self, max_retry_times, self._loaded_retry_config)
