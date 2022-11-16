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
from aliyunsdkcloudapi.endpoint import endpoint_data

class DescribeDeployedApisRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'DescribeDeployedApis','apigateway')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StageName(self): # String
		return self.get_query_params().get('StageName')

	def set_StageName(self, StageName):  # String
		self.add_query_param('StageName', StageName)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_ApiMethod(self): # String
		return self.get_query_params().get('ApiMethod')

	def set_ApiMethod(self, ApiMethod):  # String
		self.add_query_param('ApiMethod', ApiMethod)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_ApiPath(self): # String
		return self.get_query_params().get('ApiPath')

	def set_ApiPath(self, ApiPath):  # String
		self.add_query_param('ApiPath', ApiPath)
	def get_EnableTagAuth(self): # Boolean
		return self.get_query_params().get('EnableTagAuth')

	def set_EnableTagAuth(self, EnableTagAuth):  # Boolean
		self.add_query_param('EnableTagAuth', EnableTagAuth)
	def get_ApiName(self): # String
		return self.get_query_params().get('ApiName')

	def set_ApiName(self, ApiName):  # String
		self.add_query_param('ApiName', ApiName)
	def get_ApiId(self): # String
		return self.get_query_params().get('ApiId')

	def set_ApiId(self, ApiId):  # String
		self.add_query_param('ApiId', ApiId)
