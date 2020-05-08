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
from aliyunsdkmts.endpoint import endpoint_data

class QueryMediaListByURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'QueryMediaListByURL')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_IncludeSummaryList(self):
		return self.get_query_params().get('IncludeSummaryList')

	def set_IncludeSummaryList(self,IncludeSummaryList):
		self.add_query_param('IncludeSummaryList',IncludeSummaryList)

	def get_FileURLs(self):
		return self.get_query_params().get('FileURLs')

	def set_FileURLs(self,FileURLs):
		self.add_query_param('FileURLs',FileURLs)

	def get_IncludePlayList(self):
		return self.get_query_params().get('IncludePlayList')

	def set_IncludePlayList(self,IncludePlayList):
		self.add_query_param('IncludePlayList',IncludePlayList)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_IncludeSnapshotList(self):
		return self.get_query_params().get('IncludeSnapshotList')

	def set_IncludeSnapshotList(self,IncludeSnapshotList):
		self.add_query_param('IncludeSnapshotList',IncludeSnapshotList)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_IncludeMediaInfo(self):
		return self.get_query_params().get('IncludeMediaInfo')

	def set_IncludeMediaInfo(self,IncludeMediaInfo):
		self.add_query_param('IncludeMediaInfo',IncludeMediaInfo)