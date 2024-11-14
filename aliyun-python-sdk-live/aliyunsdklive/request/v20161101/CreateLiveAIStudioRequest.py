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
from aliyunsdklive.endpoint import endpoint_data
import json

class CreateLiveAIStudioRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'CreateLiveAIStudio','live')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BackgroundResourceId(self): # String
		return self.get_query_params().get('BackgroundResourceId')

	def set_BackgroundResourceId(self, BackgroundResourceId):  # String
		self.add_query_param('BackgroundResourceId', BackgroundResourceId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_MediaLayout(self): # Struct
		return self.get_query_params().get('MediaLayout')

	def set_MediaLayout(self, MediaLayout):  # Struct
		self.add_query_param("MediaLayout", json.dumps(MediaLayout))
	def get_BackgroundType(self): # String
		return self.get_query_params().get('BackgroundType')

	def set_BackgroundType(self, BackgroundType):  # String
		self.add_query_param('BackgroundType', BackgroundType)
	def get_MattingType(self): # String
		return self.get_query_params().get('MattingType')

	def set_MattingType(self, MattingType):  # String
		self.add_query_param('MattingType', MattingType)
	def get_MediaResourceUrl(self): # String
		return self.get_query_params().get('MediaResourceUrl')

	def set_MediaResourceUrl(self, MediaResourceUrl):  # String
		self.add_query_param('MediaResourceUrl', MediaResourceUrl)
	def get_Height(self): # Integer
		return self.get_query_params().get('Height')

	def set_Height(self, Height):  # Integer
		self.add_query_param('Height', Height)
	def get_BackgroundResourceUrl(self): # String
		return self.get_query_params().get('BackgroundResourceUrl')

	def set_BackgroundResourceUrl(self, BackgroundResourceUrl):  # String
		self.add_query_param('BackgroundResourceUrl', BackgroundResourceUrl)
	def get_MediaResourceId(self): # String
		return self.get_query_params().get('MediaResourceId')

	def set_MediaResourceId(self, MediaResourceId):  # String
		self.add_query_param('MediaResourceId', MediaResourceId)
	def get_MattingLayout(self): # Struct
		return self.get_query_params().get('MattingLayout')

	def set_MattingLayout(self, MattingLayout):  # Struct
		self.add_query_param("MattingLayout", json.dumps(MattingLayout))
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_StudioName(self): # String
		return self.get_query_params().get('StudioName')

	def set_StudioName(self, StudioName):  # String
		self.add_query_param('StudioName', StudioName)
	def get_Width(self): # Integer
		return self.get_query_params().get('Width')

	def set_Width(self, Width):  # Integer
		self.add_query_param('Width', Width)
	def get_MediaType(self): # String
		return self.get_query_params().get('MediaType')

	def set_MediaType(self, MediaType):  # String
		self.add_query_param('MediaType', MediaType)
