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

class UpdateUserDevicesSharingStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'UpdateUserDevicesSharingStatus')
		self.set_method('POST')

	def get_SharingStatus(self): # Boolean
		return self.get_body_params().get('SharingStatus')

	def set_SharingStatus(self, SharingStatus):  # Boolean
		self.add_body_params('SharingStatus', SharingStatus)
	def get_DeviceTags(self): # Array
		return self.get_body_params().get('DeviceTags')

	def set_DeviceTags(self, DeviceTags):  # Array
		for index1, value1 in enumerate(DeviceTags):
			self.add_body_params('DeviceTags.' + str(index1 + 1), value1)
