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
from aliyunsdkcbn.endpoint import endpoint_data

class ListTransitRouterRouteTablesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'ListTransitRouterRouteTables','cbn')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TransitRouterRouteTableNamess(self):
		return self.get_query_params().get('TransitRouterRouteTableNames')

	def set_TransitRouterRouteTableNamess(self, TransitRouterRouteTableNamess):
		for depth1 in range(len(TransitRouterRouteTableNamess)):
			if TransitRouterRouteTableNamess[depth1] is not None:
				self.add_query_param('TransitRouterRouteTableNames.' + str(depth1 + 1) , TransitRouterRouteTableNamess[depth1])

	def get_TransitRouterRouteTableType(self):
		return self.get_query_params().get('TransitRouterRouteTableType')

	def set_TransitRouterRouteTableType(self,TransitRouterRouteTableType):
		self.add_query_param('TransitRouterRouteTableType',TransitRouterRouteTableType)

	def get_TransitRouterRouteTableStatus(self):
		return self.get_query_params().get('TransitRouterRouteTableStatus')

	def set_TransitRouterRouteTableStatus(self,TransitRouterRouteTableStatus):
		self.add_query_param('TransitRouterRouteTableStatus',TransitRouterRouteTableStatus)

	def get_TransitRouterRouteTableIdss(self):
		return self.get_query_params().get('TransitRouterRouteTableIds')

	def set_TransitRouterRouteTableIdss(self, TransitRouterRouteTableIdss):
		for depth1 in range(len(TransitRouterRouteTableIdss)):
			if TransitRouterRouteTableIdss[depth1] is not None:
				self.add_query_param('TransitRouterRouteTableIds.' + str(depth1 + 1) , TransitRouterRouteTableIdss[depth1])

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TransitRouterId(self):
		return self.get_query_params().get('TransitRouterId')

	def set_TransitRouterId(self,TransitRouterId):
		self.add_query_param('TransitRouterId',TransitRouterId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)