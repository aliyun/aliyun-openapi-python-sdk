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
import json

class CreateNatGatewayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateNatGateway','vpc')
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
	def get_SecurityProtectionEnabled(self): # Boolean
		return self.get_query_params().get('SecurityProtectionEnabled')

	def set_SecurityProtectionEnabled(self, SecurityProtectionEnabled):  # Boolean
		self.add_query_param('SecurityProtectionEnabled', SecurityProtectionEnabled)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_NetworkType(self): # String
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self, NetworkType):  # String
		self.add_query_param('NetworkType', NetworkType)
	def get_Spec(self): # String
		return self.get_query_params().get('Spec')

	def set_Spec(self, Spec):  # String
		self.add_query_param('Spec', Spec)
	def get_Duration(self): # String
		return self.get_query_params().get('Duration')

	def set_Duration(self, Duration):  # String
		self.add_query_param('Duration', Duration)
	def get_IcmpReplyEnabled(self): # Boolean
		return self.get_query_params().get('IcmpReplyEnabled')

	def set_IcmpReplyEnabled(self, IcmpReplyEnabled):  # Boolean
		self.add_query_param('IcmpReplyEnabled', IcmpReplyEnabled)
	def get_NatType(self): # String
		return self.get_query_params().get('NatType')

	def set_NatType(self, NatType):  # String
		self.add_query_param('NatType', NatType)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
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
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_PrivateLinkEnabled(self): # Boolean
		return self.get_query_params().get('PrivateLinkEnabled')

	def set_PrivateLinkEnabled(self, PrivateLinkEnabled):  # Boolean
		self.add_query_param('PrivateLinkEnabled', PrivateLinkEnabled)
	def get_EipBindMode(self): # String
		return self.get_query_params().get('EipBindMode')

	def set_EipBindMode(self, EipBindMode):  # String
		self.add_query_param('EipBindMode', EipBindMode)
	def get_PricingCycle(self): # String
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self, PricingCycle):  # String
		self.add_query_param('PricingCycle', PricingCycle)
	def get_AccessMode(self): # Struct
		return self.get_query_params().get('AccessMode')

	def set_AccessMode(self, AccessMode):  # Struct
		self.add_query_param("AccessMode", json.dumps(AccessMode))
