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
from aliyunsdkice.endpoint import endpoint_data

class UpdateMediaInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'UpdateMediaInfo','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Title(self): # String
		return self.get_query_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_query_param('Title', Title)
	def get_BusinessType(self): # String
		return self.get_query_params().get('BusinessType')

	def set_BusinessType(self, BusinessType):  # String
		self.add_query_param('BusinessType', BusinessType)
	def get_CoverURL(self): # String
		return self.get_query_params().get('CoverURL')

	def set_CoverURL(self, CoverURL):  # String
		self.add_query_param('CoverURL', CoverURL)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_CateId(self): # Long
		return self.get_query_params().get('CateId')

	def set_CateId(self, CateId):  # Long
		self.add_query_param('CateId', CateId)
	def get_MediaTags(self): # String
		return self.get_query_params().get('MediaTags')

	def set_MediaTags(self, MediaTags):  # String
		self.add_query_param('MediaTags', MediaTags)
	def get_InputURL(self): # String
		return self.get_query_params().get('InputURL')

	def set_InputURL(self, InputURL):  # String
		self.add_query_param('InputURL', InputURL)
	def get_MediaId(self): # String
		return self.get_query_params().get('MediaId')

	def set_MediaId(self, MediaId):  # String
		self.add_query_param('MediaId', MediaId)
	def get_ReferenceId(self): # String
		return self.get_query_params().get('ReferenceId')

	def set_ReferenceId(self, ReferenceId):  # String
		self.add_query_param('ReferenceId', ReferenceId)
	def get_AppendTags(self): # Boolean
		return self.get_query_params().get('AppendTags')

	def set_AppendTags(self, AppendTags):  # Boolean
		self.add_query_param('AppendTags', AppendTags)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
