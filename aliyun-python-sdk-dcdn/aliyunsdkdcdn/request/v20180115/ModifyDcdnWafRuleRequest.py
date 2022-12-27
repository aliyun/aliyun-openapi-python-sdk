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
from aliyunsdkdcdn.endpoint import endpoint_data

class ModifyDcdnWafRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dcdn', '2018-01-15', 'ModifyDcdnWafRule')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RuleConfig(self): # String
		return self.get_body_params().get('RuleConfig')

	def set_RuleConfig(self, RuleConfig):  # String
		self.add_body_params('RuleConfig', RuleConfig)
	def get_RuleStatus(self): # String
		return self.get_body_params().get('RuleStatus')

	def set_RuleStatus(self, RuleStatus):  # String
		self.add_body_params('RuleStatus', RuleStatus)
	def get_RuleName(self): # String
		return self.get_body_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_body_params('RuleName', RuleName)
	def get_RuleId(self): # Long
		return self.get_body_params().get('RuleId')

	def set_RuleId(self, RuleId):  # Long
		self.add_body_params('RuleId', RuleId)
