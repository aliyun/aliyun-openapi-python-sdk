# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest

class GwListGatewayRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'LRG', '2019-10-10', 'GwListGateway')
		self.set_uri_pattern('/api/v2/gw/xgw/gw-server?action=list')
		self.set_method('POST')

	def get_big_region_name(self):
		return self.get_body_params().get('big_region_name')

	def set_big_region_name(self,big_region_name):
		self.add_body_params('big_region_name', big_region_name)

	def get_Status(self):
		return self.get_body_params().get('Status')

	def set_Status(self,Status):
		self.add_body_params('Status', Status)