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

class AddMockRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'AddMockRule','mse')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ExtraJson(self):
		return self.get_query_params().get('ExtraJson')

	def set_ExtraJson(self,ExtraJson):
		self.add_query_param('ExtraJson',ExtraJson)

	def get_ProviderAppId(self):
		return self.get_query_params().get('ProviderAppId')

	def set_ProviderAppId(self,ProviderAppId):
		self.add_query_param('ProviderAppId',ProviderAppId)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_Enable(self):
		return self.get_query_params().get('Enable')

	def set_Enable(self,Enable):
		self.add_query_param('Enable',Enable)

	def get_ScMockItems(self):
		return self.get_query_params().get('ScMockItems')

	def set_ScMockItems(self,ScMockItems):
		self.add_query_param('ScMockItems',ScMockItems)

	def get_ProviderAppName(self):
		return self.get_query_params().get('ProviderAppName')

	def set_ProviderAppName(self,ProviderAppName):
		self.add_query_param('ProviderAppName',ProviderAppName)

	def get_ConsumerAppIds(self):
		return self.get_query_params().get('ConsumerAppIds')

	def set_ConsumerAppIds(self,ConsumerAppIds):
		self.add_query_param('ConsumerAppIds',ConsumerAppIds)

	def get_DubboMockItems(self):
		return self.get_query_params().get('DubboMockItems')

	def set_DubboMockItems(self,DubboMockItems):
		self.add_query_param('DubboMockItems',DubboMockItems)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)