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
from aliyunsdkclickhouse.endpoint import endpoint_data

class TransferVersionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'clickhouse', '2019-11-11', 'TransferVersion','service')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_SourceAccount(self): # String
		return self.get_query_params().get('SourceAccount')

	def set_SourceAccount(self, SourceAccount):  # String
		self.add_query_param('SourceAccount', SourceAccount)
	def get_TargetAccount(self): # String
		return self.get_query_params().get('TargetAccount')

	def set_TargetAccount(self, TargetAccount):  # String
		self.add_query_param('TargetAccount', TargetAccount)
	def get_SourceClusterName(self): # String
		return self.get_query_params().get('SourceClusterName')

	def set_SourceClusterName(self, SourceClusterName):  # String
		self.add_query_param('SourceClusterName', SourceClusterName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_SourcePassword(self): # String
		return self.get_query_params().get('SourcePassword')

	def set_SourcePassword(self, SourcePassword):  # String
		self.add_query_param('SourcePassword', SourcePassword)
	def get_DisableWriteWindows(self): # String
		return self.get_query_params().get('DisableWriteWindows')

	def set_DisableWriteWindows(self, DisableWriteWindows):  # String
		self.add_query_param('DisableWriteWindows', DisableWriteWindows)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_TargetPassword(self): # String
		return self.get_query_params().get('TargetPassword')

	def set_TargetPassword(self, TargetPassword):  # String
		self.add_query_param('TargetPassword', TargetPassword)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TargetDbClusterId(self): # String
		return self.get_query_params().get('TargetDbClusterId')

	def set_TargetDbClusterId(self, TargetDbClusterId):  # String
		self.add_query_param('TargetDbClusterId', TargetDbClusterId)
	def get_SourceShards(self): # String
		return self.get_query_params().get('SourceShards')

	def set_SourceShards(self, SourceShards):  # String
		self.add_query_param('SourceShards', SourceShards)
