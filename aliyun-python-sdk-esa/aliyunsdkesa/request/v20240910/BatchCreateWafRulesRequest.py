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

class BatchCreateWafRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'BatchCreateWafRules')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Phase(self): # String
		return self.get_body_params().get('Phase')

	def set_Phase(self, Phase):  # String
		self.add_body_params('Phase', Phase)
	def get_Configs(self): # Array
		return self.get_body_params().get('Configs')

	def set_Configs(self, Configs):  # Array
		self.add_body_params("Configs", json.dumps(Configs))
	def get_Shared(self): # Struct
		return self.get_body_params().get('Shared')

	def set_Shared(self, Shared):  # Struct
		self.add_body_params("Shared", json.dumps(Shared))
	def get_SiteVersion(self): # Integer
		return self.get_query_params().get('SiteVersion')

	def set_SiteVersion(self, SiteVersion):  # Integer
		self.add_query_param('SiteVersion', SiteVersion)
	def get_SiteId(self): # Long
		return self.get_query_params().get('SiteId')

	def set_SiteId(self, SiteId):  # Long
		self.add_query_param('SiteId', SiteId)
