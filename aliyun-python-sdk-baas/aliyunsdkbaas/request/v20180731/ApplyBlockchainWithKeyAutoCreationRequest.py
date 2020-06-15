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
from aliyunsdkbaas.endpoint import endpoint_data

class ApplyBlockchainWithKeyAutoCreationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'ApplyBlockchainWithKeyAutoCreation')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OrganizationUnitName(self):
		return self.get_body_params().get('OrganizationUnitName')

	def set_OrganizationUnitName(self,OrganizationUnitName):
		self.add_body_params('OrganizationUnitName', OrganizationUnitName)

	def get_LocalityName(self):
		return self.get_body_params().get('LocalityName')

	def set_LocalityName(self,LocalityName):
		self.add_body_params('LocalityName', LocalityName)

	def get_Password(self):
		return self.get_body_params().get('Password')

	def set_Password(self,Password):
		self.add_body_params('Password', Password)

	def get_CommonName(self):
		return self.get_body_params().get('CommonName')

	def set_CommonName(self,CommonName):
		self.add_body_params('CommonName', CommonName)

	def get_CountryName(self):
		return self.get_body_params().get('CountryName')

	def set_CountryName(self,CountryName):
		self.add_body_params('CountryName', CountryName)

	def get_StateOrProvinceName(self):
		return self.get_body_params().get('StateOrProvinceName')

	def set_StateOrProvinceName(self,StateOrProvinceName):
		self.add_body_params('StateOrProvinceName', StateOrProvinceName)

	def get_OrganizationName(self):
		return self.get_body_params().get('OrganizationName')

	def set_OrganizationName(self,OrganizationName):
		self.add_body_params('OrganizationName', OrganizationName)

	def get_Bizid(self):
		return self.get_body_params().get('Bizid')

	def set_Bizid(self,Bizid):
		self.add_body_params('Bizid', Bizid)