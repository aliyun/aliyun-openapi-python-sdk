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

class GetInstanceMetricsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'pai-dsw', '2022-01-01', 'GetInstanceMetrics')
		self.set_uri_pattern('/api/v2/instance/[InstanceId]/metrics')
		self.set_method('GET')

	def get_MetricType(self): # String
		return self.get_query_params().get('MetricType')

	def set_MetricType(self, MetricType):  # String
		self.add_query_param('MetricType', MetricType)
	def get_InstanceId(self): # String
		return self.get_path_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_path_param('InstanceId', InstanceId)
	def get_TimeStep(self): # String
		return self.get_query_params().get('TimeStep')

	def set_TimeStep(self, TimeStep):  # String
		self.add_query_param('TimeStep', TimeStep)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
