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
from aliyunsdkdds.endpoint import endpoint_data

class ModifySecurityIpsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dds', '2015-12-01', 'ModifySecurityIps','dds')
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

	def get_SecurityIpGroupName(self):
		return self.get_query_params().get('SecurityIpGroupName')

	def set_SecurityIpGroupName(self,SecurityIpGroupName):
		self.add_query_param('SecurityIpGroupName',SecurityIpGroupName)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_ModifyMode(self):
		return self.get_query_params().get('ModifyMode')

	def set_ModifyMode(self,ModifyMode):
		self.add_query_param('ModifyMode',ModifyMode)

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

	def get_SecurityIpGroupAttribute(self):
		return self.get_query_params().get('SecurityIpGroupAttribute')

	def set_SecurityIpGroupAttribute(self,SecurityIpGroupAttribute):
		self.add_query_param('SecurityIpGroupAttribute',SecurityIpGroupAttribute)