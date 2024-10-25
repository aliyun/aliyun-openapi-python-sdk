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

class ListFullNatEntriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ListFullNatEntries','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_NetworkInterfaceIdss(self): # RepeatList
		return self.get_query_params().get('NetworkInterfaceIds')

	def set_NetworkInterfaceIdss(self, NetworkInterfaceIds):  # RepeatList
		for depth1 in range(len(NetworkInterfaceIds)):
			self.add_query_param('NetworkInterfaceIds.' + str(depth1 + 1), NetworkInterfaceIds[depth1])
	def get_FullNatEntryId(self): # String
		return self.get_query_params().get('FullNatEntryId')

	def set_FullNatEntryId(self, FullNatEntryId):  # String
		self.add_query_param('FullNatEntryId', FullNatEntryId)
	def get_NatIpPort(self): # String
		return self.get_query_params().get('NatIpPort')

	def set_NatIpPort(self, NatIpPort):  # String
		self.add_query_param('NatIpPort', NatIpPort)
	def get_FullNatTableId(self): # String
		return self.get_query_params().get('FullNatTableId')

	def set_FullNatTableId(self, FullNatTableId):  # String
		self.add_query_param('FullNatTableId', FullNatTableId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_FullNatEntryNamess(self): # RepeatList
		return self.get_query_params().get('FullNatEntryNames')

	def set_FullNatEntryNamess(self, FullNatEntryNames):  # RepeatList
		for depth1 in range(len(FullNatEntryNames)):
			self.add_query_param('FullNatEntryNames.' + str(depth1 + 1), FullNatEntryNames[depth1])
	def get_NatGatewayId(self): # String
		return self.get_query_params().get('NatGatewayId')

	def set_NatGatewayId(self, NatGatewayId):  # String
		self.add_query_param('NatGatewayId', NatGatewayId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_IpProtocol(self): # String
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self, IpProtocol):  # String
		self.add_query_param('IpProtocol', IpProtocol)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_NatIp(self): # String
		return self.get_query_params().get('NatIp')

	def set_NatIp(self, NatIp):  # String
		self.add_query_param('NatIp', NatIp)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
