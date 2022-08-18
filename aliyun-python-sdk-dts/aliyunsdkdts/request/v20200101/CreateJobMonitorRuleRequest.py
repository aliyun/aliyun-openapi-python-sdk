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
from aliyunsdkdts.endpoint import endpoint_data

class CreateJobMonitorRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'CreateJobMonitorRule','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_NoticeValue(self): # Integer
		return self.get_query_params().get('NoticeValue')

	def set_NoticeValue(self, NoticeValue):  # Integer
		self.add_query_param('NoticeValue', NoticeValue)
	def get_Times(self): # Integer
		return self.get_query_params().get('Times')

	def set_Times(self, Times):  # Integer
		self.add_query_param('Times', Times)
	def get_DtsJobId(self): # String
		return self.get_query_params().get('DtsJobId')

	def set_DtsJobId(self, DtsJobId):  # String
		self.add_query_param('DtsJobId', DtsJobId)
	def get_State(self): # String
		return self.get_query_params().get('State')

	def set_State(self, State):  # String
		self.add_query_param('State', State)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_DelayRuleTime(self): # Long
		return self.get_query_params().get('DelayRuleTime')

	def set_DelayRuleTime(self, DelayRuleTime):  # Long
		self.add_query_param('DelayRuleTime', DelayRuleTime)
	def get_Phone(self): # String
		return self.get_query_params().get('Phone')

	def set_Phone(self, Phone):  # String
		self.add_query_param('Phone', Phone)
