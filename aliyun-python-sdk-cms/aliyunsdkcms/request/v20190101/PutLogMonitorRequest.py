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

class PutLogMonitorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutLogMonitor','cms')
		self.set_method('POST')

	def get_SlsLogstore(self): # String
		return self.get_query_params().get('SlsLogstore')

	def set_SlsLogstore(self, SlsLogstore):  # String
		self.add_query_param('SlsLogstore', SlsLogstore)
	def get_SlsProject(self): # String
		return self.get_query_params().get('SlsProject')

	def set_SlsProject(self, SlsProject):  # String
		self.add_query_param('SlsProject', SlsProject)
	def get_ValueFilters(self): # RepeatList
		return self.get_query_params().get('ValueFilter')

	def set_ValueFilters(self, ValueFilter):  # RepeatList
		for depth1 in range(len(ValueFilter)):
			if ValueFilter[depth1].get('Value') is not None:
				self.add_query_param('ValueFilter.' + str(depth1 + 1) + '.Value', ValueFilter[depth1].get('Value'))
			if ValueFilter[depth1].get('Key') is not None:
				self.add_query_param('ValueFilter.' + str(depth1 + 1) + '.Key', ValueFilter[depth1].get('Key'))
			if ValueFilter[depth1].get('Operator') is not None:
				self.add_query_param('ValueFilter.' + str(depth1 + 1) + '.Operator', ValueFilter[depth1].get('Operator'))
	def get_MetricExpress(self): # String
		return self.get_query_params().get('MetricExpress')

	def set_MetricExpress(self, MetricExpress):  # String
		self.add_query_param('MetricExpress', MetricExpress)
	def get_SlsRegionId(self): # String
		return self.get_query_params().get('SlsRegionId')

	def set_SlsRegionId(self, SlsRegionId):  # String
		self.add_query_param('SlsRegionId', SlsRegionId)
	def get_MetricName(self): # String
		return self.get_query_params().get('MetricName')

	def set_MetricName(self, MetricName):  # String
		self.add_query_param('MetricName', MetricName)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_Tumblingwindows(self): # String
		return self.get_query_params().get('Tumblingwindows')

	def set_Tumblingwindows(self, Tumblingwindows):  # String
		self.add_query_param('Tumblingwindows', Tumblingwindows)
	def get_ValueFilterRelation(self): # String
		return self.get_query_params().get('ValueFilterRelation')

	def set_ValueFilterRelation(self, ValueFilterRelation):  # String
		self.add_query_param('ValueFilterRelation', ValueFilterRelation)
	def get_Unit(self): # String
		return self.get_query_params().get('Unit')

	def set_Unit(self, Unit):  # String
		self.add_query_param('Unit', Unit)
	def get_Groupbyss(self): # RepeatList
		return self.get_query_params().get('Groupbys')

	def set_Groupbyss(self, Groupbys):  # RepeatList
		for depth1 in range(len(Groupbys)):
			if Groupbys[depth1].get('FieldName') is not None:
				self.add_query_param('Groupbys.' + str(depth1 + 1) + '.FieldName', Groupbys[depth1].get('FieldName'))
			if Groupbys[depth1].get('Alias') is not None:
				self.add_query_param('Groupbys.' + str(depth1 + 1) + '.Alias', Groupbys[depth1].get('Alias'))
	def get_LogId(self): # String
		return self.get_query_params().get('LogId')

	def set_LogId(self, LogId):  # String
		self.add_query_param('LogId', LogId)
	def get_Aggregatess(self): # RepeatList
		return self.get_query_params().get('Aggregates')

	def set_Aggregatess(self, Aggregates):  # RepeatList
		for depth1 in range(len(Aggregates)):
			if Aggregates[depth1].get('FieldName') is not None:
				self.add_query_param('Aggregates.' + str(depth1 + 1) + '.FieldName', Aggregates[depth1].get('FieldName'))
			if Aggregates[depth1].get('Function') is not None:
				self.add_query_param('Aggregates.' + str(depth1 + 1) + '.Function', Aggregates[depth1].get('Function'))
			if Aggregates[depth1].get('Alias') is not None:
				self.add_query_param('Aggregates.' + str(depth1 + 1) + '.Alias', Aggregates[depth1].get('Alias'))
