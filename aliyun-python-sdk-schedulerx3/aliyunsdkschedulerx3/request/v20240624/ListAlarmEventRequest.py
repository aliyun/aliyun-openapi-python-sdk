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

class ListAlarmEventRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SchedulerX3', '2024-06-24', 'ListAlarmEvent')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_PageNum(self): # String
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # String
		self.add_query_param('PageNum', PageNum)
	def get_AlarmChannel(self): # String
		return self.get_query_params().get('AlarmChannel')

	def set_AlarmChannel(self, AlarmChannel):  # String
		self.add_query_param('AlarmChannel', AlarmChannel)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_JobName(self): # String
		return self.get_query_params().get('JobName')

	def set_JobName(self, JobName):  # String
		self.add_query_param('JobName', JobName)
	def get_AlarmType(self): # String
		return self.get_query_params().get('AlarmType')

	def set_AlarmType(self, AlarmType):  # String
		self.add_query_param('AlarmType', AlarmType)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_Reverse(self): # Boolean
		return self.get_query_params().get('Reverse')

	def set_Reverse(self, Reverse):  # Boolean
		self.add_query_param('Reverse', Reverse)
	def get_AlarmStatus(self): # String
		return self.get_query_params().get('AlarmStatus')

	def set_AlarmStatus(self, AlarmStatus):  # String
		self.add_query_param('AlarmStatus', AlarmStatus)
