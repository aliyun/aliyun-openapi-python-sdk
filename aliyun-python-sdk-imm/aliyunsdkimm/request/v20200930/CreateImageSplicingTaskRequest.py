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

class CreateImageSplicingTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'CreateImageSplicingTask','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Padding(self): # Long
		return self.get_query_params().get('Padding')

	def set_Padding(self, Padding):  # Long
		self.add_query_param('Padding', Padding)
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_Margin(self): # Long
		return self.get_query_params().get('Margin')

	def set_Margin(self, Margin):  # Long
		self.add_query_param('Margin', Margin)
	def get_NotifyTopicName(self): # String
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_query_param('NotifyTopicName', NotifyTopicName)
	def get_Sources(self): # Array
		return self.get_query_params().get('Sources')

	def set_Sources(self, Sources):  # Array
		self.add_query_param("Sources", json.dumps(Sources))
	def get_CredentialConfig(self): # Struct
		return self.get_query_params().get('CredentialConfig')

	def set_CredentialConfig(self, CredentialConfig):  # Struct
		self.add_query_param("CredentialConfig", json.dumps(CredentialConfig))
	def get_Align(self): # Long
		return self.get_query_params().get('Align')

	def set_Align(self, Align):  # Long
		self.add_query_param('Align', Align)
	def get_Quality(self): # Long
		return self.get_query_params().get('Quality')

	def set_Quality(self, Quality):  # Long
		self.add_query_param('Quality', Quality)
	def get_BackgroundColor(self): # String
		return self.get_query_params().get('BackgroundColor')

	def set_BackgroundColor(self, BackgroundColor):  # String
		self.add_query_param('BackgroundColor', BackgroundColor)
	def get_Tags(self): # Map
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Map
		self.add_query_param("Tags", json.dumps(Tags))
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_NotifyEndpoint(self): # String
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self, NotifyEndpoint):  # String
		self.add_query_param('NotifyEndpoint', NotifyEndpoint)
	def get_TargetURI(self): # String
		return self.get_query_params().get('TargetURI')

	def set_TargetURI(self, TargetURI):  # String
		self.add_query_param('TargetURI', TargetURI)
	def get_ScaleType(self): # String
		return self.get_query_params().get('ScaleType')

	def set_ScaleType(self, ScaleType):  # String
		self.add_query_param('ScaleType', ScaleType)
	def get_ImageFormat(self): # String
		return self.get_query_params().get('ImageFormat')

	def set_ImageFormat(self, ImageFormat):  # String
		self.add_query_param('ImageFormat', ImageFormat)
	def get_Direction(self): # String
		return self.get_query_params().get('Direction')

	def set_Direction(self, Direction):  # String
		self.add_query_param('Direction', Direction)
