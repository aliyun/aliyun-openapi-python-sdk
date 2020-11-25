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

class DescribeImagesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeImages','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ActionType(self):
		return self.get_query_params().get('ActionType')

	def set_ActionType(self,ActionType):
		self.add_query_param('ActionType',ActionType)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_Usage(self):
		return self.get_query_params().get('Usage')

	def set_Usage(self,Usage):
		self.add_query_param('Usage',Usage)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_ImageOwnerAlias(self):
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self,ImageOwnerAlias):
		self.add_query_param('ImageOwnerAlias',ImageOwnerAlias)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_IsSupportIoOptimized(self):
		return self.get_query_params().get('IsSupportIoOptimized')

	def set_IsSupportIoOptimized(self,IsSupportIoOptimized):
		self.add_query_param('IsSupportIoOptimized',IsSupportIoOptimized)

	def get_ImageName(self):
		return self.get_query_params().get('ImageName')

	def set_ImageName(self,ImageName):
		self.add_query_param('ImageName',ImageName)

	def get_IsSupportCloudinit(self):
		return self.get_query_params().get('IsSupportCloudinit')

	def set_IsSupportCloudinit(self,IsSupportCloudinit):
		self.add_query_param('IsSupportCloudinit',IsSupportCloudinit)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

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

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_ShowExpired(self):
		return self.get_query_params().get('ShowExpired')

	def set_ShowExpired(self,ShowExpired):
		self.add_query_param('ShowExpired',ShowExpired)

	def get_OSType(self):
		return self.get_query_params().get('OSType')

	def set_OSType(self,OSType):
		self.add_query_param('OSType',OSType)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Filters(self):
		return self.get_query_params().get('Filter')

	def set_Filters(self, Filters):
		for depth1 in range(len(Filters)):
			if Filters[depth1].get('Value') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.Value', Filters[depth1].get('Value'))
			if Filters[depth1].get('Key') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.Key', Filters[depth1].get('Key'))

	def get_ImageFamily(self):
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self,ImageFamily):
		self.add_query_param('ImageFamily',ImageFamily)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)