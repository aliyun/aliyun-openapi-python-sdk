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
class CreatePhotoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'CreatePhoto','cloudphoto')
		self.set_protocol_type('https');

	def get_PhotoTitle(self):
		return self.get_query_params().get('PhotoTitle')

	def set_PhotoTitle(self,PhotoTitle):
		self.add_query_param('PhotoTitle',PhotoTitle)

	def get_LibraryId(self):
		return self.get_query_params().get('LibraryId')

	def set_LibraryId(self,LibraryId):
		self.add_query_param('LibraryId',LibraryId)

	def get_ShareExpireTime(self):
		return self.get_query_params().get('ShareExpireTime')

	def set_ShareExpireTime(self,ShareExpireTime):
		self.add_query_param('ShareExpireTime',ShareExpireTime)

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_UploadType(self):
		return self.get_query_params().get('UploadType')

	def set_UploadType(self,UploadType):
		self.add_query_param('UploadType',UploadType)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_SessionId(self):
		return self.get_query_params().get('SessionId')

	def set_SessionId(self,SessionId):
		self.add_query_param('SessionId',SessionId)

	def get_Staging(self):
		return self.get_query_params().get('Staging')

	def set_Staging(self,Staging):
		self.add_query_param('Staging',Staging)

	def get_FileId(self):
		return self.get_query_params().get('FileId')

	def set_FileId(self,FileId):
		self.add_query_param('FileId',FileId)