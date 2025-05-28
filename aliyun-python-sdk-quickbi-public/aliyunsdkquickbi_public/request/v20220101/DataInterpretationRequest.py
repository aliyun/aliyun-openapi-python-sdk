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

class DataInterpretationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'DataInterpretation','2.2.0')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PromptForceOverride(self): # Boolean
		return self.get_query_params().get('PromptForceOverride')

	def set_PromptForceOverride(self, PromptForceOverride):  # Boolean
		self.add_query_param('PromptForceOverride', PromptForceOverride)
	def get_Data(self): # String
		return self.get_query_params().get('Data')

	def set_Data(self, Data):  # String
		self.add_query_param('Data', Data)
	def get_UserQuestion(self): # String
		return self.get_query_params().get('UserQuestion')

	def set_UserQuestion(self, UserQuestion):  # String
		self.add_query_param('UserQuestion', UserQuestion)
	def get_UserPrompt(self): # String
		return self.get_query_params().get('UserPrompt')

	def set_UserPrompt(self, UserPrompt):  # String
		self.add_query_param('UserPrompt', UserPrompt)
	def get_ModelCode(self): # String
		return self.get_query_params().get('ModelCode')

	def set_ModelCode(self, ModelCode):  # String
		self.add_query_param('ModelCode', ModelCode)
