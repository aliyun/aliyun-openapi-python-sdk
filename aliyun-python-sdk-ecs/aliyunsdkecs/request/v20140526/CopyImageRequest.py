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

class CopyImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CopyImage','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_EncryptAlgorithm(self):
		return self.get_query_params().get('EncryptAlgorithm')

	def set_EncryptAlgorithm(self,EncryptAlgorithm):
		self.add_query_param('EncryptAlgorithm',EncryptAlgorithm)

	def get_DestinationRegionId(self):
		return self.get_query_params().get('DestinationRegionId')

	def set_DestinationRegionId(self,DestinationRegionId):
		self.add_query_param('DestinationRegionId',DestinationRegionId)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_DestinationImageName(self):
		return self.get_query_params().get('DestinationImageName')

	def set_DestinationImageName(self,DestinationImageName):
		self.add_query_param('DestinationImageName',DestinationImageName)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Encrypted(self):
		return self.get_query_params().get('Encrypted')

	def set_Encrypted(self,Encrypted):
		self.add_query_param('Encrypted',Encrypted)

	def get_KMSKeyId(self):
		return self.get_query_params().get('KMSKeyId')

	def set_KMSKeyId(self,KMSKeyId):
		self.add_query_param('KMSKeyId',KMSKeyId)

	def get_DestinationDescription(self):
		return self.get_query_params().get('DestinationDescription')

	def set_DestinationDescription(self,DestinationDescription):
		self.add_query_param('DestinationDescription',DestinationDescription)