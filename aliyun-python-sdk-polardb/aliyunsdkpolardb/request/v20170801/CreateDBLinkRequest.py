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

class CreateDBLinkRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'CreateDBLink','polardb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_SourceDBName(self): # String
		return self.get_query_params().get('SourceDBName')

	def set_SourceDBName(self, SourceDBName):  # String
		self.add_query_param('SourceDBName', SourceDBName)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TargetDBName(self): # String
		return self.get_query_params().get('TargetDBName')

	def set_TargetDBName(self, TargetDBName):  # String
		self.add_query_param('TargetDBName', TargetDBName)
	def get_TargetIp(self): # String
		return self.get_query_params().get('TargetIp')

	def set_TargetIp(self, TargetIp):  # String
		self.add_query_param('TargetIp', TargetIp)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_DBLinkName(self): # String
		return self.get_query_params().get('DBLinkName')

	def set_DBLinkName(self, DBLinkName):  # String
		self.add_query_param('DBLinkName', DBLinkName)
	def get_TargetPort(self): # String
		return self.get_query_params().get('TargetPort')

	def set_TargetPort(self, TargetPort):  # String
		self.add_query_param('TargetPort', TargetPort)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_TargetDBInstanceName(self): # String
		return self.get_query_params().get('TargetDBInstanceName')

	def set_TargetDBInstanceName(self, TargetDBInstanceName):  # String
		self.add_query_param('TargetDBInstanceName', TargetDBInstanceName)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_TargetDBPasswd(self): # String
		return self.get_query_params().get('TargetDBPasswd')

	def set_TargetDBPasswd(self, TargetDBPasswd):  # String
		self.add_query_param('TargetDBPasswd', TargetDBPasswd)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TargetDBAccount(self): # String
		return self.get_query_params().get('TargetDBAccount')

	def set_TargetDBAccount(self, TargetDBAccount):  # String
		self.add_query_param('TargetDBAccount', TargetDBAccount)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
