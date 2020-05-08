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

class CreateRoleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'CreateRole','resourcemanager')
		self.set_protocol_type('https')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MaxSessionDuration(self):
		return self.get_query_params().get('MaxSessionDuration')

	def set_MaxSessionDuration(self,MaxSessionDuration):
		self.add_query_param('MaxSessionDuration',MaxSessionDuration)

	def get_RoleName(self):
		return self.get_query_params().get('RoleName')

	def set_RoleName(self,RoleName):
		self.add_query_param('RoleName',RoleName)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_AssumeRolePolicyDocument(self):
		return self.get_query_params().get('AssumeRolePolicyDocument')

	def set_AssumeRolePolicyDocument(self,AssumeRolePolicyDocument):
		self.add_query_param('AssumeRolePolicyDocument',AssumeRolePolicyDocument)