# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ChatRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Chatbot', '2017-10-11', 'Chat','beebot')

	def get_KnowledgeId(self):
		return self.get_query_params().get('KnowledgeId')

	def set_KnowledgeId(self,KnowledgeId):
		self.add_query_param('KnowledgeId',KnowledgeId)

	def get_SenderId(self):
		return self.get_query_params().get('SenderId')

	def set_SenderId(self,SenderId):
		self.add_query_param('SenderId',SenderId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_SenderNick(self):
		return self.get_query_params().get('SenderNick')

	def set_SenderNick(self,SenderNick):
		self.add_query_param('SenderNick',SenderNick)

	def get_Perspectives(self):
		return self.get_query_params().get('Perspectives')

	def set_Perspectives(self,Perspectives):
		for i in range(len(Perspectives)):	
			if Perspectives[i] is not None:
				self.add_query_param('Perspective.' + str(i + 1) , Perspectives[i]);

	def get_SessionId(self):
		return self.get_query_params().get('SessionId')

	def set_SessionId(self,SessionId):
		self.add_query_param('SessionId',SessionId)

	def get_Tag(self):
		return self.get_query_params().get('Tag')

	def set_Tag(self,Tag):
		self.add_query_param('Tag',Tag)

	def get_Utterance(self):
		return self.get_query_params().get('Utterance')

	def set_Utterance(self,Utterance):
		self.add_query_param('Utterance',Utterance)