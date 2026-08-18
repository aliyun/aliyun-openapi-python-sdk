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

class CreateRootCACertificateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cas', '2020-06-30', 'CreateRootCACertificate','cas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_CountryCode(self): # String
		return self.get_query_params().get('CountryCode')

	def set_CountryCode(self, CountryCode):  # String
		self.add_query_param('CountryCode', CountryCode)
	def get_Locality(self): # String
		return self.get_query_params().get('Locality')

	def set_Locality(self, Locality):  # String
		self.add_query_param('Locality', Locality)
	def get_Years(self): # Integer
		return self.get_query_params().get('Years')

	def set_Years(self, Years):  # Integer
		self.add_query_param('Years', Years)
	def get_CommonName(self): # String
		return self.get_query_params().get('CommonName')

	def set_CommonName(self, CommonName):  # String
		self.add_query_param('CommonName', CommonName)
	def get_Organization(self): # String
		return self.get_query_params().get('Organization')

	def set_Organization(self, Organization):  # String
		self.add_query_param('Organization', Organization)
	def get_State(self): # String
		return self.get_query_params().get('State')

	def set_State(self, State):  # String
		self.add_query_param('State', State)
	def get_OrganizationUnit(self): # String
		return self.get_query_params().get('OrganizationUnit')

	def set_OrganizationUnit(self, OrganizationUnit):  # String
		self.add_query_param('OrganizationUnit', OrganizationUnit)
	def get_Algorithm(self): # String
		return self.get_query_params().get('Algorithm')

	def set_Algorithm(self, Algorithm):  # String
		self.add_query_param('Algorithm', Algorithm)
