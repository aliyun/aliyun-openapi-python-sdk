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
from aliyunsdkram.endpoint import endpoint_data
import json

class CreateRoleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ram', '2015-05-01', 'CreateRole','ram')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_AssumeRolePolicyDocument(self): # String
		return self.get_query_params().get('AssumeRolePolicyDocument')

	def set_AssumeRolePolicyDocument(self, AssumeRolePolicyDocument):  # String
		self.add_query_param('AssumeRolePolicyDocument', AssumeRolePolicyDocument)
	def get_Tag(self): # Array
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		self.add_query_param("Tag", json.dumps(Tag))
	def get_MaxSessionDuration(self): # Long
		return self.get_query_params().get('MaxSessionDuration')

	def set_MaxSessionDuration(self, MaxSessionDuration):  # Long
		self.add_query_param('MaxSessionDuration', MaxSessionDuration)
	def get_RoleName(self): # String
		return self.get_query_params().get('RoleName')

	def set_RoleName(self, RoleName):  # String
		self.add_query_param('RoleName', RoleName)
