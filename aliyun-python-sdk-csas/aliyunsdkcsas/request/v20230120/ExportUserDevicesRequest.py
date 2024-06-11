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

class ExportUserDevicesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ExportUserDevices')
		self.set_method('POST')

	def get_Mac(self): # String
		return self.get_body_params().get('Mac')

	def set_Mac(self, Mac):  # String
		self.add_body_params('Mac', Mac)
	def get_DeviceTypes(self): # Array
		return self.get_body_params().get('DeviceTypes')

	def set_DeviceTypes(self, DeviceTypes):  # Array
		for index1, value1 in enumerate(DeviceTypes):
			self.add_body_params('DeviceTypes.' + str(index1 + 1), value1)
	def get_Hostname(self): # String
		return self.get_body_params().get('Hostname')

	def set_Hostname(self, Hostname):  # String
		self.add_body_params('Hostname', Hostname)
	def get_AppStatuses(self): # Array
		return self.get_body_params().get('AppStatuses')

	def set_AppStatuses(self, AppStatuses):  # Array
		for index1, value1 in enumerate(AppStatuses):
			self.add_body_params('AppStatuses.' + str(index1 + 1), value1)
	def get_DlpStatuses(self): # Array
		return self.get_body_params().get('DlpStatuses')

	def set_DlpStatuses(self, DlpStatuses):  # Array
		for index1, value1 in enumerate(DlpStatuses):
			self.add_body_params('DlpStatuses.' + str(index1 + 1), value1)
	def get_SaseUserId(self): # String
		return self.get_body_params().get('SaseUserId')

	def set_SaseUserId(self, SaseUserId):  # String
		self.add_body_params('SaseUserId', SaseUserId)
	def get_NacStatuses(self): # Array
		return self.get_body_params().get('NacStatuses')

	def set_NacStatuses(self, NacStatuses):  # Array
		for index1, value1 in enumerate(NacStatuses):
			self.add_body_params('NacStatuses.' + str(index1 + 1), value1)
	def get_Department(self): # String
		return self.get_body_params().get('Department')

	def set_Department(self, Department):  # String
		self.add_body_params('Department', Department)
	def get_IaStatuses(self): # Array
		return self.get_body_params().get('IaStatuses')

	def set_IaStatuses(self, IaStatuses):  # Array
		for index1, value1 in enumerate(IaStatuses):
			self.add_body_params('IaStatuses.' + str(index1 + 1), value1)
	def get_DeviceBelong(self): # String
		return self.get_body_params().get('DeviceBelong')

	def set_DeviceBelong(self, DeviceBelong):  # String
		self.add_body_params('DeviceBelong', DeviceBelong)
	def get_SharingStatus(self): # Boolean
		return self.get_body_params().get('SharingStatus')

	def set_SharingStatus(self, SharingStatus):  # Boolean
		self.add_body_params('SharingStatus', SharingStatus)
	def get_DeviceTags(self): # Array
		return self.get_body_params().get('DeviceTags')

	def set_DeviceTags(self, DeviceTags):  # Array
		for index1, value1 in enumerate(DeviceTags):
			self.add_body_params('DeviceTags.' + str(index1 + 1), value1)
	def get_DeviceStatuses(self): # Array
		return self.get_body_params().get('DeviceStatuses')

	def set_DeviceStatuses(self, DeviceStatuses):  # Array
		for index1, value1 in enumerate(DeviceStatuses):
			self.add_body_params('DeviceStatuses.' + str(index1 + 1), value1)
	def get_PaStatuses(self): # Array
		return self.get_body_params().get('PaStatuses')

	def set_PaStatuses(self, PaStatuses):  # Array
		for index1, value1 in enumerate(PaStatuses):
			self.add_body_params('PaStatuses.' + str(index1 + 1), value1)
	def get_Username(self): # String
		return self.get_body_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_body_params('Username', Username)
