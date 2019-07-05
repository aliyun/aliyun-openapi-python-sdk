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
class CreateKeywordLibRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'CreateKeywordLib','green')

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_LibType(self):
		return self.get_query_params().get('LibType')

	def set_LibType(self,LibType):
		self.add_query_param('LibType',LibType)

	def get_Enable(self):
		return self.get_query_params().get('Enable')

	def set_Enable(self,Enable):
		self.add_query_param('Enable',Enable)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_BizTypes(self):
		return self.get_query_params().get('BizTypes')

	def set_BizTypes(self,BizTypes):
		self.add_query_param('BizTypes',BizTypes)

	def get_Language(self):
		return self.get_query_params().get('Language')

	def set_Language(self,Language):
		self.add_query_param('Language',Language)

	def get_ServiceModule(self):
		return self.get_query_params().get('ServiceModule')

	def set_ServiceModule(self,ServiceModule):
		self.add_query_param('ServiceModule',ServiceModule)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_MatchMode(self):
		return self.get_query_params().get('MatchMode')

	def set_MatchMode(self,MatchMode):
		self.add_query_param('MatchMode',MatchMode)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)