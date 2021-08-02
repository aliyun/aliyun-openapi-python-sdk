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
from aliyunsdkververica.endpoint import endpoint_data

class DeleteDeploymentRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'ververica', '2020-05-01', 'DeleteDeployment')
		self.set_uri_pattern('/pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]')
		self.set_method('DELETE')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_workspace(self):
		return self.get_path_params().get('workspace')

	def set_workspace(self,workspace):
		self.add_path_param('workspace',workspace)

	def get_deploymentId(self):
		return self.get_path_params().get('deploymentId')

	def set_deploymentId(self,deploymentId):
		self.add_path_param('deploymentId',deploymentId)

	def get_namespace(self):
		return self.get_path_params().get('namespace')

	def set_namespace(self,namespace):
		self.add_path_param('namespace',namespace)