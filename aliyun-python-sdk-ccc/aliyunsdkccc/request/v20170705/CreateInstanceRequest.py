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
from aliyunsdkccc.endpoint import endpoint_data

class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'CreateInstance','CCC')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PhoneNumberss(self):
		return self.get_query_params().get('PhoneNumbers')

	def set_PhoneNumberss(self, PhoneNumberss):
		for depth1 in range(len(PhoneNumberss)):
			if PhoneNumberss[depth1] is not None:
				self.add_query_param('PhoneNumbers.' + str(depth1 + 1) , PhoneNumberss[depth1])

	def get_UserObjects(self):
		return self.get_query_params().get('UserObject')

	def set_UserObjects(self, UserObjects):
		for depth1 in range(len(UserObjects)):
			if UserObjects[depth1] is not None:
				self.add_query_param('UserObject.' + str(depth1 + 1) , UserObjects[depth1])

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_PhoneNumber(self):
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self,PhoneNumber):
		self.add_query_param('PhoneNumber',PhoneNumber)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_StorageMaxDays(self):
		return self.get_query_params().get('StorageMaxDays')

	def set_StorageMaxDays(self,StorageMaxDays):
		self.add_query_param('StorageMaxDays',StorageMaxDays)

	def get_AdminRamIds(self):
		return self.get_query_params().get('AdminRamId')

	def set_AdminRamIds(self, AdminRamIds):
		for depth1 in range(len(AdminRamIds)):
			if AdminRamIds[depth1] is not None:
				self.add_query_param('AdminRamId.' + str(depth1 + 1) , AdminRamIds[depth1])

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_StorageMaxSize(self):
		return self.get_query_params().get('StorageMaxSize')

	def set_StorageMaxSize(self,StorageMaxSize):
		self.add_query_param('StorageMaxSize',StorageMaxSize)

	def get_DirectoryId(self):
		return self.get_query_params().get('DirectoryId')

	def set_DirectoryId(self,DirectoryId):
		self.add_query_param('DirectoryId',DirectoryId)