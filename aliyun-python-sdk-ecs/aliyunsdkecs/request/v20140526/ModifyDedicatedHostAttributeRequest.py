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
from aliyunsdkecs.endpoint import endpoint_data

class ModifyDedicatedHostAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyDedicatedHostAttribute','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_CpuOverCommitRatio(self):
		return self.get_query_params().get('CpuOverCommitRatio')

	def set_CpuOverCommitRatio(self,CpuOverCommitRatio):
		self.add_query_param('CpuOverCommitRatio',CpuOverCommitRatio)

	def get_ActionOnMaintenance(self):
		return self.get_query_params().get('ActionOnMaintenance')

	def set_ActionOnMaintenance(self,ActionOnMaintenance):
		self.add_query_param('ActionOnMaintenance',ActionOnMaintenance)

	def get_DedicatedHostClusterId(self):
		return self.get_query_params().get('DedicatedHostClusterId')

	def set_DedicatedHostClusterId(self,DedicatedHostClusterId):
		self.add_query_param('DedicatedHostClusterId',DedicatedHostClusterId)

	def get_DedicatedHostName(self):
		return self.get_query_params().get('DedicatedHostName')

	def set_DedicatedHostName(self,DedicatedHostName):
		self.add_query_param('DedicatedHostName',DedicatedHostName)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_DedicatedHostId(self):
		return self.get_query_params().get('DedicatedHostId')

	def set_DedicatedHostId(self,DedicatedHostId):
		self.add_query_param('DedicatedHostId',DedicatedHostId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_NetworkAttributesSlbUdpTimeout(self):
		return self.get_query_params().get('NetworkAttributes.SlbUdpTimeout')

	def set_NetworkAttributesSlbUdpTimeout(self,NetworkAttributesSlbUdpTimeout):
		self.add_query_param('NetworkAttributes.SlbUdpTimeout',NetworkAttributesSlbUdpTimeout)

	def get_AutoPlacement(self):
		return self.get_query_params().get('AutoPlacement')

	def set_AutoPlacement(self,AutoPlacement):
		self.add_query_param('AutoPlacement',AutoPlacement)

	def get_NetworkAttributesUdpTimeout(self):
		return self.get_query_params().get('NetworkAttributes.UdpTimeout')

	def set_NetworkAttributesUdpTimeout(self,NetworkAttributesUdpTimeout):
		self.add_query_param('NetworkAttributes.UdpTimeout',NetworkAttributesUdpTimeout)