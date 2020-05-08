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
from aliyunsdkehpc.endpoint import endpoint_data

class AddNodesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'AddNodes','ehs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_JobQueue(self):
		return self.get_query_params().get('JobQueue')

	def set_JobQueue(self,JobQueue):
		self.add_query_param('JobQueue',JobQueue)

	def get_ImageOwnerAlias(self):
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self,ImageOwnerAlias):
		self.add_query_param('ImageOwnerAlias',ImageOwnerAlias)

	def get_SystemDiskType(self):
		return self.get_query_params().get('SystemDiskType')

	def set_SystemDiskType(self,SystemDiskType):
		self.add_query_param('SystemDiskType',SystemDiskType)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDiskSize',SystemDiskSize)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_HostNamePrefix(self):
		return self.get_query_params().get('HostNamePrefix')

	def set_HostNamePrefix(self,HostNamePrefix):
		self.add_query_param('HostNamePrefix',HostNamePrefix)

	def get_ComputeSpotPriceLimit(self):
		return self.get_query_params().get('ComputeSpotPriceLimit')

	def set_ComputeSpotPriceLimit(self,ComputeSpotPriceLimit):
		self.add_query_param('ComputeSpotPriceLimit',ComputeSpotPriceLimit)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_Count(self):
		return self.get_query_params().get('Count')

	def set_Count(self,Count):
		self.add_query_param('Count',Count)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ComputeSpotStrategy(self):
		return self.get_query_params().get('ComputeSpotStrategy')

	def set_ComputeSpotStrategy(self,ComputeSpotStrategy):
		self.add_query_param('ComputeSpotStrategy',ComputeSpotStrategy)

	def get_HostNameSuffix(self):
		return self.get_query_params().get('HostNameSuffix')

	def set_HostNameSuffix(self,HostNameSuffix):
		self.add_query_param('HostNameSuffix',HostNameSuffix)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_ComputeEnableHt(self):
		return self.get_query_params().get('ComputeEnableHt')

	def set_ComputeEnableHt(self,ComputeEnableHt):
		self.add_query_param('ComputeEnableHt',ComputeEnableHt)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_EcsChargeType(self):
		return self.get_query_params().get('EcsChargeType')

	def set_EcsChargeType(self,EcsChargeType):
		self.add_query_param('EcsChargeType',EcsChargeType)

	def get_CreateMode(self):
		return self.get_query_params().get('CreateMode')

	def set_CreateMode(self,CreateMode):
		self.add_query_param('CreateMode',CreateMode)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)