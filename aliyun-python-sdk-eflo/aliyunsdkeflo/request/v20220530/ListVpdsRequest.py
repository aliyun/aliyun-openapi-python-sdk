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

class ListVpdsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'ListVpds','eflo')
		self.set_method('POST')

	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_WithDependence(self): # Boolean
		return self.get_body_params().get('WithDependence')

	def set_WithDependence(self, WithDependence):  # Boolean
		self.add_body_params('WithDependence', WithDependence)
	def get_WithoutVcc(self): # Boolean
		return self.get_body_params().get('WithoutVcc')

	def set_WithoutVcc(self, WithoutVcc):  # Boolean
		self.add_body_params('WithoutVcc', WithoutVcc)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_ForSelect(self): # Boolean
		return self.get_body_params().get('ForSelect')

	def set_ForSelect(self, ForSelect):  # Boolean
		self.add_body_params('ForSelect', ForSelect)
	def get_FilterErId(self): # String
		return self.get_body_params().get('FilterErId')

	def set_FilterErId(self, FilterErId):  # String
		self.add_body_params('FilterErId', FilterErId)
	def get_VpdId(self): # String
		return self.get_body_params().get('VpdId')

	def set_VpdId(self, VpdId):  # String
		self.add_body_params('VpdId', VpdId)
	def get_EnablePage(self): # Boolean
		return self.get_body_params().get('EnablePage')

	def set_EnablePage(self, EnablePage):  # Boolean
		self.add_body_params('EnablePage', EnablePage)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
