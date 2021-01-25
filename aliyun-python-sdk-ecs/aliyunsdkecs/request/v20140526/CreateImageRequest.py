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

class CreateImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateImage','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DiskDeviceMappings(self):
		return self.get_query_params().get('DiskDeviceMapping')

	def set_DiskDeviceMappings(self, DiskDeviceMappings):
		for depth1 in range(len(DiskDeviceMappings)):
			if DiskDeviceMappings[depth1].get('SnapshotId') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(depth1 + 1) + '.SnapshotId', DiskDeviceMappings[depth1].get('SnapshotId'))
			if DiskDeviceMappings[depth1].get('Size') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(depth1 + 1) + '.Size', DiskDeviceMappings[depth1].get('Size'))
			if DiskDeviceMappings[depth1].get('DiskType') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(depth1 + 1) + '.DiskType', DiskDeviceMappings[depth1].get('DiskType'))
			if DiskDeviceMappings[depth1].get('Device') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(depth1 + 1) + '.Device', DiskDeviceMappings[depth1].get('Device'))

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

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Platform(self):
		return self.get_query_params().get('Platform')

	def set_Platform(self,Platform):
		self.add_query_param('Platform',Platform)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_ImageName(self):
		return self.get_query_params().get('ImageName')

	def set_ImageName(self,ImageName):
		self.add_query_param('ImageName',ImageName)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_Architecture(self):
		return self.get_query_params().get('Architecture')

	def set_Architecture(self,Architecture):
		self.add_query_param('Architecture',Architecture)

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

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_ImageFamily(self):
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self,ImageFamily):
		self.add_query_param('ImageFamily',ImageFamily)

	def get_ImageVersion(self):
		return self.get_query_params().get('ImageVersion')

	def set_ImageVersion(self,ImageVersion):
		self.add_query_param('ImageVersion',ImageVersion)