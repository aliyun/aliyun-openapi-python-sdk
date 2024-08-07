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

class ListApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BPStudio', '2021-09-31', 'ListApplication','bpstudio')
		self.set_method('POST')

	def get_ResourceId(self): # String
		return self.get_body_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_body_params('ResourceId', ResourceId)
	def get_TemplateId(self): # String
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_body_params('TemplateId', TemplateId)
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
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
