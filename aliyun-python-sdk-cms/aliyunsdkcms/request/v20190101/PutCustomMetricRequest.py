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

class PutCustomMetricRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutCustomMetric','cms')
		self.set_method('POST')

	def get_MetricLists(self):
		return self.get_query_params().get('MetricList')

	def set_MetricLists(self, MetricLists):
		for depth1 in range(len(MetricLists)):
			if MetricLists[depth1].get('Period') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Period', MetricLists[depth1].get('Period'))
			if MetricLists[depth1].get('GroupId') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.GroupId', MetricLists[depth1].get('GroupId'))
			if MetricLists[depth1].get('Values') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Values', MetricLists[depth1].get('Values'))
			if MetricLists[depth1].get('Time') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Time', MetricLists[depth1].get('Time'))
			if MetricLists[depth1].get('MetricName') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.MetricName', MetricLists[depth1].get('MetricName'))
			if MetricLists[depth1].get('Type') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Type', MetricLists[depth1].get('Type'))
			if MetricLists[depth1].get('Dimensions') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Dimensions', MetricLists[depth1].get('Dimensions'))