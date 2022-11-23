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

class UpdateTaskFlowScheduleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'UpdateTaskFlowSchedule','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CronType(self): # String
		return self.get_query_params().get('CronType')

	def set_CronType(self, CronType):  # String
		self.add_query_param('CronType', CronType)
	def get_CronStr(self): # String
		return self.get_query_params().get('CronStr')

	def set_CronStr(self, CronStr):  # String
		self.add_query_param('CronStr', CronStr)
	def get_TriggerType(self): # String
		return self.get_query_params().get('TriggerType')

	def set_TriggerType(self, TriggerType):  # String
		self.add_query_param('TriggerType', TriggerType)
	def get_DagId(self): # Long
		return self.get_query_params().get('DagId')

	def set_DagId(self, DagId):  # Long
		self.add_query_param('DagId', DagId)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_TimeZoneId(self): # String
		return self.get_query_params().get('TimeZoneId')

	def set_TimeZoneId(self, TimeZoneId):  # String
		self.add_query_param('TimeZoneId', TimeZoneId)
	def get_CronBeginDate(self): # String
		return self.get_query_params().get('CronBeginDate')

	def set_CronBeginDate(self, CronBeginDate):  # String
		self.add_query_param('CronBeginDate', CronBeginDate)
	def get_ScheduleSwitch(self): # Boolean
		return self.get_query_params().get('ScheduleSwitch')

	def set_ScheduleSwitch(self, ScheduleSwitch):  # Boolean
		self.add_query_param('ScheduleSwitch', ScheduleSwitch)
	def get_CronEndDate(self): # String
		return self.get_query_params().get('CronEndDate')

	def set_CronEndDate(self, CronEndDate):  # String
		self.add_query_param('CronEndDate', CronEndDate)
	def get_ScheduleParam(self): # String
		return self.get_query_params().get('ScheduleParam')

	def set_ScheduleParam(self, ScheduleParam):  # String
		self.add_query_param('ScheduleParam', ScheduleParam)
