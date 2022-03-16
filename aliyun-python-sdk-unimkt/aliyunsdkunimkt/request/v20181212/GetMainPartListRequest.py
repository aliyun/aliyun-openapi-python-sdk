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
from aliyunsdkunimkt.endpoint import endpoint_data

class GetMainPartListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'GetMainPartList')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AccountType(self): # String
		return self.get_query_params().get('AccountType')

	def set_AccountType(self, AccountType):  # String
		self.add_query_param('AccountType', AccountType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_PageIndex(self): # Integer
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self, PageIndex):  # Integer
		self.add_query_param('PageIndex', PageIndex)
	def get_MainType(self): # Integer
		return self.get_query_params().get('MainType')

	def set_MainType(self, MainType):  # Integer
		self.add_query_param('MainType', MainType)
	def get_ParentMainId(self): # Long
		return self.get_query_params().get('ParentMainId')

	def set_ParentMainId(self, ParentMainId):  # Long
		self.add_query_param('ParentMainId', ParentMainId)
	def get_MainName(self): # String
		return self.get_query_params().get('MainName')

	def set_MainName(self, MainName):  # String
		self.add_query_param('MainName', MainName)
