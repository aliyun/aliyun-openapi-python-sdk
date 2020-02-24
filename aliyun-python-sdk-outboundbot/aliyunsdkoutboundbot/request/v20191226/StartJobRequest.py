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

class StartJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'StartJob','outboundbot')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_JobJson(self):
		return self.get_query_params().get('JobJson')

	def set_JobJson(self,JobJson):
		self.add_query_param('JobJson',JobJson)

	def get_CallingNumbers(self):
		return self.get_query_params().get('CallingNumbers')

	def set_CallingNumbers(self,CallingNumbers):
		for i in range(len(CallingNumbers)):	
			if CallingNumbers[i] is not None:
				self.add_query_param('CallingNumber.' + str(i + 1) , CallingNumbers[i]);

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_JobGroupId(self):
		return self.get_query_params().get('JobGroupId')

	def set_JobGroupId(self,JobGroupId):
		self.add_query_param('JobGroupId',JobGroupId)

	def get_SelfHostedCallCenter(self):
		return self.get_query_params().get('SelfHostedCallCenter')

	def set_SelfHostedCallCenter(self,SelfHostedCallCenter):
		self.add_query_param('SelfHostedCallCenter',SelfHostedCallCenter)

	def get_ScenarioId(self):
		return self.get_query_params().get('ScenarioId')

	def set_ScenarioId(self,ScenarioId):
		self.add_query_param('ScenarioId',ScenarioId)