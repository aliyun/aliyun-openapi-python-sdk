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
class DescribeClusterIdsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ocs', '2015-04-07', 'DescribeClusterIds')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_storageEngine(self):
		return self.get_query_params().get('storageEngine')

	def set_storageEngine(self,storageEngine):
		self.add_query_param('storageEngine',storageEngine)

	def get_regions(self):
		return self.get_query_params().get('regions')

	def set_regions(self,regions):
		self.add_query_param('regions',regions)

	def get_hasDataSource(self):
		return self.get_query_params().get('hasDataSource')

	def set_hasDataSource(self,hasDataSource):
		self.add_query_param('hasDataSource',hasDataSource)

	def get_appType(self):
		return self.get_query_params().get('appType')

	def set_appType(self,appType):
		self.add_query_param('appType',appType)