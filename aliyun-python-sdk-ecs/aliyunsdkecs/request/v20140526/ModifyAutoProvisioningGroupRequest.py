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

class ModifyAutoProvisioningGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyAutoProvisioningGroup','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TerminateInstancesWithExpiration(self):
		return self.get_query_params().get('TerminateInstancesWithExpiration')

	def set_TerminateInstancesWithExpiration(self,TerminateInstancesWithExpiration):
		self.add_query_param('TerminateInstancesWithExpiration',TerminateInstancesWithExpiration)

	def get_DefaultTargetCapacityType(self):
		return self.get_query_params().get('DefaultTargetCapacityType')

	def set_DefaultTargetCapacityType(self,DefaultTargetCapacityType):
		self.add_query_param('DefaultTargetCapacityType',DefaultTargetCapacityType)

	def get_ExcessCapacityTerminationPolicy(self):
		return self.get_query_params().get('ExcessCapacityTerminationPolicy')

	def set_ExcessCapacityTerminationPolicy(self,ExcessCapacityTerminationPolicy):
		self.add_query_param('ExcessCapacityTerminationPolicy',ExcessCapacityTerminationPolicy)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_AutoProvisioningGroupId(self):
		return self.get_query_params().get('AutoProvisioningGroupId')

	def set_AutoProvisioningGroupId(self,AutoProvisioningGroupId):
		self.add_query_param('AutoProvisioningGroupId',AutoProvisioningGroupId)

	def get_PayAsYouGoTargetCapacity(self):
		return self.get_query_params().get('PayAsYouGoTargetCapacity')

	def set_PayAsYouGoTargetCapacity(self,PayAsYouGoTargetCapacity):
		self.add_query_param('PayAsYouGoTargetCapacity',PayAsYouGoTargetCapacity)

	def get_TotalTargetCapacity(self):
		return self.get_query_params().get('TotalTargetCapacity')

	def set_TotalTargetCapacity(self,TotalTargetCapacity):
		self.add_query_param('TotalTargetCapacity',TotalTargetCapacity)

	def get_SpotTargetCapacity(self):
		return self.get_query_params().get('SpotTargetCapacity')

	def set_SpotTargetCapacity(self,SpotTargetCapacity):
		self.add_query_param('SpotTargetCapacity',SpotTargetCapacity)

	def get_MaxSpotPrice(self):
		return self.get_query_params().get('MaxSpotPrice')

	def set_MaxSpotPrice(self,MaxSpotPrice):
		self.add_query_param('MaxSpotPrice',MaxSpotPrice)

	def get_AutoProvisioningGroupName(self):
		return self.get_query_params().get('AutoProvisioningGroupName')

	def set_AutoProvisioningGroupName(self,AutoProvisioningGroupName):
		self.add_query_param('AutoProvisioningGroupName',AutoProvisioningGroupName)