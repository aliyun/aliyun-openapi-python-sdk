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
from aliyunsdkros.endpoint import endpoint_data

class CreateStackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ROS', '2019-09-10', 'CreateStack','ros')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TimeoutInMinutes(self):
		return self.get_query_params().get('TimeoutInMinutes')

	def set_TimeoutInMinutes(self,TimeoutInMinutes):
		self.add_query_param('TimeoutInMinutes',TimeoutInMinutes)

	def get_DeletionProtection(self):
		return self.get_query_params().get('DeletionProtection')

	def set_DeletionProtection(self,DeletionProtection):
		self.add_query_param('DeletionProtection',DeletionProtection)

	def get_TemplateVersion(self):
		return self.get_query_params().get('TemplateVersion')

	def set_TemplateVersion(self,TemplateVersion):
		self.add_query_param('TemplateVersion',TemplateVersion)

	def get_StackName(self):
		return self.get_query_params().get('StackName')

	def set_StackName(self,StackName):
		self.add_query_param('StackName',StackName)

	def get_DisableRollback(self):
		return self.get_query_params().get('DisableRollback')

	def set_DisableRollback(self,DisableRollback):
		self.add_query_param('DisableRollback',DisableRollback)

	def get_TemplateId(self):
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_query_param('TemplateId',TemplateId)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tagss):
		for depth1 in range(len(Tagss)):
			if Tagss[depth1].get('Value') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Value', Tagss[depth1].get('Value'))
			if Tagss[depth1].get('Key') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Key', Tagss[depth1].get('Key'))

	def get_Parameters(self):
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameterss):
		for depth1 in range(len(Parameterss)):
			if Parameterss[depth1].get('ParameterValue') is not None:
				self.add_query_param('Parameters.' + str(depth1 + 1) + '.ParameterValue', Parameterss[depth1].get('ParameterValue'))
			if Parameterss[depth1].get('ParameterKey') is not None:
				self.add_query_param('Parameters.' + str(depth1 + 1) + '.ParameterKey', Parameterss[depth1].get('ParameterKey'))

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_TemplateBody(self):
		return self.get_query_params().get('TemplateBody')

	def set_TemplateBody(self,TemplateBody):
		self.add_query_param('TemplateBody',TemplateBody)

	def get_TemplateURL(self):
		return self.get_query_params().get('TemplateURL')

	def set_TemplateURL(self,TemplateURL):
		self.add_query_param('TemplateURL',TemplateURL)

	def get_NotificationURLs(self):
		return self.get_query_params().get('NotificationURLs')

	def set_NotificationURLs(self, NotificationURLss):
		for depth1 in range(len(NotificationURLss)):
			if NotificationURLss[depth1] is not None:
				self.add_query_param('NotificationURLs.' + str(depth1 + 1) , NotificationURLss[depth1])

	def get_StackPolicyBody(self):
		return self.get_query_params().get('StackPolicyBody')

	def set_StackPolicyBody(self,StackPolicyBody):
		self.add_query_param('StackPolicyBody',StackPolicyBody)

	def get_RamRoleName(self):
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self,RamRoleName):
		self.add_query_param('RamRoleName',RamRoleName)

	def get_CreateOption(self):
		return self.get_query_params().get('CreateOption')

	def set_CreateOption(self,CreateOption):
		self.add_query_param('CreateOption',CreateOption)

	def get_StackPolicyURL(self):
		return self.get_query_params().get('StackPolicyURL')

	def set_StackPolicyURL(self,StackPolicyURL):
		self.add_query_param('StackPolicyURL',StackPolicyURL)