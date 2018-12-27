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

"""
MD5 tools module.
"""

import hashlib

from aliyunsdkcore.compat import ensure_bytes
from aliyunsdkcore.compat import ensure_string
from aliyunsdkcore.compat import b64_encode_bytes


def get_md5_base64_str(content):
    m = hashlib.md5()
    content_bytes = ensure_bytes(content)
    m.update(ensure_bytes(content_bytes))
    return ensure_string(b64_encode_bytes(m.digest()).strip())
