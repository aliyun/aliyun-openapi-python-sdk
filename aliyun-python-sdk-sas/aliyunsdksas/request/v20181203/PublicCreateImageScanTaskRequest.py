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

class PublicCreateImageScanTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'PublicCreateImageScanTask')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_Digests(self): # String
		return self.get_query_params().get('Digests')

	def set_Digests(self, Digests):  # String
		self.add_query_param('Digests', Digests)
	def get_RegistryTypes(self): # String
		return self.get_query_params().get('RegistryTypes')

	def set_RegistryTypes(self, RegistryTypes):  # String
		self.add_query_param('RegistryTypes', RegistryTypes)
	def get_RegionIds(self): # String
		return self.get_query_params().get('RegionIds')

	def set_RegionIds(self, RegionIds):  # String
		self.add_query_param('RegionIds', RegionIds)
	def get_Tags(self): # String
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # String
		self.add_query_param('Tags', Tags)
	def get_RepoNamespaces(self): # String
		return self.get_query_params().get('RepoNamespaces')

	def set_RepoNamespaces(self, RepoNamespaces):  # String
		self.add_query_param('RepoNamespaces', RepoNamespaces)
	def get_InstanceIds(self): # String
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # String
		self.add_query_param('InstanceIds', InstanceIds)
	def get_RepoIds(self): # String
		return self.get_query_params().get('RepoIds')

	def set_RepoIds(self, RepoIds):  # String
		self.add_query_param('RepoIds', RepoIds)
	def get_RepoNames(self): # String
		return self.get_query_params().get('RepoNames')

	def set_RepoNames(self, RepoNames):  # String
		self.add_query_param('RepoNames', RepoNames)
