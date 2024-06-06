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

class ListUserDevicesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListUserDevices')
		self.set_method('GET')

	def get_Mac(self): # String
		return self.get_query_params().get('Mac')

	def set_Mac(self, Mac):  # String
		self.add_query_param('Mac', Mac)
	def get_DeviceTypes(self): # Array
		return self.get_query_params().get('DeviceTypes')

	def set_DeviceTypes(self, DeviceTypes):  # Array
		for index1, value1 in enumerate(DeviceTypes):
			self.add_query_param('DeviceTypes.' + str(index1 + 1), value1)
	def get_Hostname(self): # String
		return self.get_query_params().get('Hostname')

	def set_Hostname(self, Hostname):  # String
		self.add_query_param('Hostname', Hostname)
	def get_AppStatuses(self): # Array
		return self.get_query_params().get('AppStatuses')

	def set_AppStatuses(self, AppStatuses):  # Array
		for index1, value1 in enumerate(AppStatuses):
			self.add_query_param('AppStatuses.' + str(index1 + 1), value1)
	def get_DlpStatuses(self): # Array
		return self.get_query_params().get('DlpStatuses')

	def set_DlpStatuses(self, DlpStatuses):  # Array
		for index1, value1 in enumerate(DlpStatuses):
			self.add_query_param('DlpStatuses.' + str(index1 + 1), value1)
	def get_SaseUserId(self): # String
		return self.get_query_params().get('SaseUserId')

	def set_SaseUserId(self, SaseUserId):  # String
		self.add_query_param('SaseUserId', SaseUserId)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_NacStatuses(self): # Array
		return self.get_query_params().get('NacStatuses')

	def set_NacStatuses(self, NacStatuses):  # Array
		for index1, value1 in enumerate(NacStatuses):
			self.add_query_param('NacStatuses.' + str(index1 + 1), value1)
	def get_Department(self): # String
		return self.get_query_params().get('Department')

	def set_Department(self, Department):  # String
		self.add_query_param('Department', Department)
	def get_InnerIp(self): # String
		return self.get_query_params().get('InnerIp')

	def set_InnerIp(self, InnerIp):  # String
		self.add_query_param('InnerIp', InnerIp)
	def get_IaStatuses(self): # Array
		return self.get_query_params().get('IaStatuses')

	def set_IaStatuses(self, IaStatuses):  # Array
		for index1, value1 in enumerate(IaStatuses):
			self.add_query_param('IaStatuses.' + str(index1 + 1), value1)
	def get_DeviceBelong(self): # String
		return self.get_query_params().get('DeviceBelong')

	def set_DeviceBelong(self, DeviceBelong):  # String
		self.add_query_param('DeviceBelong', DeviceBelong)
	def get_CurrentPage(self): # Long
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Long
		self.add_query_param('CurrentPage', CurrentPage)
	def get_SharingStatus(self): # Boolean
		return self.get_query_params().get('SharingStatus')

	def set_SharingStatus(self, SharingStatus):  # Boolean
		self.add_query_param('SharingStatus', SharingStatus)
	def get_DeviceTags(self): # Array
		return self.get_query_params().get('DeviceTags')

	def set_DeviceTags(self, DeviceTags):  # Array
		for index1, value1 in enumerate(DeviceTags):
			self.add_query_param('DeviceTags.' + str(index1 + 1), value1)
	def get_DeviceStatuses(self): # Array
		return self.get_query_params().get('DeviceStatuses')

	def set_DeviceStatuses(self, DeviceStatuses):  # Array
		for index1, value1 in enumerate(DeviceStatuses):
			self.add_query_param('DeviceStatuses.' + str(index1 + 1), value1)
	def get_PaStatuses(self): # Array
		return self.get_query_params().get('PaStatuses')

	def set_PaStatuses(self, PaStatuses):  # Array
		for index1, value1 in enumerate(PaStatuses):
			self.add_query_param('PaStatuses.' + str(index1 + 1), value1)
	def get_SortBy(self): # String
		return self.get_query_params().get('SortBy')

	def set_SortBy(self, SortBy):  # String
		self.add_query_param('SortBy', SortBy)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
