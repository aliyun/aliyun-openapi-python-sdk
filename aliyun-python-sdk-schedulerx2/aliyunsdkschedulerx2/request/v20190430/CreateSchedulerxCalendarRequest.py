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
from aliyunsdkschedulerx2.endpoint import endpoint_data

class CreateSchedulerxCalendarRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'schedulerx2', '2019-04-30', 'CreateSchedulerxCalendar','schedulerx2')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Year(self): # Integer
		return self.get_body_params().get('Year')

	def set_Year(self, Year):  # Integer
		self.add_body_params('Year', Year)
	def get_CalendarName(self): # String
		return self.get_body_params().get('CalendarName')

	def set_CalendarName(self, CalendarName):  # String
		self.add_body_params('CalendarName', CalendarName)
	def get_MonthDaysContent(self): # String
		return self.get_body_params().get('MonthDaysContent')

	def set_MonthDaysContent(self, MonthDaysContent):  # String
		self.add_body_params('MonthDaysContent', MonthDaysContent)
