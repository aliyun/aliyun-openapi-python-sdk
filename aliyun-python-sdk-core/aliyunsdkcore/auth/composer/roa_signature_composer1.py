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
import hmac

from aliyunsdkcore.vendored.six import iteritems
from aliyunsdkcore.vendored.six.moves.urllib.parse import urlencode
from aliyunsdkcore.auth.algorithm import sha_hmac1 as mac1
from aliyunsdkcore.utils import parameter_helper as helper
from aliyunsdkcore.http import format_type as FormatType


CONTENT_MD5 = "Content-MD5"
CONTENT_TYPE = "Content-Type"
DATE = "Date"
ACCEPT = "Accept"
QUERY_SEPARATOR = "&"
HEADER_SEPARATOR = "\n"


# this function will append the necessary parameters for signers process.
# parameters: the orignal parameters
# signers: sha_hmac1 or sha_hmac256
# accessKeyId: this is aliyun_access_key_id
# format: XML or JSON
# input parameters is headers
def refresh_sign_parameters(parameters, format=FormatType.RAW, signer=mac1):
    if parameters is None or not isinstance(parameters, dict):
        parameters = dict()
    parameters["Date"] = helper.get_rfc_2616_date()
    parameters["Accept"] = FormatType.map_format_to_accept(format)
    parameters["x-acs-signature-method"] = signer.get_signer_name()
    parameters["x-acs-signature-version"] = signer.get_signer_version()
    return parameters


def compose_string_to_sign(
        method,
        queries,
        uri_pattern=None,
        headers={},
        paths=None,
        signer=mac1):
    sign_to_string = ""
    sign_to_string += method
    sign_to_string += HEADER_SEPARATOR
    if ACCEPT in headers and headers[ACCEPT] is not None:
        sign_to_string += headers[ACCEPT]
    sign_to_string += HEADER_SEPARATOR
    if CONTENT_MD5 in headers and headers[CONTENT_MD5] is not None:
        sign_to_string += headers[CONTENT_MD5]
    sign_to_string += HEADER_SEPARATOR
    if CONTENT_TYPE in headers and headers[CONTENT_TYPE] is not None:
        sign_to_string += headers[CONTENT_TYPE]
    sign_to_string += HEADER_SEPARATOR
    if DATE in headers and headers[DATE] is not None:
        sign_to_string += headers[DATE]
    sign_to_string += HEADER_SEPARATOR
    sign_to_string += build_canonical_headers(headers, "x-acs-")

    uri = replace_occupied_parameters(uri_pattern, paths)
    sign_to_string += __build_query_string(uri, queries)

    return sign_to_string


def replace_occupied_parameters(uri_pattern, paths):
    result = uri_pattern
    if paths is not None:
        for (key, value) in iteritems(paths):
            target = "[" + key + "]"
            result = result.replace(target, value)
    return result

# change the give headerBegin to the lower() which in the headers
# and change it to key.lower():value


def build_canonical_headers(headers, header_begin):
    result = ""
    unsort_map = dict()
    for (key, value) in iteritems(headers):
        if key.lower().find(header_begin) >= 0:
            unsort_map[key.lower()] = value
    sort_map = sorted(iteritems(unsort_map), key=lambda d: d[0])
    for (key, value) in sort_map:
        result += key + ":" + value
        result += HEADER_SEPARATOR
    return result


def __build_query_string(uri, queries):
    uri_parts = uri.split("?")
    if len(uri_parts) > 1 and uri_parts[1] is not None:
        queries[uri_parts[1]] = None
    query_builder = uri_parts[0]
    sorted_map = sorted(iteritems(queries), key=lambda queries: queries[0])
    if len(sorted_map) > 0:
        query_builder += "?"
    for (k, v) in sorted_map:
        query_builder += k
        if v is not None:
            query_builder += "="
            query_builder += str(v)
        query_builder += '&'
    if query_builder.endswith('&'):
        query_builder = query_builder[0:(len(query_builder) - 1)]
    return query_builder


def get_signed_signature(queries, format, headers, uri_pattern, paths, method):
    headers = refresh_sign_parameters(
        parameters=headers,
        format=format)
    sign_to_string = compose_string_to_sign(
        method=method,
        queries=queries,
        headers=headers,
        uri_pattern=uri_pattern,
        paths=paths)

    return sign_to_string


def get_signed_headers(access_key, secret, headers, sign_to_string=None, signer=mac1):
    signature = signer.get_sign_string(sign_to_string, secret=secret)
    headers["Authorization"] = "acs " + str(access_key) + ":" + str(signature)
    return headers


