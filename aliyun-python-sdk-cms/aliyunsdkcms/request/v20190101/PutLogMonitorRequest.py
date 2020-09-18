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

	def get_SlsLogstore(self):
		return self.get_query_params().get('SlsLogstore')

	def set_SlsLogstore(self,SlsLogstore):
		self.add_query_param('SlsLogstore',SlsLogstore)

	def get_SlsProject(self):
		return self.get_query_params().get('SlsProject')

	def set_SlsProject(self,SlsProject):
		self.add_query_param('SlsProject',SlsProject)

	def get_ValueFilters(self):
		return self.get_query_params().get('ValueFilter')

	def set_ValueFilters(self, ValueFilters):
		for depth1 in range(len(ValueFilters)):
			if ValueFilters[depth1].get('Value') is not None:
				self.add_query_param('ValueFilter.' + str(depth1 + 1) + '.Value', ValueFilters[depth1].get('Value'))
			if ValueFilters[depth1].get('Key') is not None:
				self.add_query_param('ValueFilter.' + str(depth1 + 1) + '.Key', ValueFilters[depth1].get('Key'))
			if ValueFilters[depth1].get('Operator') is not None:
				self.add_query_param('ValueFilter.' + str(depth1 + 1) + '.Operator', ValueFilters[depth1].get('Operator'))

	def get_MetricExpress(self):
		return self.get_query_params().get('MetricExpress')

	def set_MetricExpress(self,MetricExpress):
		self.add_query_param('MetricExpress',MetricExpress)

	def get_SlsRegionId(self):
		return self.get_query_params().get('SlsRegionId')

	def set_SlsRegionId(self,SlsRegionId):
		self.add_query_param('SlsRegionId',SlsRegionId)

	def get_MetricName(self):
		return self.get_query_params().get('MetricName')

	def set_MetricName(self,MetricName):
		self.add_query_param('MetricName',MetricName)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Tumblingwindows(self):
		return self.get_query_params().get('Tumblingwindows')

	def set_Tumblingwindows(self,Tumblingwindows):
		self.add_query_param('Tumblingwindows',Tumblingwindows)

	def get_ValueFilterRelation(self):
		return self.get_query_params().get('ValueFilterRelation')

	def set_ValueFilterRelation(self,ValueFilterRelation):
		self.add_query_param('ValueFilterRelation',ValueFilterRelation)

	def get_Unit(self):
		return self.get_query_params().get('Unit')

	def set_Unit(self,Unit):
		self.add_query_param('Unit',Unit)

	def get_Groupbyss(self):
		return self.get_query_params().get('Groupbys')

	def set_Groupbyss(self, Groupbyss):
		for depth1 in range(len(Groupbyss)):
			if Groupbyss[depth1].get('FieldName') is not None:
				self.add_query_param('Groupbys.' + str(depth1 + 1) + '.FieldName', Groupbyss[depth1].get('FieldName'))
			if Groupbyss[depth1].get('Alias') is not None:
				self.add_query_param('Groupbys.' + str(depth1 + 1) + '.Alias', Groupbyss[depth1].get('Alias'))

	def get_LogId(self):
		return self.get_query_params().get('LogId')

	def set_LogId(self,LogId):
		self.add_query_param('LogId',LogId)

	def get_Aggregatess(self):
		return self.get_query_params().get('Aggregates')

	def set_Aggregatess(self, Aggregatess):
		for depth1 in range(len(Aggregatess)):
			if Aggregatess[depth1].get('FieldName') is not None:
				self.add_query_param('Aggregates.' + str(depth1 + 1) + '.FieldName', Aggregatess[depth1].get('FieldName'))
			if Aggregatess[depth1].get('Function') is not None:
				self.add_query_param('Aggregates.' + str(depth1 + 1) + '.Function', Aggregatess[depth1].get('Function'))
			if Aggregatess[depth1].get('Alias') is not None:
				self.add_query_param('Aggregates.' + str(depth1 + 1) + '.Alias', Aggregatess[depth1].get('Alias'))