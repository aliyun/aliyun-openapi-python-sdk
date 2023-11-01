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

class ModifyMetricRuleBlackListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'ModifyMetricRuleBlackList','cms')
		self.set_method('POST')

	def get_ScopeType(self): # String
		return self.get_query_params().get('ScopeType')

	def set_ScopeType(self, ScopeType):  # String
		self.add_query_param('ScopeType', ScopeType)
	def get_Instancess(self): # RepeatList
		return self.get_query_params().get('Instances')

	def set_Instancess(self, Instances):  # RepeatList
		for depth1 in range(len(Instances)):
			self.add_query_param('Instances.' + str(depth1 + 1), Instances[depth1])
	def get_EnableEndTime(self): # String
		return self.get_query_params().get('EnableEndTime')

	def set_EnableEndTime(self, EnableEndTime):  # String
		self.add_query_param('EnableEndTime', EnableEndTime)
	def get_ScopeValue(self): # String
		return self.get_query_params().get('ScopeValue')

	def set_ScopeValue(self, ScopeValue):  # String
		self.add_query_param('ScopeValue', ScopeValue)
	def get_EnableStartTime(self): # String
		return self.get_query_params().get('EnableStartTime')

	def set_EnableStartTime(self, EnableStartTime):  # String
		self.add_query_param('EnableStartTime', EnableStartTime)
	def get_EffectiveTime(self): # String
		return self.get_query_params().get('EffectiveTime')

	def set_EffectiveTime(self, EffectiveTime):  # String
		self.add_query_param('EffectiveTime', EffectiveTime)
	def get_Id(self): # String
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_query_param('Id', Id)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_Metricss(self): # RepeatList
		return self.get_query_params().get('Metrics')

	def set_Metricss(self, Metrics):  # RepeatList
		for depth1 in range(len(Metrics)):
			if Metrics[depth1].get('Resource') is not None:
				self.add_query_param('Metrics.' + str(depth1 + 1) + '.Resource', Metrics[depth1].get('Resource'))
			if Metrics[depth1].get('MetricName') is not None:
				self.add_query_param('Metrics.' + str(depth1 + 1) + '.MetricName', Metrics[depth1].get('MetricName'))
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
