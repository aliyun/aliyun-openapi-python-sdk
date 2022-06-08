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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class AddDesensitizationRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'AddDesensitizationRule','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RuleDescription(self): # String
		return self.get_query_params().get('RuleDescription')

	def set_RuleDescription(self, RuleDescription):  # String
		self.add_query_param('RuleDescription', RuleDescription)
	def get_FunctionParams(self): # Array
		return self.get_body_params().get('FunctionParams')

	def set_FunctionParams(self, FunctionParams):  # Array
		for index1, value1 in enumerate(FunctionParams):
			for key2, value2 in value1.items():
				self.add_body_params('FunctionParams.' + str(index1 + 1) , value2)
	def get_RuleType(self): # String
		return self.get_query_params().get('RuleType')

	def set_RuleType(self, RuleType):  # String
		self.add_query_param('RuleType', RuleType)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_FunctionType(self): # String
		return self.get_query_params().get('FunctionType')

	def set_FunctionType(self, FunctionType):  # String
		self.add_query_param('FunctionType', FunctionType)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
