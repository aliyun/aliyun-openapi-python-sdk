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

class SearchImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'WebsiteBuild', '2025-04-29', 'SearchImage')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_HasPerson(self): # Boolean
		return self.get_query_params().get('HasPerson')

	def set_HasPerson(self, HasPerson):  # Boolean
		self.add_query_param('HasPerson', HasPerson)
	def get_MaxWidth(self): # Integer
		return self.get_query_params().get('MaxWidth')

	def set_MaxWidth(self, MaxWidth):  # Integer
		self.add_query_param('MaxWidth', MaxWidth)
	def get_OssKey(self): # String
		return self.get_query_params().get('OssKey')

	def set_OssKey(self, OssKey):  # String
		self.add_query_param('OssKey', OssKey)
	def get_ImageCategory(self): # String
		return self.get_query_params().get('ImageCategory')

	def set_ImageCategory(self, ImageCategory):  # String
		self.add_query_param('ImageCategory', ImageCategory)
	def get_MaxHeight(self): # Integer
		return self.get_query_params().get('MaxHeight')

	def set_MaxHeight(self, MaxHeight):  # Integer
		self.add_query_param('MaxHeight', MaxHeight)
	def get_ImageRatio(self): # String
		return self.get_query_params().get('ImageRatio')

	def set_ImageRatio(self, ImageRatio):  # String
		self.add_query_param('ImageRatio', ImageRatio)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Text(self): # String
		return self.get_query_params().get('Text')

	def set_Text(self, Text):  # String
		self.add_query_param('Text', Text)
	def get_ColorHex(self): # String
		return self.get_query_params().get('ColorHex')

	def set_ColorHex(self, ColorHex):  # String
		self.add_query_param('ColorHex', ColorHex)
	def get_MinHeight(self): # Integer
		return self.get_query_params().get('MinHeight')

	def set_MinHeight(self, MinHeight):  # Integer
		self.add_query_param('MinHeight', MinHeight)
	def get_Start(self): # Integer
		return self.get_query_params().get('Start')

	def set_Start(self, Start):  # Integer
		self.add_query_param('Start', Start)
	def get_Tags(self): # Array
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Array
		for index1, value1 in enumerate(Tags):
			self.add_query_param('Tags.' + str(index1 + 1), value1)
	def get_Size(self): # Integer
		return self.get_query_params().get('Size')

	def set_Size(self, Size):  # Integer
		self.add_query_param('Size', Size)
	def get_MinWidth(self): # Integer
		return self.get_query_params().get('MinWidth')

	def set_MinWidth(self, MinWidth):  # Integer
		self.add_query_param('MinWidth', MinWidth)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
