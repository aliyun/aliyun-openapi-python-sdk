# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8
import time

from aliyunsdkcore.vendored.six import iteritems
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode
from aliyunsdkcore.vendored.six.moves.urllib.request import pathname2url

from aliyunsdkcore.auth.algorithm import sha_hmac1 as mac1
from aliyunsdkcore.utils import parameter_helper as helper

FORMAT_ISO_8601 = "%Y-%m-%dT%H:%M:%SZ"


# this function will append the necessary parameters for signers process.
# parameters: the orignal parameters
# signers: sha_hmac1 or sha_hmac256
# accessKeyId: this is aliyun_access_key_id
# format: XML or JSON
def __refresh_sign_parameters(
        parameters,
        accept_format="JSON",
        signer=mac1):
    if parameters is None or not isinstance(parameters, dict):
        parameters = dict()
    if 'Signature' in parameters:
        del parameters['Signature']
    parameters["Timestamp"] = helper.get_iso_8061_date()
    parameters["SignatureMethod"] = signer.get_signer_name()
    parameters["SignatureType"] = signer.get_signer_type()
    parameters["SignatureVersion"] = signer.get_signer_version()
    parameters["SignatureNonce"] = helper.get_uuid()
    if accept_format is not None:
        parameters["Format"] = accept_format
    return parameters


def __compose_string_to_sign(method, queries):
    sorted_parameters = sorted(iteritems(queries), key=lambda queries: queries[0])
    sorted_query_string = __pop_standard_urlencode(urlencode(sorted_parameters))
    canonicalized_query_string = __pop_standard_urlencode(pathname2url(sorted_query_string))
    string_to_sign = method + "&%2F&" + canonicalized_query_string
    return string_to_sign


def __get_signature(string_to_sign, secret, signer=mac1):
    return signer.get_sign_string(string_to_sign, secret + '&')


def get_url_params(params, accept_format, signer):
    url_params = __refresh_sign_parameters(params, accept_format, signer)
    return url_params


def get_signed_signature(region_id, access_key_id, method, body_params, url_params):
    sign_params = dict(url_params)
    if 'RegionId' not in sign_params:
        sign_params['RegionId'] = region_id
    sign_params["AccessKeyId"] = access_key_id
    sign_params.update(body_params)
    string_to_sign = __compose_string_to_sign(method, sign_params)
    return string_to_sign


def get_signed_url(region_id, access_key_id, secret, url_params, string_to_sign, signer):
    sign_params = dict(url_params)
    if 'RegionId' not in sign_params:
        sign_params['RegionId'] = region_id
    sign_params["AccessKeyId"] = access_key_id
    signature = __get_signature(string_to_sign, secret, signer)
    sign_params['Signature'] = signature
    url = '?' + urlencode(sign_params)
    return url


class RPC:
    def __init__(self, credentials):
        self.credentials = credentials

    def calc_signature(self, request, params):
        string_to_sign = ''

        sorted_parameters = sorted(iteritems(params), key=lambda queries: queries[0])
        sorted_query_string = urlencode(sorted_parameters)
        canonicalized_query_string = pathname2url(sorted_query_string)
        string_to_sign = request.get_method() + "&%2F&" + canonicalized_query_string

        b64 = mac1.get_sign_string(string_to_sign, self.credentials.access_key_secret + '&')
        return b64

    def canonicalized_query_string(self, request):
        if self.credentials is None:
            pass
            # raise NoCredentialsError
        parameters = request.get_query_params()
        if parameters is None:
            parameters = {}
        parameters['Version'] = request.get_version()
        parameters['Action'] = request.get_action_name()
        parameters['Format'] = request.get_accept_format()

        parameters["Timestamp"] = time.strftime(FORMAT_ISO_8601, time.gmtime())
        parameters["SignatureMethod"] = mac1.get_signer_name()
        parameters["SignatureType"] = mac1.get_signer_type()
        parameters["SignatureVersion"] = mac1.get_signer_version()
        parameters["SignatureNonce"] = helper.get_uuid()
        if request.get_accept_format() is not None:
            parameters["Format"] = request.get_accept_format()
        if 'RegionId' not in parameters:
            parameters['RegionId'] = 'cn-hangzhou'
        parameters["AccessKeyId"] = self.credentials.access_key_id
        parameters.update(request.get_body_params())
        # if self.credentials.token:
        #     parameters['SecurityToken'] = self.credentials.token
        # 获取签名
        signature = self.calc_signature(request, parameters)
        parameters['Signature'] = signature

        return parameters
