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

class UpdateEndpointGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'UpdateEndpointGroup','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PortOverridess(self): # RepeatList
		return self.get_query_params().get('PortOverrides')

	def set_PortOverridess(self, PortOverrides):  # RepeatList
		for depth1 in range(len(PortOverrides)):
			if PortOverrides[depth1].get('ListenerPort') is not None:
				self.add_query_param('PortOverrides.' + str(depth1 + 1) + '.ListenerPort', PortOverrides[depth1].get('ListenerPort'))
			if PortOverrides[depth1].get('EndpointPort') is not None:
				self.add_query_param('PortOverrides.' + str(depth1 + 1) + '.EndpointPort', PortOverrides[depth1].get('EndpointPort'))
	def get_HealthCheckEnabled(self): # Boolean
		return self.get_query_params().get('HealthCheckEnabled')

	def set_HealthCheckEnabled(self, HealthCheckEnabled):  # Boolean
		self.add_query_param('HealthCheckEnabled', HealthCheckEnabled)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_HealthCheckIntervalSeconds(self): # Integer
		return self.get_query_params().get('HealthCheckIntervalSeconds')

	def set_HealthCheckIntervalSeconds(self, HealthCheckIntervalSeconds):  # Integer
		self.add_query_param('HealthCheckIntervalSeconds', HealthCheckIntervalSeconds)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_HealthCheckProtocol(self): # String
		return self.get_query_params().get('HealthCheckProtocol')

	def set_HealthCheckProtocol(self, HealthCheckProtocol):  # String
		self.add_query_param('HealthCheckProtocol', HealthCheckProtocol)
	def get_EndpointRequestProtocol(self): # String
		return self.get_query_params().get('EndpointRequestProtocol')

	def set_EndpointRequestProtocol(self, EndpointRequestProtocol):  # String
		self.add_query_param('EndpointRequestProtocol', EndpointRequestProtocol)
	def get_HealthCheckPath(self): # String
		return self.get_query_params().get('HealthCheckPath')

	def set_HealthCheckPath(self, HealthCheckPath):  # String
		self.add_query_param('HealthCheckPath', HealthCheckPath)
	def get_EndpointConfigurationss(self): # RepeatList
		return self.get_query_params().get('EndpointConfigurations')

	def set_EndpointConfigurationss(self, EndpointConfigurations):  # RepeatList
		for depth1 in range(len(EndpointConfigurations)):
			if EndpointConfigurations[depth1].get('Type') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.Type', EndpointConfigurations[depth1].get('Type'))
			if EndpointConfigurations[depth1].get('EnableClientIPPreservation') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.EnableClientIPPreservation', EndpointConfigurations[depth1].get('EnableClientIPPreservation'))
			if EndpointConfigurations[depth1].get('Weight') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.Weight', EndpointConfigurations[depth1].get('Weight'))
			if EndpointConfigurations[depth1].get('EnableProxyProtocol') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.EnableProxyProtocol', EndpointConfigurations[depth1].get('EnableProxyProtocol'))
			if EndpointConfigurations[depth1].get('Endpoint') is not None:
				self.add_query_param('EndpointConfigurations.' + str(depth1 + 1) + '.Endpoint', EndpointConfigurations[depth1].get('Endpoint'))
	def get_EndpointGroupId(self): # String
		return self.get_query_params().get('EndpointGroupId')

	def set_EndpointGroupId(self, EndpointGroupId):  # String
		self.add_query_param('EndpointGroupId', EndpointGroupId)
	def get_TrafficPercentage(self): # Integer
		return self.get_query_params().get('TrafficPercentage')

	def set_TrafficPercentage(self, TrafficPercentage):  # Integer
		self.add_query_param('TrafficPercentage', TrafficPercentage)
	def get_HealthCheckPort(self): # Integer
		return self.get_query_params().get('HealthCheckPort')

	def set_HealthCheckPort(self, HealthCheckPort):  # Integer
		self.add_query_param('HealthCheckPort', HealthCheckPort)
	def get_ThresholdCount(self): # Integer
		return self.get_query_params().get('ThresholdCount')

	def set_ThresholdCount(self, ThresholdCount):  # Integer
		self.add_query_param('ThresholdCount', ThresholdCount)
	def get_EndpointGroupRegion(self): # String
		return self.get_query_params().get('EndpointGroupRegion')

	def set_EndpointGroupRegion(self, EndpointGroupRegion):  # String
		self.add_query_param('EndpointGroupRegion', EndpointGroupRegion)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
