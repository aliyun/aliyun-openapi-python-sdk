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
from aliyunsdkdomain.endpoint import endpoint_data

class SaveSingleTaskForReserveDropListDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveSingleTaskForReserveDropListDomain','domain')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Dns2(self): # String
		return self.get_query_params().get('Dns2')

	def set_Dns2(self, Dns2):  # String
		self.add_query_param('Dns2', Dns2)
	def get_Dns1(self): # String
		return self.get_query_params().get('Dns1')

	def set_Dns1(self, Dns1):  # String
		self.add_query_param('Dns1', Dns1)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_ContactTemplateId(self): # String
		return self.get_query_params().get('ContactTemplateId')

	def set_ContactTemplateId(self, ContactTemplateId):  # String
		self.add_query_param('ContactTemplateId', ContactTemplateId)
