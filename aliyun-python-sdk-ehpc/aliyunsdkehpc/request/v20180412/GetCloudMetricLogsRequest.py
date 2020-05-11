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
from aliyunsdkehpc.endpoint import endpoint_data

class GetCloudMetricLogsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'GetCloudMetricLogs')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MetricScope(self):
		return self.get_query_params().get('MetricScope')

	def set_MetricScope(self,MetricScope):
		self.add_query_param('MetricScope',MetricScope)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_AggregationInterval(self):
		return self.get_query_params().get('AggregationInterval')

	def set_AggregationInterval(self,AggregationInterval):
		self.add_query_param('AggregationInterval',AggregationInterval)

	def get_Reverse(self):
		return self.get_query_params().get('Reverse')

	def set_Reverse(self,Reverse):
		self.add_query_param('Reverse',Reverse)

	def get_AggregationType(self):
		return self.get_query_params().get('AggregationType')

	def set_AggregationType(self,AggregationType):
		self.add_query_param('AggregationType',AggregationType)

	def get_Filter(self):
		return self.get_query_params().get('Filter')

	def set_Filter(self,Filter):
		self.add_query_param('Filter',Filter)

	def get_MetricCategories(self):
		return self.get_query_params().get('MetricCategories')

	def set_MetricCategories(self,MetricCategories):
		self.add_query_param('MetricCategories',MetricCategories)

	def get__From(self):
		return self.get_query_params().get('From')

	def set__From(self,_From):
		self.add_query_param('From',_From)

	def get_To(self):
		return self.get_query_params().get('To')

	def set_To(self,To):
		self.add_query_param('To',To)