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

from aliyunsdkcore.request import RoaRequest


class TestRoaApiRequest(RoaRequest):
    def __init__(self):
        RoaRequest.__init__(self, 'Ft', '2016-01-02', 'TestRoaApi')
        self.set_uri_pattern('/web/cloudapi')
        self.set_method('POST')

    def get_body_param(self):
        return self.get_body_params().get('BodyParam')

    def set_body_param(self, body_param):
        self.add_body_params('BodyParam', body_param)

    def get_query_param(self):
        return self.get_query_params().get('QueryParam')

    def set_query_param(self, query_param):
        self.add_query_param('QueryParam', query_param)

    def get_header_param(self):
        return self.get_headers().get('HeaderParam')

    def set_header_param(self, header_param):
        self.add_header('HeaderParam', header_param)
