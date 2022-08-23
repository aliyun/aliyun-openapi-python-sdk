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
from aliyunsdkmse.endpoint import endpoint_data

class AddGatewayDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'AddGatewayDomain','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MseSessionId(self): # String
		return self.get_query_params().get('MseSessionId')

	def set_MseSessionId(self, MseSessionId):  # String
		self.add_query_param('MseSessionId', MseSessionId)
	def get_GatewayUniqueId(self): # String
		return self.get_query_params().get('GatewayUniqueId')

	def set_GatewayUniqueId(self, GatewayUniqueId):  # String
		self.add_query_param('GatewayUniqueId', GatewayUniqueId)
	def get_TlsMax(self): # String
		return self.get_query_params().get('TlsMax')

	def set_TlsMax(self, TlsMax):  # String
		self.add_query_param('TlsMax', TlsMax)
	def get_Protocol(self): # String
		return self.get_query_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_query_param('Protocol', Protocol)
	def get_MustHttps(self): # Boolean
		return self.get_query_params().get('MustHttps')

	def set_MustHttps(self, MustHttps):  # Boolean
		self.add_query_param('MustHttps', MustHttps)
	def get_Http2(self): # String
		return self.get_query_params().get('Http2')

	def set_Http2(self, Http2):  # String
		self.add_query_param('Http2', Http2)
	def get_TlsMin(self): # String
		return self.get_query_params().get('TlsMin')

	def set_TlsMin(self, TlsMin):  # String
		self.add_query_param('TlsMin', TlsMin)
	def get_CertIdentifier(self): # String
		return self.get_query_params().get('CertIdentifier')

	def set_CertIdentifier(self, CertIdentifier):  # String
		self.add_query_param('CertIdentifier', CertIdentifier)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
