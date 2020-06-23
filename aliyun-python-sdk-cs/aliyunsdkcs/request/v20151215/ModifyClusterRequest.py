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
from aliyunsdkcs.endpoint import endpoint_data

class ModifyClusterRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'CS', '2015-12-15', 'ModifyCluster')
		self.set_uri_pattern('/api/v2/clusters/[ClusterId]')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_api_server_eip(self):
		return self.get_body_params().get('api_server_eip')

	def set_api_server_eip(self,api_server_eip):
		self.add_body_params('api_server_eip', api_server_eip)

	def get_resource_group_id(self):
		return self.get_body_params().get('resource_group_id')

	def set_resource_group_id(self,resource_group_id):
		self.add_body_params('resource_group_id', resource_group_id)

	def get_ingress_domain_rebinding(self):
		return self.get_body_params().get('ingress_domain_rebinding')

	def set_ingress_domain_rebinding(self,ingress_domain_rebinding):
		self.add_body_params('ingress_domain_rebinding', ingress_domain_rebinding)

	def get_deletion_protection(self):
		return self.get_body_params().get('deletion_protection')

	def set_deletion_protection(self,deletion_protection):
		self.add_body_params('deletion_protection', deletion_protection)

	def get_ingress_loadbalancer_id(self):
		return self.get_body_params().get('ingress_loadbalancer_id')

	def set_ingress_loadbalancer_id(self,ingress_loadbalancer_id):
		self.add_body_params('ingress_loadbalancer_id', ingress_loadbalancer_id)

	def get_ClusterId(self):
		return self.get_path_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_path_param('ClusterId',ClusterId)

	def get_api_server_eip_id(self):
		return self.get_body_params().get('api_server_eip_id')

	def set_api_server_eip_id(self,api_server_eip_id):
		self.add_body_params('api_server_eip_id', api_server_eip_id)