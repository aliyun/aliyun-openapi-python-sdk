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
class CreateImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateImage','ecs')

	def get_DiskDeviceMappings(self):
		return self.get_query_params().get('DiskDeviceMappings')

	def set_DiskDeviceMappings(self,DiskDeviceMappings):
		for i in range(len(DiskDeviceMappings)):	
			if DiskDeviceMappings[i].get('Size') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.Size' , DiskDeviceMappings[i].get('Size'))
			if DiskDeviceMappings[i].get('SnapshotId') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.SnapshotId' , DiskDeviceMappings[i].get('SnapshotId'))
			if DiskDeviceMappings[i].get('Device') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.Device' , DiskDeviceMappings[i].get('Device'))
			if DiskDeviceMappings[i].get('DiskType') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.DiskType' , DiskDeviceMappings[i].get('DiskType'))


	def get_Tag4Value(self):
		return self.get_query_params().get('Tag.4.Value')

	def set_Tag4Value(self,Tag4Value):
		self.add_query_param('Tag.4.Value',Tag4Value)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_Tag2Key(self):
		return self.get_query_params().get('Tag.2.Key')

	def set_Tag2Key(self,Tag2Key):
		self.add_query_param('Tag.2.Key',Tag2Key)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Tag3Key(self):
		return self.get_query_params().get('Tag.3.Key')

	def set_Tag3Key(self,Tag3Key):
		self.add_query_param('Tag.3.Key',Tag3Key)

	def get_Platform(self):
		return self.get_query_params().get('Platform')

	def set_Platform(self,Platform):
		self.add_query_param('Platform',Platform)

	def get_Tag1Value(self):
		return self.get_query_params().get('Tag.1.Value')

	def set_Tag1Value(self,Tag1Value):
		self.add_query_param('Tag.1.Value',Tag1Value)

	def get_ImageName(self):
		return self.get_query_params().get('ImageName')

	def set_ImageName(self,ImageName):
		self.add_query_param('ImageName',ImageName)

	def get_Tag3Value(self):
		return self.get_query_params().get('Tag.3.Value')

	def set_Tag3Value(self,Tag3Value):
		self.add_query_param('Tag.3.Value',Tag3Value)

	def get_Architecture(self):
		return self.get_query_params().get('Architecture')

	def set_Architecture(self,Architecture):
		self.add_query_param('Architecture',Architecture)

	def get_Tag5Key(self):
		return self.get_query_params().get('Tag.5.Key')

	def set_Tag5Key(self,Tag5Key):
		self.add_query_param('Tag.5.Key',Tag5Key)

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

	def get_Tag5Value(self):
		return self.get_query_params().get('Tag.5.Value')

	def set_Tag5Value(self,Tag5Value):
		self.add_query_param('Tag.5.Value',Tag5Value)

	def get_Tag1Key(self):
		return self.get_query_params().get('Tag.1.Key')

	def set_Tag1Key(self,Tag1Key):
		self.add_query_param('Tag.1.Key',Tag1Key)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Tag2Value(self):
		return self.get_query_params().get('Tag.2.Value')

	def set_Tag2Value(self,Tag2Value):
		self.add_query_param('Tag.2.Value',Tag2Value)

	def get_ImageVersion(self):
		return self.get_query_params().get('ImageVersion')

	def set_ImageVersion(self,ImageVersion):
		self.add_query_param('ImageVersion',ImageVersion)

	def get_Tag4Key(self):
		return self.get_query_params().get('Tag.4.Key')

	def set_Tag4Key(self,Tag4Key):
		self.add_query_param('Tag.4.Key',Tag4Key)