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

class ModifyDomainConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'waf-openapi', '2018-01-17', 'ModifyDomainConfig','waf')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HttpPort(self):
		return self.get_query_params().get('HttpPort')

	def set_HttpPort(self,HttpPort):
		self.add_query_param('HttpPort',HttpPort)

	def get_Protocols(self):
		return self.get_query_params().get('Protocols')

	def set_Protocols(self,Protocols):
		self.add_query_param('Protocols',Protocols)

	def get_HttpsRedirect(self):
		return self.get_query_params().get('HttpsRedirect')

	def set_HttpsRedirect(self,HttpsRedirect):
		self.add_query_param('HttpsRedirect',HttpsRedirect)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_SourceIps(self):
		return self.get_query_params().get('SourceIps')

	def set_SourceIps(self,SourceIps):
		self.add_query_param('SourceIps',SourceIps)

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)

	def get_IsAccessProduct(self):
		return self.get_query_params().get('IsAccessProduct')

	def set_IsAccessProduct(self,IsAccessProduct):
		self.add_query_param('IsAccessProduct',IsAccessProduct)

	def get_HttpsPort(self):
		return self.get_query_params().get('HttpsPort')

	def set_HttpsPort(self,HttpsPort):
		self.add_query_param('HttpsPort',HttpsPort)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)

	def get_LoadBalancing(self):
		return self.get_query_params().get('LoadBalancing')

	def set_LoadBalancing(self,LoadBalancing):
		self.add_query_param('LoadBalancing',LoadBalancing)

	def get_HttpToUserIp(self):
		return self.get_query_params().get('HttpToUserIp')

	def set_HttpToUserIp(self,HttpToUserIp):
		self.add_query_param('HttpToUserIp',HttpToUserIp)