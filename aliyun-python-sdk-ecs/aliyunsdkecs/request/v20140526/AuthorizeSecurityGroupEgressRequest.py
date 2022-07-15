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
from aliyunsdkecs.endpoint import endpoint_data

class AuthorizeSecurityGroupEgressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'AuthorizeSecurityGroupEgress','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NicType(self): # String
		return self.get_query_params().get('NicType')

	def set_NicType(self, NicType):  # String
		self.add_query_param('NicType', NicType)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_SourcePortRange(self): # String
		return self.get_query_params().get('SourcePortRange')

	def set_SourcePortRange(self, SourcePortRange):  # String
		self.add_query_param('SourcePortRange', SourcePortRange)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_DestPrefixListId(self): # String
		return self.get_query_params().get('DestPrefixListId')

	def set_DestPrefixListId(self, DestPrefixListId):  # String
		self.add_query_param('DestPrefixListId', DestPrefixListId)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Permissions(self): # Array
		return self.get_query_params().get('Permissions')

	def set_Permissions(self, Permissions):  # Array
		for index1, value1 in enumerate(Permissions):
			if value1.get('Policy') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.Policy', value1.get('Policy'))
			if value1.get('Priority') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.Priority', value1.get('Priority'))
			if value1.get('IpProtocol') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.IpProtocol', value1.get('IpProtocol'))
			if value1.get('DestCidrIp') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.DestCidrIp', value1.get('DestCidrIp'))
			if value1.get('Ipv6DestCidrIp') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.Ipv6DestCidrIp', value1.get('Ipv6DestCidrIp'))
			if value1.get('DestGroupId') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.DestGroupId', value1.get('DestGroupId'))
			if value1.get('DestPrefixListId') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.DestPrefixListId', value1.get('DestPrefixListId'))
			if value1.get('PortRange') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.PortRange', value1.get('PortRange'))
			if value1.get('SourceCidrIp') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.SourceCidrIp', value1.get('SourceCidrIp'))
			if value1.get('Ipv6SourceCidrIp') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.Ipv6SourceCidrIp', value1.get('Ipv6SourceCidrIp'))
			if value1.get('SourcePortRange') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.SourcePortRange', value1.get('SourcePortRange'))
			if value1.get('DestGroupOwnerAccount') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.DestGroupOwnerAccount', value1.get('DestGroupOwnerAccount'))
			if value1.get('DestGroupOwnerId') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.DestGroupOwnerId', value1.get('DestGroupOwnerId'))
			if value1.get('NicType') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.NicType', value1.get('NicType'))
			if value1.get('Description') is not None:
				self.add_query_param('Permissions.' + str(index1 + 1) + '.Description', value1.get('Description'))
	def get_Policy(self): # String
		return self.get_query_params().get('Policy')

	def set_Policy(self, Policy):  # String
		self.add_query_param('Policy', Policy)
	def get_Ipv6DestCidrIp(self): # String
		return self.get_query_params().get('Ipv6DestCidrIp')

	def set_Ipv6DestCidrIp(self, Ipv6DestCidrIp):  # String
		self.add_query_param('Ipv6DestCidrIp', Ipv6DestCidrIp)
	def get_Ipv6SourceCidrIp(self): # String
		return self.get_query_params().get('Ipv6SourceCidrIp')

	def set_Ipv6SourceCidrIp(self, Ipv6SourceCidrIp):  # String
		self.add_query_param('Ipv6SourceCidrIp', Ipv6SourceCidrIp)
	def get_PortRange(self): # String
		return self.get_query_params().get('PortRange')

	def set_PortRange(self, PortRange):  # String
		self.add_query_param('PortRange', PortRange)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_IpProtocol(self): # String
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self, IpProtocol):  # String
		self.add_query_param('IpProtocol', IpProtocol)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_SourceCidrIp(self): # String
		return self.get_query_params().get('SourceCidrIp')

	def set_SourceCidrIp(self, SourceCidrIp):  # String
		self.add_query_param('SourceCidrIp', SourceCidrIp)
	def get_DestGroupId(self): # String
		return self.get_query_params().get('DestGroupId')

	def set_DestGroupId(self, DestGroupId):  # String
		self.add_query_param('DestGroupId', DestGroupId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Priority(self): # String
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # String
		self.add_query_param('Priority', Priority)
	def get_DestGroupOwnerAccount(self): # String
		return self.get_query_params().get('DestGroupOwnerAccount')

	def set_DestGroupOwnerAccount(self, DestGroupOwnerAccount):  # String
		self.add_query_param('DestGroupOwnerAccount', DestGroupOwnerAccount)
	def get_DestCidrIp(self): # String
		return self.get_query_params().get('DestCidrIp')

	def set_DestCidrIp(self, DestCidrIp):  # String
		self.add_query_param('DestCidrIp', DestCidrIp)
	def get_DestGroupOwnerId(self): # Long
		return self.get_query_params().get('DestGroupOwnerId')

	def set_DestGroupOwnerId(self, DestGroupOwnerId):  # Long
		self.add_query_param('DestGroupOwnerId', DestGroupOwnerId)
