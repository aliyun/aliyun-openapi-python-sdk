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

class CreateCdnCertificateSigningRequestRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2018-05-10', 'CreateCdnCertificateSigningRequest')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Country(self): # String
		return self.get_query_params().get('Country')

	def set_Country(self, Country):  # String
		self.add_query_param('Country', Country)
	def get_City(self): # String
		return self.get_query_params().get('City')

	def set_City(self, City):  # String
		self.add_query_param('City', City)
	def get_CommonName(self): # String
		return self.get_query_params().get('CommonName')

	def set_CommonName(self, CommonName):  # String
		self.add_query_param('CommonName', CommonName)
	def get_State(self): # String
		return self.get_query_params().get('State')

	def set_State(self, State):  # String
		self.add_query_param('State', State)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_SANs(self): # String
		return self.get_query_params().get('SANs')

	def set_SANs(self, SANs):  # String
		self.add_query_param('SANs', SANs)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Organization(self): # String
		return self.get_query_params().get('Organization')

	def set_Organization(self, Organization):  # String
		self.add_query_param('Organization', Organization)
	def get_OrganizationUnit(self): # String
		return self.get_query_params().get('OrganizationUnit')

	def set_OrganizationUnit(self, OrganizationUnit):  # String
		self.add_query_param('OrganizationUnit', OrganizationUnit)
