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
class ExecContainerCommandRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eci', '2018-08-08', 'ExecContainerCommand','eci')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ContainerName(self):
		return self.get_query_params().get('ContainerName')

	def set_ContainerName(self,ContainerName):
		self.add_query_param('ContainerName',ContainerName)

	def get_ContainerGroupId(self):
		return self.get_query_params().get('ContainerGroupId')

	def set_ContainerGroupId(self,ContainerGroupId):
		self.add_query_param('ContainerGroupId',ContainerGroupId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Command(self):
		return self.get_query_params().get('Command')

	def set_Command(self, Command):
		self.add_query_param('Command', Command)

	def get_TTY(self):
		return self.get_query_params().get('TTY')

	def set_TTY(self, TTY):
		self.add_query_param('TTY', TTY)

	def get_Stdin(self):
		return self.get_query_params().get('Stdin')

	def set_Stdin(self, Stdin):
		self.add_query_param('Stdin', Stdin)

	def get_Sync(self):
		return self.get_query_params().get('Sync')

	def set_Sync(self, Sync):
		self.add_query_param('Sync', Sync)
