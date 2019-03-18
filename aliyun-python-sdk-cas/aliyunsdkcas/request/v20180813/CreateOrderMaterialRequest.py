# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateOrderMaterialRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cas', '2018-08-13', 'CreateOrderMaterial','cas_esign_fdd')

	def get_LeaderName(self):
		return self.get_query_params().get('LeaderName')

	def set_LeaderName(self,LeaderName):
		self.add_query_param('LeaderName',LeaderName)

	def get_City(self):
		return self.get_query_params().get('City')

	def set_City(self,City):
		self.add_query_param('City',City)

	def get_CountryCode(self):
		return self.get_query_params().get('CountryCode')

	def set_CountryCode(self,CountryCode):
		self.add_query_param('CountryCode',CountryCode)

	def get_LeaderEmail(self):
		return self.get_query_params().get('LeaderEmail')

	def set_LeaderEmail(self,LeaderEmail):
		self.add_query_param('LeaderEmail',LeaderEmail)

	def get_CompanyAddress(self):
		return self.get_query_params().get('CompanyAddress')

	def set_CompanyAddress(self,CompanyAddress):
		self.add_query_param('CompanyAddress',CompanyAddress)

	def get_CompanyCode(self):
		return self.get_query_params().get('CompanyCode')

	def set_CompanyCode(self,CompanyCode):
		self.add_query_param('CompanyCode',CompanyCode)

	def get_PersonEmail(self):
		return self.get_query_params().get('PersonEmail')

	def set_PersonEmail(self,PersonEmail):
		self.add_query_param('PersonEmail',PersonEmail)

	def get_Province(self):
		return self.get_query_params().get('Province')

	def set_Province(self,Province):
		self.add_query_param('Province',Province)

	def get_DomainAuthType(self):
		return self.get_query_params().get('DomainAuthType')

	def set_DomainAuthType(self,DomainAuthType):
		self.add_query_param('DomainAuthType',DomainAuthType)

	def get_LeaderPhone(self):
		return self.get_query_params().get('LeaderPhone')

	def set_LeaderPhone(self,LeaderPhone):
		self.add_query_param('LeaderPhone',LeaderPhone)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_CsrContent(self):
		return self.get_query_params().get('CsrContent')

	def set_CsrContent(self,CsrContent):
		self.add_query_param('CsrContent',CsrContent)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_PersonName(self):
		return self.get_query_params().get('PersonName')

	def set_PersonName(self,PersonName):
		self.add_query_param('PersonName',PersonName)

	def get_PersonIdCardNumber(self):
		return self.get_query_params().get('PersonIdCardNumber')

	def set_PersonIdCardNumber(self,PersonIdCardNumber):
		self.add_query_param('PersonIdCardNumber',PersonIdCardNumber)

	def get_OrderId(self):
		return self.get_query_params().get('OrderId')

	def set_OrderId(self,OrderId):
		self.add_query_param('OrderId',OrderId)

	def get_LeaderTitle(self):
		return self.get_query_params().get('LeaderTitle')

	def set_LeaderTitle(self,LeaderTitle):
		self.add_query_param('LeaderTitle',LeaderTitle)

	def get_PersonTitle(self):
		return self.get_query_params().get('PersonTitle')

	def set_PersonTitle(self,PersonTitle):
		self.add_query_param('PersonTitle',PersonTitle)

	def get_PostCode(self):
		return self.get_query_params().get('PostCode')

	def set_PostCode(self,PostCode):
		self.add_query_param('PostCode',PostCode)

	def get_CreateCsr(self):
		return self.get_query_params().get('CreateCsr')

	def set_CreateCsr(self,CreateCsr):
		self.add_query_param('CreateCsr',CreateCsr)

	def get_PersonPhone(self):
		return self.get_query_params().get('PersonPhone')

	def set_PersonPhone(self,PersonPhone):
		self.add_query_param('PersonPhone',PersonPhone)

	def get_CompanyName(self):
		return self.get_query_params().get('CompanyName')

	def set_CompanyName(self,CompanyName):
		self.add_query_param('CompanyName',CompanyName)

	def get_CompanyPhone(self):
		return self.get_query_params().get('CompanyPhone')

	def set_CompanyPhone(self,CompanyPhone):
		self.add_query_param('CompanyPhone',CompanyPhone)

	def get_CompanyType(self):
		return self.get_query_params().get('CompanyType')

	def set_CompanyType(self,CompanyType):
		self.add_query_param('CompanyType',CompanyType)

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)

	def get_PersonDepartment(self):
		return self.get_query_params().get('PersonDepartment')

	def set_PersonDepartment(self,PersonDepartment):
		self.add_query_param('PersonDepartment',PersonDepartment)