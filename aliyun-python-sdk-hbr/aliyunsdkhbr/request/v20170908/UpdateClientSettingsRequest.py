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
from aliyunsdkhbr.endpoint import endpoint_data

class UpdateClientSettingsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateClientSettings')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DataProxySetting(self): # String
		return self.get_query_params().get('DataProxySetting')

	def set_DataProxySetting(self, DataProxySetting):  # String
		self.add_query_param('DataProxySetting', DataProxySetting)
	def get_ProxyPort(self): # Integer
		return self.get_query_params().get('ProxyPort')

	def set_ProxyPort(self, ProxyPort):  # Integer
		self.add_query_param('ProxyPort', ProxyPort)
	def get_ClientId(self): # String
		return self.get_query_params().get('ClientId')

	def set_ClientId(self, ClientId):  # String
		self.add_query_param('ClientId', ClientId)
	def get_VaultId(self): # String
		return self.get_query_params().get('VaultId')

	def set_VaultId(self, VaultId):  # String
		self.add_query_param('VaultId', VaultId)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ProxyUser(self): # String
		return self.get_query_params().get('ProxyUser')

	def set_ProxyUser(self, ProxyUser):  # String
		self.add_query_param('ProxyUser', ProxyUser)
	def get_UseHttps(self): # Boolean
		return self.get_query_params().get('UseHttps')

	def set_UseHttps(self, UseHttps):  # Boolean
		self.add_query_param('UseHttps', UseHttps)
	def get_MaxWorker(self): # Integer
		return self.get_query_params().get('MaxWorker')

	def set_MaxWorker(self, MaxWorker):  # Integer
		self.add_query_param('MaxWorker', MaxWorker)
	def get_MaxCpuCore(self): # Integer
		return self.get_query_params().get('MaxCpuCore')

	def set_MaxCpuCore(self, MaxCpuCore):  # Integer
		self.add_query_param('MaxCpuCore', MaxCpuCore)
	def get_DataNetworkType(self): # String
		return self.get_query_params().get('DataNetworkType')

	def set_DataNetworkType(self, DataNetworkType):  # String
		self.add_query_param('DataNetworkType', DataNetworkType)
	def get_ProxyPassword(self): # String
		return self.get_query_params().get('ProxyPassword')

	def set_ProxyPassword(self, ProxyPassword):  # String
		self.add_query_param('ProxyPassword', ProxyPassword)
	def get_ProxyHost(self): # String
		return self.get_query_params().get('ProxyHost')

	def set_ProxyHost(self, ProxyHost):  # String
		self.add_query_param('ProxyHost', ProxyHost)
