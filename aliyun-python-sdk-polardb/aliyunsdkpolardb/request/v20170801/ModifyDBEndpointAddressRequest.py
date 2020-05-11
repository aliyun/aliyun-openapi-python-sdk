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

class ModifyDBEndpointAddressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'ModifyDBEndpointAddress','polardb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ConnectionStringPrefix(self):
		return self.get_query_params().get('ConnectionStringPrefix')

	def set_ConnectionStringPrefix(self,ConnectionStringPrefix):
		self.add_query_param('ConnectionStringPrefix',ConnectionStringPrefix)

	def get_DBEndpointId(self):
		return self.get_query_params().get('DBEndpointId')

	def set_DBEndpointId(self,DBEndpointId):
		self.add_query_param('DBEndpointId',DBEndpointId)

	def get_PrivateZoneName(self):
		return self.get_query_params().get('PrivateZoneName')

	def set_PrivateZoneName(self,PrivateZoneName):
		self.add_query_param('PrivateZoneName',PrivateZoneName)

	def get_PrivateZoneAddressPrefix(self):
		return self.get_query_params().get('PrivateZoneAddressPrefix')

	def set_PrivateZoneAddressPrefix(self,PrivateZoneAddressPrefix):
		self.add_query_param('PrivateZoneAddressPrefix',PrivateZoneAddressPrefix)

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

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)