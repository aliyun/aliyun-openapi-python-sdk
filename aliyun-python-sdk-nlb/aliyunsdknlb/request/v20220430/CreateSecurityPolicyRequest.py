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
from aliyunsdknlb.endpoint import endpoint_data

class CreateSecurityPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Nlb', '2022-04-30', 'CreateSecurityPolicy','nlb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_Cipherss(self): # RepeatList
		return self.get_body_params().get('Ciphers')

	def set_Cipherss(self, Ciphers):  # RepeatList
		for depth1 in range(len(Ciphers)):
			self.add_body_params('Ciphers.' + str(depth1 + 1), Ciphers[depth1])
	def get_TlsVersionss(self): # RepeatList
		return self.get_body_params().get('TlsVersions')

	def set_TlsVersionss(self, TlsVersions):  # RepeatList
		for depth1 in range(len(TlsVersions)):
			self.add_body_params('TlsVersions.' + str(depth1 + 1), TlsVersions[depth1])
	def get_SecurityPolicyName(self): # String
		return self.get_body_params().get('SecurityPolicyName')

	def set_SecurityPolicyName(self, SecurityPolicyName):  # String
		self.add_body_params('SecurityPolicyName', SecurityPolicyName)
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
