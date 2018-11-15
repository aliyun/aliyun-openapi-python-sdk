# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ValidateSecurityGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ValidateSecurityGroup','ecs')

	def get_NicType(self):
		return self.get_query_params().get('NicType')

	def set_NicType(self,NicType):
		self.add_query_param('NicType',NicType)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SourcePort(self):
		return self.get_query_params().get('SourcePort')

	def set_SourcePort(self,SourcePort):
		self.add_query_param('SourcePort',SourcePort)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_Direction(self):
		return self.get_query_params().get('Direction')

	def set_Direction(self,Direction):
		self.add_query_param('Direction',Direction)

	def get_DestIp(self):
		return self.get_query_params().get('DestIp')

	def set_DestIp(self,DestIp):
		self.add_query_param('DestIp',DestIp)

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

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_DestPort(self):
		return self.get_query_params().get('DestPort')

	def set_DestPort(self,DestPort):
		self.add_query_param('DestPort',DestPort)