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
from aliyunsdksgw.endpoint import endpoint_data

class SetGatewayLDAPInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'SetGatewayLDAPInfo','hcs_sgw')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IsTls(self): # Boolean
		return self.get_query_params().get('IsTls')

	def set_IsTls(self, IsTls):  # Boolean
		self.add_query_param('IsTls', IsTls)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_RootDN(self): # String
		return self.get_query_params().get('RootDN')

	def set_RootDN(self, RootDN):  # String
		self.add_query_param('RootDN', RootDN)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_ServerIp(self): # String
		return self.get_query_params().get('ServerIp')

	def set_ServerIp(self, ServerIp):  # String
		self.add_query_param('ServerIp', ServerIp)
	def get_BaseDN(self): # String
		return self.get_query_params().get('BaseDN')

	def set_BaseDN(self, BaseDN):  # String
		self.add_query_param('BaseDN', BaseDN)
	def get_GatewayId(self): # String
		return self.get_query_params().get('GatewayId')

	def set_GatewayId(self, GatewayId):  # String
		self.add_query_param('GatewayId', GatewayId)
	def get_IsEnabled(self): # Boolean
		return self.get_query_params().get('IsEnabled')

	def set_IsEnabled(self, IsEnabled):  # Boolean
		self.add_query_param('IsEnabled', IsEnabled)
