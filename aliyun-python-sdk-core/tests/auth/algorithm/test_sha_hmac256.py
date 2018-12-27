# coding=utf-8

import unittest

from mock import MagicMock, patch
from aliyunsdkcore.auth.algorithm import sha_hmac256 as hmac256
from aliyunsdkcore.acs_exception.exceptions import ClientException


class TestShaHmac256(unittest.TestCase):
    def test_sha_hmac256(self):
        self.assertEqual(hmac256.get_signer_name(), "SHA256withRSA")
        self.assertEqual(hmac256.get_signer_type(), "PRIVATEKEY")
        self.assertEqual(hmac256.get_singer_version(), "1.0")

    @patch("platform.system")
    def test_sha_hmac256_windows(self, mock_system):
        mock_system.return_value = "Windows"
        secret = '''MIICeQIBADANBgkqhkiG9w0BAQEFAASCAmMwggJfAgEAAoGBAOJC+2WXtkXZ+6sa
3+qJp4mDOsiZb3BghHT9nVbjTeaw4hsZWHYxQ6l6XDmTg4twPB59LOGAlAjYrT31
3pdwEawnmdf6zyF93Zvxxpy7lO2HoxYKSjbtXO4I0pcq3WTnw2xlbhqHvrcuWwt+
FqH9akzcnwHjc03siZBzt/dwDL3vAgMBAAECgYEAzwgZPqFuUEYgaTVDFDl2ynYA
kNMMzBgUu3Pgx0Nf4amSitdLQYLcdbQXtTtMT4eYCxHgwkpDqkCRbLOQRKNwFo0I
oaCuhjZlxWcKil4z4Zb/zB7gkeuXPOVUjFSS3FogsRWMtnNAMgR/yJRlbcg/Puqk
Magt/yDk+7cJCe6H96ECQQDxMT4S+tVP9nOw//QT39Dk+kWe/YVEhnWnCMZmGlEq
1gnN6qpUi68ts6b3BVgrDPrPN6wm/Z9vpcKNeWpIvxXRAkEA8CcT2UEUwDGRKAUu
WVPJqdAJjpjc072eRF5g792NyO+TAF6thBlDKNslRvFQDB6ymLsjfy8JYCnGbbSb
WqbHvwJBAIs7KeI6+jiWxGJA3t06LpSABQCqyOut0u0Bm8YFGyXnOPGtrXXwzMdN
Fe0zIJp5e69zK+W2Mvt4bL7OgBROeoECQQDsE+4uLw0gFln0tosmovhmp60NcfX7
bLbtzL2MbwbXlbOztF7ssgzUWAHgKI6hK3g0LhsqBuo3jzmSVO43giZvAkEA08Nm
2TI9EvX6DfCVfPOiKZM+Pijh0xLN4Dn8qUgt3Tcew/vfj4WA2ZV6qiJqL01vMsHc
vftlY0Hs1vNXcaBgEA=='''
        with self.assertRaises(ClientException) as ex:
            result = hmac256.get_sign_string("source", secret)
        self.assertEqual(ex.exception.error_code, 'SDK.NotSupport')
        self.assertEqual(ex.exception.message,
                         "uth type [publicKeyId] is disabled in Windows "
                         "because 'pycrypto' is not supported, we will resolve this soon")
        mock_system.assert_called_once_with()
