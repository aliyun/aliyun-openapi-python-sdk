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
class CreateUisNodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Uis', '2018-08-21', 'CreateUisNode','uis')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_UisNodeBandwidth(self):
		return self.get_query_params().get('UisNodeBandwidth')

	def set_UisNodeBandwidth(self,UisNodeBandwidth):
		self.add_query_param('UisNodeBandwidth',UisNodeBandwidth)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_UisNodeAreaId(self):
		return self.get_query_params().get('UisNodeAreaId')

	def set_UisNodeAreaId(self,UisNodeAreaId):
		self.add_query_param('UisNodeAreaId',UisNodeAreaId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_UisId(self):
		return self.get_query_params().get('UisId')

	def set_UisId(self,UisId):
		self.add_query_param('UisId',UisId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_IpAddrsNum(self):
		return self.get_query_params().get('IpAddrsNum')

	def set_IpAddrsNum(self,IpAddrsNum):
		self.add_query_param('IpAddrsNum',IpAddrsNum)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)