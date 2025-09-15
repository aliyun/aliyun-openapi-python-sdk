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
from aliyunsdkcas.endpoint import endpoint_data

class CreateCustomCertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cas', '2020-06-30', 'CreateCustomCertificate','cas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Csr(self): # String
		return self.get_query_params().get('Csr')

	def set_Csr(self, Csr):  # String
		self.add_query_param('Csr', Csr)
	def get_EnableCrl(self): # Long
		return self.get_query_params().get('EnableCrl')

	def set_EnableCrl(self, EnableCrl):  # Long
		self.add_query_param('EnableCrl', EnableCrl)
	def get_Immediately(self): # Integer
		return self.get_query_params().get('Immediately')

	def set_Immediately(self, Immediately):  # Integer
		self.add_query_param('Immediately', Immediately)
	def get_ParentIdentifier(self): # String
		return self.get_query_params().get('ParentIdentifier')

	def set_ParentIdentifier(self, ParentIdentifier):  # String
		self.add_query_param('ParentIdentifier', ParentIdentifier)
	def get_Validity(self): # String
		return self.get_query_params().get('Validity')

	def set_Validity(self, Validity):  # String
		self.add_query_param('Validity', Validity)
	def get_ApiPassthrough(self): # Struct
		return self.get_query_params().get('ApiPassthrough')

	def set_ApiPassthrough(self, ApiPassthrough):  # Struct
		if ApiPassthrough.get('Subject') is not None:
			if ApiPassthrough.get('Subject').get('Country') is not None:
				self.add_query_param('ApiPassthrough.Subject.Country', ApiPassthrough.get('Subject').get('Country'))
			if ApiPassthrough.get('Subject').get('State') is not None:
				self.add_query_param('ApiPassthrough.Subject.State', ApiPassthrough.get('Subject').get('State'))
			if ApiPassthrough.get('Subject').get('Locality') is not None:
				self.add_query_param('ApiPassthrough.Subject.Locality', ApiPassthrough.get('Subject').get('Locality'))
			if ApiPassthrough.get('Subject').get('Organization') is not None:
				self.add_query_param('ApiPassthrough.Subject.Organization', ApiPassthrough.get('Subject').get('Organization'))
			if ApiPassthrough.get('Subject').get('OrganizationUnit') is not None:
				self.add_query_param('ApiPassthrough.Subject.OrganizationUnit', ApiPassthrough.get('Subject').get('OrganizationUnit'))
			if ApiPassthrough.get('Subject').get('CommonName') is not None:
				self.add_query_param('ApiPassthrough.Subject.CommonName', ApiPassthrough.get('Subject').get('CommonName'))
			if ApiPassthrough.get('Subject').get('CustomAttributes') is not None:
				for index1, value1 in enumerate(ApiPassthrough.get('Subject').get('CustomAttributes')):
					if value1.get('ObjectIdentifier') is not None:
						self.add_query_param('ApiPassthrough.Subject.CustomAttributes.' + str(index1 + 1) + '.ObjectIdentifier', value1.get('ObjectIdentifier'))
					if value1.get('Value') is not None:
						self.add_query_param('ApiPassthrough.Subject.CustomAttributes.' + str(index1 + 1) + '.Value', value1.get('Value'))
		if ApiPassthrough.get('Extensions') is not None:
			if ApiPassthrough.get('Extensions').get('KeyUsage') is not None:
				if ApiPassthrough.get('Extensions').get('KeyUsage').get('DigitalSignature') is not None:
					self.add_query_param('ApiPassthrough.Extensions.KeyUsage.DigitalSignature', ApiPassthrough.get('Extensions').get('KeyUsage').get('DigitalSignature'))
				if ApiPassthrough.get('Extensions').get('KeyUsage').get('ContentCommitment') is not None:
					self.add_query_param('ApiPassthrough.Extensions.KeyUsage.ContentCommitment', ApiPassthrough.get('Extensions').get('KeyUsage').get('ContentCommitment'))
				if ApiPassthrough.get('Extensions').get('KeyUsage').get('NonRepudiation') is not None:
					self.add_query_param('ApiPassthrough.Extensions.KeyUsage.NonRepudiation', ApiPassthrough.get('Extensions').get('KeyUsage').get('NonRepudiation'))
				if ApiPassthrough.get('Extensions').get('KeyUsage').get('KeyEncipherment') is not None:
					self.add_query_param('ApiPassthrough.Extensions.KeyUsage.KeyEncipherment', ApiPassthrough.get('Extensions').get('KeyUsage').get('KeyEncipherment'))
				if ApiPassthrough.get('Extensions').get('KeyUsage').get('DataEncipherment') is not None:
					self.add_query_param('ApiPassthrough.Extensions.KeyUsage.DataEncipherment', ApiPassthrough.get('Extensions').get('KeyUsage').get('DataEncipherment'))
				if ApiPassthrough.get('Extensions').get('KeyUsage').get('KeyAgreement') is not None:
					self.add_query_param('ApiPassthrough.Extensions.KeyUsage.KeyAgreement', ApiPassthrough.get('Extensions').get('KeyUsage').get('KeyAgreement'))
				if ApiPassthrough.get('Extensions').get('KeyUsage').get('EncipherOnly') is not None:
					self.add_query_param('ApiPassthrough.Extensions.KeyUsage.EncipherOnly', ApiPassthrough.get('Extensions').get('KeyUsage').get('EncipherOnly'))
				if ApiPassthrough.get('Extensions').get('KeyUsage').get('DecipherOnly') is not None:
					self.add_query_param('ApiPassthrough.Extensions.KeyUsage.DecipherOnly', ApiPassthrough.get('Extensions').get('KeyUsage').get('DecipherOnly'))
			if ApiPassthrough.get('Extensions').get('ExtendedKeyUsages') is not None:
				for index1, value1 in enumerate(ApiPassthrough.get('Extensions').get('ExtendedKeyUsages')):
					self.add_query_param('ApiPassthrough.Extensions.ExtendedKeyUsages.' + str(index1 + 1), value1)
			if ApiPassthrough.get('Extensions').get('SubjectAlternativeNames') is not None:
				for index1, value1 in enumerate(ApiPassthrough.get('Extensions').get('SubjectAlternativeNames')):
					if value1.get('Type') is not None:
						self.add_query_param('ApiPassthrough.Extensions.SubjectAlternativeNames.' + str(index1 + 1) + '.Type', value1.get('Type'))
					if value1.get('Value') is not None:
						self.add_query_param('ApiPassthrough.Extensions.SubjectAlternativeNames.' + str(index1 + 1) + '.Value', value1.get('Value'))
			if ApiPassthrough.get('Extensions').get('Criticals') is not None:
				for index1, value1 in enumerate(ApiPassthrough.get('Extensions').get('Criticals')):
					self.add_query_param('ApiPassthrough.Extensions.Criticals.' + str(index1 + 1), value1)
		if ApiPassthrough.get('SerialNumber') is not None:
			self.add_query_param('ApiPassthrough.SerialNumber', ApiPassthrough.get('SerialNumber'))
