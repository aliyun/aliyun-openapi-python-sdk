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

class CopySnapshotRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CopySnapshot','ecs')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SnapshotId(self):
		return self.get_query_params().get('SnapshotId')

	def set_SnapshotId(self,SnapshotId):
		self.add_query_param('SnapshotId',SnapshotId)

	def get_DestinationRegionId(self):
		return self.get_query_params().get('DestinationRegionId')

	def set_DestinationRegionId(self,DestinationRegionId):
		self.add_query_param('DestinationRegionId',DestinationRegionId)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		for i in range(len(Tags)):	
			if Tags[i].get('Key') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Key' , Tags[i].get('Key'))
			if Tags[i].get('Value') is not None:
				self.add_query_param('Tag.' + str(i + 1) + '.Value' , Tags[i].get('Value'))


	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DestinationSnapshotName(self):
		return self.get_query_params().get('DestinationSnapshotName')

	def set_DestinationSnapshotName(self,DestinationSnapshotName):
		self.add_query_param('DestinationSnapshotName',DestinationSnapshotName)

	def get_DestinationSnapshotDescription(self):
		return self.get_query_params().get('DestinationSnapshotDescription')

	def set_DestinationSnapshotDescription(self,DestinationSnapshotDescription):
		self.add_query_param('DestinationSnapshotDescription',DestinationSnapshotDescription)

	def get_RetentionDays(self):
		return self.get_query_params().get('RetentionDays')

	def set_RetentionDays(self,RetentionDays):
		self.add_query_param('RetentionDays',RetentionDays)