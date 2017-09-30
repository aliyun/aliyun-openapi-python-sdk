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

import urllib.parse
import urllib.request
import urllib.response

from aliyunsdkcore.auth.algorithm import sha_hmac1 as mac1
from aliyunsdkcore.utils import parameter_helper as helper


def __init__():
    pass


# this function will append the necessary parameters for signer process.
# parameters: the orignal parameters
# signer: sha_hmac1 or sha_hmac256
# accessKeyId: this is aliyun_access_key_id
# format: XML or JSON
def __refresh_sign_parameters(
        parameters,
        access_key_id,
        accept_format="JSON",
        signer=mac1):
    if parameters is None or not isinstance(parameters, dict):
        parameters = dict()
    parameters["Timestamp"] = helper.get_iso_8061_date()
    parameters["SignatureMethod"] = signer.get_signer_name()
    parameters["SignatureType"] = signer.get_signer_type()
    parameters["SignatureVersion"] = signer.get_singer_version()
    parameters["SignatureNonce"] = helper.get_uuid()
    parameters["AccessKeyId"] = access_key_id
    if accept_format is not None:
        parameters["Format"] = accept_format
    return parameters


def __pop_standard_urlencode(query):
    ret = urllib.parse.urlencode(query)
    ret = ret.replace('+', '%20')
    ret = ret.replace('*', '%2A')
    ret = ret.replace('%7E', '~')
    return ret


def __compose_string_to_sign(method, queries):
    sorted_parameters = sorted(list(queries.items()), key=lambda queries: queries[0])
    string_to_sign = method + "&%2F&" + \
        urllib.request.pathname2url(__pop_standard_urlencode(sorted_parameters))
    return string_to_sign


def __get_signature(string_to_sign, secret, signer=mac1):
    return signer.get_sign_string(string_to_sign, secret + '&')


def get_signed_url(params, ak, secret, accept_format, method, body_params, signer=mac1):
    url_params = __refresh_sign_parameters(params, ak, accept_format, signer)
    sign_params = dict(url_params)
    sign_params.update(body_params)
    string_to_sign = __compose_string_to_sign(method, sign_params)
    signature = __get_signature(string_to_sign, secret, signer)
    url_params['Signature'] = signature
    url = '/?' + __pop_standard_urlencode(url_params)
    return url
