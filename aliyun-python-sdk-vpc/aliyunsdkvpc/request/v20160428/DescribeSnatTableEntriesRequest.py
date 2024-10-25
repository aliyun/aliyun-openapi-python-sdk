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

class DescribeSnatTableEntriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DescribeSnatTableEntries','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_NetworkInterfaceIds(self): # Array
		return self.get_query_params().get('NetworkInterfaceIds')

	def set_NetworkInterfaceIds(self, NetworkInterfaceIds):  # Array
		for index1, value1 in enumerate(NetworkInterfaceIds):
			self.add_query_param('NetworkInterfaceIds.' + str(index1 + 1), value1)
	def get_SourceCIDR(self): # String
		return self.get_query_params().get('SourceCIDR')

	def set_SourceCIDR(self, SourceCIDR):  # String
		self.add_query_param('SourceCIDR', SourceCIDR)
	def get_SnatIp(self): # String
		return self.get_query_params().get('SnatIp')

	def set_SnatIp(self, SnatIp):  # String
		self.add_query_param('SnatIp', SnatIp)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_SourceVSwitchId(self): # String
		return self.get_query_params().get('SourceVSwitchId')

	def set_SourceVSwitchId(self, SourceVSwitchId):  # String
		self.add_query_param('SourceVSwitchId', SourceVSwitchId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_SnatEntryId(self): # String
		return self.get_query_params().get('SnatEntryId')

	def set_SnatEntryId(self, SnatEntryId):  # String
		self.add_query_param('SnatEntryId', SnatEntryId)
	def get_NatGatewayId(self): # String
		return self.get_query_params().get('NatGatewayId')

	def set_NatGatewayId(self, NatGatewayId):  # String
		self.add_query_param('NatGatewayId', NatGatewayId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_SnatTableId(self): # String
		return self.get_query_params().get('SnatTableId')

	def set_SnatTableId(self, SnatTableId):  # String
		self.add_query_param('SnatTableId', SnatTableId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SnatEntryName(self): # String
		return self.get_query_params().get('SnatEntryName')

	def set_SnatEntryName(self, SnatEntryName):  # String
		self.add_query_param('SnatEntryName', SnatEntryName)
