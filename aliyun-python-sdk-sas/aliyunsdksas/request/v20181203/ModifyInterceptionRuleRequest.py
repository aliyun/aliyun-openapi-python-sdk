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

class ModifyInterceptionRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ModifyInterceptionRule','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_OrderIndex(self): # Long
		return self.get_query_params().get('OrderIndex')

	def set_OrderIndex(self, OrderIndex):  # Long
		self.add_query_param('OrderIndex', OrderIndex)
	def get_DstTarget(self): # String
		return self.get_query_params().get('DstTarget')

	def set_DstTarget(self, DstTarget):  # String
		self.add_query_param('DstTarget', DstTarget)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_InterceptType(self): # Integer
		return self.get_query_params().get('InterceptType')

	def set_InterceptType(self, InterceptType):  # Integer
		self.add_query_param('InterceptType', InterceptType)
	def get_RuleSwitch(self): # Integer
		return self.get_query_params().get('RuleSwitch')

	def set_RuleSwitch(self, RuleSwitch):  # Integer
		self.add_query_param('RuleSwitch', RuleSwitch)
	def get_RuleId(self): # Long
		return self.get_query_params().get('RuleId')

	def set_RuleId(self, RuleId):  # Long
		self.add_query_param('RuleId', RuleId)
	def get_SrcTarget(self): # String
		return self.get_query_params().get('SrcTarget')

	def set_SrcTarget(self, SrcTarget):  # String
		self.add_query_param('SrcTarget', SrcTarget)
