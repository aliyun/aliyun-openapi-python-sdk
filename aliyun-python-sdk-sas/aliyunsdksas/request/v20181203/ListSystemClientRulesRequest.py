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
from aliyunsdksas.endpoint import endpoint_data

class ListSystemClientRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ListSystemClientRules','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RuleTypess(self): # RepeatList
		return self.get_query_params().get('RuleTypes')

	def set_RuleTypess(self, RuleTypes):  # RepeatList
		for depth1 in range(len(RuleTypes)):
			self.add_query_param('RuleTypes.' + str(depth1 + 1), RuleTypes[depth1])
	def get_SystemType(self): # Integer
		return self.get_query_params().get('SystemType')

	def set_SystemType(self, SystemType):  # Integer
		self.add_query_param('SystemType', SystemType)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_IsContainer(self): # Integer
		return self.get_query_params().get('IsContainer')

	def set_IsContainer(self, IsContainer):  # Integer
		self.add_query_param('IsContainer', IsContainer)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_AggregationIdss(self): # RepeatList
		return self.get_query_params().get('AggregationIds')

	def set_AggregationIdss(self, AggregationIds):  # RepeatList
		for depth1 in range(len(AggregationIds)):
			self.add_query_param('AggregationIds.' + str(depth1 + 1), AggregationIds[depth1])
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
