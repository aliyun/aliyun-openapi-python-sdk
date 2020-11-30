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

class DescribeSnapshotsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeSnapshots','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Filter2Value(self):
		return self.get_query_params().get('Filter.2.Value')

	def set_Filter2Value(self,Filter2Value):
		self.add_query_param('Filter.2.Value',Filter2Value)

	def get_SnapshotIds(self):
		return self.get_query_params().get('SnapshotIds')

	def set_SnapshotIds(self,SnapshotIds):
		self.add_query_param('SnapshotIds',SnapshotIds)

	def get_Usage(self):
		return self.get_query_params().get('Usage')

	def set_Usage(self,Usage):
		self.add_query_param('Usage',Usage)

	def get_SnapshotLinkId(self):
		return self.get_query_params().get('SnapshotLinkId')

	def set_SnapshotLinkId(self,SnapshotLinkId):
		self.add_query_param('SnapshotLinkId',SnapshotLinkId)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_Filter1Key(self):
		return self.get_query_params().get('Filter.1.Key')

	def set_Filter1Key(self,Filter1Key):
		self.add_query_param('Filter.1.Key',Filter1Key)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_Filter1Value(self):
		return self.get_query_params().get('Filter.1.Value')

	def set_Filter1Value(self,Filter1Value):
		self.add_query_param('Filter.1.Value',Filter1Value)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)

	def get_SnapshotName(self):
		return self.get_query_params().get('SnapshotName')

	def set_SnapshotName(self,SnapshotName):
		self.add_query_param('SnapshotName',SnapshotName)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_DiskId(self):
		return self.get_query_params().get('DiskId')

	def set_DiskId(self,DiskId):
		self.add_query_param('DiskId',DiskId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_SourceDiskType(self):
		return self.get_query_params().get('SourceDiskType')

	def set_SourceDiskType(self,SourceDiskType):
		self.add_query_param('SourceDiskType',SourceDiskType)

	def get_Filter2Key(self):
		return self.get_query_params().get('Filter.2.Key')

	def set_Filter2Key(self,Filter2Key):
		self.add_query_param('Filter.2.Key',Filter2Key)

	def get_Encrypted(self):
		return self.get_query_params().get('Encrypted')

	def set_Encrypted(self,Encrypted):
		self.add_query_param('Encrypted',Encrypted)

	def get_SnapshotType(self):
		return self.get_query_params().get('SnapshotType')

	def set_SnapshotType(self,SnapshotType):
		self.add_query_param('SnapshotType',SnapshotType)

	def get_KMSKeyId(self):
		return self.get_query_params().get('KMSKeyId')

	def set_KMSKeyId(self,KMSKeyId):
		self.add_query_param('KMSKeyId',KMSKeyId)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)