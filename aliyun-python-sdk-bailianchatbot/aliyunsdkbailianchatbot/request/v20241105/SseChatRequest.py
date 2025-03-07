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

class SseChatRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BailianChatBot', '2024-11-05', 'SseChat')
		self.set_method('POST')

	def get_SessionId(self): # String
		return self.get_query_params().get('SessionId')

	def set_SessionId(self, SessionId):  # String
		self.add_query_param('SessionId', SessionId)
	def get_Command(self): # String
		return self.get_query_params().get('Command')

	def set_Command(self, Command):  # String
		self.add_query_param('Command', Command)
	def get_VendorParam(self): # String
		return self.get_query_params().get('VendorParam')

	def set_VendorParam(self, VendorParam):  # String
		self.add_query_param('VendorParam', VendorParam)
	def get_SenderId(self): # String
		return self.get_query_params().get('SenderId')

	def set_SenderId(self, SenderId):  # String
		self.add_query_param('SenderId', SenderId)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_SenderNick(self): # String
		return self.get_query_params().get('SenderNick')

	def set_SenderNick(self, SenderNick):  # String
		self.add_query_param('SenderNick', SenderNick)
	def get_Utterance(self): # String
		return self.get_query_params().get('Utterance')

	def set_Utterance(self, Utterance):  # String
		self.add_query_param('Utterance', Utterance)
	def get_WorkspaceId(self): # String
		return self.get_query_params().get('WorkspaceId')

	def set_WorkspaceId(self, WorkspaceId):  # String
		self.add_query_param('WorkspaceId', WorkspaceId)
