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
from aliyunsdkess.endpoint import endpoint_data

class DescribePatternTypesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribePatternTypes','ess')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MemoryLists(self): # RepeatList
		return self.get_query_params().get('MemoryList')

	def set_MemoryLists(self, MemoryList):  # RepeatList
		for depth1 in range(len(MemoryList)):
			self.add_query_param('MemoryList.' + str(depth1 + 1), MemoryList[depth1])
	def get_Memory(self): # Float
		return self.get_query_params().get('Memory')

	def set_Memory(self, Memory):  # Float
		self.add_query_param('Memory', Memory)
	def get_CoresLists(self): # RepeatList
		return self.get_query_params().get('CoresList')

	def set_CoresLists(self, CoresList):  # RepeatList
		for depth1 in range(len(CoresList)):
			self.add_query_param('CoresList.' + str(depth1 + 1), CoresList[depth1])
	def get_Cores(self): # Integer
		return self.get_query_params().get('Cores')

	def set_Cores(self, Cores):  # Integer
		self.add_query_param('Cores', Cores)
	def get_Architectures(self): # RepeatList
		return self.get_query_params().get('Architecture')

	def set_Architectures(self, Architecture):  # RepeatList
		for depth1 in range(len(Architecture)):
			self.add_query_param('Architecture.' + str(depth1 + 1), Architecture[depth1])
	def get_MaxPrice(self): # Float
		return self.get_query_params().get('MaxPrice')

	def set_MaxPrice(self, MaxPrice):  # Float
		self.add_query_param('MaxPrice', MaxPrice)
	def get_ExcludedInstanceTypes(self): # RepeatList
		return self.get_query_params().get('ExcludedInstanceType')

	def set_ExcludedInstanceTypes(self, ExcludedInstanceType):  # RepeatList
		for depth1 in range(len(ExcludedInstanceType)):
			self.add_query_param('ExcludedInstanceType.' + str(depth1 + 1), ExcludedInstanceType[depth1])
	def get_BurstablePerformance(self): # String
		return self.get_query_params().get('BurstablePerformance')

	def set_BurstablePerformance(self, BurstablePerformance):  # String
		self.add_query_param('BurstablePerformance', BurstablePerformance)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_VSwitchIds(self): # RepeatList
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchIds(self, VSwitchId):  # RepeatList
		for depth1 in range(len(VSwitchId)):
			self.add_query_param('VSwitchId.' + str(depth1 + 1), VSwitchId[depth1])
	def get_InstanceFamilyLevel(self): # String
		return self.get_query_params().get('InstanceFamilyLevel')

	def set_InstanceFamilyLevel(self, InstanceFamilyLevel):  # String
		self.add_query_param('InstanceFamilyLevel', InstanceFamilyLevel)
	def get_ChannelId(self): # Long
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # Long
		self.add_query_param('ChannelId', ChannelId)
