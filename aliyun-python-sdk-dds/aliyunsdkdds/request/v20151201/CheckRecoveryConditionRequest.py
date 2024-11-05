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
from aliyunsdkdds.endpoint import endpoint_data

class CheckRecoveryConditionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dds', '2015-12-01', 'CheckRecoveryCondition','dds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_EngineVersion(self): # String
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self, EngineVersion):  # String
		self.add_query_param('EngineVersion', EngineVersion)
	def get_SrcRegion(self): # String
		return self.get_query_params().get('SrcRegion')

	def set_SrcRegion(self, SrcRegion):  # String
		self.add_query_param('SrcRegion', SrcRegion)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_DatabaseNames(self): # String
		return self.get_query_params().get('DatabaseNames')

	def set_DatabaseNames(self, DatabaseNames):  # String
		self.add_query_param('DatabaseNames', DatabaseNames)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_RestoreTime(self): # String
		return self.get_query_params().get('RestoreTime')

	def set_RestoreTime(self, RestoreTime):  # String
		self.add_query_param('RestoreTime', RestoreTime)
	def get_DestRegion(self): # String
		return self.get_query_params().get('DestRegion')

	def set_DestRegion(self, DestRegion):  # String
		self.add_query_param('DestRegion', DestRegion)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_BackupId(self): # String
		return self.get_query_params().get('BackupId')

	def set_BackupId(self, BackupId):  # String
		self.add_query_param('BackupId', BackupId)
	def get_SourceDBInstance(self): # String
		return self.get_query_params().get('SourceDBInstance')

	def set_SourceDBInstance(self, SourceDBInstance):  # String
		self.add_query_param('SourceDBInstance', SourceDBInstance)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_RestoreType(self): # String
		return self.get_query_params().get('RestoreType')

	def set_RestoreType(self, RestoreType):  # String
		self.add_query_param('RestoreType', RestoreType)
