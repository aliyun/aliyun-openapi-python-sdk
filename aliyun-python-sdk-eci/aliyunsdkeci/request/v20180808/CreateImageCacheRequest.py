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

class CreateImageCacheRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eci', '2018-08-08', 'CreateImageCache','eci')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_ImageCacheName(self):
		return self.get_query_params().get('ImageCacheName')

	def set_ImageCacheName(self,ImageCacheName):
		self.add_query_param('ImageCacheName',ImageCacheName)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_ImageCacheSize(self):
		return self.get_query_params().get('ImageCacheSize')

	def set_ImageCacheSize(self,ImageCacheSize):
		self.add_query_param('ImageCacheSize',ImageCacheSize)

	def get_ImageRegistryCredentials(self):
		return self.get_query_params().get('ImageRegistryCredentials')

	def set_ImageRegistryCredentials(self,ImageRegistryCredentials):
		for i in range(len(ImageRegistryCredentials)):	
			if ImageRegistryCredentials[i].get('Server') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(i + 1) + '.Server' , ImageRegistryCredentials[i].get('Server'))
			if ImageRegistryCredentials[i].get('UserName') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(i + 1) + '.UserName' , ImageRegistryCredentials[i].get('UserName'))
			if ImageRegistryCredentials[i].get('Password') is not None:
				self.add_query_param('ImageRegistryCredential.' + str(i + 1) + '.Password' , ImageRegistryCredentials[i].get('Password'))


	def get_EipInstanceId(self):
		return self.get_query_params().get('EipInstanceId')

	def set_EipInstanceId(self,EipInstanceId):
		self.add_query_param('EipInstanceId',EipInstanceId)

	def get_Images(self):
		return self.get_query_params().get('Images')

	def set_Images(self,Images):
		for i in range(len(Images)):	
			if Images[i] is not None:
				self.add_query_param('Image.' + str(i + 1) , Images[i])

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

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_RetentionDays(self):
		return self.get_query_params().get('RetentionDays')

	def set_RetentionDays(self, RetentionDays):
		self.add_query_param('RetentionDays', RetentionDays)

	def get_AutoMatchImageCache(self):
		return self.get_query_params().get('AutoMatchImageCache')

	def set_AutoMatchImageCache(self, AutoMatchImageCache):
		self.add_query_param('AutoMatchImageCache', AutoMatchImageCache)

	def get_Flash(self):
		return self.get_query_params().get("Flash")

	def set_Flash(self, Flash):
		self.add_query_param("Flash", Flash)

	def get_AcrRegistryInfos(self):
		return self.get_query_params().get('AcrRegistryInfos')

	def set_AcrRegistryInfos(self, AcrRegistryInfos):
		if AcrRegistryInfos is not None:
			for i in range(len(AcrRegistryInfos)):
				if AcrRegistryInfos[i].get('Domains') is not None:
					for j in range(len(AcrRegistryInfos[i].get('Domains'))):
						self.add_query_param('AcrRegistryInfo.' + str(i + 1) + 'Domain.' + str(j + 1),
											 AcrRegistryInfos[i].get('Domains')[j])
				if AcrRegistryInfos[i].get('InstanceName') is not None:
					self.add_query_param('AcrRegistryInfo.' + str(i + 1) + '.InstanceName',
										 AcrRegistryInfos[i].get('InstanceName'))
				if AcrRegistryInfos[i].get('InstanceId') is not None:
					self.add_query_param('AcrRegistryInfo.' + str(i + 1) + '.InstanceId',
										 AcrRegistryInfos[i].get('InstanceId'))
				if AcrRegistryInfos[i].get('RegionId') is not None:
					self.add_query_param('AcrRegistryInfo.' + str(i + 1) + '.RegionId',
										 AcrRegistryInfos[i].get('RegionId'))

