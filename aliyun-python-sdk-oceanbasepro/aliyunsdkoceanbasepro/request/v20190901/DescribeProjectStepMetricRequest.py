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

from aliyunsdkcore.request import RpcRequest
from aliyunsdkoceanbasepro.endpoint import endpoint_data

class DescribeProjectStepMetricRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'DescribeProjectStepMetric','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MetricType(self): # String
		return self.get_body_params().get('MetricType')

	def set_MetricType(self, MetricType):  # String
		self.add_body_params('MetricType', MetricType)
	def get_StepName(self): # String
		return self.get_body_params().get('StepName')

	def set_StepName(self, StepName):  # String
		self.add_body_params('StepName', StepName)
	def get_Aggregator(self): # String
		return self.get_body_params().get('Aggregator')

	def set_Aggregator(self, Aggregator):  # String
		self.add_body_params('Aggregator', Aggregator)
	def get_MaxPointNum(self): # Integer
		return self.get_body_params().get('MaxPointNum')

	def set_MaxPointNum(self, MaxPointNum):  # Integer
		self.add_body_params('MaxPointNum', MaxPointNum)
	def get_EndTimestamp(self): # Long
		return self.get_body_params().get('EndTimestamp')

	def set_EndTimestamp(self, EndTimestamp):  # Long
		self.add_body_params('EndTimestamp', EndTimestamp)
	def get_BeginTimestamp(self): # Long
		return self.get_body_params().get('BeginTimestamp')

	def set_BeginTimestamp(self, BeginTimestamp):  # Long
		self.add_body_params('BeginTimestamp', BeginTimestamp)
	def get_ProjectId(self): # String
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # String
		self.add_body_params('ProjectId', ProjectId)
