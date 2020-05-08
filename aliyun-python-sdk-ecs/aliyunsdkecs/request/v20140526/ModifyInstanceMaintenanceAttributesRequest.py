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

class ModifyInstanceMaintenanceAttributesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyInstanceMaintenanceAttributes','ecs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_MaintenanceWindows(self):
		return self.get_query_params().get('MaintenanceWindows')

	def set_MaintenanceWindows(self,MaintenanceWindows):
		for i in range(len(MaintenanceWindows)):	
			if MaintenanceWindows[i].get('StartTime') is not None:
				self.add_query_param('MaintenanceWindow.' + str(i + 1) + '.StartTime' , MaintenanceWindows[i].get('StartTime'))
			if MaintenanceWindows[i].get('EndTime') is not None:
				self.add_query_param('MaintenanceWindow.' + str(i + 1) + '.EndTime' , MaintenanceWindows[i].get('EndTime'))


	def get_ActionOnMaintenance(self):
		return self.get_query_params().get('ActionOnMaintenance')

	def set_ActionOnMaintenance(self,ActionOnMaintenance):
		self.add_query_param('ActionOnMaintenance',ActionOnMaintenance)

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

	def get_InstanceIds(self):
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self,InstanceIds):
		for i in range(len(InstanceIds)):	
			if InstanceIds[i] is not None:
				self.add_query_param('InstanceId.' + str(i + 1) , InstanceIds[i]);