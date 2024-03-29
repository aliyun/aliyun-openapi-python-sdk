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
from aliyunsdkopensearch.endpoint import endpoint_data

class UpdateABTestExperimentRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'OpenSearch', '2017-12-25', 'UpdateABTestExperiment')
		self.set_uri_pattern('/v4/openapi/app-groups/[appGroupIdentity]/scenes/[sceneId]/groups/[groupId]/experiments/[experimentId]')
		self.set_method('PUT')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_groupId(self): # Integer
		return self.get_path_params().get('groupId')

	def set_groupId(self, groupId):  # Integer
		self.add_path_param('groupId', groupId)
	def get_sceneId(self): # Integer
		return self.get_path_params().get('sceneId')

	def set_sceneId(self, sceneId):  # Integer
		self.add_path_param('sceneId', sceneId)
	def get_experimentId(self): # Integer
		return self.get_path_params().get('experimentId')

	def set_experimentId(self, experimentId):  # Integer
		self.add_path_param('experimentId', experimentId)
	def get_appGroupIdentity(self): # String
		return self.get_path_params().get('appGroupIdentity')

	def set_appGroupIdentity(self, appGroupIdentity):  # String
		self.add_path_param('appGroupIdentity', appGroupIdentity)
