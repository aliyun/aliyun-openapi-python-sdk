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
class CreateSAGLinkLevelHaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'CreateSAGLinkLevelHa','smartag')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_BackupLinkId(self):
		return self.get_query_params().get('BackupLinkId')

	def set_BackupLinkId(self,BackupLinkId):
		self.add_query_param('BackupLinkId',BackupLinkId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_HaType(self):
		return self.get_query_params().get('HaType')

	def set_HaType(self,HaType):
		self.add_query_param('HaType',HaType)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_MainLinkRegionId(self):
		return self.get_query_params().get('MainLinkRegionId')

	def set_MainLinkRegionId(self,MainLinkRegionId):
		self.add_query_param('MainLinkRegionId',MainLinkRegionId)

	def get_SmartAGId(self):
		return self.get_query_params().get('SmartAGId')

	def set_SmartAGId(self,SmartAGId):
		self.add_query_param('SmartAGId',SmartAGId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_MainLinkId(self):
		return self.get_query_params().get('MainLinkId')

	def set_MainLinkId(self,MainLinkId):
		self.add_query_param('MainLinkId',MainLinkId)

	def get_BackupLinkRegionId(self):
		return self.get_query_params().get('BackupLinkRegionId')

	def set_BackupLinkRegionId(self,BackupLinkRegionId):
		self.add_query_param('BackupLinkRegionId',BackupLinkRegionId)