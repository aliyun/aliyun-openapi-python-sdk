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
from aliyunsdkmaxcompute.endpoint import endpoint_data

class ListResourcesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'MaxCompute', '2022-01-04', 'ListResources')
		self.set_uri_pattern('/api/v1/projects/[projectName]/resources')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_projectName(self): # String
		return self.get_path_params().get('projectName')

	def set_projectName(self, projectName):  # String
		self.add_path_param('projectName', projectName)
	def get_marker(self): # String
		return self.get_query_params().get('marker')

	def set_marker(self, marker):  # String
		self.add_query_param('marker', marker)
	def get_name(self): # String
		return self.get_query_params().get('name')

	def set_name(self, name):  # String
		self.add_query_param('name', name)
	def get_maxItem(self): # Integer
		return self.get_query_params().get('maxItem')

	def set_maxItem(self, maxItem):  # Integer
		self.add_query_param('maxItem', maxItem)
