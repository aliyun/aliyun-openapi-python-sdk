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

class ListEmrHiveAuditLogsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2018-06-01', 'ListEmrHiveAuditLogs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DatabaseName(self): # String
		return self.get_query_params().get('DatabaseName')

	def set_DatabaseName(self, DatabaseName):  # String
		self.add_query_param('DatabaseName', DatabaseName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_EndTime(self): # Integer
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Integer
		self.add_query_param('EndTime', EndTime)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_StartTime(self): # Integer
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Integer
		self.add_query_param('StartTime', StartTime)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
