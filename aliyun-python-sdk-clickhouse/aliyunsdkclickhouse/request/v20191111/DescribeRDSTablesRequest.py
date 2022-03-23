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

class DescribeRDSTablesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'clickhouse', '2019-11-11', 'DescribeRDSTables')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Schema(self): # String
		return self.get_query_params().get('Schema')

	def set_Schema(self, Schema):  # String
		self.add_query_param('Schema', Schema)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_RdsPassword(self): # String
		return self.get_query_params().get('RdsPassword')

	def set_RdsPassword(self, RdsPassword):  # String
		self.add_query_param('RdsPassword', RdsPassword)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DbClusterId(self): # String
		return self.get_query_params().get('DbClusterId')

	def set_DbClusterId(self, DbClusterId):  # String
		self.add_query_param('DbClusterId', DbClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_RdsId(self): # String
		return self.get_query_params().get('RdsId')

	def set_RdsId(self, RdsId):  # String
		self.add_query_param('RdsId', RdsId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_RdsPort(self): # Long
		return self.get_query_params().get('RdsPort')

	def set_RdsPort(self, RdsPort):  # Long
		self.add_query_param('RdsPort', RdsPort)
	def get_RdsVpcUrl(self): # String
		return self.get_query_params().get('RdsVpcUrl')

	def set_RdsVpcUrl(self, RdsVpcUrl):  # String
		self.add_query_param('RdsVpcUrl', RdsVpcUrl)
	def get_RdsUserName(self): # String
		return self.get_query_params().get('RdsUserName')

	def set_RdsUserName(self, RdsUserName):  # String
		self.add_query_param('RdsUserName', RdsUserName)
