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

class UpdateUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'UpdateUser','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PhoneNumber(self): # String
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self, PhoneNumber):  # String
		self.add_query_param('PhoneNumber', PhoneNumber)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
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
			if value1.get('Operation') is not None:
				self.add_query_param('CustomFields.' + str(index1 + 1) + '.Operation', value1.get('Operation'))
	def get_PhoneNumberVerified(self): # Boolean
		return self.get_query_params().get('PhoneNumberVerified')

	def set_PhoneNumberVerified(self, PhoneNumberVerified):  # Boolean
		self.add_query_param('PhoneNumberVerified', PhoneNumberVerified)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
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
