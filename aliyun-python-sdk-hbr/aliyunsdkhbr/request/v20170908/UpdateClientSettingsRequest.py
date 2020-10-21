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
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateClientSettings','hbr')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MaxWorker(self):
		return self.get_query_params().get('MaxWorker')

	def set_MaxWorker(self,MaxWorker):
		self.add_query_param('MaxWorker',MaxWorker)

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_MaxCpuCore(self):
		return self.get_query_params().get('MaxCpuCore')

	def set_MaxCpuCore(self,MaxCpuCore):
		self.add_query_param('MaxCpuCore',MaxCpuCore)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_DataNetworkType(self):
		return self.get_query_params().get('DataNetworkType')

	def set_DataNetworkType(self,DataNetworkType):
		self.add_query_param('DataNetworkType',DataNetworkType)

	def get_UseHttps(self):
		return self.get_query_params().get('UseHttps')

	def set_UseHttps(self,UseHttps):
		self.add_query_param('UseHttps',UseHttps)