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

	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_CreatedDateBefore(self): # String
		return self.get_query_params().get('CreatedDateBefore')

	def set_CreatedDateBefore(self, CreatedDateBefore):  # String
		self.add_query_param('CreatedDateBefore', CreatedDateBefore)
	def get_CreatedBy(self): # String
		return self.get_query_params().get('CreatedBy')

	def set_CreatedBy(self, CreatedBy):  # String
		self.add_query_param('CreatedBy', CreatedBy)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_TemplateType(self): # String
		return self.get_query_params().get('TemplateType')

	def set_TemplateType(self, TemplateType):  # String
		self.add_query_param('TemplateType', TemplateType)
	def get_TemplateName(self): # String
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self, TemplateName):  # String
		self.add_query_param('TemplateName', TemplateName)
	def get_SortOrder(self): # String
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self, SortOrder):  # String
		self.add_query_param('SortOrder', SortOrder)
	def get_ShareType(self): # String
		return self.get_query_params().get('ShareType')

	def set_ShareType(self, ShareType):  # String
		self.add_query_param('ShareType', ShareType)
	def get_HasTrigger(self): # Boolean
		return self.get_query_params().get('HasTrigger')

	def set_HasTrigger(self, HasTrigger):  # Boolean
		self.add_query_param('HasTrigger', HasTrigger)
	def get_CreatedDateAfter(self): # String
		return self.get_query_params().get('CreatedDateAfter')

	def set_CreatedDateAfter(self, CreatedDateAfter):  # String
		self.add_query_param('CreatedDateAfter', CreatedDateAfter)
	def get_Tags(self): # Json
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Json
		self.add_query_param('Tags', Tags)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_TemplateFormat(self): # String
		return self.get_query_params().get('TemplateFormat')

	def set_TemplateFormat(self, TemplateFormat):  # String
		self.add_query_param('TemplateFormat', TemplateFormat)
	def get_SortField(self): # String
		return self.get_query_params().get('SortField')

	def set_SortField(self, SortField):  # String
		self.add_query_param('SortField', SortField)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
