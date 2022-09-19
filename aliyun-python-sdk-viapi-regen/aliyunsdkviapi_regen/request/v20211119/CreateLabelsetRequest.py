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
from aliyunsdkviapi_regen.endpoint import endpoint_data

class CreateLabelsetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'viapi-regen', '2021-11-19', 'CreateLabelset','selflearning')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_PreLabelId(self): # Long
		return self.get_body_params().get('PreLabelId')

	def set_PreLabelId(self, PreLabelId):  # Long
		self.add_body_params('PreLabelId', PreLabelId)
	def get_TagUserList(self): # String
		return self.get_body_params().get('TagUserList')

	def set_TagUserList(self, TagUserList):  # String
		self.add_body_params('TagUserList', TagUserList)
	def get_UserOssUrl(self): # String
		return self.get_body_params().get('UserOssUrl')

	def set_UserOssUrl(self, UserOssUrl):  # String
		self.add_body_params('UserOssUrl', UserOssUrl)
	def get_ObjectKey(self): # String
		return self.get_body_params().get('ObjectKey')

	def set_ObjectKey(self, ObjectKey):  # String
		self.add_body_params('ObjectKey', ObjectKey)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_DatasetId(self): # Long
		return self.get_body_params().get('DatasetId')

	def set_DatasetId(self, DatasetId):  # Long
		self.add_body_params('DatasetId', DatasetId)
	def get_TagSettings(self): # String
		return self.get_body_params().get('TagSettings')

	def set_TagSettings(self, TagSettings):  # String
		self.add_body_params('TagSettings', TagSettings)
