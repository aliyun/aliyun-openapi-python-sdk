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
from aliyunsdksmartag.endpoint import endpoint_data

class ModifySagWifiRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'ModifySagWifi','smartag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_EncryptAlgorithm(self): # String
		return self.get_query_params().get('EncryptAlgorithm')

	def set_EncryptAlgorithm(self, EncryptAlgorithm):  # String
		self.add_query_param('EncryptAlgorithm', EncryptAlgorithm)
	def get_Channel(self): # String
		return self.get_query_params().get('Channel')

	def set_Channel(self, Channel):  # String
		self.add_query_param('Channel', Channel)
	def get_AuthenticationType(self): # String
		return self.get_query_params().get('AuthenticationType')

	def set_AuthenticationType(self, AuthenticationType):  # String
		self.add_query_param('AuthenticationType', AuthenticationType)
	def get_SSID(self): # String
		return self.get_query_params().get('SSID')

	def set_SSID(self, SSID):  # String
		self.add_query_param('SSID', SSID)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_IsBroadcast(self): # String
		return self.get_query_params().get('IsBroadcast')

	def set_IsBroadcast(self, IsBroadcast):  # String
		self.add_query_param('IsBroadcast', IsBroadcast)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_Bandwidth(self): # String
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self, Bandwidth):  # String
		self.add_query_param('Bandwidth', Bandwidth)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_IsEnable(self): # String
		return self.get_query_params().get('IsEnable')

	def set_IsEnable(self, IsEnable):  # String
		self.add_query_param('IsEnable', IsEnable)
	def get_SmartAGId(self): # String
		return self.get_query_params().get('SmartAGId')

	def set_SmartAGId(self, SmartAGId):  # String
		self.add_query_param('SmartAGId', SmartAGId)
	def get_SmartAGSn(self): # String
		return self.get_query_params().get('SmartAGSn')

	def set_SmartAGSn(self, SmartAGSn):  # String
		self.add_query_param('SmartAGSn', SmartAGSn)
	def get_IsAuth(self): # String
		return self.get_query_params().get('IsAuth')

	def set_IsAuth(self, IsAuth):  # String
		self.add_query_param('IsAuth', IsAuth)
