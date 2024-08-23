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

class CreateStorageVolumeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateStorageVolume','ens')
		self.set_method('POST')

	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_GatewayId(self): # String
		return self.get_query_params().get('GatewayId')

	def set_GatewayId(self, GatewayId):  # String
		self.add_query_param('GatewayId', GatewayId)
	def get_AuthUser(self): # String
		return self.get_query_params().get('AuthUser')

	def set_AuthUser(self, AuthUser):  # String
		self.add_query_param('AuthUser', AuthUser)
	def get_VolumeName(self): # String
		return self.get_query_params().get('VolumeName')

	def set_VolumeName(self, VolumeName):  # String
		self.add_query_param('VolumeName', VolumeName)
	def get_AuthPassword(self): # String
		return self.get_query_params().get('AuthPassword')

	def set_AuthPassword(self, AuthPassword):  # String
		self.add_query_param('AuthPassword', AuthPassword)
	def get_AuthProtocol(self): # String
		return self.get_query_params().get('AuthProtocol')

	def set_AuthProtocol(self, AuthProtocol):  # String
		self.add_query_param('AuthProtocol', AuthProtocol)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_IsEnable(self): # String
		return self.get_query_params().get('IsEnable')

	def set_IsEnable(self, IsEnable):  # String
		self.add_query_param('IsEnable', IsEnable)
	def get_IsAuth(self): # String
		return self.get_query_params().get('IsAuth')

	def set_IsAuth(self, IsAuth):  # String
		self.add_query_param('IsAuth', IsAuth)
	def get_StorageId(self): # String
		return self.get_query_params().get('StorageId')

	def set_StorageId(self, StorageId):  # String
		self.add_query_param('StorageId', StorageId)
