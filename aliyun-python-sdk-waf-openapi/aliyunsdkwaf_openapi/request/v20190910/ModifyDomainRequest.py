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
from aliyunsdkwaf_openapi.endpoint import endpoint_data

class ModifyDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'waf-openapi', '2019-09-10', 'ModifyDomain','waf')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IpFollowStatus(self): # Integer
		return self.get_query_params().get('IpFollowStatus')

	def set_IpFollowStatus(self, IpFollowStatus):  # Integer
		self.add_query_param('IpFollowStatus', IpFollowStatus)
	def get_SniHost(self): # String
		return self.get_query_params().get('SniHost')

	def set_SniHost(self, SniHost):  # String
		self.add_query_param('SniHost', SniHost)
	def get_HttpPort(self): # String
		return self.get_query_params().get('HttpPort')

	def set_HttpPort(self, HttpPort):  # String
		self.add_query_param('HttpPort', HttpPort)
	def get_Http2Port(self): # String
		return self.get_query_params().get('Http2Port')

	def set_Http2Port(self, Http2Port):  # String
		self.add_query_param('Http2Port', Http2Port)
	def get_WriteTime(self): # Integer
		return self.get_query_params().get('WriteTime')

	def set_WriteTime(self, WriteTime):  # Integer
		self.add_query_param('WriteTime', WriteTime)
	def get_SniStatus(self): # Integer
		return self.get_query_params().get('SniStatus')

	def set_SniStatus(self, SniStatus):  # Integer
		self.add_query_param('SniStatus', SniStatus)
	def get_AccessHeaderMode(self): # Integer
		return self.get_query_params().get('AccessHeaderMode')

	def set_AccessHeaderMode(self, AccessHeaderMode):  # Integer
		self.add_query_param('AccessHeaderMode', AccessHeaderMode)
	def get_AccessType(self): # String
		return self.get_query_params().get('AccessType')

	def set_AccessType(self, AccessType):  # String
		self.add_query_param('AccessType', AccessType)
	def get_LogHeaders(self): # String
		return self.get_query_params().get('LogHeaders')

	def set_LogHeaders(self, LogHeaders):  # String
		self.add_query_param('LogHeaders', LogHeaders)
	def get_AccessHeaders(self): # String
		return self.get_query_params().get('AccessHeaders')

	def set_AccessHeaders(self, AccessHeaders):  # String
		self.add_query_param('AccessHeaders', AccessHeaders)
	def get_ConnectionTime(self): # Integer
		return self.get_query_params().get('ConnectionTime')

	def set_ConnectionTime(self, ConnectionTime):  # Integer
		self.add_query_param('ConnectionTime', ConnectionTime)
	def get_ClusterType(self): # Integer
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self, ClusterType):  # Integer
		self.add_query_param('ClusterType', ClusterType)
	def get_CloudNativeInstances(self): # String
		return self.get_query_params().get('CloudNativeInstances')

	def set_CloudNativeInstances(self, CloudNativeInstances):  # String
		self.add_query_param('CloudNativeInstances', CloudNativeInstances)
	def get_HttpsRedirect(self): # Integer
		return self.get_query_params().get('HttpsRedirect')

	def set_HttpsRedirect(self, HttpsRedirect):  # Integer
		self.add_query_param('HttpsRedirect', HttpsRedirect)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_SourceIps(self): # String
		return self.get_query_params().get('SourceIps')

	def set_SourceIps(self, SourceIps):  # String
		self.add_query_param('SourceIps', SourceIps)
	def get_Domain(self): # String
		return self.get_query_params().get('Domain')

	def set_Domain(self, Domain):  # String
		self.add_query_param('Domain', Domain)
	def get_IsAccessProduct(self): # Integer
		return self.get_query_params().get('IsAccessProduct')

	def set_IsAccessProduct(self, IsAccessProduct):  # Integer
		self.add_query_param('IsAccessProduct', IsAccessProduct)
	def get_ReadTime(self): # Integer
		return self.get_query_params().get('ReadTime')

	def set_ReadTime(self, ReadTime):  # Integer
		self.add_query_param('ReadTime', ReadTime)
	def get_HttpsPort(self): # String
		return self.get_query_params().get('HttpsPort')

	def set_HttpsPort(self, HttpsPort):  # String
		self.add_query_param('HttpsPort', HttpsPort)
	def get_LoadBalancing(self): # Integer
		return self.get_query_params().get('LoadBalancing')

	def set_LoadBalancing(self, LoadBalancing):  # Integer
		self.add_query_param('LoadBalancing', LoadBalancing)
	def get_HttpToUserIp(self): # Integer
		return self.get_query_params().get('HttpToUserIp')

	def set_HttpToUserIp(self, HttpToUserIp):  # Integer
		self.add_query_param('HttpToUserIp', HttpToUserIp)
