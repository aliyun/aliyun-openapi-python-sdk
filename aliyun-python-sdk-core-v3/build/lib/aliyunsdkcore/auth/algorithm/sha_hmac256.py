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

import base64
import platform
from aliyunsdkcore.acs_exception import exceptions
from aliyunsdkcore.acs_exception import error_code



def get_sign_string(source, access_secret):
    if platform.system() != "Windows":
        from Crypto.Signature import PKCS1_v1_5
        from Crypto.Hash import SHA256
        from Crypto.PublicKey import RSA
        if isinstance(access_secret, str):
            access_secret = bytearray(access_secret, "utf-8")
        secret = base64.decodebytes(access_secret)
        key = RSA.importKey(secret)
        if isinstance(source, str):
            source = bytes(source, "utf-8")
        h = SHA256.new(source)
        signer = PKCS1_v1_5.new(key)
        signed_bytes = signer.sign(h)
        signed_base64 = base64.encodebytes(signed_bytes)
        signature = str(signed_base64, "utf-8").replace('\n', '')
        return signature
    else:
        message = "uth type [publicKeyId] is disabled in Windows because 'pycrypto' is not supported," \
                  " we will resolve this soon"
        raise exceptions.ClientException(error_code.SDK_NOT_SUPPORT, message)


def get_signer_name():
    return "SHA256withRSA"


def get_singer_version():
    return "1.0"


def get_signer_type():
    return "PRIVATEKEY"