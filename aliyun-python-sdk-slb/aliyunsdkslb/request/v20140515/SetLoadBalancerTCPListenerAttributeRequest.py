# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class SetLoadBalancerTCPListenerAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Slb', '2014-05-15', 'SetLoadBalancerTCPListenerAttribute')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_LoadBalancerId(self):
		return self.get_query_params().get('LoadBalancerId')

	def set_LoadBalancerId(self,LoadBalancerId):
		self.add_query_param('LoadBalancerId',LoadBalancerId)

	def get_ListenerPort(self):
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self,ListenerPort):
		self.add_query_param('ListenerPort',ListenerPort)

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

	def get_Scheduler(self):
		return self.get_query_params().get('Scheduler')

	def set_Scheduler(self,Scheduler):
		self.add_query_param('Scheduler',Scheduler)

	def get_PersistenceTimeout(self):
		return self.get_query_params().get('PersistenceTimeout')

	def set_PersistenceTimeout(self,PersistenceTimeout):
		self.add_query_param('PersistenceTimeout',PersistenceTimeout)

	def get_HealthyThreshold(self):
		return self.get_query_params().get('HealthyThreshold')

	def set_HealthyThreshold(self,HealthyThreshold):
		self.add_query_param('HealthyThreshold',HealthyThreshold)

	def get_UnhealthyThreshold(self):
		return self.get_query_params().get('UnhealthyThreshold')

	def set_UnhealthyThreshold(self,UnhealthyThreshold):
		self.add_query_param('UnhealthyThreshold',UnhealthyThreshold)

	def get_HealthCheckConnectTimeout(self):
		return self.get_query_params().get('HealthCheckConnectTimeout')

	def set_HealthCheckConnectTimeout(self,HealthCheckConnectTimeout):
		self.add_query_param('HealthCheckConnectTimeout',HealthCheckConnectTimeout)

	def get_HealthCheckConnectPort(self):
		return self.get_query_params().get('HealthCheckConnectPort')

	def set_HealthCheckConnectPort(self,HealthCheckConnectPort):
		self.add_query_param('HealthCheckConnectPort',HealthCheckConnectPort)

	def get_HealthCheckInterval(self):
		return self.get_query_params().get('HealthCheckInterval')

	def set_HealthCheckInterval(self,HealthCheckInterval):
		self.add_query_param('HealthCheckInterval',HealthCheckInterval)

	def get_HealthCheckDomain(self):
		return self.get_query_params().get('HealthCheckDomain')

	def set_HealthCheckDomain(self,HealthCheckDomain):
		self.add_query_param('HealthCheckDomain',HealthCheckDomain)

	def get_HealthCheckURI(self):
		return self.get_query_params().get('HealthCheckURI')

	def set_HealthCheckURI(self,HealthCheckURI):
		self.add_query_param('HealthCheckURI',HealthCheckURI)

	def get_HealthCheckHttpCode(self):
		return self.get_query_params().get('HealthCheckHttpCode')

	def set_HealthCheckHttpCode(self,HealthCheckHttpCode):
		self.add_query_param('HealthCheckHttpCode',HealthCheckHttpCode)

	def get_HealthCheckType(self):
		return self.get_query_params().get('HealthCheckType')

	def set_HealthCheckType(self,HealthCheckType):
		self.add_query_param('HealthCheckType',HealthCheckType)

	def get_SynProxy(self):
		return self.get_query_params().get('SynProxy')

	def set_SynProxy(self,SynProxy):
		self.add_query_param('SynProxy',SynProxy)

	def get_MaxConnection(self):
		return self.get_query_params().get('MaxConnection')

	def set_MaxConnection(self,MaxConnection):
		self.add_query_param('MaxConnection',MaxConnection)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_access_key_id(self):
		return self.get_query_params().get('access_key_id')

	def set_access_key_id(self,access_key_id):
		self.add_query_param('access_key_id',access_key_id)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_VServerGroup(self):
		return self.get_query_params().get('VServerGroup')

	def set_VServerGroup(self,VServerGroup):
		self.add_query_param('VServerGroup',VServerGroup)

	def get_VServerGroupId(self):
		return self.get_query_params().get('VServerGroupId')

	def set_VServerGroupId(self,VServerGroupId):
		self.add_query_param('VServerGroupId',VServerGroupId)