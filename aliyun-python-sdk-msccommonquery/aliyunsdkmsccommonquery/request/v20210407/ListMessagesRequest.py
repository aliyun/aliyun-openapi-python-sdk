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

class ListMessagesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'MscCommonQuery', '2021-04-07', 'ListMessages')
		self.set_method('POST')

	def get_StartTimestamp(self): # Long
		return self.get_body_params().get('StartTimestamp')

	def set_StartTimestamp(self, StartTimestamp):  # Long
		self.add_body_params('StartTimestamp', StartTimestamp)
	def get_Locale(self): # String
		return self.get_query_params().get('Locale')

	def set_Locale(self, Locale):  # String
		self.add_query_param('Locale', Locale)
	def get_EndTimestamp(self): # Long
		return self.get_body_params().get('EndTimestamp')

	def set_EndTimestamp(self, EndTimestamp):  # Long
		self.add_body_params('EndTimestamp', EndTimestamp)
	def get_PageNo(self): # Integer
		return self.get_body_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_body_params('PageNo', PageNo)
	def get_ChannelType(self): # String
		return self.get_body_params().get('ChannelType')

	def set_ChannelType(self, ChannelType):  # String
		self.add_body_params('ChannelType', ChannelType)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
