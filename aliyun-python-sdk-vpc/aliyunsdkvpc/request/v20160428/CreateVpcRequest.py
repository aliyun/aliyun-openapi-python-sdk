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

class CreateVpcRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateVpc','vpc')
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
	def get_EnableIpv6(self): # Boolean
		return self.get_query_params().get('EnableIpv6')

	def set_EnableIpv6(self, EnableIpv6):  # Boolean
		self.add_query_param('EnableIpv6', EnableIpv6)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Ipv4CidrMask(self): # Integer
		return self.get_query_params().get('Ipv4CidrMask')

	def set_Ipv4CidrMask(self, Ipv4CidrMask):  # Integer
		self.add_query_param('Ipv4CidrMask', Ipv4CidrMask)
	def get_VpcName(self): # String
		return self.get_query_params().get('VpcName')

	def set_VpcName(self, VpcName):  # String
		self.add_query_param('VpcName', VpcName)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Ipv4IpamPoolId(self): # String
		return self.get_query_params().get('Ipv4IpamPoolId')

	def set_Ipv4IpamPoolId(self, Ipv4IpamPoolId):  # String
		self.add_query_param('Ipv4IpamPoolId', Ipv4IpamPoolId)
	def get_Ipv6Isp(self): # String
		return self.get_query_params().get('Ipv6Isp')

	def set_Ipv6Isp(self, Ipv6Isp):  # String
		self.add_query_param('Ipv6Isp', Ipv6Isp)
	def get_UserCidr(self): # String
		return self.get_query_params().get('UserCidr')

	def set_UserCidr(self, UserCidr):  # String
		self.add_query_param('UserCidr', UserCidr)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_EnableDnsHostname(self): # Boolean
		return self.get_query_params().get('EnableDnsHostname')

	def set_EnableDnsHostname(self, EnableDnsHostname):  # Boolean
		self.add_query_param('EnableDnsHostname', EnableDnsHostname)
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
	def get_Ipv6CidrBlock(self): # String
		return self.get_query_params().get('Ipv6CidrBlock')

	def set_Ipv6CidrBlock(self, Ipv6CidrBlock):  # String
		self.add_query_param('Ipv6CidrBlock', Ipv6CidrBlock)
	def get_CidrBlock(self): # String
		return self.get_query_params().get('CidrBlock')

	def set_CidrBlock(self, CidrBlock):  # String
		self.add_query_param('CidrBlock', CidrBlock)
