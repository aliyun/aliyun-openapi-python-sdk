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
class ModifyImageSharePermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyImageSharePermission')

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

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_AddAccount1(self):
		return self.get_query_params().get('AddAccount.1')

	def set_AddAccount1(self,AddAccount1):
		self.add_query_param('AddAccount.1',AddAccount1)

	def get_AddAccount2(self):
		return self.get_query_params().get('AddAccount.2')

	def set_AddAccount2(self,AddAccount2):
		self.add_query_param('AddAccount.2',AddAccount2)

	def get_AddAccount3(self):
		return self.get_query_params().get('AddAccount.3')

	def set_AddAccount3(self,AddAccount3):
		self.add_query_param('AddAccount.3',AddAccount3)

	def get_AddAccount4(self):
		return self.get_query_params().get('AddAccount.4')

	def set_AddAccount4(self,AddAccount4):
		self.add_query_param('AddAccount.4',AddAccount4)

	def get_AddAccount5(self):
		return self.get_query_params().get('AddAccount.5')

	def set_AddAccount5(self,AddAccount5):
		self.add_query_param('AddAccount.5',AddAccount5)

	def get_AddAccount6(self):
		return self.get_query_params().get('AddAccount.6')

	def set_AddAccount6(self,AddAccount6):
		self.add_query_param('AddAccount.6',AddAccount6)

	def get_AddAccount7(self):
		return self.get_query_params().get('AddAccount.7')

	def set_AddAccount7(self,AddAccount7):
		self.add_query_param('AddAccount.7',AddAccount7)

	def get_AddAccount8(self):
		return self.get_query_params().get('AddAccount.8')

	def set_AddAccount8(self,AddAccount8):
		self.add_query_param('AddAccount.8',AddAccount8)

	def get_AddAccount9(self):
		return self.get_query_params().get('AddAccount.9')

	def set_AddAccount9(self,AddAccount9):
		self.add_query_param('AddAccount.9',AddAccount9)

	def get_AddAccount10(self):
		return self.get_query_params().get('AddAccount.10')

	def set_AddAccount10(self,AddAccount10):
		self.add_query_param('AddAccount.10',AddAccount10)

	def get_RemoveAccount1(self):
		return self.get_query_params().get('RemoveAccount.1')

	def set_RemoveAccount1(self,RemoveAccount1):
		self.add_query_param('RemoveAccount.1',RemoveAccount1)

	def get_RemoveAccount2(self):
		return self.get_query_params().get('RemoveAccount.2')

	def set_RemoveAccount2(self,RemoveAccount2):
		self.add_query_param('RemoveAccount.2',RemoveAccount2)

	def get_RemoveAccount3(self):
		return self.get_query_params().get('RemoveAccount.3')

	def set_RemoveAccount3(self,RemoveAccount3):
		self.add_query_param('RemoveAccount.3',RemoveAccount3)

	def get_RemoveAccount4(self):
		return self.get_query_params().get('RemoveAccount.4')

	def set_RemoveAccount4(self,RemoveAccount4):
		self.add_query_param('RemoveAccount.4',RemoveAccount4)

	def get_RemoveAccount5(self):
		return self.get_query_params().get('RemoveAccount.5')

	def set_RemoveAccount5(self,RemoveAccount5):
		self.add_query_param('RemoveAccount.5',RemoveAccount5)

	def get_RemoveAccount6(self):
		return self.get_query_params().get('RemoveAccount.6')

	def set_RemoveAccount6(self,RemoveAccount6):
		self.add_query_param('RemoveAccount.6',RemoveAccount6)

	def get_RemoveAccount7(self):
		return self.get_query_params().get('RemoveAccount.7')

	def set_RemoveAccount7(self,RemoveAccount7):
		self.add_query_param('RemoveAccount.7',RemoveAccount7)

	def get_RemoveAccount8(self):
		return self.get_query_params().get('RemoveAccount.8')

	def set_RemoveAccount8(self,RemoveAccount8):
		self.add_query_param('RemoveAccount.8',RemoveAccount8)

	def get_RemoveAccount9(self):
		return self.get_query_params().get('RemoveAccount.9')

	def set_RemoveAccount9(self,RemoveAccount9):
		self.add_query_param('RemoveAccount.9',RemoveAccount9)

	def get_RemoveAccount10(self):
		return self.get_query_params().get('RemoveAccount.10')

	def set_RemoveAccount10(self,RemoveAccount10):
		self.add_query_param('RemoveAccount.10',RemoveAccount10)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)