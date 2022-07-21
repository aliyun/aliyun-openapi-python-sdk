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

class CreateStoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'CreateStory','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MinFileCount(self): # Long
		return self.get_body_params().get('MinFileCount')

	def set_MinFileCount(self, MinFileCount):  # Long
		self.add_body_params('MinFileCount', MinFileCount)
	def get_ProjectName(self): # String
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_body_params('ProjectName', ProjectName)
	def get_CustomLabels(self): # String
		return self.get_body_params().get('CustomLabels')

	def set_CustomLabels(self, CustomLabels):  # String
		self.add_body_params('CustomLabels', CustomLabels)
	def get_StoryStartTime(self): # String
		return self.get_body_params().get('StoryStartTime')

	def set_StoryStartTime(self, StoryStartTime):  # String
		self.add_body_params('StoryStartTime', StoryStartTime)
	def get_NotifyTopicName(self): # String
		return self.get_body_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_body_params('NotifyTopicName', NotifyTopicName)
	def get_StoryType(self): # String
		return self.get_body_params().get('StoryType')

	def set_StoryType(self, StoryType):  # String
		self.add_body_params('StoryType', StoryType)
	def get_CustomId(self): # String
		return self.get_body_params().get('CustomId')

	def set_CustomId(self, CustomId):  # String
		self.add_body_params('CustomId', CustomId)
	def get_Tags(self): # Map
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Map
		self.add_query_param("Tags", json.dumps(Tags))
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_NotifyEndpoint(self): # String
		return self.get_body_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self, NotifyEndpoint):  # String
		self.add_body_params('NotifyEndpoint', NotifyEndpoint)
	def get_MaxFileCount(self): # Long
		return self.get_body_params().get('MaxFileCount')

	def set_MaxFileCount(self, MaxFileCount):  # Long
		self.add_body_params('MaxFileCount', MaxFileCount)
	def get_StorySubType(self): # String
		return self.get_body_params().get('StorySubType')

	def set_StorySubType(self, StorySubType):  # String
		self.add_body_params('StorySubType', StorySubType)
	def get_DatasetName(self): # String
		return self.get_body_params().get('DatasetName')

	def set_DatasetName(self, DatasetName):  # String
		self.add_body_params('DatasetName', DatasetName)
	def get_StoryEndTime(self): # String
		return self.get_body_params().get('StoryEndTime')

	def set_StoryEndTime(self, StoryEndTime):  # String
		self.add_body_params('StoryEndTime', StoryEndTime)
	def get_ObjectId(self): # String
		return self.get_body_params().get('ObjectId')

	def set_ObjectId(self, ObjectId):  # String
		self.add_body_params('ObjectId', ObjectId)
	def get_StoryName(self): # String
		return self.get_body_params().get('StoryName')

	def set_StoryName(self, StoryName):  # String
		self.add_body_params('StoryName', StoryName)
