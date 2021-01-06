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
from aliyunsdksas.endpoint import endpoint_data

class StartImageVulScanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'StartImageVulScan','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RepoId(self):
		return self.get_query_params().get('RepoId')

	def set_RepoId(self,RepoId):
		self.add_query_param('RepoId',RepoId)

	def get_RepoNamespace(self):
		return self.get_query_params().get('RepoNamespace')

	def set_RepoNamespace(self,RepoNamespace):
		self.add_query_param('RepoNamespace',RepoNamespace)

	def get_ImageDigest(self):
		return self.get_query_params().get('ImageDigest')

	def set_ImageDigest(self,ImageDigest):
		self.add_query_param('ImageDigest',ImageDigest)

	def get_RepName(self):
		return self.get_query_params().get('RepName')

	def set_RepName(self,RepName):
		self.add_query_param('RepName',RepName)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_ImageTag(self):
		return self.get_query_params().get('ImageTag')

	def set_ImageTag(self,ImageTag):
		self.add_query_param('ImageTag',ImageTag)

	def get_RegistryTypess(self):
		return self.get_query_params().get('RegistryTypes')

	def set_RegistryTypess(self, RegistryTypess):
		for depth1 in range(len(RegistryTypess)):
			if RegistryTypess[depth1] is not None:
				self.add_query_param('RegistryTypes.' + str(depth1 + 1) , RegistryTypess[depth1])

	def get_RepoInstanceId(self):
		return self.get_query_params().get('RepoInstanceId')

	def set_RepoInstanceId(self,RepoInstanceId):
		self.add_query_param('RepoInstanceId',RepoInstanceId)

	def get_ImageLayer(self):
		return self.get_query_params().get('ImageLayer')

	def set_ImageLayer(self,ImageLayer):
		self.add_query_param('ImageLayer',ImageLayer)

	def get_RepoRegionId(self):
		return self.get_query_params().get('RepoRegionId')

	def set_RepoRegionId(self,RepoRegionId):
		self.add_query_param('RepoRegionId',RepoRegionId)