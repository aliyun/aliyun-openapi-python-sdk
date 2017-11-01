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
class ModifyForwardEntryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyForwardEntry','ecs')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

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

	def get_ForwardTableId(self):
		return self.get_query_params().get('ForwardTableId')

	def set_ForwardTableId(self,ForwardTableId):
		self.add_query_param('ForwardTableId',ForwardTableId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InternalIp(self):
		return self.get_query_params().get('InternalIp')

	def set_InternalIp(self,InternalIp):
		self.add_query_param('InternalIp',InternalIp)

	def get_ForwardEntryId(self):
		return self.get_query_params().get('ForwardEntryId')

	def set_ForwardEntryId(self,ForwardEntryId):
		self.add_query_param('ForwardEntryId',ForwardEntryId)

	def get_InternalPort(self):
		return self.get_query_params().get('InternalPort')

	def set_InternalPort(self,InternalPort):
		self.add_query_param('InternalPort',InternalPort)

	def get_ExternalIp(self):
		return self.get_query_params().get('ExternalIp')

	def set_ExternalIp(self,ExternalIp):
		self.add_query_param('ExternalIp',ExternalIp)

	def get_ExternalPort(self):
		return self.get_query_params().get('ExternalPort')

	def set_ExternalPort(self,ExternalPort):
		self.add_query_param('ExternalPort',ExternalPort)