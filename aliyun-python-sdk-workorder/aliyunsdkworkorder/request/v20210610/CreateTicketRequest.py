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
from aliyunsdkworkorder.endpoint import endpoint_data
import json

class CreateTicketRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Workorder', '2021-06-10', 'CreateTicket')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Severity(self): # Integer
		return self.get_body_params().get('Severity')

	def set_Severity(self, Severity):  # Integer
		self.add_body_params('Severity', Severity)
	def get_CreatorId(self): # String
		return self.get_body_params().get('CreatorId')

	def set_CreatorId(self, CreatorId):  # String
		self.add_body_params('CreatorId', CreatorId)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_Title(self): # String
		return self.get_body_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_body_params('Title', Title)
	def get_FileNameList(self): # Array
		return self.get_body_params().get('FileNameList')

	def set_FileNameList(self, FileNameList):  # Array
		for index1, value1 in enumerate(FileNameList):
			self.add_body_params('FileNameList.' + str(index1 + 1), value1)
	def get_SecretInfo(self): # Struct
		return self.get_query_params().get('SecretInfo')

	def set_SecretInfo(self, SecretInfo):  # Struct
		self.add_query_param("SecretInfo", json.dumps(SecretInfo))
	def get_CategoryId(self): # String
		return self.get_body_params().get('CategoryId')

	def set_CategoryId(self, CategoryId):  # String
		self.add_body_params('CategoryId', CategoryId)
	def get_Email(self): # String
		return self.get_body_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_body_params('Email', Email)
