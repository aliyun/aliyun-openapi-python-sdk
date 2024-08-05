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
from aliyunsdkarms.endpoint import endpoint_data
import json

class CreateGrafanaWorkspaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'CreateGrafanaWorkspace','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AliyunLang(self): # String
		return self.get_query_params().get('AliyunLang')

	def set_AliyunLang(self, AliyunLang):  # String
		self.add_query_param('AliyunLang', AliyunLang)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_GrafanaWorkspaceName(self): # String
		return self.get_query_params().get('GrafanaWorkspaceName')

	def set_GrafanaWorkspaceName(self, GrafanaWorkspaceName):  # String
		self.add_query_param('GrafanaWorkspaceName', GrafanaWorkspaceName)
	def get_Tags(self): # Array
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Array
		self.add_query_param("Tags", json.dumps(Tags))
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_GrafanaVersion(self): # String
		return self.get_query_params().get('GrafanaVersion')

	def set_GrafanaVersion(self, GrafanaVersion):  # String
		self.add_query_param('GrafanaVersion', GrafanaVersion)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_GrafanaWorkspaceEdition(self): # String
		return self.get_query_params().get('GrafanaWorkspaceEdition')

	def set_GrafanaWorkspaceEdition(self, GrafanaWorkspaceEdition):  # String
		self.add_query_param('GrafanaWorkspaceEdition', GrafanaWorkspaceEdition)
