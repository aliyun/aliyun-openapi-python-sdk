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

class UpdateRoleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'UpdateRole')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NewAssumeRolePolicyDocument(self): # String
		return self.get_query_params().get('NewAssumeRolePolicyDocument')

	def set_NewAssumeRolePolicyDocument(self, NewAssumeRolePolicyDocument):  # String
		self.add_query_param('NewAssumeRolePolicyDocument', NewAssumeRolePolicyDocument)
	def get_RoleName(self): # String
		return self.get_query_params().get('RoleName')

	def set_RoleName(self, RoleName):  # String
		self.add_query_param('RoleName', RoleName)
	def get_NewMaxSessionDuration(self): # Long
		return self.get_query_params().get('NewMaxSessionDuration')

	def set_NewMaxSessionDuration(self, NewMaxSessionDuration):  # Long
		self.add_query_param('NewMaxSessionDuration', NewMaxSessionDuration)
	def get_NewDescription(self): # String
		return self.get_query_params().get('NewDescription')

	def set_NewDescription(self, NewDescription):  # String
		self.add_query_param('NewDescription', NewDescription)
