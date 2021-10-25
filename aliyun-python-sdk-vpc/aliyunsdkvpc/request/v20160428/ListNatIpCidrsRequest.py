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

class ListNatIpCidrsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ListNatIpCidrs','vpc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NatIpCidrss(self):
		return self.get_query_params().get('NatIpCidrs')

	def set_NatIpCidrss(self, NatIpCidrss):
		for depth1 in range(len(NatIpCidrss)):
			if NatIpCidrss[depth1] is not None:
				self.add_query_param('NatIpCidrs.' + str(depth1 + 1) , NatIpCidrss[depth1])

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_NatGatewayId(self):
		return self.get_query_params().get('NatGatewayId')

	def set_NatGatewayId(self,NatGatewayId):
		self.add_query_param('NatGatewayId',NatGatewayId)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_NatIpCidrNames(self):
		return self.get_query_params().get('NatIpCidrName')

	def set_NatIpCidrNames(self, NatIpCidrNames):
		for depth1 in range(len(NatIpCidrNames)):
			if NatIpCidrNames[depth1] is not None:
				self.add_query_param('NatIpCidrName.' + str(depth1 + 1) , NatIpCidrNames[depth1])

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_NatIpCidr(self):
		return self.get_query_params().get('NatIpCidr')

	def set_NatIpCidr(self,NatIpCidr):
		self.add_query_param('NatIpCidr',NatIpCidr)

	def get_NatIpCidrStatus(self):
		return self.get_query_params().get('NatIpCidrStatus')

	def set_NatIpCidrStatus(self,NatIpCidrStatus):
		self.add_query_param('NatIpCidrStatus',NatIpCidrStatus)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)