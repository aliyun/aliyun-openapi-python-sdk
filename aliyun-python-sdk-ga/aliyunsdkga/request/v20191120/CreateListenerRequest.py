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

class CreateListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateListener','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_CustomRoutingEndpointGroupConfigurations(self): # Array
		return self.get_query_params().get('CustomRoutingEndpointGroupConfigurations')

	def set_CustomRoutingEndpointGroupConfigurations(self, CustomRoutingEndpointGroupConfigurations):  # Array
		for index1, value1 in enumerate(CustomRoutingEndpointGroupConfigurations):
			if value1.get('EndpointGroupRegion') is not None:
				self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointGroupRegion', value1.get('EndpointGroupRegion'))
			if value1.get('Name') is not None:
				self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.Name', value1.get('Name'))
			if value1.get('Description') is not None:
				self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.Description', value1.get('Description'))
			if value1.get('DestinationConfigurations') is not None:
				for index2, value2 in enumerate(value1.get('DestinationConfigurations')):
					if value2.get('Protocols') is not None:
						for index3, value3 in enumerate(value2.get('Protocols')):
							self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.DestinationConfigurations.' + str(index2 + 1) + '.Protocols.' + str(index3 + 1), value3)
					if value2.get('FromPort') is not None:
						self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.DestinationConfigurations.' + str(index2 + 1) + '.FromPort', value2.get('FromPort'))
					if value2.get('ToPort') is not None:
						self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.DestinationConfigurations.' + str(index2 + 1) + '.ToPort', value2.get('ToPort'))
			if value1.get('EndpointConfigurations') is not None:
				for index2, value2 in enumerate(value1.get('EndpointConfigurations')):
					if value2.get('Type') is not None:
						self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointConfigurations.' + str(index2 + 1) + '.Type', value2.get('Type'))
					if value2.get('Endpoint') is not None:
						self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointConfigurations.' + str(index2 + 1) + '.Endpoint', value2.get('Endpoint'))
					if value2.get('TrafficToEndpointPolicy') is not None:
						self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointConfigurations.' + str(index2 + 1) + '.TrafficToEndpointPolicy', value2.get('TrafficToEndpointPolicy'))
					if value2.get('PolicyConfigurations') is not None:
						for index3, value3 in enumerate(value2.get('PolicyConfigurations')):
							if value3.get('Address') is not None:
								self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointConfigurations.' + str(index2 + 1) + '.PolicyConfigurations.' + str(index3 + 1) + '.Address', value3.get('Address'))
							if value3.get('PortRanges') is not None:
								for index4, value4 in enumerate(value3.get('PortRanges')):
									if value4.get('FromPort') is not None:
										self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointConfigurations.' + str(index2 + 1) + '.PolicyConfigurations.' + str(index3 + 1) + '.PortRanges.' + str(index4 + 1) + '.FromPort', value4.get('FromPort'))
									if value4.get('ToPort') is not None:
										self.add_query_param('CustomRoutingEndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointConfigurations.' + str(index2 + 1) + '.PolicyConfigurations.' + str(index3 + 1) + '.PortRanges.' + str(index4 + 1) + '.ToPort', value4.get('ToPort'))
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Protocol(self): # String
		return self.get_query_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_query_param('Protocol', Protocol)
	def get_AcceleratorId(self): # String
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self, AcceleratorId):  # String
		self.add_query_param('AcceleratorId', AcceleratorId)
	def get_EndpointGroupConfigurations(self): # Array
		return self.get_query_params().get('EndpointGroupConfigurations')

	def set_EndpointGroupConfigurations(self, EndpointGroupConfigurations):  # Array
		for index1, value1 in enumerate(EndpointGroupConfigurations):
			if value1.get('EndpointGroupName') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointGroupName', value1.get('EndpointGroupName'))
			if value1.get('EndpointGroupDescription') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointGroupDescription', value1.get('EndpointGroupDescription'))
			if value1.get('EndpointGroupRegion') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointGroupRegion', value1.get('EndpointGroupRegion'))
			if value1.get('TrafficPercentage') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.TrafficPercentage', value1.get('TrafficPercentage'))
			if value1.get('HealthCheckEnabled') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.HealthCheckEnabled', value1.get('HealthCheckEnabled'))
			if value1.get('HealthCheckIntervalSeconds') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.HealthCheckIntervalSeconds', value1.get('HealthCheckIntervalSeconds'))
			if value1.get('HealthCheckPath') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.HealthCheckPath', value1.get('HealthCheckPath'))
			if value1.get('HealthCheckPort') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.HealthCheckPort', value1.get('HealthCheckPort'))
			if value1.get('HealthCheckProtocol') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.HealthCheckProtocol', value1.get('HealthCheckProtocol'))
			if value1.get('ThresholdCount') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.ThresholdCount', value1.get('ThresholdCount'))
			if value1.get('EndpointConfigurations') is not None:
				for index2, value2 in enumerate(value1.get('EndpointConfigurations')):
					if value2.get('Type') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointConfigurations.' + str(index2 + 1) + '.Type', value2.get('Type'))
					if value2.get('Weight') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointConfigurations.' + str(index2 + 1) + '.Weight', value2.get('Weight'))
					if value2.get('Endpoint') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointConfigurations.' + str(index2 + 1) + '.Endpoint', value2.get('Endpoint'))
			if value1.get('EndpointRequestProtocol') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointRequestProtocol', value1.get('EndpointRequestProtocol'))
			if value1.get('EndpointGroupType') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EndpointGroupType', value1.get('EndpointGroupType'))
			if value1.get('PortOverrides') is not None:
				for index2, value2 in enumerate(value1.get('PortOverrides')):
					if value2.get('ListenerPort') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.PortOverrides.' + str(index2 + 1) + '.ListenerPort', value2.get('ListenerPort'))
					if value2.get('EndpointPort') is not None:
						self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.PortOverrides.' + str(index2 + 1) + '.EndpointPort', value2.get('EndpointPort'))
			if value1.get('EnableClientIPPreservationToa') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EnableClientIPPreservationToa', value1.get('EnableClientIPPreservationToa'))
			if value1.get('EnableClientIPPreservationProxyProtocol') is not None:
				self.add_query_param('EndpointGroupConfigurations.' + str(index1 + 1) + '.EnableClientIPPreservationProxyProtocol', value1.get('EnableClientIPPreservationProxyProtocol'))
	def get_XForwardedForConfig(self): # Struct
		return self.get_query_params().get('XForwardedForConfig')

	def set_XForwardedForConfig(self, XForwardedForConfig):  # Struct
		if XForwardedForConfig.get('XForwardedForGaIdEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForGaIdEnabled', XForwardedForConfig.get('XForwardedForGaIdEnabled'))
		if XForwardedForConfig.get('XForwardedForGaApEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForGaApEnabled', XForwardedForConfig.get('XForwardedForGaApEnabled'))
		if XForwardedForConfig.get('XForwardedForProtoEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForProtoEnabled', XForwardedForConfig.get('XForwardedForProtoEnabled'))
		if XForwardedForConfig.get('XForwardedForPortEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForPortEnabled', XForwardedForConfig.get('XForwardedForPortEnabled'))
		if XForwardedForConfig.get('XRealIpEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XRealIpEnabled', XForwardedForConfig.get('XRealIpEnabled'))
	def get_SecurityPolicyId(self): # String
		return self.get_query_params().get('SecurityPolicyId')

	def set_SecurityPolicyId(self, SecurityPolicyId):  # String
		self.add_query_param('SecurityPolicyId', SecurityPolicyId)
	def get_ProxyProtocol(self): # Boolean
		return self.get_query_params().get('ProxyProtocol')

	def set_ProxyProtocol(self, ProxyProtocol):  # Boolean
		self.add_query_param('ProxyProtocol', ProxyProtocol)
	def get_PortRangess(self): # RepeatList
		return self.get_query_params().get('PortRanges')

	def set_PortRangess(self, PortRanges):  # RepeatList
		for depth1 in range(len(PortRanges)):
			if PortRanges[depth1].get('FromPort') is not None:
				self.add_query_param('PortRanges.' + str(depth1 + 1) + '.FromPort', PortRanges[depth1].get('FromPort'))
			if PortRanges[depth1].get('ToPort') is not None:
				self.add_query_param('PortRanges.' + str(depth1 + 1) + '.ToPort', PortRanges[depth1].get('ToPort'))
	def get_Certificatess(self): # RepeatList
		return self.get_query_params().get('Certificates')

	def set_Certificatess(self, Certificates):  # RepeatList
		for depth1 in range(len(Certificates)):
			if Certificates[depth1].get('Id') is not None:
				self.add_query_param('Certificates.' + str(depth1 + 1) + '.Id', Certificates[depth1].get('Id'))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ClientAffinity(self): # String
		return self.get_query_params().get('ClientAffinity')

	def set_ClientAffinity(self, ClientAffinity):  # String
		self.add_query_param('ClientAffinity', ClientAffinity)
