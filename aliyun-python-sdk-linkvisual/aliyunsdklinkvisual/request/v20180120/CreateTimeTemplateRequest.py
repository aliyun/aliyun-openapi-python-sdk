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
from aliyunsdklinkvisual.endpoint import endpoint_data

class CreateTimeTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Linkvisual', '2018-01-20', 'CreateTimeTemplate','Linkvisual')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TimeSectionss(self): # RepeatList
		return self.get_query_params().get('TimeSections')

	def set_TimeSectionss(self, TimeSections):  # RepeatList
		for depth1 in range(len(TimeSections)):
			if TimeSections[depth1].get('DayOfWeek') is not None:
				self.add_query_param('TimeSections.' + str(depth1 + 1) + '.DayOfWeek', TimeSections[depth1].get('DayOfWeek'))
			if TimeSections[depth1].get('Begin') is not None:
				self.add_query_param('TimeSections.' + str(depth1 + 1) + '.Begin', TimeSections[depth1].get('Begin'))
			if TimeSections[depth1].get('End') is not None:
				self.add_query_param('TimeSections.' + str(depth1 + 1) + '.End', TimeSections[depth1].get('End'))
	def get_AllDay(self): # Integer
		return self.get_query_params().get('AllDay')

	def set_AllDay(self, AllDay):  # Integer
		self.add_query_param('AllDay', AllDay)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
