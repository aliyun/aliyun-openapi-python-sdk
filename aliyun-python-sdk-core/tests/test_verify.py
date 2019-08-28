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
import os
import unittest
from aliyunsdkcore.http.http_response import HttpResponse


class VerifyTest(unittest.TestCase):

    def test_response_set_path(self):
        response = HttpResponse(verify=False)
        os.environ["ALIBABA_CLOUD_CA_BUNDLE"] = '/path/cacerts.pem'
        self.assertEqual(response.get_verify_value(), False)

        response = HttpResponse(verify=True)
        os.environ["ALIBABA_CLOUD_CA_BUNDLE"] = '/path/cacerts.pem'
        self.assertEqual(response.get_verify_value(), True)

        response = HttpResponse(verify=None)
        os.environ["ALIBABA_CLOUD_CA_BUNDLE"] = '/path/cacerts.pem'
        self.assertEqual(response.get_verify_value(), '/path/cacerts.pem')

        response = HttpResponse(verify='/path/cacerts1.pem')
        os.environ["ALIBABA_CLOUD_CA_BUNDLE"] = '/path/cacerts.pem'
        self.assertEqual(response.get_verify_value(), '/path/cacerts1.pem')

        os.environ.pop("ALIBABA_CLOUD_CA_BUNDLE", None)

        response = HttpResponse()
        self.assertEqual(response.get_verify_value(), True)

        os.environ["ALIBABA_CLOUD_CA_BUNDLE"] = '/path/cacerts.pem'
        response = HttpResponse()
        self.assertEqual(response.get_verify_value(), '/path/cacerts.pem')

        os.environ.pop("ALIBABA_CLOUD_CA_BUNDLE", None)


if __name__ == '__main__':
    unittest.main()

