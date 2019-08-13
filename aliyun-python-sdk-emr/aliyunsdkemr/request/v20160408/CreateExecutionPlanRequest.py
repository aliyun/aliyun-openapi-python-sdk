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

	def get_CreateClusterOnDemand(self):
		return self.get_query_params().get('CreateClusterOnDemand')

	def set_CreateClusterOnDemand(self,CreateClusterOnDemand):
		self.add_query_param('CreateClusterOnDemand',CreateClusterOnDemand)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_JobIdLists(self):
		return self.get_query_params().get('JobIdLists')

	def set_JobIdLists(self,JobIdLists):
		for i in range(len(JobIdLists)):	
			if JobIdLists[i] is not None:
				self.add_query_param('JobIdList.' + str(i + 1) , JobIdLists[i]);

	def get_DayOfMonth(self):
		return self.get_query_params().get('DayOfMonth')

	def set_DayOfMonth(self,DayOfMonth):
		self.add_query_param('DayOfMonth',DayOfMonth)

	def get_BootstrapActions(self):
		return self.get_query_params().get('BootstrapActions')

	def set_BootstrapActions(self,BootstrapActions):
		for i in range(len(BootstrapActions)):	
			if BootstrapActions[i].get('Path') is not None:
				self.add_query_param('BootstrapAction.' + str(i + 1) + '.Path' , BootstrapActions[i].get('Path'))
			if BootstrapActions[i].get('Arg') is not None:
				self.add_query_param('BootstrapAction.' + str(i + 1) + '.Arg' , BootstrapActions[i].get('Arg'))
			if BootstrapActions[i].get('Name') is not None:
				self.add_query_param('BootstrapAction.' + str(i + 1) + '.Name' , BootstrapActions[i].get('Name'))


	def get_UseLocalMetaDb(self):
		return self.get_query_params().get('UseLocalMetaDb')

	def set_UseLocalMetaDb(self,UseLocalMetaDb):
		self.add_query_param('UseLocalMetaDb',UseLocalMetaDb)

	def get_EmrVer(self):
		return self.get_query_params().get('EmrVer')

	def set_EmrVer(self,EmrVer):
		self.add_query_param('EmrVer',EmrVer)

	def get_UserDefinedEmrEcsRole(self):
		return self.get_query_params().get('UserDefinedEmrEcsRole')

	def set_UserDefinedEmrEcsRole(self,UserDefinedEmrEcsRole):
		self.add_query_param('UserDefinedEmrEcsRole',UserDefinedEmrEcsRole)

	def get_IsOpenPublicIp(self):
		return self.get_query_params().get('IsOpenPublicIp')

	def set_IsOpenPublicIp(self,IsOpenPublicIp):
		self.add_query_param('IsOpenPublicIp',IsOpenPublicIp)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_TimeUnit(self):
		return self.get_query_params().get('TimeUnit')

	def set_TimeUnit(self,TimeUnit):
		self.add_query_param('TimeUnit',TimeUnit)

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

	def set_OptionSoftWareLists(self,OptionSoftWareLists):
		for i in range(len(OptionSoftWareLists)):	
			if OptionSoftWareLists[i] is not None:
				self.add_query_param('OptionSoftWareList.' + str(i + 1) , OptionSoftWareLists[i]);

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)

	def get_EcsOrders(self):
		return self.get_query_params().get('EcsOrders')

	def set_EcsOrders(self,EcsOrders):
		for i in range(len(EcsOrders)):	
			if EcsOrders[i].get('NodeType') is not None:
				self.add_query_param('EcsOrder.' + str(i + 1) + '.NodeType' , EcsOrders[i].get('NodeType'))
			if EcsOrders[i].get('DiskCount') is not None:
				self.add_query_param('EcsOrder.' + str(i + 1) + '.DiskCount' , EcsOrders[i].get('DiskCount'))
			if EcsOrders[i].get('NodeCount') is not None:
				self.add_query_param('EcsOrder.' + str(i + 1) + '.NodeCount' , EcsOrders[i].get('NodeCount'))
			if EcsOrders[i].get('DiskCapacity') is not None:
				self.add_query_param('EcsOrder.' + str(i + 1) + '.DiskCapacity' , EcsOrders[i].get('DiskCapacity'))
			if EcsOrders[i].get('Index') is not None:
				self.add_query_param('EcsOrder.' + str(i + 1) + '.Index' , EcsOrders[i].get('Index'))
			if EcsOrders[i].get('InstanceType') is not None:
				self.add_query_param('EcsOrder.' + str(i + 1) + '.InstanceType' , EcsOrders[i].get('InstanceType'))
			if EcsOrders[i].get('DiskType') is not None:
				self.add_query_param('EcsOrder.' + str(i + 1) + '.DiskType' , EcsOrders[i].get('DiskType'))


	def get_WorkflowDefinition(self):
		return self.get_query_params().get('WorkflowDefinition')

	def set_WorkflowDefinition(self,WorkflowDefinition):
		self.add_query_param('WorkflowDefinition',WorkflowDefinition)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_DayOfWeek(self):
		return self.get_query_params().get('DayOfWeek')

	def set_DayOfWeek(self,DayOfWeek):
		self.add_query_param('DayOfWeek',DayOfWeek)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_UseCustomHiveMetaDB(self):
		return self.get_query_params().get('UseCustomHiveMetaDB')

	def set_UseCustomHiveMetaDB(self,UseCustomHiveMetaDB):
		self.add_query_param('UseCustomHiveMetaDB',UseCustomHiveMetaDB)

	def get_Strategy(self):
		return self.get_query_params().get('Strategy')

	def set_Strategy(self,Strategy):
		self.add_query_param('Strategy',Strategy)

	def get_Configs(self):
		return self.get_query_params().get('Configs')

	def set_Configs(self,Configs):
		for i in range(len(Configs)):	
			if Configs[i].get('ConfigKey') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.ConfigKey' , Configs[i].get('ConfigKey'))
			if Configs[i].get('FileName') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.FileName' , Configs[i].get('FileName'))
			if Configs[i].get('Encrypt') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.Encrypt' , Configs[i].get('Encrypt'))
			if Configs[i].get('Replace') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.Replace' , Configs[i].get('Replace'))
			if Configs[i].get('ConfigValue') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.ConfigValue' , Configs[i].get('ConfigValue'))
			if Configs[i].get('ServiceName') is not None:
				self.add_query_param('Config.' + str(i + 1) + '.ServiceName' , Configs[i].get('ServiceName'))


	def get_HighAvailabilityEnable(self):
		return self.get_query_params().get('HighAvailabilityEnable')

	def set_HighAvailabilityEnable(self,HighAvailabilityEnable):
		self.add_query_param('HighAvailabilityEnable',HighAvailabilityEnable)

	def get_InitCustomHiveMetaDB(self):
		return self.get_query_params().get('InitCustomHiveMetaDB')

	def set_InitCustomHiveMetaDB(self,InitCustomHiveMetaDB):
		self.add_query_param('InitCustomHiveMetaDB',InitCustomHiveMetaDB)

	def get_LogEnable(self):
		return self.get_query_params().get('LogEnable')

	def set_LogEnable(self,LogEnable):
		self.add_query_param('LogEnable',LogEnable)