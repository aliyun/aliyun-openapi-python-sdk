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

class ListRealtimeAgentStatesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'ListRealtimeAgentStates','CCC')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CallTypeList(self): # String
		return self.get_query_params().get('CallTypeList')

	def set_CallTypeList(self, CallTypeList):  # String
		self.add_query_param('CallTypeList', CallTypeList)
	def get_Query(self): # String
		return self.get_query_params().get('Query')

	def set_Query(self, Query):  # String
		self.add_query_param('Query', Query)
	def get_OutboundScenario(self): # Boolean
		return self.get_query_params().get('OutboundScenario')

	def set_OutboundScenario(self, OutboundScenario):  # Boolean
		self.add_query_param('OutboundScenario', OutboundScenario)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_WorkModeList(self): # String
		return self.get_query_params().get('WorkModeList')

	def set_WorkModeList(self, WorkModeList):  # String
		self.add_query_param('WorkModeList', WorkModeList)
	def get_AgentIdList(self): # String
		return self.get_body_params().get('AgentIdList')

	def set_AgentIdList(self, AgentIdList):  # String
		self.add_body_params('AgentIdList', AgentIdList)
	def get_SkillGroupId(self): # String
		return self.get_query_params().get('SkillGroupId')

	def set_SkillGroupId(self, SkillGroupId):  # String
		self.add_query_param('SkillGroupId', SkillGroupId)
	def get_AgentName(self): # String
		return self.get_query_params().get('AgentName')

	def set_AgentName(self, AgentName):  # String
		self.add_query_param('AgentName', AgentName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_StateList(self): # String
		return self.get_body_params().get('StateList')

	def set_StateList(self, StateList):  # String
		self.add_body_params('StateList', StateList)
