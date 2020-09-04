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

class ModifyInstanceDeploymentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyInstanceDeployment','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DeploymentSetGroupNo(self):
		return self.get_query_params().get('DeploymentSetGroupNo')

	def set_DeploymentSetGroupNo(self,DeploymentSetGroupNo):
		self.add_query_param('DeploymentSetGroupNo',DeploymentSetGroupNo)

	def get_DedicatedHostClusterId(self):
		return self.get_query_params().get('DedicatedHostClusterId')

	def set_DedicatedHostClusterId(self,DedicatedHostClusterId):
		self.add_query_param('DedicatedHostClusterId',DedicatedHostClusterId)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_DeploymentSetId(self):
		return self.get_query_params().get('DeploymentSetId')

	def set_DeploymentSetId(self,DeploymentSetId):
		self.add_query_param('DeploymentSetId',DeploymentSetId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Tenancy(self):
		return self.get_query_params().get('Tenancy')

	def set_Tenancy(self,Tenancy):
		self.add_query_param('Tenancy',Tenancy)

	def get_DedicatedHostId(self):
		return self.get_query_params().get('DedicatedHostId')

	def set_DedicatedHostId(self,DedicatedHostId):
		self.add_query_param('DedicatedHostId',DedicatedHostId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Force(self):
		return self.get_query_params().get('Force')

	def set_Force(self,Force):
		self.add_query_param('Force',Force)

	def get_MigrationType(self):
		return self.get_query_params().get('MigrationType')

	def set_MigrationType(self,MigrationType):
		self.add_query_param('MigrationType',MigrationType)

	def get_Affinity(self):
		return self.get_query_params().get('Affinity')

	def set_Affinity(self,Affinity):
		self.add_query_param('Affinity',Affinity)