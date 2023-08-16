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
import json

class UpdatePrivateAccessApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'UpdatePrivateAccessApplication')
		self.set_method('POST')

	def get_Addresses(self): # Array
		return self.get_body_params().get('Addresses')

	def set_Addresses(self, Addresses):  # Array
		self.add_body_params("Addresses", json.dumps(Addresses))
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_Protocol(self): # String
		return self.get_body_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_body_params('Protocol', Protocol)
	def get_ApplicationId(self): # String
		return self.get_body_params().get('ApplicationId')

	def set_ApplicationId(self, ApplicationId):  # String
		self.add_body_params('ApplicationId', ApplicationId)
	def get_TagIds(self): # Array
		return self.get_body_params().get('TagIds')

	def set_TagIds(self, TagIds):  # Array
		self.add_body_params("TagIds", json.dumps(TagIds))
	def get_PortRanges(self): # Array
		return self.get_body_params().get('PortRanges')

	def set_PortRanges(self, PortRanges):  # Array
		self.add_body_params("PortRanges", json.dumps(PortRanges))
	def get_ModifyType(self): # String
		return self.get_body_params().get('ModifyType')

	def set_ModifyType(self, ModifyType):  # String
		self.add_body_params('ModifyType', ModifyType)
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
