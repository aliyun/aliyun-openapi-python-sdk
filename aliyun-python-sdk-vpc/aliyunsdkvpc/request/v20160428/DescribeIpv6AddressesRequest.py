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

class DescribeIpv6AddressesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DescribeIpv6Addresses','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ServiceManaged(self): # Boolean
		return self.get_query_params().get('ServiceManaged')

	def set_ServiceManaged(self, ServiceManaged):  # Boolean
		self.add_query_param('ServiceManaged', ServiceManaged)
	def get_Ipv6InternetBandwidthId(self): # String
		return self.get_query_params().get('Ipv6InternetBandwidthId')

	def set_Ipv6InternetBandwidthId(self, Ipv6InternetBandwidthId):  # String
		self.add_query_param('Ipv6InternetBandwidthId', Ipv6InternetBandwidthId)
	def get_NetworkType(self): # String
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self, NetworkType):  # String
		self.add_query_param('NetworkType', NetworkType)
	def get_IncludeReservationData(self): # Boolean
		return self.get_query_params().get('IncludeReservationData')

	def set_IncludeReservationData(self, IncludeReservationData):  # Boolean
		self.add_query_param('IncludeReservationData', IncludeReservationData)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_AssociatedInstanceType(self): # String
		return self.get_query_params().get('AssociatedInstanceType')

	def set_AssociatedInstanceType(self, AssociatedInstanceType):  # String
		self.add_query_param('AssociatedInstanceType', AssociatedInstanceType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_AddressType(self): # String
		return self.get_query_params().get('AddressType')

	def set_AddressType(self, AddressType):  # String
		self.add_query_param('AddressType', AddressType)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
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
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_Ipv6AddressId(self): # String
		return self.get_query_params().get('Ipv6AddressId')

	def set_Ipv6AddressId(self, Ipv6AddressId):  # String
		self.add_query_param('Ipv6AddressId', Ipv6AddressId)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Ipv6Address(self): # String
		return self.get_query_params().get('Ipv6Address')

	def set_Ipv6Address(self, Ipv6Address):  # String
		self.add_query_param('Ipv6Address', Ipv6Address)
	def get_AssociatedInstanceId(self): # String
		return self.get_query_params().get('AssociatedInstanceId')

	def set_AssociatedInstanceId(self, AssociatedInstanceId):  # String
		self.add_query_param('AssociatedInstanceId', AssociatedInstanceId)
