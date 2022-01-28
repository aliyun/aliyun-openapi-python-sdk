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

class CreateCampaignRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'CreateCampaign')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_QueueId(self):
		return self.get_query_params().get('QueueId')

	def set_QueueId(self,QueueId):
		self.add_query_param('QueueId',QueueId)

	def get_ContactFlowId(self):
		return self.get_query_params().get('ContactFlowId')

	def set_ContactFlowId(self,ContactFlowId):
		self.add_query_param('ContactFlowId',ContactFlowId)

	def get_Simulation(self):
		return self.get_query_params().get('Simulation')

	def set_Simulation(self,Simulation):
		self.add_query_param('Simulation',Simulation)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_MaxAttemptCount(self):
		return self.get_query_params().get('MaxAttemptCount')

	def set_MaxAttemptCount(self,MaxAttemptCount):
		self.add_query_param('MaxAttemptCount',MaxAttemptCount)

	def get_StrategyParameters(self):
		return self.get_query_params().get('StrategyParameters')

	def set_StrategyParameters(self,StrategyParameters):
		self.add_query_param('StrategyParameters',StrategyParameters)

	def get_CaseFileKey(self):
		return self.get_query_params().get('CaseFileKey')

	def set_CaseFileKey(self,CaseFileKey):
		self.add_query_param('CaseFileKey',CaseFileKey)

	def get_MinAttemptInterval(self):
		return self.get_query_params().get('MinAttemptInterval')

	def set_MinAttemptInterval(self,MinAttemptInterval):
		self.add_query_param('MinAttemptInterval',MinAttemptInterval)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_SimulationParameters(self):
		return self.get_query_params().get('SimulationParameters')

	def set_SimulationParameters(self,SimulationParameters):
		self.add_query_param('SimulationParameters',SimulationParameters)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_StrategyType(self):
		return self.get_query_params().get('StrategyType')

	def set_StrategyType(self,StrategyType):
		self.add_query_param('StrategyType',StrategyType)

	def get_CaseList(self):
		return self.get_query_params().get('CaseList')

	def set_CaseList(self,CaseList):
		self.add_query_param('CaseList',CaseList)

	def get_CallableTime(self):
		return self.get_query_params().get('CallableTime')

	def set_CallableTime(self,CallableTime):
		self.add_query_param('CallableTime',CallableTime)