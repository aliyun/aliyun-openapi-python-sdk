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


	def get_VlanIdss(self):
		return self.get_query_params().get('VlanIds')

	def set_VlanIdss(self, VlanIdss):
		for depth1 in range(len(VlanIdss)):
			if VlanIdss[depth1] is not None:
				self.add_query_param('VlanIds.' + str(depth1 + 1) , VlanIdss[depth1])

	def get_VirtualPhysicalConnectionBusinessStatus(self):
		return self.get_query_params().get('VirtualPhysicalConnectionBusinessStatus')

	def set_VirtualPhysicalConnectionBusinessStatus(self,VirtualPhysicalConnectionBusinessStatus):
		self.add_query_param('VirtualPhysicalConnectionBusinessStatus',VirtualPhysicalConnectionBusinessStatus)

	def get_VirtualPhysicalConnectionAliUidss(self):
		return self.get_query_params().get('VirtualPhysicalConnectionAliUids')

	def set_VirtualPhysicalConnectionAliUidss(self, VirtualPhysicalConnectionAliUidss):
		for depth1 in range(len(VirtualPhysicalConnectionAliUidss)):
			if VirtualPhysicalConnectionAliUidss[depth1] is not None:
				self.add_query_param('VirtualPhysicalConnectionAliUids.' + str(depth1 + 1) , VirtualPhysicalConnectionAliUidss[depth1])

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_VirtualPhysicalConnectionIdss(self):
		return self.get_query_params().get('VirtualPhysicalConnectionIds')

	def set_VirtualPhysicalConnectionIdss(self, VirtualPhysicalConnectionIdss):
		for depth1 in range(len(VirtualPhysicalConnectionIdss)):
			if VirtualPhysicalConnectionIdss[depth1] is not None:
				self.add_query_param('VirtualPhysicalConnectionIds.' + str(depth1 + 1) , VirtualPhysicalConnectionIdss[depth1])

	def get_IsConfirmed(self):
		return self.get_query_params().get('IsConfirmed')

	def set_IsConfirmed(self,IsConfirmed):
		self.add_query_param('IsConfirmed',IsConfirmed)

	def get_VirtualPhysicalConnectionStatusess(self):
		return self.get_query_params().get('VirtualPhysicalConnectionStatuses')

	def set_VirtualPhysicalConnectionStatusess(self, VirtualPhysicalConnectionStatusess):
		for depth1 in range(len(VirtualPhysicalConnectionStatusess)):
			if VirtualPhysicalConnectionStatusess[depth1] is not None:
				self.add_query_param('VirtualPhysicalConnectionStatuses.' + str(depth1 + 1) , VirtualPhysicalConnectionStatusess[depth1])

	def get_PhysicalConnectionId(self):
		return self.get_query_params().get('PhysicalConnectionId')

	def set_PhysicalConnectionId(self,PhysicalConnectionId):
		self.add_query_param('PhysicalConnectionId',PhysicalConnectionId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)