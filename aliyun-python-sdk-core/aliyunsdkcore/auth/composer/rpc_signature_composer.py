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
from aliyunsdkcore.vendored.six import iteritems
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode
from aliyunsdkcore.vendored.six.moves.urllib.request import pathname2url

from aliyunsdkcore.auth.algorithm import sha_hmac1 as mac1
from alibabacloud.utils import parameter_helper as helper


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


def __pop_standard_urlencode(query):
    # print(22222222222222222, query)
    # ret = query.replace('+', '%20')
    # print(444444444, ret)
    # print(id(query),id(ret))
    # ret = ret.replace('*', '%2A')
    # ret = ret.replace('%7E', '~')
    # return ret
    return query


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
    url = '?' + __pop_standard_urlencode(urlencode(sign_params))
    return url
