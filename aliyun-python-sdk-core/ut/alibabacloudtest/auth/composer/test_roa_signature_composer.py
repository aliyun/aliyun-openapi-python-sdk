# coding=utf-8

from tests import unittest

from mock import patch
from alibabacloud.signer.composer \
    import get_url, get_signature, get_signature_headers, compose_string_to_sign, \
    build_canonical_headers, refresh_sign_parameters


class TestRoaSignatureComposer(unittest.TestCase):
    def test_get_url(self):
        self.assertEqual(get_url("/", {}, {}), "/")
        self.assertEqual(get_url("/?", {}, {}), "/")
        self.assertEqual(get_url("/", {'q': 'v'}, {}), "/?q=v")
        self.assertEqual(get_url(
            "/users/[user]", {'q': 'v'}, {'user': 'jacksontian'}), "/users/jacksontian?q=v")
        self.assertEqual(
            get_url("/users/[user]", {'q': 'v'}, None), "/users/[user]?q=v")

    def test_compose_string_to_sign(self):
        self.assertEqual(compose_string_to_sign(
            'GET', {}, "/", {}, {}), "GET\n\n\n\n\n/")
        self.assertEqual(compose_string_to_sign(
            'GET', {}, "/?q", {}, {}), "GET\n\n\n\n\n/?q")
        self.assertEqual(compose_string_to_sign(
            'GET', {}, "/", {'Accept': 'application/json'}, {}), "GET\napplication/json\n\n\n\n/")
        self.assertEqual(compose_string_to_sign('GET', {}, "/", {'Accept': 'application/json',
                                                                 'Content-MD5': 'hash'}, {}),
                         "GET\napplication/json\nhash\n\n\n/")
        self.assertEqual(compose_string_to_sign('GET', {}, "/", {'Accept': 'application/json',
                                                                 'Content-MD5': 'hash',
                                                                 'Content-Type': 'text/plain'},
                                                {}),
                         "GET\napplication/json\nhash\ntext/plain\n\n/")
        self.assertEqual(compose_string_to_sign('GET', {}, "/", {'Accept': 'application/json',
                                                                 'Content-MD5': 'hash',
                                                                 'Content-Type': 'text/plain',
                                                                 'Date': 'date str'}, {}),
                         "GET\napplication/json\nhash\ntext/plain\ndate str\n/")
        headers = {'Accept': 'application/json', 'Content-MD5': 'hash',
                   'Content-Type': 'text/plain', 'Date': 'date str'}
        queries = {'key': 'value'}
        self.assertEqual(compose_string_to_sign('GET', queries, "/", headers, {}),
                         "GET\napplication/json\nhash\ntext/plain\ndate str\n/?key=value")
        queries = {'key': 'value', 'none': None}
        self.assertEqual(compose_string_to_sign('GET', queries, "/", headers, {}),
                         "GET\napplication/json\nhash\ntext/plain\ndate str\n/?key=value&none")

    def test_build_canonical_headers(self):
        self.assertEqual(build_canonical_headers({}, 'x-acs-'), '')
        self.assertEqual(build_canonical_headers(
            {'key': 'value'}, 'x-acs-'), '')
        self.assertEqual(build_canonical_headers(
            {'key': 'value', 'x-acs-client': 'client'}, 'x-acs-'), 'x-acs-client:client\n')
        self.assertEqual(build_canonical_headers({'key': 'value', 'x-acs-client': 'client',
                                                  'x-acs-abc': 'abc-value'}, 'x-acs-'),
                         'x-acs-abc:abc-value\nx-acs-client:client\n')

    @patch("aliyunsdkcore.utils.parameter_helper.get_rfc_2616_date")
    def test_refresh_sign_parameters(self, mock_get_rfc_2616_date):
        mock_get_rfc_2616_date.return_value = "2018-12-04T03:25:29Z"
        parameters = refresh_sign_parameters({})
        mock_get_rfc_2616_date.assert_called_once_with()
        self.assertEqual(parameters.get('Date'), '2018-12-04T03:25:29Z')
        self.assertEqual(parameters.get('Accept'), 'application/octet-stream')
        self.assertEqual(parameters.get('x-acs-signature-method'), 'HMAC-SHA1')
        self.assertEqual(parameters.get('x-acs-signature-version'), '1.0')
        # with none
        parameters = refresh_sign_parameters(None)
        mock_get_rfc_2616_date.assert_called_with()
        self.assertEqual(parameters.get('Date'), '2018-12-04T03:25:29Z')
        self.assertEqual(parameters.get('Accept'), 'application/octet-stream')
        self.assertEqual(parameters.get('x-acs-signature-method'), 'HMAC-SHA1')
        self.assertEqual(parameters.get('x-acs-signature-version'), '1.0')

    @patch("aliyunsdkcore.utils.parameter_helper.get_rfc_2616_date")
    def test_get_signature(self, mock_get_rfc_2616_date):
        mock_get_rfc_2616_date.return_value = "2018-12-04T03:55:31Z"
        sign, _ = get_signature({}, 'access_key_id',
                                'access_key_secret', 'json', {}, '/', {}, 'GET')
        mock_get_rfc_2616_date.assert_called_once_with()
        self.assertEqual(sign, 'HKCpm41tJg6b3EYdtGMbNuwALZU=')

    @patch("aliyunsdkcore.utils.parameter_helper.get_rfc_2616_date")
    def test_get_signature_headers(self, mock_get_rfc_2616_date):
        mock_get_rfc_2616_date.return_value = "2018-12-04T03:55:31Z"
        headers, _ = get_signature_headers(
            {}, 'access_key_id', 'access_key_secret', 'json', {}, '/', {}, 'GET')
        mock_get_rfc_2616_date.assert_called_once_with()
        self.assertEqual(headers.get('Authorization'),
                         'acs access_key_id:HKCpm41tJg6b3EYdtGMbNuwALZU=')
