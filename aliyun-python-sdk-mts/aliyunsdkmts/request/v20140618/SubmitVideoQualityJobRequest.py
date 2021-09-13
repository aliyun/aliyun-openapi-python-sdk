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
from aliyunsdkmts.endpoint import endpoint_data

class SubmitVideoQualityJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'SubmitVideoQualityJob','mts')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_JobParams(self):
		return self.get_query_params().get('JobParams')

	def set_JobParams(self,JobParams):
		self.add_query_param('JobParams',JobParams)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_Output(self):
		return self.get_query_params().get('Output')

	def set_Output(self,Output):
		self.add_query_param('Output',Output)

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_NotifyUrl(self):
		return self.get_query_params().get('NotifyUrl')

	def set_NotifyUrl(self,NotifyUrl):
		self.add_query_param('NotifyUrl',NotifyUrl)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_ModelId(self):
		return self.get_query_params().get('ModelId')

	def set_ModelId(self,ModelId):
		self.add_query_param('ModelId',ModelId)

	def get_PipelineId(self):
		return self.get_query_params().get('PipelineId')

	def set_PipelineId(self,PipelineId):
		self.add_query_param('PipelineId',PipelineId)

	def get_Input(self):
		return self.get_query_params().get('Input')

	def set_Input(self,Input):
		self.add_query_param('Input',Input)

	def get_ScheduleParams(self):
		return self.get_query_params().get('ScheduleParams')

	def set_ScheduleParams(self,ScheduleParams):
		self.add_query_param('ScheduleParams',ScheduleParams)