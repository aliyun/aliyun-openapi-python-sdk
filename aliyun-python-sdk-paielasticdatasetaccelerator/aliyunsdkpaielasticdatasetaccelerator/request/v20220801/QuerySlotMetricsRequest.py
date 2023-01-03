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

class QuerySlotMetricsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'PAIElasticDatasetAccelerator', '2022-08-01', 'QuerySlotMetrics','datasetacc')
		self.set_uri_pattern('/api/v1/slots/[SlotId]/metrics/action/query')
		self.set_method('POST')

	def get_MetricType(self): # String
		return self.get_query_params().get('MetricType')

	def set_MetricType(self, MetricType):  # String
		self.add_query_param('MetricType', MetricType)
	def get_TimeStep(self): # String
		return self.get_query_params().get('TimeStep')

	def set_TimeStep(self, TimeStep):  # String
		self.add_query_param('TimeStep', TimeStep)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_SlotId(self): # String
		return self.get_path_params().get('SlotId')

	def set_SlotId(self, SlotId):  # String
		self.add_path_param('SlotId', SlotId)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_Dimensions(self): # String
		return self.get_query_params().get('Dimensions')

	def set_Dimensions(self, Dimensions):  # String
		self.add_query_param('Dimensions', Dimensions)
