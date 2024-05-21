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
class EditPhotosRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'EditPhotos','cloudphoto')
		self.set_protocol_type('https');

	def get_TakenAt(self):
		return self.get_query_params().get('TakenAt')

	def set_TakenAt(self,TakenAt):
		self.add_query_param('TakenAt',TakenAt)

	def get_LibraryId(self):
		return self.get_query_params().get('LibraryId')

	def set_LibraryId(self,LibraryId):
		self.add_query_param('LibraryId',LibraryId)

	def get_ShareExpireTime(self):
		return self.get_query_params().get('ShareExpireTime')

	def set_ShareExpireTime(self,ShareExpireTime):
		self.add_query_param('ShareExpireTime',ShareExpireTime)

	def get_PhotoIds(self):
		return self.get_query_params().get('PhotoIds')

	def set_PhotoIds(self,PhotoIds):
		for i in range(len(PhotoIds)):	
			if PhotoIds[i] is not None:
				self.add_query_param('PhotoId.' + str(i + 1) , PhotoIds[i]);

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)