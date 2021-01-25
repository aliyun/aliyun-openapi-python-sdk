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

class DescribeReservedInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeReservedInstances','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_LockReason(self):
		return self.get_query_params().get('LockReason')

	def set_LockReason(self,LockReason):
		self.add_query_param('LockReason',LockReason)

	def get_Scope(self):
		return self.get_query_params().get('Scope')

	def set_Scope(self,Scope):
		self.add_query_param('Scope',Scope)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_InstanceTypeFamily(self):
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamily(self,InstanceTypeFamily):
		self.add_query_param('InstanceTypeFamily',InstanceTypeFamily)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ReservedInstanceIds(self):
		return self.get_query_params().get('ReservedInstanceId')

	def set_ReservedInstanceIds(self, ReservedInstanceIds):
		for depth1 in range(len(ReservedInstanceIds)):
			if ReservedInstanceIds[depth1] is not None:
				self.add_query_param('ReservedInstanceId.' + str(depth1 + 1) , ReservedInstanceIds[depth1])

	def get_OfferingType(self):
		return self.get_query_params().get('OfferingType')

	def set_OfferingType(self,OfferingType):
		self.add_query_param('OfferingType',OfferingType)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_ReservedInstanceName(self):
		return self.get_query_params().get('ReservedInstanceName')

	def set_ReservedInstanceName(self,ReservedInstanceName):
		self.add_query_param('ReservedInstanceName',ReservedInstanceName)

	def get_Statuss(self):
		return self.get_query_params().get('Status')

	def set_Statuss(self, Statuss):
		for depth1 in range(len(Statuss)):
			if Statuss[depth1] is not None:
				self.add_query_param('Status.' + str(depth1 + 1) , Statuss[depth1])

	def get_AllocationType(self):
		return self.get_query_params().get('AllocationType')

	def set_AllocationType(self,AllocationType):
		self.add_query_param('AllocationType',AllocationType)