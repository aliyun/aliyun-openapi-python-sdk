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
import json

class GetNisNetworkMetricsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nis', '2021-12-16', 'GetNisNetworkMetrics','networkana')
		self.set_method('POST')

	def get_UseCrossAccount(self): # Boolean
		return self.get_query_params().get('UseCrossAccount')

	def set_UseCrossAccount(self, UseCrossAccount):  # Boolean
		self.add_query_param('UseCrossAccount', UseCrossAccount)
	def get_ScanBy(self): # String
		return self.get_query_params().get('ScanBy')

	def set_ScanBy(self, ScanBy):  # String
		self.add_query_param('ScanBy', ScanBy)
	def get_MetricName(self): # String
		return self.get_query_params().get('MetricName')

	def set_MetricName(self, MetricName):  # String
		self.add_query_param('MetricName', MetricName)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_BeginTime(self): # Long
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # Long
		self.add_query_param('BeginTime', BeginTime)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_RegionNo(self): # String
		return self.get_query_params().get('RegionNo')

	def set_RegionNo(self, RegionNo):  # String
		self.add_query_param('RegionNo', RegionNo)
	def get_AccountIdss(self): # RepeatList
		return self.get_query_params().get('AccountIds')

	def set_AccountIdss(self, AccountIds):  # RepeatList
		for depth1 in range(len(AccountIds)):
			self.add_query_param('AccountIds.' + str(depth1 + 1), AccountIds[depth1])
	def get_Dimensions(self): # Array
		return self.get_query_params().get('Dimensions')

	def set_Dimensions(self, Dimensions):  # Array
		self.add_query_param("Dimensions", json.dumps(Dimensions))
