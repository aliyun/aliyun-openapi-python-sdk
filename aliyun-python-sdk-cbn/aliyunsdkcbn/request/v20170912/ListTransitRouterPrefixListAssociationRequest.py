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

class ListTransitRouterPrefixListAssociationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'ListTransitRouterPrefixListAssociation')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_NextHopInstanceId(self): # String
		return self.get_query_params().get('NextHopInstanceId')

	def set_NextHopInstanceId(self, NextHopInstanceId):  # String
		self.add_query_param('NextHopInstanceId', NextHopInstanceId)
	def get_PrefixListId(self): # String
		return self.get_query_params().get('PrefixListId')

	def set_PrefixListId(self, PrefixListId):  # String
		self.add_query_param('PrefixListId', PrefixListId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_OwnerUid(self): # Long
		return self.get_query_params().get('OwnerUid')

	def set_OwnerUid(self, OwnerUid):  # Long
		self.add_query_param('OwnerUid', OwnerUid)
	def get_NextHopType(self): # String
		return self.get_query_params().get('NextHopType')

	def set_NextHopType(self, NextHopType):  # String
		self.add_query_param('NextHopType', NextHopType)
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
	def get_TransitRouterTableId(self): # String
		return self.get_query_params().get('TransitRouterTableId')

	def set_TransitRouterTableId(self, TransitRouterTableId):  # String
		self.add_query_param('TransitRouterTableId', TransitRouterTableId)
	def get_NextHop(self): # String
		return self.get_query_params().get('NextHop')

	def set_NextHop(self, NextHop):  # String
		self.add_query_param('NextHop', NextHop)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
