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

class UpdateListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'UpdateListener','gaplus')
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
	def get_BackendPortss(self): # RepeatList
		return self.get_query_params().get('BackendPorts')

	def set_BackendPortss(self, BackendPorts):  # RepeatList
		for depth1 in range(len(BackendPorts)):
			if BackendPorts[depth1].get('FromPort') is not None:
				self.add_query_param('BackendPorts.' + str(depth1 + 1) + '.FromPort', BackendPorts[depth1].get('FromPort'))
			if BackendPorts[depth1].get('ToPort') is not None:
				self.add_query_param('BackendPorts.' + str(depth1 + 1) + '.ToPort', BackendPorts[depth1].get('ToPort'))
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_Protocol(self): # String
		return self.get_query_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_query_param('Protocol', Protocol)
	def get_XForwardedForConfig(self): # Struct
		return self.get_query_params().get('XForwardedForConfig')

	def set_XForwardedForConfig(self, XForwardedForConfig):  # Struct
		if XForwardedForConfig.get('XForwardedForGaIdEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForGaIdEnabled', XForwardedForConfig.get('XForwardedForGaIdEnabled'))
		if XForwardedForConfig.get('XForwardedForProtoEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForProtoEnabled', XForwardedForConfig.get('XForwardedForProtoEnabled'))
		if XForwardedForConfig.get('XForwardedForPortEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForPortEnabled', XForwardedForConfig.get('XForwardedForPortEnabled'))
		if XForwardedForConfig.get('XRealIpEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XRealIpEnabled', XForwardedForConfig.get('XRealIpEnabled'))
		if XForwardedForConfig.get('XForwardedForGaApEnabled') is not None:
			self.add_query_param('XForwardedForConfig.XForwardedForGaApEnabled', XForwardedForConfig.get('XForwardedForGaApEnabled'))
	def get_SecurityPolicyId(self): # String
		return self.get_query_params().get('SecurityPolicyId')

	def set_SecurityPolicyId(self, SecurityPolicyId):  # String
		self.add_query_param('SecurityPolicyId', SecurityPolicyId)
	def get_ProxyProtocol(self): # String
		return self.get_query_params().get('ProxyProtocol')

	def set_ProxyProtocol(self, ProxyProtocol):  # String
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
