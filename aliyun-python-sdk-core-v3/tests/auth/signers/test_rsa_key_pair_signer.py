
from tests import unittest
import os
from mock import MagicMock, patch, Mock

from aliyunsdkcore.acs_exception.exceptions import ClientException, ServerException
from aliyunsdkcore.auth.credentials import RsaKeyPairCredential
from aliyunsdkcore.auth.signers.rsa_key_pair_signer import RsaKeyPairSigner, GetSessionAkRequest
from aliyunsdkcore.request import RpcRequest, RoaRequest
from aliyunsdkcore.compat import ensure_bytes


class TestRsaKeyPairSigner(unittest.TestCase):
    def test_rsa_key_pair_signer(self):
        public_key_path = os.path.join(os.path.dirname(
            __file__), "..", "..", "fixtures", "id_rsa.pub")
        public_key_id = open(public_key_path).read()
        private_key_path = os.path.join(os.path.dirname(
            __file__), "..", "..", "fixtures", "id_rsa")
        private_key_id = open(private_key_path).read()

        # invalid session period
        with self.assertRaises(ClientException) as ce:
            credential = RsaKeyPairCredential(
                public_key_id, private_key_id, session_period=12)
            RsaKeyPairSigner(credential, "region_id")
        self.assertEqual(
            "Session expiration must between 900 and 3600 seconds", ce.exception.message)
        # ok
        credential = RsaKeyPairCredential(
            public_key_id, private_key_id, session_period=3600)
        signer = RsaKeyPairSigner(credential, "region_id")
        # for rpc
        request = RpcRequest("product", "version", "action_name")
        self.assertIsNone(request.get_query_params().get("SecurityToken"))
        signer._sts_client = Mock()
        do_action = Mock()
        do_action.return_value = ensure_bytes(
            '{"SessionAccessKey":{"SessionAccessKeyId":"session_access_key_id",' +
            '"SessionAccessKeySecret":"session_access_key_secret"}}')
        signer._sts_client.do_action_with_exception = do_action
        headers, url = signer.sign('cn-hangzhou', request)
        # self.assertEqual(url, '/?SignatureVersion=1.0&Format=None"
        # "&Timestamp=2018-12-02T11%3A03%3A01Z&RegionId=cn-hangzhou"
        # "&AccessKeyId=access_key_id&SignatureMethod=HMAC-SHA1"
        # "&Version=version&Signature=AmdeJh1ZOW6PgwM3%2BROhEnbKII4%3D"
        # "&Action=action_name&SignatureNonce=d5e6e832-7f95-4f26-9e28-017f735721f8&SignatureType=')
        # second
        headers, url = signer.sign('cn-hangzhou', request)
        # mock should update
        signer._last_update_time = signer._last_update_time - signer._session_period - 10
        headers, url = signer.sign('cn-hangzhou', request)

    def test_rsa_key_pair_signer_invaid_ak(self):
        public_key_path = os.path.join(os.path.dirname(
            __file__), "..", "..", "fixtures", "id_rsa.pub")
        public_key_id = open(public_key_path).read()
        private_key_path = os.path.join(os.path.dirname(
            __file__), "..", "..", "fixtures", "id_rsa")
        private_key_id = open(private_key_path).read()

        # ok
        credential = RsaKeyPairCredential(
            public_key_id, private_key_id, session_period=3600)
        signer = RsaKeyPairSigner(credential, "region_id")
        # for rpc
        request = RpcRequest("product", "version", "action_name")
        self.assertIsNone(request.get_query_params().get("SecurityToken"))
        signer._sts_client = Mock()
        do_action = Mock()
        do_action.side_effect = ServerException(
            "InvalidAccessKeyId.NotFound", "msg")
        signer._sts_client.do_action_with_exception = do_action
        with self.assertRaises(ClientException) as ce:
            signer.sign('cn-hangzhou', request)
        self.assertEqual("SDK.InvalidCredential", ce.exception.error_code)
        self.assertEqual(
            "Need a ak&secret pair or public_key_id&private_key pair to auth.",
            ce.exception.message)

    def test_rsa_key_pair_signer_other_exception(self):
        public_key_path = os.path.join(os.path.dirname(
            __file__), "..", "..", "fixtures", "id_rsa.pub")
        public_key_id = open(public_key_path).read()
        private_key_path = os.path.join(os.path.dirname(
            __file__), "..", "..", "fixtures", "id_rsa")
        private_key_id = open(private_key_path).read()

        # ok
        credential = RsaKeyPairCredential(
            public_key_id, private_key_id, session_period=3600)
        signer = RsaKeyPairSigner(credential, "region_id")
        # for rpc
        request = RpcRequest("product", "version", "action_name")
        self.assertIsNone(request.get_query_params().get("SecurityToken"))
        signer._sts_client = Mock()
        do_action = Mock()
        do_action.side_effect = ServerException(
            "BOOM", "msg")
        signer._sts_client.do_action_with_exception = do_action
        with self.assertRaises(ServerException) as se:
            signer.sign('cn-hangzhou', request)
        self.assertEqual("BOOM", se.exception.error_code)
        self.assertEqual(
            "msg", se.exception.message)


class TestGetSessionAkRequest(unittest.TestCase):
    def test_get_session_ak_request(self):
        request = GetSessionAkRequest()
        self.assertEqual(request.get_protocol_type(), "https")
        # getter/setter for public key id
        self.assertIsNone(request.get_public_key_id())
        request.set_public_key_id("public_key_id")
        self.assertEqual(request.get_public_key_id(), "public_key_id")
        # getter/setter for duration_seconds
        self.assertIsNone(request.get_duration_seconds())
        request.set_duration_seconds("3600")
        self.assertEqual(request.get_duration_seconds(), "3600")
