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

class CreateNetworkChannelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'CreateNetworkChannel','polardb')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Notes(self): # String
		return self.get_query_params().get('Notes')

	def set_Notes(self, Notes):  # String
		self.add_query_param('Notes', Notes)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TargetIp(self): # String
		return self.get_query_params().get('TargetIp')

	def set_TargetIp(self, TargetIp):  # String
		self.add_query_param('TargetIp', TargetIp)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_TargetPort(self): # String
		return self.get_query_params().get('TargetPort')

	def set_TargetPort(self, TargetPort):  # String
		self.add_query_param('TargetPort', TargetPort)
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
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ChannelName(self): # String
		return self.get_query_params().get('ChannelName')

	def set_ChannelName(self, ChannelName):  # String
		self.add_query_param('ChannelName', ChannelName)
	def get_TargetDBClusterId(self): # String
		return self.get_query_params().get('TargetDBClusterId')

	def set_TargetDBClusterId(self, TargetDBClusterId):  # String
		self.add_query_param('TargetDBClusterId', TargetDBClusterId)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
