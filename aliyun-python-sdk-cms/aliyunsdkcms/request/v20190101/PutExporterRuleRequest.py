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

class PutExporterRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutExporterRule','cms')
		self.set_method('POST')

	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_DstNamess(self): # RepeatList
		return self.get_query_params().get('DstNames')

	def set_DstNamess(self, DstNames):  # RepeatList
		for depth1 in range(len(DstNames)):
			self.add_query_param('DstNames.' + str(depth1 + 1), DstNames[depth1])
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_TargetWindows(self): # String
		return self.get_query_params().get('TargetWindows')

	def set_TargetWindows(self, TargetWindows):  # String
		self.add_query_param('TargetWindows', TargetWindows)
	def get_Describe(self): # String
		return self.get_query_params().get('Describe')

	def set_Describe(self, Describe):  # String
		self.add_query_param('Describe', Describe)
	def get_MetricName(self): # String
		return self.get_query_params().get('MetricName')

	def set_MetricName(self, MetricName):  # String
		self.add_query_param('MetricName', MetricName)
