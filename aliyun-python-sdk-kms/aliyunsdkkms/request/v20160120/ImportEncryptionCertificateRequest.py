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
from aliyunsdkkms.endpoint import endpoint_data

class ImportEncryptionCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Kms', '2016-01-20', 'ImportEncryptionCertificate','kms-service')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AsymmetricAlgorithm(self):
		return self.get_query_params().get('AsymmetricAlgorithm')

	def set_AsymmetricAlgorithm(self,AsymmetricAlgorithm):
		self.add_query_param('AsymmetricAlgorithm',AsymmetricAlgorithm)

	def get_SymmetricAlgorithm(self):
		return self.get_query_params().get('SymmetricAlgorithm')

	def set_SymmetricAlgorithm(self,SymmetricAlgorithm):
		self.add_query_param('SymmetricAlgorithm',SymmetricAlgorithm)

	def get_EncryptedPrivateKey(self):
		return self.get_query_params().get('EncryptedPrivateKey')

	def set_EncryptedPrivateKey(self,EncryptedPrivateKey):
		self.add_query_param('EncryptedPrivateKey',EncryptedPrivateKey)

	def get_EncryptedSymmetricKey(self):
		return self.get_query_params().get('EncryptedSymmetricKey')

	def set_EncryptedSymmetricKey(self,EncryptedSymmetricKey):
		self.add_query_param('EncryptedSymmetricKey',EncryptedSymmetricKey)

	def get_CertificateId(self):
		return self.get_query_params().get('CertificateId')

	def set_CertificateId(self,CertificateId):
		self.add_query_param('CertificateId',CertificateId)

	def get_Certificate(self):
		return self.get_query_params().get('Certificate')

	def set_Certificate(self,Certificate):
		self.add_query_param('Certificate',Certificate)

	def get_CertificateChain(self):
		return self.get_query_params().get('CertificateChain')

	def set_CertificateChain(self,CertificateChain):
		self.add_query_param('CertificateChain',CertificateChain)