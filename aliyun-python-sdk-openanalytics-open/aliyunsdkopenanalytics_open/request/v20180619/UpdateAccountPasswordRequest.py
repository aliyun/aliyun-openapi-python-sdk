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
from aliyunsdkopenanalytics_open.endpoint import endpoint_data

class UpdateAccountPasswordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'openanalytics-open', '2018-06-19', 'UpdateAccountPassword','openanalytics')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IsShort(self):
		return self.get_body_params().get('IsShort')

	def set_IsShort(self,IsShort):
		self.add_body_params('IsShort', IsShort)

	def get_Password(self):
		return self.get_body_params().get('Password')

	def set_Password(self,Password):
		self.add_body_params('Password', Password)

	def get_AccountName(self):
		return self.get_body_params().get('AccountName')

	def set_AccountName(self,AccountName):
		self.add_body_params('AccountName', AccountName)

	def get_EnableKMS(self):
		return self.get_body_params().get('EnableKMS')

	def set_EnableKMS(self,EnableKMS):
		self.add_body_params('EnableKMS', EnableKMS)

	def get_UseRandomPassword(self):
		return self.get_body_params().get('UseRandomPassword')

	def set_UseRandomPassword(self,UseRandomPassword):
		self.add_body_params('UseRandomPassword', UseRandomPassword)