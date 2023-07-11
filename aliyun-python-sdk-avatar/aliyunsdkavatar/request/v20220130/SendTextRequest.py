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

class SendTextRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'avatar', '2022-01-30', 'SendText')
		self.set_method('POST')

	def get_Feedback(self): # Boolean
		return self.get_query_params().get('Feedback')

	def set_Feedback(self, Feedback):  # Boolean
		self.add_query_param('Feedback', Feedback)
	def get_UniqueCode(self): # String
		return self.get_query_params().get('UniqueCode')

	def set_UniqueCode(self, UniqueCode):  # String
		self.add_query_param('UniqueCode', UniqueCode)
	def get_StreamExtension(self): # Struct
		return self.get_query_params().get('StreamExtension')

	def set_StreamExtension(self, StreamExtension):  # Struct
		self.add_query_param("StreamExtension", json.dumps(StreamExtension))
	def get_TenantId(self): # Long
		return self.get_query_params().get('TenantId')

	def set_TenantId(self, TenantId):  # Long
		self.add_query_param('TenantId', TenantId)
	def get_Interrupt(self): # Boolean
		return self.get_query_params().get('Interrupt')

	def set_Interrupt(self, Interrupt):  # Boolean
		self.add_query_param('Interrupt', Interrupt)
	def get_SessionId(self): # String
		return self.get_query_params().get('SessionId')

	def set_SessionId(self, SessionId):  # String
		self.add_query_param('SessionId', SessionId)
	def get_Text(self): # String
		return self.get_query_params().get('Text')

	def set_Text(self, Text):  # String
		self.add_query_param('Text', Text)
