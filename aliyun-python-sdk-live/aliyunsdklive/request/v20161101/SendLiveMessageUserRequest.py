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
from aliyunsdklive.endpoint import endpoint_data

class SendLiveMessageUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'SendLiveMessageUser','live')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DataCenter(self): # String
		return self.get_query_params().get('DataCenter')

	def set_DataCenter(self, DataCenter):  # String
		self.add_query_param('DataCenter', DataCenter)
	def get_MsgTid(self): # String
		return self.get_query_params().get('MsgTid')

	def set_MsgTid(self, MsgTid):  # String
		self.add_query_param('MsgTid', MsgTid)
	def get_Body(self): # String
		return self.get_query_params().get('Body')

	def set_Body(self, Body):  # String
		self.add_query_param('Body', Body)
	def get_SenderId(self): # String
		return self.get_query_params().get('SenderId')

	def set_SenderId(self, SenderId):  # String
		self.add_query_param('SenderId', SenderId)
	def get_ReceiverId(self): # String
		return self.get_query_params().get('ReceiverId')

	def set_ReceiverId(self, ReceiverId):  # String
		self.add_query_param('ReceiverId', ReceiverId)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_SenderInfo(self): # String
		return self.get_query_params().get('SenderInfo')

	def set_SenderInfo(self, SenderInfo):  # String
		self.add_query_param('SenderInfo', SenderInfo)
	def get_MsgType(self): # Long
		return self.get_query_params().get('MsgType')

	def set_MsgType(self, MsgType):  # Long
		self.add_query_param('MsgType', MsgType)
