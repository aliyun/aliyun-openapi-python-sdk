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

class ListRulesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2020-11-26', 'ListRules','airec')
		self.set_uri_pattern('/v2/openapi/instances/[instanceId]/rules')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_instanceId(self): # String
		return self.get_path_params().get('instanceId')

	def set_instanceId(self, instanceId):  # String
		self.add_path_param('instanceId', instanceId)
	def get_size(self): # Integer
		return self.get_query_params().get('size')

	def set_size(self, size):  # Integer
		self.add_query_param('size', size)
	def get_ruleType(self): # String
		return self.get_query_params().get('ruleType')

	def set_ruleType(self, ruleType):  # String
		self.add_query_param('ruleType', ruleType)
	def get_sceneId(self): # String
		return self.get_query_params().get('sceneId')

	def set_sceneId(self, sceneId):  # String
		self.add_query_param('sceneId', sceneId)
	def get_endTime(self): # Long
		return self.get_query_params().get('endTime')

	def set_endTime(self, endTime):  # Long
		self.add_query_param('endTime', endTime)
	def get_page(self): # Integer
		return self.get_query_params().get('page')

	def set_page(self, page):  # Integer
		self.add_query_param('page', page)
	def get_startTime(self): # Long
		return self.get_query_params().get('startTime')

	def set_startTime(self, startTime):  # Long
		self.add_query_param('startTime', startTime)
	def get_status(self): # String
		return self.get_query_params().get('status')

	def set_status(self, status):  # String
		self.add_query_param('status', status)
