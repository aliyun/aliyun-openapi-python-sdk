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
from aliyunsdkgreen.endpoint import endpoint_data

class UpdateNotificationSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'UpdateNotificationSetting','green')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RealtimeMessageList(self):
		return self.get_query_params().get('RealtimeMessageList')

	def set_RealtimeMessageList(self,RealtimeMessageList):
		self.add_query_param('RealtimeMessageList',RealtimeMessageList)

	def get_ScheduleMessageTime(self):
		return self.get_query_params().get('ScheduleMessageTime')

	def set_ScheduleMessageTime(self,ScheduleMessageTime):
		self.add_query_param('ScheduleMessageTime',ScheduleMessageTime)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_ReminderModeList(self):
		return self.get_query_params().get('ReminderModeList')

	def set_ReminderModeList(self,ReminderModeList):
		self.add_query_param('ReminderModeList',ReminderModeList)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_ScheduleMessageTimeZone(self):
		return self.get_query_params().get('ScheduleMessageTimeZone')

	def set_ScheduleMessageTimeZone(self,ScheduleMessageTimeZone):
		self.add_query_param('ScheduleMessageTimeZone',ScheduleMessageTimeZone)