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

class CreateEndpointGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateEndpointGroup','gaplus')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PortOverridess(self):
		return self.get_query_params().get('PortOverrides')

	def set_PortOverridess(self, PortOverridess):
		for depth1 in range(len(PortOverridess)):
			if PortOverridess[depth1].get('ListenerPort') is not None:
				self.add_query_param('PortOverrides.' + str(depth1 + 1) + '.ListenerPort', PortOverridess[depth1].get('ListenerPort'))
			if PortOverridess[depth1].get('EndpointPort') is not None:
				self.add_query_param('PortOverrides.' + str(depth1 + 1) + '.EndpointPort', PortOverridess[depth1].get('EndpointPort'))

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_HealthCheckIntervalSeconds(self):
		return self.get_query_params().get('HealthCheckIntervalSeconds')

	def set_HealthCheckIntervalSeconds(self,HealthCheckIntervalSeconds):
		self.add_query_param('HealthCheckIntervalSeconds',HealthCheckIntervalSeconds)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_HealthCheckProtocol(self):
		return self.get_query_params().get('HealthCheckProtocol')

	def set_HealthCheckProtocol(self,HealthCheckProtocol):
		self.add_query_param('HealthCheckProtocol',HealthCheckProtocol)

	def get_EndpointRequestProtocol(self):
		return self.get_query_params().get('EndpointRequestProtocol')

	def set_EndpointRequestProtocol(self,EndpointRequestProtocol):
		self.add_query_param('EndpointRequestProtocol',EndpointRequestProtocol)

	def get_ListenerId(self):
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self,ListenerId):
		self.add_query_param('ListenerId',ListenerId)

	def get_HealthCheckPath(self):
		return self.get_query_params().get('HealthCheckPath')

	def set_HealthCheckPath(self,HealthCheckPath):
		self.add_query_param('HealthCheckPath',HealthCheckPath)

	def get_EndpointConfigurationss(self):
		return self.get_query_params().get('EndpointConfigurations')

	def set_EndpointConfigurationss(self, EndpointConfigurationss):
		for depth1 in range(len(EndpointConfigurationss)):
			if EndpointConfigurationss[depth1].get('Type') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.Type', EndpointConfigurationss[depth1].get('Type'))
			if EndpointConfigurationss[depth1].get('EnableClientIPPreservation') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.EnableClientIPPreservation', EndpointConfigurationss[depth1].get('EnableClientIPPreservation'))
			if EndpointConfigurationss[depth1].get('Weight') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.Weight', EndpointConfigurationss[depth1].get('Weight'))
			if EndpointConfigurationss[depth1].get('EnableProxyProtocol') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.EnableProxyProtocol', EndpointConfigurationss[depth1].get('EnableProxyProtocol'))
			if EndpointConfigurationss[depth1].get('Endpoint') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.Endpoint', EndpointConfigurationss[depth1].get('Endpoint'))

	def get_EndpointGroupType(self):
		return self.get_query_params().get('EndpointGroupType')

	def set_EndpointGroupType(self,EndpointGroupType):
		self.add_query_param('EndpointGroupType',EndpointGroupType)

	def get_AcceleratorId(self):
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self,AcceleratorId):
		self.add_query_param('AcceleratorId',AcceleratorId)

	def get_TrafficPercentage(self):
		return self.get_query_params().get('TrafficPercentage')

	def set_TrafficPercentage(self,TrafficPercentage):
		self.add_query_param('TrafficPercentage',TrafficPercentage)

	def get_HealthCheckPort(self):
		return self.get_query_params().get('HealthCheckPort')

	def set_HealthCheckPort(self,HealthCheckPort):
		self.add_query_param('HealthCheckPort',HealthCheckPort)

	def get_ThresholdCount(self):
		return self.get_query_params().get('ThresholdCount')

	def set_ThresholdCount(self,ThresholdCount):
		self.add_query_param('ThresholdCount',ThresholdCount)

	def get_EndpointGroupRegion(self):
		return self.get_query_params().get('EndpointGroupRegion')

	def set_EndpointGroupRegion(self,EndpointGroupRegion):
		self.add_query_param('EndpointGroupRegion',EndpointGroupRegion)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)