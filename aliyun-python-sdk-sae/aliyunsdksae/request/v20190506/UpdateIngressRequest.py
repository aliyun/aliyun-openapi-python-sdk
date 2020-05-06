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

class UpdateIngressRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'sae', '2019-05-06', 'UpdateIngress')
		self.set_uri_pattern('/pop/v1/sam/ingress/Ingress')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IngressId(self):
		return self.get_query_params().get('IngressId')

	def set_IngressId(self,IngressId):
		self.add_query_param('IngressId',IngressId)

	def get_ListenerPort(self):
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self,ListenerPort):
		self.add_query_param('ListenerPort',ListenerPort)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Rules(self):
		return self.get_query_params().get('Rules')

	def set_Rules(self,Rules):
		self.add_query_param('Rules',Rules)

	def get_CertId(self):
		return self.get_query_params().get('CertId')

	def set_CertId(self,CertId):
		self.add_query_param('CertId',CertId)

	def get_DefaultRule(self):
		return self.get_query_params().get('DefaultRule')

	def set_DefaultRule(self,DefaultRule):
		self.add_query_param('DefaultRule',DefaultRule)