# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class AllocateDedicatedHostsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'AllocateDedicatedHosts','ecs')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_ActionOnMaintenance(self):
		return self.get_query_params().get('ActionOnMaintenance')

	def set_ActionOnMaintenance(self,ActionOnMaintenance):
		self.add_query_param('ActionOnMaintenance',ActionOnMaintenance)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		for i in range(len(Tags)):	
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key' , Tags[i].get('Key'))
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value' , Tags[i].get('Value'))


	def get_DedicatedHostType(self):
		return self.get_query_params().get('DedicatedHostType')

	def set_DedicatedHostType(self,DedicatedHostType):
		self.add_query_param('DedicatedHostType',DedicatedHostType)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_Quantity(self):
		return self.get_query_params().get('Quantity')

	def set_Quantity(self,Quantity):
		self.add_query_param('Quantity',Quantity)

	def get_DedicatedHostName(self):
		return self.get_query_params().get('DedicatedHostName')

	def set_DedicatedHostName(self,DedicatedHostName):
		self.add_query_param('DedicatedHostName',DedicatedHostName)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_AutoReleaseTime(self):
		return self.get_query_params().get('AutoReleaseTime')

	def set_AutoReleaseTime(self,AutoReleaseTime):
		self.add_query_param('AutoReleaseTime',AutoReleaseTime)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_NetworkAttributesSlbUdpTimeout(self):
		return self.get_query_params().get('NetworkAttributes.SlbUdpTimeout')

	def set_NetworkAttributesSlbUdpTimeout(self,NetworkAttributesSlbUdpTimeout):
		self.add_query_param('NetworkAttributes.SlbUdpTimeout',NetworkAttributesSlbUdpTimeout)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_NetworkAttributesUdpTimeout(self):
		return self.get_query_params().get('NetworkAttributes.UdpTimeout')

	def set_NetworkAttributesUdpTimeout(self,NetworkAttributesUdpTimeout):
		self.add_query_param('NetworkAttributes.UdpTimeout',NetworkAttributesUdpTimeout)