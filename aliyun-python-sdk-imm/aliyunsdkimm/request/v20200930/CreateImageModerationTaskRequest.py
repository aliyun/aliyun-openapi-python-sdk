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

class CreateImageModerationTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'CreateImageModerationTask','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_NotifyTopicName(self): # String
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_query_param('NotifyTopicName', NotifyTopicName)
	def get_NotifyEndpoint(self): # String
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self, NotifyEndpoint):  # String
		self.add_query_param('NotifyEndpoint', NotifyEndpoint)
	def get_SourceURI(self): # String
		return self.get_query_params().get('SourceURI')

	def set_SourceURI(self, SourceURI):  # String
		self.add_query_param('SourceURI', SourceURI)
	def get_Scenes(self): # Array
		return self.get_query_params().get('Scenes')

	def set_Scenes(self, Scenes):  # Array
		self.add_query_param("Scenes", json.dumps(Scenes))
	def get_MaxFrames(self): # Long
		return self.get_query_params().get('MaxFrames')

	def set_MaxFrames(self, MaxFrames):  # Long
		self.add_query_param('MaxFrames', MaxFrames)
	def get_Interval(self): # Long
		return self.get_query_params().get('Interval')

	def set_Interval(self, Interval):  # Long
		self.add_query_param('Interval', Interval)
	def get_CredentialConfig(self): # Struct
		return self.get_query_params().get('CredentialConfig')

	def set_CredentialConfig(self, CredentialConfig):  # Struct
		self.add_query_param("CredentialConfig", json.dumps(CredentialConfig))
	def get_Reviewer(self): # String
		return self.get_query_params().get('Reviewer')

	def set_Reviewer(self, Reviewer):  # String
		self.add_query_param('Reviewer', Reviewer)
	def get_Tags(self): # Map
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Map
		self.add_query_param("Tags", json.dumps(Tags))
