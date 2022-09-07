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

class UpdateCallRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SmartSales', '2022-08-18', 'UpdateCall')
		self.set_method('POST')

	def get_CallId(self): # Long
		return self.get_query_params().get('CallId')

	def set_CallId(self, CallId):  # Long
		self.add_query_param('CallId', CallId)
	def get_ClueStatusRemark(self): # String
		return self.get_query_params().get('ClueStatusRemark')

	def set_ClueStatusRemark(self, ClueStatusRemark):  # String
		self.add_query_param('ClueStatusRemark', ClueStatusRemark)
	def get_AgentKey(self): # String
		return self.get_query_params().get('AgentKey')

	def set_AgentKey(self, AgentKey):  # String
		self.add_query_param('AgentKey', AgentKey)
	def get_BusinessResult(self): # Integer
		return self.get_query_params().get('BusinessResult')

	def set_BusinessResult(self, BusinessResult):  # Integer
		self.add_query_param('BusinessResult', BusinessResult)
	def get_CustomCallId(self): # String
		return self.get_query_params().get('CustomCallId')

	def set_CustomCallId(self, CustomCallId):  # String
		self.add_query_param('CustomCallId', CustomCallId)
