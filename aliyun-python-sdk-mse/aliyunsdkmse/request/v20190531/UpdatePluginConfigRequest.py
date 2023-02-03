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
from aliyunsdkmse.endpoint import endpoint_data

class UpdatePluginConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'UpdatePluginConfig','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_GatewayUniqueId(self): # String
		return self.get_query_params().get('GatewayUniqueId')

	def set_GatewayUniqueId(self, GatewayUniqueId):  # String
		self.add_query_param('GatewayUniqueId', GatewayUniqueId)
	def get_GmtModified(self): # String
		return self.get_query_params().get('GmtModified')

	def set_GmtModified(self, GmtModified):  # String
		self.add_query_param('GmtModified', GmtModified)
	def get_Enable(self): # Boolean
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # Boolean
		self.add_query_param('Enable', Enable)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_GatewayId(self): # Long
		return self.get_query_params().get('GatewayId')

	def set_GatewayId(self, GatewayId):  # Long
		self.add_query_param('GatewayId', GatewayId)
	def get_PluginId(self): # Long
		return self.get_query_params().get('PluginId')

	def set_PluginId(self, PluginId):  # Long
		self.add_query_param('PluginId', PluginId)
	def get_GmtCreate(self): # String
		return self.get_query_params().get('GmtCreate')

	def set_GmtCreate(self, GmtCreate):  # String
		self.add_query_param('GmtCreate', GmtCreate)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_ConfigLevel(self): # Integer
		return self.get_query_params().get('ConfigLevel')

	def set_ConfigLevel(self, ConfigLevel):  # Integer
		self.add_query_param('ConfigLevel', ConfigLevel)
	def get_Config(self): # String
		return self.get_query_params().get('Config')

	def set_Config(self, Config):  # String
		self.add_query_param('Config', Config)
