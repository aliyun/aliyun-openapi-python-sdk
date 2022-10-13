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

class DuplexDecisionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'avatar', '2022-01-30', 'DuplexDecision')
		self.set_method('POST')

	def get_InterruptType(self): # Integer
		return self.get_query_params().get('InterruptType')

	def set_InterruptType(self, InterruptType):  # Integer
		self.add_query_param('InterruptType', InterruptType)
	def get_CustomKeywords(self): # Array
		return self.get_query_params().get('CustomKeywords')

	def set_CustomKeywords(self, CustomKeywords):  # Array
		self.add_query_param("CustomKeywords", json.dumps(CustomKeywords))
	def get_SessionId(self): # String
		return self.get_query_params().get('SessionId')

	def set_SessionId(self, SessionId):  # String
		self.add_query_param('SessionId', SessionId)
	def get_DialogStatus(self): # String
		return self.get_query_params().get('DialogStatus')

	def set_DialogStatus(self, DialogStatus):  # String
		self.add_query_param('DialogStatus', DialogStatus)
	def get_DialogContext(self): # Struct
		return self.get_query_params().get('DialogContext')

	def set_DialogContext(self, DialogContext):  # Struct
		self.add_query_param("DialogContext", json.dumps(DialogContext))
	def get_CallTime(self): # Integer
		return self.get_query_params().get('CallTime')

	def set_CallTime(self, CallTime):  # Integer
		self.add_query_param('CallTime', CallTime)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_TenantId(self): # Long
		return self.get_query_params().get('TenantId')

	def set_TenantId(self, TenantId):  # Long
		self.add_query_param('TenantId', TenantId)
	def get_Text(self): # String
		return self.get_query_params().get('Text')

	def set_Text(self, Text):  # String
		self.add_query_param('Text', Text)
	def get_BizRequestId(self): # String
		return self.get_query_params().get('BizRequestId')

	def set_BizRequestId(self, BizRequestId):  # String
		self.add_query_param('BizRequestId', BizRequestId)
