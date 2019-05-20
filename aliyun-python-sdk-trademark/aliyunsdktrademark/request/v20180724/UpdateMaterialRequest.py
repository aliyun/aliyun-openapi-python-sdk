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
class UpdateMaterialRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'UpdateMaterial','trademark')

	def get_ContactEmail(self):
		return self.get_query_params().get('ContactEmail')

	def set_ContactEmail(self,ContactEmail):
		self.add_query_param('ContactEmail',ContactEmail)

	def get_ContactAddress(self):
		return self.get_query_params().get('ContactAddress')

	def set_ContactAddress(self,ContactAddress):
		self.add_query_param('ContactAddress',ContactAddress)

	def get_EAddress(self):
		return self.get_query_params().get('EAddress')

	def set_EAddress(self,EAddress):
		self.add_query_param('EAddress',EAddress)

	def get_LegalNoticeOssKey(self):
		return self.get_query_params().get('LegalNoticeOssKey')

	def set_LegalNoticeOssKey(self,LegalNoticeOssKey):
		self.add_query_param('LegalNoticeOssKey',LegalNoticeOssKey)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_Town(self):
		return self.get_query_params().get('Town')

	def set_Town(self,Town):
		self.add_query_param('Town',Town)

	def get_ContactNumber(self):
		return self.get_query_params().get('ContactNumber')

	def set_ContactNumber(self,ContactNumber):
		self.add_query_param('ContactNumber',ContactNumber)

	def get_City(self):
		return self.get_query_params().get('City')

	def set_City(self,City):
		self.add_query_param('City',City)

	def get_IdCardOssKey(self):
		return self.get_query_params().get('IdCardOssKey')

	def set_IdCardOssKey(self,IdCardOssKey):
		self.add_query_param('IdCardOssKey',IdCardOssKey)

	def get_ContactName(self):
		return self.get_query_params().get('ContactName')

	def set_ContactName(self,ContactName):
		self.add_query_param('ContactName',ContactName)

	def get_PassportOssKey(self):
		return self.get_query_params().get('PassportOssKey')

	def set_PassportOssKey(self,PassportOssKey):
		self.add_query_param('PassportOssKey',PassportOssKey)

	def get_ContactZipcode(self):
		return self.get_query_params().get('ContactZipcode')

	def set_ContactZipcode(self,ContactZipcode):
		self.add_query_param('ContactZipcode',ContactZipcode)

	def get_EName(self):
		return self.get_query_params().get('EName')

	def set_EName(self,EName):
		self.add_query_param('EName',EName)

	def get_Province(self):
		return self.get_query_params().get('Province')

	def set_Province(self,Province):
		self.add_query_param('Province',Province)

	def get_BusinessLicenceOssKey(self):
		return self.get_query_params().get('BusinessLicenceOssKey')

	def set_BusinessLicenceOssKey(self,BusinessLicenceOssKey):
		self.add_query_param('BusinessLicenceOssKey',BusinessLicenceOssKey)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_CardNumber(self):
		return self.get_query_params().get('CardNumber')

	def set_CardNumber(self,CardNumber):
		self.add_query_param('CardNumber',CardNumber)

	def get_LoaId(self):
		return self.get_query_params().get('LoaId')

	def set_LoaId(self,LoaId):
		self.add_query_param('LoaId',LoaId)

	def get_LoaOssKey(self):
		return self.get_query_params().get('LoaOssKey')

	def set_LoaOssKey(self,LoaOssKey):
		self.add_query_param('LoaOssKey',LoaOssKey)