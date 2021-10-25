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


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_NetworkInterfaceIdss(self):
		return self.get_query_params().get('NetworkInterfaceIds')

	def set_NetworkInterfaceIdss(self, NetworkInterfaceIdss):
		for depth1 in range(len(NetworkInterfaceIdss)):
			if NetworkInterfaceIdss[depth1] is not None:
				self.add_query_param('NetworkInterfaceIds.' + str(depth1 + 1) , NetworkInterfaceIdss[depth1])

	def get_FullNatEntryStatus(self):
		return self.get_query_params().get('FullNatEntryStatus')

	def set_FullNatEntryStatus(self,FullNatEntryStatus):
		self.add_query_param('FullNatEntryStatus',FullNatEntryStatus)

	def get_FullNatEntryId(self):
		return self.get_query_params().get('FullNatEntryId')

	def set_FullNatEntryId(self,FullNatEntryId):
		self.add_query_param('FullNatEntryId',FullNatEntryId)

	def get_FullNatTableId(self):
		return self.get_query_params().get('FullNatTableId')

	def set_FullNatTableId(self,FullNatTableId):
		self.add_query_param('FullNatTableId',FullNatTableId)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_FullNatEntryNamess(self):
		return self.get_query_params().get('FullNatEntryNames')

	def set_FullNatEntryNamess(self, FullNatEntryNamess):
		for depth1 in range(len(FullNatEntryNamess)):
			if FullNatEntryNamess[depth1] is not None:
				self.add_query_param('FullNatEntryNames.' + str(depth1 + 1) , FullNatEntryNamess[depth1])

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_IpProtocol(self):
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self,IpProtocol):
		self.add_query_param('IpProtocol',IpProtocol)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)