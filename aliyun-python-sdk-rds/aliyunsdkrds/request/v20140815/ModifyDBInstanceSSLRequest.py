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
from aliyunsdkrds.endpoint import endpoint_data

class ModifyDBInstanceSSLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyDBInstanceSSL')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ConnectionString(self): # String
		return self.get_query_params().get('ConnectionString')

	def set_ConnectionString(self, ConnectionString):  # String
		self.add_query_param('ConnectionString', ConnectionString)
	def get_ServerKey(self): # String
		return self.get_query_params().get('ServerKey')

	def set_ServerKey(self, ServerKey):  # String
		self.add_query_param('ServerKey', ServerKey)
	def get_ClientCrlEnabled(self): # Integer
		return self.get_query_params().get('ClientCrlEnabled')

	def set_ClientCrlEnabled(self, ClientCrlEnabled):  # Integer
		self.add_query_param('ClientCrlEnabled', ClientCrlEnabled)
	def get_ACL(self): # String
		return self.get_query_params().get('ACL')

	def set_ACL(self, ACL):  # String
		self.add_query_param('ACL', ACL)
	def get_ClientCertRevocationList(self): # String
		return self.get_query_params().get('ClientCertRevocationList')

	def set_ClientCertRevocationList(self, ClientCertRevocationList):  # String
		self.add_query_param('ClientCertRevocationList', ClientCertRevocationList)
	def get_ServerCert(self): # String
		return self.get_query_params().get('ServerCert')

	def set_ServerCert(self, ServerCert):  # String
		self.add_query_param('ServerCert', ServerCert)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_ClientCAEnabled(self): # Integer
		return self.get_query_params().get('ClientCAEnabled')

	def set_ClientCAEnabled(self, ClientCAEnabled):  # Integer
		self.add_query_param('ClientCAEnabled', ClientCAEnabled)
	def get_ClientCACert(self): # String
		return self.get_query_params().get('ClientCACert')

	def set_ClientCACert(self, ClientCACert):  # String
		self.add_query_param('ClientCACert', ClientCACert)
	def get_ReplicationACL(self): # String
		return self.get_query_params().get('ReplicationACL')

	def set_ReplicationACL(self, ReplicationACL):  # String
		self.add_query_param('ReplicationACL', ReplicationACL)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_CAType(self): # String
		return self.get_query_params().get('CAType')

	def set_CAType(self, CAType):  # String
		self.add_query_param('CAType', CAType)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SSLEnabled(self): # Integer
		return self.get_query_params().get('SSLEnabled')

	def set_SSLEnabled(self, SSLEnabled):  # Integer
		self.add_query_param('SSLEnabled', SSLEnabled)
