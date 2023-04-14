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
from aliyunsdkcams.endpoint import endpoint_data
import json

class BeeBotChatRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cams', '2020-06-06', 'BeeBotChat')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SessionId(self): # String
		return self.get_body_params().get('SessionId')

	def set_SessionId(self, SessionId):  # String
		self.add_body_params('SessionId', SessionId)
	def get_IntentName(self): # String
		return self.get_body_params().get('IntentName')

	def set_IntentName(self, IntentName):  # String
		self.add_body_params('IntentName', IntentName)
	def get_SenderNick(self): # String
		return self.get_body_params().get('SenderNick')

	def set_SenderNick(self, SenderNick):  # String
		self.add_body_params('SenderNick', SenderNick)
	def get_Perspective(self): # Array
		return self.get_body_params().get('Perspective')

	def set_Perspective(self, Perspective):  # Array
		self.add_body_params("Perspective", json.dumps(Perspective))
	def get_Utterance(self): # String
		return self.get_body_params().get('Utterance')

	def set_Utterance(self, Utterance):  # String
		self.add_body_params('Utterance', Utterance)
	def get_IsvCode(self): # String
		return self.get_body_params().get('IsvCode')

	def set_IsvCode(self, IsvCode):  # String
		self.add_body_params('IsvCode', IsvCode)
	def get_KnowledgeId(self): # String
		return self.get_body_params().get('KnowledgeId')

	def set_KnowledgeId(self, KnowledgeId):  # String
		self.add_body_params('KnowledgeId', KnowledgeId)
	def get_VendorParam(self): # Map
		return self.get_body_params().get('VendorParam')

	def set_VendorParam(self, VendorParam):  # Map
		self.add_body_params("VendorParam", json.dumps(VendorParam))
	def get_SenderId(self): # String
		return self.get_body_params().get('SenderId')

	def set_SenderId(self, SenderId):  # String
		self.add_body_params('SenderId', SenderId)
	def get_ChatBotInstanceId(self): # String
		return self.get_body_params().get('ChatBotInstanceId')

	def set_ChatBotInstanceId(self, ChatBotInstanceId):  # String
		self.add_body_params('ChatBotInstanceId', ChatBotInstanceId)
	def get_CustSpaceId(self): # String
		return self.get_body_params().get('CustSpaceId')

	def set_CustSpaceId(self, CustSpaceId):  # String
		self.add_body_params('CustSpaceId', CustSpaceId)
