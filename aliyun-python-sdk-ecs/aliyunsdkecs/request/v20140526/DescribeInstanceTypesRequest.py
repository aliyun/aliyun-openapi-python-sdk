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
from aliyunsdkecs.endpoint import endpoint_data

class DescribeInstanceTypesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeInstanceTypes','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_GPUSpec(self): # String
		return self.get_query_params().get('GPUSpec')

	def set_GPUSpec(self, GPUSpec):  # String
		self.add_query_param('GPUSpec', GPUSpec)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_MaximumCpuCoreCount(self): # Integer
		return self.get_query_params().get('MaximumCpuCoreCount')

	def set_MaximumCpuCoreCount(self, MaximumCpuCoreCount):  # Integer
		self.add_query_param('MaximumCpuCoreCount', MaximumCpuCoreCount)
	def get_MaximumGPUAmount(self): # Integer
		return self.get_query_params().get('MaximumGPUAmount')

	def set_MaximumGPUAmount(self, MaximumGPUAmount):  # Integer
		self.add_query_param('MaximumGPUAmount', MaximumGPUAmount)
	def get_LocalStorageCategory(self): # String
		return self.get_query_params().get('LocalStorageCategory')

	def set_LocalStorageCategory(self, LocalStorageCategory):  # String
		self.add_query_param('LocalStorageCategory', LocalStorageCategory)
	def get_MaximumMemorySize(self): # Float
		return self.get_query_params().get('MaximumMemorySize')

	def set_MaximumMemorySize(self, MaximumMemorySize):  # Float
		self.add_query_param('MaximumMemorySize', MaximumMemorySize)
	def get_InstanceCategory(self): # String
		return self.get_query_params().get('InstanceCategory')

	def set_InstanceCategory(self, InstanceCategory):  # String
		self.add_query_param('InstanceCategory', InstanceCategory)
	def get_MinimumInstancePpsTx(self): # Long
		return self.get_query_params().get('MinimumInstancePpsTx')

	def set_MinimumInstancePpsTx(self, MinimumInstancePpsTx):  # Long
		self.add_query_param('MinimumInstancePpsTx', MinimumInstancePpsTx)
	def get_MinimumCpuCoreCount(self): # Integer
		return self.get_query_params().get('MinimumCpuCoreCount')

	def set_MinimumCpuCoreCount(self, MinimumCpuCoreCount):  # Integer
		self.add_query_param('MinimumCpuCoreCount', MinimumCpuCoreCount)
	def get_MinimumPrimaryEniQueueNumber(self): # Integer
		return self.get_query_params().get('MinimumPrimaryEniQueueNumber')

	def set_MinimumPrimaryEniQueueNumber(self, MinimumPrimaryEniQueueNumber):  # Integer
		self.add_query_param('MinimumPrimaryEniQueueNumber', MinimumPrimaryEniQueueNumber)
	def get_MinimumBaselineCredit(self): # Integer
		return self.get_query_params().get('MinimumBaselineCredit')

	def set_MinimumBaselineCredit(self, MinimumBaselineCredit):  # Integer
		self.add_query_param('MinimumBaselineCredit', MinimumBaselineCredit)
	def get_MinimumSecondaryEniQueueNumber(self): # Integer
		return self.get_query_params().get('MinimumSecondaryEniQueueNumber')

	def set_MinimumSecondaryEniQueueNumber(self, MinimumSecondaryEniQueueNumber):  # Integer
		self.add_query_param('MinimumSecondaryEniQueueNumber', MinimumSecondaryEniQueueNumber)
	def get_MinimumInstanceBandwidthTx(self): # Integer
		return self.get_query_params().get('MinimumInstanceBandwidthTx')

	def set_MinimumInstanceBandwidthTx(self, MinimumInstanceBandwidthTx):  # Integer
		self.add_query_param('MinimumInstanceBandwidthTx', MinimumInstanceBandwidthTx)
	def get_MinimumGPUAmount(self): # Integer
		return self.get_query_params().get('MinimumGPUAmount')

	def set_MinimumGPUAmount(self, MinimumGPUAmount):  # Integer
		self.add_query_param('MinimumGPUAmount', MinimumGPUAmount)
	def get_MaximumCpuSpeedFrequency(self): # Float
		return self.get_query_params().get('MaximumCpuSpeedFrequency')

	def set_MaximumCpuSpeedFrequency(self, MaximumCpuSpeedFrequency):  # Float
		self.add_query_param('MaximumCpuSpeedFrequency', MaximumCpuSpeedFrequency)
	def get_CpuArchitecture(self): # String
		return self.get_query_params().get('CpuArchitecture')

	def set_CpuArchitecture(self, CpuArchitecture):  # String
		self.add_query_param('CpuArchitecture', CpuArchitecture)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_MinimumMemorySize(self): # Float
		return self.get_query_params().get('MinimumMemorySize')

	def set_MinimumMemorySize(self, MinimumMemorySize):  # Float
		self.add_query_param('MinimumMemorySize', MinimumMemorySize)
	def get_MinimumEniQuantity(self): # Integer
		return self.get_query_params().get('MinimumEniQuantity')

	def set_MinimumEniQuantity(self, MinimumEniQuantity):  # Integer
		self.add_query_param('MinimumEniQuantity', MinimumEniQuantity)
	def get_InstanceFamilyLevel(self): # String
		return self.get_query_params().get('InstanceFamilyLevel')

	def set_InstanceFamilyLevel(self, InstanceFamilyLevel):  # String
		self.add_query_param('InstanceFamilyLevel', InstanceFamilyLevel)
	def get_MinimumQueuePairNumber(self): # Integer
		return self.get_query_params().get('MinimumQueuePairNumber')

	def set_MinimumQueuePairNumber(self, MinimumQueuePairNumber):  # Integer
		self.add_query_param('MinimumQueuePairNumber', MinimumQueuePairNumber)
	def get_MinimumLocalStorageAmount(self): # Integer
		return self.get_query_params().get('MinimumLocalStorageAmount')

	def set_MinimumLocalStorageAmount(self, MinimumLocalStorageAmount):  # Integer
		self.add_query_param('MinimumLocalStorageAmount', MinimumLocalStorageAmount)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
	def get_PhysicalProcessorModel(self): # String
		return self.get_query_params().get('PhysicalProcessorModel')

	def set_PhysicalProcessorModel(self, PhysicalProcessorModel):  # String
		self.add_query_param('PhysicalProcessorModel', PhysicalProcessorModel)
	def get_MaximumCpuTurboFrequency(self): # Float
		return self.get_query_params().get('MaximumCpuTurboFrequency')

	def set_MaximumCpuTurboFrequency(self, MaximumCpuTurboFrequency):  # Float
		self.add_query_param('MaximumCpuTurboFrequency', MaximumCpuTurboFrequency)
	def get_InstanceTypess(self): # RepeatList
		return self.get_query_params().get('InstanceTypes')

	def set_InstanceTypess(self, InstanceTypes):  # RepeatList
		for depth1 in range(len(InstanceTypes)):
			self.add_query_param('InstanceTypes.' + str(depth1 + 1), InstanceTypes[depth1])
	def get_MinimumInstancePpsRx(self): # Long
		return self.get_query_params().get('MinimumInstancePpsRx')

	def set_MinimumInstancePpsRx(self, MinimumInstancePpsRx):  # Long
		self.add_query_param('MinimumInstancePpsRx', MinimumInstancePpsRx)
	def get_MinimumEniIpv6AddressQuantity(self): # Integer
		return self.get_query_params().get('MinimumEniIpv6AddressQuantity')

	def set_MinimumEniIpv6AddressQuantity(self, MinimumEniIpv6AddressQuantity):  # Integer
		self.add_query_param('MinimumEniIpv6AddressQuantity', MinimumEniIpv6AddressQuantity)
	def get_MinimumEriQuantity(self): # Integer
		return self.get_query_params().get('MinimumEriQuantity')

	def set_MinimumEriQuantity(self, MinimumEriQuantity):  # Integer
		self.add_query_param('MinimumEriQuantity', MinimumEriQuantity)
	def get_MinimumDiskQuantity(self): # Integer
		return self.get_query_params().get('MinimumDiskQuantity')

	def set_MinimumDiskQuantity(self, MinimumDiskQuantity):  # Integer
		self.add_query_param('MinimumDiskQuantity', MinimumDiskQuantity)
	def get_MinimumCpuTurboFrequency(self): # Float
		return self.get_query_params().get('MinimumCpuTurboFrequency')

	def set_MinimumCpuTurboFrequency(self, MinimumCpuTurboFrequency):  # Float
		self.add_query_param('MinimumCpuTurboFrequency', MinimumCpuTurboFrequency)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_MinimumInstanceBandwidthRx(self): # Integer
		return self.get_query_params().get('MinimumInstanceBandwidthRx')

	def set_MinimumInstanceBandwidthRx(self, MinimumInstanceBandwidthRx):  # Integer
		self.add_query_param('MinimumInstanceBandwidthRx', MinimumInstanceBandwidthRx)
	def get_MinimumCpuSpeedFrequency(self): # Float
		return self.get_query_params().get('MinimumCpuSpeedFrequency')

	def set_MinimumCpuSpeedFrequency(self, MinimumCpuSpeedFrequency):  # Float
		self.add_query_param('MinimumCpuSpeedFrequency', MinimumCpuSpeedFrequency)
	def get_NvmeSupport(self): # String
		return self.get_query_params().get('NvmeSupport')

	def set_NvmeSupport(self, NvmeSupport):  # String
		self.add_query_param('NvmeSupport', NvmeSupport)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_MinimumInitialCredit(self): # Integer
		return self.get_query_params().get('MinimumInitialCredit')

	def set_MinimumInitialCredit(self, MinimumInitialCredit):  # Integer
		self.add_query_param('MinimumInitialCredit', MinimumInitialCredit)
	def get_InstanceTypeFamily(self): # String
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamily(self, InstanceTypeFamily):  # String
		self.add_query_param('InstanceTypeFamily', InstanceTypeFamily)
	def get_MinimumEniPrivateIpAddressQuantity(self): # Integer
		return self.get_query_params().get('MinimumEniPrivateIpAddressQuantity')

	def set_MinimumEniPrivateIpAddressQuantity(self, MinimumEniPrivateIpAddressQuantity):  # Integer
		self.add_query_param('MinimumEniPrivateIpAddressQuantity', MinimumEniPrivateIpAddressQuantity)
	def get_MinimumLocalStorageCapacity(self): # Long
		return self.get_query_params().get('MinimumLocalStorageCapacity')

	def set_MinimumLocalStorageCapacity(self, MinimumLocalStorageCapacity):  # Long
		self.add_query_param('MinimumLocalStorageCapacity', MinimumLocalStorageCapacity)
