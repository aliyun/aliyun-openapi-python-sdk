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
from aliyunsdksas.endpoint import endpoint_data

class ListCheckResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ListCheckResult')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StandardIdss(self): # RepeatList
		return self.get_query_params().get('StandardIds')

	def set_StandardIdss(self, StandardIds):  # RepeatList
		for depth1 in range(len(StandardIds)):
			self.add_query_param('StandardIds.' + str(depth1 + 1), StandardIds[depth1])
	def get_RiskLevelss(self): # RepeatList
		return self.get_query_params().get('RiskLevels')

	def set_RiskLevelss(self, RiskLevels):  # RepeatList
		for depth1 in range(len(RiskLevels)):
			self.add_query_param('RiskLevels.' + str(depth1 + 1), RiskLevels[depth1])
	def get_InstanceTypess(self): # RepeatList
		return self.get_query_params().get('InstanceTypes')

	def set_InstanceTypess(self, InstanceTypes):  # RepeatList
		for depth1 in range(len(InstanceTypes)):
			self.add_query_param('InstanceTypes.' + str(depth1 + 1), InstanceTypes[depth1])
	def get_CheckKey(self): # String
		return self.get_query_params().get('CheckKey')

	def set_CheckKey(self, CheckKey):  # String
		self.add_query_param('CheckKey', CheckKey)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Vendorss(self): # RepeatList
		return self.get_query_params().get('Vendors')

	def set_Vendorss(self, Vendors):  # RepeatList
		for depth1 in range(len(Vendors)):
			self.add_query_param('Vendors.' + str(depth1 + 1), Vendors[depth1])
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_RequirementIdss(self): # RepeatList
		return self.get_query_params().get('RequirementIds')

	def set_RequirementIdss(self, RequirementIds):  # RepeatList
		for depth1 in range(len(RequirementIds)):
			self.add_query_param('RequirementIds.' + str(depth1 + 1), RequirementIds[depth1])
	def get_SortTypess(self): # RepeatList
		return self.get_query_params().get('SortTypes')

	def set_SortTypess(self, SortTypes):  # RepeatList
		for depth1 in range(len(SortTypes)):
			self.add_query_param('SortTypes.' + str(depth1 + 1), SortTypes[depth1])
	def get_InstanceIdss(self): # RepeatList
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIdss(self, InstanceIds):  # RepeatList
		for depth1 in range(len(InstanceIds)):
			self.add_query_param('InstanceIds.' + str(depth1 + 1), InstanceIds[depth1])
	def get_Statusess(self): # RepeatList
		return self.get_query_params().get('Statuses')

	def set_Statusess(self, Statuses):  # RepeatList
		for depth1 in range(len(Statuses)):
			self.add_query_param('Statuses.' + str(depth1 + 1), Statuses[depth1])
