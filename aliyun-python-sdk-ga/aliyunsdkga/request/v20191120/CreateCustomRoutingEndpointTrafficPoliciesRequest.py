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
from aliyunsdkga.endpoint import endpoint_data

class CreateCustomRoutingEndpointTrafficPoliciesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateCustomRoutingEndpointTrafficPolicies','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_EndpointId(self): # String
		return self.get_query_params().get('EndpointId')

	def set_EndpointId(self, EndpointId):  # String
		self.add_query_param('EndpointId', EndpointId)
	def get_PolicyConfigurationss(self): # RepeatList
		return self.get_query_params().get('PolicyConfigurations')

	def set_PolicyConfigurationss(self, PolicyConfigurations):  # RepeatList
		for depth1 in range(len(PolicyConfigurations)):
			if PolicyConfigurations[depth1].get('Address') is not None:
				self.add_query_param('PolicyConfigurations.' + str(depth1 + 1) + '.Address', PolicyConfigurations[depth1].get('Address'))
			if PolicyConfigurations[depth1].get('PortRanges') is not None:
				for depth2 in range(len(PolicyConfigurations[depth1].get('PortRanges'))):
					if PolicyConfigurations[depth1].get('PortRanges')[depth2].get('FromPort') is not None:
						self.add_query_param('PolicyConfigurations.' + str(depth1 + 1) + '.PortRanges.'  + str(depth2 + 1) + '.FromPort', PolicyConfigurations[depth1].get('PortRanges')[depth2].get('FromPort'))
					if PolicyConfigurations[depth1].get('PortRanges')[depth2].get('ToPort') is not None:
						self.add_query_param('PolicyConfigurations.' + str(depth1 + 1) + '.PortRanges.'  + str(depth2 + 1) + '.ToPort', PolicyConfigurations[depth1].get('PortRanges')[depth2].get('ToPort'))
