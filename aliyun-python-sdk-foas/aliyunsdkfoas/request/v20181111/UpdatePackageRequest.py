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

class UpdatePackageRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'foas', '2018-11-11', 'UpdatePackage','foas')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v2/projects/[projectName]/packages/[packageName]')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_projectName(self):
		return self.get_path_params().get('projectName')

	def set_projectName(self,projectName):
		self.add_path_param('projectName',projectName)

	def get_ossBucket(self):
		return self.get_body_params().get('ossBucket')

	def set_ossBucket(self,ossBucket):
		self.add_body_params('ossBucket', ossBucket)

	def get_ossOwner(self):
		return self.get_body_params().get('ossOwner')

	def set_ossOwner(self,ossOwner):
		self.add_body_params('ossOwner', ossOwner)

	def get_packageName(self):
		return self.get_path_params().get('packageName')

	def set_packageName(self,packageName):
		self.add_path_param('packageName',packageName)

	def get_ossEndpoint(self):
		return self.get_body_params().get('ossEndpoint')

	def set_ossEndpoint(self,ossEndpoint):
		self.add_body_params('ossEndpoint', ossEndpoint)

	def get_description(self):
		return self.get_body_params().get('description')

	def set_description(self,description):
		self.add_body_params('description', description)

	def get_tag(self):
		return self.get_body_params().get('tag')

	def set_tag(self,tag):
		self.add_body_params('tag', tag)

	def get_originName(self):
		return self.get_body_params().get('originName')

	def set_originName(self,originName):
		self.add_body_params('originName', originName)

	def get_ossPath(self):
		return self.get_body_params().get('ossPath')

	def set_ossPath(self,ossPath):
		self.add_body_params('ossPath', ossPath)

	def get_md5(self):
		return self.get_body_params().get('md5')

	def set_md5(self,md5):
		self.add_body_params('md5', md5)