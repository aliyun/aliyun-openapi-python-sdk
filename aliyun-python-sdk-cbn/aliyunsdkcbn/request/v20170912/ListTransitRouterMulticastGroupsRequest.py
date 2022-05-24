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

class ListTransitRouterMulticastGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'ListTransitRouterMulticastGroups')
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
	def get_VSwitchIdss(self): # RepeatList
		return self.get_query_params().get('VSwitchIds')

	def set_VSwitchIdss(self, VSwitchIds):  # RepeatList
		for depth1 in range(len(VSwitchIds)):
			self.add_query_param('VSwitchIds.' + str(depth1 + 1), VSwitchIds[depth1])
	def get_TransitRouterMulticastDomainId(self): # String
		return self.get_query_params().get('TransitRouterMulticastDomainId')

	def set_TransitRouterMulticastDomainId(self, TransitRouterMulticastDomainId):  # String
		self.add_query_param('TransitRouterMulticastDomainId', TransitRouterMulticastDomainId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_GroupIpAddress(self): # String
		return self.get_query_params().get('GroupIpAddress')

	def set_GroupIpAddress(self, GroupIpAddress):  # String
		self.add_query_param('GroupIpAddress', GroupIpAddress)
	def get_ResourceId(self): # String
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_query_param('ResourceId', ResourceId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_PeerTransitRouterMulticastDomainss(self): # RepeatList
		return self.get_query_params().get('PeerTransitRouterMulticastDomains')

	def set_PeerTransitRouterMulticastDomainss(self, PeerTransitRouterMulticastDomains):  # RepeatList
		for depth1 in range(len(PeerTransitRouterMulticastDomains)):
			self.add_query_param('PeerTransitRouterMulticastDomains.' + str(depth1 + 1), PeerTransitRouterMulticastDomains[depth1])
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_TransitRouterAttachmentId(self): # String
		return self.get_query_params().get('TransitRouterAttachmentId')

	def set_TransitRouterAttachmentId(self, TransitRouterAttachmentId):  # String
		self.add_query_param('TransitRouterAttachmentId', TransitRouterAttachmentId)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
