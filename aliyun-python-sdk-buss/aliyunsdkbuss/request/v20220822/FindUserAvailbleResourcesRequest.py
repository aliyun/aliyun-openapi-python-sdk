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

class FindUserAvailbleResourcesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'FindUserAvailbleResources')
		self.set_method('GET')

	def get_bussinessCode(self): # String
		return self.get_query_params().get('bussinessCode')

	def set_bussinessCode(self, bussinessCode):  # String
		self.add_query_param('bussinessCode', bussinessCode)
	def get_currPage(self): # Integer
		return self.get_query_params().get('currPage')

	def set_currPage(self, currPage):  # Integer
		self.add_query_param('currPage', currPage)
	def get_pageSize(self): # Integer
		return self.get_query_params().get('pageSize')

	def set_pageSize(self, pageSize):  # Integer
		self.add_query_param('pageSize', pageSize)
	def get_userId(self): # String
		return self.get_query_params().get('userId')

	def set_userId(self, userId):  # String
		self.add_query_param('userId', userId)
	def get_resourceType(self): # String
		return self.get_query_params().get('resourceType')

	def set_resourceType(self, resourceType):  # String
		self.add_query_param('resourceType', resourceType)
