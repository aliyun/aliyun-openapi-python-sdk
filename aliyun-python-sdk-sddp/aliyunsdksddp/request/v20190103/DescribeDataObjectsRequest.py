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
from aliyunsdksddp.endpoint import endpoint_data

class DescribeDataObjectsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'DescribeDataObjects','sddp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FileType(self): # Long
		return self.get_query_params().get('FileType')

	def set_FileType(self, FileType):  # Long
		self.add_query_param('FileType', FileType)
	def get_RiskLevels(self): # String
		return self.get_query_params().get('RiskLevels')

	def set_RiskLevels(self, RiskLevels):  # String
		self.add_query_param('RiskLevels', RiskLevels)
	def get_QueryName(self): # String
		return self.get_query_params().get('QueryName')

	def set_QueryName(self, QueryName):  # String
		self.add_query_param('QueryName', QueryName)
	def get_DomainId(self): # Long
		return self.get_query_params().get('DomainId')

	def set_DomainId(self, DomainId):  # Long
		self.add_query_param('DomainId', DomainId)
	def get_ParentCategoryIds(self): # String
		return self.get_query_params().get('ParentCategoryIds')

	def set_ParentCategoryIds(self, ParentCategoryIds):  # String
		self.add_query_param('ParentCategoryIds', ParentCategoryIds)
	def get_ProductIds(self): # String
		return self.get_query_params().get('ProductIds')

	def set_ProductIds(self, ProductIds):  # String
		self.add_query_param('ProductIds', ProductIds)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_ServiceRegionId(self): # String
		return self.get_query_params().get('ServiceRegionId')

	def set_ServiceRegionId(self, ServiceRegionId):  # String
		self.add_query_param('ServiceRegionId', ServiceRegionId)
	def get_ModelTagIds(self): # String
		return self.get_query_params().get('ModelTagIds')

	def set_ModelTagIds(self, ModelTagIds):  # String
		self.add_query_param('ModelTagIds', ModelTagIds)
	def get_FeatureType(self): # Integer
		return self.get_query_params().get('FeatureType')

	def set_FeatureType(self, FeatureType):  # Integer
		self.add_query_param('FeatureType', FeatureType)
	def get_FileCategoryCode(self): # Long
		return self.get_query_params().get('FileCategoryCode')

	def set_FileCategoryCode(self, FileCategoryCode):  # Long
		self.add_query_param('FileCategoryCode', FileCategoryCode)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_TemplateId(self): # Long
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # Long
		self.add_query_param('TemplateId', TemplateId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ModelIds(self): # String
		return self.get_query_params().get('ModelIds')

	def set_ModelIds(self, ModelIds):  # String
		self.add_query_param('ModelIds', ModelIds)
