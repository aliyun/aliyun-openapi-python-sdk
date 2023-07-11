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

class SendCommandRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'avatar', '2022-01-30', 'SendCommand')
		self.set_method('POST')

	def get_Feedback(self): # Boolean
		return self.get_query_params().get('Feedback')

	def set_Feedback(self, Feedback):  # Boolean
		self.add_query_param('Feedback', Feedback)
	def get_Code(self): # String
		return self.get_query_params().get('Code')

	def set_Code(self, Code):  # String
		self.add_query_param('Code', Code)
	def get_UniqueCode(self): # String
		return self.get_query_params().get('UniqueCode')

	def set_UniqueCode(self, UniqueCode):  # String
		self.add_query_param('UniqueCode', UniqueCode)
	def get_TenantId(self): # Long
		return self.get_query_params().get('TenantId')

	def set_TenantId(self, TenantId):  # Long
		self.add_query_param('TenantId', TenantId)
	def get_SessionId(self): # String
		return self.get_query_params().get('SessionId')

	def set_SessionId(self, SessionId):  # String
		self.add_query_param('SessionId', SessionId)
	def get_Content(self): # Map
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # Map
		self.add_query_param("Content", json.dumps(Content))
