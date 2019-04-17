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

import sys

from alibabacloud.vendored import six

if six.PY2:
    from base64 import encodestring as b64_encode_bytes
    from base64 import decodestring as b64_decode_bytes
    from urllib import urlencode


    def ensure_bytes(s, encoding='utf-8', errors='strict'):
        if isinstance(s, unicode):
            return s.encode(encoding, errors)
        if isinstance(s, str):
            return s
        raise ValueError("Expected str or unicode, received %s." % type(s))

    def ensure_string(s, encoding='utf-8', errors='strict'):
        if isinstance(s, unicode):
            return s.encode(encoding, errors)
        if isinstance(s, str):
            return s
        raise ValueError("Expected str or unicode, received %s." % type(s))

else:
    from base64 import encodebytes as b64_encode_bytes
    from base64 import decodebytes as b64_decode_bytes
    from urllib.parse import urlencode


    def ensure_bytes(s, encoding='utf-8', errors='strict'):
        if isinstance(s, str):
            return bytes(s, encoding=encoding)
        if isinstance(s, bytes):
            return s
        if isinstance(s, bytearray):
            return bytes(s)
        raise ValueError(
            "Expected str or bytes or bytearray, received %s." %
            type(s))

    def ensure_string(s, encoding='utf-8', errors='strict'):
        if isinstance(s, str):
            return s
        if isinstance(s, (bytes, bytearray)):
            return str(s, encoding='utf-8')
        raise ValueError(
            "Expected str or bytes or bytearray, received %s." %
            type(s))
