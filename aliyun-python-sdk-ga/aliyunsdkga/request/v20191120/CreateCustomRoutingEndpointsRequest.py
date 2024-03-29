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

class CreateCustomRoutingEndpointsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateCustomRoutingEndpoints','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_EndpointConfigurationss(self): # RepeatList
		return self.get_query_params().get('EndpointConfigurations')

	def set_EndpointConfigurationss(self, EndpointConfigurations):  # RepeatList
		for depth1 in range(len(EndpointConfigurations)):
			if EndpointConfigurations[depth1].get('Type') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.Type', EndpointConfigurations[depth1].get('Type'))
			if EndpointConfigurations[depth1].get('Endpoint') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.Endpoint', EndpointConfigurations[depth1].get('Endpoint'))
			if EndpointConfigurations[depth1].get('TrafficToEndpointPolicy') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.TrafficToEndpointPolicy', EndpointConfigurations[depth1].get('TrafficToEndpointPolicy'))
			if EndpointConfigurations[depth1].get('PolicyConfigurations') is not None:
				for depth2 in range(len(EndpointConfigurations[depth1].get('PolicyConfigurations'))):
					if EndpointConfigurations[depth1].get('PolicyConfigurations')[depth2].get('Address') is not None:
						self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.PolicyConfigurations.'  + str(depth2 + 1) + '.Address', EndpointConfigurations[depth1].get('PolicyConfigurations')[depth2].get('Address'))
					if EndpointConfigurations[depth1].get('PolicyConfigurations')[depth2].get('PortRanges') is not None:
						for depth3 in range(len(EndpointConfigurations[depth1].get('PolicyConfigurations')[depth2].get('PortRanges'))):
							if EndpointConfigurations[depth1].get('PolicyConfigurations')[depth2].get('PortRanges')[depth3].get('FromPort') is not None:
								self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.PolicyConfigurations.'  + str(depth2 + 1) + '.PortRanges.'  + str(depth3 + 1) + '.FromPort', EndpointConfigurations[depth1].get('PolicyConfigurations')[depth2].get('PortRanges')[depth3].get('FromPort'))
							if EndpointConfigurations[depth1].get('PolicyConfigurations')[depth2].get('PortRanges')[depth3].get('ToPort') is not None:
								self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.PolicyConfigurations.'  + str(depth2 + 1) + '.PortRanges.'  + str(depth3 + 1) + '.ToPort', EndpointConfigurations[depth1].get('PolicyConfigurations')[depth2].get('PortRanges')[depth3].get('ToPort'))
	def get_EndpointGroupId(self): # String
		return self.get_query_params().get('EndpointGroupId')

	def set_EndpointGroupId(self, EndpointGroupId):  # String
		self.add_query_param('EndpointGroupId', EndpointGroupId)
