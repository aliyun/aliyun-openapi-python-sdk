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

class ChatMessageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AIMath', '2024-11-14', 'ChatMessage')
		self.set_method('POST')

	def get_ConversationId(self): # String
		return self.get_body_params().get('ConversationId')

	def set_ConversationId(self, ConversationId):  # String
		self.add_body_params('ConversationId', ConversationId)
	def get_UserId(self): # String
		return self.get_body_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_body_params('UserId', UserId)
	def get_Content(self): # String
		return self.get_body_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_body_params('Content', Content)
