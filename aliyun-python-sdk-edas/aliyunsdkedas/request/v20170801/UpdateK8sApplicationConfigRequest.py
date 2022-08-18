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
from aliyunsdkedas.endpoint import endpoint_data

class UpdateK8sApplicationConfigRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UpdateK8sApplicationConfig','Edas')
		self.set_uri_pattern('/pop/v5/k8s/acs/k8s_app_configuration')
		self.set_method('PUT')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MemoryRequest(self): # string
		return self.get_query_params().get('MemoryRequest')

	def set_MemoryRequest(self, MemoryRequest):  # string
		self.add_query_param('MemoryRequest', MemoryRequest)
	def get_AppId(self): # string
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # string
		self.add_query_param('AppId', AppId)
	def get_EphemeralStorageRequest(self): # string
		return self.get_query_params().get('EphemeralStorageRequest')

	def set_EphemeralStorageRequest(self, EphemeralStorageRequest):  # string
		self.add_query_param('EphemeralStorageRequest', EphemeralStorageRequest)
	def get_CpuRequest(self): # string
		return self.get_query_params().get('CpuRequest')

	def set_CpuRequest(self, CpuRequest):  # string
		self.add_query_param('CpuRequest', CpuRequest)
	def get_MemoryLimit(self): # string
		return self.get_query_params().get('MemoryLimit')

	def set_MemoryLimit(self, MemoryLimit):  # string
		self.add_query_param('MemoryLimit', MemoryLimit)
	def get_ClusterId(self): # string
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # string
		self.add_query_param('ClusterId', ClusterId)
	def get_CpuLimit(self): # string
		return self.get_query_params().get('CpuLimit')

	def set_CpuLimit(self, CpuLimit):  # string
		self.add_query_param('CpuLimit', CpuLimit)
	def get_McpuLimit(self): # string
		return self.get_query_params().get('McpuLimit')

	def set_McpuLimit(self, McpuLimit):  # string
		self.add_query_param('McpuLimit', McpuLimit)
	def get_McpuRequest(self): # string
		return self.get_query_params().get('McpuRequest')

	def set_McpuRequest(self, McpuRequest):  # string
		self.add_query_param('McpuRequest', McpuRequest)
	def get_Timeout(self): # integer
		return self.get_query_params().get('Timeout')

	def set_Timeout(self, Timeout):  # integer
		self.add_query_param('Timeout', Timeout)
	def get_EphemeralStorageLimit(self): # string
		return self.get_query_params().get('EphemeralStorageLimit')

	def set_EphemeralStorageLimit(self, EphemeralStorageLimit):  # string
		self.add_query_param('EphemeralStorageLimit', EphemeralStorageLimit)
