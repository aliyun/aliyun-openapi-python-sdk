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
from aliyunsdkscsp.endpoint import endpoint_data

class CreateSkillGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'CreateSkillGroup')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_DisplayName(self): # String
		return self.get_body_params().get('DisplayName')

	def set_DisplayName(self, DisplayName):  # String
		self.add_body_params('DisplayName', DisplayName)
	def get_ChannelType(self): # Integer
		return self.get_body_params().get('ChannelType')

	def set_ChannelType(self, ChannelType):  # Integer
		self.add_body_params('ChannelType', ChannelType)
	def get_SkillGroupName(self): # String
		return self.get_body_params().get('SkillGroupName')

	def set_SkillGroupName(self, SkillGroupName):  # String
		self.add_body_params('SkillGroupName', SkillGroupName)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
