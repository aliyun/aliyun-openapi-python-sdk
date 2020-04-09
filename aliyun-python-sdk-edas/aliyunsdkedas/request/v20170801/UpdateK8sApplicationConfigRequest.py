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
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UpdateK8sApplicationConfig','edas')
		self.set_uri_pattern('/pop/v5/k8s/acs/k8s_app_configuration')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_MemoryLimit(self):
		return self.get_query_params().get('MemoryLimit')

	def set_MemoryLimit(self,MemoryLimit):
		self.add_query_param('MemoryLimit',MemoryLimit)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_CpuLimit(self):
		return self.get_query_params().get('CpuLimit')

	def set_CpuLimit(self,CpuLimit):
		self.add_query_param('CpuLimit',CpuLimit)

	def get_McpuLimit(self):
		return self.get_query_params().get('McpuLimit')

	def set_McpuLimit(self,McpuLimit):
		self.add_query_param('McpuLimit',McpuLimit)