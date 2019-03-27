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


class AlibabaCloudCredentials:

    def __init__(self):
        self.access_key_id = None
        self.access_key_secret = None
        self.security_token = None
        self.bearer_token = None


# credentials
class AccessKeyCredentials(AlibabaCloudCredentials):

    def __init__(self, access_key_id, access_key_secret):
        AlibabaCloudCredentials.__init__(self)
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret


class BearerTokenCredentials(AlibabaCloudCredentials):

    def __init__(self, bearer_token):
        AlibabaCloudCredentials.__init__(self)
        self.bearer_token = bearer_token


class SecurityCredentials(AlibabaCloudCredentials):

    def __init__(self, access_key_id, access_key_secret, security_token):
        AlibabaCloudCredentials.__init__(self)
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.security_token = security_token
