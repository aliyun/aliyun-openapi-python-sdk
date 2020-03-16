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
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_EncryptAlgorithm(self):
		return self.get_query_params().get('EncryptAlgorithm')

	def set_EncryptAlgorithm(self,EncryptAlgorithm):
		self.add_query_param('EncryptAlgorithm',EncryptAlgorithm)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_DiskName(self):
		return self.get_query_params().get('DiskName')

	def set_DiskName(self,DiskName):
		self.add_query_param('DiskName',DiskName)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_DiskCategory(self):
		return self.get_query_params().get('DiskCategory')

	def set_DiskCategory(self,DiskCategory):
		self.add_query_param('DiskCategory',DiskCategory)

	def get_StorageSetPartitionNumber(self):
		return self.get_query_params().get('StorageSetPartitionNumber')

	def set_StorageSetPartitionNumber(self,StorageSetPartitionNumber):
		self.add_query_param('StorageSetPartitionNumber',StorageSetPartitionNumber)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		for i in range(len(Tags)):	
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value' , Tags[i].get('Value'))
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key' , Tags[i].get('Key'))


	def get_Arns(self):
		return self.get_query_params().get('Arns')

	def set_Arns(self,Arns):
		for i in range(len(Arns)):	
			if Arns[i].get('Rolearn') is not None:
				self.add_query_param('Arn.' + str(i + 1) + '.Rolearn' , Arns[i].get('Rolearn'))
			if Arns[i].get('RoleType') is not None:
				self.add_query_param('Arn.' + str(i + 1) + '.RoleType' , Arns[i].get('RoleType'))
			if Arns[i].get('AssumeRoleFor') is not None:
				self.add_query_param('Arn.' + str(i + 1) + '.AssumeRoleFor' , Arns[i].get('AssumeRoleFor'))


	def get_AdvancedFeatures(self):
		return self.get_query_params().get('AdvancedFeatures')

	def set_AdvancedFeatures(self,AdvancedFeatures):
		self.add_query_param('AdvancedFeatures',AdvancedFeatures)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_PerformanceLevel(self):
		return self.get_query_params().get('PerformanceLevel')

	def set_PerformanceLevel(self,PerformanceLevel):
		self.add_query_param('PerformanceLevel',PerformanceLevel)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_StorageSetId(self):
		return self.get_query_params().get('StorageSetId')

	def set_StorageSetId(self,StorageSetId):
		self.add_query_param('StorageSetId',StorageSetId)

	def get_Size(self):
		return self.get_query_params().get('Size')

	def set_Size(self,Size):
		self.add_query_param('Size',Size)

	def get_Encrypted(self):
		return self.get_query_params().get('Encrypted')

	def set_Encrypted(self,Encrypted):
		self.add_query_param('Encrypted',Encrypted)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_KMSKeyId(self):
		return self.get_query_params().get('KMSKeyId')

	def set_KMSKeyId(self,KMSKeyId):
		self.add_query_param('KMSKeyId',KMSKeyId)