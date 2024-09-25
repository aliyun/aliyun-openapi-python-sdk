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

from aliyunsdkcore.request import RpcRequest
import json

class UpdateWafRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'UpdateWafRule')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_SiteVersion(self): # Integer
		return self.get_query_params().get('SiteVersion')

	def set_SiteVersion(self, SiteVersion):  # Integer
		self.add_query_param('SiteVersion', SiteVersion)
	def get_SiteId(self): # Long
		return self.get_query_params().get('SiteId')

	def set_SiteId(self, SiteId):  # Long
		self.add_query_param('SiteId', SiteId)
	def get_Id(self): # Long
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_body_params('Id', Id)
	def get_Position(self): # Long
		return self.get_body_params().get('Position')

	def set_Position(self, Position):  # Long
		self.add_body_params('Position', Position)
	def get_Config(self): # Struct
		return self.get_body_params().get('Config')

	def set_Config(self, Config):  # Struct
		self.add_body_params("Config", json.dumps(Config))
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
