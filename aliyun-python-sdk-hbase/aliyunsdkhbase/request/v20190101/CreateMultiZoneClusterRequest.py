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
from aliyunsdkhbase.endpoint import endpoint_data

class CreateMultiZoneClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'CreateMultiZoneCluster','hbase')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ArchVersion(self):
		return self.get_query_params().get('ArchVersion')

	def set_ArchVersion(self,ArchVersion):
		self.add_query_param('ArchVersion',ArchVersion)

	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_EngineVersion(self):
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self,EngineVersion):
		self.add_query_param('EngineVersion',EngineVersion)

	def get_LogDiskType(self):
		return self.get_query_params().get('LogDiskType')

	def set_LogDiskType(self,LogDiskType):
		self.add_query_param('LogDiskType',LogDiskType)

	def get_PrimaryVSwitchId(self):
		return self.get_query_params().get('PrimaryVSwitchId')

	def set_PrimaryVSwitchId(self,PrimaryVSwitchId):
		self.add_query_param('PrimaryVSwitchId',PrimaryVSwitchId)

	def get_LogInstanceType(self):
		return self.get_query_params().get('LogInstanceType')

	def set_LogInstanceType(self,LogInstanceType):
		self.add_query_param('LogInstanceType',LogInstanceType)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_LogNodeCount(self):
		return self.get_query_params().get('LogNodeCount')

	def set_LogNodeCount(self,LogNodeCount):
		self.add_query_param('LogNodeCount',LogNodeCount)

	def get_SecurityIPList(self):
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self,SecurityIPList):
		self.add_query_param('SecurityIPList',SecurityIPList)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_CoreDiskType(self):
		return self.get_query_params().get('CoreDiskType')

	def set_CoreDiskType(self,CoreDiskType):
		self.add_query_param('CoreDiskType',CoreDiskType)

	def get_ArbiterZoneId(self):
		return self.get_query_params().get('ArbiterZoneId')

	def set_ArbiterZoneId(self,ArbiterZoneId):
		self.add_query_param('ArbiterZoneId',ArbiterZoneId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_MultiZoneCombination(self):
		return self.get_query_params().get('MultiZoneCombination')

	def set_MultiZoneCombination(self,MultiZoneCombination):
		self.add_query_param('MultiZoneCombination',MultiZoneCombination)

	def get_PrimaryZoneId(self):
		return self.get_query_params().get('PrimaryZoneId')

	def set_PrimaryZoneId(self,PrimaryZoneId):
		self.add_query_param('PrimaryZoneId',PrimaryZoneId)

	def get_Engine(self):
		return self.get_query_params().get('Engine')

	def set_Engine(self,Engine):
		self.add_query_param('Engine',Engine)

	def get_StandbyVSwitchId(self):
		return self.get_query_params().get('StandbyVSwitchId')

	def set_StandbyVSwitchId(self,StandbyVSwitchId):
		self.add_query_param('StandbyVSwitchId',StandbyVSwitchId)

	def get_StandbyZoneId(self):
		return self.get_query_params().get('StandbyZoneId')

	def set_StandbyZoneId(self,StandbyZoneId):
		self.add_query_param('StandbyZoneId',StandbyZoneId)

	def get_MasterInstanceType(self):
		return self.get_query_params().get('MasterInstanceType')

	def set_MasterInstanceType(self,MasterInstanceType):
		self.add_query_param('MasterInstanceType',MasterInstanceType)

	def get_CoreNodeCount(self):
		return self.get_query_params().get('CoreNodeCount')

	def set_CoreNodeCount(self,CoreNodeCount):
		self.add_query_param('CoreNodeCount',CoreNodeCount)

	def get_LogDiskSize(self):
		return self.get_query_params().get('LogDiskSize')

	def set_LogDiskSize(self,LogDiskSize):
		self.add_query_param('LogDiskSize',LogDiskSize)

	def get_CoreInstanceType(self):
		return self.get_query_params().get('CoreInstanceType')

	def set_CoreInstanceType(self,CoreInstanceType):
		self.add_query_param('CoreInstanceType',CoreInstanceType)

	def get_CoreDiskSize(self):
		return self.get_query_params().get('CoreDiskSize')

	def set_CoreDiskSize(self,CoreDiskSize):
		self.add_query_param('CoreDiskSize',CoreDiskSize)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)

	def get_ArbiterVSwitchId(self):
		return self.get_query_params().get('ArbiterVSwitchId')

	def set_ArbiterVSwitchId(self,ArbiterVSwitchId):
		self.add_query_param('ArbiterVSwitchId',ArbiterVSwitchId)