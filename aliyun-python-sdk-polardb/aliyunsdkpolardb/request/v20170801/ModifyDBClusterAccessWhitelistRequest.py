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

class ModifyDBClusterAccessWhitelistRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'ModifyDBClusterAccessWhitelist','polardb')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SecurityIps(self):
		return self.get_query_params().get('SecurityIps')

	def set_SecurityIps(self,SecurityIps):
		self.add_query_param('SecurityIps',SecurityIps)

	def get_DBClusterIPArrayAttribute(self):
		return self.get_query_params().get('DBClusterIPArrayAttribute')

	def set_DBClusterIPArrayAttribute(self,DBClusterIPArrayAttribute):
		self.add_query_param('DBClusterIPArrayAttribute',DBClusterIPArrayAttribute)

	def get_ModifyMode(self):
		return self.get_query_params().get('ModifyMode')

	def set_ModifyMode(self,ModifyMode):
		self.add_query_param('ModifyMode',ModifyMode)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_DBClusterId(self):
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self,DBClusterId):
		self.add_query_param('DBClusterId',DBClusterId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_WhiteListType(self):
		return self.get_query_params().get('WhiteListType')

	def set_WhiteListType(self,WhiteListType):
		self.add_query_param('WhiteListType',WhiteListType)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SecurityGroupIds(self):
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIds(self,SecurityGroupIds):
		self.add_query_param('SecurityGroupIds',SecurityGroupIds)

	def get_DBClusterIPArrayName(self):
		return self.get_query_params().get('DBClusterIPArrayName')

	def set_DBClusterIPArrayName(self,DBClusterIPArrayName):
		self.add_query_param('DBClusterIPArrayName',DBClusterIPArrayName)