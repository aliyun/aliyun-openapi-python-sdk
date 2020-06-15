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

class SendVerifyCodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Risk', '2015-03-23', 'SendVerifyCode')
		self.set_method('POST')

	def get_IdType(self):
		return self.get_query_params().get('IdType')

	def set_IdType(self,IdType):
		self.add_query_param('IdType',IdType)

	def get_EventId(self):
		return self.get_query_params().get('EventId')

	def set_EventId(self,EventId):
		self.add_query_param('EventId',EventId)

	def get_TimeInterval(self):
		return self.get_query_params().get('TimeInterval')

	def set_TimeInterval(self,TimeInterval):
		self.add_query_param('TimeInterval',TimeInterval)

	def get_CodeType(self):
		return self.get_query_params().get('CodeType')

	def set_CodeType(self,CodeType):
		self.add_query_param('CodeType',CodeType)

	def get_RequestId(self):
		return self.get_query_params().get('RequestId')

	def set_RequestId(self,RequestId):
		self.add_query_param('RequestId',RequestId)

	def get_ChannelType(self):
		return self.get_query_params().get('ChannelType')

	def set_ChannelType(self,ChannelType):
		self.add_query_param('ChannelType',ChannelType)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_MessageReiver(self):
		return self.get_query_params().get('MessageReiver')

	def set_MessageReiver(self,MessageReiver):
		self.add_query_param('MessageReiver',MessageReiver)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_MteeCode(self):
		return self.get_query_params().get('MteeCode')

	def set_MteeCode(self,MteeCode):
		self.add_query_param('MteeCode',MteeCode)