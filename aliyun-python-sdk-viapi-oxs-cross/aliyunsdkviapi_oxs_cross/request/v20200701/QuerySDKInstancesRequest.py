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

class QuerySDKInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'viapi-oxs-cross', '2020-07-01', 'QuerySDKInstances')
		self.set_method('POST')

	def get_CodeList(self): # String
		return self.get_query_params().get('CodeList')

	def set_CodeList(self, CodeList):  # String
		self.add_query_param('CodeList', CodeList)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_CreatedBeforeDate(self): # String
		return self.get_query_params().get('CreatedBeforeDate')

	def set_CreatedBeforeDate(self, CreatedBeforeDate):  # String
		self.add_query_param('CreatedBeforeDate', CreatedBeforeDate)
	def get_CreatedAfterDate(self): # String
		return self.get_query_params().get('CreatedAfterDate')

	def set_CreatedAfterDate(self, CreatedAfterDate):  # String
		self.add_query_param('CreatedAfterDate', CreatedAfterDate)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Pk(self): # String
		return self.get_query_params().get('Pk')

	def set_Pk(self, Pk):  # String
		self.add_query_param('Pk', Pk)
