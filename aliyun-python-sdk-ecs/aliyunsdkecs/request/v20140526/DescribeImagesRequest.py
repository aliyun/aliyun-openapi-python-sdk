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

	def get_ActionType(self): # String
		return self.get_query_params().get('ActionType')

	def set_ActionType(self, ActionType):  # String
		self.add_query_param('ActionType', ActionType)
	def get_ImageOwnerId(self): # Long
		return self.get_query_params().get('ImageOwnerId')

	def set_ImageOwnerId(self, ImageOwnerId):  # Long
		self.add_query_param('ImageOwnerId', ImageOwnerId)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_SnapshotId(self): # String
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self, SnapshotId):  # String
		self.add_query_param('SnapshotId', SnapshotId)
	def get_Usage(self): # String
		return self.get_query_params().get('Usage')

	def set_Usage(self, Usage):  # String
		self.add_query_param('Usage', Usage)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ImageOwnerAlias(self): # String
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self, ImageOwnerAlias):  # String
		self.add_query_param('ImageOwnerAlias', ImageOwnerAlias)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_IsSupportIoOptimized(self): # Boolean
		return self.get_query_params().get('IsSupportIoOptimized')

	def set_IsSupportIoOptimized(self, IsSupportIoOptimized):  # Boolean
		self.add_query_param('IsSupportIoOptimized', IsSupportIoOptimized)
	def get_ImageName(self): # String
		return self.get_query_params().get('ImageName')

	def set_ImageName(self, ImageName):  # String
		self.add_query_param('ImageName', ImageName)
	def get_IsSupportCloudinit(self): # Boolean
		return self.get_query_params().get('IsSupportCloudinit')

	def set_IsSupportCloudinit(self, IsSupportCloudinit):  # Boolean
		self.add_query_param('IsSupportCloudinit', IsSupportCloudinit)
	def get_IsPublic(self): # Boolean
		return self.get_query_params().get('IsPublic')

	def set_IsPublic(self, IsPublic):  # Boolean
		self.add_query_param('IsPublic', IsPublic)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.value', Tag[depth1].get('value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_Architecture(self): # String
		return self.get_query_params().get('Architecture')

	def set_Architecture(self, Architecture):  # String
		self.add_query_param('Architecture', Architecture)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_ShowExpired(self): # Boolean
		return self.get_query_params().get('ShowExpired')

	def set_ShowExpired(self, ShowExpired):  # Boolean
		self.add_query_param('ShowExpired', ShowExpired)
	def get_OSType(self): # String
		return self.get_query_params().get('OSType')

	def set_OSType(self, OSType):  # String
		self.add_query_param('OSType', OSType)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Filters(self): # RepeatList
		return self.get_query_params().get('Filter')

	def set_Filters(self, Filter):  # RepeatList
		for depth1 in range(len(Filter)):
			if Filter[depth1].get('Value') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.Value', Filter[depth1].get('Value'))
			if Filter[depth1].get('Key') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.Key', Filter[depth1].get('Key'))
	def get_ImageFamily(self): # String
		return self.get_query_params().get('ImageFamily')

	def set_ImageFamily(self, ImageFamily):  # String
		self.add_query_param('ImageFamily', ImageFamily)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
