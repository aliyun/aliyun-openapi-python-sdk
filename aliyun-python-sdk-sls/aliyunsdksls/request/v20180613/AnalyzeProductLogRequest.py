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
from aliyunsdksls.endpoint import endpoint_data

class AnalyzeProductLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sls', '2018-06-13', 'AnalyzeProductLog')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_CloudProduct(self):
		return self.get_query_params().get('CloudProduct')

	def set_CloudProduct(self,CloudProduct):
		self.add_query_param('CloudProduct',CloudProduct)

	def get_ResourceQuota(self):
		return self.get_query_params().get('ResourceQuota')

	def set_ResourceQuota(self,ResourceQuota):
		self.add_query_param('ResourceQuota',ResourceQuota)

	def get_VariableMap(self):
		return self.get_query_params().get('VariableMap')

	def set_VariableMap(self,VariableMap):
		self.add_query_param('VariableMap',VariableMap)

	def get_TTL(self):
		return self.get_query_params().get('TTL')

	def set_TTL(self,TTL):
		self.add_query_param('TTL',TTL)

	def get_ClientIp(self):
		return self.get_query_params().get('ClientIp')

	def set_ClientIp(self,ClientIp):
		self.add_query_param('ClientIp',ClientIp)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Logstore(self):
		return self.get_query_params().get('Logstore')

	def set_Logstore(self,Logstore):
		self.add_query_param('Logstore',Logstore)

	def get_Overwrite(self):
		return self.get_query_params().get('Overwrite')

	def set_Overwrite(self,Overwrite):
		self.add_query_param('Overwrite',Overwrite)