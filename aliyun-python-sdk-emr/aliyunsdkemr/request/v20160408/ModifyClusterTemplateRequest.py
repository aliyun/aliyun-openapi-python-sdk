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
class ModifyClusterTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyClusterTemplate')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_LogPath(self):
		return self.get_query_params().get('LogPath')

	def set_LogPath(self,LogPath):
		self.add_query_param('LogPath',LogPath)

	def get_MasterPwd(self):
		return self.get_query_params().get('MasterPwd')

	def set_MasterPwd(self,MasterPwd):
		self.add_query_param('MasterPwd',MasterPwd)

	def get_Configurations(self):
		return self.get_query_params().get('Configurations')

	def set_Configurations(self,Configurations):
		self.add_query_param('Configurations',Configurations)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_SshEnable(self):
		return self.get_query_params().get('SshEnable')

	def set_SshEnable(self,SshEnable):
		self.add_query_param('SshEnable',SshEnable)

	def get_EasEnable(self):
		return self.get_query_params().get('EasEnable')

	def set_EasEnable(self,EasEnable):
		self.add_query_param('EasEnable',EasEnable)

	def get_SecurityGroupName(self):
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self,SecurityGroupName):
		self.add_query_param('SecurityGroupName',SecurityGroupName)

	def get_BootstrapActions(self):
		return self.get_query_params().get('BootstrapActions')

	def set_BootstrapActions(self,BootstrapActions):
		for i in range(len(BootstrapActions)):	
			if BootstrapActions[i].get('Name') is not None:
				self.add_query_param('BootstrapAction.' + str(i + 1) + '.Name' , BootstrapActions[i].get('Name'))
			if BootstrapActions[i].get('Path') is not None:
				self.add_query_param('BootstrapAction.' + str(i + 1) + '.Path' , BootstrapActions[i].get('Path'))
			if BootstrapActions[i].get('Arg') is not None:
				self.add_query_param('BootstrapAction.' + str(i + 1) + '.Arg' , BootstrapActions[i].get('Arg'))


	def get_UseLocalMetaDb(self):
		return self.get_query_params().get('UseLocalMetaDb')

	def set_UseLocalMetaDb(self,UseLocalMetaDb):
		self.add_query_param('UseLocalMetaDb',UseLocalMetaDb)

	def get_EmrVer(self):
		return self.get_query_params().get('EmrVer')

	def set_EmrVer(self,EmrVer):
		self.add_query_param('EmrVer',EmrVer)

	def get_TemplateName(self):
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self,TemplateName):
		self.add_query_param('TemplateName',TemplateName)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_UserDefinedEmrEcsRole(self):
		return self.get_query_params().get('UserDefinedEmrEcsRole')

	def set_UserDefinedEmrEcsRole(self,UserDefinedEmrEcsRole):
		self.add_query_param('UserDefinedEmrEcsRole',UserDefinedEmrEcsRole)

	def get_IsOpenPublicIp(self):
		return self.get_query_params().get('IsOpenPublicIp')

	def set_IsOpenPublicIp(self,IsOpenPublicIp):
		self.add_query_param('IsOpenPublicIp',IsOpenPublicIp)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_lIoOptimized(self):
		return self.get_query_params().get('lIoOptimized')

	def set_lIoOptimized(self,lIoOptimized):
		self.add_query_param('lIoOptimized',lIoOptimized)

	def get_InstanceGeneration(self):
		return self.get_query_params().get('InstanceGeneration')

	def set_InstanceGeneration(self,InstanceGeneration):
		self.add_query_param('InstanceGeneration',InstanceGeneration)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

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

	def get_HostGroups(self):
		return self.get_query_params().get('HostGroups')

	def set_HostGroups(self,HostGroups):
		for i in range(len(HostGroups)):	
			if HostGroups[i].get('HostGroupId') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.HostGroupId' , HostGroups[i].get('HostGroupId'))
			if HostGroups[i].get('HostGroupName') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.HostGroupName' , HostGroups[i].get('HostGroupName'))
			if HostGroups[i].get('HostGroupType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.HostGroupType' , HostGroups[i].get('HostGroupType'))
			if HostGroups[i].get('ClusterId') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.ClusterId' , HostGroups[i].get('ClusterId'))
			if HostGroups[i].get('Comment') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.Comment' , HostGroups[i].get('Comment'))
			if HostGroups[i].get('CreateType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.CreateType' , HostGroups[i].get('CreateType'))
			if HostGroups[i].get('ChargeType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.ChargeType' , HostGroups[i].get('ChargeType'))
			if HostGroups[i].get('Period') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.Period' , HostGroups[i].get('Period'))
			if HostGroups[i].get('NodeCount') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.NodeCount' , HostGroups[i].get('NodeCount'))
			if HostGroups[i].get('InstanceType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.InstanceType' , HostGroups[i].get('InstanceType'))
			if HostGroups[i].get('DiskType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.DiskType' , HostGroups[i].get('DiskType'))
			if HostGroups[i].get('DiskCapacity') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.DiskCapacity' , HostGroups[i].get('DiskCapacity'))
			if HostGroups[i].get('DiskCount') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.DiskCount' , HostGroups[i].get('DiskCount'))
			if HostGroups[i].get('SysDiskCapacity') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.SysDiskCapacity' , HostGroups[i].get('SysDiskCapacity'))
			if HostGroups[i].get('AutoRenew') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.AutoRenew' , HostGroups[i].get('AutoRenew'))
			if HostGroups[i].get('VSwitchId') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.VSwitchId' , HostGroups[i].get('VSwitchId'))


	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_HighAvailabilityEnable(self):
		return self.get_query_params().get('HighAvailabilityEnable')

	def set_HighAvailabilityEnable(self,HighAvailabilityEnable):
		self.add_query_param('HighAvailabilityEnable',HighAvailabilityEnable)