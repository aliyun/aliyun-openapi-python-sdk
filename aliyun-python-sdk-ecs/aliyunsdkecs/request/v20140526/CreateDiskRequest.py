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
from aliyunsdkecs.endpoint import endpoint_data

class CreateDiskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateDisk','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_SnapshotId(self): # String
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self, SnapshotId):  # String
		self.add_query_param('SnapshotId', SnapshotId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_EncryptAlgorithm(self): # String
		return self.get_query_params().get('EncryptAlgorithm')

	def set_EncryptAlgorithm(self, EncryptAlgorithm):  # String
		self.add_query_param('EncryptAlgorithm', EncryptAlgorithm)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_DiskName(self): # String
		return self.get_query_params().get('DiskName')

	def set_DiskName(self, DiskName):  # String
		self.add_query_param('DiskName', DiskName)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_DiskCategory(self): # String
		return self.get_query_params().get('DiskCategory')

	def set_DiskCategory(self, DiskCategory):  # String
		self.add_query_param('DiskCategory', DiskCategory)
	def get_StorageSetPartitionNumber(self): # Integer
		return self.get_query_params().get('StorageSetPartitionNumber')

	def set_StorageSetPartitionNumber(self, StorageSetPartitionNumber):  # Integer
		self.add_query_param('StorageSetPartitionNumber', StorageSetPartitionNumber)
	def get_MultiAttach(self): # String
		return self.get_query_params().get('MultiAttach')

	def set_MultiAttach(self, MultiAttach):  # String
		self.add_query_param('MultiAttach', MultiAttach)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.value', Tag[depth1].get('value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_AdvancedFeatures(self): # String
		return self.get_query_params().get('AdvancedFeatures')

	def set_AdvancedFeatures(self, AdvancedFeatures):  # String
		self.add_query_param('AdvancedFeatures', AdvancedFeatures)
	def get_Arns(self): # RepeatList
		return self.get_query_params().get('Arn')

	def set_Arns(self, Arn):  # RepeatList
		for depth1 in range(len(Arn)):
			if Arn[depth1].get('Rolearn') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.Rolearn', Arn[depth1].get('Rolearn'))
			if Arn[depth1].get('RoleType') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.RoleType', Arn[depth1].get('RoleType'))
			if Arn[depth1].get('AssumeRoleFor') is not None:
				self.add_query_param('Arn.' + str(depth1 + 1) + '.AssumeRoleFor', Arn[depth1].get('AssumeRoleFor'))
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_PerformanceLevel(self): # String
		return self.get_query_params().get('PerformanceLevel')

	def set_PerformanceLevel(self, PerformanceLevel):  # String
		self.add_query_param('PerformanceLevel', PerformanceLevel)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_StorageSetId(self): # String
		return self.get_query_params().get('StorageSetId')

	def set_StorageSetId(self, StorageSetId):  # String
		self.add_query_param('StorageSetId', StorageSetId)
	def get_Size(self): # Integer
		return self.get_query_params().get('Size')

	def set_Size(self, Size):  # Integer
		self.add_query_param('Size', Size)
	def get_Encrypted(self): # Boolean
		return self.get_query_params().get('Encrypted')

	def set_Encrypted(self, Encrypted):  # Boolean
		self.add_query_param('Encrypted', Encrypted)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_StorageClusterId(self): # String
		return self.get_query_params().get('StorageClusterId')

	def set_StorageClusterId(self, StorageClusterId):  # String
		self.add_query_param('StorageClusterId', StorageClusterId)
	def get_KMSKeyId(self): # String
		return self.get_query_params().get('KMSKeyId')

	def set_KMSKeyId(self, KMSKeyId):  # String
		self.add_query_param('KMSKeyId', KMSKeyId)
