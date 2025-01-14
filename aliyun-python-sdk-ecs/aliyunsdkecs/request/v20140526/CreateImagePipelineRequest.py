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

class CreateImagePipelineRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateImagePipeline','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BaseImageType(self): # String
		return self.get_query_params().get('BaseImageType')

	def set_BaseImageType(self, BaseImageType):  # String
		self.add_query_param('BaseImageType', BaseImageType)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ToRegionIds(self): # RepeatList
		return self.get_query_params().get('ToRegionId')

	def set_ToRegionIds(self, ToRegionId):  # RepeatList
		for depth1 in range(len(ToRegionId)):
			self.add_query_param('ToRegionId.' + str(depth1 + 1), ToRegionId[depth1])
	def get_InternetMaxBandwidthOut(self): # Integer
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):  # Integer
		self.add_query_param('InternetMaxBandwidthOut', InternetMaxBandwidthOut)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
	def get_SystemDiskSize(self): # Integer
		return self.get_query_params().get('SystemDiskSize')

	def set_SystemDiskSize(self, SystemDiskSize):  # Integer
		self.add_query_param('SystemDiskSize', SystemDiskSize)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
	def get_AdvancedOptions(self): # Struct
		return self.get_query_params().get('AdvancedOptions')

	def set_AdvancedOptions(self, AdvancedOptions):  # Struct
		if AdvancedOptions.get('RetainCloudAssistant') is not None:
			self.add_query_param('AdvancedOptions.RetainCloudAssistant', AdvancedOptions.get('RetainCloudAssistant'))
		if AdvancedOptions.get('SkipBuildImage') is not None:
			self.add_query_param('AdvancedOptions.SkipBuildImage', AdvancedOptions.get('SkipBuildImage'))
		if AdvancedOptions.get('SkipCheckImage') is not None:
			self.add_query_param('AdvancedOptions.SkipCheckImage', AdvancedOptions.get('SkipCheckImage'))
	def get_NvmeSupport(self): # String
		return self.get_query_params().get('NvmeSupport')

	def set_NvmeSupport(self, NvmeSupport):  # String
		self.add_query_param('NvmeSupport', NvmeSupport)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_RepairMode(self): # String
		return self.get_query_params().get('RepairMode')

	def set_RepairMode(self, RepairMode):  # String
		self.add_query_param('RepairMode', RepairMode)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_BaseImage(self): # String
		return self.get_query_params().get('BaseImage')

	def set_BaseImage(self, BaseImage):  # String
		self.add_query_param('BaseImage', BaseImage)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_AddAccounts(self): # RepeatList
		return self.get_query_params().get('AddAccount')

	def set_AddAccounts(self, AddAccount):  # RepeatList
		for depth1 in range(len(AddAccount)):
			self.add_query_param('AddAccount.' + str(depth1 + 1), AddAccount[depth1])
	def get_DeleteInstanceOnFailure(self): # Boolean
		return self.get_query_params().get('DeleteInstanceOnFailure')

	def set_DeleteInstanceOnFailure(self, DeleteInstanceOnFailure):  # Boolean
		self.add_query_param('DeleteInstanceOnFailure', DeleteInstanceOnFailure)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ImageFamily(self): # String
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self, ImageFamily):  # String
		self.add_query_param('ImageFamily', ImageFamily)
	def get_BuildContent(self): # String
		return self.get_query_params().get('BuildContent')

	def set_BuildContent(self, BuildContent):  # String
		self.add_query_param('BuildContent', BuildContent)
	def get_ImportImageOptions(self): # Struct
		return self.get_query_params().get('ImportImageOptions')

	def set_ImportImageOptions(self, ImportImageOptions):  # Struct
		if ImportImageOptions.get('Architecture') is not None:
			self.add_query_param('ImportImageOptions.Architecture', ImportImageOptions.get('Architecture'))
		if ImportImageOptions.get('OSType') is not None:
			self.add_query_param('ImportImageOptions.OSType', ImportImageOptions.get('OSType'))
		if ImportImageOptions.get('Platform') is not None:
			self.add_query_param('ImportImageOptions.Platform', ImportImageOptions.get('Platform'))
		if ImportImageOptions.get('BootMode') is not None:
			self.add_query_param('ImportImageOptions.BootMode', ImportImageOptions.get('BootMode'))
		if ImportImageOptions.get('LicenseType') is not None:
			self.add_query_param('ImportImageOptions.LicenseType', ImportImageOptions.get('LicenseType'))
		if ImportImageOptions.get('DiskDeviceMappings') is not None:
			for index1, value1 in enumerate(ImportImageOptions.get('DiskDeviceMappings')):
				if value1.get('OSSBucket') is not None:
					self.add_query_param('ImportImageOptions.DiskDeviceMappings.' + str(index1 + 1) + '.OSSBucket', value1.get('OSSBucket'))
				if value1.get('OSSObject') is not None:
					self.add_query_param('ImportImageOptions.DiskDeviceMappings.' + str(index1 + 1) + '.OSSObject', value1.get('OSSObject'))
				if value1.get('Format') is not None:
					self.add_query_param('ImportImageOptions.DiskDeviceMappings.' + str(index1 + 1) + '.Format', value1.get('Format'))
				if value1.get('DiskImageSize') is not None:
					self.add_query_param('ImportImageOptions.DiskDeviceMappings.' + str(index1 + 1) + '.DiskImageSize', value1.get('DiskImageSize'))
		if ImportImageOptions.get('Features') is not None:
			if ImportImageOptions.get('Features').get('NvmeSupport') is not None:
				self.add_query_param('ImportImageOptions.Features.NvmeSupport', ImportImageOptions.get('Features').get('NvmeSupport'))
		if ImportImageOptions.get('RetainImportedImage') is not None:
			self.add_query_param('ImportImageOptions.RetainImportedImage', ImportImageOptions.get('RetainImportedImage'))
	def get_TestContent(self): # String
		return self.get_query_params().get('TestContent')

	def set_TestContent(self, TestContent):  # String
		self.add_query_param('TestContent', TestContent)
