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
from aliyunsdkslb.endpoint import endpoint_data

class SetLoadBalancerUDPListenerAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Slb', '2014-05-15', 'SetLoadBalancerUDPListenerAttribute','slb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_AclStatus(self):
		return self.get_query_params().get('AclStatus')

	def set_AclStatus(self,AclStatus):
		self.add_query_param('AclStatus',AclStatus)

	def get_AclType(self):
		return self.get_query_params().get('AclType')

	def set_AclType(self,AclType):
		self.add_query_param('AclType',AclType)

	def get_MasterSlaveServerGroup(self):
		return self.get_query_params().get('MasterSlaveServerGroup')

	def set_MasterSlaveServerGroup(self,MasterSlaveServerGroup):
		self.add_query_param('MasterSlaveServerGroup',MasterSlaveServerGroup)

	def get_VServerGroupId(self):
		return self.get_query_params().get('VServerGroupId')

	def set_VServerGroupId(self,VServerGroupId):
		self.add_query_param('VServerGroupId',VServerGroupId)

	def get_AclId(self):
		return self.get_query_params().get('AclId')

	def set_AclId(self,AclId):
		self.add_query_param('AclId',AclId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_LoadBalancerId(self):
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self,LoadBalancerId):
		self.add_query_param('LoadBalancerId',LoadBalancerId)

	def get_MasterSlaveServerGroupId(self):
		return self.get_query_params().get('MasterSlaveServerGroupId')

	def set_MasterSlaveServerGroupId(self,MasterSlaveServerGroupId):
		self.add_query_param('MasterSlaveServerGroupId',MasterSlaveServerGroupId)

	def get_healthCheckReq(self):
		return self.get_query_params().get('healthCheckReq')

	def set_healthCheckReq(self,healthCheckReq):
		self.add_query_param('healthCheckReq',healthCheckReq)

	def get_HealthCheckInterval(self):
		return self.get_query_params().get('HealthCheckInterval')

	def set_HealthCheckInterval(self,HealthCheckInterval):
		self.add_query_param('HealthCheckInterval',HealthCheckInterval)

	def get_healthCheckExp(self):
		return self.get_query_params().get('healthCheckExp')

	def set_healthCheckExp(self,healthCheckExp):
		self.add_query_param('healthCheckExp',healthCheckExp)

	def get_HealthCheckConnectTimeout(self):
		return self.get_query_params().get('HealthCheckConnectTimeout')

	def set_HealthCheckConnectTimeout(self,HealthCheckConnectTimeout):
		self.add_query_param('HealthCheckConnectTimeout',HealthCheckConnectTimeout)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_UnhealthyThreshold(self):
		return self.get_query_params().get('UnhealthyThreshold')

	def set_UnhealthyThreshold(self,UnhealthyThreshold):
		self.add_query_param('UnhealthyThreshold',UnhealthyThreshold)

	def get_HealthyThreshold(self):
		return self.get_query_params().get('HealthyThreshold')

	def set_HealthyThreshold(self,HealthyThreshold):
		self.add_query_param('HealthyThreshold',HealthyThreshold)

	def get_Scheduler(self):
		return self.get_query_params().get('Scheduler')

	def set_Scheduler(self,Scheduler):
		self.add_query_param('Scheduler',Scheduler)

	def get_ListenerPort(self):
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self,ListenerPort):
		self.add_query_param('ListenerPort',ListenerPort)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_HealthCheckConnectPort(self):
		return self.get_query_params().get('HealthCheckConnectPort')

	def set_HealthCheckConnectPort(self,HealthCheckConnectPort):
		self.add_query_param('HealthCheckConnectPort',HealthCheckConnectPort)

	def get_VServerGroup(self):
		return self.get_query_params().get('VServerGroup')

	def set_VServerGroup(self,VServerGroup):
		self.add_query_param('VServerGroup',VServerGroup)