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
class SetDomainCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'SetDomainCertificate','apigateway')

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_CertificatePrivateKey(self):
		return self.get_query_params().get('CertificatePrivateKey')

	def set_CertificatePrivateKey(self,CertificatePrivateKey):
		self.add_query_param('CertificatePrivateKey',CertificatePrivateKey)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_CertificateName(self):
		return self.get_query_params().get('CertificateName')

	def set_CertificateName(self,CertificateName):
		self.add_query_param('CertificateName',CertificateName)

	def get_CertificateBody(self):
		return self.get_query_params().get('CertificateBody')

	def set_CertificateBody(self,CertificateBody):
		self.add_query_param('CertificateBody',CertificateBody)