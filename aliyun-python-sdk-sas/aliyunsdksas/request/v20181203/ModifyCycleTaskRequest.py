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
from aliyunsdksas.endpoint import endpoint_data

class ModifyCycleTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ModifyCycleTask','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FirstDateStr(self): # Long
		return self.get_query_params().get('FirstDateStr')

	def set_FirstDateStr(self, FirstDateStr):  # Long
		self.add_query_param('FirstDateStr', FirstDateStr)
	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_TargetStartTime(self): # Integer
		return self.get_query_params().get('TargetStartTime')

	def set_TargetStartTime(self, TargetStartTime):  # Integer
		self.add_query_param('TargetStartTime', TargetStartTime)
	def get_IntervalPeriod(self): # Integer
		return self.get_query_params().get('IntervalPeriod')

	def set_IntervalPeriod(self, IntervalPeriod):  # Integer
		self.add_query_param('IntervalPeriod', IntervalPeriod)
	def get_Param(self): # String
		return self.get_query_params().get('Param')

	def set_Param(self, Param):  # String
		self.add_query_param('Param', Param)
	def get_Enable(self): # Integer
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # Integer
		self.add_query_param('Enable', Enable)
	def get_TaskType(self): # String
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # String
		self.add_query_param('TaskType', TaskType)
	def get_TargetEndTime(self): # Integer
		return self.get_query_params().get('TargetEndTime')

	def set_TargetEndTime(self, TargetEndTime):  # Integer
		self.add_query_param('TargetEndTime', TargetEndTime)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_ConfigId(self): # String
		return self.get_query_params().get('ConfigId')

	def set_ConfigId(self, ConfigId):  # String
		self.add_query_param('ConfigId', ConfigId)
