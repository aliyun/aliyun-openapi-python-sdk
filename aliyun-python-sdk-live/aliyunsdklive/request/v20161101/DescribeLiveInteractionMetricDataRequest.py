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
from aliyunsdklive.endpoint import endpoint_data

class DescribeLiveInteractionMetricDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'DescribeLiveInteractionMetricData','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MetricType(self): # String
		return self.get_query_params().get('MetricType')

	def set_MetricType(self, MetricType):  # String
		self.add_query_param('MetricType', MetricType)
	def get_EndTs(self): # Long
		return self.get_query_params().get('EndTs')

	def set_EndTs(self, EndTs):  # Long
		self.add_query_param('EndTs', EndTs)
	def get_Os(self): # String
		return self.get_query_params().get('Os')

	def set_Os(self, Os):  # String
		self.add_query_param('Os', Os)
	def get_BeginTs(self): # Long
		return self.get_query_params().get('BeginTs')

	def set_BeginTs(self, BeginTs):  # Long
		self.add_query_param('BeginTs', BeginTs)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_TerminalType(self): # String
		return self.get_query_params().get('TerminalType')

	def set_TerminalType(self, TerminalType):  # String
		self.add_query_param('TerminalType', TerminalType)
