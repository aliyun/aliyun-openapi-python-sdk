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
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'CreateDBCluster')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DBClusterDescription(self): # String
		return self.get_query_params().get('DBClusterDescription')

	def set_DBClusterDescription(self, DBClusterDescription):  # String
		self.add_query_param('DBClusterDescription', DBClusterDescription)
	def get_CreationCategory(self): # String
		return self.get_query_params().get('CreationCategory')

	def set_CreationCategory(self, CreationCategory):  # String
		self.add_query_param('CreationCategory', CreationCategory)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_DBNodeClass(self): # String
		return self.get_query_params().get('DBNodeClass')

	def set_DBNodeClass(self, DBNodeClass):  # String
		self.add_query_param('DBNodeClass', DBNodeClass)
	def get_CreationOption(self): # String
		return self.get_query_params().get('CreationOption')

	def set_CreationOption(self, CreationOption):  # String
		self.add_query_param('CreationOption', CreationOption)
	def get_SourceResourceId(self): # String
		return self.get_query_params().get('SourceResourceId')

	def set_SourceResourceId(self, SourceResourceId):  # String
		self.add_query_param('SourceResourceId', SourceResourceId)
	def get_BackupRetentionPolicyOnClusterDeletion(self): # String
		return self.get_query_params().get('BackupRetentionPolicyOnClusterDeletion')

	def set_BackupRetentionPolicyOnClusterDeletion(self, BackupRetentionPolicyOnClusterDeletion):  # String
		self.add_query_param('BackupRetentionPolicyOnClusterDeletion', BackupRetentionPolicyOnClusterDeletion)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_SecurityIPList(self): # String
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self, SecurityIPList):  # String
		self.add_query_param('SecurityIPList', SecurityIPList)
	def get_DBMinorVersion(self): # String
		return self.get_query_params().get('DBMinorVersion')

	def set_DBMinorVersion(self, DBMinorVersion):  # String
		self.add_query_param('DBMinorVersion', DBMinorVersion)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_TDEStatus(self): # Boolean
		return self.get_query_params().get('TDEStatus')

	def set_TDEStatus(self, TDEStatus):  # Boolean
		self.add_query_param('TDEStatus', TDEStatus)
	def get_LowerCaseTableNames(self): # String
		return self.get_query_params().get('LowerCaseTableNames')

	def set_LowerCaseTableNames(self, LowerCaseTableNames):  # String
		self.add_query_param('LowerCaseTableNames', LowerCaseTableNames)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_DefaultTimeZone(self): # String
		return self.get_query_params().get('DefaultTimeZone')

	def set_DefaultTimeZone(self, DefaultTimeZone):  # String
		self.add_query_param('DefaultTimeZone', DefaultTimeZone)
	def get_ClusterNetworkType(self): # String
		return self.get_query_params().get('ClusterNetworkType')

	def set_ClusterNetworkType(self, ClusterNetworkType):  # String
		self.add_query_param('ClusterNetworkType', ClusterNetworkType)
	def get_ParameterGroupId(self): # String
		return self.get_query_params().get('ParameterGroupId')

	def set_ParameterGroupId(self, ParameterGroupId):  # String
		self.add_query_param('ParameterGroupId', ParameterGroupId)
	def get_GDNId(self): # String
		return self.get_query_params().get('GDNId')

	def set_GDNId(self, GDNId):  # String
		self.add_query_param('GDNId', GDNId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_UsedTime(self): # String
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self, UsedTime):  # String
		self.add_query_param('UsedTime', UsedTime)
	def get_VPCId(self): # String
		return self.get_query_params().get('VPCId')

	def set_VPCId(self, VPCId):  # String
		self.add_query_param('VPCId', VPCId)
	def get_DBType(self): # String
		return self.get_query_params().get('DBType')

	def set_DBType(self, DBType):  # String
		self.add_query_param('DBType', DBType)
	def get_DBVersion(self): # String
		return self.get_query_params().get('DBVersion')

	def set_DBVersion(self, DBVersion):  # String
		self.add_query_param('DBVersion', DBVersion)
	def get_CloneDataPoint(self): # String
		return self.get_query_params().get('CloneDataPoint')

	def set_CloneDataPoint(self, CloneDataPoint):  # String
		self.add_query_param('CloneDataPoint', CloneDataPoint)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
