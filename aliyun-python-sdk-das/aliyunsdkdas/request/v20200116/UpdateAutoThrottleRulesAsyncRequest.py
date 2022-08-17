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
from aliyunsdkdas.endpoint import endpoint_data

class UpdateAutoThrottleRulesAsyncRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'UpdateAutoThrottleRulesAsync')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResultId(self): # String
		return self.get_query_params().get('ResultId')

	def set_ResultId(self, ResultId):  # String
		self.add_query_param('ResultId', ResultId)
	def get_CpuSessionRelation(self): # String
		return self.get_query_params().get('CpuSessionRelation')

	def set_CpuSessionRelation(self, CpuSessionRelation):  # String
		self.add_query_param('CpuSessionRelation', CpuSessionRelation)
	def get_AbnormalDuration(self): # Double
		return self.get_query_params().get('AbnormalDuration')

	def set_AbnormalDuration(self, AbnormalDuration):  # Double
		self.add_query_param('AbnormalDuration', AbnormalDuration)
	def get_MaxThrottleTime(self): # Double
		return self.get_query_params().get('MaxThrottleTime')

	def set_MaxThrottleTime(self, MaxThrottleTime):  # Double
		self.add_query_param('MaxThrottleTime', MaxThrottleTime)
	def get_ConsoleContext(self): # String
		return self.get_query_params().get('ConsoleContext')

	def set_ConsoleContext(self, ConsoleContext):  # String
		self.add_query_param('ConsoleContext', ConsoleContext)
	def get_CpuUsage(self): # Double
		return self.get_query_params().get('CpuUsage')

	def set_CpuUsage(self, CpuUsage):  # Double
		self.add_query_param('CpuUsage', CpuUsage)
	def get_AutoKillSession(self): # Boolean
		return self.get_query_params().get('AutoKillSession')

	def set_AutoKillSession(self, AutoKillSession):  # Boolean
		self.add_query_param('AutoKillSession', AutoKillSession)
	def get_AllowThrottleStartTime(self): # String
		return self.get_query_params().get('AllowThrottleStartTime')

	def set_AllowThrottleStartTime(self, AllowThrottleStartTime):  # String
		self.add_query_param('AllowThrottleStartTime', AllowThrottleStartTime)
	def get_AllowThrottleEndTime(self): # String
		return self.get_query_params().get('AllowThrottleEndTime')

	def set_AllowThrottleEndTime(self, AllowThrottleEndTime):  # String
		self.add_query_param('AllowThrottleEndTime', AllowThrottleEndTime)
	def get_InstanceIds(self): # String
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # String
		self.add_query_param('InstanceIds', InstanceIds)
	def get_ActiveSessions(self): # Long
		return self.get_query_params().get('ActiveSessions')

	def set_ActiveSessions(self, ActiveSessions):  # Long
		self.add_query_param('ActiveSessions', ActiveSessions)
