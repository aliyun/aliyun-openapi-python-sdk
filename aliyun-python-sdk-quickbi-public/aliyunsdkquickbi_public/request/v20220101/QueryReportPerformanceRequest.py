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

class QueryReportPerformanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'QueryReportPerformance','2.2.0')
		self.set_method('POST')

	def get_ReportId(self): # String
		return self.get_query_params().get('ReportId')

	def set_ReportId(self, ReportId):  # String
		self.add_query_param('ReportId', ReportId)
	def get_PageNum(self): # Integer
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # Integer
		self.add_query_param('PageNum', PageNum)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_CostTimeAvgMin(self): # Integer
		return self.get_query_params().get('CostTimeAvgMin')

	def set_CostTimeAvgMin(self, CostTimeAvgMin):  # Integer
		self.add_query_param('CostTimeAvgMin', CostTimeAvgMin)
	def get_QueryType(self): # String
		return self.get_query_params().get('QueryType')

	def set_QueryType(self, QueryType):  # String
		self.add_query_param('QueryType', QueryType)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_WorkspaceId(self): # String
		return self.get_query_params().get('WorkspaceId')

	def set_WorkspaceId(self, WorkspaceId):  # String
		self.add_query_param('WorkspaceId', WorkspaceId)
