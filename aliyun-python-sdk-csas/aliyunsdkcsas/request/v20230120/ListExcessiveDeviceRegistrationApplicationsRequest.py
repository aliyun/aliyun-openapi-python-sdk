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

class ListExcessiveDeviceRegistrationApplicationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListExcessiveDeviceRegistrationApplications')
		self.set_method('GET')

	def get_DeviceTag(self): # String
		return self.get_query_params().get('DeviceTag')

	def set_DeviceTag(self, DeviceTag):  # String
		self.add_query_param('DeviceTag', DeviceTag)
	def get_Mac(self): # String
		return self.get_query_params().get('Mac')

	def set_Mac(self, Mac):  # String
		self.add_query_param('Mac', Mac)
	def get_Hostname(self): # String
		return self.get_query_params().get('Hostname')

	def set_Hostname(self, Hostname):  # String
		self.add_query_param('Hostname', Hostname)
	def get_SaseUserId(self): # String
		return self.get_query_params().get('SaseUserId')

	def set_SaseUserId(self, SaseUserId):  # String
		self.add_query_param('SaseUserId', SaseUserId)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_Department(self): # String
		return self.get_query_params().get('Department')

	def set_Department(self, Department):  # String
		self.add_query_param('Department', Department)
	def get_CurrentPage(self): # Long
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Long
		self.add_query_param('CurrentPage', CurrentPage)
	def get_ApplicationIds(self): # Array
		return self.get_query_params().get('ApplicationIds')

	def set_ApplicationIds(self, ApplicationIds):  # Array
		for index1, value1 in enumerate(ApplicationIds):
			self.add_query_param('ApplicationIds.' + str(index1 + 1), value1)
	def get_Statuses(self): # Array
		return self.get_query_params().get('Statuses')

	def set_Statuses(self, Statuses):  # Array
		for index1, value1 in enumerate(Statuses):
			self.add_query_param('Statuses.' + str(index1 + 1), value1)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
