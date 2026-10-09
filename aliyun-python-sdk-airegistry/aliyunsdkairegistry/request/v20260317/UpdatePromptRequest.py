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
import json

class UpdatePromptRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AIRegistry', '2026-03-17', 'UpdatePrompt','AIRegistry')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PromptKey(self): # String
		return self.get_query_params().get('PromptKey')

	def set_PromptKey(self, PromptKey):  # String
		self.add_query_param('PromptKey', PromptKey)
	def get_BizTags(self): # Array
		return self.get_query_params().get('BizTags')

	def set_BizTags(self, BizTags):  # Array
		self.add_query_param("BizTags", json.dumps(BizTags))
	def get_NamespaceId(self): # String
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self, NamespaceId):  # String
		self.add_query_param('NamespaceId', NamespaceId)
	def get_Labels(self): # Map
		return self.get_query_params().get('Labels')

	def set_Labels(self, Labels):  # Map
		self.add_query_param("Labels", json.dumps(Labels))
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
