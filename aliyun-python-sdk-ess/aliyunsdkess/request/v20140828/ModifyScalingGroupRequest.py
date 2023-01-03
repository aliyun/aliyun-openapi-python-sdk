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

class ModifyScalingGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'ModifyScalingGroup','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_AzBalance(self): # Boolean
		return self.get_query_params().get('AzBalance')

	def set_AzBalance(self, AzBalance):  # Boolean
		self.add_query_param('AzBalance', AzBalance)
	def get_VSwitchIdss(self): # RepeatList
		return self.get_query_params().get('VSwitchIds')

	def set_VSwitchIdss(self, VSwitchIds):  # RepeatList
		for depth1 in range(len(VSwitchIds)):
			self.add_query_param('VSwitchIds.' + str(depth1 + 1), VSwitchIds[depth1])
	def get_MaxInstanceLifetime(self): # Integer
		return self.get_query_params().get('MaxInstanceLifetime')

	def set_MaxInstanceLifetime(self, MaxInstanceLifetime):  # Integer
		self.add_query_param('MaxInstanceLifetime', MaxInstanceLifetime)
	def get_ActiveScalingConfigurationId(self): # String
		return self.get_query_params().get('ActiveScalingConfigurationId')

	def set_ActiveScalingConfigurationId(self, ActiveScalingConfigurationId):  # String
		self.add_query_param('ActiveScalingConfigurationId', ActiveScalingConfigurationId)
	def get_SpotInstanceRemedy(self): # Boolean
		return self.get_query_params().get('SpotInstanceRemedy')

	def set_SpotInstanceRemedy(self, SpotInstanceRemedy):  # Boolean
		self.add_query_param('SpotInstanceRemedy', SpotInstanceRemedy)
	def get_CustomPolicyARN(self): # String
		return self.get_query_params().get('CustomPolicyARN')

	def set_CustomPolicyARN(self, CustomPolicyARN):  # String
		self.add_query_param('CustomPolicyARN', CustomPolicyARN)
	def get_DefaultCooldown(self): # Integer
		return self.get_query_params().get('DefaultCooldown')

	def set_DefaultCooldown(self, DefaultCooldown):  # Integer
		self.add_query_param('DefaultCooldown', DefaultCooldown)
	def get_MultiAZPolicy(self): # String
		return self.get_query_params().get('MultiAZPolicy')

	def set_MultiAZPolicy(self, MultiAZPolicy):  # String
		self.add_query_param('MultiAZPolicy', MultiAZPolicy)
	def get_LaunchTemplateId(self): # String
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self, LaunchTemplateId):  # String
		self.add_query_param('LaunchTemplateId', LaunchTemplateId)
	def get_DesiredCapacity(self): # Integer
		return self.get_query_params().get('DesiredCapacity')

	def set_DesiredCapacity(self, DesiredCapacity):  # Integer
		self.add_query_param('DesiredCapacity', DesiredCapacity)
	def get_LaunchTemplateOverrides(self): # RepeatList
		return self.get_query_params().get('LaunchTemplateOverride')

	def set_LaunchTemplateOverrides(self, LaunchTemplateOverride):  # RepeatList
		for depth1 in range(len(LaunchTemplateOverride)):
			if LaunchTemplateOverride[depth1].get('WeightedCapacity') is not None:
				self.add_query_param('LaunchTemplateOverride.' + str(depth1 + 1) + '.WeightedCapacity', LaunchTemplateOverride[depth1].get('WeightedCapacity'))
			if LaunchTemplateOverride[depth1].get('InstanceType') is not None:
				self.add_query_param('LaunchTemplateOverride.' + str(depth1 + 1) + '.InstanceType', LaunchTemplateOverride[depth1].get('InstanceType'))
			if LaunchTemplateOverride[depth1].get('SpotPriceLimit') is not None:
				self.add_query_param('LaunchTemplateOverride.' + str(depth1 + 1) + '.SpotPriceLimit', LaunchTemplateOverride[depth1].get('SpotPriceLimit'))
	def get_CompensateWithOnDemand(self): # Boolean
		return self.get_query_params().get('CompensateWithOnDemand')

	def set_CompensateWithOnDemand(self, CompensateWithOnDemand):  # Boolean
		self.add_query_param('CompensateWithOnDemand', CompensateWithOnDemand)
	def get_MinSize(self): # Integer
		return self.get_query_params().get('MinSize')

	def set_MinSize(self, MinSize):  # Integer
		self.add_query_param('MinSize', MinSize)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_MaxSize(self): # Integer
		return self.get_query_params().get('MaxSize')

	def set_MaxSize(self, MaxSize):  # Integer
		self.add_query_param('MaxSize', MaxSize)
	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_OnDemandBaseCapacity(self): # Integer
		return self.get_query_params().get('OnDemandBaseCapacity')

	def set_OnDemandBaseCapacity(self, OnDemandBaseCapacity):  # Integer
		self.add_query_param('OnDemandBaseCapacity', OnDemandBaseCapacity)
	def get_OnDemandPercentageAboveBaseCapacity(self): # Integer
		return self.get_query_params().get('OnDemandPercentageAboveBaseCapacity')

	def set_OnDemandPercentageAboveBaseCapacity(self, OnDemandPercentageAboveBaseCapacity):  # Integer
		self.add_query_param('OnDemandPercentageAboveBaseCapacity', OnDemandPercentageAboveBaseCapacity)
	def get_SpotAllocationStrategy(self): # String
		return self.get_query_params().get('SpotAllocationStrategy')

	def set_SpotAllocationStrategy(self, SpotAllocationStrategy):  # String
		self.add_query_param('SpotAllocationStrategy', SpotAllocationStrategy)
	def get_RemovalPolicy1(self): # String
		return self.get_query_params().get('RemovalPolicy.1')

	def set_RemovalPolicy1(self, RemovalPolicy1):  # String
		self.add_query_param('RemovalPolicy.1', RemovalPolicy1)
	def get_RemovalPolicy2(self): # String
		return self.get_query_params().get('RemovalPolicy.2')

	def set_RemovalPolicy2(self, RemovalPolicy2):  # String
		self.add_query_param('RemovalPolicy.2', RemovalPolicy2)
	def get_RemovalPolicy3(self): # String
		return self.get_query_params().get('RemovalPolicy.3')

	def set_RemovalPolicy3(self, RemovalPolicy3):  # String
		self.add_query_param('RemovalPolicy.3', RemovalPolicy3)
	def get_HealthCheckType(self): # String
		return self.get_query_params().get('HealthCheckType')

	def set_HealthCheckType(self, HealthCheckType):  # String
		self.add_query_param('HealthCheckType', HealthCheckType)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_ScalingGroupName(self): # String
		return self.get_query_params().get('ScalingGroupName')

	def set_ScalingGroupName(self, ScalingGroupName):  # String
		self.add_query_param('ScalingGroupName', ScalingGroupName)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_SpotInstancePools(self): # Integer
		return self.get_query_params().get('SpotInstancePools')

	def set_SpotInstancePools(self, SpotInstancePools):  # Integer
		self.add_query_param('SpotInstancePools', SpotInstancePools)
	def get_GroupDeletionProtection(self): # Boolean
		return self.get_query_params().get('GroupDeletionProtection')

	def set_GroupDeletionProtection(self, GroupDeletionProtection):  # Boolean
		self.add_query_param('GroupDeletionProtection', GroupDeletionProtection)
	def get_LaunchTemplateVersion(self): # String
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self, LaunchTemplateVersion):  # String
		self.add_query_param('LaunchTemplateVersion', LaunchTemplateVersion)
	def get_AllocationStrategy(self): # String
		return self.get_query_params().get('AllocationStrategy')

	def set_AllocationStrategy(self, AllocationStrategy):  # String
		self.add_query_param('AllocationStrategy', AllocationStrategy)
