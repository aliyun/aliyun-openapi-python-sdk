# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class Update2dAvatarRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'avatar', '2022-01-30', 'Update2dAvatar')
		self.set_method('POST')

	def get_Image(self): # String
		return self.get_query_params().get('Image')

	def set_Image(self, Image):  # String
		self.add_query_param('Image', Image)
	def get_Orientation(self): # Integer
		return self.get_query_params().get('Orientation')

	def set_Orientation(self, Orientation):  # Integer
		self.add_query_param('Orientation', Orientation)
	def get_Code(self): # String
		return self.get_query_params().get('Code')

	def set_Code(self, Code):  # String
		self.add_query_param('Code', Code)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Video(self): # String
		return self.get_query_params().get('Video')

	def set_Video(self, Video):  # String
		self.add_query_param('Video', Video)
	def get_Portrait(self): # String
		return self.get_query_params().get('Portrait')

	def set_Portrait(self, Portrait):  # String
		self.add_query_param('Portrait', Portrait)
	def get_Transparent(self): # Boolean
		return self.get_query_params().get('Transparent')

	def set_Transparent(self, Transparent):  # Boolean
		self.add_query_param('Transparent', Transparent)
	def get_TenantId(self): # Long
		return self.get_query_params().get('TenantId')

	def set_TenantId(self, TenantId):  # Long
		self.add_query_param('TenantId', TenantId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Callback(self): # Boolean
		return self.get_query_params().get('Callback')

	def set_Callback(self, Callback):  # Boolean
		self.add_query_param('Callback', Callback)
