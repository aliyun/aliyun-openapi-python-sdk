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

class ListErsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'ListErs','eflo')
		self.set_method('POST')

	def get_MasterZoneId(self): # String
		return self.get_body_params().get('MasterZoneId')

	def set_MasterZoneId(self, MasterZoneId):  # String
		self.add_body_params('MasterZoneId', MasterZoneId)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_InstanceType(self): # String
		return self.get_body_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_body_params('InstanceType', InstanceType)
	def get_ErId(self): # String
		return self.get_body_params().get('ErId')

	def set_ErId(self, ErId):  # String
		self.add_body_params('ErId', ErId)
	def get_ErName(self): # String
		return self.get_body_params().get('ErName')

	def set_ErName(self, ErName):  # String
		self.add_body_params('ErName', ErName)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_EnablePage(self): # Boolean
		return self.get_body_params().get('EnablePage')

	def set_EnablePage(self, EnablePage):  # Boolean
		self.add_body_params('EnablePage', EnablePage)
