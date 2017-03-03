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
class ModifyDiskAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyDiskAttribute')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DiskId(self):
		return self.get_query_params().get('DiskId')

	def set_DiskId(self,DiskId):
		self.add_query_param('DiskId',DiskId)

	def get_DiskName(self):
		return self.get_query_params().get('DiskName')

	def set_DiskName(self,DiskName):
		self.add_query_param('DiskName',DiskName)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_DeleteWithInstance(self):
		return self.get_query_params().get('DeleteWithInstance')

	def set_DeleteWithInstance(self,DeleteWithInstance):
		self.add_query_param('DeleteWithInstance',DeleteWithInstance)

	def get_DeleteAutoSnapshot(self):
		return self.get_query_params().get('DeleteAutoSnapshot')

	def set_DeleteAutoSnapshot(self,DeleteAutoSnapshot):
		self.add_query_param('DeleteAutoSnapshot',DeleteAutoSnapshot)

	def get_EnableAutoSnapshot(self):
		return self.get_query_params().get('EnableAutoSnapshot')

	def set_EnableAutoSnapshot(self,EnableAutoSnapshot):
		self.add_query_param('EnableAutoSnapshot',EnableAutoSnapshot)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)