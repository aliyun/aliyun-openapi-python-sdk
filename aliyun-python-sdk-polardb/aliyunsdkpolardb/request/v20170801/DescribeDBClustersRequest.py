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
from aliyunsdkpolardb.endpoint import endpoint_data

class DescribeDBClustersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'DescribeDBClusters','polardb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DBClusterDescription(self):
		return self.get_query_params().get('DBClusterDescription')

	def set_DBClusterDescription(self,DBClusterDescription):
		self.add_query_param('DBClusterDescription',DBClusterDescription)

	def get_DBClusterStatus(self):
		return self.get_query_params().get('DBClusterStatus')

	def set_DBClusterStatus(self,DBClusterStatus):
		self.add_query_param('DBClusterStatus',DBClusterStatus)

	def get_ConnectionString(self):
		return self.get_query_params().get('ConnectionString')

	def set_ConnectionString(self,ConnectionString):
		self.add_query_param('ConnectionString',ConnectionString)

	def get_RecentExpirationInterval(self):
		return self.get_query_params().get('RecentExpirationInterval')

	def set_RecentExpirationInterval(self,RecentExpirationInterval):
		self.add_query_param('RecentExpirationInterval',RecentExpirationInterval)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_DBNodeIds(self):
		return self.get_query_params().get('DBNodeIds')

	def set_DBNodeIds(self,DBNodeIds):
		self.add_query_param('DBNodeIds',DBNodeIds)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_RecentCreationInterval(self):
		return self.get_query_params().get('RecentCreationInterval')

	def set_RecentCreationInterval(self,RecentCreationInterval):
		self.add_query_param('RecentCreationInterval',RecentCreationInterval)

	def get_Expired(self):
		return self.get_query_params().get('Expired')

	def set_Expired(self,Expired):
		self.add_query_param('Expired',Expired)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

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

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DBType(self):
		return self.get_query_params().get('DBType')

	def set_DBType(self,DBType):
		self.add_query_param('DBType',DBType)

	def get_DBVersion(self):
		return self.get_query_params().get('DBVersion')

	def set_DBVersion(self,DBVersion):
		self.add_query_param('DBVersion',DBVersion)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)

	def get_DBClusterIds(self):
		return self.get_query_params().get('DBClusterIds')

	def set_DBClusterIds(self,DBClusterIds):
		self.add_query_param('DBClusterIds',DBClusterIds)