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

class CallbackTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mseap', '2021-01-18', 'CallbackTask')
		self.set_method('POST')

	def get_UserCallerParentId(self): # Long
		return self.get_query_params().get('UserCallerParentId')

	def set_UserCallerParentId(self, UserCallerParentId):  # Long
		self.add_query_param('UserCallerParentId', UserCallerParentId)
	def get_OutTaskId(self): # String
		return self.get_query_params().get('OutTaskId')

	def set_OutTaskId(self, OutTaskId):  # String
		self.add_query_param('OutTaskId', OutTaskId)
	def get_ApiType(self): # String
		return self.get_query_params().get('ApiType')

	def set_ApiType(self, ApiType):  # String
		self.add_query_param('ApiType', ApiType)
	def get_UserMfaPresent(self): # Boolean
		return self.get_query_params().get('UserMfaPresent')

	def set_UserMfaPresent(self, UserMfaPresent):  # Boolean
		self.add_query_param('UserMfaPresent', UserMfaPresent)
	def get_UserKp(self): # String
		return self.get_query_params().get('UserKp')

	def set_UserKp(self, UserKp):  # String
		self.add_query_param('UserKp', UserKp)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_UserCallerType(self): # String
		return self.get_query_params().get('UserCallerType')

	def set_UserCallerType(self, UserCallerType):  # String
		self.add_query_param('UserCallerType', UserCallerType)
	def get_TaskType(self): # String
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # String
		self.add_query_param('TaskType', TaskType)
	def get_UserSecurityToken(self): # String
		return self.get_query_params().get('UserSecurityToken')

	def set_UserSecurityToken(self, UserSecurityToken):  # String
		self.add_query_param('UserSecurityToken', UserSecurityToken)
	def get_UserAccessKeyId(self): # String
		return self.get_query_params().get('UserAccessKeyId')

	def set_UserAccessKeyId(self, UserAccessKeyId):  # String
		self.add_query_param('UserAccessKeyId', UserAccessKeyId)
	def get_OrderId(self): # String
		return self.get_query_params().get('OrderId')

	def set_OrderId(self, OrderId):  # String
		self.add_query_param('OrderId', OrderId)
	def get_AliyunKp(self): # String
		return self.get_query_params().get('AliyunKp')

	def set_AliyunKp(self, AliyunKp):  # String
		self.add_query_param('AliyunKp', AliyunKp)
	def get_UserBid(self): # String
		return self.get_query_params().get('UserBid')

	def set_UserBid(self, UserBid):  # String
		self.add_query_param('UserBid', UserBid)
	def get_OriginalRequest(self): # String
		return self.get_query_params().get('OriginalRequest')

	def set_OriginalRequest(self, OriginalRequest):  # String
		self.add_query_param('OriginalRequest', OriginalRequest)
	def get_PrincipalKey(self): # String
		return self.get_query_params().get('PrincipalKey')

	def set_PrincipalKey(self, PrincipalKey):  # String
		self.add_query_param('PrincipalKey', PrincipalKey)
	def get_UserCallerSecurityTransport(self): # Boolean
		return self.get_query_params().get('UserCallerSecurityTransport')

	def set_UserCallerSecurityTransport(self, UserCallerSecurityTransport):  # Boolean
		self.add_query_param('UserCallerSecurityTransport', UserCallerSecurityTransport)
	def get_BizCode(self): # String
		return self.get_query_params().get('BizCode')

	def set_BizCode(self, BizCode):  # String
		self.add_query_param('BizCode', BizCode)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
	def get_TaskData(self): # String
		return self.get_query_params().get('TaskData')

	def set_TaskData(self, TaskData):  # String
		self.add_query_param('TaskData', TaskData)
	def get_Bid(self): # String
		return self.get_query_params().get('Bid')

	def set_Bid(self, Bid):  # String
		self.add_query_param('Bid', Bid)
