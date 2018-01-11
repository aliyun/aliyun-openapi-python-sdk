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
class RegisterPhotoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'RegisterPhoto','cloudphoto')
		self.set_protocol_type('https');

	def get_LibraryId(self):
		return self.get_query_params().get('LibraryId')

	def set_LibraryId(self,LibraryId):
		self.add_query_param('LibraryId',LibraryId)

	def get_Latitude(self):
		return self.get_query_params().get('Latitude')

	def set_Latitude(self,Latitude):
		self.add_query_param('Latitude',Latitude)

	def get_PhotoTitle(self):
		return self.get_query_params().get('PhotoTitle')

	def set_PhotoTitle(self,PhotoTitle):
		self.add_query_param('PhotoTitle',PhotoTitle)

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_IsVideo(self):
		return self.get_query_params().get('IsVideo')

	def set_IsVideo(self,IsVideo):
		self.add_query_param('IsVideo',IsVideo)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_Size(self):
		return self.get_query_params().get('Size')

	def set_Size(self,Size):
		self.add_query_param('Size',Size)

	def get_TakenAt(self):
		return self.get_query_params().get('TakenAt')

	def set_TakenAt(self,TakenAt):
		self.add_query_param('TakenAt',TakenAt)

	def get_Width(self):
		return self.get_query_params().get('Width')

	def set_Width(self,Width):
		self.add_query_param('Width',Width)

	def get_Location(self):
		return self.get_query_params().get('Location')

	def set_Location(self,Location):
		self.add_query_param('Location',Location)

	def get_Longitude(self):
		return self.get_query_params().get('Longitude')

	def set_Longitude(self,Longitude):
		self.add_query_param('Longitude',Longitude)

	def get_Height(self):
		return self.get_query_params().get('Height')

	def set_Height(self,Height):
		self.add_query_param('Height',Height)

	def get_Md5(self):
		return self.get_query_params().get('Md5')

	def set_Md5(self,Md5):
		self.add_query_param('Md5',Md5)