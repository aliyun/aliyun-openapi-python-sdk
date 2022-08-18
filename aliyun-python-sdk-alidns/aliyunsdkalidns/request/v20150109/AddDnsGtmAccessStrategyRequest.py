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
from aliyunsdkalidns.endpoint import endpoint_data

class AddDnsGtmAccessStrategyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'AddDnsGtmAccessStrategy','alidns')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DefaultLbaStrategy(self): # String
		return self.get_query_params().get('DefaultLbaStrategy')

	def set_DefaultLbaStrategy(self, DefaultLbaStrategy):  # String
		self.add_query_param('DefaultLbaStrategy', DefaultLbaStrategy)
	def get_FailoverAddrPoolType(self): # String
		return self.get_query_params().get('FailoverAddrPoolType')

	def set_FailoverAddrPoolType(self, FailoverAddrPoolType):  # String
		self.add_query_param('FailoverAddrPoolType', FailoverAddrPoolType)
	def get_DefaultAddrPoolType(self): # String
		return self.get_query_params().get('DefaultAddrPoolType')

	def set_DefaultAddrPoolType(self, DefaultAddrPoolType):  # String
		self.add_query_param('DefaultAddrPoolType', DefaultAddrPoolType)
	def get_FailoverMaxReturnAddrNum(self): # Integer
		return self.get_query_params().get('FailoverMaxReturnAddrNum')

	def set_FailoverMaxReturnAddrNum(self, FailoverMaxReturnAddrNum):  # Integer
		self.add_query_param('FailoverMaxReturnAddrNum', FailoverMaxReturnAddrNum)
	def get_FailoverLbaStrategy(self): # String
		return self.get_query_params().get('FailoverLbaStrategy')

	def set_FailoverLbaStrategy(self, FailoverLbaStrategy):  # String
		self.add_query_param('FailoverLbaStrategy', FailoverLbaStrategy)
	def get_DefaultAddrPools(self): # RepeatList
		return self.get_query_params().get('DefaultAddrPool')

	def set_DefaultAddrPools(self, DefaultAddrPool):  # RepeatList
		for depth1 in range(len(DefaultAddrPool)):
			if DefaultAddrPool[depth1].get('Id') is not None:
				self.add_query_param('DefaultAddrPool.' + str(depth1 + 1) + '.Id', DefaultAddrPool[depth1].get('Id'))
			if DefaultAddrPool[depth1].get('LbaWeight') is not None:
				self.add_query_param('DefaultAddrPool.' + str(depth1 + 1) + '.LbaWeight', DefaultAddrPool[depth1].get('LbaWeight'))
	def get_FailoverMinAvailableAddrNum(self): # Integer
		return self.get_query_params().get('FailoverMinAvailableAddrNum')

	def set_FailoverMinAvailableAddrNum(self, FailoverMinAvailableAddrNum):  # Integer
		self.add_query_param('FailoverMinAvailableAddrNum', FailoverMinAvailableAddrNum)
	def get_DefaultMaxReturnAddrNum(self): # Integer
		return self.get_query_params().get('DefaultMaxReturnAddrNum')

	def set_DefaultMaxReturnAddrNum(self, DefaultMaxReturnAddrNum):  # Integer
		self.add_query_param('DefaultMaxReturnAddrNum', DefaultMaxReturnAddrNum)
	def get_DefaultMinAvailableAddrNum(self): # Integer
		return self.get_query_params().get('DefaultMinAvailableAddrNum')

	def set_DefaultMinAvailableAddrNum(self, DefaultMinAvailableAddrNum):  # Integer
		self.add_query_param('DefaultMinAvailableAddrNum', DefaultMinAvailableAddrNum)
	def get_StrategyMode(self): # String
		return self.get_query_params().get('StrategyMode')

	def set_StrategyMode(self, StrategyMode):  # String
		self.add_query_param('StrategyMode', StrategyMode)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Lines(self): # String
		return self.get_query_params().get('Lines')

	def set_Lines(self, Lines):  # String
		self.add_query_param('Lines', Lines)
	def get_StrategyName(self): # String
		return self.get_query_params().get('StrategyName')

	def set_StrategyName(self, StrategyName):  # String
		self.add_query_param('StrategyName', StrategyName)
	def get_DefaultLatencyOptimization(self): # String
		return self.get_query_params().get('DefaultLatencyOptimization')

	def set_DefaultLatencyOptimization(self, DefaultLatencyOptimization):  # String
		self.add_query_param('DefaultLatencyOptimization', DefaultLatencyOptimization)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_FailoverLatencyOptimization(self): # String
		return self.get_query_params().get('FailoverLatencyOptimization')

	def set_FailoverLatencyOptimization(self, FailoverLatencyOptimization):  # String
		self.add_query_param('FailoverLatencyOptimization', FailoverLatencyOptimization)
	def get_FailoverAddrPools(self): # RepeatList
		return self.get_query_params().get('FailoverAddrPool')

	def set_FailoverAddrPools(self, FailoverAddrPool):  # RepeatList
		for depth1 in range(len(FailoverAddrPool)):
			if FailoverAddrPool[depth1].get('Id') is not None:
				self.add_query_param('FailoverAddrPool.' + str(depth1 + 1) + '.Id', FailoverAddrPool[depth1].get('Id'))
			if FailoverAddrPool[depth1].get('LbaWeight') is not None:
				self.add_query_param('FailoverAddrPool.' + str(depth1 + 1) + '.LbaWeight', FailoverAddrPool[depth1].get('LbaWeight'))
