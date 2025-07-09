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

class CreateLogoTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'WebsiteBuild', '2025-04-29', 'CreateLogoTask')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_NegativePrompt(self): # String
		return self.get_query_params().get('NegativePrompt')

	def set_NegativePrompt(self, NegativePrompt):  # String
		self.add_query_param('NegativePrompt', NegativePrompt)
	def get_Prompt(self): # String
		return self.get_query_params().get('Prompt')

	def set_Prompt(self, Prompt):  # String
		self.add_query_param('Prompt', Prompt)
	def get_Parameters(self): # String
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # String
		self.add_query_param('Parameters', Parameters)
	def get_LogoVersion(self): # String
		return self.get_query_params().get('LogoVersion')

	def set_LogoVersion(self, LogoVersion):  # String
		self.add_query_param('LogoVersion', LogoVersion)
