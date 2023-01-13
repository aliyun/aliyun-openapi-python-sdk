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
from aliyunsdkoutboundbot.endpoint import endpoint_data

class ModifyEmptyNumberNoMoreCallsInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'ModifyEmptyNumberNoMoreCallsInfo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StrategyLevel(self): # Integer
		return self.get_query_params().get('StrategyLevel')

	def set_StrategyLevel(self, StrategyLevel):  # Integer
		self.add_query_param('StrategyLevel', StrategyLevel)
	def get_EmptyNumberNoMoreCalls(self): # Boolean
		return self.get_query_params().get('EmptyNumberNoMoreCalls')

	def set_EmptyNumberNoMoreCalls(self, EmptyNumberNoMoreCalls):  # Boolean
		self.add_query_param('EmptyNumberNoMoreCalls', EmptyNumberNoMoreCalls)
	def get_EntryId(self): # String
		return self.get_query_params().get('EntryId')

	def set_EntryId(self, EntryId):  # String
		self.add_query_param('EntryId', EntryId)
