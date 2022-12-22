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

class ListVirtualPhysicalConnectionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ListVirtualPhysicalConnections','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_VlanIdss(self): # RepeatList
		return self.get_query_params().get('VlanIds')

	def set_VlanIdss(self, VlanIds):  # RepeatList
		for depth1 in range(len(VlanIds)):
			self.add_query_param('VlanIds.' + str(depth1 + 1), VlanIds[depth1])
	def get_VirtualPhysicalConnectionBusinessStatus(self): # String
		return self.get_query_params().get('VirtualPhysicalConnectionBusinessStatus')

	def set_VirtualPhysicalConnectionBusinessStatus(self, VirtualPhysicalConnectionBusinessStatus):  # String
		self.add_query_param('VirtualPhysicalConnectionBusinessStatus', VirtualPhysicalConnectionBusinessStatus)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_VirtualPhysicalConnectionAliUidss(self): # RepeatList
		return self.get_query_params().get('VirtualPhysicalConnectionAliUids')

	def set_VirtualPhysicalConnectionAliUidss(self, VirtualPhysicalConnectionAliUids):  # RepeatList
		for depth1 in range(len(VirtualPhysicalConnectionAliUids)):
			self.add_query_param('VirtualPhysicalConnectionAliUids.' + str(depth1 + 1), VirtualPhysicalConnectionAliUids[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_VirtualPhysicalConnectionIdss(self): # RepeatList
		return self.get_query_params().get('VirtualPhysicalConnectionIds')

	def set_VirtualPhysicalConnectionIdss(self, VirtualPhysicalConnectionIds):  # RepeatList
		for depth1 in range(len(VirtualPhysicalConnectionIds)):
			self.add_query_param('VirtualPhysicalConnectionIds.' + str(depth1 + 1), VirtualPhysicalConnectionIds[depth1])
	def get_IsConfirmed(self): # Boolean
		return self.get_query_params().get('IsConfirmed')

	def set_IsConfirmed(self, IsConfirmed):  # Boolean
		self.add_query_param('IsConfirmed', IsConfirmed)
	def get_Tagss(self): # RepeatList
		return self.get_query_params().get('Tags')

	def set_Tagss(self, Tags):  # RepeatList
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
	def get_VirtualPhysicalConnectionStatusess(self): # RepeatList
		return self.get_query_params().get('VirtualPhysicalConnectionStatuses')

	def set_VirtualPhysicalConnectionStatusess(self, VirtualPhysicalConnectionStatuses):  # RepeatList
		for depth1 in range(len(VirtualPhysicalConnectionStatuses)):
			self.add_query_param('VirtualPhysicalConnectionStatuses.' + str(depth1 + 1), VirtualPhysicalConnectionStatuses[depth1])
	def get_PhysicalConnectionId(self): # String
		return self.get_query_params().get('PhysicalConnectionId')

	def set_PhysicalConnectionId(self, PhysicalConnectionId):  # String
		self.add_query_param('PhysicalConnectionId', PhysicalConnectionId)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
