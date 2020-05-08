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
from aliyunsdkfoas.endpoint import endpoint_data

class UpdateJobRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'foas', '2018-11-11', 'UpdateJob','foas')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v2/projects/[projectName]/jobs/[jobName]')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_queueName(self):
		return self.get_body_params().get('queueName')

	def set_queueName(self,queueName):
		self.add_body_params('queueName', queueName)

	def get_projectName(self):
		return self.get_path_params().get('projectName')

	def set_projectName(self,projectName):
		self.add_path_param('projectName',projectName)

	def get_code(self):
		return self.get_body_params().get('code')

	def set_code(self,code):
		self.add_body_params('code', code)

	def get_description(self):
		return self.get_body_params().get('description')

	def set_description(self,description):
		self.add_body_params('description', description)

	def get_planJson(self):
		return self.get_body_params().get('planJson')

	def set_planJson(self,planJson):
		self.add_body_params('planJson', planJson)

	def get_engineVersion(self):
		return self.get_body_params().get('engineVersion')

	def set_engineVersion(self,engineVersion):
		self.add_body_params('engineVersion', engineVersion)

	def get_clusterId(self):
		return self.get_body_params().get('clusterId')

	def set_clusterId(self,clusterId):
		self.add_body_params('clusterId', clusterId)

	def get_packages(self):
		return self.get_body_params().get('packages')

	def set_packages(self,packages):
		self.add_body_params('packages', packages)

	def get_folderId(self):
		return self.get_body_params().get('folderId')

	def set_folderId(self,folderId):
		self.add_body_params('folderId', folderId)

	def get_properties(self):
		return self.get_body_params().get('properties')

	def set_properties(self,properties):
		self.add_body_params('properties', properties)

	def get_jobName(self):
		return self.get_path_params().get('jobName')

	def set_jobName(self,jobName):
		self.add_path_param('jobName',jobName)