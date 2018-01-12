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
class ImportImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ImportImage','ecs')

	def get_DiskDeviceMappings(self):
		return self.get_query_params().get('DiskDeviceMappings')

	def set_DiskDeviceMappings(self,DiskDeviceMappings):
		for i in range(len(DiskDeviceMappings)):	
			if DiskDeviceMappings[i].get('Format') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.Format' , DiskDeviceMappings[i].get('Format'))
			if DiskDeviceMappings[i].get('OSSBucket') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.OSSBucket' , DiskDeviceMappings[i].get('OSSBucket'))
			if DiskDeviceMappings[i].get('OSSObject') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.OSSObject' , DiskDeviceMappings[i].get('OSSObject'))
			if DiskDeviceMappings[i].get('DiskImSize') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.DiskImSize' , DiskDeviceMappings[i].get('DiskImSize'))
			if DiskDeviceMappings[i].get('DiskImageSize') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.DiskImageSize' , DiskDeviceMappings[i].get('DiskImageSize'))
			if DiskDeviceMappings[i].get('Device') is not None:
				self.add_query_param('DiskDeviceMapping.' + str(i + 1) + '.Device' , DiskDeviceMappings[i].get('Device'))


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ImageName(self):
		return self.get_query_params().get('ImageName')

	def set_ImageName(self,ImageName):
		self.add_query_param('ImageName',ImageName)

	def get_RoleName(self):
		return self.get_query_params().get('RoleName')

	def set_RoleName(self,RoleName):
		self.add_query_param('RoleName',RoleName)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_OSType(self):
		return self.get_query_params().get('OSType')

	def set_OSType(self,OSType):
		self.add_query_param('OSType',OSType)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Platform(self):
		return self.get_query_params().get('Platform')

	def set_Platform(self,Platform):
		self.add_query_param('Platform',Platform)

	def get_Architecture(self):
		return self.get_query_params().get('Architecture')

	def set_Architecture(self,Architecture):
		self.add_query_param('Architecture',Architecture)