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
from aliyunsdkpolardb.endpoint import endpoint_data

class CreateDBClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'CreateDBCluster','polardb')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DBClusterDescription(self):
		return self.get_query_params().get('DBClusterDescription')

	def set_DBClusterDescription(self,DBClusterDescription):
		self.add_query_param('DBClusterDescription',DBClusterDescription)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_ClusterNetworkType(self):
		return self.get_query_params().get('ClusterNetworkType')

	def set_ClusterNetworkType(self,ClusterNetworkType):
		self.add_query_param('ClusterNetworkType',ClusterNetworkType)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_DBNodeClass(self):
		return self.get_query_params().get('DBNodeClass')

	def set_DBNodeClass(self,DBNodeClass):
		self.add_query_param('DBNodeClass',DBNodeClass)

	def get_GDNId(self):
		return self.get_query_params().get('GDNId')

	def set_GDNId(self,GDNId):
		self.add_query_param('GDNId',GDNId)

	def get_CreationOption(self):
		return self.get_query_params().get('CreationOption')

	def set_CreationOption(self,CreationOption):
		self.add_query_param('CreationOption',CreationOption)

	def get_SourceResourceId(self):
		return self.get_query_params().get('SourceResourceId')

	def set_SourceResourceId(self,SourceResourceId):
		self.add_query_param('SourceResourceId',SourceResourceId)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_UsedTime(self):
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self,UsedTime):
		self.add_query_param('UsedTime',UsedTime)

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

	def get_VPCId(self):
		return self.get_query_params().get('VPCId')

	def set_VPCId(self,VPCId):
		self.add_query_param('VPCId',VPCId)

	def get_DBType(self):
		return self.get_query_params().get('DBType')

	def set_DBType(self,DBType):
		self.add_query_param('DBType',DBType)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_DBVersion(self):
		return self.get_query_params().get('DBVersion')

	def set_DBVersion(self,DBVersion):
		self.add_query_param('DBVersion',DBVersion)

	def get_CloneDataPoint(self):
		return self.get_query_params().get('CloneDataPoint')

	def set_CloneDataPoint(self,CloneDataPoint):
		self.add_query_param('CloneDataPoint',CloneDataPoint)

	def get_TDEStatus(self):
		return self.get_query_params().get('TDEStatus')

	def set_TDEStatus(self,TDEStatus):
		self.add_query_param('TDEStatus',TDEStatus)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)