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

	def get_MetricLists(self): # RepeatList
		return self.get_query_params().get('MetricList')

	def set_MetricLists(self, MetricList):  # RepeatList
		for depth1 in range(len(MetricList)):
			if MetricList[depth1].get('Period') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Period', MetricList[depth1].get('Period'))
			if MetricList[depth1].get('GroupId') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.GroupId', MetricList[depth1].get('GroupId'))
			if MetricList[depth1].get('Values') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Values', MetricList[depth1].get('Values'))
			if MetricList[depth1].get('Time') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Time', MetricList[depth1].get('Time'))
			if MetricList[depth1].get('Type') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Type', MetricList[depth1].get('Type'))
			if MetricList[depth1].get('MetricName') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.MetricName', MetricList[depth1].get('MetricName'))
			if MetricList[depth1].get('Dimensions') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Dimensions', MetricList[depth1].get('Dimensions'))
