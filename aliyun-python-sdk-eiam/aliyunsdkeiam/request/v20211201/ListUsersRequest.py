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

class ListUsersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'ListUsers','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PhoneNumber(self): # String
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self, PhoneNumber):  # String
		self.add_query_param('PhoneNumber', PhoneNumber)
	def get_PhoneRegion(self): # String
		return self.get_query_params().get('PhoneRegion')

	def set_PhoneRegion(self, PhoneRegion):  # String
		self.add_query_param('PhoneRegion', PhoneRegion)
	def get_PageNumber(self): # Long
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Long
		self.add_query_param('PageNumber', PageNumber)
	def get_UsernameStartsWith(self): # String
		return self.get_query_params().get('UsernameStartsWith')

	def set_UsernameStartsWith(self, UsernameStartsWith):  # String
		self.add_query_param('UsernameStartsWith', UsernameStartsWith)
	def get_UserSourceType(self): # String
		return self.get_query_params().get('UserSourceType')

	def set_UserSourceType(self, UserSourceType):  # String
		self.add_query_param('UserSourceType', UserSourceType)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_UserExternalId(self): # String
		return self.get_query_params().get('UserExternalId')

	def set_UserExternalId(self, UserExternalId):  # String
		self.add_query_param('UserExternalId', UserExternalId)
	def get_DisplayNameStartsWith(self): # String
		return self.get_query_params().get('DisplayNameStartsWith')

	def set_DisplayNameStartsWith(self, DisplayNameStartsWith):  # String
		self.add_query_param('DisplayNameStartsWith', DisplayNameStartsWith)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_UserIds(self): # Array
		return self.get_query_params().get('UserIds')

	def set_UserIds(self, UserIds):  # Array
		for index1, value1 in enumerate(UserIds):
			self.add_query_param('UserIds.' + str(index1 + 1), value1)
	def get_UserSourceId(self): # String
		return self.get_query_params().get('UserSourceId')

	def set_UserSourceId(self, UserSourceId):  # String
		self.add_query_param('UserSourceId', UserSourceId)
	def get_OrganizationalUnitId(self): # String
		return self.get_query_params().get('OrganizationalUnitId')

	def set_OrganizationalUnitId(self, OrganizationalUnitId):  # String
		self.add_query_param('OrganizationalUnitId', OrganizationalUnitId)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
