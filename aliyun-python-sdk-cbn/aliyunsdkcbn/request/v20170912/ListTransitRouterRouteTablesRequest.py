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
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'ListTransitRouterRouteTables')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_TransitRouterRouteTableNamess(self): # RepeatList
		return self.get_query_params().get('TransitRouterRouteTableNames')

	def set_TransitRouterRouteTableNamess(self, TransitRouterRouteTableNames):  # RepeatList
		for depth1 in range(len(TransitRouterRouteTableNames)):
			self.add_query_param('TransitRouterRouteTableNames.' + str(depth1 + 1), TransitRouterRouteTableNames[depth1])
	def get_TransitRouterRouteTableType(self): # String
		return self.get_query_params().get('TransitRouterRouteTableType')

	def set_TransitRouterRouteTableType(self, TransitRouterRouteTableType):  # String
		self.add_query_param('TransitRouterRouteTableType', TransitRouterRouteTableType)
	def get_TransitRouterRouteTableStatus(self): # String
		return self.get_query_params().get('TransitRouterRouteTableStatus')

	def set_TransitRouterRouteTableStatus(self, TransitRouterRouteTableStatus):  # String
		self.add_query_param('TransitRouterRouteTableStatus', TransitRouterRouteTableStatus)
	def get_TransitRouterRouteTableIdss(self): # RepeatList
		return self.get_query_params().get('TransitRouterRouteTableIds')

	def set_TransitRouterRouteTableIdss(self, TransitRouterRouteTableIds):  # RepeatList
		for depth1 in range(len(TransitRouterRouteTableIds)):
			self.add_query_param('TransitRouterRouteTableIds.' + str(depth1 + 1), TransitRouterRouteTableIds[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
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
	def get_TransitRouterId(self): # String
		return self.get_query_params().get('TransitRouterId')

	def set_TransitRouterId(self, TransitRouterId):  # String
		self.add_query_param('TransitRouterId', TransitRouterId)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