def get_signed_url(uri_pattern, queries, path_parameters):
    url = ""
    # self.set_uri_pattern('/repos/[RepoNamespace]/[RepoName]/build')
    url += replace_occupied_parameters(uri_pattern, path_parameters)
    if not url.endswith("?"):
        url += "?"
    url += urlencode(queries)
    if url.endswith("?"):
        url = url[0:(len(url) - 1)]
    return url

class ROA:

    def __init__(self, credentials):
        self.credentials = credentials

    def sign_string(self, string_to_sign):
        from hashlib import sha1
        from aliyunsdkcore.compat import b64_encode_bytes

        new_hmac = hmac.new(self.credentials.secret_key.encode('utf-8'),
                            digestmod=sha1)
        new_hmac.update(string_to_sign.encode('utf-8'))

        return b64_encode_bytes(new_hmac.digest()).strip().decode('utf-8')

    def canonical_standard_headers(self, headers):
        interesting_headers = ['Content-MD5', 'Content-Type', 'Date', 'Accept']

        hoi = []
        for ih in interesting_headers:
            found = False
            for key in headers:
                lk = key.lower()
                if headers[key] is not None and lk == ih:
                    hoi.append(headers[key].strip())
                    found = True
            if not found:
                hoi.append('')
        return '\n'.join(hoi)

    def canonical_custom_headers(self, headers):
        hoi = []
        custom_headers = {}
        for key in headers:
            lk = key.lower()
            if headers[key] is not None:
                if lk.startswith('x-acs-'):
                    custom_headers[lk] = headers[key]
        sorted_header_keys = sorted(custom_headers.keys())
        for key in sorted_header_keys:
            hoi.append("%s:%s" % (key, custom_headers[key]))

        return '\n'.join(hoi)

    def canonical_resource(self, uri, req_params):
        uri_parts = uri.split("?")
        if len(uri_parts) > 1 and uri_parts[1] is not None:
            req_params[uri_parts[1]] = None
        query_builder = uri_parts[0]
        sorted_map = sorted(iteritems(req_params), key=lambda queries: queries[0])
        if len(sorted_map) > 0:
            query_builder += "?"
        for (k, v) in sorted_map:
            query_builder += k
            if v is not None:
                query_builder += "="
                query_builder += str(v)
                query_builder += '&'
        if query_builder.endswith('&'):
            query_builder = query_builder[0:(len(query_builder) - 1)]

        return query_builder

    def canonical_string(self, request, req_params, headers):
        method = request.get_method()

        cs = method.upper() + '\n'
        cs += self.canonical_standard_headers(headers) + '\n'

        custom_headers = self.canonical_custom_headers(headers)

        if custom_headers:
            cs += custom_headers + '\n'

        uri = replace_occupied_parameters(request.get_uri_pattern(), request.get_path_params())

        cs += self.canonical_resource(uri, req_params)
        return cs

    def get_signature(self, req_params, request):
        headers = request.get_headers()
        if self.credentials.token:
            del headers['x-amz-security-token']
            headers['x-amz-security-token'] = self.credentials.token
        headers["Date"] = helper.get_rfc_2616_date()
        headers["Accept"] = FormatType.map_format_to_accept(format)
        headers["x-acs-signature-method"] = mac1.get_signer_name()
        headers["x-acs-signature-version"] = mac1.get_signer_version()
        string_to_sign = self.canonical_string(request, req_params, headers)

        return self.sign_string(string_to_sign)


    def _inject_signature(self, headers, signature):
        if 'Authorization' in headers:
            # We have to do this because request.headers is not
            # normal dictionary.  It has the (unintuitive) behavior
            # of aggregating repeated setattr calls for the same
            # key value.  For example:
            # headers['foo'] = 'a'; headers['foo'] = 'b'
            # list(headers) will print ['foo', 'foo'].
            del headers['Authorization']
        headers["Authorization"] = "acs %s:%s" % (self.credentials.access_key, signature)


    def add_auth(self, request):
        if self.credentials is None:
            print('NoCredentialsError')
            # raise NoCredentialsError
        from aliyunsdkcore.utils.parameter_helper import md5_sum

        req_params = request.get_query_params()
        request.add_header("x-acs-version", request.get_version())
        if request.get_content() is not None:
            request.add_header(
                'Content-MD5', md5_sum(request.get_content()))
        # if 'RegionId' not in req_params.keys():
        #     req_params['RegionId'] = region_id
        #     request.add_header('x-acs-region-id', str(region_id))

        signature = self.get_signature(req_params, request)
        self._inject_signature(headers, signature)
