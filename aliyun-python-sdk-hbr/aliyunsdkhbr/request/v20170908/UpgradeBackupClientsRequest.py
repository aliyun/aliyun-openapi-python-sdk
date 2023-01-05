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
from aliyunsdkhbr.endpoint import endpoint_data

class UpgradeBackupClientsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpgradeBackupClients')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CrossAccountType(self): # String
		return self.get_query_params().get('CrossAccountType')

	def set_CrossAccountType(self, CrossAccountType):  # String
		self.add_query_param('CrossAccountType', CrossAccountType)
	def get_CrossAccountRoleName(self): # String
		return self.get_query_params().get('CrossAccountRoleName')

	def set_CrossAccountRoleName(self, CrossAccountRoleName):  # String
		self.add_query_param('CrossAccountRoleName', CrossAccountRoleName)
	def get_ClientIds(self): # String
		return self.get_query_params().get('ClientIds')

	def set_ClientIds(self, ClientIds):  # String
		self.add_query_param('ClientIds', ClientIds)
	def get_InstanceIds(self): # String
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # String
		self.add_query_param('InstanceIds', InstanceIds)
	def get_CrossAccountUserId(self): # Long
		return self.get_query_params().get('CrossAccountUserId')

	def set_CrossAccountUserId(self, CrossAccountUserId):  # Long
		self.add_query_param('CrossAccountUserId', CrossAccountUserId)
