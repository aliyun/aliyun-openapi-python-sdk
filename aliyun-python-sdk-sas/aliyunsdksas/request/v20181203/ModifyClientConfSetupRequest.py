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

class ModifyClientConfSetupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ModifyClientConfSetup','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StrategyConfig(self): # String
		return self.get_query_params().get('StrategyConfig')

	def set_StrategyConfig(self, StrategyConfig):  # String
		self.add_query_param('StrategyConfig', StrategyConfig)
	def get_StrategyTag(self): # String
		return self.get_query_params().get('StrategyTag')

	def set_StrategyTag(self, StrategyTag):  # String
		self.add_query_param('StrategyTag', StrategyTag)
	def get_StrategyTagValue(self): # String
		return self.get_query_params().get('StrategyTagValue')

	def set_StrategyTagValue(self, StrategyTagValue):  # String
		self.add_query_param('StrategyTagValue', StrategyTagValue)
