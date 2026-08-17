# Copyright 2026 Alibaba Cloud Inc. All rights reserved.
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
import re
import unittest
import warnings

from aliyunsdkcore.vendored.requests.packages import certifi
from aliyunsdkcore.vendored.requests.packages.certifi import core as certifi_core
from aliyunsdkcore.vendored.requests import certs


class CertifiTest(unittest.TestCase):

    def test_version_fixes_cve_2023_37920(self):
        # CVE-2023-37920 is fixed in certifi >= 2023.07.22
        match = re.match(r'^(\d{4})\.(\d{2})\.(\d{2})$', certifi.__version__)
        self.assertIsNotNone(match, 'unexpected certifi version: %s' % certifi.__version__)
        year, month, day = (int(g) for g in match.groups())
        self.assertGreaterEqual((year, month, day), (2023, 7, 22))

    def test_cacert_pem_exists_via_where(self):
        path = certifi.where()
        self.assertTrue(os.path.isfile(path))
        self.assertEqual(os.path.basename(path), 'cacert.pem')
        self.assertGreater(os.path.getsize(path), 0)

    def test_requests_certs_uses_vendored_certifi(self):
        self.assertEqual(certs.where(), certifi.where())

    def test_cacert_pem_excludes_e_tugra_roots(self):
        with open(certifi.where(), 'r') as f:
            content = f.read()
        self.assertNotIn('E-Tugra', content)
        self.assertNotIn('e-Tugra', content)

    def test_old_where_aliases_where(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            path = certifi_core.old_where()
        self.assertEqual(path, certifi.where())
        self.assertTrue(any(issubclass(w.category, certifi_core.DeprecatedBundleWarning)
                            for w in caught))


if __name__ == '__main__':
    unittest.main()
