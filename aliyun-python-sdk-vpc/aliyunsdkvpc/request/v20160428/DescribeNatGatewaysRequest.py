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
from aliyunsdkvpc.endpoint import endpoint_data

class DescribeNatGatewaysRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DescribeNatGateways','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_NetworkType(self): # String
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self, NetworkType):  # String
		self.add_query_param('NetworkType', NetworkType)
	def get_Spec(self): # String
		return self.get_query_params().get('Spec')

	def set_Spec(self, Spec):  # String
		self.add_query_param('Spec', Spec)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_NatType(self): # String
		return self.get_query_params().get('NatType')

	def set_NatType(self, NatType):  # String
		self.add_query_param('NatType', NatType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_NatGatewayId(self): # String
		return self.get_query_params().get('NatGatewayId')

	def set_NatGatewayId(self, NatGatewayId):  # String
		self.add_query_param('NatGatewayId', NatGatewayId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
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
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
