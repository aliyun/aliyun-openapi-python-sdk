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

class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'CreateInstance')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_DbInstanceConnType(self):
		return self.get_query_params().get('DbInstanceConnType')

	def set_DbInstanceConnType(self,DbInstanceConnType):
		self.add_query_param('DbInstanceConnType',DbInstanceConnType)

	def get_EngineVersion(self):
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self,EngineVersion):
		self.add_query_param('EngineVersion',EngineVersion)

	def get_DepMode(self):
		return self.get_query_params().get('DepMode')

	def set_DepMode(self,DepMode):
		self.add_query_param('DepMode',DepMode)

	def get_BackupId(self):
		return self.get_query_params().get('BackupId')

	def set_BackupId(self,BackupId):
		self.add_query_param('BackupId',BackupId)

	def get_DbInstanceType(self):
		return self.get_query_params().get('DbInstanceType')

	def set_DbInstanceType(self,DbInstanceType):
		self.add_query_param('DbInstanceType',DbInstanceType)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_SecurityIPList(self):
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self,SecurityIPList):
		self.add_query_param('SecurityIPList',SecurityIPList)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_CoreDiskType(self):
		return self.get_query_params().get('CoreDiskType')

	def set_CoreDiskType(self,CoreDiskType):
		self.add_query_param('CoreDiskType',CoreDiskType)

	def get_PricingCycle(self):
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self,PricingCycle):
		self.add_query_param('PricingCycle',PricingCycle)

	def get_CoreInstanceQuantity(self):
		return self.get_query_params().get('CoreInstanceQuantity')

	def set_CoreInstanceQuantity(self,CoreInstanceQuantity):
		self.add_query_param('CoreInstanceQuantity',CoreInstanceQuantity)

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_Engine(self):
		return self.get_query_params().get('Engine')

	def set_Engine(self,Engine):
		self.add_query_param('Engine',Engine)

	def get_RestoreTime(self):
		return self.get_query_params().get('RestoreTime')

	def set_RestoreTime(self,RestoreTime):
		self.add_query_param('RestoreTime',RestoreTime)

	def get_SrcDBInstanceId(self):
		return self.get_query_params().get('SrcDBInstanceId')

	def set_SrcDBInstanceId(self,SrcDBInstanceId):
		self.add_query_param('SrcDBInstanceId',SrcDBInstanceId)

	def get_MasterInstanceType(self):
		return self.get_query_params().get('MasterInstanceType')

	def set_MasterInstanceType(self,MasterInstanceType):
		self.add_query_param('MasterInstanceType',MasterInstanceType)

	def get_ColdStorageSize(self):
		return self.get_query_params().get('ColdStorageSize')

	def set_ColdStorageSize(self,ColdStorageSize):
		self.add_query_param('ColdStorageSize',ColdStorageSize)

	def get_CoreDiskQuantity(self):
		return self.get_query_params().get('CoreDiskQuantity')

	def set_CoreDiskQuantity(self,CoreDiskQuantity):
		self.add_query_param('CoreDiskQuantity',CoreDiskQuantity)

	def get_IsColdStorage(self):
		return self.get_query_params().get('IsColdStorage')

	def set_IsColdStorage(self,IsColdStorage):
		self.add_query_param('IsColdStorage',IsColdStorage)

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

	def get_DbType(self):
		return self.get_query_params().get('DbType')

	def set_DbType(self,DbType):
		self.add_query_param('DbType',DbType)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)