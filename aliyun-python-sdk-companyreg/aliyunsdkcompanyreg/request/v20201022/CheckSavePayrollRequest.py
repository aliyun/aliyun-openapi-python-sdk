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

class CheckSavePayrollRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2020-10-22', 'CheckSavePayroll','companyreg')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Income(self):
		return self.get_query_params().get('Income')

	def set_Income(self,Income):
		self.add_query_param('Income',Income)

	def get_CorporateHousingAccumulationFund(self):
		return self.get_query_params().get('CorporateHousingAccumulationFund')

	def set_CorporateHousingAccumulationFund(self,CorporateHousingAccumulationFund):
		self.add_query_param('CorporateHousingAccumulationFund',CorporateHousingAccumulationFund)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_CorporateSocialInsurance(self):
		return self.get_query_params().get('CorporateSocialInsurance')

	def set_CorporateSocialInsurance(self,CorporateSocialInsurance):
		self.add_query_param('CorporateSocialInsurance',CorporateSocialInsurance)

	def get_IdNo(self):
		return self.get_query_params().get('IdNo')

	def set_IdNo(self,IdNo):
		self.add_query_param('IdNo',IdNo)

	def get_EmployeeTime(self):
		return self.get_query_params().get('EmployeeTime')

	def set_EmployeeTime(self,EmployeeTime):
		self.add_query_param('EmployeeTime',EmployeeTime)

	def get_PersonHousingAccumulationFund(self):
		return self.get_query_params().get('PersonHousingAccumulationFund')

	def set_PersonHousingAccumulationFund(self,PersonHousingAccumulationFund):
		self.add_query_param('PersonHousingAccumulationFund',PersonHousingAccumulationFund)

	def get_UpdateEmployeeFlag(self):
		return self.get_query_params().get('UpdateEmployeeFlag')

	def set_UpdateEmployeeFlag(self,UpdateEmployeeFlag):
		self.add_query_param('UpdateEmployeeFlag',UpdateEmployeeFlag)

	def get_Phone(self):
		return self.get_query_params().get('Phone')

	def set_Phone(self,Phone):
		self.add_query_param('Phone',Phone)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_PersonSocialInsurance(self):
		return self.get_query_params().get('PersonSocialInsurance')

	def set_PersonSocialInsurance(self,PersonSocialInsurance):
		self.add_query_param('PersonSocialInsurance',PersonSocialInsurance)