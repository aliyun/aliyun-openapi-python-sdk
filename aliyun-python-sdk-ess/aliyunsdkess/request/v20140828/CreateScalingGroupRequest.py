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

class CreateScalingGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'CreateScalingGroup','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

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
	def get_SpotInstanceRemedy(self): # Boolean
		return self.get_query_params().get('SpotInstanceRemedy')

	def set_SpotInstanceRemedy(self, SpotInstanceRemedy):  # Boolean
		self.add_query_param('SpotInstanceRemedy', SpotInstanceRemedy)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_GroupType(self): # String
		return self.get_query_params().get('GroupType')

	def set_GroupType(self, GroupType):  # String
		self.add_query_param('GroupType', GroupType)
	def get_CustomPolicyARN(self): # String
		return self.get_query_params().get('CustomPolicyARN')

	def set_CustomPolicyARN(self, CustomPolicyARN):  # String
		self.add_query_param('CustomPolicyARN', CustomPolicyARN)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Propagate') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Propagate', Tag[depth1].get('Propagate'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_DefaultCooldown(self): # Integer
		return self.get_query_params().get('DefaultCooldown')

	def set_DefaultCooldown(self, DefaultCooldown):  # Integer
		self.add_query_param('DefaultCooldown', DefaultCooldown)
	def get_ContainerGroupId(self): # String
		return self.get_query_params().get('ContainerGroupId')

	def set_ContainerGroupId(self, ContainerGroupId):  # String
		self.add_query_param('ContainerGroupId', ContainerGroupId)
	def get_MultiAZPolicy(self): # String
		return self.get_query_params().get('MultiAZPolicy')

	def set_MultiAZPolicy(self, MultiAZPolicy):  # String
		self.add_query_param('MultiAZPolicy', MultiAZPolicy)
	def get_DBInstanceIds(self): # String
		return self.get_query_params().get('DBInstanceIds')

	def set_DBInstanceIds(self, DBInstanceIds):  # String
		self.add_query_param('DBInstanceIds', DBInstanceIds)
	def get_LaunchTemplateId(self): # String
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self, LaunchTemplateId):  # String
		self.add_query_param('LaunchTemplateId', LaunchTemplateId)
	def get_DesiredCapacity(self): # Integer
		return self.get_query_params().get('DesiredCapacity')

	def set_DesiredCapacity(self, DesiredCapacity):  # Integer
		self.add_query_param('DesiredCapacity', DesiredCapacity)
	def get_ServerGroups(self): # RepeatList
		return self.get_query_params().get('ServerGroup')

	def set_ServerGroups(self, ServerGroup):  # RepeatList
		for depth1 in range(len(ServerGroup)):
			if ServerGroup[depth1].get('ServerGroupId') is not None:
				self.add_query_param('ServerGroup.' + str(depth1 + 1) + '.ServerGroupId', ServerGroup[depth1].get('ServerGroupId'))
			if ServerGroup[depth1].get('Port') is not None:
				self.add_query_param('ServerGroup.' + str(depth1 + 1) + '.Port', ServerGroup[depth1].get('Port'))
			if ServerGroup[depth1].get('Weight') is not None:
				self.add_query_param('ServerGroup.' + str(depth1 + 1) + '.Weight', ServerGroup[depth1].get('Weight'))
			if ServerGroup[depth1].get('Type') is not None:
				self.add_query_param('ServerGroup.' + str(depth1 + 1) + '.Type', ServerGroup[depth1].get('Type'))
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
	def get_AlbServerGroups(self): # RepeatList
		return self.get_query_params().get('AlbServerGroup')

	def set_AlbServerGroups(self, AlbServerGroup):  # RepeatList
		for depth1 in range(len(AlbServerGroup)):
			if AlbServerGroup[depth1].get('AlbServerGroupId') is not None:
				self.add_query_param('AlbServerGroup.' + str(depth1 + 1) + '.AlbServerGroupId', AlbServerGroup[depth1].get('AlbServerGroupId'))
			if AlbServerGroup[depth1].get('Port') is not None:
				self.add_query_param('AlbServerGroup.' + str(depth1 + 1) + '.Port', AlbServerGroup[depth1].get('Port'))
			if AlbServerGroup[depth1].get('Weight') is not None:
				self.add_query_param('AlbServerGroup.' + str(depth1 + 1) + '.Weight', AlbServerGroup[depth1].get('Weight'))
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_MaxSize(self): # Integer
		return self.get_query_params().get('MaxSize')

	def set_MaxSize(self, MaxSize):  # Integer
		self.add_query_param('MaxSize', MaxSize)
	def get_LifecycleHooks(self): # RepeatList
		return self.get_query_params().get('LifecycleHook')

	def set_LifecycleHooks(self, LifecycleHook):  # RepeatList
		for depth1 in range(len(LifecycleHook)):
			if LifecycleHook[depth1].get('DefaultResult') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.DefaultResult', LifecycleHook[depth1].get('DefaultResult'))
			if LifecycleHook[depth1].get('LifecycleHookName') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.LifecycleHookName', LifecycleHook[depth1].get('LifecycleHookName'))
			if LifecycleHook[depth1].get('HeartbeatTimeout') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.HeartbeatTimeout', LifecycleHook[depth1].get('HeartbeatTimeout'))
			if LifecycleHook[depth1].get('NotificationArn') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.NotificationArn', LifecycleHook[depth1].get('NotificationArn'))
			if LifecycleHook[depth1].get('NotificationMetadata') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.NotificationMetadata', LifecycleHook[depth1].get('NotificationMetadata'))
			if LifecycleHook[depth1].get('LifecycleTransition') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.LifecycleTransition', LifecycleHook[depth1].get('LifecycleTransition'))
	def get_LoadBalancerIds(self): # String
		return self.get_query_params().get('LoadBalancerIds')

	def set_LoadBalancerIds(self, LoadBalancerIds):  # String
		self.add_query_param('LoadBalancerIds', LoadBalancerIds)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
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
	def get_ScalingPolicy(self): # String
		return self.get_query_params().get('ScalingPolicy')

	def set_ScalingPolicy(self, ScalingPolicy):  # String
		self.add_query_param('ScalingPolicy', ScalingPolicy)
	def get_AllocationStrategy(self): # String
		return self.get_query_params().get('AllocationStrategy')

	def set_AllocationStrategy(self, AllocationStrategy):  # String
		self.add_query_param('AllocationStrategy', AllocationStrategy)
	def get_VServerGroups(self): # RepeatList
		return self.get_query_params().get('VServerGroup')

	def set_VServerGroups(self, VServerGroup):  # RepeatList
		for depth1 in range(len(VServerGroup)):
			if VServerGroup[depth1].get('LoadBalancerId') is not None:
				self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.LoadBalancerId', VServerGroup[depth1].get('LoadBalancerId'))
			if VServerGroup[depth1].get('VServerGroupAttribute') is not None:
				for depth2 in range(len(VServerGroup[depth1].get('VServerGroupAttribute'))):
					if VServerGroup[depth1].get('VServerGroupAttribute')[depth2].get('VServerGroupId') is not None:
						self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.VServerGroupAttribute.'  + str(depth2 + 1) + '.VServerGroupId', VServerGroup[depth1].get('VServerGroupAttribute')[depth2].get('VServerGroupId'))
					if VServerGroup[depth1].get('VServerGroupAttribute')[depth2].get('Port') is not None:
						self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.VServerGroupAttribute.'  + str(depth2 + 1) + '.Port', VServerGroup[depth1].get('VServerGroupAttribute')[depth2].get('Port'))
					if VServerGroup[depth1].get('VServerGroupAttribute')[depth2].get('Weight') is not None:
						self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.VServerGroupAttribute.'  + str(depth2 + 1) + '.Weight', VServerGroup[depth1].get('VServerGroupAttribute')[depth2].get('Weight'))
