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

class AllocateDedicatedHostsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'AllocateDedicatedHosts','ecs')
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
	def get_CpuOverCommitRatio(self): # Float
		return self.get_query_params().get('CpuOverCommitRatio')

	def set_CpuOverCommitRatio(self, CpuOverCommitRatio):  # Float
		self.add_query_param('CpuOverCommitRatio', CpuOverCommitRatio)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_MinQuantity(self): # Integer
		return self.get_query_params().get('MinQuantity')

	def set_MinQuantity(self, MinQuantity):  # Integer
		self.add_query_param('MinQuantity', MinQuantity)
	def get_ActionOnMaintenance(self): # String
		return self.get_query_params().get('ActionOnMaintenance')

	def set_ActionOnMaintenance(self, ActionOnMaintenance):  # String
		self.add_query_param('ActionOnMaintenance', ActionOnMaintenance)
	def get_DedicatedHostClusterId(self): # String
		return self.get_query_params().get('DedicatedHostClusterId')

	def set_DedicatedHostClusterId(self, DedicatedHostClusterId):  # String
		self.add_query_param('DedicatedHostClusterId', DedicatedHostClusterId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
	def get_DedicatedHostType(self): # String
		return self.get_query_params().get('DedicatedHostType')

	def set_DedicatedHostType(self, DedicatedHostType):  # String
		self.add_query_param('DedicatedHostType', DedicatedHostType)
	def get_AutoRenewPeriod(self): # Integer
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self, AutoRenewPeriod):  # Integer
		self.add_query_param('AutoRenewPeriod', AutoRenewPeriod)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_Quantity(self): # Integer
		return self.get_query_params().get('Quantity')

	def set_Quantity(self, Quantity):  # Integer
		self.add_query_param('Quantity', Quantity)
	def get_DedicatedHostName(self): # String
		return self.get_query_params().get('DedicatedHostName')

	def set_DedicatedHostName(self, DedicatedHostName):  # String
		self.add_query_param('DedicatedHostName', DedicatedHostName)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_AutoReleaseTime(self): # String
		return self.get_query_params().get('AutoReleaseTime')

	def set_AutoReleaseTime(self, AutoReleaseTime):  # String
		self.add_query_param('AutoReleaseTime', AutoReleaseTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_NetworkAttributesSlbUdpTimeout(self): # Integer
		return self.get_query_params().get('NetworkAttributes.SlbUdpTimeout')

	def set_NetworkAttributesSlbUdpTimeout(self, NetworkAttributesSlbUdpTimeout):  # Integer
		self.add_query_param('NetworkAttributes.SlbUdpTimeout', NetworkAttributesSlbUdpTimeout)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_AutoPlacement(self): # String
		return self.get_query_params().get('AutoPlacement')

	def set_AutoPlacement(self, AutoPlacement):  # String
		self.add_query_param('AutoPlacement', AutoPlacement)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_NetworkAttributesUdpTimeout(self): # Integer
		return self.get_query_params().get('NetworkAttributes.UdpTimeout')

	def set_NetworkAttributesUdpTimeout(self, NetworkAttributesUdpTimeout):  # Integer
		self.add_query_param('NetworkAttributes.UdpTimeout', NetworkAttributesUdpTimeout)
