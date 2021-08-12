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

class UpdateRulesAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'UpdateRulesAttribute','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Rules(self): # Array
		return self.get_query_params().get('Rules')

	def set_Rules(self, Rules):  # Array
		for index1, value1 in enumerate(Rules):
			for key2, value2 in value1.items():
				for index3, value3 in enumerate(value2):
					for key4, value4 in value3.items():
						for key5, value5 in value4.items():
							for index6, value6 in enumerate(value5):
								self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.String', value6)
						for key5, value5 in value4.items():
							for index6, value6 in enumerate(value5):
								self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.String', value6)
						for key5, value5 in value4.items():
							for index6, value6 in enumerate(value5):
								self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.String', value6)
						for key5, value5 in value4.items():
							for index6, value6 in enumerate(value5):
								for key7, value7 in value6.items():
									self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.' + key7 + '.Value', value7)
									self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.' + key7 + '.Key', value7)
						for key5, value5 in value4.items():
							for index6, value6 in enumerate(value5):
								self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.String', value6)
						for key5, value5 in value4.items():
							for index6, value6 in enumerate(value5):
								self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.String', value6)
						for key5, value5 in value4.items():
							for index6, value6 in enumerate(value5):
								for key7, value7 in value6.items():
									self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.' + key7 + '.Value', value7)
									self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.' + key7 + '.Key', value7)
						self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.Type', value4)
						for key5, value5 in value4.items():
							for index6, value6 in enumerate(value5):
								self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.String', value6)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Key', value5)
						for key5, value5 in value4.items():
							for index6, value6 in enumerate(value5):
								self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.String', value6)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Key', value5)
				self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.RuleName', value2)
				self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.Priority', value2)
				self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.RuleId', value2)
				for index3, value3 in enumerate(value2):
					for key4, value4 in value3.items():
						for key5, value5 in value4.items():
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.HttpCode', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Content', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.ContentType', value5)
						for key5, value5 in value4.items():
							for key6, value6 in value5.items():
								for index7, value7 in enumerate(value6):
									for key8, value8 in value7.items():
										self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + key6 + '.' + str(index7 + 1) + '.' + key8 + '.ServerGroupId', value8)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.TargetType', value5)
						for key5, value5 in value4.items():
							for key6, value6 in value5.items():
								self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + key6 + '.Enabled', value6)
								self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + key6 + '.Timeout', value6)
							for index6, value6 in enumerate(value5):
								for key7, value7 in value6.items():
									self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.' + key7 + '.ServerGroupId', value7)
									self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.' + str(index6 + 1) + '.' + key7 + '.Weight', value7)
						for key5, value5 in value4.items():
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Key', value5)
						for key5, value5 in value4.items():
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.ValueType', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.CoverEnabled', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Value', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Key', value5)
						for key5, value5 in value4.items():
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.QPS', value5)
						for key5, value5 in value4.items():
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Path', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Protocol', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Port', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Query', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Host', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.HttpCode', value5)
						self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.Type', value4)
						self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.Order', value4)
						for key5, value5 in value4.items():
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Path', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Query', value5)
							self.add_query_param('Rules.' + str(index1 + 1) + '.' + key2 + '.' + str(index3 + 1) + '.' + key4 + '.' + key5 + '.Host', value5)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
