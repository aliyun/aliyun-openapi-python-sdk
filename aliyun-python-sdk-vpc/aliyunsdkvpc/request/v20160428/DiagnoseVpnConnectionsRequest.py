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

class DiagnoseVpnConnectionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DiagnoseVpnConnections','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TunnelIdss(self): # RepeatList
		return self.get_query_params().get('TunnelIds')

	def set_TunnelIdss(self, TunnelIds):  # RepeatList
		for depth1 in range(len(TunnelIds)):
			self.add_query_param('TunnelIds.' + str(depth1 + 1), TunnelIds[depth1])
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_VpnGatewayId(self): # String
		return self.get_query_params().get('VpnGatewayId')

	def set_VpnGatewayId(self, VpnGatewayId):  # String
		self.add_query_param('VpnGatewayId', VpnGatewayId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_VpnConnectionIdss(self): # RepeatList
		return self.get_query_params().get('VpnConnectionIds')

	def set_VpnConnectionIdss(self, VpnConnectionIds):  # RepeatList
		for depth1 in range(len(VpnConnectionIds)):
			self.add_query_param('VpnConnectionIds.' + str(depth1 + 1), VpnConnectionIds[depth1])
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
