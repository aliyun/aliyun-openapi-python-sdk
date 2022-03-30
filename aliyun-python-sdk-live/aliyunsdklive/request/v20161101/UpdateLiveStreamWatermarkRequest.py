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

class UpdateLiveStreamWatermarkRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'UpdateLiveStreamWatermark','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_YOffset(self): # Float
		return self.get_query_params().get('YOffset')

	def set_YOffset(self, YOffset):  # Float
		self.add_query_param('YOffset', YOffset)
	def get_PictureUrl(self): # String
		return self.get_query_params().get('PictureUrl')

	def set_PictureUrl(self, PictureUrl):  # String
		self.add_query_param('PictureUrl', PictureUrl)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Height(self): # Integer
		return self.get_query_params().get('Height')

	def set_Height(self, Height):  # Integer
		self.add_query_param('Height', Height)
	def get_XOffset(self): # Float
		return self.get_query_params().get('XOffset')

	def set_XOffset(self, XOffset):  # Float
		self.add_query_param('XOffset', XOffset)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_RefWidth(self): # Integer
		return self.get_query_params().get('RefWidth')

	def set_RefWidth(self, RefWidth):  # Integer
		self.add_query_param('RefWidth', RefWidth)
	def get_Transparency(self): # Integer
		return self.get_query_params().get('Transparency')

	def set_Transparency(self, Transparency):  # Integer
		self.add_query_param('Transparency', Transparency)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_OffsetCorner(self): # String
		return self.get_query_params().get('OffsetCorner')

	def set_OffsetCorner(self, OffsetCorner):  # String
		self.add_query_param('OffsetCorner', OffsetCorner)
	def get_RefHeight(self): # Integer
		return self.get_query_params().get('RefHeight')

	def set_RefHeight(self, RefHeight):  # Integer
		self.add_query_param('RefHeight', RefHeight)
