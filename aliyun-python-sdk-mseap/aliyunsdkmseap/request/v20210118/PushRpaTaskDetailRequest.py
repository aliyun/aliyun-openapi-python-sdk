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

class PushRpaTaskDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mseap', '2021-01-18', 'PushRpaTaskDetail')
		self.set_method('POST')

	def get_UserCallerParentId(self): # Long
		return self.get_query_params().get('UserCallerParentId')

	def set_UserCallerParentId(self, UserCallerParentId):  # Long
		self.add_query_param('UserCallerParentId', UserCallerParentId)
	def get_ApiType(self): # String
		return self.get_query_params().get('ApiType')

	def set_ApiType(self, ApiType):  # String
		self.add_query_param('ApiType', ApiType)
	def get_ModelDetailId(self): # Long
		return self.get_query_params().get('ModelDetailId')

	def set_ModelDetailId(self, ModelDetailId):  # Long
		self.add_query_param('ModelDetailId', ModelDetailId)
	def get_UserKp(self): # String
		return self.get_query_params().get('UserKp')

	def set_UserKp(self, UserKp):  # String
		self.add_query_param('UserKp', UserKp)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_TaskId(self): # Long
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # Long
		self.add_query_param('TaskId', TaskId)
	def get_UserCallerType(self): # String
		return self.get_query_params().get('UserCallerType')

	def set_UserCallerType(self, UserCallerType):  # String
		self.add_query_param('UserCallerType', UserCallerType)
	def get_UserSecurityToken(self): # String
		return self.get_query_params().get('UserSecurityToken')

	def set_UserSecurityToken(self, UserSecurityToken):  # String
		self.add_query_param('UserSecurityToken', UserSecurityToken)
	def get_UserAccessKeyId(self): # String
		return self.get_query_params().get('UserAccessKeyId')

	def set_UserAccessKeyId(self, UserAccessKeyId):  # String
		self.add_query_param('UserAccessKeyId', UserAccessKeyId)
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
	def get_InputScreenshot(self): # String
		return self.get_query_params().get('InputScreenshot')

	def set_InputScreenshot(self, InputScreenshot):  # String
		self.add_query_param('InputScreenshot', InputScreenshot)
	def get_InputData(self): # String
		return self.get_query_params().get('InputData')

	def set_InputData(self, InputData):  # String
		self.add_query_param('InputData', InputData)
	def get_OutputData(self): # String
		return self.get_query_params().get('OutputData')

	def set_OutputData(self, OutputData):  # String
		self.add_query_param('OutputData', OutputData)
	def get_InputHtml(self): # String
		return self.get_query_params().get('InputHtml')

	def set_InputHtml(self, InputHtml):  # String
		self.add_query_param('InputHtml', InputHtml)
	def get_TaskDetailId(self): # Long
		return self.get_query_params().get('TaskDetailId')

	def set_TaskDetailId(self, TaskDetailId):  # Long
		self.add_query_param('TaskDetailId', TaskDetailId)
	def get_OutputHtml(self): # String
		return self.get_query_params().get('OutputHtml')

	def set_OutputHtml(self, OutputHtml):  # String
		self.add_query_param('OutputHtml', OutputHtml)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
	def get_Bid(self): # String
		return self.get_query_params().get('Bid')

	def set_Bid(self, Bid):  # String
		self.add_query_param('Bid', Bid)
	def get_OutputScreenshot(self): # String
		return self.get_query_params().get('OutputScreenshot')

	def set_OutputScreenshot(self, OutputScreenshot):  # String
		self.add_query_param('OutputScreenshot', OutputScreenshot)
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
