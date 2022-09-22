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
from aliyunsdkga.endpoint import endpoint_data

class DissociateAdditionalCertificatesFromListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'DissociateAdditionalCertificatesFromListener','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Domainss(self): # RepeatList
		return self.get_query_params().get('Domains')

	def set_Domainss(self, Domains):  # RepeatList
		for depth1 in range(len(Domains)):
			self.add_query_param('Domains.' + str(depth1 + 1), Domains[depth1])
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_AcceleratorId(self): # String
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self, AcceleratorId):  # String
		self.add_query_param('AcceleratorId', AcceleratorId)
