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
from aliyunsdkarms.endpoint import endpoint_data

class QueryMetricByPageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'QueryMetricByPage','arms')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_OrderBy(self):
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self,OrderBy):
		self.add_query_param('OrderBy',OrderBy)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_Filterss(self):
		return self.get_query_params().get('Filters')

	def set_Filterss(self, Filterss):
		for depth1 in range(len(Filterss)):
			if Filterss[depth1].get('Value') is not None:
				self.add_query_param('Filters.' + str(depth1 + 1) + '.Value', Filterss[depth1].get('Value'))
			if Filterss[depth1].get('Key') is not None:
				self.add_query_param('Filters.' + str(depth1 + 1) + '.Key', Filterss[depth1].get('Key'))

	def get_Measuress(self):
		return self.get_query_params().get('Measures')

	def set_Measuress(self, Measuress):
		for depth1 in range(len(Measuress)):
			if Measuress[depth1] is not None:
				self.add_query_param('Measures.' + str(depth1 + 1) , Measuress[depth1])

	def get_IntervalInSec(self):
		return self.get_query_params().get('IntervalInSec')

	def set_IntervalInSec(self,IntervalInSec):
		self.add_query_param('IntervalInSec',IntervalInSec)

	def get_Metric(self):
		return self.get_query_params().get('Metric')

	def set_Metric(self,Metric):
		self.add_query_param('Metric',Metric)

	def get_CustomFilterss(self):
		return self.get_query_params().get('CustomFilters')

	def set_CustomFilterss(self, CustomFilterss):
		for depth1 in range(len(CustomFilterss)):
			if CustomFilterss[depth1] is not None:
				self.add_query_param('CustomFilters.' + str(depth1 + 1) , CustomFilterss[depth1])

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Dimensionss(self):
		return self.get_query_params().get('Dimensions')

	def set_Dimensionss(self, Dimensionss):
		for depth1 in range(len(Dimensionss)):
			if Dimensionss[depth1] is not None:
				self.add_query_param('Dimensions.' + str(depth1 + 1) , Dimensionss[depth1])

	def get_Order(self):
		return self.get_query_params().get('Order')

	def set_Order(self,Order):
		self.add_query_param('Order',Order)