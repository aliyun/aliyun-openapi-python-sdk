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
from aliyunsdkcdn.endpoint import endpoint_data

class SetDomainServerCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2018-05-10', 'SetDomainServerCertificate')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ServerCertificate(self):
		return self.get_query_params().get('ServerCertificate')

	def set_ServerCertificate(self,ServerCertificate):
		self.add_query_param('ServerCertificate',ServerCertificate)

	def get_PrivateKey(self):
		return self.get_query_params().get('PrivateKey')

	def set_PrivateKey(self,PrivateKey):
		self.add_query_param('PrivateKey',PrivateKey)

	def get_ServerCertificateStatus(self):
		return self.get_query_params().get('ServerCertificateStatus')

	def set_ServerCertificateStatus(self,ServerCertificateStatus):
		self.add_query_param('ServerCertificateStatus',ServerCertificateStatus)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_CertType(self):
		return self.get_query_params().get('CertType')

	def set_CertType(self,CertType):
		self.add_query_param('CertType',CertType)

	def get_ForceSet(self):
		return self.get_query_params().get('ForceSet')

	def set_ForceSet(self,ForceSet):
		self.add_query_param('ForceSet',ForceSet)

	def get_CertName(self):
		return self.get_query_params().get('CertName')

	def set_CertName(self,CertName):
		self.add_query_param('CertName',CertName)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)