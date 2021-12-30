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

class CreateSurveyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'CreateSurvey')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Role(self):
		return self.get_query_params().get('Role')

	def set_Role(self,Role):
		self.add_query_param('Role',Role)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_SpeechOptimizationParam(self):
		return self.get_query_params().get('SpeechOptimizationParam')

	def set_SpeechOptimizationParam(self,SpeechOptimizationParam):
		self.add_query_param('SpeechOptimizationParam',SpeechOptimizationParam)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Round(self):
		return self.get_query_params().get('Round')

	def set_Round(self,Round):
		self.add_query_param('Round',Round)

	def get_FlowJson(self):
		return self.get_query_params().get('FlowJson')

	def set_FlowJson(self,FlowJson):
		self.add_query_param('FlowJson',FlowJson)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_GlobalQuestions(self):
		return self.get_query_params().get('GlobalQuestions')

	def set_GlobalQuestions(self,GlobalQuestions):
		self.add_query_param('GlobalQuestions',GlobalQuestions)

	def get_Corpora(self):
		return self.get_query_params().get('Corpora')

	def set_Corpora(self,Corpora):
		self.add_query_param('Corpora',Corpora)

	def get_ScenarioId(self):
		return self.get_query_params().get('ScenarioId')

	def set_ScenarioId(self,ScenarioId):
		self.add_query_param('ScenarioId',ScenarioId)