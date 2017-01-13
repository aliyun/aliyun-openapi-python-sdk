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
class SaveContactTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2016-05-11', 'SaveContactTemplate')

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_ContactTemplateId(self):
		return self.get_query_params().get('ContactTemplateId')

	def set_ContactTemplateId(self,ContactTemplateId):
		self.add_query_param('ContactTemplateId',ContactTemplateId)

	def get_DefaultTemplate(self):
		return self.get_query_params().get('DefaultTemplate')

	def set_DefaultTemplate(self,DefaultTemplate):
		self.add_query_param('DefaultTemplate',DefaultTemplate)

	def get_CCity(self):
		return self.get_query_params().get('CCity')

	def set_CCity(self,CCity):
		self.add_query_param('CCity',CCity)

	def get_CCompany(self):
		return self.get_query_params().get('CCompany')

	def set_CCompany(self,CCompany):
		self.add_query_param('CCompany',CCompany)

	def get_CCountry(self):
		return self.get_query_params().get('CCountry')

	def set_CCountry(self,CCountry):
		self.add_query_param('CCountry',CCountry)

	def get_CName(self):
		return self.get_query_params().get('CName')

	def set_CName(self,CName):
		self.add_query_param('CName',CName)

	def get_CProvince(self):
		return self.get_query_params().get('CProvince')

	def set_CProvince(self,CProvince):
		self.add_query_param('CProvince',CProvince)

	def get_CVenu(self):
		return self.get_query_params().get('CVenu')

	def set_CVenu(self,CVenu):
		self.add_query_param('CVenu',CVenu)

	def get_ECity(self):
		return self.get_query_params().get('ECity')

	def set_ECity(self,ECity):
		self.add_query_param('ECity',ECity)

	def get_ECompany(self):
		return self.get_query_params().get('ECompany')

	def set_ECompany(self,ECompany):
		self.add_query_param('ECompany',ECompany)

	def get_EName(self):
		return self.get_query_params().get('EName')

	def set_EName(self,EName):
		self.add_query_param('EName',EName)

	def get_EProvince(self):
		return self.get_query_params().get('EProvince')

	def set_EProvince(self,EProvince):
		self.add_query_param('EProvince',EProvince)

	def get_EVenu(self):
		return self.get_query_params().get('EVenu')

	def set_EVenu(self,EVenu):
		self.add_query_param('EVenu',EVenu)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)

	def get_PostalCode(self):
		return self.get_query_params().get('PostalCode')

	def set_PostalCode(self,PostalCode):
		self.add_query_param('PostalCode',PostalCode)

	def get_TelArea(self):
		return self.get_query_params().get('TelArea')

	def set_TelArea(self,TelArea):
		self.add_query_param('TelArea',TelArea)

	def get_TelMain(self):
		return self.get_query_params().get('TelMain')

	def set_TelMain(self,TelMain):
		self.add_query_param('TelMain',TelMain)

	def get_TelExt(self):
		return self.get_query_params().get('TelExt')

	def set_TelExt(self,TelExt):
		self.add_query_param('TelExt',TelExt)

	def get_RegType(self):
		return self.get_query_params().get('RegType')

	def set_RegType(self,RegType):
		self.add_query_param('RegType',RegType)