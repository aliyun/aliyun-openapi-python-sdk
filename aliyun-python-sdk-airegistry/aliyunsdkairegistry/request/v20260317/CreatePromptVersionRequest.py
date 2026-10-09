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

class CreatePromptVersionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AIRegistry', '2026-03-17', 'CreatePromptVersion','AIRegistry')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PromptKey(self): # String
		return self.get_query_params().get('PromptKey')

	def set_PromptKey(self, PromptKey):  # String
		self.add_query_param('PromptKey', PromptKey)
	def get_NamespaceId(self): # String
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self, NamespaceId):  # String
		self.add_query_param('NamespaceId', NamespaceId)
	def get_TargetVersion(self): # String
		return self.get_query_params().get('TargetVersion')

	def set_TargetVersion(self, TargetVersion):  # String
		self.add_query_param('TargetVersion', TargetVersion)
	def get_Template(self): # String
		return self.get_query_params().get('Template')

	def set_Template(self, Template):  # String
		self.add_query_param('Template', Template)
	def get_BasedOnVersion(self): # String
		return self.get_query_params().get('BasedOnVersion')

	def set_BasedOnVersion(self, BasedOnVersion):  # String
		self.add_query_param('BasedOnVersion', BasedOnVersion)
	def get_Variables(self): # String
		return self.get_query_params().get('Variables')

	def set_Variables(self, Variables):  # String
		self.add_query_param('Variables', Variables)
	def get_CommitMsg(self): # String
		return self.get_query_params().get('CommitMsg')

	def set_CommitMsg(self, CommitMsg):  # String
		self.add_query_param('CommitMsg', CommitMsg)
