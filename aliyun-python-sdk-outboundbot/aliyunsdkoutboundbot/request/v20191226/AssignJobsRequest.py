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
from aliyunsdkoutboundbot.endpoint import endpoint_data

class AssignJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'AssignJobs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_JobsJsons(self): # RepeatList
		return self.get_query_params().get('JobsJson')

	def set_JobsJsons(self, JobsJson):  # RepeatList
		for depth1 in range(len(JobsJson)):
			self.add_query_param('JobsJson.' + str(depth1 + 1), JobsJson[depth1])
	def get_CallingNumbers(self): # RepeatList
		return self.get_query_params().get('CallingNumber')

	def set_CallingNumbers(self, CallingNumber):  # RepeatList
		for depth1 in range(len(CallingNumber)):
			self.add_query_param('CallingNumber.' + str(depth1 + 1), CallingNumber[depth1])
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_RosterType(self): # String
		return self.get_query_params().get('RosterType')

	def set_RosterType(self, RosterType):  # String
		self.add_query_param('RosterType', RosterType)
	def get_JobDataParsingTaskId(self): # String
		return self.get_query_params().get('JobDataParsingTaskId')

	def set_JobDataParsingTaskId(self, JobDataParsingTaskId):  # String
		self.add_query_param('JobDataParsingTaskId', JobDataParsingTaskId)
	def get_StrategyJson(self): # String
		return self.get_query_params().get('StrategyJson')

	def set_StrategyJson(self, StrategyJson):  # String
		self.add_query_param('StrategyJson', StrategyJson)
	def get_JobGroupId(self): # String
		return self.get_query_params().get('JobGroupId')

	def set_JobGroupId(self, JobGroupId):  # String
		self.add_query_param('JobGroupId', JobGroupId)
	def get_IsAsynchrony(self): # Boolean
		return self.get_query_params().get('IsAsynchrony')

	def set_IsAsynchrony(self, IsAsynchrony):  # Boolean
		self.add_query_param('IsAsynchrony', IsAsynchrony)
