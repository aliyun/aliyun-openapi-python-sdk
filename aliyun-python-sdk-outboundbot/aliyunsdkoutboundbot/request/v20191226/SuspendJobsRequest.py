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

class SuspendJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'SuspendJobs','outboundbot')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_All(self):
		return self.get_query_params().get('All')

	def set_All(self,All):
		self.add_query_param('All',All)

	def get_JobReferenceIds(self):
		return self.get_query_params().get('JobReferenceIds')

	def set_JobReferenceIds(self,JobReferenceIds):
		for i in range(len(JobReferenceIds)):	
			if JobReferenceIds[i] is not None:
				self.add_query_param('JobReferenceId.' + str(i + 1) , JobReferenceIds[i]);

	def get_JobIds(self):
		return self.get_query_params().get('JobIds')

	def set_JobIds(self,JobIds):
		for i in range(len(JobIds)):	
			if JobIds[i] is not None:
				self.add_query_param('JobId.' + str(i + 1) , JobIds[i]);

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_JobGroupId(self):
		return self.get_query_params().get('JobGroupId')

	def set_JobGroupId(self,JobGroupId):
		self.add_query_param('JobGroupId',JobGroupId)

	def get_ScenarioId(self):
		return self.get_query_params().get('ScenarioId')

	def set_ScenarioId(self,ScenarioId):
		self.add_query_param('ScenarioId',ScenarioId)