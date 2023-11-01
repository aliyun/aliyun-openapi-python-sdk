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

class ListCloudSiemPredefinedRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'ListCloudSiemPredefinedRules','cloud-siem')
		self.set_method('POST')

	def get_RuleName(self): # String
		return self.get_body_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_body_params('RuleName', RuleName)
	def get_StartTime(self): # Long
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_body_params('StartTime', StartTime)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_Id(self): # String
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_body_params('Id', Id)
	def get_RuleType(self): # String
		return self.get_body_params().get('RuleType')

	def set_RuleType(self, RuleType):  # String
		self.add_body_params('RuleType', RuleType)
	def get_EndTime(self): # Long
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_body_params('EndTime', EndTime)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_AlertType(self): # String
		return self.get_body_params().get('AlertType')

	def set_AlertType(self, AlertType):  # String
		self.add_body_params('AlertType', AlertType)
	def get_ThreatLevels(self): # RepeatList
		return self.get_body_params().get('ThreatLevel')

	def set_ThreatLevels(self, ThreatLevel):  # RepeatList
		for depth1 in range(len(ThreatLevel)):
			self.add_body_params('ThreatLevel.' + str(depth1 + 1), ThreatLevel[depth1])
	def get_Status(self): # Integer
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_body_params('Status', Status)
