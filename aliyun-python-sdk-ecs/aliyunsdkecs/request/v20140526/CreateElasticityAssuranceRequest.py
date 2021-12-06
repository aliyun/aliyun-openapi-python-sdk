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

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_PrivatePoolOptionsMatchCriteria(self):
		return self.get_query_params().get('PrivatePoolOptions.MatchCriteria')

	def set_PrivatePoolOptionsMatchCriteria(self,PrivatePoolOptionsMatchCriteria):
		self.add_query_param('PrivatePoolOptions.MatchCriteria',PrivatePoolOptionsMatchCriteria)

	def get_InstanceTypes(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceTypes(self, InstanceTypes):
		for depth1 in range(len(InstanceTypes)):
			if InstanceTypes[depth1] is not None:
				self.add_query_param('InstanceType.' + str(depth1 + 1) , InstanceTypes[depth1])

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_PrivatePoolOptionsName(self):
		return self.get_query_params().get('PrivatePoolOptions.Name')

	def set_PrivatePoolOptionsName(self,PrivatePoolOptionsName):
		self.add_query_param('PrivatePoolOptions.Name',PrivatePoolOptionsName)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_AssuranceTimes(self):
		return self.get_query_params().get('AssuranceTimes')

	def set_AssuranceTimes(self,AssuranceTimes):
		self.add_query_param('AssuranceTimes',AssuranceTimes)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InstanceCpuCoreCount(self):
		return self.get_query_params().get('InstanceCpuCoreCount')

	def set_InstanceCpuCoreCount(self,InstanceCpuCoreCount):
		self.add_query_param('InstanceCpuCoreCount',InstanceCpuCoreCount)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_ZoneIds(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneIds(self, ZoneIds):
		for depth1 in range(len(ZoneIds)):
			if ZoneIds[depth1] is not None:
				self.add_query_param('ZoneId.' + str(depth1 + 1) , ZoneIds[depth1])

	def get_InstanceAmount(self):
		return self.get_query_params().get('InstanceAmount')

	def set_InstanceAmount(self,InstanceAmount):
		self.add_query_param('InstanceAmount',InstanceAmount)