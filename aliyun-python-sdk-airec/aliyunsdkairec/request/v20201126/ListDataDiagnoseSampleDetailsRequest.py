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

class ListDataDiagnoseSampleDetailsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2020-11-26', 'ListDataDiagnoseSampleDetails','airec')
		self.set_uri_pattern('/v2/openapi/instances/[instanceId]/data-diagnose-reports/sample-details')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_instanceId(self): # String
		return self.get_path_params().get('instanceId')

	def set_instanceId(self, instanceId):  # String
		self.add_path_param('instanceId', instanceId)
	def get_taskSource(self): # String
		return self.get_query_params().get('taskSource')

	def set_taskSource(self, taskSource):  # String
		self.add_query_param('taskSource', taskSource)
	def get_endTime(self): # Long
		return self.get_query_params().get('endTime')

	def set_endTime(self, endTime):  # Long
		self.add_query_param('endTime', endTime)
	def get_startTime(self): # Long
		return self.get_query_params().get('startTime')

	def set_startTime(self, startTime):  # Long
		self.add_query_param('startTime', startTime)
	def get_taskCreateTime(self): # Long
		return self.get_query_params().get('taskCreateTime')

	def set_taskCreateTime(self, taskCreateTime):  # Long
		self.add_query_param('taskCreateTime', taskCreateTime)
	def get_key(self): # String
		return self.get_query_params().get('key')

	def set_key(self, key):  # String
		self.add_query_param('key', key)
