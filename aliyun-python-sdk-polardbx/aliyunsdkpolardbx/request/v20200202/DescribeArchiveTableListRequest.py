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
from aliyunsdkpolardbx.endpoint import endpoint_data

class DescribeArchiveTableListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardbx', '2020-02-02', 'DescribeArchiveTableList','polardbx')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBInstanceName(self): # String
		return self.get_query_params().get('DBInstanceName')

	def set_DBInstanceName(self, DBInstanceName):  # String
		self.add_query_param('DBInstanceName', DBInstanceName)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_PageIndex(self): # Long
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self, PageIndex):  # Long
		self.add_query_param('PageIndex', PageIndex)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
	def get_SchemaName(self): # String
		return self.get_query_params().get('SchemaName')

	def set_SchemaName(self, SchemaName):  # String
		self.add_query_param('SchemaName', SchemaName)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
