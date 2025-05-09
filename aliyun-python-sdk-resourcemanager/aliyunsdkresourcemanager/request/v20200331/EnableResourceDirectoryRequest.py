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
from aliyunsdkresourcemanager.endpoint import endpoint_data

class EnableResourceDirectoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'EnableResourceDirectory','resourcemanager')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EnableMode(self): # String
		return self.get_query_params().get('EnableMode')

	def set_EnableMode(self, EnableMode):  # String
		self.add_query_param('EnableMode', EnableMode)
	def get_MASecureMobilePhone(self): # String
		return self.get_query_params().get('MASecureMobilePhone')

	def set_MASecureMobilePhone(self, MASecureMobilePhone):  # String
		self.add_query_param('MASecureMobilePhone', MASecureMobilePhone)
	def get_MAName(self): # String
		return self.get_query_params().get('MAName')

	def set_MAName(self, MAName):  # String
		self.add_query_param('MAName', MAName)
	def get_VerificationCode(self): # String
		return self.get_query_params().get('VerificationCode')

	def set_VerificationCode(self, VerificationCode):  # String
		self.add_query_param('VerificationCode', VerificationCode)
