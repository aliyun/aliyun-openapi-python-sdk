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
from aliyunsdksas.endpoint import endpoint_data

class CreateFileProtectRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'CreateFileProtectRule','sas')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FilePathss(self): # RepeatList
		return self.get_query_params().get('FilePaths')

	def set_FilePathss(self, FilePaths):  # RepeatList
		for depth1 in range(len(FilePaths)):
			self.add_query_param('FilePaths.' + str(depth1 + 1), FilePaths[depth1])
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_ProcPathss(self): # RepeatList
		return self.get_query_params().get('ProcPaths')

	def set_ProcPathss(self, ProcPaths):  # RepeatList
		for depth1 in range(len(ProcPaths)):
			self.add_query_param('ProcPaths.' + str(depth1 + 1), ProcPaths[depth1])
	def get_AlertLevel(self): # Integer
		return self.get_query_params().get('AlertLevel')

	def set_AlertLevel(self, AlertLevel):  # Integer
		self.add_query_param('AlertLevel', AlertLevel)
	def get_RuleAction(self): # String
		return self.get_query_params().get('RuleAction')

	def set_RuleAction(self, RuleAction):  # String
		self.add_query_param('RuleAction', RuleAction)
	def get_SwitchId(self): # String
		return self.get_query_params().get('SwitchId')

	def set_SwitchId(self, SwitchId):  # String
		self.add_query_param('SwitchId', SwitchId)
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
	def get_FileOpss(self): # RepeatList
		return self.get_query_params().get('FileOps')

	def set_FileOpss(self, FileOps):  # RepeatList
		for depth1 in range(len(FileOps)):
			self.add_query_param('FileOps.' + str(depth1 + 1), FileOps[depth1])
