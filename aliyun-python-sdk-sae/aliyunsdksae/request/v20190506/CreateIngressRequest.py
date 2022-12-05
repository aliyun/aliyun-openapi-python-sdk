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

from aliyunsdkcore.request import RoaRequest
from aliyunsdksae.endpoint import endpoint_data

class CreateIngressRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'sae', '2019-05-06', 'CreateIngress','serverless')
		self.set_uri_pattern('/pop/v1/sam/ingress/Ingress')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ListenerPort(self): # Integer
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self, ListenerPort):  # Integer
		self.add_query_param('ListenerPort', ListenerPort)
	def get_SlbId(self): # String
		return self.get_query_params().get('SlbId')

	def set_SlbId(self, SlbId):  # String
		self.add_query_param('SlbId', SlbId)
	def get_NamespaceId(self): # String
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self, NamespaceId):  # String
		self.add_query_param('NamespaceId', NamespaceId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_LoadBalanceType(self): # String
		return self.get_query_params().get('LoadBalanceType')

	def set_LoadBalanceType(self, LoadBalanceType):  # String
		self.add_query_param('LoadBalanceType', LoadBalanceType)
	def get_Rules(self): # String
		return self.get_body_params().get('Rules')

	def set_Rules(self, Rules):  # String
		self.add_body_params('Rules', Rules)
	def get_CertId(self): # String
		return self.get_query_params().get('CertId')

	def set_CertId(self, CertId):  # String
		self.add_query_param('CertId', CertId)
	def get_CertIds(self): # String
		return self.get_query_params().get('CertIds')

	def set_CertIds(self, CertIds):  # String
		self.add_query_param('CertIds', CertIds)
	def get_ListenerProtocol(self): # String
		return self.get_query_params().get('ListenerProtocol')

	def set_ListenerProtocol(self, ListenerProtocol):  # String
		self.add_query_param('ListenerProtocol', ListenerProtocol)
	def get_DefaultRule(self): # String
		return self.get_query_params().get('DefaultRule')

	def set_DefaultRule(self, DefaultRule):  # String
		self.add_query_param('DefaultRule', DefaultRule)
