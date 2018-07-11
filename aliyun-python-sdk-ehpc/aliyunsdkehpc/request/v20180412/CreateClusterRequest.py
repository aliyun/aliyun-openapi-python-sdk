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
class CreateClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'CreateCluster','ehs')

	def get_SccClusterId(self):
		return self.get_query_params().get('SccClusterId')

	def set_SccClusterId(self,SccClusterId):
		self.add_query_param('SccClusterId',SccClusterId)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_EcsOrderManagerInstanceType(self):
		return self.get_query_params().get('EcsOrder.Manager.InstanceType')

	def set_EcsOrderManagerInstanceType(self,EcsOrderManagerInstanceType):
		self.add_query_param('EcsOrder.Manager.InstanceType',EcsOrderManagerInstanceType)

	def get_EhpcVersion(self):
		return self.get_query_params().get('EhpcVersion')

	def set_EhpcVersion(self,EhpcVersion):
		self.add_query_param('EhpcVersion',EhpcVersion)

	def get_AccountType(self):
		return self.get_query_params().get('AccountType')

	def set_AccountType(self,AccountType):
		self.add_query_param('AccountType',AccountType)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_SecurityGroupName(self):
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self,SecurityGroupName):
		self.add_query_param('SecurityGroupName',SecurityGroupName)

	def get_EcsOrderComputeInstanceType(self):
		return self.get_query_params().get('EcsOrder.Compute.InstanceType')

	def set_EcsOrderComputeInstanceType(self,EcsOrderComputeInstanceType):
		self.add_query_param('EcsOrder.Compute.InstanceType',EcsOrderComputeInstanceType)

	def get_ImageOwnerAlias(self):
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self,ImageOwnerAlias):
		self.add_query_param('ImageOwnerAlias',ImageOwnerAlias)

	def get_VolumeType(self):
		return self.get_query_params().get('VolumeType')

	def set_VolumeType(self,VolumeType):
		self.add_query_param('VolumeType',VolumeType)

	def get_DeployMode(self):
		return self.get_query_params().get('DeployMode')

	def set_DeployMode(self,DeployMode):
		self.add_query_param('DeployMode',DeployMode)

	def get_EcsOrderManagerCount(self):
		return self.get_query_params().get('EcsOrder.Manager.Count')

	def set_EcsOrderManagerCount(self,EcsOrderManagerCount):
		self.add_query_param('EcsOrder.Manager.Count',EcsOrderManagerCount)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_EcsOrderLoginCount(self):
		return self.get_query_params().get('EcsOrder.Login.Count')

	def set_EcsOrderLoginCount(self,EcsOrderLoginCount):
		self.add_query_param('EcsOrder.Login.Count',EcsOrderLoginCount)

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

	def get_VolumeProtocol(self):
		return self.get_query_params().get('VolumeProtocol')

	def set_VolumeProtocol(self,VolumeProtocol):
		self.add_query_param('VolumeProtocol',VolumeProtocol)

	def get_OsTag(self):
		return self.get_query_params().get('OsTag')

	def set_OsTag(self,OsTag):
		self.add_query_param('OsTag',OsTag)

	def get_RemoteDirectory(self):
		return self.get_query_params().get('RemoteDirectory')

	def set_RemoteDirectory(self,RemoteDirectory):
		self.add_query_param('RemoteDirectory',RemoteDirectory)

	def get_EcsOrderComputeCount(self):
		return self.get_query_params().get('EcsOrder.Compute.Count')

	def set_EcsOrderComputeCount(self,EcsOrderComputeCount):
		self.add_query_param('EcsOrder.Compute.Count',EcsOrderComputeCount)

	def get_ComputeSpotStrategy(self):
		return self.get_query_params().get('ComputeSpotStrategy')

	def set_ComputeSpotStrategy(self,ComputeSpotStrategy):
		self.add_query_param('ComputeSpotStrategy',ComputeSpotStrategy)

	def get_PostInstallScripts(self):
		return self.get_query_params().get('PostInstallScripts')

	def set_PostInstallScripts(self,PostInstallScripts):
		for i in range(len(PostInstallScripts)):	
			if PostInstallScripts[i].get('Url') is not None:
				self.add_query_param('PostInstallScript.' + str(i + 1) + '.Url' , PostInstallScripts[i].get('Url'))
			if PostInstallScripts[i].get('Args') is not None:
				self.add_query_param('PostInstallScript.' + str(i + 1) + '.Args' , PostInstallScripts[i].get('Args'))


	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_Applications(self):
		return self.get_query_params().get('Applications')

	def set_Applications(self,Applications):
		for i in range(len(Applications)):	
			if Applications[i].get('Tag') is not None:
				self.add_query_param('Application.' + str(i + 1) + '.Tag' , Applications[i].get('Tag'))


	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_EcsChargeType(self):
		return self.get_query_params().get('EcsChargeType')

	def set_EcsChargeType(self,EcsChargeType):
		self.add_query_param('EcsChargeType',EcsChargeType)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_HaEnable(self):
		return self.get_query_params().get('HaEnable')

	def set_HaEnable(self,HaEnable):
		self.add_query_param('HaEnable',HaEnable)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_SchedulerType(self):
		return self.get_query_params().get('SchedulerType')

	def set_SchedulerType(self,SchedulerType):
		self.add_query_param('SchedulerType',SchedulerType)

	def get_VolumeId(self):
		return self.get_query_params().get('VolumeId')

	def set_VolumeId(self,VolumeId):
		self.add_query_param('VolumeId',VolumeId)

	def get_VolumeMountpoint(self):
		return self.get_query_params().get('VolumeMountpoint')

	def set_VolumeMountpoint(self,VolumeMountpoint):
		self.add_query_param('VolumeMountpoint',VolumeMountpoint)

	def get_EcsOrderLoginInstanceType(self):
		return self.get_query_params().get('EcsOrder.Login.InstanceType')

	def set_EcsOrderLoginInstanceType(self,EcsOrderLoginInstanceType):
		self.add_query_param('EcsOrder.Login.InstanceType',EcsOrderLoginInstanceType)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)