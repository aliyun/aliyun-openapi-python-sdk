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

class ModifyOutboundCallNumberRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'ModifyOutboundCallNumber','outboundbot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OutboundCallNumberId(self):
		return self.get_query_params().get('OutboundCallNumberId')

	def set_OutboundCallNumberId(self,OutboundCallNumberId):
		self.add_query_param('OutboundCallNumberId',OutboundCallNumberId)

	def get_RateLimitCount(self):
		return self.get_query_params().get('RateLimitCount')

	def set_RateLimitCount(self,RateLimitCount):
		self.add_query_param('RateLimitCount',RateLimitCount)

	def get_Number(self):
		return self.get_query_params().get('Number')

	def set_Number(self,Number):
		self.add_query_param('Number',Number)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_RateLimitPeriod(self):
		return self.get_query_params().get('RateLimitPeriod')

	def set_RateLimitPeriod(self,RateLimitPeriod):
		self.add_query_param('RateLimitPeriod',RateLimitPeriod)