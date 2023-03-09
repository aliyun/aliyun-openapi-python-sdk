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
from aliyunsdkadb.endpoint import endpoint_data

class DownloadDiagnosisRecordsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'adb', '2019-03-15', 'DownloadDiagnosisRecords','ads')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_QueryCondition(self): # String
		return self.get_query_params().get('QueryCondition')

	def set_QueryCondition(self, QueryCondition):  # String
		self.add_query_param('QueryCondition', QueryCondition)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_Database(self): # String
		return self.get_query_params().get('Database')

	def set_Database(self, Database):  # String
		self.add_query_param('Database', Database)
	def get_ClientIp(self): # String
		return self.get_query_params().get('ClientIp')

	def set_ClientIp(self, ClientIp):  # String
		self.add_query_param('ClientIp', ClientIp)
	def get_Keyword(self): # String
		return self.get_query_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_query_param('Keyword', Keyword)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_MaxScanSize(self): # Long
		return self.get_query_params().get('MaxScanSize')

	def set_MaxScanSize(self, MaxScanSize):  # Long
		self.add_query_param('MaxScanSize', MaxScanSize)
	def get_ResourceGroup(self): # String
		return self.get_query_params().get('ResourceGroup')

	def set_ResourceGroup(self, ResourceGroup):  # String
		self.add_query_param('ResourceGroup', ResourceGroup)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_MinPeakMemory(self): # Long
		return self.get_query_params().get('MinPeakMemory')

	def set_MinPeakMemory(self, MinPeakMemory):  # Long
		self.add_query_param('MinPeakMemory', MinPeakMemory)
	def get_MinScanSize(self): # Long
		return self.get_query_params().get('MinScanSize')

	def set_MinScanSize(self, MinScanSize):  # Long
		self.add_query_param('MinScanSize', MinScanSize)
	def get_MaxPeakMemory(self): # Long
		return self.get_query_params().get('MaxPeakMemory')

	def set_MaxPeakMemory(self, MaxPeakMemory):  # Long
		self.add_query_param('MaxPeakMemory', MaxPeakMemory)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
