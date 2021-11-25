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

class GetOfficePreviewURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'GetOfficePreviewURL','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SrcType(self): # String
		return self.get_query_params().get('SrcType')

	def set_SrcType(self, SrcType):  # String
		self.add_query_param('SrcType', SrcType)
	def get_Project(self): # String
		return self.get_query_params().get('Project')

	def set_Project(self, Project):  # String
		self.add_query_param('Project', Project)
	def get_WatermarkVertical(self): # Integer
		return self.get_query_params().get('WatermarkVertical')

	def set_WatermarkVertical(self, WatermarkVertical):  # Integer
		self.add_query_param('WatermarkVertical', WatermarkVertical)
	def get_WatermarkType(self): # Integer
		return self.get_query_params().get('WatermarkType')

	def set_WatermarkType(self, WatermarkType):  # Integer
		self.add_query_param('WatermarkType', WatermarkType)
	def get_WatermarkRotate(self): # Float
		return self.get_query_params().get('WatermarkRotate')

	def set_WatermarkRotate(self, WatermarkRotate):  # Float
		self.add_query_param('WatermarkRotate', WatermarkRotate)
	def get_WatermarkValue(self): # String
		return self.get_query_params().get('WatermarkValue')

	def set_WatermarkValue(self, WatermarkValue):  # String
		self.add_query_param('WatermarkValue', WatermarkValue)
	def get_WatermarkFont(self): # String
		return self.get_query_params().get('WatermarkFont')

	def set_WatermarkFont(self, WatermarkFont):  # String
		self.add_query_param('WatermarkFont', WatermarkFont)
	def get_WatermarkHorizontal(self): # Integer
		return self.get_query_params().get('WatermarkHorizontal')

	def set_WatermarkHorizontal(self, WatermarkHorizontal):  # Integer
		self.add_query_param('WatermarkHorizontal', WatermarkHorizontal)
	def get_SrcUri(self): # String
		return self.get_query_params().get('SrcUri')

	def set_SrcUri(self, SrcUri):  # String
		self.add_query_param('SrcUri', SrcUri)
	def get_WatermarkFillStyle(self): # String
		return self.get_query_params().get('WatermarkFillStyle')

	def set_WatermarkFillStyle(self, WatermarkFillStyle):  # String
		self.add_query_param('WatermarkFillStyle', WatermarkFillStyle)
