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

class CreateTicketRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'CreateTicket','2.2.0')
		self.set_method('POST')

	def get_AccountType(self): # Integer
		return self.get_query_params().get('AccountType')

	def set_AccountType(self, AccountType):  # Integer
		self.add_query_param('AccountType', AccountType)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_AccountName(self): # String
		return self.get_query_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_query_param('AccountName', AccountName)
	def get_ExpireTime(self): # Integer
		return self.get_query_params().get('ExpireTime')

	def set_ExpireTime(self, ExpireTime):  # Integer
		self.add_query_param('ExpireTime', ExpireTime)
	def get_CmptId(self): # String
		return self.get_query_params().get('CmptId')

	def set_CmptId(self, CmptId):  # String
		self.add_query_param('CmptId', CmptId)
	def get_GlobalParam(self): # String
		return self.get_query_params().get('GlobalParam')

	def set_GlobalParam(self, GlobalParam):  # String
		self.add_query_param('GlobalParam', GlobalParam)
	def get_WorksId(self): # String
		return self.get_query_params().get('WorksId')

	def set_WorksId(self, WorksId):  # String
		self.add_query_param('WorksId', WorksId)
	def get_TicketNum(self): # Integer
		return self.get_query_params().get('TicketNum')

	def set_TicketNum(self, TicketNum):  # Integer
		self.add_query_param('TicketNum', TicketNum)
	def get_WatermarkParam(self): # String
		return self.get_query_params().get('WatermarkParam')

	def set_WatermarkParam(self, WatermarkParam):  # String
		self.add_query_param('WatermarkParam', WatermarkParam)
