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

class GetMetaTableProducingTasksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'GetMetaTableProducingTasks')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DataSourceType(self): # String
		return self.get_query_params().get('DataSourceType')

	def set_DataSourceType(self, DataSourceType):  # String
		self.add_query_param('DataSourceType', DataSourceType)
	def get_SchemaName(self): # String
		return self.get_query_params().get('SchemaName')

	def set_SchemaName(self, SchemaName):  # String
		self.add_query_param('SchemaName', SchemaName)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_DbName(self): # String
		return self.get_query_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_query_param('DbName', DbName)
	def get_TableGuid(self): # String
		return self.get_query_params().get('TableGuid')

	def set_TableGuid(self, TableGuid):  # String
		self.add_query_param('TableGuid', TableGuid)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
