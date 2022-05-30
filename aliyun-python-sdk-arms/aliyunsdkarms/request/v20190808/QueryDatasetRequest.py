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

class QueryDatasetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'QueryDataset','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DateStr(self): # String
		return self.get_query_params().get('DateStr')

	def set_DateStr(self, DateStr):  # String
		self.add_query_param('DateStr', DateStr)
	def get_MinTime(self): # Long
		return self.get_query_params().get('MinTime')

	def set_MinTime(self, MinTime):  # Long
		self.add_query_param('MinTime', MinTime)
	def get_ProxyUserId(self): # String
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self, ProxyUserId):  # String
		self.add_query_param('ProxyUserId', ProxyUserId)
	def get_ReduceTail(self): # Boolean
		return self.get_query_params().get('ReduceTail')

	def set_ReduceTail(self, ReduceTail):  # Boolean
		self.add_query_param('ReduceTail', ReduceTail)
	def get_MaxTime(self): # Long
		return self.get_query_params().get('MaxTime')

	def set_MaxTime(self, MaxTime):  # Long
		self.add_query_param('MaxTime', MaxTime)
	def get_OptionalDimss(self): # RepeatList
		return self.get_query_params().get('OptionalDims')

	def set_OptionalDimss(self, OptionalDims):  # RepeatList
		for depth1 in range(len(OptionalDims)):
			if OptionalDims[depth1].get('Type') is not None:
				self.add_query_param('OptionalDims.' + str(depth1 + 1) + '.Type', OptionalDims[depth1].get('Type'))
			if OptionalDims[depth1].get('Value') is not None:
				self.add_query_param('OptionalDims.' + str(depth1 + 1) + '.Value', OptionalDims[depth1].get('Value'))
			if OptionalDims[depth1].get('Key') is not None:
				self.add_query_param('OptionalDims.' + str(depth1 + 1) + '.Key', OptionalDims[depth1].get('Key'))
	def get_Measuress(self): # RepeatList
		return self.get_query_params().get('Measures')

	def set_Measuress(self, Measures):  # RepeatList
		for depth1 in range(len(Measures)):
			self.add_query_param('Measures.' + str(depth1 + 1), Measures[depth1])
	def get_IntervalInSec(self): # Integer
		return self.get_query_params().get('IntervalInSec')

	def set_IntervalInSec(self, IntervalInSec):  # Integer
		self.add_query_param('IntervalInSec', IntervalInSec)
	def get_IsDrillDown(self): # Boolean
		return self.get_query_params().get('IsDrillDown')

	def set_IsDrillDown(self, IsDrillDown):  # Boolean
		self.add_query_param('IsDrillDown', IsDrillDown)
	def get_HungryMode(self): # Boolean
		return self.get_query_params().get('HungryMode')

	def set_HungryMode(self, HungryMode):  # Boolean
		self.add_query_param('HungryMode', HungryMode)
	def get_OrderByKey(self): # String
		return self.get_query_params().get('OrderByKey')

	def set_OrderByKey(self, OrderByKey):  # String
		self.add_query_param('OrderByKey', OrderByKey)
	def get_Limit(self): # Integer
		return self.get_query_params().get('Limit')

	def set_Limit(self, Limit):  # Integer
		self.add_query_param('Limit', Limit)
	def get_DatasetId(self): # Long
		return self.get_query_params().get('DatasetId')

	def set_DatasetId(self, DatasetId):  # Long
		self.add_query_param('DatasetId', DatasetId)
	def get_RequiredDimss(self): # RepeatList
		return self.get_query_params().get('RequiredDims')

	def set_RequiredDimss(self, RequiredDims):  # RepeatList
		for depth1 in range(len(RequiredDims)):
			if RequiredDims[depth1].get('Type') is not None:
				self.add_query_param('RequiredDims.' + str(depth1 + 1) + '.Type', RequiredDims[depth1].get('Type'))
			if RequiredDims[depth1].get('Value') is not None:
				self.add_query_param('RequiredDims.' + str(depth1 + 1) + '.Value', RequiredDims[depth1].get('Value'))
			if RequiredDims[depth1].get('Key') is not None:
				self.add_query_param('RequiredDims.' + str(depth1 + 1) + '.Key', RequiredDims[depth1].get('Key'))
	def get_Dimensionss(self): # RepeatList
		return self.get_query_params().get('Dimensions')

	def set_Dimensionss(self, Dimensions):  # RepeatList
		for depth1 in range(len(Dimensions)):
			if Dimensions[depth1].get('Type') is not None:
				self.add_query_param('Dimensions.' + str(depth1 + 1) + '.Type', Dimensions[depth1].get('Type'))
			if Dimensions[depth1].get('Value') is not None:
				self.add_query_param('Dimensions.' + str(depth1 + 1) + '.Value', Dimensions[depth1].get('Value'))
			if Dimensions[depth1].get('Key') is not None:
				self.add_query_param('Dimensions.' + str(depth1 + 1) + '.Key', Dimensions[depth1].get('Key'))
