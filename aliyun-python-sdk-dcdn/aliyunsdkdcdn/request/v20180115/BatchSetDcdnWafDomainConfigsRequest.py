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

class BatchSetDcdnWafDomainConfigsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dcdn', '2018-01-15', 'BatchSetDcdnWafDomainConfigs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DomainNames(self): # String
		return self.get_body_params().get('DomainNames')

	def set_DomainNames(self, DomainNames):  # String
		self.add_body_params('DomainNames', DomainNames)
	def get_ClientIpTag(self): # String
		return self.get_body_params().get('ClientIpTag')

	def set_ClientIpTag(self, ClientIpTag):  # String
		self.add_body_params('ClientIpTag', ClientIpTag)
	def get_DefenseStatus(self): # String
		return self.get_body_params().get('DefenseStatus')

	def set_DefenseStatus(self, DefenseStatus):  # String
		self.add_body_params('DefenseStatus', DefenseStatus)
