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

class CreateTransitRouterVpcAttachmentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'CreateTransitRouterVpcAttachment')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_VpcOwnerId(self): # Long
		return self.get_query_params().get('VpcOwnerId')

	def set_VpcOwnerId(self, VpcOwnerId):  # Long
		self.add_query_param('VpcOwnerId', VpcOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_CenId(self): # String
		return self.get_query_params().get('CenId')

	def set_CenId(self, CenId):  # String
		self.add_query_param('CenId', CenId)
	def get_TransitRouterAttachmentName(self): # String
		return self.get_query_params().get('TransitRouterAttachmentName')

	def set_TransitRouterAttachmentName(self, TransitRouterAttachmentName):  # String
		self.add_query_param('TransitRouterAttachmentName', TransitRouterAttachmentName)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_ZoneMappingss(self): # RepeatList
		return self.get_query_params().get('ZoneMappings')

	def set_ZoneMappingss(self, ZoneMappings):  # RepeatList
		for depth1 in range(len(ZoneMappings)):
			if ZoneMappings[depth1].get('VSwitchId') is not None:
				self.add_query_param('ZoneMappings.' + str(depth1 + 1) + '.VSwitchId', ZoneMappings[depth1].get('VSwitchId'))
			if ZoneMappings[depth1].get('ZoneId') is not None:
				self.add_query_param('ZoneMappings.' + str(depth1 + 1) + '.ZoneId', ZoneMappings[depth1].get('ZoneId'))
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
	def get_TransitRouterAttachmentDescription(self): # String
		return self.get_query_params().get('TransitRouterAttachmentDescription')

	def set_TransitRouterAttachmentDescription(self, TransitRouterAttachmentDescription):  # String
		self.add_query_param('TransitRouterAttachmentDescription', TransitRouterAttachmentDescription)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
