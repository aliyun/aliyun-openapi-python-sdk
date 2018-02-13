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

import hashlib
import hmac
import base64


def get_sign_string(source, secret):
    if isinstance(source, str):
        source = bytes(source, "utf-8")
    if isinstance(source, bytearray):
        source = bytes(source)
    if isinstance(secret, bytearray):
        secret = bytes(secret)
    if isinstance(secret, str):
        secret = bytes(secret, "utf-8")
    h = hmac.new(secret, source, hashlib.sha1)
    signature = str(base64.encodebytes(h.digest()).strip(), "utf-8")
    return signature


def get_signer_name():
    return "HMAC-SHA1"


def get_singer_version():
    return "1.0"


def get_signer_type():
    return ""