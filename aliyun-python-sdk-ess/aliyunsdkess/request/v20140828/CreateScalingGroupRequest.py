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
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_VSwitchIdss(self):
		return self.get_query_params().get('VSwitchIdss')

	def set_VSwitchIdss(self,VSwitchIdss):
		for i in range(len(VSwitchIdss)):	
			if VSwitchIdss[i] is not None:
				self.add_query_param('VSwitchIds.' + str(i + 1) , VSwitchIdss[i]);

	def get_SpotInstanceRemedy(self):
		return self.get_query_params().get('SpotInstanceRemedy')

	def set_SpotInstanceRemedy(self,SpotInstanceRemedy):
		self.add_query_param('SpotInstanceRemedy',SpotInstanceRemedy)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		for i in range(len(Tags)):	
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value' , Tags[i].get('Value'))
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key' , Tags[i].get('Key'))


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
		return self.get_query_params().get('LifecycleHooks')

	def set_LifecycleHooks(self,LifecycleHooks):
		for i in range(len(LifecycleHooks)):	
			if LifecycleHooks[i].get('DefaultResult') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.DefaultResult' , LifecycleHooks[i].get('DefaultResult'))
			if LifecycleHooks[i].get('LifecycleHookName') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.LifecycleHookName' , LifecycleHooks[i].get('LifecycleHookName'))
			if LifecycleHooks[i].get('HeartbeatTimeout') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.HeartbeatTimeout' , LifecycleHooks[i].get('HeartbeatTimeout'))
			if LifecycleHooks[i].get('NotificationArn') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.NotificationArn' , LifecycleHooks[i].get('NotificationArn'))
			if LifecycleHooks[i].get('NotificationMetadata') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.NotificationMetadata' , LifecycleHooks[i].get('NotificationMetadata'))
			if LifecycleHooks[i].get('LifecycleTransition') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.LifecycleTransition' , LifecycleHooks[i].get('LifecycleTransition'))


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
		return self.get_query_params().get('VServerGroups')

	def set_VServerGroups(self,VServerGroups):
		for i in range(len(VServerGroups)):	
			if VServerGroups[i].get('LoadBalancerId') is not None:
				self.add_query_param('VServerGroup.' + str(i + 1) + '.LoadBalancerId' , VServerGroups[i].get('LoadBalancerId'))
			for j in range(len(VServerGroups[i].get('VServerGroupAttributes'))):
				if VServerGroups[i].get('VServerGroupAttributes')[j] is not None:
					if VServerGroups[i].get('VServerGroupAttributes')[j].get('VServerGroupId') is not None:
						self.add_query_param('VServerGroup.' + str(i + 1) + '.VServerGroupAttribute.'+str(j + 1)+ '.VServerGroupId', VServerGroups[i].get('VServerGroupAttributes')[j].get('VServerGroupId'))
					if VServerGroups[i].get('VServerGroupAttributes')[j].get('Port') is not None:
						self.add_query_param('VServerGroup.' + str(i + 1) + '.VServerGroupAttribute.'+str(j + 1)+ '.Port', VServerGroups[i].get('VServerGroupAttributes')[j].get('Port'))
					if VServerGroups[i].get('VServerGroupAttributes')[j].get('Weight') is not None:
						self.add_query_param('VServerGroup.' + str(i + 1) + '.VServerGroupAttribute.'+str(j + 1)+ '.Weight', VServerGroups[i].get('VServerGroupAttributes')[j].get('Weight'))
