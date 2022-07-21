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
from aliyunsdkdomain.endpoint import endpoint_data

class SaveBatchTaskForUpdatingContactInfoByNewContactRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveBatchTaskForUpdatingContactInfoByNewContact')
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
	def get_TransferOutProhibited(self): # Boolean
		return self.get_query_params().get('TransferOutProhibited')

	def set_TransferOutProhibited(self, TransferOutProhibited):  # Boolean
		self.add_query_param('TransferOutProhibited', TransferOutProhibited)
	def get_ZhCity(self): # String
		return self.get_query_params().get('ZhCity')

	def set_ZhCity(self, ZhCity):  # String
		self.add_query_param('ZhCity', ZhCity)
	def get_TelExt(self): # String
		return self.get_query_params().get('TelExt')

	def set_TelExt(self, TelExt):  # String
		self.add_query_param('TelExt', TelExt)
	def get_Province(self): # String
		return self.get_query_params().get('Province')

	def set_Province(self, Province):  # String
		self.add_query_param('Province', Province)
	def get_ZhRegistrantName(self): # String
		return self.get_query_params().get('ZhRegistrantName')

	def set_ZhRegistrantName(self, ZhRegistrantName):  # String
		self.add_query_param('ZhRegistrantName', ZhRegistrantName)
	def get_PostalCode(self): # String
		return self.get_query_params().get('PostalCode')

	def set_PostalCode(self, PostalCode):  # String
		self.add_query_param('PostalCode', PostalCode)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_ZhRegistrantOrganization(self): # String
		return self.get_query_params().get('ZhRegistrantOrganization')

	def set_ZhRegistrantOrganization(self, ZhRegistrantOrganization):  # String
		self.add_query_param('ZhRegistrantOrganization', ZhRegistrantOrganization)
	def get_Address(self): # String
		return self.get_query_params().get('Address')

	def set_Address(self, Address):  # String
		self.add_query_param('Address', Address)
	def get_TelArea(self): # String
		return self.get_query_params().get('TelArea')

	def set_TelArea(self, TelArea):  # String
		self.add_query_param('TelArea', TelArea)
	def get_ContactType(self): # String
		return self.get_query_params().get('ContactType')

	def set_ContactType(self, ContactType):  # String
		self.add_query_param('ContactType', ContactType)
	def get_ZhAddress(self): # String
		return self.get_query_params().get('ZhAddress')

	def set_ZhAddress(self, ZhAddress):  # String
		self.add_query_param('ZhAddress', ZhAddress)
	def get_RegistrantType(self): # String
		return self.get_query_params().get('RegistrantType')

	def set_RegistrantType(self, RegistrantType):  # String
		self.add_query_param('RegistrantType', RegistrantType)
	def get_DomainNames(self): # RepeatList
		return self.get_query_params().get('DomainName')

	def set_DomainNames(self, DomainName):  # RepeatList
		for depth1 in range(len(DomainName)):
			self.add_query_param('DomainName.' + str(depth1 + 1), DomainName[depth1])
	def get_Telephone(self): # String
		return self.get_query_params().get('Telephone')

	def set_Telephone(self, Telephone):  # String
		self.add_query_param('Telephone', Telephone)
	def get_ZhProvince(self): # String
		return self.get_query_params().get('ZhProvince')

	def set_ZhProvince(self, ZhProvince):  # String
		self.add_query_param('ZhProvince', ZhProvince)
	def get_RegistrantOrganization(self): # String
		return self.get_query_params().get('RegistrantOrganization')

	def set_RegistrantOrganization(self, RegistrantOrganization):  # String
		self.add_query_param('RegistrantOrganization', RegistrantOrganization)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
	def get_RegistrantName(self): # String
		return self.get_query_params().get('RegistrantName')

	def set_RegistrantName(self, RegistrantName):  # String
		self.add_query_param('RegistrantName', RegistrantName)
