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
from aliyunsdkoos.endpoint import endpoint_data

class ListTemplatesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'ListTemplates','oos')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CreatedDateBefore(self):
		return self.get_query_params().get('CreatedDateBefore')

	def set_CreatedDateBefore(self,CreatedDateBefore):
		self.add_query_param('CreatedDateBefore',CreatedDateBefore)

	def get_CreatedBy(self):
		return self.get_query_params().get('CreatedBy')

	def set_CreatedBy(self,CreatedBy):
		self.add_query_param('CreatedBy',CreatedBy)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_TemplateType(self):
		return self.get_query_params().get('TemplateType')

	def set_TemplateType(self,TemplateType):
		self.add_query_param('TemplateType',TemplateType)

	def get_TemplateName(self):
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self,TemplateName):
		self.add_query_param('TemplateName',TemplateName)

	def get_SortOrder(self):
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self,SortOrder):
		self.add_query_param('SortOrder',SortOrder)

	def get_ShareType(self):
		return self.get_query_params().get('ShareType')

	def set_ShareType(self,ShareType):
		self.add_query_param('ShareType',ShareType)

	def get_HasTrigger(self):
		return self.get_query_params().get('HasTrigger')

	def set_HasTrigger(self,HasTrigger):
		self.add_query_param('HasTrigger',HasTrigger)

	def get_CreatedDateAfter(self):
		return self.get_query_params().get('CreatedDateAfter')

	def set_CreatedDateAfter(self,CreatedDateAfter):
		self.add_query_param('CreatedDateAfter',CreatedDateAfter)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_TemplateFormat(self):
		return self.get_query_params().get('TemplateFormat')

	def set_TemplateFormat(self,TemplateFormat):
		self.add_query_param('TemplateFormat',TemplateFormat)

	def get_SortField(self):
		return self.get_query_params().get('SortField')

	def set_SortField(self,SortField):
		self.add_query_param('SortField',SortField)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)