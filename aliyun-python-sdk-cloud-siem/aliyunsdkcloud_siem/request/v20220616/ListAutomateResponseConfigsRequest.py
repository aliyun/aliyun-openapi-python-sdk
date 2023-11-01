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

class ListAutomateResponseConfigsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'ListAutomateResponseConfigs','cloud-siem')
		self.set_method('POST')

	def get_ActionType(self): # String
		return self.get_body_params().get('ActionType')

	def set_ActionType(self, ActionType):  # String
		self.add_body_params('ActionType', ActionType)
	def get_RuleName(self): # String
		return self.get_body_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_body_params('RuleName', RuleName)
	def get_SubUserId(self): # Long
		return self.get_body_params().get('SubUserId')

	def set_SubUserId(self, SubUserId):  # Long
		self.add_body_params('SubUserId', SubUserId)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_AutoResponseType(self): # String
		return self.get_body_params().get('AutoResponseType')

	def set_AutoResponseType(self, AutoResponseType):  # String
		self.add_body_params('AutoResponseType', AutoResponseType)
	def get_Id(self): # Long
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_body_params('Id', Id)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_PlaybookUuid(self): # String
		return self.get_body_params().get('PlaybookUuid')

	def set_PlaybookUuid(self, PlaybookUuid):  # String
		self.add_body_params('PlaybookUuid', PlaybookUuid)
	def get_Status(self): # Integer
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_body_params('Status', Status)
