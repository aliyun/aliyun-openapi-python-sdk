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

class ListTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BPStudio', '2021-09-31', 'ListTemplate','bpstudio')
		self.set_method('POST')

	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_TagList(self): # Integer
		return self.get_body_params().get('TagList')

	def set_TagList(self, TagList):  # Integer
		self.add_body_params('TagList', TagList)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_NextToken(self): # Integer
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # Integer
		self.add_body_params('NextToken', NextToken)
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
	def get_Keyword(self): # String
		return self.get_body_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_body_params('Keyword', Keyword)
	def get_OrderType(self): # Long
		return self.get_body_params().get('OrderType')

	def set_OrderType(self, OrderType):  # Long
		self.add_body_params('OrderType', OrderType)
