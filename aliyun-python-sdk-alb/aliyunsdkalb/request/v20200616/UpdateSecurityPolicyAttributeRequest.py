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
from aliyunsdkalb.endpoint import endpoint_data

class UpdateSecurityPolicyAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'UpdateSecurityPolicyAttribute','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Ciphers(self): # Array
		return self.get_query_params().get('Ciphers')

	def set_Ciphers(self, Ciphers):  # Array
		for index1, value1 in enumerate(Ciphers):
			self.add_query_param('Ciphers.' + str(index1 + 1), value1)
	def get_TLSVersions(self): # Array
		return self.get_query_params().get('TLSVersions')

	def set_TLSVersions(self, TLSVersions):  # Array
		for index1, value1 in enumerate(TLSVersions):
			self.add_query_param('TLSVersions.' + str(index1 + 1), value1)
	def get_SecurityPolicyName(self): # String
		return self.get_query_params().get('SecurityPolicyName')

	def set_SecurityPolicyName(self, SecurityPolicyName):  # String
		self.add_query_param('SecurityPolicyName', SecurityPolicyName)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_SecurityPolicyId(self): # String
		return self.get_query_params().get('SecurityPolicyId')

	def set_SecurityPolicyId(self, SecurityPolicyId):  # String
		self.add_query_param('SecurityPolicyId', SecurityPolicyId)
