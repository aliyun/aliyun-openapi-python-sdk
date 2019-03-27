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

from alibabacloud.signer.algorithm import NoHandle, ShaHmac1


class Signer(object):

    @staticmethod
    def sign(credentials, context):
        signer = ShaHmac1
        if getattr(credentials, 'bearer_token') is not None:
            signer = NoHandle

        request = context.api_request
        region_id = context.config.region_id
        # which token
        from alibabacloud.signer.composer import SIGNER_MAP
        cls = SIGNER_MAP[request.get_style()]
        auth = cls(credentials, request, region_id, signer=signer)
        signature, headers, params = auth.signature, auth.headers, auth.params
        return signature, headers, params

