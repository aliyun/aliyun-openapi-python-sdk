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

class RevokeSecurityGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'RevokeSecurityGroup','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NicType(self):
		return self.get_query_params().get('NicType')

	def set_NicType(self,NicType):
		self.add_query_param('NicType',NicType)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SourcePortRange(self):
		return self.get_query_params().get('SourcePortRange')

	def set_SourcePortRange(self,SourcePortRange):
		self.add_query_param('SourcePortRange',SourcePortRange)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_SourceGroupOwnerId(self):
		return self.get_query_params().get('SourceGroupOwnerId')

	def set_SourceGroupOwnerId(self,SourceGroupOwnerId):
		self.add_query_param('SourceGroupOwnerId',SourceGroupOwnerId)

	def get_SourceGroupOwnerAccount(self):
		return self.get_query_params().get('SourceGroupOwnerAccount')

	def set_SourceGroupOwnerAccount(self,SourceGroupOwnerAccount):
		self.add_query_param('SourceGroupOwnerAccount',SourceGroupOwnerAccount)

	def get_Ipv6DestCidrIp(self):
		return self.get_query_params().get('Ipv6DestCidrIp')

	def set_Ipv6DestCidrIp(self,Ipv6DestCidrIp):
		self.add_query_param('Ipv6DestCidrIp',Ipv6DestCidrIp)

	def get_Ipv6SourceCidrIp(self):
		return self.get_query_params().get('Ipv6SourceCidrIp')

	def set_Ipv6SourceCidrIp(self,Ipv6SourceCidrIp):
		self.add_query_param('Ipv6SourceCidrIp',Ipv6SourceCidrIp)

	def get_Policy(self):
		return self.get_query_params().get('Policy')

	def set_Policy(self,Policy):
		self.add_query_param('Policy',Policy)

	def get_PortRange(self):
		return self.get_query_params().get('PortRange')

	def set_PortRange(self,PortRange):
		self.add_query_param('PortRange',PortRange)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_IpProtocol(self):
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self,IpProtocol):
		self.add_query_param('IpProtocol',IpProtocol)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_SourceCidrIp(self):
		return self.get_query_params().get('SourceCidrIp')

	def set_SourceCidrIp(self,SourceCidrIp):
		self.add_query_param('SourceCidrIp',SourceCidrIp)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_DestCidrIp(self):
		return self.get_query_params().get('DestCidrIp')

	def set_DestCidrIp(self,DestCidrIp):
		self.add_query_param('DestCidrIp',DestCidrIp)

	def get_SourceGroupId(self):
		return self.get_query_params().get('SourceGroupId')

	def set_SourceGroupId(self,SourceGroupId):
		self.add_query_param('SourceGroupId',SourceGroupId)