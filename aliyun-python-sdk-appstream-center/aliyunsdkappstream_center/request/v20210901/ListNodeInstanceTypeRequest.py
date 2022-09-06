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

class ListNodeInstanceTypeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'appstream-center', '2021-09-01', 'ListNodeInstanceType')
		self.set_method('POST')

	def get_BizRegionId(self): # String
		return self.get_query_params().get('BizRegionId')

	def set_BizRegionId(self, BizRegionId):  # String
		self.add_query_param('BizRegionId', BizRegionId)
	def get_Language(self): # String
		return self.get_query_params().get('Language')

	def set_Language(self, Language):  # String
		self.add_query_param('Language', Language)
	def get_OsType(self): # String
		return self.get_query_params().get('OsType')

	def set_OsType(self, OsType):  # String
		self.add_query_param('OsType', OsType)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ProductType(self): # String
		return self.get_query_params().get('ProductType')

	def set_ProductType(self, ProductType):  # String
		self.add_query_param('ProductType', ProductType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
