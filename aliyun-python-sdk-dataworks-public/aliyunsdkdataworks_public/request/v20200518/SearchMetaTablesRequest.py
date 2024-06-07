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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class SearchMetaTablesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'SearchMetaTables')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Schema(self): # String
		return self.get_query_params().get('Schema')

	def set_Schema(self, Schema):  # String
		self.add_query_param('Schema', Schema)
	def get_DataSourceType(self): # String
		return self.get_query_params().get('DataSourceType')

	def set_DataSourceType(self, DataSourceType):  # String
		self.add_query_param('DataSourceType', DataSourceType)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_EntityType(self): # Integer
		return self.get_query_params().get('EntityType')

	def set_EntityType(self, EntityType):  # Integer
		self.add_query_param('EntityType', EntityType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_AppGuid(self): # String
		return self.get_query_params().get('AppGuid')

	def set_AppGuid(self, AppGuid):  # String
		self.add_query_param('AppGuid', AppGuid)
	def get_Keyword(self): # String
		return self.get_query_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_query_param('Keyword', Keyword)
