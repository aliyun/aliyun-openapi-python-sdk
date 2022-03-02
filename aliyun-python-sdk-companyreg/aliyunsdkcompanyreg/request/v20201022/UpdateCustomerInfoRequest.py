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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class UpdateCustomerInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2020-10-22', 'UpdateCustomerInfo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ContactTelInfo(self): # String
		return self.get_query_params().get('ContactTelInfo')

	def set_ContactTelInfo(self, ContactTelInfo):  # String
		self.add_query_param('ContactTelInfo', ContactTelInfo)
	def get_TaxPreparerName(self): # String
		return self.get_query_params().get('TaxPreparerName')

	def set_TaxPreparerName(self, TaxPreparerName):  # String
		self.add_query_param('TaxPreparerName', TaxPreparerName)
	def get_TaxAgentSecret(self): # String
		return self.get_query_params().get('TaxAgentSecret')

	def set_TaxAgentSecret(self, TaxAgentSecret):  # String
		self.add_query_param('TaxAgentSecret', TaxAgentSecret)
	def get_LegalRepresentative(self): # String
		return self.get_query_params().get('LegalRepresentative')

	def set_LegalRepresentative(self, LegalRepresentative):  # String
		self.add_query_param('LegalRepresentative', LegalRepresentative)
	def get_TaxPreparerPassword(self): # String
		return self.get_query_params().get('TaxPreparerPassword')

	def set_TaxPreparerPassword(self, TaxPreparerPassword):  # String
		self.add_query_param('TaxPreparerPassword', TaxPreparerPassword)
	def get_EstablishmentDate(self): # String
		return self.get_query_params().get('EstablishmentDate')

	def set_EstablishmentDate(self, EstablishmentDate):  # String
		self.add_query_param('EstablishmentDate', EstablishmentDate)
	def get_ContactName(self): # String
		return self.get_query_params().get('ContactName')

	def set_ContactName(self, ContactName):  # String
		self.add_query_param('ContactName', ContactName)
	def get_BizScope(self): # String
		return self.get_query_params().get('BizScope')

	def set_BizScope(self, BizScope):  # String
		self.add_query_param('BizScope', BizScope)
	def get_IncomeDeclarationPassword(self): # String
		return self.get_query_params().get('IncomeDeclarationPassword')

	def set_IncomeDeclarationPassword(self, IncomeDeclarationPassword):  # String
		self.add_query_param('IncomeDeclarationPassword', IncomeDeclarationPassword)
	def get_CompanyType(self): # String
		return self.get_query_params().get('CompanyType')

	def set_CompanyType(self, CompanyType):  # String
		self.add_query_param('CompanyType', CompanyType)
	def get_CorpAddress(self): # String
		return self.get_query_params().get('CorpAddress')

	def set_CorpAddress(self, CorpAddress):  # String
		self.add_query_param('CorpAddress', CorpAddress)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_IsRefreshInfo(self): # Boolean
		return self.get_query_params().get('IsRefreshInfo')

	def set_IsRefreshInfo(self, IsRefreshInfo):  # Boolean
		self.add_query_param('IsRefreshInfo', IsRefreshInfo)
	def get_RegisteredCapital(self): # String
		return self.get_query_params().get('RegisteredCapital')

	def set_RegisteredCapital(self, RegisteredCapital):  # String
		self.add_query_param('RegisteredCapital', RegisteredCapital)
	def get_OperatingPeriod(self): # String
		return self.get_query_params().get('OperatingPeriod')

	def set_OperatingPeriod(self, OperatingPeriod):  # String
		self.add_query_param('OperatingPeriod', OperatingPeriod)
