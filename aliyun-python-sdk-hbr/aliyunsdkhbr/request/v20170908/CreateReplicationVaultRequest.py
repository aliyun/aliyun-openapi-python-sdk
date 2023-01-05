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
from aliyunsdkhbr.endpoint import endpoint_data

class CreateReplicationVaultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateReplicationVault')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ReplicationSourceVaultId(self): # String
		return self.get_query_params().get('ReplicationSourceVaultId')

	def set_ReplicationSourceVaultId(self, ReplicationSourceVaultId):  # String
		self.add_query_param('ReplicationSourceVaultId', ReplicationSourceVaultId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_VaultName(self): # String
		return self.get_query_params().get('VaultName')

	def set_VaultName(self, VaultName):  # String
		self.add_query_param('VaultName', VaultName)
	def get_RedundancyType(self): # String
		return self.get_query_params().get('RedundancyType')

	def set_RedundancyType(self, RedundancyType):  # String
		self.add_query_param('RedundancyType', RedundancyType)
	def get_ReplicationSourceRegionId(self): # String
		return self.get_query_params().get('ReplicationSourceRegionId')

	def set_ReplicationSourceRegionId(self, ReplicationSourceRegionId):  # String
		self.add_query_param('ReplicationSourceRegionId', ReplicationSourceRegionId)
	def get_VaultRegionId(self): # String
		return self.get_query_params().get('VaultRegionId')

	def set_VaultRegionId(self, VaultRegionId):  # String
		self.add_query_param('VaultRegionId', VaultRegionId)
	def get_VaultStorageClass(self): # String
		return self.get_query_params().get('VaultStorageClass')

	def set_VaultStorageClass(self, VaultStorageClass):  # String
		self.add_query_param('VaultStorageClass', VaultStorageClass)
