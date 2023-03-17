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

class CreateTransitRouteTableAggregationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'CreateTransitRouteTableAggregation')
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
	def get_TransitRouteTableAggregationDescription(self): # String
		return self.get_query_params().get('TransitRouteTableAggregationDescription')

	def set_TransitRouteTableAggregationDescription(self, TransitRouteTableAggregationDescription):  # String
		self.add_query_param('TransitRouteTableAggregationDescription', TransitRouteTableAggregationDescription)
	def get_TransitRouteTableAggregationName(self): # String
		return self.get_query_params().get('TransitRouteTableAggregationName')

	def set_TransitRouteTableAggregationName(self, TransitRouteTableAggregationName):  # String
		self.add_query_param('TransitRouteTableAggregationName', TransitRouteTableAggregationName)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_TransitRouteTableAggregationScope(self): # String
		return self.get_query_params().get('TransitRouteTableAggregationScope')

	def set_TransitRouteTableAggregationScope(self, TransitRouteTableAggregationScope):  # String
		self.add_query_param('TransitRouteTableAggregationScope', TransitRouteTableAggregationScope)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TransitRouteTableId(self): # String
		return self.get_query_params().get('TransitRouteTableId')

	def set_TransitRouteTableId(self, TransitRouteTableId):  # String
		self.add_query_param('TransitRouteTableId', TransitRouteTableId)
	def get_TransitRouteTableAggregationCidr(self): # String
		return self.get_query_params().get('TransitRouteTableAggregationCidr')

	def set_TransitRouteTableAggregationCidr(self, TransitRouteTableAggregationCidr):  # String
		self.add_query_param('TransitRouteTableAggregationCidr', TransitRouteTableAggregationCidr)
