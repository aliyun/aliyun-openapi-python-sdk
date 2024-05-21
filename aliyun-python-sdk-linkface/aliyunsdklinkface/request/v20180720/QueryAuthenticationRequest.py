# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class QueryAuthenticationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkFace', '2018-07-20', 'QueryAuthentication')
		self.set_protocol_type('https');
		self.set_method('POST')

	def get_LicenseType(self):
		return self.get_body_params().get('LicenseType')

	def set_LicenseType(self,LicenseType):
		self.add_body_params('LicenseType', LicenseType)

	def get_IotId(self):
		return self.get_body_params().get('IotId')

	def set_IotId(self,IotId):
		self.add_body_params('IotId', IotId)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_CurrentPage(self):
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_body_params('CurrentPage', CurrentPage)

	def get_DeviceName(self):
		return self.get_body_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_body_params('DeviceName', DeviceName)

	def get_ProductKey(self):
		return self.get_body_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_body_params('ProductKey', ProductKey)