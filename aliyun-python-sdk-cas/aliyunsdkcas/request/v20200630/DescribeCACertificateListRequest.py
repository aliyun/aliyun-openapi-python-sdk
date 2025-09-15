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

class DescribeCACertificateListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cas', '2020-06-30', 'DescribeCACertificateList','cas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CaStatus(self): # String
		return self.get_query_params().get('CaStatus')

	def set_CaStatus(self, CaStatus):  # String
		self.add_query_param('CaStatus', CaStatus)
	def get_CertType(self): # String
		return self.get_query_params().get('CertType')

	def set_CertType(self, CertType):  # String
		self.add_query_param('CertType', CertType)
	def get_ValidStatus(self): # String
		return self.get_query_params().get('ValidStatus')

	def set_ValidStatus(self, ValidStatus):  # String
		self.add_query_param('ValidStatus', ValidStatus)
	def get_IssuerType(self): # String
		return self.get_query_params().get('IssuerType')

	def set_IssuerType(self, IssuerType):  # String
		self.add_query_param('IssuerType', IssuerType)
	def get_Identifier(self): # String
		return self.get_query_params().get('Identifier')

	def set_Identifier(self, Identifier):  # String
		self.add_query_param('Identifier', Identifier)
	def get_ShowSize(self): # Integer
		return self.get_query_params().get('ShowSize')

	def set_ShowSize(self, ShowSize):  # Integer
		self.add_query_param('ShowSize', ShowSize)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
