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
from aliyunsdkess.endpoint import endpoint_data

class DescribeScalingInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribeScalingInstances','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_LifecycleState(self): # String
		return self.get_query_params().get('LifecycleState')

	def set_LifecycleState(self, LifecycleState):  # String
		self.add_query_param('LifecycleState', LifecycleState)
	def get_CreationType(self): # String
		return self.get_query_params().get('CreationType')

	def set_CreationType(self, CreationType):  # String
		self.add_query_param('CreationType', CreationType)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ScalingActivityId(self): # String
		return self.get_query_params().get('ScalingActivityId')

	def set_ScalingActivityId(self, ScalingActivityId):  # String
		self.add_query_param('ScalingActivityId', ScalingActivityId)
	def get_CreationTypess(self): # RepeatList
		return self.get_query_params().get('CreationTypes')

	def set_CreationTypess(self, CreationTypes):  # RepeatList
		for depth1 in range(len(CreationTypes)):
			self.add_query_param('CreationTypes.' + str(depth1 + 1), CreationTypes[depth1])
	def get_ScalingConfigurationId(self): # String
		return self.get_query_params().get('ScalingConfigurationId')

	def set_ScalingConfigurationId(self, ScalingConfigurationId):  # String
		self.add_query_param('ScalingConfigurationId', ScalingConfigurationId)
	def get_InstanceIds(self): # RepeatList
		return self.get_query_params().get('InstanceId')

	def set_InstanceIds(self, InstanceId):  # RepeatList
		for depth1 in range(len(InstanceId)):
			self.add_query_param('InstanceId.' + str(depth1 + 1), InstanceId[depth1])
	def get_HealthStatus(self): # String
		return self.get_query_params().get('HealthStatus')

	def set_HealthStatus(self, HealthStatus):  # String
		self.add_query_param('HealthStatus', HealthStatus)
	def get_LifecycleStatess(self): # RepeatList
		return self.get_query_params().get('LifecycleStates')

	def set_LifecycleStatess(self, LifecycleStates):  # RepeatList
		for depth1 in range(len(LifecycleStates)):
			self.add_query_param('LifecycleStates.' + str(depth1 + 1), LifecycleStates[depth1])
