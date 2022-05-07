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

class ListIpsecServersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ListIpsecServers','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_VpnGatewayId(self): # String
		return self.get_query_params().get('VpnGatewayId')

	def set_VpnGatewayId(self, VpnGatewayId):  # String
		self.add_query_param('VpnGatewayId', VpnGatewayId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_IpsecServerName(self): # String
		return self.get_query_params().get('IpsecServerName')

	def set_IpsecServerName(self, IpsecServerName):  # String
		self.add_query_param('IpsecServerName', IpsecServerName)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_IpsecServerIds(self): # RepeatList
		return self.get_query_params().get('IpsecServerId')

	def set_IpsecServerIds(self, IpsecServerId):  # RepeatList
		for depth1 in range(len(IpsecServerId)):
			self.add_query_param('IpsecServerId.' + str(depth1 + 1), IpsecServerId[depth1])
