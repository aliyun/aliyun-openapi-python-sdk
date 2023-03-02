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
from aliyunsdksts.endpoint import endpoint_data

class AssumeRoleWithOIDCRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sts', '2015-04-01', 'AssumeRoleWithOIDC')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RoleArn(self): # String
		return self.get_query_params().get('RoleArn')

	def set_RoleArn(self, RoleArn):  # String
		self.add_query_param('RoleArn', RoleArn)
	def get_RoleSessionName(self): # String
		return self.get_query_params().get('RoleSessionName')

	def set_RoleSessionName(self, RoleSessionName):  # String
		self.add_query_param('RoleSessionName', RoleSessionName)
	def get_OIDCToken(self): # String
		return self.get_query_params().get('OIDCToken')

	def set_OIDCToken(self, OIDCToken):  # String
		self.add_query_param('OIDCToken', OIDCToken)
	def get_DurationSeconds(self): # Long
		return self.get_query_params().get('DurationSeconds')

	def set_DurationSeconds(self, DurationSeconds):  # Long
		self.add_query_param('DurationSeconds', DurationSeconds)
	def get_OIDCProviderArn(self): # String
		return self.get_query_params().get('OIDCProviderArn')

	def set_OIDCProviderArn(self, OIDCProviderArn):  # String
		self.add_query_param('OIDCProviderArn', OIDCProviderArn)
	def get_Policy(self): # String
		return self.get_query_params().get('Policy')

	def set_Policy(self, Policy):  # String
		self.add_query_param('Policy', Policy)
