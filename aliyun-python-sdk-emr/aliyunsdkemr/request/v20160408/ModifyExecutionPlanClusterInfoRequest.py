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
class ModifyExecutionPlanClusterInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyExecutionPlanClusterInfo')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_LogEnable(self):
		return self.get_query_params().get('LogEnable')

	def set_LogEnable(self,LogEnable):
		self.add_query_param('LogEnable',LogEnable)

	def get_LogPath(self):
		return self.get_query_params().get('LogPath')

	def set_LogPath(self,LogPath):
		self.add_query_param('LogPath',LogPath)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_IsOpenPublicIp(self):
		return self.get_query_params().get('IsOpenPublicIp')

	def set_IsOpenPublicIp(self,IsOpenPublicIp):
		self.add_query_param('IsOpenPublicIp',IsOpenPublicIp)

	def get_CreateClusterOnDemand(self):
		return self.get_query_params().get('CreateClusterOnDemand')

	def set_CreateClusterOnDemand(self,CreateClusterOnDemand):
		self.add_query_param('CreateClusterOnDemand',CreateClusterOnDemand)

	def get_EmrVer(self):
		return self.get_query_params().get('EmrVer')

	def set_EmrVer(self,EmrVer):
		self.add_query_param('EmrVer',EmrVer)

	def get_OptionSoftWareLists(self):
		return self.get_query_params().get('OptionSoftWareLists')

	def set_OptionSoftWareLists(self,OptionSoftWareLists):
		for i in range(len(OptionSoftWareLists)):	
			self.add_query_param('OptionSoftWareList.' + bytes(i + 1) , OptionSoftWareLists[i]);

	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_HighAvailabilityEnable(self):
		return self.get_query_params().get('HighAvailabilityEnable')

	def set_HighAvailabilityEnable(self,HighAvailabilityEnable):
		self.add_query_param('HighAvailabilityEnable',HighAvailabilityEnable)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_InstanceGeneration(self):
		return self.get_query_params().get('InstanceGeneration')

	def set_InstanceGeneration(self,InstanceGeneration):
		self.add_query_param('InstanceGeneration',InstanceGeneration)

	def get_EcsOrders(self):
		return self.get_query_params().get('EcsOrders')

	def set_EcsOrders(self,EcsOrders):
		for i in range(len(EcsOrders)):	
			self.add_query_param('EcsOrder.' + bytes(i + 1) + '.Index' , EcsOrders[i].get('Index'))
			self.add_query_param('EcsOrder.' + bytes(i + 1) + '.NodeCount' , EcsOrders[i].get('NodeCount'))
			self.add_query_param('EcsOrder.' + bytes(i + 1) + '.InstanceType' , EcsOrders[i].get('InstanceType'))
			self.add_query_param('EcsOrder.' + bytes(i + 1) + '.DiskType' , EcsOrders[i].get('DiskType'))
			self.add_query_param('EcsOrder.' + bytes(i + 1) + '.DiskCapacity' , EcsOrders[i].get('DiskCapacity'))
			self.add_query_param('EcsOrder.' + bytes(i + 1) + '.NodeType' , EcsOrders[i].get('NodeType'))
			self.add_query_param('EcsOrder.' + bytes(i + 1) + '.DiskCount' , EcsOrders[i].get('DiskCount'))


	def get_BootstrapActions(self):
		return self.get_query_params().get('BootstrapActions')

	def set_BootstrapActions(self,BootstrapActions):
		for i in range(len(BootstrapActions)):	
			self.add_query_param('BootstrapAction.' + bytes(i + 1) + '.Name' , BootstrapActions[i].get('Name'))
			self.add_query_param('BootstrapAction.' + bytes(i + 1) + '.Path' , BootstrapActions[i].get('Path'))
			self.add_query_param('BootstrapAction.' + bytes(i + 1) + '.Arg' , BootstrapActions[i].get('Arg'))


	def get_Configurations(self):
		return self.get_query_params().get('Configurations')

	def set_Configurations(self,Configurations):
		self.add_query_param('Configurations',Configurations)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)