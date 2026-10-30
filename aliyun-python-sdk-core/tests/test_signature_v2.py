# coding=utf-8
import base64
import hashlib
import hmac
import itertools
import json
import os
from urllib.parse import parse_qsl, quote, urlsplit

from mock import patch
from tests import unittest

from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.auth.algorithm import hmac_sha256, sha_hmac1
from aliyunsdkcore.auth.credentials import AccessKeyCredential, RamRoleArnCredential, StsTokenCredential
from aliyunsdkcore.auth.signers.rsa_key_pair_signer import GetSessionAkRequest
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest, RoaRequest, RpcRequest


class TestSignatureV2(unittest.TestCase):
    def setUp(self):
        environment = patch.dict(os.environ, {}, clear=True)
        environment.start()
        self.addCleanup(environment.stop)

    @staticmethod
    def request(style, method):
        if style.startswith('common'):
            request = CommonRequest(product='Ecs', version='2014-05-26', action_name='DescribeRegions')
            if style == 'common_roa':
                request.set_uri_pattern('/regions/[region_id]/clusters')
                request.add_path_param('region_id', 'cn-hangzhou')
        elif style == 'rpc':
            request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions')
        else:
            request = RoaRequest('CS', '2015-12-15', 'DescribeClustersForRegion',
                                 uri_pattern='/regions/[region_id]/clusters',
                                 path_params={'region_id': 'cn-hangzhou'})
        request.set_accept_format('JSON')
        request.set_method(method)
        request.add_query_param('Value', 'Unicode-中文 +/~*')
        if method == 'POST':
            request.add_body_params('BodyValue', 'body +/~*')
        return request

    @staticmethod
    def rpc_string(message):
        parameters = dict(parse_qsl(urlsplit(message.get_url()).query, keep_blank_values=True))
        parameters.pop('Signature')
        parameters.update(parse_qsl(message.get_content() or '', keep_blank_values=True))
        canonical = '&'.join(quote(key, safe='~') + '=' + quote(value, safe='~')
                             for key, value in sorted(parameters.items()))
        return message.get_method() + '&%2F&' + quote(canonical, safe='~')

    def assert_signature(self, message, style, method, secret, token=None):
        algorithm = hashlib.sha1 if method == 'HMAC-SHA1' else hashlib.sha256
        if style.endswith('rpc'):
            parameters = dict(parse_qsl(urlsplit(message.get_url()).query, keep_blank_values=True))
            self.assertEqual(method, parameters['SignatureMethod'])
            self.assertEqual('1.0', parameters['SignatureVersion'])
            self.assertEqual(token, parameters.get('SecurityToken'))
            signature = parameters['Signature']
            canonical = self.rpc_string(message)
            secret += '&'
        else:
            headers = message.get_headers()
            self.assertEqual(method, headers['x-acs-signature-method'])
            self.assertEqual('1.0', headers['x-acs-signature-version'])
            self.assertEqual(token, headers.get('x-acs-security-token'))
            signature = headers['Authorization'].split(':', 1)[1]
            canonical = message.get_method() + '\n'
            for name in ('Accept', 'Content-MD5', 'Content-Type', 'Date'):
                canonical += headers.get(name, '') + '\n'
            canonical += ''.join(name.lower() + ':' + value + '\n'
                                 for name, value in sorted(headers.items(), key=lambda item: item[0].lower())
                                 if name.lower().startswith('x-acs-'))
            uri = urlsplit(message.get_url())
            canonical += uri.path
            parameters = sorted(parse_qsl(uri.query, keep_blank_values=True))
            if parameters:
                canonical += '?' + '&'.join(key + '=' + value for key, value in parameters)
        expected = base64.b64encode(hmac.new(secret.encode('utf-8'), canonical.encode('utf-8'),
                                             algorithm).digest()).decode('ascii')
        self.assertEqual(expected, signature)

    def test_client_algorithms(self):
        cases = itertools.product(('rpc', 'roa', 'common_rpc', 'common_roa'),
                                  ('GET', 'POST'), (False, True), (None, 'HMAC-SHA1', 'HMAC-SHA256'))
        for style, http_method, sts, method in cases:
            with self.subTest(style=style, http_method=http_method, sts=sts, method=method):
                credential = (StsTokenCredential('key', 'secret', 'token+/=')
                              if sts else AccessKeyCredential('key', 'secret'))
                options = {} if method is None else {'signature_method': method}
                client = AcsClient(credential=credential, **options)
                request = self.request(style, http_method)
                message = client._make_http_response('example.test', request, 10, 10)
                self.assert_signature(message, style, method or 'HMAC-SHA256', 'secret', 'token+/=' if sts else None)
                client.session.close()

    def test_explicit_request_signer_overrides_client_default(self):
        client = AcsClient('key', 'secret')
        request = RpcRequest('Ecs', '2014-05-26', 'DescribeRegions', signer=sha_hmac1)
        message = client._make_http_response('example.test', request, 10, 10)
        self.assert_signature(message, 'rpc', 'HMAC-SHA1', 'secret')
        client.session.close()

    def test_request_can_be_reused_with_different_client_defaults(self):
        for style in ('rpc', 'roa', 'common_rpc', 'common_roa'):
            request = self.request(style, 'GET')
            for method in ('HMAC-SHA1', 'HMAC-SHA256'):
                with self.subTest(style=style, method=method):
                    client = AcsClient('key', 'secret', signature_method=method)
                    message = client._make_http_response('example.test', request, 10, 10)
                    self.assert_signature(message, style, method, 'secret')
                    client.session.close()

    def test_assume_role_inherits_client_algorithm(self):
        for method in ('HMAC-SHA256', 'HMAC-SHA1'):
            with self.subTest(method=method):
                credential = RamRoleArnCredential('source-key', 'source-secret', 'role-arn', 'session')
                client = AcsClient(credential=credential, signature_method=method)
                exchange = []

                def assume_role(request, signer):
                    exchange.append(client._make_http_response('example.test', request, 10, 10, signer))
                    return 200, {}, json.dumps({'Credentials': {
                        'AccessKeyId': 'temporary-key', 'AccessKeySecret': 'temporary-secret',
                        'SecurityToken': 'temporary-token'
                    }}).encode('utf-8'), None

                client._signer._doAction = assume_role
                message = client._make_http_response('example.test', self.request('rpc', 'GET'), 10, 10)
                self.assertEqual(1, len(exchange))
                self.assert_signature(exchange[0], 'rpc', method, 'source-secret')
                self.assert_signature(message, 'rpc', method, 'temporary-secret', 'temporary-token')
                client.session.close()

    @patch('aliyunsdkcore.auth.algorithm.sha_hmac256.get_sign_string', return_value='rsa-signature')
    def test_rsa_exchange_keeps_explicit_algorithm(self, sign):
        client = AcsClient('public-key-id', 'private-key', signature_method='HMAC-SHA1')
        message = client._make_http_response('example.test', GetSessionAkRequest(), 10, 10)
        parameters = dict(parse_qsl(urlsplit(message.get_url()).query))
        self.assertEqual('SHA256withRSA', parameters['SignatureMethod'])
        self.assertEqual('PRIVATEKEY', parameters['SignatureType'])
        self.assertEqual('rsa-signature', parameters['Signature'])
        sign.assert_called_once()
        client.session.close()

    def test_invalid_client_algorithm(self):
        for method in ('sha1', '', None, []):
            with self.subTest(method=method):
                with self.assertRaises(ClientException) as error:
                    AcsClient('key', 'secret', signature_method=method)
                self.assertEqual('SDK.InvalidParams', error.exception.error_code)

    def test_hmac_sha256_vectors(self):
        self.assertEqual('HMAC-SHA256', hmac_sha256.get_signer_name())
        self.assertEqual('1.0', hmac_sha256.get_signer_version())
        self.assertEqual('', hmac_sha256.get_signer_type())
        for source in ('source', '中文unicode'):
            expected = base64.b64encode(hmac.new(b'secret', source.encode('utf-8'), hashlib.sha256).digest())
            self.assertEqual(expected.decode('ascii'), hmac_sha256.get_sign_string(source, 'secret'))
