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

class SetPasswordInitializationConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'SetPasswordInitializationConfiguration','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PasswordInitializationType(self): # String
		return self.get_query_params().get('PasswordInitializationType')

	def set_PasswordInitializationType(self, PasswordInitializationType):  # String
		self.add_query_param('PasswordInitializationType', PasswordInitializationType)
	def get_PasswordInitializationNotificationChannels(self): # Array
		return self.get_query_params().get('PasswordInitializationNotificationChannels')

	def set_PasswordInitializationNotificationChannels(self, PasswordInitializationNotificationChannels):  # Array
		for index1, value1 in enumerate(PasswordInitializationNotificationChannels):
			self.add_query_param('PasswordInitializationNotificationChannels.' + str(index1 + 1), value1)
	def get_PasswordInitializationStatus(self): # String
		return self.get_query_params().get('PasswordInitializationStatus')

	def set_PasswordInitializationStatus(self, PasswordInitializationStatus):  # String
		self.add_query_param('PasswordInitializationStatus', PasswordInitializationStatus)
	def get_PasswordForcedUpdateStatus(self): # String
		return self.get_query_params().get('PasswordForcedUpdateStatus')

	def set_PasswordForcedUpdateStatus(self, PasswordForcedUpdateStatus):  # String
		self.add_query_param('PasswordForcedUpdateStatus', PasswordForcedUpdateStatus)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
