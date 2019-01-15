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
class UploadMediaByURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'UploadMediaByURL','vod')

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TemplateGroupId(self):
		return self.get_query_params().get('TemplateGroupId')

	def set_TemplateGroupId(self,TemplateGroupId):
		self.add_query_param('TemplateGroupId',TemplateGroupId)

	def get_UploadMetadatas(self):
		return self.get_query_params().get('UploadMetadatas')

	def set_UploadMetadatas(self,UploadMetadatas):
		self.add_query_param('UploadMetadatas',UploadMetadatas)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_UploadURLs(self):
		return self.get_query_params().get('UploadURLs')

	def set_UploadURLs(self,UploadURLs):
		self.add_query_param('UploadURLs',UploadURLs)

	def get_MessageCallback(self):
		return self.get_query_params().get('MessageCallback')

	def set_MessageCallback(self,MessageCallback):
		self.add_query_param('MessageCallback',MessageCallback)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_StorageLocation(self):
		return self.get_query_params().get('StorageLocation')

	def set_StorageLocation(self,StorageLocation):
		self.add_query_param('StorageLocation',StorageLocation)