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

class CreateTriggerHookRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'CS', '2015-12-15', 'CreateTriggerHook')
		self.set_uri_pattern('/hook/trigger')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_cluster_id(self):
		return self.get_body_params().get('cluster_id')

	def set_cluster_id(self,cluster_id):
		self.add_body_params('cluster_id', cluster_id)

	def get_project_id(self):
		return self.get_body_params().get('project_id')

	def set_project_id(self,project_id):
		self.add_body_params('project_id', project_id)

	def get_trigger_url(self):
		return self.get_body_params().get('trigger_url')

	def set_trigger_url(self,trigger_url):
		self.add_body_params('trigger_url', trigger_url)

	def get_region_id(self):
		return self.get_body_params().get('region_id')

	def set_region_id(self,region_id):
		self.add_body_params('region_id', region_id)