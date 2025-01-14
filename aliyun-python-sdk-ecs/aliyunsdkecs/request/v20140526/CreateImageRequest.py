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

	def get_DiskDeviceMappings(self): # RepeatList
		return self.get_query_params().get('DiskDeviceMapping')

	def set_DiskDeviceMappings(self, DiskDeviceMapping):  # RepeatList
		for depth1 in range(len(DiskDeviceMapping)):
			if DiskDeviceMapping[depth1].get('SnapshotId') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(depth1 + 1) + '.SnapshotId', DiskDeviceMapping[depth1].get('SnapshotId'))
			if DiskDeviceMapping[depth1].get('Size') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(depth1 + 1) + '.Size', DiskDeviceMapping[depth1].get('Size'))
			if DiskDeviceMapping[depth1].get('DiskType') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(depth1 + 1) + '.DiskType', DiskDeviceMapping[depth1].get('DiskType'))
			if DiskDeviceMapping[depth1].get('Device') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(depth1 + 1) + '.Device', DiskDeviceMapping[depth1].get('Device'))
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
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Platform(self): # String
		return self.get_query_params().get('Platform')

	def set_Platform(self, Platform):  # String
		self.add_query_param('Platform', Platform)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Features(self): # Struct
		return self.get_query_params().get('Features')

	def set_Features(self, Features):  # Struct
		if Features.get('ImdsSupport') is not None:
			self.add_query_param('Features.ImdsSupport', Features.get('ImdsSupport'))
	def get_BootMode(self): # String
		return self.get_query_params().get('BootMode')

	def set_BootMode(self, BootMode):  # String
		self.add_query_param('BootMode', BootMode)
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_Architecture(self): # String
		return self.get_query_params().get('Architecture')

	def set_Architecture(self, Architecture):  # String
		self.add_query_param('Architecture', Architecture)
	def get_DetectionStrategy(self): # String
		return self.get_query_params().get('DetectionStrategy')

	def set_DetectionStrategy(self, DetectionStrategy):  # String
		self.add_query_param('DetectionStrategy', DetectionStrategy)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
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
	def get_ImageFamily(self): # String
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self, ImageFamily):  # String
		self.add_query_param('ImageFamily', ImageFamily)
	def get_ImageVersion(self): # String
		return self.get_query_params().get('ImageVersion')

	def set_ImageVersion(self, ImageVersion):  # String
		self.add_query_param('ImageVersion', ImageVersion)
