# coding:utf-8

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
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


import logging
import os
from aliyunsdkcore.acs_exception import error_msg
from aliyunsdkcore.acs_exception import error_code
from aliyunsdkcore.acs_exception import exceptions
from aliyunsdkcore.auth import credentials
from . import access_key_signer
from . import sts_token_signer
from . import ram_role_arn_signer
from . import ecs_ram_role_singer
from . import rsa_key_pair_signer


class SignerFactory(object):
    @staticmethod
    def get_signer(cred, region_id, do_action_api, debug=False):
        if cred['ak'] is not None and cred['secret'] is not None:
            access_key_credential = credentials.AccessKeyCredential(cred['ak'], cred['secret'])
            return access_key_signer.AccessKeySigner(access_key_credential)
        elif os.environ.get('ALIYUN_ACCESS_KEY_ID') is not None and os.environ.get('ALIYUN_ACCESS_KEY_SECRET') is not None:
            access_key_credential = credentials.AccessKeyCredential(os.environ.get('ALIYUN_ACCESS_KEY_ID'),
                                                                    os.environ.get('ALIYUN_ACCESS_KEY_SECRET'))
            return access_key_signer.AccessKeySigner(access_key_credential)
        elif cred['credential'] is not None:
            credential = cred['credential']
            if isinstance(credential, credentials.AccessKeyCredential):
                return access_key_signer.AccessKeySigner(credential)
            elif isinstance(credential, credentials.StsTokenCredential):
                return sts_token_signer.StsTokenSigner(credential)
            elif isinstance(credential, credentials.RamRoleArnCredential):
                return ram_role_arn_signer.RamRoleArnSigner(credential, do_action_api)
            elif isinstance(credential, credentials.EcsRamRoleCredential):
                return ecs_ram_role_singer.EcsRamRoleSigner(credential)
            elif isinstance(credential, credentials.RsaKeyPairCredential):
                return rsa_key_pair_signer.RsaKeyPairSigner(credential, region_id, debug)
        elif cred['public_key_id'] is not None and cred['private_key'] is not None:
            logging.info("'AcsClient(regionId, pub_key_id, pri_key)' is deprecated")
            rsa_key_pair_credential = credentials.RsaKeyPairCredential(cred['public_key_id'], cred['private_key'],
                                                                       cred['session_period'], region_id, debug)
            return rsa_key_pair_signer.RsaKeyPairSigner(rsa_key_pair_credential)
        else:
            raise exceptions.ClientException(error_code.SDK_INVALID_CREDENTIAL,
                                             error_msg.get_msg('SDK_INVALID_CREDENTIAL'))
