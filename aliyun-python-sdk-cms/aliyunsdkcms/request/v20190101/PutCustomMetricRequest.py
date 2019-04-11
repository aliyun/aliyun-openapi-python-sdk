# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
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

	def get_MetricLists(self):
		return self.get_query_params().get('MetricLists')

	def set_MetricLists(self,MetricLists):
		for i in range(len(MetricLists)):	
			if MetricLists[i].get('Period') is not None:
				self.add_query_param('MetricList.' + str(i + 1) + '.Period' , MetricLists[i].get('Period'))
			if MetricLists[i].get('GroupId') is not None:
				self.add_query_param('MetricList.' + str(i + 1) + '.GroupId' , MetricLists[i].get('GroupId'))
			if MetricLists[i].get('Values') is not None:
				self.add_query_param('MetricList.' + str(i + 1) + '.Values' , MetricLists[i].get('Values'))
			if MetricLists[i].get('Time') is not None:
				self.add_query_param('MetricList.' + str(i + 1) + '.Time' , MetricLists[i].get('Time'))
			if MetricLists[i].get('MetricName') is not None:
				self.add_query_param('MetricList.' + str(i + 1) + '.MetricName' , MetricLists[i].get('MetricName'))
			if MetricLists[i].get('Type') is not None:
				self.add_query_param('MetricList.' + str(i + 1) + '.Type' , MetricLists[i].get('Type'))
			if MetricLists[i].get('Dimensions') is not None:
				self.add_query_param('MetricList.' + str(i + 1) + '.Dimensions' , MetricLists[i].get('Dimensions'))
