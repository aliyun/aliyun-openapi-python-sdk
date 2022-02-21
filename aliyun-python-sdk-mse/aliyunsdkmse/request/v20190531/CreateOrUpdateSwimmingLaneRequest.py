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
from aliyunsdkmse.endpoint import endpoint_data

class CreateOrUpdateSwimmingLaneRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'CreateOrUpdateSwimmingLane')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_GmtModified(self): # String
		return self.get_query_params().get('GmtModified')

	def set_GmtModified(self, GmtModified):  # String
		self.add_query_param('GmtModified', GmtModified)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_LicenseKey(self): # String
		return self.get_query_params().get('LicenseKey')

	def set_LicenseKey(self, LicenseKey):  # String
		self.add_query_param('LicenseKey', LicenseKey)
	def get_EntryRule(self): # String
		return self.get_query_params().get('EntryRule')

	def set_EntryRule(self, EntryRule):  # String
		self.add_query_param('EntryRule', EntryRule)
	def get_Enable(self): # Boolean
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # Boolean
		self.add_query_param('Enable', Enable)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_Tag(self): # String
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # String
		self.add_query_param('Tag', Tag)
	def get_EntryRuless(self): # RepeatList
		return self.get_query_params().get('EntryRules')

	def set_EntryRuless(self, EntryRules):  # RepeatList
		for depth1 in range(len(EntryRules)):
			if EntryRules[depth1].get('RestItems') is not None:
				for depth2 in range(len(EntryRules[depth1].get('RestItems'))):
					if EntryRules[depth1].get('RestItems')[depth2].get('Datum') is not None:
						self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Datum', EntryRules[depth1].get('RestItems')[depth2].get('Datum'))
					if EntryRules[depth1].get('RestItems')[depth2].get('Divisor') is not None:
						self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Divisor', EntryRules[depth1].get('RestItems')[depth2].get('Divisor'))
					if EntryRules[depth1].get('RestItems')[depth2].get('Rate') is not None:
						self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Rate', EntryRules[depth1].get('RestItems')[depth2].get('Rate'))
					if EntryRules[depth1].get('RestItems')[depth2].get('NameList') is not None:
						for depth3 in range(len(EntryRules[depth1].get('RestItems')[depth2].get('NameList'))):
							self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.NameList' + str(depth3 + 1), EntryRules[depth1].get('RestItems')[depth2].get('NameList')[depth3])
					if EntryRules[depth1].get('RestItems')[depth2].get('Name') is not None:
						self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Name', EntryRules[depth1].get('RestItems')[depth2].get('Name'))
					if EntryRules[depth1].get('RestItems')[depth2].get('Type') is not None:
						self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Type', EntryRules[depth1].get('RestItems')[depth2].get('Type'))
					if EntryRules[depth1].get('RestItems')[depth2].get('Cond') is not None:
						self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Cond', EntryRules[depth1].get('RestItems')[depth2].get('Cond'))
					if EntryRules[depth1].get('RestItems')[depth2].get('Remainder') is not None:
						self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Remainder', EntryRules[depth1].get('RestItems')[depth2].get('Remainder'))
					if EntryRules[depth1].get('RestItems')[depth2].get('Value') is not None:
						self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Value', EntryRules[depth1].get('RestItems')[depth2].get('Value'))
					if EntryRules[depth1].get('RestItems')[depth2].get('Operator') is not None:
						self.add_query_param('EntryRules.' + str(depth1 + 1) + str(depth2 + 1) + '.Operator', EntryRules[depth1].get('RestItems')[depth2].get('Operator'))
			if EntryRules[depth1].get('Path') is not None:
				self.add_query_param('EntryRules.' + str(depth1 + 1) + '.Path', EntryRules[depth1].get('Path'))
			if EntryRules[depth1].get('Condition') is not None:
				self.add_query_param('EntryRules.' + str(depth1 + 1) + '.Condition', EntryRules[depth1].get('Condition'))
			if EntryRules[depth1].get('Enable') is not None:
				self.add_query_param('EntryRules.' + str(depth1 + 1) + '.Enable', EntryRules[depth1].get('Enable'))
			if EntryRules[depth1].get('Priority') is not None:
				self.add_query_param('EntryRules.' + str(depth1 + 1) + '.Priority', EntryRules[depth1].get('Priority'))
	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_GmtCreate(self): # String
		return self.get_query_params().get('GmtCreate')

	def set_GmtCreate(self, GmtCreate):  # String
		self.add_query_param('GmtCreate', GmtCreate)
	def get_EnableRules(self): # Boolean
		return self.get_query_params().get('EnableRules')

	def set_EnableRules(self, EnableRules):  # Boolean
		self.add_query_param('EnableRules', EnableRules)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
