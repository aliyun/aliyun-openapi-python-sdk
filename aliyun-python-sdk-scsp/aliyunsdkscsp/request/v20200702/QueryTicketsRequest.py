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
from aliyunsdkscsp.endpoint import endpoint_data

class QueryTicketsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'QueryTickets')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SrType(self): # Long
		return self.get_body_params().get('SrType')

	def set_SrType(self, SrType):  # Long
		self.add_body_params('SrType', SrType)
	def get_TouchId(self): # Long
		return self.get_body_params().get('TouchId')

	def set_TouchId(self, TouchId):  # Long
		self.add_body_params('TouchId', TouchId)
	def get_DealId(self): # Long
		return self.get_body_params().get('DealId')

	def set_DealId(self, DealId):  # Long
		self.add_body_params('DealId', DealId)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_TaskStatus(self): # Integer
		return self.get_body_params().get('TaskStatus')

	def set_TaskStatus(self, TaskStatus):  # Integer
		self.add_body_params('TaskStatus', TaskStatus)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_AccountName(self): # String
		return self.get_body_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_body_params('AccountName', AccountName)
	def get_CaseId(self): # Long
		return self.get_body_params().get('CaseId')

	def set_CaseId(self, CaseId):  # Long
		self.add_body_params('CaseId', CaseId)
	def get_Extra(self): # String
		return self.get_body_params().get('Extra')

	def set_Extra(self, Extra):  # String
		self.add_body_params('Extra', Extra)
	def get_ChannelType(self): # Integer
		return self.get_body_params().get('ChannelType')

	def set_ChannelType(self, ChannelType):  # Integer
		self.add_body_params('ChannelType', ChannelType)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_CaseType(self): # Integer
		return self.get_body_params().get('CaseType')

	def set_CaseType(self, CaseType):  # Integer
		self.add_body_params('CaseType', CaseType)
	def get_CaseStatus(self): # Integer
		return self.get_body_params().get('CaseStatus')

	def set_CaseStatus(self, CaseStatus):  # Integer
		self.add_body_params('CaseStatus', CaseStatus)
	def get_ChannelId(self): # String
		return self.get_body_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_body_params('ChannelId', ChannelId)
