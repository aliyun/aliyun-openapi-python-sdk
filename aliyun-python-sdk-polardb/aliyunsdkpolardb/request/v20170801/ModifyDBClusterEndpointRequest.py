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

class ModifyDBClusterEndpointRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'ModifyDBClusterEndpoint','polardb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AutoAddNewNodes(self): # String
		return self.get_query_params().get('AutoAddNewNodes')

	def set_AutoAddNewNodes(self, AutoAddNewNodes):  # String
		self.add_query_param('AutoAddNewNodes', AutoAddNewNodes)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DBEndpointId(self): # String
		return self.get_query_params().get('DBEndpointId')

	def set_DBEndpointId(self, DBEndpointId):  # String
		self.add_query_param('DBEndpointId', DBEndpointId)
	def get_PolarSccWaitTimeout(self): # String
		return self.get_query_params().get('PolarSccWaitTimeout')

	def set_PolarSccWaitTimeout(self, PolarSccWaitTimeout):  # String
		self.add_query_param('PolarSccWaitTimeout', PolarSccWaitTimeout)
	def get_ReadWriteMode(self): # String
		return self.get_query_params().get('ReadWriteMode')

	def set_ReadWriteMode(self, ReadWriteMode):  # String
		self.add_query_param('ReadWriteMode', ReadWriteMode)
	def get_PolarSccTimeoutAction(self): # String
		return self.get_query_params().get('PolarSccTimeoutAction')

	def set_PolarSccTimeoutAction(self, PolarSccTimeoutAction):  # String
		self.add_query_param('PolarSccTimeoutAction', PolarSccTimeoutAction)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_EndpointConfig(self): # String
		return self.get_query_params().get('EndpointConfig')

	def set_EndpointConfig(self, EndpointConfig):  # String
		self.add_query_param('EndpointConfig', EndpointConfig)
	def get_DBEndpointDescription(self): # String
		return self.get_query_params().get('DBEndpointDescription')

	def set_DBEndpointDescription(self, DBEndpointDescription):  # String
		self.add_query_param('DBEndpointDescription', DBEndpointDescription)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Nodes(self): # String
		return self.get_query_params().get('Nodes')

	def set_Nodes(self, Nodes):  # String
		self.add_query_param('Nodes', Nodes)
	def get_SccMode(self): # String
		return self.get_query_params().get('SccMode')

	def set_SccMode(self, SccMode):  # String
		self.add_query_param('SccMode', SccMode)
