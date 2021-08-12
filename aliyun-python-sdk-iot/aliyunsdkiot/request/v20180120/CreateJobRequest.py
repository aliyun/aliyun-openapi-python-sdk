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
from aliyunsdkiot.endpoint import endpoint_data

class CreateJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateJob','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_JobDocument(self):
		return self.get_query_params().get('JobDocument')

	def set_JobDocument(self,JobDocument):
		self.add_query_param('JobDocument',JobDocument)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_RolloutConfig(self):
		return self.get_query_params().get('RolloutConfig')

	def set_RolloutConfig(self,RolloutConfig):
		self.add_query_param('RolloutConfig',RolloutConfig)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_JobName(self):
		return self.get_query_params().get('JobName')

	def set_JobName(self,JobName):
		self.add_query_param('JobName',JobName)

	def get_TimeoutConfig(self):
		return self.get_query_params().get('TimeoutConfig')

	def set_TimeoutConfig(self,TimeoutConfig):
		self.add_query_param('TimeoutConfig',TimeoutConfig)

	def get_TargetConfig(self):
		return self.get_query_params().get('TargetConfig')

	def set_TargetConfig(self,TargetConfig):
		self.add_query_param('TargetConfig',TargetConfig)

	def get_JobFile(self):
		return self.get_query_params().get('JobFile')

	def set_JobFile(self,JobFile):
		self.add_query_param('JobFile',JobFile)

	def get_ScheduledTime(self):
		return self.get_query_params().get('ScheduledTime')

	def set_ScheduledTime(self,ScheduledTime):
		self.add_query_param('ScheduledTime',ScheduledTime)