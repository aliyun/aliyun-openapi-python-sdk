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
from aliyunsdkvs.endpoint import endpoint_data

class ModifyGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vs', '2018-12-12', 'ModifyGroup','vs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Enabled(self):
		return self.get_query_params().get('Enabled')

	def set_Enabled(self,Enabled):
		self.add_query_param('Enabled',Enabled)

	def get_PushDomain(self):
		return self.get_query_params().get('PushDomain')

	def set_PushDomain(self,PushDomain):
		self.add_query_param('PushDomain',PushDomain)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_PlayDomain(self):
		return self.get_query_params().get('PlayDomain')

	def set_PlayDomain(self,PlayDomain):
		self.add_query_param('PlayDomain',PlayDomain)

	def get_OutProtocol(self):
		return self.get_query_params().get('OutProtocol')

	def set_OutProtocol(self,OutProtocol):
		self.add_query_param('OutProtocol',OutProtocol)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InProtocol(self):
		return self.get_query_params().get('InProtocol')

	def set_InProtocol(self,InProtocol):
		self.add_query_param('InProtocol',InProtocol)

	def get_LazyPull(self):
		return self.get_query_params().get('LazyPull')

	def set_LazyPull(self,LazyPull):
		self.add_query_param('LazyPull',LazyPull)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Callback(self):
		return self.get_query_params().get('Callback')

	def set_Callback(self,Callback):
		self.add_query_param('Callback',Callback)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)