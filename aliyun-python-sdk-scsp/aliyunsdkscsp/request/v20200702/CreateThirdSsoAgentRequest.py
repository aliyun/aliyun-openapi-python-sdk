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

class CreateThirdSsoAgentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'CreateThirdSsoAgent')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_ClientId(self): # String
		return self.get_body_params().get('ClientId')

	def set_ClientId(self, ClientId):  # String
		self.add_body_params('ClientId', ClientId)
	def get_AccountId(self): # String
		return self.get_body_params().get('AccountId')

	def set_AccountId(self, AccountId):  # String
		self.add_body_params('AccountId', AccountId)
	def get_AccountName(self): # String
		return self.get_body_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_body_params('AccountName', AccountName)
	def get_DisplayName(self): # String
		return self.get_body_params().get('DisplayName')

	def set_DisplayName(self, DisplayName):  # String
		self.add_body_params('DisplayName', DisplayName)
	def get_SkillGroupIds(self): # Array
		return self.get_body_params().get('SkillGroupIds')

	def set_SkillGroupIds(self, SkillGroupIds):  # Array
		for index1, value1 in enumerate(SkillGroupIds):
			self.add_body_params('SkillGroupIds.' + str(index1 + 1) + '.SkillGroupIds', value1)
	def get_RoleIds(self): # Array
		return self.get_body_params().get('RoleIds')

	def set_RoleIds(self, RoleIds):  # Array
		for index1, value1 in enumerate(RoleIds):
			self.add_body_params('RoleIds.' + str(index1 + 1) + '.RoleIds', value1)
