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
from aliyunsdkalb.endpoint import endpoint_data

class CreateRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'CreateRule','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_RuleActions(self): # Array
		return self.get_query_params().get('RuleActions')

	def set_RuleActions(self, RuleActions):  # Array
		for index1, value1 in enumerate(RuleActions):
			for key2, value2 in value1.items():
				for key3, value3 in value2.items():
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.HttpCode', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Content', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.ContentType', value3)
				for key3, value3 in value2.items():
					for index4, value4 in enumerate(value3):
						for key5, value5 in value4.items():
							self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.' + key5 + '.ServerGroupId', value5)
				for key3, value3 in value2.items():
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.ValueType', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Value', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Key', value3)
				for key3, value3 in value2.items():
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Path', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Protocol', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Port', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Query', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Host', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.HttpCode', value3)
				self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.Type', value2)
				self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.Order', value2)
				for key3, value3 in value2.items():
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Path', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Query', value3)
					self.add_query_param('RuleActions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Host', value3)
	def get_RuleConditions(self): # Array
		return self.get_query_params().get('RuleConditions')

	def set_RuleConditions(self, RuleConditions):  # Array
		for index1, value1 in enumerate(RuleConditions):
			for key2, value2 in value1.items():
				for key3, value3 in value2.items():
					for index4, value4 in enumerate(value3):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.String', value4)
				for key3, value3 in value2.items():
					for index4, value4 in enumerate(value3):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.String', value4)
				for key3, value3 in value2.items():
					for index4, value4 in enumerate(value3):
						for key5, value5 in value4.items():
							self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.' + key5 + '.Value', value5)
							self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.' + key5 + '.Key', value5)
				for key3, value3 in value2.items():
					for index4, value4 in enumerate(value3):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.String', value4)
				for key3, value3 in value2.items():
					for index4, value4 in enumerate(value3):
						for key5, value5 in value4.items():
							self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.' + key5 + '.Value', value5)
							self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.' + key5 + '.Key', value5)
				self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.Type', value2)
				for key3, value3 in value2.items():
					for index4, value4 in enumerate(value3):
						self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.' + str(index4 + 1) + '.String', value4)
					self.add_query_param('RuleConditions.' + str(index1 + 1) + '.' + key2 + '.' + key3 + '.Key', value3)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
