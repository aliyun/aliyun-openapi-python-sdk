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
from aliyunsdkccc.endpoint import endpoint_data

class CreatePredictiveJobGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'CreatePredictiveJobGroup','CCC')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_TimingSchedule(self):
		return self.get_query_params().get('TimingSchedule')

	def set_TimingSchedule(self,TimingSchedule):
		self.add_query_param('TimingSchedule',TimingSchedule)

	def get_JobsJsons(self):
		return self.get_body_params().get('JobsJson')

	def set_JobsJsons(self, JobsJsons):
		for depth1 in range(len(JobsJsons)):
			if JobsJsons[depth1] is not None:
				self.add_body_params('JobsJson.' + str(depth1 + 1) , JobsJsons[depth1])

	def get_JobFilePath(self):
		return self.get_query_params().get('JobFilePath')

	def set_JobFilePath(self,JobFilePath):
		self.add_query_param('JobFilePath',JobFilePath)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_IsDraft(self):
		return self.get_query_params().get('IsDraft')

	def set_IsDraft(self,IsDraft):
		self.add_query_param('IsDraft',IsDraft)

	def get_SkillGroupId(self):
		return self.get_query_params().get('SkillGroupId')

	def set_SkillGroupId(self,SkillGroupId):
		self.add_query_param('SkillGroupId',SkillGroupId)

	def get_StrategyJson(self):
		return self.get_query_params().get('StrategyJson')

	def set_StrategyJson(self,StrategyJson):
		self.add_query_param('StrategyJson',StrategyJson)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)