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

class CreatePrivateAccessApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'CreatePrivateAccessApplication')
		self.set_method('POST')

	def get_Addresses(self): # Array
		return self.get_body_params().get('Addresses')

	def set_Addresses(self, Addresses):  # Array
		for index1, value1 in enumerate(Addresses):
			self.add_body_params('Addresses.' + str(index1 + 1), value1)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_Protocol(self): # String
		return self.get_body_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_body_params('Protocol', Protocol)
	def get_TagIds(self): # Array
		return self.get_body_params().get('TagIds')

	def set_TagIds(self, TagIds):  # Array
		for index1, value1 in enumerate(TagIds):
			self.add_body_params('TagIds.' + str(index1 + 1), value1)
	def get_PortRanges(self): # Array
		return self.get_body_params().get('PortRanges')

	def set_PortRanges(self, PortRanges):  # Array
		for index1, value1 in enumerate(PortRanges):
			if value1.get('End') is not None:
				self.add_body_params('PortRanges.' + str(index1 + 1) + '.End', value1.get('End'))
			if value1.get('Begin') is not None:
				self.add_body_params('PortRanges.' + str(index1 + 1) + '.Begin', value1.get('Begin'))
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
