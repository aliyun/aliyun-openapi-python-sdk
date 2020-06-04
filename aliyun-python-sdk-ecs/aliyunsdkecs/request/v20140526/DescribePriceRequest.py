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


	def get_DataDisk3Size(self):
		return self.get_query_params().get('DataDisk.3.Size')

	def set_DataDisk3Size(self,DataDisk3Size):
		self.add_query_param('DataDisk.3.Size',DataDisk3Size)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DataDisk3Category(self):
		return self.get_query_params().get('DataDisk.3.Category')

	def set_DataDisk3Category(self,DataDisk3Category):
		self.add_query_param('DataDisk.3.Category',DataDisk3Category)

	def get_DataDisk4Size(self):
		return self.get_query_params().get('DataDisk.4.Size')

	def set_DataDisk4Size(self,DataDisk4Size):
		self.add_query_param('DataDisk.4.Size',DataDisk4Size)

	def get_PriceUnit(self):
		return self.get_query_params().get('PriceUnit')

	def set_PriceUnit(self,PriceUnit):
		self.add_query_param('PriceUnit',PriceUnit)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_DataDisk1PerformanceLevel(self):
		return self.get_query_params().get('DataDisk.1.PerformanceLevel')

	def set_DataDisk1PerformanceLevel(self,DataDisk1PerformanceLevel):
		self.add_query_param('DataDisk.1.PerformanceLevel',DataDisk1PerformanceLevel)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_InstanceNetworkType(self):
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self,InstanceNetworkType):
		self.add_query_param('InstanceNetworkType',InstanceNetworkType)

	def get_InstanceAmount(self):
		return self.get_query_params().get('InstanceAmount')

	def set_InstanceAmount(self,InstanceAmount):
		self.add_query_param('InstanceAmount',InstanceAmount)

	def get_DataDisk3PerformanceLevel(self):
		return self.get_query_params().get('DataDisk.3.PerformanceLevel')

	def set_DataDisk3PerformanceLevel(self,DataDisk3PerformanceLevel):
		self.add_query_param('DataDisk.3.PerformanceLevel',DataDisk3PerformanceLevel)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_InternetMaxBandwidthOut(self):
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self,InternetMaxBandwidthOut):
		self.add_query_param('InternetMaxBandwidthOut',InternetMaxBandwidthOut)

	def get_SystemDiskCategory(self):
		return self.get_query_params().get('SystemDisk.Category')

	def set_SystemDiskCategory(self,SystemDiskCategory):
		self.add_query_param('SystemDisk.Category',SystemDiskCategory)

	def get_Platform(self):
		return self.get_query_params().get('Platform')

	def set_Platform(self,Platform):
		self.add_query_param('Platform',Platform)

	def get_Capacity(self):
		return self.get_query_params().get('Capacity')

	def set_Capacity(self,Capacity):
		self.add_query_param('Capacity',Capacity)

	def get_SystemDiskPerformanceLevel(self):
		return self.get_query_params().get('SystemDisk.PerformanceLevel')

	def set_SystemDiskPerformanceLevel(self,SystemDiskPerformanceLevel):
		self.add_query_param('SystemDisk.PerformanceLevel',SystemDiskPerformanceLevel)

	def get_DataDisk4Category(self):
		return self.get_query_params().get('DataDisk.4.Category')

	def set_DataDisk4Category(self,DataDisk4Category):
		self.add_query_param('DataDisk.4.Category',DataDisk4Category)

	def get_DataDisk4PerformanceLevel(self):
		return self.get_query_params().get('DataDisk.4.PerformanceLevel')

	def set_DataDisk4PerformanceLevel(self,DataDisk4PerformanceLevel):
		self.add_query_param('DataDisk.4.PerformanceLevel',DataDisk4PerformanceLevel)

	def get_Scope(self):
		return self.get_query_params().get('Scope')

	def set_Scope(self,Scope):
		self.add_query_param('Scope',Scope)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_DataDisk2Category(self):
		return self.get_query_params().get('DataDisk.2.Category')

	def set_DataDisk2Category(self,DataDisk2Category):
		self.add_query_param('DataDisk.2.Category',DataDisk2Category)

	def get_DataDisk1Size(self):
		return self.get_query_params().get('DataDisk.1.Size')

	def set_DataDisk1Size(self,DataDisk1Size):
		self.add_query_param('DataDisk.1.Size',DataDisk1Size)

	def get_Amount(self):
		return self.get_query_params().get('Amount')

	def set_Amount(self,Amount):
		self.add_query_param('Amount',Amount)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_DataDisk2Size(self):
		return self.get_query_params().get('DataDisk.2.Size')

	def set_DataDisk2Size(self,DataDisk2Size):
		self.add_query_param('DataDisk.2.Size',DataDisk2Size)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_DataDisk1Category(self):
		return self.get_query_params().get('DataDisk.1.Category')

	def set_DataDisk1Category(self,DataDisk1Category):
		self.add_query_param('DataDisk.1.Category',DataDisk1Category)

	def get_DataDisk2PerformanceLevel(self):
		return self.get_query_params().get('DataDisk.2.PerformanceLevel')

	def set_DataDisk2PerformanceLevel(self,DataDisk2PerformanceLevel):
		self.add_query_param('DataDisk.2.PerformanceLevel',DataDisk2PerformanceLevel)

	def get_SystemDiskSize(self):
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self,SystemDiskSize):
		self.add_query_param('SystemDisk.Size',SystemDiskSize)

	def get_OfferingType(self):
		return self.get_query_params().get('OfferingType')

	def set_OfferingType(self,OfferingType):
		self.add_query_param('OfferingType',OfferingType)