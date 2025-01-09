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

class SetPasswordExpirationConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'SetPasswordExpirationConfiguration','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PasswordForcedUpdateDuration(self): # Integer
		return self.get_query_params().get('PasswordForcedUpdateDuration')

	def set_PasswordForcedUpdateDuration(self, PasswordForcedUpdateDuration):  # Integer
		self.add_query_param('PasswordForcedUpdateDuration', PasswordForcedUpdateDuration)
	def get_EffectiveAuthenticationSourceIds(self): # Array
		return self.get_query_params().get('EffectiveAuthenticationSourceIds')

	def set_EffectiveAuthenticationSourceIds(self, EffectiveAuthenticationSourceIds):  # Array
		for index1, value1 in enumerate(EffectiveAuthenticationSourceIds):
			self.add_query_param('EffectiveAuthenticationSourceIds.' + str(index1 + 1), value1)
	def get_PasswordExpirationNotificationDuration(self): # Integer
		return self.get_query_params().get('PasswordExpirationNotificationDuration')

	def set_PasswordExpirationNotificationDuration(self, PasswordExpirationNotificationDuration):  # Integer
		self.add_query_param('PasswordExpirationNotificationDuration', PasswordExpirationNotificationDuration)
	def get_PasswordExpirationStatus(self): # String
		return self.get_query_params().get('PasswordExpirationStatus')

	def set_PasswordExpirationStatus(self, PasswordExpirationStatus):  # String
		self.add_query_param('PasswordExpirationStatus', PasswordExpirationStatus)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_PasswordExpirationAction(self): # String
		return self.get_query_params().get('PasswordExpirationAction')

	def set_PasswordExpirationAction(self, PasswordExpirationAction):  # String
		self.add_query_param('PasswordExpirationAction', PasswordExpirationAction)
	def get_PasswordValidMaxDay(self): # Integer
		return self.get_query_params().get('PasswordValidMaxDay')

	def set_PasswordValidMaxDay(self, PasswordValidMaxDay):  # Integer
		self.add_query_param('PasswordValidMaxDay', PasswordValidMaxDay)
	def get_PasswordExpirationNotificationChannels(self): # Array
		return self.get_query_params().get('PasswordExpirationNotificationChannels')

	def set_PasswordExpirationNotificationChannels(self, PasswordExpirationNotificationChannels):  # Array
		for index1, value1 in enumerate(PasswordExpirationNotificationChannels):
			self.add_query_param('PasswordExpirationNotificationChannels.' + str(index1 + 1), value1)
	def get_PasswordExpirationNotificationStatus(self): # String
		return self.get_query_params().get('PasswordExpirationNotificationStatus')

	def set_PasswordExpirationNotificationStatus(self, PasswordExpirationNotificationStatus):  # String
		self.add_query_param('PasswordExpirationNotificationStatus', PasswordExpirationNotificationStatus)
