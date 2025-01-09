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

class UpdateUserPasswordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eiam', '2021-12-01', 'UpdateUserPassword','eiam')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_UserNotificationChannels(self): # Array
		return self.get_query_params().get('UserNotificationChannels')

	def set_UserNotificationChannels(self, UserNotificationChannels):  # Array
		for index1, value1 in enumerate(UserNotificationChannels):
			self.add_query_param('UserNotificationChannels.' + str(index1 + 1), value1)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_PasswordForcedUpdateStatus(self): # String
		return self.get_query_params().get('PasswordForcedUpdateStatus')

	def set_PasswordForcedUpdateStatus(self, PasswordForcedUpdateStatus):  # String
		self.add_query_param('PasswordForcedUpdateStatus', PasswordForcedUpdateStatus)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
