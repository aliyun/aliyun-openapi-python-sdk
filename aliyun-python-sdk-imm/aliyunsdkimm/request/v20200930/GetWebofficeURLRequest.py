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
from aliyunsdkimm.endpoint import endpoint_data
import json

class GetWebofficeURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'GetWebofficeURL','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Referer(self): # String
		return self.get_query_params().get('Referer')

	def set_Referer(self, Referer):  # String
		self.add_query_param('Referer', Referer)
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_Watermark(self): # Struct
		return self.get_query_params().get('Watermark')

	def set_Watermark(self, Watermark):  # Struct
		self.add_query_param("Watermark", json.dumps(Watermark))
	def get_NotifyTopicName(self): # String
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_query_param('NotifyTopicName', NotifyTopicName)
	def get_CachePreview(self): # Boolean
		return self.get_query_params().get('CachePreview')

	def set_CachePreview(self, CachePreview):  # Boolean
		self.add_query_param('CachePreview', CachePreview)
	def get_ExternalUploaded(self): # Boolean
		return self.get_query_params().get('ExternalUploaded')

	def set_ExternalUploaded(self, ExternalUploaded):  # Boolean
		self.add_query_param('ExternalUploaded', ExternalUploaded)
	def get_Permission(self): # Struct
		return self.get_query_params().get('Permission')

	def set_Permission(self, Permission):  # Struct
		self.add_query_param("Permission", json.dumps(Permission))
	def get_CredentialConfig(self): # Struct
		return self.get_query_params().get('CredentialConfig')

	def set_CredentialConfig(self, CredentialConfig):  # Struct
		self.add_query_param("CredentialConfig", json.dumps(CredentialConfig))
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_PreviewPages(self): # Long
		return self.get_query_params().get('PreviewPages')

	def set_PreviewPages(self, PreviewPages):  # Long
		self.add_query_param('PreviewPages', PreviewPages)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_Filename(self): # String
		return self.get_query_params().get('Filename')

	def set_Filename(self, Filename):  # String
		self.add_query_param('Filename', Filename)
	def get_Hidecmb(self): # Boolean
		return self.get_query_params().get('Hidecmb')

	def set_Hidecmb(self, Hidecmb):  # Boolean
		self.add_query_param('Hidecmb', Hidecmb)
	def get_SourceURI(self): # String
		return self.get_query_params().get('SourceURI')

	def set_SourceURI(self, SourceURI):  # String
		self.add_query_param('SourceURI', SourceURI)
	def get_NotifyEndpoint(self): # String
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self, NotifyEndpoint):  # String
		self.add_query_param('NotifyEndpoint', NotifyEndpoint)
	def get_User(self): # Struct
		return self.get_query_params().get('User')

	def set_User(self, User):  # Struct
		self.add_query_param("User", json.dumps(User))
