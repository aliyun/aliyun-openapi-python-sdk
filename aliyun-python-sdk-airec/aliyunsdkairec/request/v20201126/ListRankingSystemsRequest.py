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

class ListRankingSystemsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2020-11-26', 'ListRankingSystems','airec')
		self.set_uri_pattern('/v2/openapi/instances/[instanceId]/ranking-systems')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_instanceId(self): # String
		return self.get_path_params().get('instanceId')

	def set_instanceId(self, instanceId):  # String
		self.add_path_param('instanceId', instanceId)
	def get_size(self): # Long
		return self.get_query_params().get('size')

	def set_size(self, size):  # Long
		self.add_query_param('size', size)
	def get_name(self): # String
		return self.get_query_params().get('name')

	def set_name(self, name):  # String
		self.add_query_param('name', name)
	def get_deployStatus(self): # String
		return self.get_query_params().get('deployStatus')

	def set_deployStatus(self, deployStatus):  # String
		self.add_query_param('deployStatus', deployStatus)
	def get_page(self): # Long
		return self.get_query_params().get('page')

	def set_page(self, page):  # Long
		self.add_query_param('page', page)
