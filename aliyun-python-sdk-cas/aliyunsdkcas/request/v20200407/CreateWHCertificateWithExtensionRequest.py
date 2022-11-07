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

class CreateWHCertificateWithExtensionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cas', '2020-04-07', 'CreateWHCertificateWithExtension')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AppendCrl(self): # Boolean
		return self.get_query_params().get('AppendCrl')

	def set_AppendCrl(self, AppendCrl):  # Boolean
		self.add_query_param('AppendCrl', AppendCrl)
	def get_CountryCode(self): # String
		return self.get_query_params().get('CountryCode')

	def set_CountryCode(self, CountryCode):  # String
		self.add_query_param('CountryCode', CountryCode)
	def get_Immediately(self): # Long
		return self.get_query_params().get('Immediately')

	def set_Immediately(self, Immediately):  # Long
		self.add_query_param('Immediately', Immediately)
	def get_CommonName(self): # String
		return self.get_query_params().get('CommonName')

	def set_CommonName(self, CommonName):  # String
		self.add_query_param('CommonName', CommonName)
	def get_CertType(self): # String
		return self.get_query_params().get('CertType')

	def set_CertType(self, CertType):  # String
		self.add_query_param('CertType', CertType)
	def get_State(self): # String
		return self.get_query_params().get('State')

	def set_State(self, State):  # String
		self.add_query_param('State', State)
	def get_CsrPemString(self): # String
		return self.get_query_params().get('CsrPemString')

	def set_CsrPemString(self, CsrPemString):  # String
		self.add_query_param('CsrPemString', CsrPemString)
	def get_AlgorithmKeySize(self): # String
		return self.get_query_params().get('AlgorithmKeySize')

	def set_AlgorithmKeySize(self, AlgorithmKeySize):  # String
		self.add_query_param('AlgorithmKeySize', AlgorithmKeySize)
	def get_AfterTime(self): # Long
		return self.get_query_params().get('AfterTime')

	def set_AfterTime(self, AfterTime):  # Long
		self.add_query_param('AfterTime', AfterTime)
	def get_Sans(self): # String
		return self.get_query_params().get('Sans')

	def set_Sans(self, Sans):  # String
		self.add_query_param('Sans', Sans)
	def get_Locality(self): # String
		return self.get_query_params().get('Locality')

	def set_Locality(self, Locality):  # String
		self.add_query_param('Locality', Locality)
	def get_BasicConstraintsCritical(self): # Boolean
		return self.get_query_params().get('BasicConstraintsCritical')

	def set_BasicConstraintsCritical(self, BasicConstraintsCritical):  # Boolean
		self.add_query_param('BasicConstraintsCritical', BasicConstraintsCritical)
	def get_AliasName(self): # String
		return self.get_query_params().get('AliasName')

	def set_AliasName(self, AliasName):  # String
		self.add_query_param('AliasName', AliasName)
	def get_Organization(self): # String
		return self.get_query_params().get('Organization')

	def set_Organization(self, Organization):  # String
		self.add_query_param('Organization', Organization)
	def get_BeforeTime(self): # Long
		return self.get_query_params().get('BeforeTime')

	def set_BeforeTime(self, BeforeTime):  # Long
		self.add_query_param('BeforeTime', BeforeTime)
	def get_ParentIdentifier(self): # String
		return self.get_query_params().get('ParentIdentifier')

	def set_ParentIdentifier(self, ParentIdentifier):  # String
		self.add_query_param('ParentIdentifier', ParentIdentifier)
	def get_OrganizationUnit(self): # String
		return self.get_query_params().get('OrganizationUnit')

	def set_OrganizationUnit(self, OrganizationUnit):  # String
		self.add_query_param('OrganizationUnit', OrganizationUnit)
