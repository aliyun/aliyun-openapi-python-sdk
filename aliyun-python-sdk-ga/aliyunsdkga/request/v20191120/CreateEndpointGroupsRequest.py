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

class CreateEndpointGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateEndpointGroups','gaplus')
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
			if EndpointGroupConfigurations[depth1].get('EndpointGroupName') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointGroupName', EndpointGroupConfigurations[depth1].get('EndpointGroupName'))
			if EndpointGroupConfigurations[depth1].get('EndpointGroupDescription') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointGroupDescription', EndpointGroupConfigurations[depth1].get('EndpointGroupDescription'))
			if EndpointGroupConfigurations[depth1].get('EndpointGroupRegion') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointGroupRegion', EndpointGroupConfigurations[depth1].get('EndpointGroupRegion'))
			if EndpointGroupConfigurations[depth1].get('TrafficPercentage') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.TrafficPercentage', EndpointGroupConfigurations[depth1].get('TrafficPercentage'))
			if EndpointGroupConfigurations[depth1].get('HealthCheckEnabled') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.HealthCheckEnabled', EndpointGroupConfigurations[depth1].get('HealthCheckEnabled'))
			if EndpointGroupConfigurations[depth1].get('HealthCheckIntervalSeconds') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.HealthCheckIntervalSeconds', EndpointGroupConfigurations[depth1].get('HealthCheckIntervalSeconds'))
			if EndpointGroupConfigurations[depth1].get('HealthCheckPath') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.HealthCheckPath', EndpointGroupConfigurations[depth1].get('HealthCheckPath'))
			if EndpointGroupConfigurations[depth1].get('HealthCheckPort') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.HealthCheckPort', EndpointGroupConfigurations[depth1].get('HealthCheckPort'))
			if EndpointGroupConfigurations[depth1].get('HealthCheckProtocol') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.HealthCheckProtocol', EndpointGroupConfigurations[depth1].get('HealthCheckProtocol'))
			if EndpointGroupConfigurations[depth1].get('ThresholdCount') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.ThresholdCount', EndpointGroupConfigurations[depth1].get('ThresholdCount'))
			if EndpointGroupConfigurations[depth1].get('EndpointConfigurations') is not None:
				for depth2 in range(len(EndpointGroupConfigurations[depth1].get('EndpointConfigurations'))):
					if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Type') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointConfigurations.'  + str(depth2 + 1) + '.Type', EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Type'))
					if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Weight') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointConfigurations.'  + str(depth2 + 1) + '.Weight', EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Weight'))
					if EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Endpoint') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointConfigurations.'  + str(depth2 + 1) + '.Endpoint', EndpointGroupConfigurations[depth1].get('EndpointConfigurations')[depth2].get('Endpoint'))
			if EndpointGroupConfigurations[depth1].get('EndpointRequestProtocol') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointRequestProtocol', EndpointGroupConfigurations[depth1].get('EndpointRequestProtocol'))
			if EndpointGroupConfigurations[depth1].get('EndpointGroupType') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EndpointGroupType', EndpointGroupConfigurations[depth1].get('EndpointGroupType'))
			if EndpointGroupConfigurations[depth1].get('PortOverrides') is not None:
				for depth2 in range(len(EndpointGroupConfigurations[depth1].get('PortOverrides'))):
					if EndpointGroupConfigurations[depth1].get('PortOverrides')[depth2].get('ListenerPort') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.PortOverrides.'  + str(depth2 + 1) + '.ListenerPort', EndpointGroupConfigurations[depth1].get('PortOverrides')[depth2].get('ListenerPort'))
					if EndpointGroupConfigurations[depth1].get('PortOverrides')[depth2].get('EndpointPort') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.PortOverrides.'  + str(depth2 + 1) + '.EndpointPort', EndpointGroupConfigurations[depth1].get('PortOverrides')[depth2].get('EndpointPort'))
			if EndpointGroupConfigurations[depth1].get('EnableClientIPPreservationToa') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EnableClientIPPreservationToa', EndpointGroupConfigurations[depth1].get('EnableClientIPPreservationToa'))
			if EndpointGroupConfigurations[depth1].get('EnableClientIPPreservationProxyProtocol') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(depth1 + 1) + '.EnableClientIPPreservationProxyProtocol', EndpointGroupConfigurations[depth1].get('EnableClientIPPreservationProxyProtocol'))
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_AcceleratorId(self): # String
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self, AcceleratorId):  # String
		self.add_query_param('AcceleratorId', AcceleratorId)
