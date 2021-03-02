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

class UpdateDnsGtmAccessStrategyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'UpdateDnsGtmAccessStrategy','alidns')
		self.set_method('POST')

	def get_DefaultLbaStrategy(self):
		return self.get_query_params().get('DefaultLbaStrategy')

	def set_DefaultLbaStrategy(self,DefaultLbaStrategy):
		self.add_query_param('DefaultLbaStrategy',DefaultLbaStrategy)

	def get_FailoverAddrPoolType(self):
		return self.get_query_params().get('FailoverAddrPoolType')

	def set_FailoverAddrPoolType(self,FailoverAddrPoolType):
		self.add_query_param('FailoverAddrPoolType',FailoverAddrPoolType)

	def get_DefaultAddrPoolType(self):
		return self.get_query_params().get('DefaultAddrPoolType')

	def set_DefaultAddrPoolType(self,DefaultAddrPoolType):
		self.add_query_param('DefaultAddrPoolType',DefaultAddrPoolType)

	def get_FailoverMaxReturnAddrNum(self):
		return self.get_query_params().get('FailoverMaxReturnAddrNum')

	def set_FailoverMaxReturnAddrNum(self,FailoverMaxReturnAddrNum):
		self.add_query_param('FailoverMaxReturnAddrNum',FailoverMaxReturnAddrNum)

	def get_FailoverLbaStrategy(self):
		return self.get_query_params().get('FailoverLbaStrategy')

	def set_FailoverLbaStrategy(self,FailoverLbaStrategy):
		self.add_query_param('FailoverLbaStrategy',FailoverLbaStrategy)

	def get_DefaultAddrPools(self):
		return self.get_query_params().get('DefaultAddrPool')

	def set_DefaultAddrPools(self, DefaultAddrPools):
		for depth1 in range(len(DefaultAddrPools)):
			if DefaultAddrPools[depth1].get('Id') is not None:
				self.add_query_param('DefaultAddrPool.' + str(depth1 + 1) + '.Id', DefaultAddrPools[depth1].get('Id'))
			if DefaultAddrPools[depth1].get('LbaWeight') is not None:
				self.add_query_param('DefaultAddrPool.' + str(depth1 + 1) + '.LbaWeight', DefaultAddrPools[depth1].get('LbaWeight'))

	def get_FailoverMinAvailableAddrNum(self):
		return self.get_query_params().get('FailoverMinAvailableAddrNum')

	def set_FailoverMinAvailableAddrNum(self,FailoverMinAvailableAddrNum):
		self.add_query_param('FailoverMinAvailableAddrNum',FailoverMinAvailableAddrNum)

	def get_DefaultMaxReturnAddrNum(self):
		return self.get_query_params().get('DefaultMaxReturnAddrNum')

	def set_DefaultMaxReturnAddrNum(self,DefaultMaxReturnAddrNum):
		self.add_query_param('DefaultMaxReturnAddrNum',DefaultMaxReturnAddrNum)

	def get_DefaultMinAvailableAddrNum(self):
		return self.get_query_params().get('DefaultMinAvailableAddrNum')

	def set_DefaultMinAvailableAddrNum(self,DefaultMinAvailableAddrNum):
		self.add_query_param('DefaultMinAvailableAddrNum',DefaultMinAvailableAddrNum)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Lines(self):
		return self.get_query_params().get('Lines')

	def set_Lines(self,Lines):
		self.add_query_param('Lines',Lines)

	def get_StrategyName(self):
		return self.get_query_params().get('StrategyName')

	def set_StrategyName(self,StrategyName):
		self.add_query_param('StrategyName',StrategyName)

	def get_DefaultLatencyOptimization(self):
		return self.get_query_params().get('DefaultLatencyOptimization')

	def set_DefaultLatencyOptimization(self,DefaultLatencyOptimization):
		self.add_query_param('DefaultLatencyOptimization',DefaultLatencyOptimization)

	def get_FailoverLatencyOptimization(self):
		return self.get_query_params().get('FailoverLatencyOptimization')

	def set_FailoverLatencyOptimization(self,FailoverLatencyOptimization):
		self.add_query_param('FailoverLatencyOptimization',FailoverLatencyOptimization)

	def get_StrategyId(self):
		return self.get_query_params().get('StrategyId')

	def set_StrategyId(self,StrategyId):
		self.add_query_param('StrategyId',StrategyId)

	def get_FailoverAddrPools(self):
		return self.get_query_params().get('FailoverAddrPool')

	def set_FailoverAddrPools(self, FailoverAddrPools):
		for depth1 in range(len(FailoverAddrPools)):
			if FailoverAddrPools[depth1].get('Id') is not None:
				self.add_query_param('FailoverAddrPool.' + str(depth1 + 1) + '.Id', FailoverAddrPools[depth1].get('Id'))
			if FailoverAddrPools[depth1].get('LbaWeight') is not None:
				self.add_query_param('FailoverAddrPool.' + str(depth1 + 1) + '.LbaWeight', FailoverAddrPools[depth1].get('LbaWeight'))