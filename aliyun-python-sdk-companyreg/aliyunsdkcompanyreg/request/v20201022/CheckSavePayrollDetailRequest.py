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

class CheckSavePayrollDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2020-10-22', 'CheckSavePayrollDetail')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Income(self): # String
		return self.get_query_params().get('Income')

	def set_Income(self, Income):  # String
		self.add_query_param('Income', Income)
	def get_CorporateHousingAccumulationFund(self): # String
		return self.get_query_params().get('CorporateHousingAccumulationFund')

	def set_CorporateHousingAccumulationFund(self, CorporateHousingAccumulationFund):  # String
		self.add_query_param('CorporateHousingAccumulationFund', CorporateHousingAccumulationFund)
	def get_PersonHousingAccumulationFund(self): # String
		return self.get_query_params().get('PersonHousingAccumulationFund')

	def set_PersonHousingAccumulationFund(self, PersonHousingAccumulationFund):  # String
		self.add_query_param('PersonHousingAccumulationFund', PersonHousingAccumulationFund)
	def get_PersMedicalInsurance(self): # String
		return self.get_query_params().get('PersMedicalInsurance')

	def set_PersMedicalInsurance(self, PersMedicalInsurance):  # String
		self.add_query_param('PersMedicalInsurance', PersMedicalInsurance)
	def get_CorpUnemploymentInsurance(self): # String
		return self.get_query_params().get('CorpUnemploymentInsurance')

	def set_CorpUnemploymentInsurance(self, CorpUnemploymentInsurance):  # String
		self.add_query_param('CorpUnemploymentInsurance', CorpUnemploymentInsurance)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_PersonSocialInsurance(self): # String
		return self.get_query_params().get('PersonSocialInsurance')

	def set_PersonSocialInsurance(self, PersonSocialInsurance):  # String
		self.add_query_param('PersonSocialInsurance', PersonSocialInsurance)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_CorporateSocialInsurance(self): # String
		return self.get_query_params().get('CorporateSocialInsurance')

	def set_CorporateSocialInsurance(self, CorporateSocialInsurance):  # String
		self.add_query_param('CorporateSocialInsurance', CorporateSocialInsurance)
	def get_CorpInjuryInsurance(self): # String
		return self.get_query_params().get('CorpInjuryInsurance')

	def set_CorpInjuryInsurance(self, CorpInjuryInsurance):  # String
		self.add_query_param('CorpInjuryInsurance', CorpInjuryInsurance)
	def get_PersPension(self): # String
		return self.get_query_params().get('PersPension')

	def set_PersPension(self, PersPension):  # String
		self.add_query_param('PersPension', PersPension)
	def get_CorpMedicalInsurance(self): # String
		return self.get_query_params().get('CorpMedicalInsurance')

	def set_CorpMedicalInsurance(self, CorpMedicalInsurance):  # String
		self.add_query_param('CorpMedicalInsurance', CorpMedicalInsurance)
	def get_IdNo(self): # String
		return self.get_query_params().get('IdNo')

	def set_IdNo(self, IdNo):  # String
		self.add_query_param('IdNo', IdNo)
	def get_EmployeeTime(self): # String
		return self.get_query_params().get('EmployeeTime')

	def set_EmployeeTime(self, EmployeeTime):  # String
		self.add_query_param('EmployeeTime', EmployeeTime)
	def get_UpdateEmployeeFlag(self): # Boolean
		return self.get_query_params().get('UpdateEmployeeFlag')

	def set_UpdateEmployeeFlag(self, UpdateEmployeeFlag):  # Boolean
		self.add_query_param('UpdateEmployeeFlag', UpdateEmployeeFlag)
	def get_Phone(self): # String
		return self.get_query_params().get('Phone')

	def set_Phone(self, Phone):  # String
		self.add_query_param('Phone', Phone)
	def get_PersUnemploymentInsurance(self): # String
		return self.get_query_params().get('PersUnemploymentInsurance')

	def set_PersUnemploymentInsurance(self, PersUnemploymentInsurance):  # String
		self.add_query_param('PersUnemploymentInsurance', PersUnemploymentInsurance)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_CorpPension(self): # String
		return self.get_query_params().get('CorpPension')

	def set_CorpPension(self, CorpPension):  # String
		self.add_query_param('CorpPension', CorpPension)
	def get_CorpMaternityInsurance(self): # String
		return self.get_query_params().get('CorpMaternityInsurance')

	def set_CorpMaternityInsurance(self, CorpMaternityInsurance):  # String
		self.add_query_param('CorpMaternityInsurance', CorpMaternityInsurance)
