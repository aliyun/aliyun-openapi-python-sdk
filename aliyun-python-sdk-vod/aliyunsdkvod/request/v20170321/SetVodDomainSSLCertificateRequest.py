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
from aliyunsdkvod.endpoint import endpoint_data

class SetVodDomainSSLCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'SetVodDomainSSLCertificate','vod')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SSLProtocol(self): # String
		return self.get_query_params().get('SSLProtocol')

	def set_SSLProtocol(self, SSLProtocol):  # String
		self.add_query_param('SSLProtocol', SSLProtocol)
	def get_CertId(self): # Long
		return self.get_query_params().get('CertId')

	def set_CertId(self, CertId):  # Long
		self.add_query_param('CertId', CertId)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_CertType(self): # String
		return self.get_query_params().get('CertType')

	def set_CertType(self, CertType):  # String
		self.add_query_param('CertType', CertType)
	def get_SSLPri(self): # String
		return self.get_query_params().get('SSLPri')

	def set_SSLPri(self, SSLPri):  # String
		self.add_query_param('SSLPri', SSLPri)
	def get_CertRegion(self): # String
		return self.get_query_params().get('CertRegion')

	def set_CertRegion(self, CertRegion):  # String
		self.add_query_param('CertRegion', CertRegion)
	def get_CertName(self): # String
		return self.get_query_params().get('CertName')

	def set_CertName(self, CertName):  # String
		self.add_query_param('CertName', CertName)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Env(self): # String
		return self.get_query_params().get('Env')

	def set_Env(self, Env):  # String
		self.add_query_param('Env', Env)
	def get_SSLPub(self): # String
		return self.get_query_params().get('SSLPub')

	def set_SSLPub(self, SSLPub):  # String
		self.add_query_param('SSLPub', SSLPub)
