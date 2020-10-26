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


	def get_VSwitchIdss(self):
		return self.get_query_params().get('VSwitchIds')

	def set_VSwitchIdss(self, VSwitchIdss):
		for depth1 in range(len(VSwitchIdss)):
			if VSwitchIdss[depth1] is not None:
				self.add_query_param('VSwitchIds.' + str(depth1 + 1) , VSwitchIdss[depth1])

	def get_SpotInstanceRemedy(self):
		return self.get_query_params().get('SpotInstanceRemedy')

	def set_SpotInstanceRemedy(self,SpotInstanceRemedy):
		self.add_query_param('SpotInstanceRemedy',SpotInstanceRemedy)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_DefaultCooldown(self):
		return self.get_query_params().get('DefaultCooldown')

	def set_DefaultCooldown(self,DefaultCooldown):
		self.add_query_param('DefaultCooldown',DefaultCooldown)

	def get_MultiAZPolicy(self):
		return self.get_query_params().get('MultiAZPolicy')

	def set_MultiAZPolicy(self,MultiAZPolicy):
		self.add_query_param('MultiAZPolicy',MultiAZPolicy)

	def get_DBInstanceIds(self):
		return self.get_query_params().get('DBInstanceIds')

	def set_DBInstanceIds(self,DBInstanceIds):
		self.add_query_param('DBInstanceIds',DBInstanceIds)

	def get_LaunchTemplateId(self):
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self,LaunchTemplateId):
		self.add_query_param('LaunchTemplateId',LaunchTemplateId)

	def get_DesiredCapacity(self):
		return self.get_query_params().get('DesiredCapacity')

	def set_DesiredCapacity(self,DesiredCapacity):
		self.add_query_param('DesiredCapacity',DesiredCapacity)

	def get_CompensateWithOnDemand(self):
		return self.get_query_params().get('CompensateWithOnDemand')

	def set_CompensateWithOnDemand(self,CompensateWithOnDemand):
		self.add_query_param('CompensateWithOnDemand',CompensateWithOnDemand)

	def get_MinSize(self):
		return self.get_query_params().get('MinSize')

	def set_MinSize(self,MinSize):
		self.add_query_param('MinSize',MinSize)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_MaxSize(self):
		return self.get_query_params().get('MaxSize')

	def set_MaxSize(self,MaxSize):
		self.add_query_param('MaxSize',MaxSize)

	def get_LifecycleHooks(self):
		return self.get_query_params().get('LifecycleHook')

	def set_LifecycleHooks(self, LifecycleHooks):
		for depth1 in range(len(LifecycleHooks)):
			if LifecycleHooks[depth1].get('DefaultResult') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.DefaultResult', LifecycleHooks[depth1].get('DefaultResult'))
			if LifecycleHooks[depth1].get('LifecycleHookName') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.LifecycleHookName', LifecycleHooks[depth1].get('LifecycleHookName'))
			if LifecycleHooks[depth1].get('HeartbeatTimeout') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.HeartbeatTimeout', LifecycleHooks[depth1].get('HeartbeatTimeout'))
			if LifecycleHooks[depth1].get('NotificationArn') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.NotificationArn', LifecycleHooks[depth1].get('NotificationArn'))
			if LifecycleHooks[depth1].get('NotificationMetadata') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.NotificationMetadata', LifecycleHooks[depth1].get('NotificationMetadata'))
			if LifecycleHooks[depth1].get('LifecycleTransition') is not None:
				self.add_query_param('LifecycleHook.' + str(depth1 + 1) + '.LifecycleTransition', LifecycleHooks[depth1].get('LifecycleTransition'))

	def get_LoadBalancerIds(self):
		return self.get_query_params().get('LoadBalancerIds')

	def set_LoadBalancerIds(self,LoadBalancerIds):
		self.add_query_param('LoadBalancerIds',LoadBalancerIds)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_OnDemandBaseCapacity(self):
		return self.get_query_params().get('OnDemandBaseCapacity')

	def set_OnDemandBaseCapacity(self,OnDemandBaseCapacity):
		self.add_query_param('OnDemandBaseCapacity',OnDemandBaseCapacity)

	def get_OnDemandPercentageAboveBaseCapacity(self):
		return self.get_query_params().get('OnDemandPercentageAboveBaseCapacity')

	def set_OnDemandPercentageAboveBaseCapacity(self,OnDemandPercentageAboveBaseCapacity):
		self.add_query_param('OnDemandPercentageAboveBaseCapacity',OnDemandPercentageAboveBaseCapacity)

	def get_RemovalPolicy1(self):
		return self.get_query_params().get('RemovalPolicy.1')

	def set_RemovalPolicy1(self,RemovalPolicy1):
		self.add_query_param('RemovalPolicy.1',RemovalPolicy1)

	def get_RemovalPolicy2(self):
		return self.get_query_params().get('RemovalPolicy.2')

	def set_RemovalPolicy2(self,RemovalPolicy2):
		self.add_query_param('RemovalPolicy.2',RemovalPolicy2)

	def get_HealthCheckType(self):
		return self.get_query_params().get('HealthCheckType')

	def set_HealthCheckType(self,HealthCheckType):
		self.add_query_param('HealthCheckType',HealthCheckType)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ScalingGroupName(self):
		return self.get_query_params().get('ScalingGroupName')

	def set_ScalingGroupName(self,ScalingGroupName):
		self.add_query_param('ScalingGroupName',ScalingGroupName)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_SpotInstancePools(self):
		return self.get_query_params().get('SpotInstancePools')

	def set_SpotInstancePools(self,SpotInstancePools):
		self.add_query_param('SpotInstancePools',SpotInstancePools)

	def get_GroupDeletionProtection(self):
		return self.get_query_params().get('GroupDeletionProtection')

	def set_GroupDeletionProtection(self,GroupDeletionProtection):
		self.add_query_param('GroupDeletionProtection',GroupDeletionProtection)

	def get_LaunchTemplateVersion(self):
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersion(self,LaunchTemplateVersion):
		self.add_query_param('LaunchTemplateVersion',LaunchTemplateVersion)

	def get_ScalingPolicy(self):
		return self.get_query_params().get('ScalingPolicy')

	def set_ScalingPolicy(self,ScalingPolicy):
		self.add_query_param('ScalingPolicy',ScalingPolicy)

	def get_VServerGroups(self):
		return self.get_query_params().get('VServerGroup')

	def set_VServerGroups(self, VServerGroups):
		for depth1 in range(len(VServerGroups)):
			if VServerGroups[depth1].get('LoadBalancerId') is not None:
				self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.LoadBalancerId', VServerGroups[depth1].get('LoadBalancerId'))
			if VServerGroups[depth1].get('VServerGroupAttribute') is not None:
				for depth2 in range(len(VServerGroups[depth1].get('VServerGroupAttribute'))):
					if VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('VServerGroupId') is not None:
						self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.VServerGroupAttribute.' + str(depth2 + 1) + '.VServerGroupId', VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('VServerGroupId'))
					if VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('Port') is not None:
						self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.VServerGroupAttribute.' + str(depth2 + 1) + '.Port', VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('Port'))
					if VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('Weight') is not None:
						self.add_query_param('VServerGroup.' + str(depth1 + 1) + '.VServerGroupAttribute.' + str(depth2 + 1) + '.Weight', VServerGroups[depth1].get('VServerGroupAttribute')[depth2].get('Weight'))