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

class CreateCustomRoutingEndpointGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateCustomRoutingEndpointGroups','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_EndpointGroupConfigurationss(self): # RepeatList
		return self.get_query_params().get('EndpointGroupConfigurations')

	def set_EndpointGroupConfigurationss(self, EndpointGroupConfigurations):  # RepeatList
		for depth1 in range(len(EndpointGroupConfigurations)):
			if EndpointGroupConfigurations[depth1].get('EndpointGroupRegion') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointGroupRegion', EndpointGroupConfigurations[depth1].get('EndpointGroupRegion'))
			if EndpointGroupConfigurations[depth1].get('Name') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.Name', EndpointGroupConfigurations[depth1].get('Name'))
			if EndpointGroupConfigurations[depth1].get('Description') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.Description', EndpointGroupConfigurations[depth1].get('Description'))
			if EndpointGroupConfigurations[depth1].get('DestinationConfigurations') is not None:
				for depth2 in range(len(EndpointGroupConfigurations[depth1].get('DestinationConfigurations'))):
					if EndpointGroupConfigurations[depth1].get('DestinationConfigurations')[depth2].get('Protocols') is not None:
						for depth3 in range(len(EndpointGroupConfigurations[depth1].get('DestinationConfigurations')[depth2].get('Protocols'))):
							self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.DestinationConfigurations.'  + str(depth2 + 1) + '.Protocols.' + str(depth3 + 1), EndpointGroupConfigurations[depth1].get('DestinationConfigurations')[depth2].get('Protocols')[depth3])
					if EndpointGroupConfigurations[depth1].get('DestinationConfigurations')[depth2].get('FromPort') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.DestinationConfigurations.'  + str(depth2 + 1) + '.FromPort', EndpointGroupConfigurations[depth1].get('DestinationConfigurations')[depth2].get('FromPort'))
					if EndpointGroupConfigurations[depth1].get('DestinationConfigurations')[depth2].get('ToPort') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.DestinationConfigurations.'  + str(depth2 + 1) + '.ToPort', EndpointGroupConfigurations[depth1].get('DestinationConfigurations')[depth2].get('ToPort'))
			if EndpointGroupConfigurations[depth1].get('EndpointConfigurations') is not None:
				for depth2 in range(len(EndpointGroupConfigurations[depth1].get('EndpointConfigurations'))):
					if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Type') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointConfigurations.'  + str(depth2 + 1) + '.Type', EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Type'))
					if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Endpoint') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointConfigurations.'  + str(depth2 + 1) + '.Endpoint', EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Endpoint'))
					if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('TrafficToEndpointPolicy') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointConfigurations.'  + str(depth2 + 1) + '.TrafficToEndpointPolicy', EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('TrafficToEndpointPolicy'))
					if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations') is not None:
						for depth3 in range(len(EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations'))):
							if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations')[depth3].get('Address') is not None:
								self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointConfigurations.'  + str(depth2 + 1) + '.PolicyConfigurations.'  + str(depth3 + 1) + '.Address', EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations')[depth3].get('Address'))
							if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations')[depth3].get('PortRanges') is not None:
								for depth4 in range(len(EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations')[depth3].get('PortRanges'))):
									if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations')[depth3].get('PortRanges')[depth4].get('FromPort') is not None:
										self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointConfigurations.'  + str(depth2 + 1) + '.PolicyConfigurations.'  + str(depth3 + 1) + '.PortRanges.'  + str(depth4 + 1) + '.FromPort', EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations')[depth3].get('PortRanges')[depth4].get('FromPort'))
									if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations')[depth3].get('PortRanges')[depth4].get('ToPort') is not None:
										self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointConfigurations.'  + str(depth2 + 1) + '.PolicyConfigurations.'  + str(depth3 + 1) + '.PortRanges.'  + str(depth4 + 1) + '.ToPort', EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('PolicyConfigurations')[depth3].get('PortRanges')[depth4].get('ToPort'))
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_AcceleratorId(self): # String
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self, AcceleratorId):  # String
		self.add_query_param('AcceleratorId', AcceleratorId)
