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

class ModifyCopilotEmbedConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'ModifyCopilotEmbedConfig','2.2.0')
		self.set_method('POST')

	def get_CopilotId(self): # String
		return self.get_query_params().get('CopilotId')

	def set_CopilotId(self, CopilotId):  # String
		self.add_query_param('CopilotId', CopilotId)
	def get_DataRange(self): # String
		return self.get_query_params().get('DataRange')

	def set_DataRange(self, DataRange):  # String
		self.add_query_param('DataRange', DataRange)
	def get_ModuleName(self): # String
		return self.get_query_params().get('ModuleName')

	def set_ModuleName(self, ModuleName):  # String
		self.add_query_param('ModuleName', ModuleName)
	def get_AgentName(self): # String
		return self.get_query_params().get('AgentName')

	def set_AgentName(self, AgentName):  # String
		self.add_query_param('AgentName', AgentName)
