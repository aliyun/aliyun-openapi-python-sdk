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

class GenerateTextDeformationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aigen', '2024-01-11', 'GenerateTextDeformation')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_TextContent(self): # String
		return self.get_body_params().get('TextContent')

	def set_TextContent(self, TextContent):  # String
		self.add_body_params('TextContent', TextContent)
	def get_FontName(self): # String
		return self.get_body_params().get('FontName')

	def set_FontName(self, FontName):  # String
		self.add_body_params('FontName', FontName)
	def get_TtfUrl(self): # String
		return self.get_body_params().get('TtfUrl')

	def set_TtfUrl(self, TtfUrl):  # String
		self.add_body_params('TtfUrl', TtfUrl)
	def get_N(self): # Long
		return self.get_body_params().get('N')

	def set_N(self, N):  # Long
		self.add_body_params('N', N)
	def get_Async(self): # Boolean
		return self.get_body_params().get('Async')

	def set_Async(self, _Async):  # Boolean
		self.add_body_params('Async', _Async)
	def get_Prompt(self): # String
		return self.get_body_params().get('Prompt')

	def set_Prompt(self, Prompt):  # String
		self.add_body_params('Prompt', Prompt)
	def get_OutputImageRatio(self): # String
		return self.get_body_params().get('OutputImageRatio')

	def set_OutputImageRatio(self, OutputImageRatio):  # String
		self.add_body_params('OutputImageRatio', OutputImageRatio)
