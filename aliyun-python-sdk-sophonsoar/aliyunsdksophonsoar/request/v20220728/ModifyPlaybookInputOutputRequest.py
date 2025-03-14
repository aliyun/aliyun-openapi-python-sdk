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

class ModifyPlaybookInputOutputRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'ModifyPlaybookInputOutput')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ParamType(self): # String
		return self.get_body_params().get('ParamType')

	def set_ParamType(self, ParamType):  # String
		self.add_body_params('ParamType', ParamType)
	def get_InputParams(self): # String
		return self.get_body_params().get('InputParams')

	def set_InputParams(self, InputParams):  # String
		self.add_body_params('InputParams', InputParams)
	def get_OutputParams(self): # String
		return self.get_body_params().get('OutputParams')

	def set_OutputParams(self, OutputParams):  # String
		self.add_body_params('OutputParams', OutputParams)
	def get_PlaybookUuid(self): # String
		return self.get_body_params().get('PlaybookUuid')

	def set_PlaybookUuid(self, PlaybookUuid):  # String
		self.add_body_params('PlaybookUuid', PlaybookUuid)
	def get_ExeConfig(self): # String
		return self.get_body_params().get('ExeConfig')

	def set_ExeConfig(self, ExeConfig):  # String
		self.add_body_params('ExeConfig', ExeConfig)
	def get_Lang(self): # String
		return self.get_body_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_body_params('Lang', Lang)
