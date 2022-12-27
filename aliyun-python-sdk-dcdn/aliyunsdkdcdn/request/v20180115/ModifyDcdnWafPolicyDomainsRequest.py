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
from aliyunsdkdcdn.endpoint import endpoint_data

class ModifyDcdnWafPolicyDomainsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dcdn', '2018-01-15', 'ModifyDcdnWafPolicyDomains')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PolicyId(self): # Long
		return self.get_body_params().get('PolicyId')

	def set_PolicyId(self, PolicyId):  # Long
		self.add_body_params('PolicyId', PolicyId)
	def get_BindDomains(self): # String
		return self.get_body_params().get('BindDomains')

	def set_BindDomains(self, BindDomains):  # String
		self.add_body_params('BindDomains', BindDomains)
	def get_UnbindDomains(self): # String
		return self.get_body_params().get('UnbindDomains')

	def set_UnbindDomains(self, UnbindDomains):  # String
		self.add_body_params('UnbindDomains', UnbindDomains)
