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

class StartExecutionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'StartExecution','oos')

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Mode(self):
		return self.get_query_params().get('Mode')

	def set_Mode(self,Mode):
		self.add_query_param('Mode',Mode)

	def get_TemplateVersion(self):
		return self.get_query_params().get('TemplateVersion')

	def set_TemplateVersion(self,TemplateVersion):
		self.add_query_param('TemplateVersion',TemplateVersion)

	def get_TemplateName(self):
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self,TemplateName):
		self.add_query_param('TemplateName',TemplateName)

	def get_LoopMode(self):
		return self.get_query_params().get('LoopMode')

	def set_LoopMode(self,LoopMode):
		self.add_query_param('LoopMode',LoopMode)

	def get_SafetyCheck(self):
		return self.get_query_params().get('SafetyCheck')

	def set_SafetyCheck(self,SafetyCheck):
		self.add_query_param('SafetyCheck',SafetyCheck)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_ParentExecutionId(self):
		return self.get_query_params().get('ParentExecutionId')

	def set_ParentExecutionId(self,ParentExecutionId):
		self.add_query_param('ParentExecutionId',ParentExecutionId)

	def get_Parameters(self):
		return self.get_query_params().get('Parameters')

	def set_Parameters(self,Parameters):
		self.add_query_param('Parameters',Parameters)