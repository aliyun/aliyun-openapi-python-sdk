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

class PutHybridMonitorMetricDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutHybridMonitorMetricData','cms')
		self.set_method('POST')

	def get_MetricLists(self): # RepeatList
		return self.get_query_params().get('MetricList')

	def set_MetricLists(self, MetricList):  # RepeatList
		for depth1 in range(len(MetricList)):
			if MetricList[depth1].get('Name') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Name', MetricList[depth1].get('Name'))
			if MetricList[depth1].get('Value') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.Value', MetricList[depth1].get('Value'))
			if MetricList[depth1].get('Labels') is not None:
				for depth2 in range(len(MetricList[depth1].get('Labels'))):
					if MetricList[depth1].get('Labels')[depth2].get('Value') is not None:
						self.add_query_param('MetricList.' + str(depth1 + 1) + str(depth2 + 1) + '.Value', MetricList[depth1].get('Labels')[depth2].get('Value'))
					if MetricList[depth1].get('Labels')[depth2].get('Key') is not None:
						self.add_query_param('MetricList.' + str(depth1 + 1) + str(depth2 + 1) + '.Key', MetricList[depth1].get('Labels')[depth2].get('Key'))
			if MetricList[depth1].get('TS') is not None:
				self.add_query_param('MetricList.' + str(depth1 + 1) + '.TS', MetricList[depth1].get('TS'))
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
