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

	def get_MaximumCpuCoreCount(self): # Integer
		return self.get_query_params().get('MaximumCpuCoreCount')

	def set_MaximumCpuCoreCount(self, MaximumCpuCoreCount):  # Integer
		self.add_query_param('MaximumCpuCoreCount', MaximumCpuCoreCount)
	def get_MaximumGpuAmount(self): # Integer
		return self.get_query_params().get('MaximumGpuAmount')

	def set_MaximumGpuAmount(self, MaximumGpuAmount):  # Integer
		self.add_query_param('MaximumGpuAmount', MaximumGpuAmount)
	def get_MaximumMemorySize(self): # Float
		return self.get_query_params().get('MaximumMemorySize')

	def set_MaximumMemorySize(self, MaximumMemorySize):  # Float
		self.add_query_param('MaximumMemorySize', MaximumMemorySize)
	def get_MinimumCpuCoreCount(self): # Integer
		return self.get_query_params().get('MinimumCpuCoreCount')

	def set_MinimumCpuCoreCount(self, MinimumCpuCoreCount):  # Integer
		self.add_query_param('MinimumCpuCoreCount', MinimumCpuCoreCount)
	def get_Cores(self): # Integer
		return self.get_query_params().get('Cores')

	def set_Cores(self, Cores):  # Integer
		self.add_query_param('Cores', Cores)
	def get_InstanceTypeFamiliess(self): # RepeatList
		return self.get_query_params().get('InstanceTypeFamilies')

	def set_InstanceTypeFamiliess(self, InstanceTypeFamilies):  # RepeatList
		for depth1 in range(len(InstanceTypeFamilies)):
			self.add_query_param('InstanceTypeFamilies.' + str(depth1 + 1), InstanceTypeFamilies[depth1])
	def get_MinimumBaselineCredit(self): # Integer
		return self.get_query_params().get('MinimumBaselineCredit')

	def set_MinimumBaselineCredit(self, MinimumBaselineCredit):  # Integer
		self.add_query_param('MinimumBaselineCredit', MinimumBaselineCredit)
	def get_CpuArchitecturess(self): # RepeatList
		return self.get_query_params().get('CpuArchitectures')

	def set_CpuArchitecturess(self, CpuArchitectures):  # RepeatList
		for depth1 in range(len(CpuArchitectures)):
			self.add_query_param('CpuArchitectures.' + str(depth1 + 1), CpuArchitectures[depth1])
	def get_InstanceCategoriess(self): # RepeatList
		return self.get_query_params().get('InstanceCategories')

	def set_InstanceCategoriess(self, InstanceCategories):  # RepeatList
		for depth1 in range(len(InstanceCategories)):
			self.add_query_param('InstanceCategories.' + str(depth1 + 1), InstanceCategories[depth1])
	def get_MaxPrice(self): # Float
		return self.get_query_params().get('MaxPrice')

	def set_MaxPrice(self, MaxPrice):  # Float
		self.add_query_param('MaxPrice', MaxPrice)
	def get_MinimumGpuAmount(self): # Integer
		return self.get_query_params().get('MinimumGpuAmount')

	def set_MinimumGpuAmount(self, MinimumGpuAmount):  # Integer
		self.add_query_param('MinimumGpuAmount', MinimumGpuAmount)
	def get_BurstablePerformance(self): # String
		return self.get_query_params().get('BurstablePerformance')

	def set_BurstablePerformance(self, BurstablePerformance):  # String
		self.add_query_param('BurstablePerformance', BurstablePerformance)
	def get_PhysicalProcessorModelss(self): # RepeatList
		return self.get_query_params().get('PhysicalProcessorModels')

	def set_PhysicalProcessorModelss(self, PhysicalProcessorModels):  # RepeatList
		for depth1 in range(len(PhysicalProcessorModels)):
			self.add_query_param('PhysicalProcessorModels.' + str(depth1 + 1), PhysicalProcessorModels[depth1])
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_VSwitchIds(self): # RepeatList
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchIds(self, VSwitchId):  # RepeatList
		for depth1 in range(len(VSwitchId)):
			self.add_query_param('VSwitchId.' + str(depth1 + 1), VSwitchId[depth1])
	def get_MinimumEniQuantity(self): # Integer
		return self.get_query_params().get('MinimumEniQuantity')

	def set_MinimumEniQuantity(self, MinimumEniQuantity):  # Integer
		self.add_query_param('MinimumEniQuantity', MinimumEniQuantity)
	def get_MinimumMemorySize(self): # Float
		return self.get_query_params().get('MinimumMemorySize')

	def set_MinimumMemorySize(self, MinimumMemorySize):  # Float
		self.add_query_param('MinimumMemorySize', MinimumMemorySize)
	def get_InstanceFamilyLevel(self): # String
		return self.get_query_params().get('InstanceFamilyLevel')

	def set_InstanceFamilyLevel(self, InstanceFamilyLevel):  # String
		self.add_query_param('InstanceFamilyLevel', InstanceFamilyLevel)
	def get_ZoneIds(self): # RepeatList
		return self.get_query_params().get('ZoneId')

	def set_ZoneIds(self, ZoneId):  # RepeatList
		for depth1 in range(len(ZoneId)):
			self.add_query_param('ZoneId.' + str(depth1 + 1), ZoneId[depth1])
	def get_MemoryLists(self): # RepeatList
		return self.get_query_params().get('MemoryList')

	def set_MemoryLists(self, MemoryList):  # RepeatList
		for depth1 in range(len(MemoryList)):
			self.add_query_param('MemoryList.' + str(depth1 + 1), MemoryList[depth1])
	def get_Memory(self): # Float
		return self.get_query_params().get('Memory')

	def set_Memory(self, Memory):  # Float
		self.add_query_param('Memory', Memory)
	def get_MinimumEniIpv6AddressQuantity(self): # Integer
		return self.get_query_params().get('MinimumEniIpv6AddressQuantity')

	def set_MinimumEniIpv6AddressQuantity(self, MinimumEniIpv6AddressQuantity):  # Integer
		self.add_query_param('MinimumEniIpv6AddressQuantity', MinimumEniIpv6AddressQuantity)
	def get_CoresLists(self): # RepeatList
		return self.get_query_params().get('CoresList')

	def set_CoresLists(self, CoresList):  # RepeatList
		for depth1 in range(len(CoresList)):
			self.add_query_param('CoresList.' + str(depth1 + 1), CoresList[depth1])
	def get_Architectures(self): # RepeatList
		return self.get_query_params().get('Architecture')

	def set_Architectures(self, Architecture):  # RepeatList
		for depth1 in range(len(Architecture)):
			self.add_query_param('Architecture.' + str(depth1 + 1), Architecture[depth1])
	def get_MinimumInitialCredit(self): # Integer
		return self.get_query_params().get('MinimumInitialCredit')

	def set_MinimumInitialCredit(self, MinimumInitialCredit):  # Integer
		self.add_query_param('MinimumInitialCredit', MinimumInitialCredit)
	def get_ExcludedInstanceTypes(self): # RepeatList
		return self.get_query_params().get('ExcludedInstanceType')

	def set_ExcludedInstanceTypes(self, ExcludedInstanceType):  # RepeatList
		for depth1 in range(len(ExcludedInstanceType)):
			self.add_query_param('ExcludedInstanceType.' + str(depth1 + 1), ExcludedInstanceType[depth1])
	def get_MinimumEniPrivateIpAddressQuantity(self): # Integer
		return self.get_query_params().get('MinimumEniPrivateIpAddressQuantity')

	def set_MinimumEniPrivateIpAddressQuantity(self, MinimumEniPrivateIpAddressQuantity):  # Integer
		self.add_query_param('MinimumEniPrivateIpAddressQuantity', MinimumEniPrivateIpAddressQuantity)
	def get_GpuSpecss(self): # RepeatList
		return self.get_query_params().get('GpuSpecs')

	def set_GpuSpecss(self, GpuSpecs):  # RepeatList
		for depth1 in range(len(GpuSpecs)):
			self.add_query_param('GpuSpecs.' + str(depth1 + 1), GpuSpecs[depth1])
	def get_ChannelId(self): # Long
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # Long
		self.add_query_param('ChannelId', ChannelId)
