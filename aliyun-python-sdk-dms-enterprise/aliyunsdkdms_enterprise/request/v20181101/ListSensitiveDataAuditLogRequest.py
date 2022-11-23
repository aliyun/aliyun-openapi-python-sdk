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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class ListSensitiveDataAuditLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'ListSensitiveDataAuditLog','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OpUserName(self): # String
		return self.get_query_params().get('OpUserName')

	def set_OpUserName(self, OpUserName):  # String
		self.add_query_param('OpUserName', OpUserName)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ModuleName(self): # String
		return self.get_query_params().get('ModuleName')

	def set_ModuleName(self, ModuleName):  # String
		self.add_query_param('ModuleName', ModuleName)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_ColumnName(self): # String
		return self.get_query_params().get('ColumnName')

	def set_ColumnName(self, ColumnName):  # String
		self.add_query_param('ColumnName', ColumnName)
	def get_DbName(self): # String
		return self.get_query_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_query_param('DbName', DbName)
