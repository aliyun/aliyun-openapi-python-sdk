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

class CreateUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'CreateUser','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PhoneNumber(self): # String
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self, PhoneNumber):  # String
		self.add_query_param('PhoneNumber', PhoneNumber)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_PhoneRegion(self): # String
		return self.get_query_params().get('PhoneRegion')

	def set_PhoneRegion(self, PhoneRegion):  # String
		self.add_query_param('PhoneRegion', PhoneRegion)
	def get_CustomFields(self): # Array
		return self.get_query_params().get('CustomFields')

	def set_CustomFields(self, CustomFields):  # Array
		for index1, value1 in enumerate(CustomFields):
			if value1.get('FieldName') is not None:
				self.add_query_param('CustomFields.' + str(index1 + 1) + '.FieldName', value1.get('FieldName'))
			if value1.get('FieldValue') is not None:
				self.add_query_param('CustomFields.' + str(index1 + 1) + '.FieldValue', value1.get('FieldValue'))
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_PasswordInitializationConfig(self): # Struct
		return self.get_query_params().get('PasswordInitializationConfig')

	def set_PasswordInitializationConfig(self, PasswordInitializationConfig):  # Struct
		if PasswordInitializationConfig.get('UserNotificationChannels') is not None:
			for index1, value1 in enumerate(PasswordInitializationConfig.get('UserNotificationChannels')):
				self.add_query_param('PasswordInitializationConfig.UserNotificationChannels.' + str(index1 + 1), value1)
		if PasswordInitializationConfig.get('PasswordInitializationPolicyPriority') is not None:
			self.add_query_param('PasswordInitializationConfig.PasswordInitializationPolicyPriority', PasswordInitializationConfig.get('PasswordInitializationPolicyPriority'))
		if PasswordInitializationConfig.get('PasswordForcedUpdateStatus') is not None:
			self.add_query_param('PasswordInitializationConfig.PasswordForcedUpdateStatus', PasswordInitializationConfig.get('PasswordForcedUpdateStatus'))
		if PasswordInitializationConfig.get('PasswordInitializationType') is not None:
			self.add_query_param('PasswordInitializationConfig.PasswordInitializationType', PasswordInitializationConfig.get('PasswordInitializationType'))
	def get_PhoneNumberVerified(self): # Boolean
		return self.get_query_params().get('PhoneNumberVerified')

	def set_PhoneNumberVerified(self, PhoneNumberVerified):  # Boolean
		self.add_query_param('PhoneNumberVerified', PhoneNumberVerified)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_PrimaryOrganizationalUnitId(self): # String
		return self.get_query_params().get('PrimaryOrganizationalUnitId')

	def set_PrimaryOrganizationalUnitId(self, PrimaryOrganizationalUnitId):  # String
		self.add_query_param('PrimaryOrganizationalUnitId', PrimaryOrganizationalUnitId)
	def get_OrganizationalUnitIds(self): # Array
		return self.get_query_params().get('OrganizationalUnitIds')

	def set_OrganizationalUnitIds(self, OrganizationalUnitIds):  # Array
		for index1, value1 in enumerate(OrganizationalUnitIds):
			self.add_query_param('OrganizationalUnitIds.' + str(index1 + 1), value1)
	def get_UserExternalId(self): # String
		return self.get_query_params().get('UserExternalId')

	def set_UserExternalId(self, UserExternalId):  # String
		self.add_query_param('UserExternalId', UserExternalId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_DisplayName(self): # String
		return self.get_query_params().get('DisplayName')

	def set_DisplayName(self, DisplayName):  # String
		self.add_query_param('DisplayName', DisplayName)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
	def get_EmailVerified(self): # Boolean
		return self.get_query_params().get('EmailVerified')

	def set_EmailVerified(self, EmailVerified):  # Boolean
		self.add_query_param('EmailVerified', EmailVerified)
