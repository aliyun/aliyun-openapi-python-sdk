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

class DescribePriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribePrice','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DataDisk3Size(self): # Integer
		return self.get_query_params().get('DataDisk.3.Size')

	def set_DataDisk3Size(self, DataDisk3Size):  # Integer
		self.add_query_param('DataDisk.3.Size', DataDisk3Size)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DataDisk3Category(self): # String
		return self.get_query_params().get('DataDisk.3.Category')

	def set_DataDisk3Category(self, DataDisk3Category):  # String
		self.add_query_param('DataDisk.3.Category', DataDisk3Category)
	def get_Isp(self): # String
		return self.get_query_params().get('Isp')

	def set_Isp(self, Isp):  # String
		self.add_query_param('Isp', Isp)
	def get_DataDisk4Size(self): # Integer
		return self.get_query_params().get('DataDisk.4.Size')

	def set_DataDisk4Size(self, DataDisk4Size):  # Integer
		self.add_query_param('DataDisk.4.Size', DataDisk4Size)
	def get_PriceUnit(self): # String
		return self.get_query_params().get('PriceUnit')

	def set_PriceUnit(self, PriceUnit):  # String
		self.add_query_param('PriceUnit', PriceUnit)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_DataDisk1PerformanceLevel(self): # String
		return self.get_query_params().get('DataDisk.1.PerformanceLevel')

	def set_DataDisk1PerformanceLevel(self, DataDisk1PerformanceLevel):  # String
		self.add_query_param('DataDisk.1.PerformanceLevel', DataDisk1PerformanceLevel)
	def get_AssuranceTimes(self): # String
		return self.get_query_params().get('AssuranceTimes')

	def set_AssuranceTimes(self, AssuranceTimes):  # String
		self.add_query_param('AssuranceTimes', AssuranceTimes)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_InstanceCpuCoreCount(self): # Integer
		return self.get_query_params().get('InstanceCpuCoreCount')

	def set_InstanceCpuCoreCount(self, InstanceCpuCoreCount):  # Integer
		self.add_query_param('InstanceCpuCoreCount', InstanceCpuCoreCount)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_InstanceNetworkType(self): # String
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self, InstanceNetworkType):  # String
		self.add_query_param('InstanceNetworkType', InstanceNetworkType)
	def get_InstanceAmount(self): # Integer
		return self.get_query_params().get('InstanceAmount')

	def set_InstanceAmount(self, InstanceAmount):  # Integer
		self.add_query_param('InstanceAmount', InstanceAmount)
	def get_InstanceTypeLists(self): # RepeatList
		return self.get_query_params().get('InstanceTypeList')

	def set_InstanceTypeLists(self, InstanceTypeList):  # RepeatList
		for depth1 in range(len(InstanceTypeList)):
			self.add_query_param('InstanceTypeList.' + str(depth1 + 1), InstanceTypeList[depth1])
	def get_DataDisk3PerformanceLevel(self): # String
		return self.get_query_params().get('DataDisk.3.PerformanceLevel')

	def set_DataDisk3PerformanceLevel(self, DataDisk3PerformanceLevel):  # String
		self.add_query_param('DataDisk.3.PerformanceLevel', DataDisk3PerformanceLevel)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_IoOptimized(self): # String
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self, IoOptimized):  # String
		self.add_query_param('IoOptimized', IoOptimized)
	def get_InternetMaxBandwidthOut(self): # Integer
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):  # Integer
		self.add_query_param('InternetMaxBandwidthOut', InternetMaxBandwidthOut)
	def get_SystemDiskCategory(self): # String
		return self.get_query_params().get('SystemDisk.Category')

	def set_SystemDiskCategory(self, SystemDiskCategory):  # String
		self.add_query_param('SystemDisk.Category', SystemDiskCategory)
	def get_Platform(self): # String
		return self.get_query_params().get('Platform')

	def set_Platform(self, Platform):  # String
		self.add_query_param('Platform', Platform)
	def get_Capacity(self): # Integer
		return self.get_query_params().get('Capacity')

	def set_Capacity(self, Capacity):  # Integer
		self.add_query_param('Capacity', Capacity)
	def get_SystemDiskPerformanceLevel(self): # String
		return self.get_query_params().get('SystemDisk.PerformanceLevel')

	def set_SystemDiskPerformanceLevel(self, SystemDiskPerformanceLevel):  # String
		self.add_query_param('SystemDisk.PerformanceLevel', SystemDiskPerformanceLevel)
	def get_DataDisk4Category(self): # String
		return self.get_query_params().get('DataDisk.4.Category')

	def set_DataDisk4Category(self, DataDisk4Category):  # String
		self.add_query_param('DataDisk.4.Category', DataDisk4Category)
	def get_DataDisk4PerformanceLevel(self): # String
		return self.get_query_params().get('DataDisk.4.PerformanceLevel')

	def set_DataDisk4PerformanceLevel(self, DataDisk4PerformanceLevel):  # String
		self.add_query_param('DataDisk.4.PerformanceLevel', DataDisk4PerformanceLevel)
	def get_Scope(self): # String
		return self.get_query_params().get('Scope')

	def set_Scope(self, Scope):  # String
		self.add_query_param('Scope', Scope)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_DedicatedHostType(self): # String
		return self.get_query_params().get('DedicatedHostType')

	def set_DedicatedHostType(self, DedicatedHostType):  # String
		self.add_query_param('DedicatedHostType', DedicatedHostType)
	def get_DataDisk2Category(self): # String
		return self.get_query_params().get('DataDisk.2.Category')

	def set_DataDisk2Category(self, DataDisk2Category):  # String
		self.add_query_param('DataDisk.2.Category', DataDisk2Category)
	def get_DataDisk1Size(self): # Integer
		return self.get_query_params().get('DataDisk.1.Size')

	def set_DataDisk1Size(self, DataDisk1Size):  # Integer
		self.add_query_param('DataDisk.1.Size', DataDisk1Size)
	def get_Amount(self): # Integer
		return self.get_query_params().get('Amount')

	def set_Amount(self, Amount):  # Integer
		self.add_query_param('Amount', Amount)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_DataDisk2Size(self): # Integer
		return self.get_query_params().get('DataDisk.2.Size')

	def set_DataDisk2Size(self, DataDisk2Size):  # Integer
		self.add_query_param('DataDisk.2.Size', DataDisk2Size)
	def get_SpotDuration(self): # Integer
		return self.get_query_params().get('SpotDuration')

	def set_SpotDuration(self, SpotDuration):  # Integer
		self.add_query_param('SpotDuration', SpotDuration)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_DataDisk1Category(self): # String
		return self.get_query_params().get('DataDisk.1.Category')

	def set_DataDisk1Category(self, DataDisk1Category):  # String
		self.add_query_param('DataDisk.1.Category', DataDisk1Category)
	def get_DataDisk2PerformanceLevel(self): # String
		return self.get_query_params().get('DataDisk.2.PerformanceLevel')

	def set_DataDisk2PerformanceLevel(self, DataDisk2PerformanceLevel):  # String
		self.add_query_param('DataDisk.2.PerformanceLevel', DataDisk2PerformanceLevel)
	def get_SystemDiskSize(self): # Integer
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self, SystemDiskSize):  # Integer
		self.add_query_param('SystemDisk.Size', SystemDiskSize)
	def get_OfferingType(self): # String
		return self.get_query_params().get('OfferingType')

	def set_OfferingType(self, OfferingType):  # String
		self.add_query_param('OfferingType', OfferingType)
