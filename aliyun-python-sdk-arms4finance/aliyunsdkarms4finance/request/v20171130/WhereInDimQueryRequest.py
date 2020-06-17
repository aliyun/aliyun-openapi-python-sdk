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

class WhereInDimQueryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS4FINANCE', '2017-11-30', 'WhereInDimQuery','arms4finance')
		self.set_method('POST')

	def get_DateStr(self):
		return self.get_query_params().get('DateStr')

	def set_DateStr(self,DateStr):
		self.add_query_param('DateStr',DateStr)

	def get_MinTime(self):
		return self.get_query_params().get('MinTime')

	def set_MinTime(self,MinTime):
		self.add_query_param('MinTime',MinTime)

	def get_MaxTime(self):
		return self.get_query_params().get('MaxTime')

	def set_MaxTime(self,MaxTime):
		self.add_query_param('MaxTime',MaxTime)

	def get_WhereInKey(self):
		return self.get_query_params().get('WhereInKey')

	def set_WhereInKey(self,WhereInKey):
		self.add_query_param('WhereInKey',WhereInKey)

	def get_Measuress(self):
		return self.get_query_params().get('Measuress')

	def set_Measuress(self, Measuress):
		for depth1 in range(len(Measuress)):
			if Measuress[depth1] is not None:
				self.add_query_param('Measures.' + str(depth1 + 1) , Measuress[depth1])

	def get_IntervalInSec(self):
		return self.get_query_params().get('IntervalInSec')

	def set_IntervalInSec(self,IntervalInSec):
		self.add_query_param('IntervalInSec',IntervalInSec)

	def get_IsDrillDown(self):
		return self.get_query_params().get('IsDrillDown')

	def set_IsDrillDown(self,IsDrillDown):
		self.add_query_param('IsDrillDown',IsDrillDown)

	def get_DatasetId(self):
		return self.get_query_params().get('DatasetId')

	def set_DatasetId(self,DatasetId):
		self.add_query_param('DatasetId',DatasetId)

	def get_WhereInValuess(self):
		return self.get_query_params().get('WhereInValuess')

	def set_WhereInValuess(self, WhereInValuess):
		for depth1 in range(len(WhereInValuess)):
			if WhereInValuess[depth1] is not None:
				self.add_query_param('WhereInValues.' + str(depth1 + 1) , WhereInValuess[depth1])

	def get_Dimensionss(self):
		return self.get_query_params().get('Dimensionss')

	def set_Dimensionss(self, Dimensionss):
		for depth1 in range(len(Dimensionss)):
			if Dimensionss[depth1].get('Value') is not None:
				self.add_query_param('Dimensions.' + str(depth1 + 1) + '.Value', Dimensionss[depth1].get('Value'))
			if Dimensionss[depth1].get('Key') is not None:
				self.add_query_param('Dimensions.' + str(depth1 + 1) + '.Key', Dimensionss[depth1].get('Key'))