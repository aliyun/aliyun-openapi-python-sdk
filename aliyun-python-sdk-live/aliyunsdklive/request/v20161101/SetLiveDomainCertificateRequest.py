# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class SetLiveDomainCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'SetLiveDomainCertificate','live')

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_SSLPub(self):
		return self.get_query_params().get('SSLPub')

	def set_SSLPub(self,SSLPub):
		self.add_query_param('SSLPub',SSLPub)

	def get_CertName(self):
		return self.get_query_params().get('CertName')

	def set_CertName(self,CertName):
		self.add_query_param('CertName',CertName)

	def get_SSLProtocol(self):
		return self.get_query_params().get('SSLProtocol')

	def set_SSLProtocol(self,SSLProtocol):
		self.add_query_param('SSLProtocol',SSLProtocol)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SSLPri(self):
		return self.get_query_params().get('SSLPri')

	def set_SSLPri(self,SSLPri):
		self.add_query_param('SSLPri',SSLPri)