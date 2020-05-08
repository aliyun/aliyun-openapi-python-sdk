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

class OperateExistsNodeClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'OperateExistsNodeCluster','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_LogPath(self):
		return self.get_query_params().get('LogPath')

	def set_LogPath(self,LogPath):
		self.add_query_param('LogPath',LogPath)

	def get_MasterInstanceIdLists(self):
		return self.get_query_params().get('MasterInstanceIdLists')

	def set_MasterInstanceIdLists(self,MasterInstanceIdLists):
		for i in range(len(MasterInstanceIdLists)):	
			if MasterInstanceIdLists[i] is not None:
				self.add_query_param('MasterInstanceIdList.' + str(i + 1) , MasterInstanceIdLists[i]);

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

	def get_IsResize(self):
		return self.get_query_params().get('IsResize')

	def set_IsResize(self,IsResize):
		self.add_query_param('IsResize',IsResize)

	def get_DepositType(self):
		return self.get_query_params().get('DepositType')

	def set_DepositType(self,DepositType):
		self.add_query_param('DepositType',DepositType)

	def get_MachineType(self):
		return self.get_query_params().get('MachineType')

	def set_MachineType(self,MachineType):
		self.add_query_param('MachineType',MachineType)

	def get_UseLocalMetaDb(self):
		return self.get_query_params().get('UseLocalMetaDb')

	def set_UseLocalMetaDb(self,UseLocalMetaDb):
		self.add_query_param('UseLocalMetaDb',UseLocalMetaDb)

	def get_EmrVer(self):
		return self.get_query_params().get('EmrVer')

	def set_EmrVer(self,EmrVer):
		self.add_query_param('EmrVer',EmrVer)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_OptionSoftWareLists(self):
		return self.get_query_params().get('OptionSoftWareLists')

	def set_OptionSoftWareLists(self,OptionSoftWareLists):
		for i in range(len(OptionSoftWareLists)):	
			if OptionSoftWareLists[i] is not None:
				self.add_query_param('OptionSoftWareList.' + str(i + 1) , OptionSoftWareLists[i]);

	def get_InstanceIdLists(self):
		return self.get_query_params().get('InstanceIdLists')

	def set_InstanceIdLists(self,InstanceIdLists):
		for i in range(len(InstanceIdLists)):	
			if InstanceIdLists[i] is not None:
				self.add_query_param('InstanceIdList.' + str(i + 1) , InstanceIdLists[i]);

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_OperateType(self):
		return self.get_query_params().get('OperateType')

	def set_OperateType(self,OperateType):
		self.add_query_param('OperateType',OperateType)

	def get_HighAvailabilityEnable(self):
		return self.get_query_params().get('HighAvailabilityEnable')

	def set_HighAvailabilityEnable(self,HighAvailabilityEnable):
		self.add_query_param('HighAvailabilityEnable',HighAvailabilityEnable)