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
from aliyunsdkarms.endpoint import endpoint_data

class CreateEnvironmentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreateEnvironment','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AliyunLang(self): # String
		return self.get_query_params().get('AliyunLang')

	def set_AliyunLang(self, AliyunLang):  # String
		self.add_query_param('AliyunLang', AliyunLang)
	def get_EnvironmentName(self): # String
		return self.get_query_params().get('EnvironmentName')

	def set_EnvironmentName(self, EnvironmentName):  # String
		self.add_query_param('EnvironmentName', EnvironmentName)
	def get_InitEnvironment(self): # Boolean
		return self.get_query_params().get('InitEnvironment')

	def set_InitEnvironment(self, InitEnvironment):  # Boolean
		self.add_query_param('InitEnvironment', InitEnvironment)
	def get_PrometheusInstanceId(self): # String
		return self.get_query_params().get('PrometheusInstanceId')

	def set_PrometheusInstanceId(self, PrometheusInstanceId):  # String
		self.add_query_param('PrometheusInstanceId', PrometheusInstanceId)
	def get_EnvironmentSubType(self): # String
		return self.get_query_params().get('EnvironmentSubType')

	def set_EnvironmentSubType(self, EnvironmentSubType):  # String
		self.add_query_param('EnvironmentSubType', EnvironmentSubType)
	def get_Tagss(self): # RepeatList
		return self.get_query_params().get('Tags')

	def set_Tagss(self, Tags):  # RepeatList
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
	def get_GrafanaWorkspaceId(self): # String
		return self.get_query_params().get('GrafanaWorkspaceId')

	def set_GrafanaWorkspaceId(self, GrafanaWorkspaceId):  # String
		self.add_query_param('GrafanaWorkspaceId', GrafanaWorkspaceId)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_EnvironmentType(self): # String
		return self.get_query_params().get('EnvironmentType')

	def set_EnvironmentType(self, EnvironmentType):  # String
		self.add_query_param('EnvironmentType', EnvironmentType)
	def get_ManagedType(self): # String
		return self.get_query_params().get('ManagedType')

	def set_ManagedType(self, ManagedType):  # String
		self.add_query_param('ManagedType', ManagedType)
	def get_BindResourceId(self): # String
		return self.get_query_params().get('BindResourceId')

	def set_BindResourceId(self, BindResourceId):  # String
		self.add_query_param('BindResourceId', BindResourceId)
	def get_FeePackage(self): # String
		return self.get_query_params().get('FeePackage')

	def set_FeePackage(self, FeePackage):  # String
		self.add_query_param('FeePackage', FeePackage)
