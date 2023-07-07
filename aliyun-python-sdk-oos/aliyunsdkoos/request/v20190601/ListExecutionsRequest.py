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

class ListExecutionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'ListExecutions','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ExecutedBy(self): # String
		return self.get_query_params().get('ExecutedBy')

	def set_ExecutedBy(self, ExecutedBy):  # String
		self.add_query_param('ExecutedBy', ExecutedBy)
	def get_IncludeChildExecution(self): # Boolean
		return self.get_query_params().get('IncludeChildExecution')

	def set_IncludeChildExecution(self, IncludeChildExecution):  # Boolean
		self.add_query_param('IncludeChildExecution', IncludeChildExecution)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Mode(self): # String
		return self.get_query_params().get('Mode')

	def set_Mode(self, Mode):  # String
		self.add_query_param('Mode', Mode)
	def get_ExecutionId(self): # String
		return self.get_query_params().get('ExecutionId')

	def set_ExecutionId(self, ExecutionId):  # String
		self.add_query_param('ExecutionId', ExecutionId)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_RamRole(self): # String
		return self.get_query_params().get('RamRole')

	def set_RamRole(self, RamRole):  # String
		self.add_query_param('RamRole', RamRole)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_TemplateName(self): # String
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self, TemplateName):  # String
		self.add_query_param('TemplateName', TemplateName)
	def get_EndDateBefore(self): # String
		return self.get_query_params().get('EndDateBefore')

	def set_EndDateBefore(self, EndDateBefore):  # String
		self.add_query_param('EndDateBefore', EndDateBefore)
	def get_SortOrder(self): # String
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self, SortOrder):  # String
		self.add_query_param('SortOrder', SortOrder)
	def get_Categories(self): # String
		return self.get_query_params().get('Categories')

	def set_Categories(self, Categories):  # String
		self.add_query_param('Categories', Categories)
	def get_ResourceId(self): # String
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_query_param('ResourceId', ResourceId)
	def get_StartDateAfter(self): # String
		return self.get_query_params().get('StartDateAfter')

	def set_StartDateAfter(self, StartDateAfter):  # String
		self.add_query_param('StartDateAfter', StartDateAfter)
	def get_StartDateBefore(self): # String
		return self.get_query_params().get('StartDateBefore')

	def set_StartDateBefore(self, StartDateBefore):  # String
		self.add_query_param('StartDateBefore', StartDateBefore)
	def get_Tags(self): # Json
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Json
		self.add_query_param('Tags', Tags)
	def get_ParentExecutionId(self): # String
		return self.get_query_params().get('ParentExecutionId')

	def set_ParentExecutionId(self, ParentExecutionId):  # String
		self.add_query_param('ParentExecutionId', ParentExecutionId)
	def get_Depth(self): # String
		return self.get_query_params().get('Depth')

	def set_Depth(self, Depth):  # String
		self.add_query_param('Depth', Depth)
	def get_EndDateAfter(self): # String
		return self.get_query_params().get('EndDateAfter')

	def set_EndDateAfter(self, EndDateAfter):  # String
		self.add_query_param('EndDateAfter', EndDateAfter)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_SortField(self): # String
		return self.get_query_params().get('SortField')

	def set_SortField(self, SortField):  # String
		self.add_query_param('SortField', SortField)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
	def get_ResourceTemplateName(self): # String
		return self.get_query_params().get('ResourceTemplateName')

	def set_ResourceTemplateName(self, ResourceTemplateName):  # String
		self.add_query_param('ResourceTemplateName', ResourceTemplateName)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
