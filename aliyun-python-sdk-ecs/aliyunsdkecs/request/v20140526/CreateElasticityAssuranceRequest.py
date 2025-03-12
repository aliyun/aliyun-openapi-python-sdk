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
from aliyunsdkecs.endpoint import endpoint_data

class CreateElasticityAssuranceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateElasticityAssurance','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_PrivatePoolOptionsMatchCriteria(self): # String
		return self.get_query_params().get('PrivatePoolOptions.MatchCriteria')

	def set_PrivatePoolOptionsMatchCriteria(self, PrivatePoolOptionsMatchCriteria):  # String
		self.add_query_param('PrivatePoolOptions.MatchCriteria', PrivatePoolOptionsMatchCriteria)
	def get_InstanceTypes(self): # RepeatList
		return self.get_query_params().get('InstanceType')

	def set_InstanceTypes(self, InstanceType):  # RepeatList
		for depth1 in range(len(InstanceType)):
			self.add_query_param('InstanceType.' + str(depth1 + 1), InstanceType[depth1])
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
	def get_AutoRenewPeriod(self): # Integer
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self, AutoRenewPeriod):  # Integer
		self.add_query_param('AutoRenewPeriod', AutoRenewPeriod)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_PrivatePoolOptionsName(self): # String
		return self.get_query_params().get('PrivatePoolOptions.Name')

	def set_PrivatePoolOptionsName(self, PrivatePoolOptionsName):  # String
		self.add_query_param('PrivatePoolOptions.Name', PrivatePoolOptionsName)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_AssuranceTimes(self): # String
		return self.get_query_params().get('AssuranceTimes')

	def set_AssuranceTimes(self, AssuranceTimes):  # String
		self.add_query_param('AssuranceTimes', AssuranceTimes)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_InstanceCpuCoreCount(self): # Integer
		return self.get_query_params().get('InstanceCpuCoreCount')

	def set_InstanceCpuCoreCount(self, InstanceCpuCoreCount):  # Integer
		self.add_query_param('InstanceCpuCoreCount', InstanceCpuCoreCount)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_ZoneIds(self): # RepeatList
		return self.get_query_params().get('ZoneId')

	def set_ZoneIds(self, ZoneId):  # RepeatList
		for depth1 in range(len(ZoneId)):
			self.add_query_param('ZoneId.' + str(depth1 + 1), ZoneId[depth1])
	def get_RecurrenceRuless(self): # RepeatList
		return self.get_query_params().get('RecurrenceRules')

	def set_RecurrenceRuless(self, RecurrenceRules):  # RepeatList
		for depth1 in range(len(RecurrenceRules)):
			if RecurrenceRules[depth1].get('RecurrenceType') is not None:
				self.add_query_param('RecurrenceRules.' + str(depth1 + 1) + '.RecurrenceType', RecurrenceRules[depth1].get('RecurrenceType'))
			if RecurrenceRules[depth1].get('RecurrenceValue') is not None:
				self.add_query_param('RecurrenceRules.' + str(depth1 + 1) + '.RecurrenceValue', RecurrenceRules[depth1].get('RecurrenceValue'))
			if RecurrenceRules[depth1].get('StartHour') is not None:
				self.add_query_param('RecurrenceRules.' + str(depth1 + 1) + '.StartHour', RecurrenceRules[depth1].get('StartHour'))
			if RecurrenceRules[depth1].get('EndHour') is not None:
				self.add_query_param('RecurrenceRules.' + str(depth1 + 1) + '.EndHour', RecurrenceRules[depth1].get('EndHour'))
	def get_InstanceAmount(self): # Integer
		return self.get_query_params().get('InstanceAmount')

	def set_InstanceAmount(self, InstanceAmount):  # Integer
		self.add_query_param('InstanceAmount', InstanceAmount)
