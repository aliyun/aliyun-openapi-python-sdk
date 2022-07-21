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

class UpdateStoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'UpdateStory','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Cover(self): # Struct
		return self.get_body_params().get('Cover')

	def set_Cover(self, Cover):  # Struct
		self.add_body_params("Cover", json.dumps(Cover))
	def get_ProjectName(self): # String
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_body_params('ProjectName', ProjectName)
	def get_CustomLabels(self): # String
		return self.get_body_params().get('CustomLabels')

	def set_CustomLabels(self, CustomLabels):  # String
		self.add_body_params('CustomLabels', CustomLabels)
	def get_DatasetName(self): # String
		return self.get_body_params().get('DatasetName')

	def set_DatasetName(self, DatasetName):  # String
		self.add_body_params('DatasetName', DatasetName)
	def get_CustomId(self): # String
		return self.get_body_params().get('CustomId')

	def set_CustomId(self, CustomId):  # String
		self.add_body_params('CustomId', CustomId)
	def get_ObjectId(self): # String
		return self.get_body_params().get('ObjectId')

	def set_ObjectId(self, ObjectId):  # String
		self.add_body_params('ObjectId', ObjectId)
	def get_StoryName(self): # String
		return self.get_body_params().get('StoryName')

	def set_StoryName(self, StoryName):  # String
		self.add_body_params('StoryName', StoryName)
