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
from aliyunsdksls.endpoint import endpoint_data

class EnableAlertRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sls', '2019-10-23', 'EnableAlert')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Language(self):
		return self.get_body_params().get('Language')

	def set_Language(self,Language):
		self.add_body_params('Language', Language)

	def get_RuleVersion(self):
		return self.get_body_params().get('RuleVersion')

	def set_RuleVersion(self,RuleVersion):
		self.add_body_params('RuleVersion', RuleVersion)

	def get_Endpoint(self):
		return self.get_body_params().get('Endpoint')

	def set_Endpoint(self,Endpoint):
		self.add_body_params('Endpoint', Endpoint)

	def get_Tokens(self):
		return self.get_body_params().get('Tokens')

	def set_Tokens(self,Tokens):
		self.add_body_params('Tokens', Tokens)

	def get_App(self):
		return self.get_body_params().get('App')

	def set_App(self,App):
		self.add_body_params('App', App)

	def get_ProjectName(self):
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_body_params('ProjectName', ProjectName)

	def get_AlertId(self):
		return self.get_body_params().get('AlertId')

	def set_AlertId(self,AlertId):
		self.add_body_params('AlertId', AlertId)

	def get_RuleId(self):
		return self.get_body_params().get('RuleId')

	def set_RuleId(self,RuleId):
		self.add_body_params('RuleId', RuleId)

	def get_Region(self):
		return self.get_body_params().get('Region')

	def set_Region(self,Region):
		self.add_body_params('Region', Region)