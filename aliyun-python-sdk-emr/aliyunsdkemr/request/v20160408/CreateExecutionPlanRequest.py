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
from aliyunsdkemr.endpoint import endpoint_data

class CreateExecutionPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateExecutionPlan','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TimeInterval(self):
		return self.get_query_params().get('TimeInterval')

	def set_TimeInterval(self,TimeInterval):
		self.add_query_param('TimeInterval',TimeInterval)

	def get_LogPath(self):
		return self.get_query_params().get('LogPath')

	def set_LogPath(self,LogPath):
		self.add_query_param('LogPath',LogPath)

	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_Configurations(self):
		return self.get_query_params().get('Configurations')

	def set_Configurations(self,Configurations):
		self.add_query_param('Configurations',Configurations)

	def get_CreateClusterOnDemand(self):
		return self.get_query_params().get('CreateClusterOnDemand')

	def set_CreateClusterOnDemand(self,CreateClusterOnDemand):
		self.add_query_param('CreateClusterOnDemand',CreateClusterOnDemand)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_BootstrapActions(self):
		return self.get_query_params().get('BootstrapActions')

	def set_BootstrapActions(self, BootstrapActions):
		for depth1 in range(len(BootstrapActions)):
			if BootstrapActions[depth1].get('Path') is not None:
				self.add_query_param('BootstrapAction.' + str(depth1 + 1) + '.Path', BootstrapActions[depth1].get('Path'))
			if BootstrapActions[depth1].get('Arg') is not None:
				self.add_query_param('BootstrapAction.' + str(depth1 + 1) + '.Arg', BootstrapActions[depth1].get('Arg'))
			if BootstrapActions[depth1].get('Name') is not None:
				self.add_query_param('BootstrapAction.' + str(depth1 + 1) + '.Name', BootstrapActions[depth1].get('Name'))

	def get_EmrVer(self):
		return self.get_query_params().get('EmrVer')

	def set_EmrVer(self,EmrVer):
		self.add_query_param('EmrVer',EmrVer)

	def get_IsOpenPublicIp(self):
		return self.get_query_params().get('IsOpenPublicIp')

	def set_IsOpenPublicIp(self,IsOpenPublicIp):
		self.add_query_param('IsOpenPublicIp',IsOpenPublicIp)

	def get_InstanceGeneration(self):
		return self.get_query_params().get('InstanceGeneration')

	def set_InstanceGeneration(self,InstanceGeneration):
		self.add_query_param('InstanceGeneration',InstanceGeneration)

	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_OptionSoftWareLists(self):
		return self.get_query_params().get('OptionSoftWareLists')

	def set_OptionSoftWareLists(self, OptionSoftWareLists):
		for depth1 in range(len(OptionSoftWareLists)):
			if OptionSoftWareLists[depth1] is not None:
				self.add_query_param('OptionSoftWareList.' + str(depth1 + 1) , OptionSoftWareLists[depth1])

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)

	def get_EcsOrders(self):
		return self.get_query_params().get('EcsOrders')

	def set_EcsOrders(self, EcsOrders):
		for depth1 in range(len(EcsOrders)):
			if EcsOrders[depth1].get('NodeType') is not None:
				self.add_query_param('EcsOrder.' + str(depth1 + 1) + '.NodeType', EcsOrders[depth1].get('NodeType'))
			if EcsOrders[depth1].get('DiskCount') is not None:
				self.add_query_param('EcsOrder.' + str(depth1 + 1) + '.DiskCount', EcsOrders[depth1].get('DiskCount'))
			if EcsOrders[depth1].get('NodeCount') is not None:
				self.add_query_param('EcsOrder.' + str(depth1 + 1) + '.NodeCount', EcsOrders[depth1].get('NodeCount'))
			if EcsOrders[depth1].get('DiskCapacity') is not None:
				self.add_query_param('EcsOrder.' + str(depth1 + 1) + '.DiskCapacity', EcsOrders[depth1].get('DiskCapacity'))
			if EcsOrders[depth1].get('Index') is not None:
				self.add_query_param('EcsOrder.' + str(depth1 + 1) + '.Index', EcsOrders[depth1].get('Index'))
			if EcsOrders[depth1].get('InstanceType') is not None:
				self.add_query_param('EcsOrder.' + str(depth1 + 1) + '.InstanceType', EcsOrders[depth1].get('InstanceType'))
			if EcsOrders[depth1].get('DiskType') is not None:
				self.add_query_param('EcsOrder.' + str(depth1 + 1) + '.DiskType', EcsOrders[depth1].get('DiskType'))

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_UseCustomHiveMetaDB(self):
		return self.get_query_params().get('UseCustomHiveMetaDB')

	def set_UseCustomHiveMetaDB(self,UseCustomHiveMetaDB):
		self.add_query_param('UseCustomHiveMetaDB',UseCustomHiveMetaDB)

	def get_InitCustomHiveMetaDB(self):
		return self.get_query_params().get('InitCustomHiveMetaDB')

	def set_InitCustomHiveMetaDB(self,InitCustomHiveMetaDB):
		self.add_query_param('InitCustomHiveMetaDB',InitCustomHiveMetaDB)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_EasEnable(self):
		return self.get_query_params().get('EasEnable')

	def set_EasEnable(self,EasEnable):
		self.add_query_param('EasEnable',EasEnable)

	def get_JobIdLists(self):
		return self.get_query_params().get('JobIdLists')

	def set_JobIdLists(self, JobIdLists):
		for depth1 in range(len(JobIdLists)):
			if JobIdLists[depth1] is not None:
				self.add_query_param('JobIdList.' + str(depth1 + 1) , JobIdLists[depth1])

	def get_DayOfMonth(self):
		return self.get_query_params().get('DayOfMonth')

	def set_DayOfMonth(self,DayOfMonth):
		self.add_query_param('DayOfMonth',DayOfMonth)

	def get_UseLocalMetaDb(self):
		return self.get_query_params().get('UseLocalMetaDb')

	def set_UseLocalMetaDb(self,UseLocalMetaDb):
		self.add_query_param('UseLocalMetaDb',UseLocalMetaDb)

	def get_UserDefinedEmrEcsRole(self):
		return self.get_query_params().get('UserDefinedEmrEcsRole')

	def set_UserDefinedEmrEcsRole(self,UserDefinedEmrEcsRole):
		self.add_query_param('UserDefinedEmrEcsRole',UserDefinedEmrEcsRole)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_TimeUnit(self):
		return self.get_query_params().get('TimeUnit')

	def set_TimeUnit(self,TimeUnit):
		self.add_query_param('TimeUnit',TimeUnit)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_WorkflowDefinition(self):
		return self.get_query_params().get('WorkflowDefinition')

	def set_WorkflowDefinition(self,WorkflowDefinition):
		self.add_query_param('WorkflowDefinition',WorkflowDefinition)

	def get_DayOfWeek(self):
		return self.get_query_params().get('DayOfWeek')

	def set_DayOfWeek(self,DayOfWeek):
		self.add_query_param('DayOfWeek',DayOfWeek)

	def get_Strategy(self):
		return self.get_query_params().get('Strategy')

	def set_Strategy(self,Strategy):
		self.add_query_param('Strategy',Strategy)

	def get_Configs(self):
		return self.get_query_params().get('Configs')

	def set_Configs(self, Configs):
		for depth1 in range(len(Configs)):
			if Configs[depth1].get('ConfigKey') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.ConfigKey', Configs[depth1].get('ConfigKey'))
			if Configs[depth1].get('FileName') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.FileName', Configs[depth1].get('FileName'))
			if Configs[depth1].get('Encrypt') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.Encrypt', Configs[depth1].get('Encrypt'))
			if Configs[depth1].get('Replace') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.Replace', Configs[depth1].get('Replace'))
			if Configs[depth1].get('ConfigValue') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.ConfigValue', Configs[depth1].get('ConfigValue'))
			if Configs[depth1].get('ServiceName') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.ServiceName', Configs[depth1].get('ServiceName'))

	def get_HighAvailabilityEnable(self):
		return self.get_query_params().get('HighAvailabilityEnable')

	def set_HighAvailabilityEnable(self,HighAvailabilityEnable):
		self.add_query_param('HighAvailabilityEnable',HighAvailabilityEnable)

	def get_LogEnable(self):
		return self.get_query_params().get('LogEnable')

	def set_LogEnable(self,LogEnable):
		self.add_query_param('LogEnable',LogEnable)