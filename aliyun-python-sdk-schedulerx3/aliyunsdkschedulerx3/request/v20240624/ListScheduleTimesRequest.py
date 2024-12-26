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

class ListScheduleTimesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SchedulerX3', '2024-06-24', 'ListScheduleTimes')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_TimeZone(self): # String
		return self.get_query_params().get('TimeZone')

	def set_TimeZone(self, TimeZone):  # String
		self.add_query_param('TimeZone', TimeZone)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_Calendar(self): # String
		return self.get_query_params().get('Calendar')

	def set_Calendar(self, Calendar):  # String
		self.add_query_param('Calendar', Calendar)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_TimeExpression(self): # String
		return self.get_query_params().get('TimeExpression')

	def set_TimeExpression(self, TimeExpression):  # String
		self.add_query_param('TimeExpression', TimeExpression)
	def get_TimeType(self): # Integer
		return self.get_query_params().get('TimeType')

	def set_TimeType(self, TimeType):  # Integer
		self.add_query_param('TimeType', TimeType)
