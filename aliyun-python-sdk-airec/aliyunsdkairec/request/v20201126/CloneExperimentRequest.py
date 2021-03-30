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
from aliyunsdkairec.endpoint import endpoint_data

class CloneExperimentRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2020-11-26', 'CloneExperiment','airec')
		self.set_uri_pattern('/v2/openapi/instances/[instanceId]/scenes/[sceneId]/experiments/[experimentId]/actions/clone')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_instanceId(self):
		return self.get_path_params().get('instanceId')

	def set_instanceId(self,instanceId):
		self.add_path_param('instanceId',instanceId)

	def get_dryRun(self):
		return self.get_query_params().get('dryRun')

	def set_dryRun(self,dryRun):
		self.add_query_param('dryRun',dryRun)

	def get_sceneId(self):
		return self.get_path_params().get('sceneId')

	def set_sceneId(self,sceneId):
		self.add_path_param('sceneId',sceneId)

	def get_experimentId(self):
		return self.get_path_params().get('experimentId')

	def set_experimentId(self,experimentId):
		self.add_path_param('experimentId',experimentId)